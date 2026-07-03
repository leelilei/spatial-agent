from __future__ import annotations

import csv
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

from build_human_audit import (  # noqa: E402
    ANNOTATION_FIELDS,
    accepted_dwell_minutes,
    balanced_sample,
    blind_item,
    trace_role_score,
)
from check_v1_release import (  # noqa: E402
    DEFAULT_AUDIT_DIR,
    DEFAULT_RESULT_DIR,
    evaluate_release_gate,
)
from prepare_human_audit_handoff import build_handoffs  # noqa: E402
from score_human_audit import cohen_kappa, score_annotations  # noqa: E402
from run_annotation_dry_run import normalize_label  # noqa: E402


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
                rows = [
                    {**row, "annotator_id": f"annotator_{suffix}"}
                    for row in annotation_rows
                ]
                with path.open("w", encoding="utf-8", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=ANNOTATION_FIELDS)
                    writer.writeheader()
                    writer.writerows(rows)
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

    def test_audit_calibration_prefers_task_completion_over_legacy_goal_sum(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            annotation = {
                "audit_id": "H001",
                "annotator_id": "annotator",
                "completion_label": "not_complete",
                "feasibility_label": "feasible",
                "replan_label": "not_applicable",
                "evidence_sufficient": "yes",
                "first_invalid_step": "",
                "confidence": "5",
                "notes": "",
            }
            annotation_paths = []
            for suffix in ("a", "b"):
                path = root / f"{suffix}.csv"
                row = {**annotation, "annotator_id": f"annotator_{suffix}"}
                with path.open("w", encoding="utf-8", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=ANNOTATION_FIELDS)
                    writer.writeheader()
                    writer.writerow(row)
                annotation_paths.append(path)
            key_path = root / "key.csv"
            with key_path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=[
                        "audit_id",
                        "goal_completion",
                        "task_completion",
                        "trace_feasibility",
                        "replanning_success",
                    ],
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "audit_id": "H001",
                        "goal_completion": "0.7",
                        "task_completion": "0.0",
                        "trace_feasibility": "1.0",
                        "replanning_success": "",
                    }
                )

            result = score_annotations(
                annotation_paths[0], annotation_paths[1], key_path
            )

        self.assertEqual(
            result["verifier_calibration"]["annotator_a"]["completion_label"][
                "exact_agreement"
            ],
            1.0,
        )

    def test_material_findings_expose_human_and_verifier_disagreement(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            common = {
                "audit_id": "H001",
                "feasibility_label": "feasible",
                "replan_label": "not_applicable",
                "evidence_sufficient": "yes",
                "first_invalid_step": "",
                "confidence": "5",
                "notes": "",
            }
            rows = [
                {**common, "annotator_id": "person_a", "completion_label": "complete"},
                {
                    **common,
                    "annotator_id": "person_b",
                    "completion_label": "not_complete",
                },
            ]
            annotation_paths = []
            for suffix, row in zip(("a", "b"), rows):
                path = root / f"{suffix}.csv"
                with path.open("w", encoding="utf-8", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=ANNOTATION_FIELDS)
                    writer.writeheader()
                    writer.writerow(row)
                annotation_paths.append(path)
            key_path = root / "key.csv"
            with key_path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=[
                        "audit_id",
                        "goal_completion",
                        "task_completion",
                        "trace_feasibility",
                        "replanning_success",
                    ],
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "audit_id": "H001",
                        "goal_completion": "1.0",
                        "task_completion": "1.0",
                        "trace_feasibility": "1.0",
                        "replanning_success": "",
                    }
                )

            result = score_annotations(
                annotation_paths[0], annotation_paths[1], key_path
            )

        kinds = {finding["kind"] for finding in result["material_findings"]}
        self.assertIn("inter_annotator_disagreement", kinds)
        self.assertIn("human_verifier_disagreement", kinds)

    def test_legacy_trace_role_score_uses_scenario_roles(self) -> None:
        scenario = {
            "success_conditions": [
                {"id": "task", "role": "outcome"},
                {"id": "budget", "role": "constraint"},
            ]
        }
        trace = {
            "metrics": {"goal_completion": 0.5},
            "conditions": [
                {"id": "task", "score": 0, "weight": 0.5},
                {"id": "budget", "score": 1, "weight": 0.5},
            ],
        }
        self.assertEqual(trace_role_score(trace, scenario, "outcome"), 0)
        self.assertEqual(trace_role_score(trace, scenario, "constraint"), 1)

    def test_model_dry_run_normalization_cannot_inject_invalid_labels(self) -> None:
        row = normalize_label(
            "H001",
            "model_a",
            {
                "completion_label": "maybe",
                "feasibility_label": "feasible",
                "replan_label": "successful",
                "evidence_sufficient": "yes",
                "first_invalid_step": "not-a-step",
                "confidence": 9,
                "notes": "test",
            },
        )
        self.assertEqual(row["completion_label"], "uncertain")
        self.assertEqual(row["first_invalid_step"], "")
        self.assertEqual(row["confidence"], 5)

    def test_accepted_dwell_excludes_rejected_steps(self) -> None:
        trace = {
            "trace": [
                {
                    "start_location": "library",
                    "action": {"kind": "dwell", "minutes": 10},
                    "violations": [],
                },
                {
                    "start_location": "cafe",
                    "action": {"kind": "dwell", "minutes": 20},
                    "violations": [{"kind": "unpaid_service_required"}],
                },
            ]
        }
        self.assertEqual(accepted_dwell_minutes(trace), {"library": 10})

    def test_v1_release_gate_rejects_blank_human_annotations(self) -> None:
        report = evaluate_release_gate(
            DEFAULT_AUDIT_DIR,
            DEFAULT_RESULT_DIR,
            run_runtime_checks=False,
        )

        self.assertEqual(report["status"], "pending_human_audit")
        self.assertIn(
            "two-person human audit incomplete: {'annotator_a': 16, 'annotator_b': 16}",
            report["blockers"],
        )

    def test_handoff_archives_exclude_sealed_and_other_annotator(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp)
            manifest = build_handoffs(DEFAULT_AUDIT_DIR, output_dir)
            self.assertFalse(manifest["sealed_material_included"])
            for archive_info in manifest["archives"]:
                archive = output_dir / archive_info["archive"]
                with zipfile.ZipFile(archive) as zf:
                    members = zf.namelist()
                self.assertFalse(any(name.startswith("sealed/") for name in members))
                own = f"annotations/{archive_info['annotator']}.csv"
                self.assertIn(own, members)
                other = (
                    "annotations/annotator_b.csv"
                    if archive_info["annotator"] == "annotator_a"
                    else "annotations/annotator_a.csv"
                )
                self.assertNotIn(other, members)


if __name__ == "__main__":
    unittest.main()
