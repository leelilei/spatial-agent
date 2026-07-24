"""Compare hard-tier CityIntent results across model backbones/vendors."""

from __future__ import annotations

import argparse
import csv
import random
import statistics
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
RESULT_ROOT = REPO_ROOT / "6-city" / "results" / "cityintent_v1_rc1"
DEFAULT_INPUTS = {
    "gpt-5.4-mini": RESULT_ROOT
    / "paper_backed_baselines_2x6hardx3_gpt54mini_2026-07-09"
    / "all_runs.csv",
    "gpt-5.6-luna": RESULT_ROOT
    / "e3_backbone_luna_2x6hardx3_2026-07-10"
    / "all_runs.csv",
    "deepseek-v4-flash": RESULT_ROOT
    / "e3d_crossvendor_deepseek_2x6hardx3_2026-07-10"
    / "all_runs.csv",
}
DEFAULT_OUTPUT_DIR = (
    RESULT_ROOT / "e3d_crossvendor_deepseek_2x6hardx3_2026-07-10"
)
POLICIES = {
    "api_llm_react_tool_policy": "ReAct",
    "api_llm_plan_and_execute": "Plan-and-Execute",
}
METRICS = (
    "task_completion",
    "trace_feasibility",
    "judge_face_plausibility",
    "judge_trace_believability",
    "face_believability_gap",
)


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def values(
    rows: list[dict[str, str]], policy: str, metric: str
) -> list[float]:
    return [
        float(row[metric])
        for row in rows
        if row["agent_type"] == policy and row.get(metric, "").strip()
    ]


def permutation_bootstrap(
    first: list[float],
    second: list[float],
    *,
    samples: int,
    seed: int,
) -> dict[str, float]:
    rng = random.Random(seed)
    observed = statistics.mean(first) - statistics.mean(second)
    pooled = first + second
    extreme = 0
    for _ in range(samples):
        shuffled = pooled[:]
        rng.shuffle(shuffled)
        delta = statistics.mean(shuffled[: len(first)]) - statistics.mean(
            shuffled[len(first) :]
        )
        if abs(delta) >= abs(observed) - 1e-15:
            extreme += 1
    bootstrap: list[float] = []
    for _ in range(samples):
        first_sample = rng.choices(first, k=len(first))
        second_sample = rng.choices(second, k=len(second))
        bootstrap.append(
            statistics.mean(first_sample) - statistics.mean(second_sample)
        )
    bootstrap.sort()
    low_index = int(0.025 * samples)
    high_index = min(samples - 1, int(0.975 * samples))
    return {
        "mean_a": statistics.mean(first),
        "mean_b": statistics.mean(second),
        "delta": observed,
        "ci_low": bootstrap[low_index],
        "ci_high": bootstrap[high_index],
        "p_value": (extreme + 1) / (samples + 1),
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--samples", type=int, default=20_000)
    parser.add_argument("--seed", type=int, default=20_260_724)
    args = parser.parse_args()

    datasets = {name: read_rows(path) for name, path in DEFAULT_INPUTS.items()}
    expected_cells: set[tuple[str, str, str]] | None = None
    for model, rows in datasets.items():
        cells = {
            (row["repeat_id"], row["scenario_id"], row["agent_type"])
            for row in rows
        }
        if len(rows) != 36 or len(cells) != 36:
            raise ValueError(f"{model} must contain exactly 36 unique rows")
        if expected_cells is None:
            expected_cells = cells
        elif cells != expected_cells:
            raise ValueError(f"{model} does not match the reference matrix")

    summary_rows: list[dict[str, Any]] = []
    for model, rows in datasets.items():
        for policy, display in POLICIES.items():
            item: dict[str, Any] = {
                "model": model,
                "policy": policy,
                "display_name": display,
                "n": sum(row["agent_type"] == policy for row in rows),
            }
            for metric in METRICS:
                item[metric] = round(statistics.mean(values(rows, policy, metric)), 6)
            summary_rows.append(item)

    comparisons: list[dict[str, Any]] = []
    comparison_index = 0
    for policy, display in POLICIES.items():
        for model_a, model_b in (
            ("deepseek-v4-flash", "gpt-5.4-mini"),
            ("deepseek-v4-flash", "gpt-5.6-luna"),
        ):
            stats = permutation_bootstrap(
                values(datasets[model_a], policy, "task_completion"),
                values(datasets[model_b], policy, "task_completion"),
                samples=args.samples,
                seed=args.seed + comparison_index,
            )
            comparison_index += 1
            comparisons.append(
                {
                    "comparison_type": "backbone",
                    "policy": policy,
                    "display_name": display,
                    "group_a": model_a,
                    "group_b": model_b,
                    **{key: round(value, 6) for key, value in stats.items()},
                    "significant_0_05": stats["p_value"] < 0.05,
                }
            )
    for model, rows in datasets.items():
        stats = permutation_bootstrap(
            values(rows, "api_llm_react_tool_policy", "task_completion"),
            values(rows, "api_llm_plan_and_execute", "task_completion"),
            samples=args.samples,
            seed=args.seed + comparison_index,
        )
        comparison_index += 1
        comparisons.append(
            {
                "comparison_type": "scaffold",
                "policy": "react_minus_plan_and_execute",
                "display_name": "ReAct − Plan-and-Execute",
                "group_a": f"{model}/ReAct",
                "group_b": f"{model}/Plan-and-Execute",
                **{key: round(value, 6) for key, value in stats.items()},
                "significant_0_05": stats["p_value"] < 0.05,
            }
        )

    write_csv(args.output_dir / "crossvendor_summary.csv", summary_rows)
    write_csv(args.output_dir / "crossvendor_significance.csv", comparisons)

    by_key = {
        (row["model"], row["display_name"]): row for row in summary_rows
    }
    with (args.output_dir / "crossvendor_comparison.md").open(
        "w", encoding="utf-8", newline="\n"
    ) as handle:
        handle.write("# E3d Cross-Vendor Backbone Comparison\n\n")
        handle.write(
            f"Two-sided permutation test ({args.samples:,} samples) and "
            "nonparametric bootstrap 95% CI, n=18 per model-policy cell. "
            f"Random seed: {args.seed}.\n\n"
        )
        handle.write("## Main Metrics\n\n")
        handle.write(
            "| Model | Policy | Task | Feasibility | Face plaus. | "
            "Trace believ. | Face-believ. gap |\n"
        )
        handle.write("|---|---|---:|---:|---:|---:|---:|\n")
        for model in datasets:
            for display in POLICIES.values():
                row = by_key[(model, display)]
                handle.write(
                    f"| {model} | {display} | {row['task_completion']:.3f} | "
                    f"{row['trace_feasibility']:.3f} | "
                    f"{row['judge_face_plausibility']:.3f} | "
                    f"{row['judge_trace_believability']:.3f} | "
                    f"{row['face_believability_gap']:.3f} |\n"
                )
        handle.write("\n## Task-Completion Significance\n\n")
        handle.write(
            "| Comparison | Policy | Δ | 95% CI | p | Verdict |\n"
        )
        handle.write("|---|---|---:|---|---:|---|\n")
        for row in comparisons:
            comparison = f"{row['group_a']} − {row['group_b']}"
            verdict = "**significant**" if row["significant_0_05"] else "not significant"
            handle.write(
                f"| {comparison} | {row['display_name']} | "
                f"{row['delta']:+.3f} | "
                f"[{row['ci_low']:+.3f}, {row['ci_high']:+.3f}] | "
                f"{row['p_value']:.4f} | {verdict} |\n"
            )
        handle.write("\n## Reading\n\n")
        handle.write(
            "- ReAct is comparatively backbone-robust: DeepSeek is descriptively "
            "above mini and Luna, but neither difference is significant.\n"
            "- Plan-and-Execute is backbone-sensitive: Luna significantly "
            "outperforms DeepSeek, while DeepSeek and mini are statistically "
            "indistinguishable.\n"
            "- The Luna scaffold inversion is not significant. On DeepSeek, "
            "ReAct significantly outperforms Plan-and-Execute, so scaffold "
            "ranking depends on the specific backbone rather than a single "
            "generic capability ordering.\n"
            "- DeepSeek ReAct remains nearly fully feasible while missing "
            "verified outcomes and retaining a substantial face-to-trace "
            "believability gap; the core evidence-gap finding crosses vendors.\n"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
