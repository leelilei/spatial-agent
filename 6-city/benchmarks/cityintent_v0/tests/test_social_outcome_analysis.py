from __future__ import annotations

import sys
import unittest
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

from analyze_social_outcomes import classify_trace, summarize_agents  # noqa: E402


class SocialOutcomeAnalysisTest(unittest.TestCase):
    def test_classifies_message_without_environment_accepted_meeting(self) -> None:
        scenario = {
            "scenario_id": "social",
            "primary_agent": "aria",
            "success_conditions": [
                {
                    "id": "meet",
                    "type": "co_presence",
                    "role": "outcome",
                    "agents": ["aria", "ben"],
                    "location_any_of": ["cafe"],
                }
            ],
        }
        item = {
            "scenario_id": "social",
            "agent_type": "agent",
            "conditions": [{"id": "meet", "score": 0.0}],
            "messages": [{"to": "ben", "content": "meet me"}],
            "entries": [{"location": "cafe", "kind": "enter", "time": 10}],
            "interactions": [],
            "trace": [],
            "metrics": {"task_completion": 0.0, "trace_feasibility": 1.0},
            "plausibility_judgment": {"face_plausibility": 0.9},
        }

        row = classify_trace(item, scenario, repeat_id=1)

        self.assertEqual(row["accepted_copresence_outcomes"], 0)
        self.assertEqual(row["message_without_social_success"], 1.0)
        self.assertEqual(row["target_entry_without_social_success"], 1.0)
        self.assertEqual(row["legal_but_ineffective"], 1.0)
        self.assertEqual(row["plausible_but_unverified"], 1.0)

    def test_social_pass_k_requires_every_repeat_to_accept_every_outcome(self) -> None:
        rows = [
            {
                "agent_type": "agent",
                "scenario_id": "s1",
                "required_copresence_outcomes": 1,
                "accepted_copresence_outcomes": accepted,
                "full_social_success": accepted,
                "task_completion": accepted,
                "trace_feasibility": 1.0,
                "joint_success": accepted,
                "legal_but_ineffective": 1.0 - accepted,
                "plausible_but_unverified": 1.0 - accepted,
                "message_without_social_success": 0.0,
                "attempt_without_social_success": 0.0,
                "target_entry_without_social_success": 0.0,
                "judge_face_plausibility": 0.9,
                "llm_calls": 1.0,
                "llm_total_tokens": 10.0,
            }
            for accepted in (1.0, 1.0, 0.0)
        ]

        summary = summarize_agents(rows)[0]

        self.assertEqual(summary["copresence_outcome_rate"], 2 / 3)
        self.assertEqual(summary["social_pass_k_rate"], 0.0)


if __name__ == "__main__":
    unittest.main()
