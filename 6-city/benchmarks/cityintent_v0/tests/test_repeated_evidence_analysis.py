from __future__ import annotations

import sys
import unittest
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

from analyze_repeated_evidence import (  # noqa: E402
    analyze_agents,
    analyze_correlations,
    average_ranks,
)
from compare_agent_models import compare_rows  # noqa: E402
from compare_plausibility_judges import binary_kappa, compare  # noqa: E402


class RepeatedEvidenceAnalysisTest(unittest.TestCase):
    def test_agent_model_comparison_requires_and_summarizes_matched_cells(self) -> None:
        baseline = [
            {
                "scenario_id": "s1",
                "agent_type": "a",
                "task_completion": "0.5",
                "trace_feasibility": "1",
            }
        ]
        candidate = [
            {
                "scenario_id": "s1",
                "agent_type": "a",
                "task_completion": "1",
                "trace_feasibility": "0.5",
            }
        ]

        pairs, summary = compare_rows(baseline, candidate)

        self.assertEqual(len(pairs), 1)
        self.assertEqual(summary[0]["delta_task_completion"], 0.5)
        self.assertEqual(summary[0]["delta_trace_feasibility"], -0.5)
        self.assertEqual(summary[0]["candidate_full_task_rate"], 1.0)

    def test_average_ranks_handles_ties(self) -> None:
        self.assertEqual(average_ranks([10, 20, 20, 30]), [1.0, 2.5, 2.5, 4.0])

    def test_agent_rates_and_pass_k(self) -> None:
        rows = [
            {
                "repeat_id": "1",
                "scenario_id": "s1",
                "agent_type": "a",
                "task_completion": "1",
                "trace_feasibility": "1",
                "judge_face_plausibility": "0.9",
                "judge_trace_believability": "0.8",
                "face_believability_gap": "0.1",
                "llm_calls": "1",
                "llm_total_tokens": "10",
            },
            {
                "repeat_id": "2",
                "scenario_id": "s1",
                "agent_type": "a",
                "task_completion": "0",
                "trace_feasibility": "0.5",
                "judge_face_plausibility": "0.8",
                "judge_trace_believability": "0.2",
                "face_believability_gap": "0.6",
                "llm_calls": "2",
                "llm_total_tokens": "20",
            },
            {
                "repeat_id": "1",
                "scenario_id": "s2",
                "agent_type": "a",
                "task_completion": "1",
                "trace_feasibility": "1",
                "judge_face_plausibility": "0.6",
                "judge_trace_believability": "0.7",
                "face_believability_gap": "0",
                "llm_calls": "1",
                "llm_total_tokens": "10",
            },
            {
                "repeat_id": "2",
                "scenario_id": "s2",
                "agent_type": "a",
                "task_completion": "1",
                "trace_feasibility": "1",
                "judge_face_plausibility": "0.6",
                "judge_trace_believability": "0.7",
                "face_believability_gap": "0",
                "llm_calls": "1",
                "llm_total_tokens": "10",
            },
        ]

        result = analyze_agents(rows, face_threshold=0.7)[0]

        self.assertEqual(result["full_task_success_rate"], 0.75)
        self.assertEqual(result["plausible_task_failure_rate"], 0.25)
        self.assertEqual(result["pass_k_task_rate"], 0.5)
        self.assertEqual(result["pass_k_feasible_rate"], 0.5)

    def test_correlations_are_reported_for_all_rows(self) -> None:
        rows = [
            {
                "repeat_id": str(index),
                "scenario_id": "s1",
                "agent_type": "a",
                "judge_face_plausibility": str(value),
                "judge_trace_believability": str(value),
                "task_completion": str(value),
                "trace_feasibility": str(value),
            }
            for index, value in enumerate((0.1, 0.5, 0.9), start=1)
        ]

        result = analyze_correlations(rows)
        overall = {
            row["comparison"]: row for row in result if row["group"] == "all"
        }

        self.assertEqual(overall["face_vs_task"]["pearson_r"], 1.0)
        self.assertEqual(overall["face_vs_task"]["spearman_rho"], 1.0)

    def test_judge_comparison_matches_identical_trace_keys(self) -> None:
        def item(face: float, trace: float) -> dict:
            return {
                "plausibility_judgment": {
                    "face_plausibility": face,
                    "trace_believability": trace,
                    "rationale_alignment": face,
                    "urban_common_sense": trace,
                }
            }

        baseline = {(1, "s1", "a1"): item(0.8, 0.6), (1, "s2", "a1"): item(0.4, 0.2)}
        candidate = {(1, "s1", "a1"): item(0.9, 0.7), (1, "s2", "a1"): item(0.3, 0.1)}

        pairs, summary, agents = compare(
            baseline, candidate, "baseline", "candidate", threshold=0.7
        )

        self.assertEqual(len(pairs), 2)
        self.assertEqual(len(summary), 4)
        self.assertEqual(len(agents), 2)
        self.assertEqual(summary[0]["threshold_agreement"], 1.0)
        self.assertEqual(binary_kappa([True, False], [True, False]), 1.0)


if __name__ == "__main__":
    unittest.main()
