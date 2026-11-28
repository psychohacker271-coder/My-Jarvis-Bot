"""Lightweight, local-first multi-agent runtime for NEXORA.

No hosted orchestration service, paid API, or framework subscription is required.
The Ollama model runs on the user's own computer.
"""
from __future__ import annotations

import ast
import datetime as dt
import json
import operator
from typing import Any

import httpx

AGENTS: dict[str, dict[str, str]] = {
    "nexora": {"name": "NEXORA", "role": "Central coordinator", "focus": "general assistance, routing, planning and coordinating specialists"},
    "kai": {"name": "KAI", "role": "Friendly companion agent", "focus": "casual conversation, gaming, encouragement and practical everyday advice"},
    "ryan": {"name": "RYAN", "role": "Technology and coding agent", "focus": "programming explanations, debugging, software design and technical research"},
    "maya": {"name": "MAYA", "role": "Study mentor agent", "focus": "school subjects, step-by-step teaching, revision and practice questions"},
    "angel": {"name": "ANGEL", "role": "Classmate companion agent", "focus": "friendly conversation, hobbies, school life and creative brainstorming"},
    "riya": {"name": "RIYA", "role": "Supportive companion agent", "focus": "empathetic listening, healthy routines, encouragement and reflection"},
}

AGENT_GUIDANCE = {
    "nexora": "You are the lead coordinator. For specialist work, use consult_agent to ask the relevant companion for a focused contribution, then synthesize the result. Do not claim a tool ran unless it did.",
    "kai": "Stay in the friendly companion role. Offer concrete ideas when useful; do not pretend to access device features.",
    "ryan": "Act as a technical problem-solving agent. Explain assumptions, give testable steps, and distinguish proposed code from code that was actually run.",
    "maya": "Teach patiently with clear steps, examples and short checks for understanding. Match the learner's level.",
    "angel": "Be a friendly classmate and creative brainstorming partner. Keep conversation age-appropriate and non-romantic.",
    "riya": "Be a supportive companion. Encourage balanced routines and real-world support; never guilt-trip or foster dependence.",
}

def _calculator(expression: str) -> str:
    """Evaluate a small arithmetic expression without eval or code execution."""
    if not isinstance(expression, str) or not expression.strip() or len(expression) > 120:
        raise ValueError("Enter a short arithmetic expression.")
    tree = ast.parse(expression, mode="eval")
    binary = {
        ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod, ast.Pow: operator.pow,
    }
    unary = {ast.UAdd: operator.pos, ast.USub: operator.neg}

    def visit(node: ast.AST) -> float | int:
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            if abs(node.value) > 10**12:
                raise ValueError("Number is too large.")
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in binary:
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 12:
                raise ValueError("Exponent is too large.")
            result = binary[type(node.op)](left, right)
            if abs(result) > 10**15:
                raise ValueError("Result is too large.")
            return result
        if isinstance(node, ast.UnaryOp) and type(node.op) in unary:
            return unary[type(node.op)](visit(node.operand))
        raise ValueError("Only basic arithmetic is allowed.")

    result = visit(tree)
    return str(result)

def tool_schemas(agent_id: str) -> list[dict[str, Any]]:
    tools: list[dict[str, Any]] = [
        {"type": "function", "function": {
            "name": "get_current_time",
            "description": "Get the current local date and time on the computer running NEXORA.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        }},
        {"type": "function", "function": {
            "name": "calculator",
            "description": "Calculate a basic arithmetic expression safely.",
            "parameters": {"type": "object", "properties": {"expression": {"type": "string"}}, "required": ["expression"]},
        }},
        {"type": "function", "function": {
            "name": "list_agents",
            "description": "List NEXORA's available specialist agents and their responsibilities.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        }},
    ]
    if agent_id in ("nexora", "ryan"):
        tools.append({"type": "function", "function": {
            "name": "get_local_model_status",
            "description": "Check which local Ollama models are installed on the NEXORA computer.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        }})
    if agent_id == "nexora":
        tools.append({"type": "function", "function": {
            "name": "consult_agent",
            "description": "Ask one specialist agent for a focused contribution. Use for tasks that benefit from a second specialist perspective.",
            "parameters": {
                "type": "object",
                "properties": {
                    "agent_id": {"type": "string", "enum": ["kai", "ryan", "maya", "angel", "riya"]},
                    "task": {"type": "string", "description": "A focused question or subtask for the specialist."},
                },
                "required": ["agent_id", "task"],
            },
        }})
    return tools

async def _model_reply(client: httpx.AsyncClient, ollama_url: str, model: str, system: str, task: str) -> str:
    response = await client.post(
        f"{ollama_url}/api/chat",
        json={"model": model, "stream": False, "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": task[:4000]},
        ], "options": {"temperature": 0.55}},
    )
    response.raise_for_status()
    return str((response.json().get("message") or {}).get("content", "")).strip()[:5000]

async def execute_tool(
    name: str, arguments: dict[str, Any], *, agent_id: str,
    client: httpx.AsyncClient, ollama_url: str, model: str,
    max_delegations: int = 2,
) -> str:
    if name == "get_current_time":
        return dt.datetime.now().astimezone().isoformat(timespec="seconds")
    if name == "calculator":
        return _calculator(str(arguments.get("expression", "")))
    if name == "list_agents":
        return json.dumps(AGENTS, ensure_ascii=False)
    if name == "get_local_model_status":
        response = await client.get(f"{ollama_url}/api/tags")
        response.raise_for_status()
        models = [m.get("name", "") for m in response.json().get("models", [])]
        return json.dumps({"configured_model": model, "configured_model_installed": model in models, "installed_models": models}, ensure_ascii=False)
    if name == "consult_agent" and agent_id == "nexora":
        specialist = str(arguments.get("agent_id", "")).lower()
        task = str(arguments.get("task", "")).strip()
        if specialist not in ("kai", "ryan", "maya", "angel", "riya") or not task:
            raise ValueError("Choose a valid specialist and provide a task.")
        if len(task) > 2000:
            raise ValueError("Specialist task is too long.")
        profile = AGENTS[specialist]
        system = (
            f"You are {profile['name']}, a specialist AI agent in NEXORA. "
            f"Your role: {profile['role']}. Your focus: {profile['focus']}. "
            f"{AGENT_GUIDANCE[specialist]} "
            "Give a concise, useful specialist contribution to the central coordinator. "
            "You are an AI, not a human. Never claim external actions were completed."
        )
        answer = await _model_reply(client, ollama_url, model, system, task)
        return json.dumps({"agent": profile["name"], "contribution": answer}, ensure_ascii=False)
    raise ValueError(f"Tool '{name}' is not available to agent '{agent_id}'.")
