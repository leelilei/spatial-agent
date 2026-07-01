from __future__ import annotations

import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

from build_human_audit import (  # noqa: E402
    ANNOTATION_FIELDS,
    balanced_sample,
    blind_item,
)
from score_human_audit import cohen_kappa, score_annotations  # noqa: E402


class HumanAuditToolsTest(unittest.TestCase):
    def test_balanced_sample_selects_each_scenario_agent_cell(self) -> None:
        rows = []
        for scenario in ("s1", "s2"):
            for agent in ("a1", "a2"):
                for repeat in range(1, 4):
                    rows.append(
                        {
                            "repeat_id": repeat,
                            "trace": {
                                "scenario_id": scenario,
                                "agent_type": agent,
                            },
                        }
                    )

        sample = balanced_sample(rows, sample_per_cell=1, seed=17)

        self.assertEqual(len(sample), 4)
        self.assertEqual(
            {
                (row["trace"]["scenario_id"], row["trace"]["agent_type"])
                for row in sample
            },
            {("s1", "a1"), ("s1", "a2"), ("s2", "a1"), ("s2", "a2")},
        )

    def test_blind_item_excludes_framework_and_verifier_labels(self) -> None:
        scenario = {
            "scenario_id": "s1",
            "title": "Test",
            "family": "test",
            "episode": {"start_time": "10:00", "end_time": "11:00"},
            "public_context": "",
            "events": [],
            "success_conditions": [],
            "primary_agent": "aria",
            "agents": [
                {
                    "agent_id": "aria",
                    "persona": "Tester",
                    "private_intention": "Reach the shop.",
                    "start_location": "home",
                    "budget": 10,
                }
            ],
        }
        trace = {
            "scenario_id": "s1",
            "agent_type": "gatsim_official_planner",
            "metrics": {"goal_completion": 1.0},
            "violations": [{"kind": "hidden"}],
            "replans": [{"hidden": True}],
            "trace": [
                {
                    "step": 1,
                    "start_time": "10:00",
                    "start_location": "home",
                    "action": {"kind": "move", "target": "shop"},
                    "end_time": "10:05",
                    "end_location": "shop",
                    "budget": 10,
                    "route_interruptions": [],
                }
            ],
            "final_state": {"time": "10:05", "location": "shop", "budget": 10},
        }

        blinded = blind_item("H001", {"trace": trace}, scenario)
        serialized = json.dumps(blinded, sort_keys=True)

        self.assertNotIn("gatsim_official_planner", serialized)
        self.assertNotIn('"metrics"', serialized)
        self.assertNotIn('"violations"', serialized)
        self.assertNotIn('"replans"', serialized)

    def test_agreement_and_calibration_from_complete_annotations(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            annotation_rows = [
                {
                    "audit_id": "H001",
                    "annotator_id": "annotator",
                    "completion_label": "complete",
                    "feasibility_label": "feasible",
                    "replan_label": "successful",
                    "evidence_sufficient": "yes",
                    "first_invalid_step": "",
                    "confidence": "5",
                    "notes": "",
                },
                {
                    "audit_id": "H002",
                    "annotator_id": "annotator",
                    "completion_label": "partial",
                    "feasibility_label": "infeasible",
                    "replan_label": "not_applicable",
                    "evidence_sufficient": "yes",
                    "first_invalid_step": "2",
                    "confidence": "4",
                    "notes": "",
                },
            ]
            key_rows = [
                {
                    "audit_id": "H001",
                    "goal_completion": "1.0",
                    "trace_feasibility": "1.0",
                    "replanning_success": "1.0",
                },
                {
                    "audit_id": "H002",
                    "goal_completion": "0.5",
                    "trace_feasibility": "0.5",
                    "replanning_success": "",
                },
            ]
            annotation_paths = []
            for suffix in ("a", "b"):
                path = root / f"{suffix}.csv"
                with path.open("w", encoding="utf-8", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=ANNOTATION_FIELDS)
                    writer.writeheader()
                    writer.writerows(annotation_rows)
                annotation_paths.append(path)
            key_path = root / "key.csv"
            with key_path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=list(key_rows[0]))
                writer.writeheader()
                writer.writerows(key_rows)

            result = score_annotations(
                annotation_paths[0], annotation_paths[1], key_path
            )

        self.assertEqual(
            result["inter_annotator_agreement"]["completion_label"]["cohen_kappa"],
            1.0,
        )
        self.assertEqual(
            result["verifier_calibration"]["annotator_a"]["completion_label"]["exact_agreement"],
            1.0,
        )

    def test_cohen_kappa_handles_empty_input(self) -> None:
        self.assertIsNone(cohen_kappa([], []))


if __name__ == "__main__":
    unittest.main()
