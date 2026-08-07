"""Analyze the E3e Claude/Qwen hard-tier backbone extension.

The test convention intentionally matches E3d: two-sided permutation tests
and nonparametric bootstrap confidence intervals over the 18 judged traces in
each model-policy cell. Holm-adjusted p-values are added across the focused
E3e comparisons to make the expanded model sweep easier to interpret.
"""

from __future__ import annotations

import csv
import statistics
from pathlib import Path
from typing import Any

from analyze_crossvendor_backbones import (
    METRICS,
    POLICIES,
    permutation_bootstrap,
    read_rows,
    values,
    write_csv,
)


REPO_ROOT = Path(__file__).resolve().parents[4]
RESULT_ROOT = REPO_ROOT / "6-city" / "results" / "cityintent_v1_rc1"
INPUTS = {
    "gpt-5.4-mini": RESULT_ROOT
    / "paper_backed_baselines_2x6hardx3_gpt54mini_2026-07-09"
    / "all_runs.csv",
    "gpt-5.6-luna": RESULT_ROOT
    / "e3_backbone_luna_2x6hardx3_2026-07-10"
    / "all_runs.csv",
    "deepseek-v4-flash": RESULT_ROOT
    / "e3d_crossvendor_deepseek_2x6hardx3_2026-07-10"
    / "all_runs.csv",
    "claude-sonnet-4-5-20250929": RESULT_ROOT
    / "e3e_yunwu_claude_sonnet45_2x6hardx3_2026-07-31"
    / "all_runs.csv",
    "qwen3-235b-a22b-instruct-2507": RESULT_ROOT
    / "e3e_yunwu_qwen3_235b_a22b_instruct_2x6hardx3_2026-07-31"
    / "all_runs.csv",
}
OUTPUT_DIR = RESULT_ROOT / "e3e_multivendor_backbone_analysis_2026-07-31"
NEW_MODELS = (
    "claude-sonnet-4-5-20250929",
    "qwen3-235b-a22b-instruct-2507",
)
REFERENCE_MODEL = "deepseek-v4-flash"


def holm_adjust(rows: list[dict[str, Any]]) -> None:
    ordered = sorted(enumerate(rows), key=lambda item: item[1]["p_value"])
    running = 0.0
    total = len(rows)
    for rank, (original_index, row) in enumerate(ordered):
        adjusted = min(1.0, (total - rank) * float(row["p_value"]))
        running = max(running, adjusted)
        rows[original_index]["p_holm"] = round(running, 6)
        rows[original_index]["significant_holm_0_05"] = running < 0.05


def validate_matrix(datasets: dict[str, list[dict[str, str]]]) -> None:
    expected: set[tuple[str, str, str]] | None = None
    for model, rows in datasets.items():
        cells = {
            (row["repeat_id"], row["scenario_id"], row["agent_type"])
            for row in rows
        }
        if len(rows) != 36 or len(cells) != 36:
            raise ValueError(f"{model} must contain exactly 36 unique rows")
        if expected is None:
            expected = cells
        elif cells != expected:
            raise ValueError(f"{model} does not match the reference matrix")


def main() -> int:
    samples = 20_000
    seed = 20_260_731
    datasets = {model: read_rows(path) for model, path in INPUTS.items()}
    validate_matrix(datasets)

    summaries: list[dict[str, Any]] = []
    for model, rows in datasets.items():
        for policy, display in POLICIES.items():
            summary: dict[str, Any] = {
                "model": model,
                "policy": policy,
                "display_name": display,
                "n": len(values(rows, policy, "task_completion")),
            }
            for metric in METRICS:
                summary[metric] = round(
                    statistics.mean(values(rows, policy, metric)), 6
                )
            summaries.append(summary)

    comparisons: list[dict[str, Any]] = []
    comparison_index = 0

    def append_comparison(
        comparison_type: str,
        display_name: str,
        group_a: str,
        group_b: str,
        first: list[float],
        second: list[float],
    ) -> None:
        nonlocal comparison_index
        stats = permutation_bootstrap(
            first,
            second,
            samples=samples,
            seed=seed + comparison_index,
        )
        comparison_index += 1
        comparisons.append(
            {
                "comparison_type": comparison_type,
                "display_name": display_name,
                "group_a": group_a,
                "group_b": group_b,
                **{key: round(value, 6) for key, value in stats.items()},
            }
        )

    for model in NEW_MODELS:
        rows = datasets[model]
        append_comparison(
            "scaffold",
            "ReAct - Plan-and-Execute",
            f"{model}/ReAct",
            f"{model}/Plan-and-Execute",
            values(rows, "api_llm_react_tool_policy", "task_completion"),
            values(rows, "api_llm_plan_and_execute", "task_completion"),
        )

    for policy, display in POLICIES.items():
        append_comparison(
            "new_model_pair",
            display,
            NEW_MODELS[0],
            NEW_MODELS[1],
            values(datasets[NEW_MODELS[0]], policy, "task_completion"),
            values(datasets[NEW_MODELS[1]], policy, "task_completion"),
        )
        for model in NEW_MODELS:
            append_comparison(
                "new_vs_deepseek",
                display,
                model,
                REFERENCE_MODEL,
                values(datasets[model], policy, "task_completion"),
                values(datasets[REFERENCE_MODEL], policy, "task_completion"),
            )

    holm_adjust(comparisons)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(OUTPUT_DIR / "multivendor_summary.csv", summaries)
    write_csv(OUTPUT_DIR / "multivendor_significance.csv", comparisons)

    summary_index = {
        (row["model"], row["display_name"]): row for row in summaries
    }
    report = OUTPUT_DIR / "multivendor_comparison.md"
    with report.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("# E3e Multi-Vendor Backbone Analysis\n\n")
        handle.write(
            f"Two-sided permutation tests ({samples:,} samples), "
            "nonparametric bootstrap 95% confidence intervals, and Holm "
            "adjustment across the eight focused E3e comparisons. "
            f"Each model-policy cell has n=18. Random seed: {seed}.\n\n"
        )
        handle.write("## Main Metrics\n\n")
        handle.write(
            "| Model | Policy | Task | Feasibility | Face plaus. | "
            "Trace believ. | Face-believ. gap |\n"
        )
        handle.write("|---|---|---:|---:|---:|---:|---:|\n")
        for model in INPUTS:
            for display in POLICIES.values():
                row = summary_index[(model, display)]
                handle.write(
                    f"| {model} | {display} | "
                    f"{row['task_completion']:.3f} | "
                    f"{row['trace_feasibility']:.3f} | "
                    f"{row['judge_face_plausibility']:.3f} | "
                    f"{row['judge_trace_believability']:.3f} | "
                    f"{row['face_believability_gap']:.3f} |\n"
                )
        handle.write("\n## Focused Task-Completion Tests\n\n")
        handle.write(
            "| Type | Comparison | Policy | Delta | 95% CI | "
            "raw p | Holm p | Holm verdict |\n"
        )
        handle.write("|---|---|---|---:|---|---:|---:|---|\n")
        for row in comparisons:
            verdict = (
                "**significant**"
                if row["significant_holm_0_05"]
                else "not significant"
            )
            handle.write(
                f"| {row['comparison_type']} | "
                f"{row['group_a']} - {row['group_b']} | "
                f"{row['display_name']} | {row['delta']:+.3f} | "
                f"[{row['ci_low']:+.3f}, {row['ci_high']:+.3f}] | "
                f"{row['p_value']:.4f} | {row['p_holm']:.4f} | "
                f"{verdict} |\n"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
