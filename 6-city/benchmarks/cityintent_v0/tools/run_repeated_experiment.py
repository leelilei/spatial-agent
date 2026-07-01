"""Run repeated CityIntent experiments and build paper-style summary tables."""

from __future__ import annotations

import argparse
import csv
import json
import math
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[2]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "6-city" / "results" / "cityintent_v0" / "api_repeated_reliability_gpt54mini"
DEFAULT_AGENTS = "utility_planner,api_llm_direct_actor,api_llm_plan_then_act,api_llm_reactive_replanner"


CORE_METRICS = [
    "goal_completion",
    "trace_feasibility",
    "intention_consistency",
    "replanning_success",
    "judge_face_plausibility",
    "judge_trace_believability",
    "face_believability_gap",
    "impossible_trace_rate",
    "done_state_loop_rate",
    "social_derailment_rate",
]


EXTRA_METRICS = [
    "plan_plausibility",
    "plausibility_feasibility_gap",
    "travel_efficiency",
    "budget_consistency",
    "social_appropriateness",
    "feasibility_violation",
    "city_false_continue",
    "face_feasibility_gap",
]


EXECUTION_METRICS = [
    "route_interruption_count",
    "verified_replan_count",
    "llm_calls",
    "llm_latency_seconds",
    "llm_total_tokens",
]


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write("\n")


def run_command(command: list[str], cwd: Path) -> None:
    print("+ " + " ".join(command), flush=True)
    subprocess.run(command, cwd=str(cwd), check=True)


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def sample_std(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    avg = mean(values)
    return math.sqrt(sum((value - avg) ** 2 for value in values) / (len(values) - 1))


def fmt_mean_std(mean_value: Any, std_value: Any) -> str:
    if mean_value in {"", None} or std_value in {"", None}:
        return ""
    return f"{float(mean_value):.3f} +/- {float(std_value):.3f}"


def flatten_judged_trace(repeat_id: int, item: dict[str, Any]) -> dict[str, Any]:
    metrics = item["metrics"]
    judgment = item.get("plausibility_judgment", {})
    failure_taxonomy = item.get("failure_taxonomy", {})
    row: dict[str, Any] = {
        "repeat_id": repeat_id,
        "scenario_id": item["scenario_id"],
        "family": item["family"],
        "agent_type": item["agent_type"],
        "failure_taxonomy": json.dumps(failure_taxonomy, ensure_ascii=False, sort_keys=True),
        "judge_main_issue": judgment.get("main_issue", ""),
        "judge_brief_reason": judgment.get("brief_reason", ""),
    }
    for key, value in metrics.items():
        row[key] = value
    row["judge_face_plausibility"] = judgment.get("face_plausibility")
    row["judge_trace_believability"] = judgment.get("trace_believability")
    row["judge_rationale_alignment"] = judgment.get("rationale_alignment")
    row["judge_urban_common_sense"] = judgment.get("urban_common_sense")
    row["face_feasibility_gap"] = item.get("face_feasibility_gap")
    row["face_believability_gap"] = item.get("face_believability_gap")
    telemetry = (item.get("model_info") or {}).get("llm_telemetry_summary", {})
    row["route_interruption_count"] = len(item.get("route_interruptions", []))
    row["verified_replan_count"] = len(item.get("replans", []))
    row["llm_calls"] = telemetry.get("calls")
    row["llm_latency_seconds"] = telemetry.get("latency_seconds")
    row["llm_total_tokens"] = telemetry.get("total_tokens")
    return row


def numeric_values(rows: list[dict[str, Any]], key: str) -> list[float]:
    values = []
    for row in rows:
        value = row.get(key)
        if value in {"", None}:
            continue
        values.append(float(value))
    return values


def summarize_by_agent(rows: list[dict[str, Any]], metrics: list[str]) -> list[dict[str, Any]]:
    summary_rows = []
    for agent_type in sorted({row["agent_type"] for row in rows}):
        agent_rows = [row for row in rows if row["agent_type"] == agent_type]
        summary: dict[str, Any] = {
            "agent_type": agent_type,
            "n": len(agent_rows),
            "scenario_count": len({row["scenario_id"] for row in agent_rows}),
            "repeat_count": len({row["repeat_id"] for row in agent_rows}),
        }
        for metric in metrics:
            values = numeric_values(agent_rows, metric)
            if not values:
                summary[f"{metric}_mean"] = ""
                summary[f"{metric}_std"] = ""
                continue
            summary[f"{metric}_mean"] = round(mean(values), 3)
            summary[f"{metric}_std"] = round(sample_std(values), 3)
        summary_rows.append(summary)
    return summary_rows


def summarize_by_scenario_agent(rows: list[dict[str, Any]], metrics: list[str]) -> list[dict[str, Any]]:
    summary_rows = []
    groups = sorted({(row["scenario_id"], row["agent_type"]) for row in rows})
    for scenario_id, agent_type in groups:
        group_rows = [
            row for row in rows
            if row["scenario_id"] == scenario_id and row["agent_type"] == agent_type
        ]
        summary: dict[str, Any] = {
            "scenario_id": scenario_id,
            "agent_type": agent_type,
            "n": len(group_rows),
        }
        for metric in metrics:
            values = numeric_values(group_rows, metric)
            if values:
                summary[f"{metric}_mean"] = round(mean(values), 3)
                summary[f"{metric}_std"] = round(sample_std(values), 3)
        summary_rows.append(summary)
    return summary_rows


def summarize_failures(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    summary_rows = []
    for agent_type in sorted({row["agent_type"] for row in rows}):
        agent_rows = [row for row in rows if row["agent_type"] == agent_type]
        counts: Counter[str] = Counter()
        for row in agent_rows:
            raw = row.get("failure_taxonomy") or "{}"
            taxonomy = json.loads(raw)
            for failure, count in taxonomy.items():
                counts[failure] += int(count)
        for failure, count in sorted(counts.items()):
            summary_rows.append(
                {
                    "agent_type": agent_type,
                    "failure": failure,
                    "count": count,
                    "events_per_trace": round(count / len(agent_rows), 3) if agent_rows else 0.0,
                }
            )
    return summary_rows


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        keys = []
        seen = set()
        for row in rows:
            for key in row:
                if key not in seen:
                    keys.append(key)
                    seen.add(key)
        fieldnames = keys
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(
    output_dir: Path,
    agent_summary: list[dict[str, Any]],
    scenario_summary: list[dict[str, Any]],
    failure_summary: list[dict[str, Any]],
    repeats: int,
    judged: bool,
) -> None:
    with (output_dir / "repeated_summary.md").open("w", encoding="utf-8", newline="\n") as f:
        f.write("# CityIntent Repeated Reliability Table\n\n")
        f.write(f"Repeated runs: {repeats}\n\n")
        source = "judged" if judged else "deterministically verified"
        f.write(f"Each cell is mean +/- sample standard deviation across all {source} scenario traces.\n\n")
        f.write("Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.\n\n")
        f.write("## Main Agent Table\n\n")
        f.write("| Agent | n | Goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |\n")
        f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
        for row in agent_summary:
            f.write(
                f"| `{row['agent_type']}` | {row['n']} | "
                f"{fmt_mean_std(row.get('goal_completion_mean'), row.get('goal_completion_std'))} | "
                f"{fmt_mean_std(row.get('trace_feasibility_mean'), row.get('trace_feasibility_std'))} | "
                f"{fmt_mean_std(row.get('intention_consistency_mean'), row.get('intention_consistency_std'))} | "
                f"{fmt_mean_std(row.get('replanning_success_mean'), row.get('replanning_success_std'))} | "
                f"{fmt_mean_std(row.get('judge_face_plausibility_mean'), row.get('judge_face_plausibility_std'))} | "
                f"{fmt_mean_std(row.get('judge_trace_believability_mean'), row.get('judge_trace_believability_std'))} | "
                f"{fmt_mean_std(row.get('face_believability_gap_mean'), row.get('face_believability_gap_std'))} | "
                f"{fmt_mean_std(row.get('impossible_trace_rate_mean'), row.get('impossible_trace_rate_std'))} |\n"
            )

        f.write("\n## Diagnostic Metrics\n\n")
        f.write("| Agent | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |\n")
        f.write("|---|---:|---:|---:|---:|---:|\n")
        for row in agent_summary:
            f.write(
                f"| `{row['agent_type']}` | "
                f"{fmt_mean_std(row.get('travel_efficiency_mean'), row.get('travel_efficiency_std'))} | "
                f"{fmt_mean_std(row.get('budget_consistency_mean'), row.get('budget_consistency_std'))} | "
                f"{fmt_mean_std(row.get('social_appropriateness_mean'), row.get('social_appropriateness_std'))} | "
                f"{fmt_mean_std(row.get('done_state_loop_rate_mean'), row.get('done_state_loop_rate_std'))} | "
                f"{fmt_mean_std(row.get('social_derailment_rate_mean'), row.get('social_derailment_rate_std'))} |\n"
            )

        f.write("\n## Execution Cost And Evidence\n\n")
        f.write("| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |\n")
        f.write("|---|---:|---:|---:|---:|---:|\n")
        for row in agent_summary:
            f.write(
                f"| `{row['agent_type']}` | "
                f"{fmt_mean_std(row.get('route_interruption_count_mean'), row.get('route_interruption_count_std'))} | "
                f"{fmt_mean_std(row.get('verified_replan_count_mean'), row.get('verified_replan_count_std'))} | "
                f"{fmt_mean_std(row.get('llm_calls_mean'), row.get('llm_calls_std'))} | "
                f"{fmt_mean_std(row.get('llm_latency_seconds_mean'), row.get('llm_latency_seconds_std'))} | "
                f"{fmt_mean_std(row.get('llm_total_tokens_mean'), row.get('llm_total_tokens_std'))} |\n"
            )

        if judged:
            f.write("\n## Highest Scenario-Agent Gaps\n\n")
            f.write("| Scenario | Agent | Face-believ. gap | Trace believ. | Goal | Feasibility |\n")
            f.write("|---|---|---:|---:|---:|---:|\n")
            scenario_rows = sorted(
                scenario_summary,
                key=lambda row: float(row.get("face_believability_gap_mean", 0.0)),
                reverse=True,
            )[:12]
            for row in scenario_rows:
                f.write(
                    f"| `{row['scenario_id']}` | `{row['agent_type']}` | "
                    f"{fmt_mean_std(row.get('face_believability_gap_mean'), row.get('face_believability_gap_std'))} | "
                    f"{fmt_mean_std(row.get('judge_trace_believability_mean'), row.get('judge_trace_believability_std'))} | "
                    f"{fmt_mean_std(row.get('goal_completion_mean'), row.get('goal_completion_std'))} | "
                    f"{fmt_mean_std(row.get('trace_feasibility_mean'), row.get('trace_feasibility_std'))} |\n"
                )
        else:
            f.write("\n## Scenario-Agent Breakdown\n\n")
            f.write("| Scenario | Agent | Goal | Feasibility | Replanning | Calls | Tokens |\n")
            f.write("|---|---|---:|---:|---:|---:|---:|\n")
            for row in scenario_summary:
                f.write(
                    f"| `{row['scenario_id']}` | `{row['agent_type']}` | "
                    f"{fmt_mean_std(row.get('goal_completion_mean'), row.get('goal_completion_std'))} | "
                    f"{fmt_mean_std(row.get('trace_feasibility_mean'), row.get('trace_feasibility_std'))} | "
                    f"{fmt_mean_std(row.get('replanning_success_mean'), row.get('replanning_success_std'))} | "
                    f"{fmt_mean_std(row.get('llm_calls_mean'), row.get('llm_calls_std'))} | "
                    f"{fmt_mean_std(row.get('llm_total_tokens_mean'), row.get('llm_total_tokens_std'))} |\n"
                )

        f.write("\n## Failure Taxonomy\n\n")
        if not failure_summary:
            f.write("No failure taxonomy events recorded.\n")
        else:
            f.write("| Agent | Failure | Count | Events/trace |\n")
            f.write("|---|---|---:|---:|\n")
            for row in failure_summary:
                f.write(
                    f"| `{row['agent_type']}` | `{row['failure']}` | "
                    f"{row['count']} | {row['events_per_trace']:.3f} |\n"
                )

        f.write("\n## Files\n\n")
        f.write("- `all_runs.csv`: one row per repeat/scenario/agent.\n")
        f.write("- `agent_repeated_summary.csv`: agent-level means and standard deviations.\n")
        f.write("- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.\n")
        f.write("- `failure_taxonomy_summary.csv`: aggregated failure counts.\n")


def artifact_count(path: Path) -> int:
    if not path.exists():
        return 0
    value = load_json(path)
    return len(value) if isinstance(value, list) else 0


def collect_rows(output_dir: Path, repeats: int, judged: bool = True) -> list[dict[str, Any]]:
    rows = []
    for repeat_id in range(1, repeats + 1):
        repeat_dir = output_dir / f"repeat_{repeat_id:02d}"
        trace_path = (
            repeat_dir / "judged" / "judged_traces.json"
            if judged
            else repeat_dir / "traces" / "traces.json"
        )
        traces = load_json(trace_path)
        rows.extend(flatten_judged_trace(repeat_id, item) for item in traces)
    return rows


def write_archive_markdown(
    output_dir: Path,
    run_config: dict[str, Any],
    run_records: list[dict[str, Any]],
    row_count: int,
) -> None:
    with (output_dir / "ARCHIVE.md").open("w", encoding="utf-8", newline="\n") as f:
        f.write("# CityIntent Repeated Experiment Archive\n\n")
        f.write(f"Timestamp: {run_config['timestamp']}\n\n")
        f.write("## Config\n\n")
        f.write("```json\n")
        f.write(json.dumps(run_config, indent=2, ensure_ascii=False))
        f.write("\n```\n\n")
        f.write("## Completed Runs\n\n")
        f.write("| Repeat | Traces | Judged | Traces dir | Judged dir |\n")
        f.write("|---:|---:|---:|---|---|\n")
        for record in run_records:
            f.write(
                f"| {record['repeat_id']} | {record['trace_count']} | {record['judged_count']} | "
                f"`{record['traces_dir']}` | `{record['judged_dir']}` |\n"
            )
        f.write("\n## Derived Files\n\n")
        f.write(f"- row count: {row_count}\n")
        f.write("- `repeated_summary.md`\n")
        f.write("- `all_runs.csv`\n")
        f.write("- `agent_repeated_summary.csv`\n")
        f.write("- `scenario_agent_repeated_summary.csv`\n")
        f.write("- `failure_taxonomy_summary.csv`\n")
        f.write("- `manifest.json`\n")
        f.write("- `run_config.json`\n")
        f.write("- `runs.json`\n")


def build_run_records(output_dir: Path, repeats: int) -> list[dict[str, Any]]:
    records = []
    for repeat_id in range(1, repeats + 1):
        repeat_dir = output_dir / f"repeat_{repeat_id:02d}"
        traces_path = repeat_dir / "traces" / "traces.json"
        judged_path = repeat_dir / "judged" / "judged_traces.json"
        trace_count = len(load_json(traces_path)) if traces_path.exists() else 0
        judged_count = len(load_json(judged_path)) if judged_path.exists() else 0
        records.append(
            {
                "repeat_id": repeat_id,
                "traces_dir": str(repeat_dir / "traces"),
                "judged_dir": str(repeat_dir / "judged"),
                "trace_count": trace_count,
                "judged_count": judged_count,
                "traces_json": str(traces_path),
                "judged_traces_json": str(judged_path),
            }
        )
    return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--agents", default=DEFAULT_AGENTS)
    parser.add_argument("--scenario-ids", default="")
    parser.add_argument("--limit-scenarios", type=int, default=None)
    parser.add_argument("--llm-config", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--skip-existing", action="store_true", help="Reuse existing repeat outputs when present.")
    parser.add_argument("--judge-sleep", type=float, default=0.0)
    parser.add_argument(
        "--skip-judge",
        action="store_true",
        help="Build repeated deterministic tables directly from raw traces.",
    )
    args = parser.parse_args()

    if args.repeats < 1:
        raise SystemExit("--repeats must be >= 1")

    runner = ROOT / "tools" / "run_baseline_traces.py"
    judge = ROOT / "tools" / "judge_trace_plausibility.py"
    args.output_dir.mkdir(parents=True, exist_ok=True)
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    existing_timestamps = []
    if args.skip_existing:
        for repeat_id in range(1, args.repeats + 1):
            repeat_manifest = (
                args.output_dir
                / f"repeat_{repeat_id:02d}"
                / "traces"
                / "run_manifest.json"
            )
            if repeat_manifest.exists():
                timestamp = load_json(repeat_manifest).get("timestamp")
                if timestamp:
                    existing_timestamps.append(timestamp)
    run_config = {
        "benchmark": "cityintent_v0",
        "script": str(Path(__file__).resolve()),
        "repeats": args.repeats,
        "agents": [item.strip() for item in args.agents.split(",") if item.strip()],
        "scenario_ids": [item.strip() for item in args.scenario_ids.split(",") if item.strip()],
        "limit_scenarios": args.limit_scenarios,
        "llm_config": str(args.llm_config),
        "output_dir": str(args.output_dir),
        "skip_existing": args.skip_existing,
        "judge_sleep": args.judge_sleep,
        "skip_judge": args.skip_judge,
        "timestamp": min(existing_timestamps) if existing_timestamps else now,
        "updated_at": now,
    }
    write_json(args.output_dir / "run_config.json", run_config)

    for repeat_id in range(1, args.repeats + 1):
        repeat_dir = args.output_dir / f"repeat_{repeat_id:02d}"
        traces_dir = repeat_dir / "traces"
        judged_dir = repeat_dir / "judged"
        traces_path = traces_dir / "traces.json"
        judged_path = judged_dir / "judged_traces.json"

        if not (args.skip_existing and traces_path.exists()):
            run_cmd = [
                sys.executable,
                str(runner),
                "--agents",
                args.agents,
                "--llm-config",
                str(args.llm_config),
                "--results-dir",
                str(traces_dir),
            ]
            if args.scenario_ids:
                run_cmd.extend(["--scenario-ids", args.scenario_ids])
            if args.limit_scenarios is not None:
                run_cmd.extend(["--limit-scenarios", str(args.limit_scenarios)])
            run_command(run_cmd, REPO_ROOT)
        else:
            run_cmd = [
                sys.executable,
                str(runner),
                "--agents",
                args.agents,
                "--llm-config",
                str(args.llm_config),
                "--results-dir",
                str(traces_dir),
                "--resume",
            ]
            if args.scenario_ids:
                run_cmd.extend(["--scenario-ids", args.scenario_ids])
            if args.limit_scenarios is not None:
                run_cmd.extend(["--limit-scenarios", str(args.limit_scenarios)])
            run_command(run_cmd, REPO_ROOT)

        trace_count = artifact_count(traces_path)
        judged_count = artifact_count(judged_path)
        judge_complete = trace_count > 0 and judged_count == trace_count
        if not args.skip_judge and not (args.skip_existing and judge_complete):
            judge_cmd = [
                sys.executable,
                str(judge),
                "--llm-config",
                str(args.llm_config),
                "--input",
                str(traces_path),
                "--output-dir",
                str(judged_dir),
            ]
            if args.judge_sleep:
                judge_cmd.extend(["--sleep", str(args.judge_sleep)])
            run_command(judge_cmd, REPO_ROOT)
        elif not args.skip_judge:
            print(f"Reusing complete judgments: {judged_path}", flush=True)

    rows = collect_rows(args.output_dir, args.repeats, judged=not args.skip_judge)
    metrics = CORE_METRICS + EXTRA_METRICS + EXECUTION_METRICS + ["judge_rationale_alignment", "judge_urban_common_sense"]
    agent_summary = summarize_by_agent(rows, metrics)
    scenario_summary = summarize_by_scenario_agent(rows, metrics)
    failure_summary = summarize_failures(rows)

    all_fieldnames = [
        "repeat_id",
        "scenario_id",
        "family",
        "agent_type",
        *CORE_METRICS,
        *EXTRA_METRICS,
        *EXECUTION_METRICS,
        "judge_rationale_alignment",
        "judge_urban_common_sense",
        "failure_taxonomy",
        "judge_main_issue",
        "judge_brief_reason",
    ]
    write_csv(args.output_dir / "all_runs.csv", rows, all_fieldnames)
    write_csv(args.output_dir / "agent_repeated_summary.csv", agent_summary)
    write_csv(args.output_dir / "scenario_agent_repeated_summary.csv", scenario_summary)
    write_csv(args.output_dir / "failure_taxonomy_summary.csv", failure_summary)
    run_records = build_run_records(args.output_dir, args.repeats)
    write_json(args.output_dir / "runs.json", run_records)
    write_json(
        args.output_dir / "manifest.json",
        {
            **run_config,
            "repeats": args.repeats,
            "core_metrics": CORE_METRICS,
            "extra_metrics": EXTRA_METRICS,
            "execution_metrics": EXECUTION_METRICS,
            "row_count": len(rows),
            "run_records": run_records,
        },
    )
    write_markdown(
        args.output_dir,
        agent_summary,
        scenario_summary,
        failure_summary,
        args.repeats,
        judged=not args.skip_judge,
    )
    write_archive_markdown(args.output_dir, run_config, run_records, len(rows))
    print(f"Wrote repeated experiment table to {args.output_dir / 'repeated_summary.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
