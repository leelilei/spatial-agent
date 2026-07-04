"""Analyze matched control/treatment CityIntent perturbation scenarios."""

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
    "impossible_trace_rate",
    "route_interruption_count",
    "verified_replan_count",
    "llm_calls",
    "llm_latency_seconds",
    "llm_total_tokens",
]


def load_scenario_pairs(scenario_dir: Path) -> dict[str, dict[str, str]]:
    scenarios: dict[str, dict[str, str]] = {}
    for path in sorted(scenario_dir.glob("*.json")):
        scenario = json.loads(path.read_text(encoding="utf-8"))
        pair = scenario.get("perturbation_pair")
        if pair:
            scenarios[scenario["scenario_id"]] = {
                "pair_id": pair["pair_id"],
                "variant": pair["variant"],
            }
    return scenarios


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def value(row: dict[str, Any], metric: str) -> float:
    raw = row.get(metric)
    return float(raw) if raw not in {None, ""} else 0.0


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def pair_rows(
    rows: list[dict[str, str]],
    scenario_pairs: dict[str, dict[str, str]],
) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str], dict[str, dict[str, str]]] = defaultdict(dict)
    for row in rows:
        metadata = scenario_pairs.get(row["scenario_id"])
        if not metadata:
            continue
        key = (row["repeat_id"], row["agent_type"], metadata["pair_id"])
        grouped[key][metadata["variant"]] = row

    paired: list[dict[str, Any]] = []
    incomplete = []
    for (repeat_id, agent_type, pair_id), variants in sorted(grouped.items()):
        if set(variants) != {"control", "treatment"}:
            incomplete.append((repeat_id, agent_type, pair_id, sorted(variants)))
            continue
        control = variants["control"]
        treatment = variants["treatment"]
        result: dict[str, Any] = {
            "repeat_id": int(repeat_id),
            "pair_id": pair_id,
            "agent_type": agent_type,
            "control_scenario_id": control["scenario_id"],
            "treatment_scenario_id": treatment["scenario_id"],
        }
        for metric in METRICS:
            control_value = value(control, metric)
            treatment_value = value(treatment, metric)
            result[f"control_{metric}"] = control_value
            result[f"treatment_{metric}"] = treatment_value
            result[f"delta_{metric}"] = treatment_value - control_value
        result["control_full_task"] = float(result["control_task_completion"] >= 0.999)
        result["treatment_full_task"] = float(result["treatment_task_completion"] >= 0.999)
        result["control_fully_feasible"] = float(result["control_trace_feasibility"] >= 0.999)
        result["treatment_fully_feasible"] = float(result["treatment_trace_feasibility"] >= 0.999)
        result["control_joint_success"] = float(
            result["control_full_task"] and result["control_fully_feasible"]
        )
        result["treatment_joint_success"] = float(
            result["treatment_full_task"] and result["treatment_fully_feasible"]
        )
        paired.append(result)
    if incomplete:
        raise ValueError(f"incomplete perturbation cells: {incomplete}")
    return paired


def summarize(pairs: list[dict[str, Any]], group_key: str) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for pair in pairs:
        grouped[str(pair[group_key])].append(pair)

    summaries = []
    for group, group_rows in sorted(grouped.items()):
        item: dict[str, Any] = {group_key: group, "n": len(group_rows)}
        for metric in METRICS:
            controls = [row[f"control_{metric}"] for row in group_rows]
            treatments = [row[f"treatment_{metric}"] for row in group_rows]
            item[f"control_{metric}"] = mean(controls)
            item[f"treatment_{metric}"] = mean(treatments)
            item[f"delta_{metric}"] = mean(treatments) - mean(controls)
        for metric in (
            "full_task",
            "fully_feasible",
            "joint_success",
        ):
            item[f"control_{metric}_rate"] = mean(
                [row[f"control_{metric}"] for row in group_rows]
            )
            item[f"treatment_{metric}_rate"] = mean(
                [row[f"treatment_{metric}"] for row in group_rows]
            )
        task_eligible = [row for row in group_rows if row["control_full_task"]]
        joint_eligible = [row for row in group_rows if row["control_joint_success"]]
        item["task_recovery_eligible_n"] = len(task_eligible)
        item["conditional_task_recovery_rate"] = (
            mean([row["treatment_full_task"] for row in task_eligible])
            if task_eligible
            else None
        )
        item["joint_recovery_eligible_n"] = len(joint_eligible)
        item["conditional_joint_recovery_rate"] = (
            mean([row["treatment_joint_success"] for row in joint_eligible])
            if joint_eligible
            else None
        )
        summaries.append(item)
    return summaries


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def optional(value: Any) -> str:
    return "n/a" if value is None else f"{float(value):.3f}"


def write_markdown(
    path: Path,
    agent_summary: list[dict[str, Any]],
    pair_summary: list[dict[str, Any]],
) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("# CityIntent Matched Perturbation Analysis\n\n")
        f.write("Deltas are treatment minus control. Negative task or feasibility deltas indicate perturbation loss.\n\n")
        f.write("## By Adapter\n\n")
        f.write("| Adapter | n | Task C/T | Task delta | Feas. C/T | Feas. delta | Joint C/T | Conditional task recovery | Conditional joint recovery |\n")
        f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|\n")
        for row in agent_summary:
            f.write(
                f"| `{row['agent_type']}` | {row['n']} | "
                f"{row['control_task_completion']:.3f}/{row['treatment_task_completion']:.3f} | "
                f"{row['delta_task_completion']:+.3f} | "
                f"{row['control_trace_feasibility']:.3f}/{row['treatment_trace_feasibility']:.3f} | "
                f"{row['delta_trace_feasibility']:+.3f} | "
                f"{row['control_joint_success_rate']:.3f}/{row['treatment_joint_success_rate']:.3f} | "
                f"{optional(row['conditional_task_recovery_rate'])} ({row['task_recovery_eligible_n']}) | "
                f"{optional(row['conditional_joint_recovery_rate'])} ({row['joint_recovery_eligible_n']}) |\n"
            )

        f.write("\n## By Perturbation\n\n")
        f.write("| Pair | n | Task C/T | Task delta | Feas. C/T | Feas. delta | Interruptions C/T | Replans C/T |\n")
        f.write("|---|---:|---:|---:|---:|---:|---:|---:|\n")
        for row in pair_summary:
            f.write(
                f"| `{row['pair_id']}` | {row['n']} | "
                f"{row['control_task_completion']:.3f}/{row['treatment_task_completion']:.3f} | "
                f"{row['delta_task_completion']:+.3f} | "
                f"{row['control_trace_feasibility']:.3f}/{row['treatment_trace_feasibility']:.3f} | "
                f"{row['delta_trace_feasibility']:+.3f} | "
                f"{row['control_route_interruption_count']:.2f}/{row['treatment_route_interruption_count']:.2f} | "
                f"{row['control_verified_replan_count']:.2f}/{row['treatment_verified_replan_count']:.2f} |\n"
            )

        f.write("\n## Interpretation Rules\n\n")
        f.write("- Compare only matched cells with identical agent, repeat, goals, and non-event scenario fields.\n")
        f.write("- Conditional recovery is evaluated only where the corresponding control succeeds.\n")
        f.write("- One repeat estimates direction; repeated pairs are required for reliability claims.\n")
        f.write("- Soft plausibility deltas are diagnostic and do not replace hard environment evidence.\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--scenario-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    scenarios = load_scenario_pairs(args.scenario_dir)
    pairs = pair_rows(read_csv(args.input), scenarios)
    agent_summary = summarize(pairs, "agent_type")
    pair_summary = summarize(pairs, "pair_id")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(args.output_dir / "perturbation_pairs.csv", pairs)
    write_csv(args.output_dir / "perturbation_agent_summary.csv", agent_summary)
    write_csv(args.output_dir / "perturbation_pair_summary.csv", pair_summary)
    write_markdown(
        args.output_dir / "perturbation_analysis.md",
        agent_summary,
        pair_summary,
    )
    manifest = {
        "schema_version": "cityintent_matched_perturbation_v1",
        "input": str(args.input),
        "scenario_dir": str(args.scenario_dir),
        "paired_cells": len(pairs),
        "pair_ids": sorted({row["pair_id"] for row in pairs}),
        "agents": sorted({row["agent_type"] for row in pairs}),
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    (args.output_dir / "perturbation_analysis_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Analyzed {len(pairs)} matched perturbation cells")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
