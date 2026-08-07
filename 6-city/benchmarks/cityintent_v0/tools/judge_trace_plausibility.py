"""Judge CityIntent trace plausibility with a real LLM provider.

This script is a second-pass evaluator. It does not execute the environment and
does not replace deterministic trace validation. It asks an independent model for
two different judgments:

1. face plausibility: whether the actions and reasons sound like a reasonable
   city plan at demo/face-validity level;
2. trace believability: whether the complete behavior still looks reasonable as
   an urban trace.

The CityAgency paper story should compare face plausibility against deterministic
trace feasibility.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[2]
STANDARD_LLM_DIR = REPO_ROOT / "0-Tools" / "research-standard"
DEFAULT_INPUT = REPO_ROOT / "6-city" / "results" / "cityintent_v0" / "api_architecture_gap_gpt54mini" / "traces.json"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "6-city" / "results" / "cityintent_v0" / "api_architecture_gap_gpt54mini_judged"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_name(f"{path.name}.tmp")
    with temp_path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write("\n")

    # Windows indexers and sync clients can briefly hold the destination file.
    # Keep the last complete archive intact and retry the atomic replacement.
    for attempt in range(5):
        try:
            temp_path.replace(path)
            return
        except OSError:
            if attempt == 4:
                raise
            time.sleep(0.2 * (attempt + 1))


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sanitized_config(path: Path) -> dict[str, Any]:
    config = load_json(path)
    return {
        key: value
        for key, value in config.items()
        if key == "api_key_env" or "key" not in key.lower()
    }


def load_scenarios(benchmark_config: Path | None = None) -> dict[str, dict[str, Any]]:
    if benchmark_config is None:
        scenario_paths = sorted((ROOT / "scenarios").glob("*.json"))
    else:
        config_path = benchmark_config.resolve()
        config = load_json(config_path)
        scenario_root = config_path.parent / config.get("scenario_dir", "scenarios")
        scenario_paths = (
            sorted(
                path
                for split in config["scenario_splits"]
                for path in (scenario_root / split).rglob("*.json")
            )
            if config.get("scenario_splits")
            else sorted(scenario_root.rglob("*.json"))
        )
    return {
        load_json(path)["scenario_id"]: load_json(path)
        for path in scenario_paths
    }


def compact_trace(result: dict[str, Any]) -> list[dict[str, Any]]:
    compact = []
    for step in result["trace"]:
        action = step.get("action", {})
        compact.append(
            {
                "step": step.get("step"),
                "start_time": step.get("start_time"),
                "start_location": step.get("start_location"),
                "kind": action.get("kind"),
                "target": action.get("target"),
                "minutes": action.get("minutes"),
                "to": action.get("to"),
                "content": action.get("content"),
                "reason": action.get("reason"),
                "end_time": step.get("end_time"),
                "end_location": step.get("end_location"),
            }
        )
    return compact


def build_prompt(result: dict[str, Any], scenario: dict[str, Any]) -> dict[str, Any]:
    primary = next(agent for agent in scenario["agents"] if agent["agent_id"] == scenario["primary_agent"])
    return {
        "task": "Judge whether this city-agent action trace is a plausible urban plan/behavior.",
        "important_instruction": [
            "Do not use deterministic validator labels; judge from the scenario and action trace.",
            "Score face_plausibility as face validity: would the actions and reasons sound like a reasonable city plan in a demo or narrative, before deterministic validation?",
            "Score trace_believability as full behavior quality: does the complete sequence still look reasonable after seeing repetitions, missed goals, odd sequencing, or social derailment?",
            "Do not require perfect optimality; plausible but inefficient behavior can still score moderately high.",
            "If actions sound locally reasonable but the full sequence loops or drifts, face_plausibility can be high while trace_believability is low.",
        ],
        "response_schema": {
            "face_plausibility": "float 0-1; surface plausibility of the actions and reasons as a city plan",
            "trace_believability": "float 0-1; full-sequence believability as city behavior",
            "rationale_alignment": "float 0-1; whether stated reasons match actions and scenario",
            "urban_common_sense": "float 0-1; whether the behavior resembles ordinary city activity",
            "main_issue": "short phrase naming the biggest plausibility issue, or 'none'",
            "brief_reason": "one concise sentence",
        },
        "scenario": {
            "id": scenario["scenario_id"],
            "title": scenario["title"],
            "family": scenario["family"],
            "public_context": scenario.get("public_context", ""),
            "episode": scenario["episode"],
            "events": scenario.get("events", []),
            "success_conditions": scenario.get("success_conditions", []),
        },
        "primary_agent": {
            "id": primary["agent_id"],
            "persona": primary["persona"],
            "private_intention": primary["private_intention"],
            "start_location": primary["start_location"],
            "budget": primary["budget"],
            "memory_seeds": primary.get("memory_seeds", []),
        },
        "agent_type": result["agent_type"],
        "action_trace_without_validator_labels": compact_trace(result),
        "final_state_without_validator_labels": {
            "time": result["final_state"]["time"],
            "location": result["final_state"]["location"],
            "budget": result["final_state"]["budget"],
        },
    }


def clamp01(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return round(max(0.0, min(1.0, number)), 3)


def normalize_judgment(raw_judgment: Any, raw_response: str) -> dict[str, Any]:
    if not isinstance(raw_judgment, dict):
        raw_judgment = {}
    face = raw_judgment.get("face_plausibility")
    if face is None:
        face = raw_judgment.get("plan_plausibility")
    trace = raw_judgment.get("trace_believability")
    if trace is None:
        trace = raw_judgment.get("plan_plausibility")
    return {
        "face_plausibility": clamp01(face),
        "trace_believability": clamp01(trace),
        "rationale_alignment": clamp01(raw_judgment.get("rationale_alignment")),
        "urban_common_sense": clamp01(raw_judgment.get("urban_common_sense")),
        "main_issue": str(raw_judgment.get("main_issue", "parse_error") or "none")[:160],
        "brief_reason": str(raw_judgment.get("brief_reason", "") or "")[:400],
        "raw_response": raw_response,
    }


def judge_one(llm: Any, parse_response_json: Any, result: dict[str, Any], scenario: dict[str, Any]) -> dict[str, Any]:
    system = (
        "You are an independent evaluator for an urban-agent benchmark. "
        "Return exactly one JSON object. No markdown. "
        "Score strictly but fairly using the requested 0-1 fields."
    )
    user = json.dumps(build_prompt(result, scenario), ensure_ascii=False, indent=2)
    raw = llm.complete(system, user)
    parsed = parse_response_json(raw)
    return normalize_judgment(parsed, raw)


def aggregate_rows(rows: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    keys = [
        "judge_face_plausibility",
        "judge_trace_believability",
        "judge_rationale_alignment",
        "judge_urban_common_sense",
        "trace_feasibility",
        "face_feasibility_gap",
        "face_believability_gap",
        "goal_completion",
    ]
    aggregate: dict[str, dict[str, float]] = {}
    for agent_type in sorted({row["agent_type"] for row in rows}):
        agent_rows = [row for row in rows if row["agent_type"] == agent_type]
        aggregate[agent_type] = {}
        for key in keys:
            values = [float(row[key]) for row in agent_rows if row.get(key) not in {"", None}]
            if values:
                aggregate[agent_type][key] = round(sum(values) / len(values), 3)
    return aggregate


def result_key(result: dict[str, Any]) -> str:
    return f"{result['scenario_id']}::{result['agent_type']}"


def row_from_judged(judged: dict[str, Any]) -> dict[str, Any]:
    judgment = judged["plausibility_judgment"]
    metrics = judged["metrics"]
    return {
        "scenario_id": judged["scenario_id"],
        "agent_type": judged["agent_type"],
        "judge_face_plausibility": judgment["face_plausibility"],
        "judge_trace_believability": judgment["trace_believability"],
        "judge_rationale_alignment": judgment["rationale_alignment"],
        "judge_urban_common_sense": judgment["urban_common_sense"],
        "trace_feasibility": float(metrics["trace_feasibility"]),
        "face_feasibility_gap": judged["face_feasibility_gap"],
        "face_believability_gap": judged["face_believability_gap"],
        "goal_completion": metrics["goal_completion"],
        "impossible_trace_rate": metrics["impossible_trace_rate"],
        "main_issue": judgment["main_issue"],
        "brief_reason": judgment["brief_reason"],
    }


def load_existing_judgments(output_dir: Path) -> list[dict[str, Any]]:
    path = output_dir / "judged_traces.json"
    if not path.exists():
        return []
    existing = load_json(path)
    if not isinstance(existing, list):
        return []
    return [
        item for item in existing
        if isinstance(item, dict) and "plausibility_judgment" in item
    ]


def write_outputs(rows: list[dict[str, Any]], judged_results: list[dict[str, Any]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    write_json(output_dir / "judged_traces.json", judged_results)
    aggregate = aggregate_rows(rows)
    write_json(output_dir / "judge_aggregate.json", aggregate)

    fieldnames = [
        "scenario_id",
        "agent_type",
        "judge_face_plausibility",
        "judge_trace_believability",
        "judge_rationale_alignment",
        "judge_urban_common_sense",
        "trace_feasibility",
        "face_feasibility_gap",
        "face_believability_gap",
        "goal_completion",
        "impossible_trace_rate",
        "main_issue",
        "brief_reason",
    ]
    with (output_dir / "judge_summary.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    with (output_dir / "judge_summary.md").open("w", encoding="utf-8", newline="\n") as f:
        f.write("# CityIntent v0 Plausibility Judge Results\n\n")
        f.write("This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.\n\n")
        f.write("## Aggregate\n\n")
        f.write("| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |\n")
        f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|\n")
        for agent_type, metrics in aggregate.items():
            f.write(
                f"| {agent_type} | {metrics.get('judge_face_plausibility', '')} | "
                f"{metrics.get('trace_feasibility', '')} | "
                f"{metrics.get('face_feasibility_gap', '')} | "
                f"{metrics.get('judge_trace_believability', '')} | "
                f"{metrics.get('face_believability_gap', '')} | "
                f"{metrics.get('goal_completion', '')} | "
                f"{metrics.get('judge_rationale_alignment', '')} | "
                f"{metrics.get('judge_urban_common_sense', '')} |\n"
            )
        f.write("\n## Scenario-Level Rows\n\n")
        f.write("See `judge_summary.csv` and `judged_traces.json` in this directory.\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument(
        "--benchmark-config",
        type=Path,
        default=None,
        help="Optional benchmark config selecting a non-default scenario package.",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--llm-config", type=Path, required=True)
    parser.add_argument("--agents", default="", help="Optional comma-separated agent filter.")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--sleep", type=float, default=0.0)
    parser.add_argument("--no-resume", action="store_true", help="Ignore existing judged_traces.json in output-dir.")
    args = parser.parse_args()

    if str(STANDARD_LLM_DIR) not in sys.path:
        sys.path.insert(0, str(STANDARD_LLM_DIR))
    from llm_client import LLM, parse_response_json  # type: ignore

    llm = LLM(args.llm_config)
    scenarios = load_scenarios(args.benchmark_config)
    results = load_json(args.input)
    agent_filter = {item.strip() for item in args.agents.split(",") if item.strip()}
    if agent_filter:
        results = [result for result in results if result["agent_type"] in agent_filter]
    if args.limit is not None:
        results = results[: args.limit]

    judged_results: list[dict[str, Any]] = [] if args.no_resume else load_existing_judgments(args.output_dir)
    judged_by_key = {result_key(result): result for result in judged_results}
    rows: list[dict[str, Any]] = [row_from_judged(result) for result in judged_results]
    for index, result in enumerate(results, start=1):
        key = result_key(result)
        if key in judged_by_key:
            print(f"[{index}/{len(results)}] skipped {result['scenario_id']} / {result['agent_type']} (already judged)")
            continue
        scenario = scenarios[result["scenario_id"]]
        judgment = judge_one(llm, parse_response_json, result, scenario)
        metrics = result["metrics"]
        trace_feasibility = float(metrics["trace_feasibility"])
        face_feasibility_gap = round(max(0.0, judgment["face_plausibility"] - trace_feasibility), 3)
        face_believability_gap = round(max(0.0, judgment["face_plausibility"] - judgment["trace_believability"]), 3)
        row = {
            "scenario_id": result["scenario_id"],
            "agent_type": result["agent_type"],
            "judge_face_plausibility": judgment["face_plausibility"],
            "judge_trace_believability": judgment["trace_believability"],
            "judge_rationale_alignment": judgment["rationale_alignment"],
            "judge_urban_common_sense": judgment["urban_common_sense"],
            "trace_feasibility": trace_feasibility,
            "face_feasibility_gap": face_feasibility_gap,
            "face_believability_gap": face_believability_gap,
            "goal_completion": metrics["goal_completion"],
            "impossible_trace_rate": metrics["impossible_trace_rate"],
            "main_issue": judgment["main_issue"],
            "brief_reason": judgment["brief_reason"],
        }
        rows.append(row)
        judged = {
            **result,
            "plausibility_judgment": judgment,
            "face_feasibility_gap": face_feasibility_gap,
            "face_believability_gap": face_believability_gap,
        }
        judged_results.append(judged)
        judged_by_key[key] = judged
        write_outputs(rows, judged_results, args.output_dir)
        print(
            f"[{index}/{len(results)}] judged {result['scenario_id']} / {result['agent_type']}: "
            f"face={judgment['face_plausibility']} trace={judgment['trace_believability']}"
        )
        if args.sleep:
            time.sleep(args.sleep)

    write_outputs(rows, judged_results, args.output_dir)
    config = sanitized_config(args.llm_config)
    write_json(
        args.output_dir / "judge_manifest.json",
        {
            "schema_version": "cityintent_plausibility_judge_v1",
            "status": "complete",
            "evaluator_role": "soft_plausibility_only",
            "judge_provider": config.get("provider"),
            "judge_model": config.get("model"),
            "judge_config_path": str(args.llm_config),
            "judge_config": config,
            "judge_config_sha256": file_sha256(args.llm_config),
            "input_path": str(args.input),
            "input_sha256": file_sha256(args.input),
            "benchmark_config_path": str(args.benchmark_config.resolve()) if args.benchmark_config else None,
            "benchmark_config_sha256": file_sha256(args.benchmark_config.resolve()) if args.benchmark_config else None,
            "input_trace_count": len(results),
            "judged_trace_count": len(judged_results),
            "agent_filter": sorted(agent_filter),
            "limit": args.limit,
            "resume_enabled": not args.no_resume,
            "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        },
    )
    print(f"Wrote judged results to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
