from __future__ import annotations

import sys
import unittest
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

from analyze_perturbation_pairs import pair_rows, summarize  # noqa: E402
from validate_cityintent_v0 import paired_common_payload, payload_sha256  # noqa: E402


class PerturbationPairTest(unittest.TestCase):
    def test_pair_rows_computes_treatment_delta_and_conditional_recovery(self) -> None:
        scenario_pairs = {
            "control": {"pair_id": "p1", "variant": "control"},
            "treatment": {"pair_id": "p1", "variant": "treatment"},
        }
        rows = [
            {
                "repeat_id": "1",
                "scenario_id": "control",
                "agent_type": "agent",
                "task_completion": "1",
                "trace_feasibility": "1",
            },
            {
                "repeat_id": "1",
                "scenario_id": "treatment",
                "agent_type": "agent",
                "task_completion": "0",
                "trace_feasibility": "0.5",
            },
        ]

        pairs = pair_rows(rows, scenario_pairs)
        summary = summarize(pairs, "agent_type")[0]

        self.assertEqual(pairs[0]["delta_task_completion"], -1.0)
        self.assertEqual(pairs[0]["delta_trace_feasibility"], -0.5)
        self.assertEqual(summary["conditional_task_recovery_rate"], 0.0)
        self.assertEqual(summary["conditional_joint_recovery_rate"], 0.0)

    def test_common_payload_ignores_only_pair_assignment_and_events(self) -> None:
        base = {
            "scenario_id": "a",
            "title": "same",
            "events": [],
            "perturbation_pair": {"pair_id": "p", "variant": "control"},
            "success_conditions": [{"id": "goal"}],
        }
        treatment = {
            **base,
            "scenario_id": "b",
            "events": [{"type": "event"}],
            "perturbation_pair": {"pair_id": "p", "variant": "treatment"},
        }

        self.assertEqual(
            payload_sha256(paired_common_payload(base)),
            payload_sha256(paired_common_payload(treatment)),
        )


if __name__ == "__main__":
    unittest.main()
