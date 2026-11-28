# NEXORA Local Multi-Agent Runtime

NEXORA uses a small local Python agent runtime rather than a hosted orchestration subscription. It is designed for the user's Windows laptop and Ollama installation.

## Agents
- NEXORA: central coordinator; can consult a specialist and combine the answer.
- KAI: friendly everyday and gaming companion.
- RYAN: technology, coding and troubleshooting specialist.
- MAYA: study mentor for school subjects and practice.
- ANGEL: friendly classmate and creative brainstorming partner.
- RIYA: supportive companion for reflection and healthy routines.

Each agent gets a role-specific system prompt and only the tools appropriate to that role. They share the same locally installed Ollama model; they are separate agent roles, not six separately trained models.

## Current local tools
- Safe arithmetic calculator (AST allowlist; no eval or shell execution).
- Local computer date/time.
- Agent roster.
- Local Ollama model status for NEXORA and RYAN.
- Specialist consultation from NEXORA to KAI, RYAN, MAYA, ANGEL or RIYA.

NEXORA can consult up to two specialists per turn. Specialist calls are bounded and do not recursively call other agents. Tool execution stays on the laptop.

## Free-use design
- No paid model API, hosted agent subscription, or per-message provider billing is used by this runtime.
- Ollama runs the selected model locally, so ordinary local inference has no provider message quota.
- Practical limits remain: computer uptime, RAM/CPU/GPU, model size, disk space, electricity, and network access for optional online services.
- Hatchable's free hosting has its own daily bandwidth quota. Local inference avoids routing each prompt through a paid hosted model, but the PWA still needs its hosting/CDN for page and model downloads.
- For phone use, the laptop must remain on and a trusted HTTPS tunnel must be configured. Never expose the local brain port directly to the public internet.

## Model compatibility
Ollama supports tool calling and agent loops for compatible models. NEXORA sends tool schemas to Ollama. If the selected model rejects tool schemas, the bridge falls back to ordinary chat so existing models remain usable; specialist delegation and tool execution then will not be available until a compatible model is selected.

Official references:
- https://github.com/ollama/ollama/blob/main/docs/capabilities/tool-calling.mdx
- https://github.com/langchain-ai/langgraph
- https://github.com/crewAIInc/crewAI

LangGraph and CrewAI were reviewed as open-source orchestration options. The current runtime intentionally uses a smaller custom loop to avoid adding large dependencies to an 8 GB laptop.

## Tests
Run:
```powershell
py -m unittest discover -s tests -v
py -m compileall -q nexora_local_brain.py nexora_agents.py
```
GitHub Actions runs the same checks for commits to `nexora-project-docs`.
