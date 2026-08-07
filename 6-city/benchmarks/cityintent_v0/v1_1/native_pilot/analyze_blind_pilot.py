#!/usr/bin/env python3
"""Analyze blind-observation CityIntent pilot traces without a soft judge."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


TOOLS = Path(__file__).resolve().parents[2] / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
import run_baseline_traces as runner  # noqa: E402


POLICY_LABELS = {
    "api_llm_react_tool_policy": "ReAct",
    "api_llm_plan_and_execute": "PlanExec",
}
HARD_METRICS = (
    "task_completion",
    "trace_feasibility",
    "constraint_satisfaction",
    "intention_consistency",
)


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def pearson(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 3 or len(xs) != len(ys):
        return None
    x_mean = sum(xs) / len(xs)
    y_mean = sum(ys) / len(ys)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
    x_scale = sum((x - x_mean) ** 2 for x in xs) ** 0.5
    y_scale = sum((y - y_mean) ** 2 for y in ys) ** 0.5
    if x_scale == 0 or y_scale == 0:
        return None
    return round(numerator / (x_scale * y_scale), 6)


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def load_benchmark(config_path: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    root = config_path.parent
    worlds = runner.load_worlds(config, root)
    scenario_root = root / config["scenario_dir"]
    scenarios = {
        scenario["scenario_id"]: scenario
        for path in scenario_root.rglob("*.json")
        for scenario in [json.loads(path.read_text(encoding="utf-8"))]
    }
    return worlds, scenarios


def replay_metrics(
    row: dict[str, Any], worlds: dict[str, Any], scenarios: dict[str, Any]
) -> dict[str, Any]:
    scenario = scenarios[row["scenario_id"]]
    primary = next(
        agent for agent in scenario["agents"]
        if agent["agent_id"] == scenario["primary_agent"]
    )
    state = runner.TraceState(
        scenario_id=scenario["scenario_id"],
        agent_id=primary["agent_id"],
        agent_type=row["agent_type"],
        time=runner.parse_time(scenario["episode"]["start_time"]),
        end_time=runner.parse_time(scenario["episode"]["end_time"]),
        location=primary["start_location"],
        budget=float(primary["budget"]),
    )
    state.inside_location = state.location
    runner.record_visit(state, state.location, state.time, kind="start")
    runner.record_entry(state, state.location, state.time, kind="start")
    action_fields = {
        "kind", "target", "path", "minutes", "to", "content", "item",
        "service", "query", "reason", "raw_response",
    }
    for record in row["trace"]:
        payload = {
            key: value for key, value in record["action"].items()
            if key in action_fields
        }
        runner.execute_action(
            worlds[scenario["world_id"]], scenario, state, runner.Action(**payload)
        )
        if payload["kind"] in {"finish", "abandon"}:
            break
    rescored = runner.score_trace(worlds[scenario["world_id"]], scenario, state)
    return {**row, "metrics": rescored["metrics"], "conditions": rescored["conditions"]}


def analyze(
    run_dirs: list[Path], expected_systems: int, benchmark_config: Path | None
) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    run_coverage = []
    benchmark = load_benchmark(benchmark_config) if benchmark_config else None
    for run_dir in run_dirs:
        traces = json.loads((run_dir / "traces.json").read_text(encoding="utf-8"))
        if benchmark:
            traces = [replay_metrics(row, *benchmark) for row in traces]
        models = sorted({
            (row.get("model_info") or {}).get("model", run_dir.name)
            for row in traces
        })
        model = models[0] if len(models) == 1 else f"mixed[{len(models)}]"
        rows.extend({
            "model": (row.get("model_info") or {}).get("model", run_dir.name),
            **row,
        } for row in traces)
        manifest_path = run_dir / "run_manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
        run_coverage.append({
            "model": model,
            "trace_count": len(traces),
            "status": manifest.get("status", "unknown"),
            "run_dir": str(run_dir),
        })

    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    item_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    system_item_scores: dict[tuple[str, str], dict[str, float]] = defaultdict(dict)
    for row in rows:
        system_key = (row["model"], POLICY_LABELS[row["agent_type"]])
        grouped[system_key].append(row)
        item_groups[row["scenario_id"]].append(row)
        system_item_scores[system_key][row["scenario_id"]] = float(
            row["metrics"]["task_completion"]
        )

    systems = []
    for (model, policy), members in sorted(grouped.items()):
        telemetry = [call for row in members for call in row.get("llm_telemetry", [])]
        systems.append({
            "model": model,
            "policy": policy,
            "episodes": len(members),
            **{
                metric: mean([float(row["metrics"][metric]) for row in members])
                for metric in HARD_METRICS
            },
            "full_task_rate": mean([
                float(row["metrics"]["task_completion"] == 1.0) for row in members
            ]),
            "calls": len(telemetry),
            "total_tokens": sum(int(call.get("total_tokens") or 0) for call in telemetry),
        })

    items = []
    for scenario_id, members in sorted(item_groups.items()):
        scores = [float(row["metrics"]["task_completion"]) for row in members]
        item_scores_for_correlation = []
        rest_scores_for_correlation = []
        for system_key, per_item in system_item_scores.items():
            if scenario_id not in per_item or len(per_item) < 2:
                continue
            other_scores = [
                score for item_id, score in per_item.items()
                if item_id != scenario_id
            ]
            item_scores_for_correlation.append(per_item[scenario_id])
            rest_scores_for_correlation.append(sum(other_scores) / len(other_scores))
        item_total_correlation = pearson(
            item_scores_for_correlation, rest_scores_for_correlation
        )
        items.append({
            "scenario_id": scenario_id,
            "construct": members[0]["family"],
            "systems_observed": len(scores),
            "systems_expected": expected_systems,
            "coverage_complete": len(scores) == expected_systems,
            "mean_task": mean(scores),
            "min_task": min(scores),
            "max_task": max(scores),
            "range": round(max(scores) - min(scores), 6),
            "corrected_item_total_correlation": item_total_correlation,
            "negative_item_total": (
                item_total_correlation is not None and item_total_correlation < 0
            ),
            "all_observed_ceiling": min(scores) >= 0.95,
            "all_observed_floor": max(scores) <= 0.05,
            "discriminating": max(scores) - min(scores) >= 0.15,
        })

    return {
        "schema_version": "cityintent_blind_pilot_hard_analysis_v1",
        "observation_contract": "intent_only_v1",
        "rescored_from_actions": benchmark_config is not None,
        "episodes_observed": len(rows),
        "episodes_expected": len(item_groups) * expected_systems,
        "coverage_complete": len(rows) == len(item_groups) * expected_systems,
        "run_coverage": run_coverage,
        "system_summary": systems,
        "item_analysis": items,
        "complete_item_count": sum(item["coverage_complete"] for item in items),
        "observed_ceiling_count": sum(item["all_observed_ceiling"] for item in items),
        "discriminating_item_count": sum(item["discriminating"] for item in items),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", action="append", type=Path, required=True)
    parser.add_argument("--expected-systems", type=int, default=6)
    parser.add_argument("--benchmark-config", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    report = analyze(
        [path.resolve() for path in args.run_dir],
        args.expected_systems,
        args.benchmark_config.resolve() if args.benchmark_config else None,
    )
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    (output / "analysis.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_csv(output / "system_summary.csv", report["system_summary"])
    write_csv(output / "item_analysis.csv", report["item_analysis"])
    with (output / "SUMMARY.md").open("w", encoding="utf-8") as handle:
        item_count = len(report["item_analysis"])
        handle.write("# CityIntent v1.1 blind pilot hard-score analysis\n\n")
        handle.write(
            f"Coverage: {report['episodes_observed']}/{report['episodes_expected']} traces; "
            f"{report['complete_item_count']}/{item_count} items have all six systems. "
            "Missing traces are not imputed.\n\n"
        )
        handle.write("| model | policy | n | task | feasibility | constraint | full-task rate | tokens |\n")
        handle.write("|---|---|---:|---:|---:|---:|---:|---:|\n")
        for row in report["system_summary"]:
            handle.write(
                f"| {row['model']} | {row['policy']} | {row['episodes']} | "
                f"{row['task_completion']:.3f} | {row['trace_feasibility']:.3f} | "
                f"{row['constraint_satisfaction']:.3f} | {row['full_task_rate']:.3f} | "
                f"{row['total_tokens']} |\n"
            )
        handle.write("\n| construct | observed | mean | min | max | range | corrected item-total r | ceiling |\n")
        handle.write("|---|---:|---:|---:|---:|---:|---:|---:|\n")
        for row in report["item_analysis"]:
            correlation = row["corrected_item_total_correlation"]
            correlation_text = "NA" if correlation is None else f"{correlation:.3f}"
            handle.write(
                f"| {row['construct']} | {row['systems_observed']}/{row['systems_expected']} | "
                f"{row['mean_task']:.3f} | {row['min_task']:.3f} | {row['max_task']:.3f} | "
                f"{row['range']:.3f} | {correlation_text} | "
                f"{'yes' if row['all_observed_ceiling'] else 'no'} |\n"
            )
    print(json.dumps({
        "episodes": report["episodes_observed"],
        "expected": report["episodes_expected"],
        "complete_items": report["complete_item_count"],
        "ceiling_items": report["observed_ceiling_count"],
        "discriminating_items": report["discriminating_item_count"],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
