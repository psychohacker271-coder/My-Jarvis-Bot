import unittest

from nexora_agents import AGENTS, tool_schemas, _calculator


class AgentRuntimeTests(unittest.TestCase):
    def test_all_six_agents_are_registered(self):
        self.assertEqual(
            set(AGENTS),
            {"nexora", "kai", "ryan", "maya", "angel", "riya"},
        )

    def test_central_agent_can_consult_specialists(self):
        names = {item["function"]["name"] for item in tool_schemas("nexora")}
        self.assertIn("consult_agent", names)
        self.assertIn("calculator", names)

    def test_companions_have_role_appropriate_tool_access(self):
        self.assertNotIn(
            "consult_agent",
            {item["function"]["name"] for item in tool_schemas("maya")},
        )
        self.assertIn(
            "get_local_model_status",
            {item["function"]["name"] for item in tool_schemas("ryan")},
        )

    def test_safe_calculator(self):
        self.assertEqual(_calculator("(12 + 8) * 3"), "60")
        self.assertEqual(_calculator("2 ** 5"), "32")

    def test_calculator_rejects_code(self):
        with self.assertRaises((ValueError, SyntaxError)):
            _calculator("__import__('os').system('echo unsafe')")


if __name__ == "__main__":
    unittest.main()
