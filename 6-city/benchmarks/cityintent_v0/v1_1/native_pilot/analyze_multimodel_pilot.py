#!/usr/bin/env python3
"""Analyze the oracle-verified CityIntent v1.1 native multi-model pilot."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


MODELS = ("claude", "qwen", "deepseek")
POLICY_LABELS = {
    "api_llm_react_tool_policy": "ReAct",
    "api_llm_plan_and_execute": "PlanExec",
}
METRICS = (
    "task_completion", "trace_feasibility", "constraint_satisfaction",
    "intention_consistency", "judge_face_plausibility", "judge_trace_believability",
    "face_believability_gap",
)


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def row_metrics(row: dict[str, Any]) -> dict[str, float]:
    metrics = row["metrics"]
    judgment = row["plausibility_judgment"]
    return {
        "task_completion": float(metrics["task_completion"]),
        "trace_feasibility": float(metrics["trace_feasibility"]),
        "constraint_satisfaction": float(metrics["constraint_satisfaction"]),
        "intention_consistency": float(metrics["intention_consistency"]),
        "judge_face_plausibility": float(judgment["face_plausibility"]),
        "judge_trace_believability": float(judgment["trace_believability"]),
        "face_believability_gap": float(row["face_believability_gap"]),
    }


def telemetry(row: dict[str, Any]) -> dict[str, float]:
    calls = row.get("llm_telemetry", [])
    return {
        "calls": len(calls),
        "latency_seconds": sum(float(call.get("latency_seconds") or 0) for call in calls),
        "input_tokens": sum(int(call.get("input_tokens") or 0) for call in calls),
        "output_tokens": sum(int(call.get("output_tokens") or 0) for call in calls),
        "total_tokens": sum(int(call.get("total_tokens") or 0) for call in calls),
    }


def analyze(result_root: Path) -> dict[str, Any]:
    rows = []
    for model in MODELS:
        run_dir = result_root / f"native_pilot_multimodel_{model}_2x8x1_2026-08-01"
        judged = json.loads((run_dir / "judged_fhl_gpt54mini" / "judged_traces.json").read_text(encoding="utf-8"))
        for row in judged:
            rows.append({"model": model, **row})

    aggregate = []
    construct_rows = []
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    construct_grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    item_scores: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        policy = POLICY_LABELS[row["agent_type"]]
        grouped[(row["model"], policy)].append(row)
        construct_grouped[(row["model"], policy, row["family"])].append(row)
        item_scores[row["scenario_id"]].append(float(row["metrics"]["task_completion"]))

    for (model, policy), members in sorted(grouped.items()):
        metric_values = [row_metrics(row) for row in members]
        tel = [telemetry(row) for row in members]
        aggregate.append({
            "model": model,
            "policy": policy,
            "episodes": len(members),
            **{metric: mean([item[metric] for item in metric_values]) for metric in METRICS},
            "full_task_rate": mean([float(item["task_completion"] == 1.0) for item in metric_values]),
            "fully_feasible_rate": mean([float(item["trace_feasibility"] == 1.0) for item in metric_values]),
            **{key: round(sum(item[key] for item in tel), 3) for key in ("calls", "latency_seconds", "input_tokens", "output_tokens", "total_tokens")},
        })

    for (model, policy, construct), members in sorted(construct_grouped.items()):
        metric_values = [row_metrics(row) for row in members]
        construct_rows.append({
            "model": model, "policy": policy, "construct": construct,
            **{metric: mean([item[metric] for item in metric_values]) for metric in METRICS},
        })

    policy_deltas = []
    for model in MODELS:
        react = next(row for row in aggregate if row["model"] == model and row["policy"] == "ReAct")
        plan = next(row for row in aggregate if row["model"] == model and row["policy"] == "PlanExec")
        policy_deltas.append({
            "model": model,
            "react_minus_plan_task": round(react["task_completion"] - plan["task_completion"], 6),
            "react_minus_plan_feasibility": round(react["trace_feasibility"] - plan["trace_feasibility"], 6),
            "react_minus_plan_constraint": round(react["constraint_satisfaction"] - plan["constraint_satisfaction"], 6),
            "react_minus_plan_trace_believability": round(react["judge_trace_believability"] - plan["judge_trace_believability"], 6),
        })

    item_analysis = [
        {
            "scenario_id": scenario_id,
            "min_task": min(scores), "max_task": max(scores),
            "range": round(max(scores) - min(scores), 6),
            "all_system_ceiling": min(scores) >= .95,
            "all_system_floor": max(scores) <= .05,
        }
        for scenario_id, scores in sorted(item_scores.items())
    ]
    return {
        "schema_version": "cityintent_native_pilot_analysis_v1",
        "episodes": len(rows),
        "aggregate": aggregate,
        "construct_rows": construct_rows,
        "policy_deltas": policy_deltas,
        "item_analysis": item_analysis,
        "all_system_ceiling_count": sum(item["all_system_ceiling"] for item in item_analysis),
        "all_system_floor_count": sum(item["all_system_floor"] for item in item_analysis),
        "discriminating_item_count": sum(item["range"] >= .15 for item in item_analysis),
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    report = analyze(args.result_root.resolve())
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    (output / "analysis.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_csv(output / "model_policy_summary.csv", report["aggregate"])
    write_csv(output / "construct_summary.csv", report["construct_rows"])
    write_csv(output / "item_analysis.csv", report["item_analysis"])
    with (output / "SUMMARY.md").open("w", encoding="utf-8") as handle:
        handle.write("# CityIntent v1.1 native multi-model pilot\n\n")
        handle.write("One oracle-verified item per construct; one run per model-policy cell. Results are descriptive calibration, not inferential leaderboard claims.\n\n")
        handle.write("| model | policy | task | feasibility | constraint | trace belief | face-belief gap | calls | tokens |\n")
        handle.write("|---|---|---:|---:|---:|---:|---:|---:|---:|\n")
        for row in report["aggregate"]:
            handle.write(f"| {row['model']} | {row['policy']} | {row['task_completion']:.3f} | {row['trace_feasibility']:.3f} | {row['constraint_satisfaction']:.3f} | {row['judge_trace_believability']:.3f} | {row['face_believability_gap']:.3f} | {int(row['calls'])} | {int(row['total_tokens'])} |\n")
        handle.write(f"\nItem screen across six real systems: {report['discriminating_item_count']}/8 range >= 0.15; {report['all_system_ceiling_count']} ceiling; {report['all_system_floor_count']} floor.\n")
    print(json.dumps({key: report[key] for key in ("episodes", "discriminating_item_count", "all_system_ceiling_count", "all_system_floor_count")}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
