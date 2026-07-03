"""Compare two CityIntent agent-model runs over matched scenario-adapter cells."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


METRICS = [
    "task_completion",
    "trace_feasibility",
    "intention_consistency",
    "judge_face_plausibility",
    "judge_trace_believability",
    "llm_calls",
    "llm_latency_seconds",
    "llm_total_tokens",
]


def read_rows(path: Path, repeat_id: int) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return [row for row in csv.DictReader(f) if int(row["repeat_id"]) == repeat_id]


def number(value: Any) -> float:
    return float(value) if value not in {"", None} else 0.0


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def compare_rows(
    baseline: list[dict[str, str]],
    candidate: list[dict[str, str]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    baseline_index = {(row["scenario_id"], row["agent_type"]): row for row in baseline}
    candidate_index = {(row["scenario_id"], row["agent_type"]): row for row in candidate}
    if baseline_index.keys() != candidate_index.keys():
        missing_candidate = sorted(baseline_index.keys() - candidate_index.keys())
        missing_baseline = sorted(candidate_index.keys() - baseline_index.keys())
        raise ValueError(
            f"unmatched cells; missing candidate={missing_candidate}, "
            f"missing baseline={missing_baseline}"
        )

    pairs: list[dict[str, Any]] = []
    for scenario_id, agent_type in sorted(baseline_index):
        baseline_row = baseline_index[(scenario_id, agent_type)]
        candidate_row = candidate_index[(scenario_id, agent_type)]
        pair: dict[str, Any] = {"scenario_id": scenario_id, "agent_type": agent_type}
        for metric in METRICS:
            baseline_value = number(baseline_row.get(metric))
            candidate_value = number(candidate_row.get(metric))
            pair[f"baseline_{metric}"] = baseline_value
            pair[f"candidate_{metric}"] = candidate_value
            pair[f"delta_{metric}"] = candidate_value - baseline_value
        pairs.append(pair)

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for pair in pairs:
        grouped[pair["agent_type"]].append(pair)

    summary = []
    for agent_type, rows in sorted(grouped.items()):
        item: dict[str, Any] = {"agent_type": agent_type, "n": len(rows)}
        for metric in METRICS:
            baseline_values = [row[f"baseline_{metric}"] for row in rows]
            candidate_values = [row[f"candidate_{metric}"] for row in rows]
            item[f"baseline_{metric}"] = mean(baseline_values)
            item[f"candidate_{metric}"] = mean(candidate_values)
            item[f"delta_{metric}"] = mean(candidate_values) - mean(baseline_values)
        item["baseline_full_task_rate"] = mean(
            [float(row["baseline_task_completion"] >= 0.999) for row in rows]
        )
        item["candidate_full_task_rate"] = mean(
            [float(row["candidate_task_completion"] >= 0.999) for row in rows]
        )
        item["baseline_fully_feasible_rate"] = mean(
            [float(row["baseline_trace_feasibility"] >= 0.999) for row in rows]
        )
        item["candidate_fully_feasible_rate"] = mean(
            [float(row["candidate_trace_feasibility"] >= 0.999) for row in rows]
        )
        summary.append(item)
    return pairs, summary


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(
    path: Path,
    summary: list[dict[str, Any]],
    baseline_label: str,
    candidate_label: str,
) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("# CityIntent Agent-Model Sensitivity\n\n")
        f.write(f"Baseline agent model: `{baseline_label}`. Candidate agent model: `{candidate_label}`.\n\n")
        f.write("All deltas are candidate minus baseline over matched scenario-adapter cells.\n\n")
        f.write("| Adapter | n | Task base | Task cand. | Delta | Feas. base | Feas. cand. | Delta | Full task base/cand. | Full feas. base/cand. |\n")
        f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
        for row in summary:
            f.write(
                f"| `{row['agent_type']}` | {row['n']} | "
                f"{row['baseline_task_completion']:.3f} | {row['candidate_task_completion']:.3f} | "
                f"{row['delta_task_completion']:+.3f} | "
                f"{row['baseline_trace_feasibility']:.3f} | {row['candidate_trace_feasibility']:.3f} | "
                f"{row['delta_trace_feasibility']:+.3f} | "
                f"{row['baseline_full_task_rate']:.3f}/{row['candidate_full_task_rate']:.3f} | "
                f"{row['baseline_fully_feasible_rate']:.3f}/{row['candidate_fully_feasible_rate']:.3f} |\n"
            )

        f.write("\n## Execution Cost\n\n")
        f.write("| Adapter | Calls base/cand. | Latency base/cand. (s) | Tokens base/cand. |\n")
        f.write("|---|---:|---:|---:|\n")
        for row in summary:
            f.write(
                f"| `{row['agent_type']}` | {row['baseline_llm_calls']:.2f}/{row['candidate_llm_calls']:.2f} | "
                f"{row['baseline_llm_latency_seconds']:.1f}/{row['candidate_llm_latency_seconds']:.1f} | "
                f"{row['baseline_llm_total_tokens']:.0f}/{row['candidate_llm_total_tokens']:.0f} |\n"
            )

        f.write("\n## Reading\n\n")
        f.write("- A positive delta is not expected for every adapter; model-by-architecture interactions are part of the result.\n")
        f.write("- This one-run paired comparison estimates direction, not repeated model-effect reliability.\n")
        f.write("- Hard task and feasibility deltas are primary; soft scores remain judge-dependent.\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--baseline-repeat", type=int, default=1)
    parser.add_argument("--candidate-repeat", type=int, default=1)
    parser.add_argument("--baseline-label", required=True)
    parser.add_argument("--candidate-label", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    baseline = read_rows(args.baseline, args.baseline_repeat)
    candidate = read_rows(args.candidate, args.candidate_repeat)
    pairs, summary = compare_rows(baseline, candidate)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(args.output_dir / "agent_model_pairs.csv", pairs)
    write_csv(args.output_dir / "agent_model_summary.csv", summary)
    write_markdown(
        args.output_dir / "agent_model_sensitivity.md",
        summary,
        args.baseline_label,
        args.candidate_label,
    )
    manifest = {
        "schema_version": "cityintent_agent_model_sensitivity_v1",
        "baseline": str(args.baseline),
        "candidate": str(args.candidate),
        "baseline_repeat": args.baseline_repeat,
        "candidate_repeat": args.candidate_repeat,
        "baseline_label": args.baseline_label,
        "candidate_label": args.candidate_label,
        "paired_cells": len(pairs),
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    (args.output_dir / "agent_model_comparison_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Compared {len(pairs)} matched agent-model cells")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
