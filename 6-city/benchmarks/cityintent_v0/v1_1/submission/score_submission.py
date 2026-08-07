#!/usr/bin/env python3
"""Strict standalone scorer for CityIntent v1.1 JSONL submissions."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LOCAL_RUNNER_PATH = Path(__file__).resolve().parent / "_runtime" / "run_baseline_traces.py"
RUNNER_PATH = LOCAL_RUNNER_PATH if LOCAL_RUNNER_PATH.exists() else ROOT.parent / "tools" / "run_baseline_traces.py"
SPEC = importlib.util.spec_from_file_location("cityintent_runner_for_scorer", RUNNER_PATH)
assert SPEC and SPEC.loader
runner = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = runner
SPEC.loader.exec_module(runner)

ALLOWED_TOP_LEVEL = {
    "scenario_id", "benchmark_version", "split_hash", "system", "actor_model",
    "provider", "action_interface", "telemetry", "disclosure", "actions",
}
REQUIRED_TOP_LEVEL = ALLOWED_TOP_LEVEL
ALLOWED_ACTION_FIELDS = {
    "kind", "target", "path", "minutes", "to", "content", "item", "service", "query", "reason"
}
ALLOWED_ACTION_KINDS = {
    "recall", "move", "enter", "use_service", "buy", "dwell", "message", "interact", "finish", "abandon"
}


class SubmissionError(ValueError):
    pass


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SubmissionError(f"line {line_number}: malformed JSON: {exc}") from exc
        if not isinstance(row, dict):
            raise SubmissionError(f"line {line_number}: episode must be an object")
        rows.append(row)
    return rows


def validate_episode_contract(row: dict[str, Any], scenario: dict[str, Any], split_hash: str) -> None:
    unknown = sorted(set(row) - ALLOWED_TOP_LEVEL)
    missing = sorted(REQUIRED_TOP_LEVEL - set(row))
    if unknown:
        raise SubmissionError(f"{scenario['scenario_id']}: forbidden or unknown fields {unknown}")
    if missing:
        raise SubmissionError(f"{scenario['scenario_id']}: missing fields {missing}")
    if row["benchmark_version"] != "1.1.0":
        raise SubmissionError(f"{scenario['scenario_id']}: benchmark version mismatch")
    if row["split_hash"] != split_hash:
        raise SubmissionError(f"{scenario['scenario_id']}: split hash mismatch")
    actions = row["actions"]
    if not isinstance(actions, list):
        raise SubmissionError(f"{scenario['scenario_id']}: actions must be a list")
    if len(actions) > int(scenario["episode"]["max_steps"]):
        raise SubmissionError(f"{scenario['scenario_id']}: action budget exceeded")
    for index, action in enumerate(actions, 1):
        if not isinstance(action, dict):
            raise SubmissionError(f"{scenario['scenario_id']} action {index}: must be an object")
        extra = sorted(set(action) - ALLOWED_ACTION_FIELDS)
        if extra:
            raise SubmissionError(f"{scenario['scenario_id']} action {index}: unknown fields {extra}")
        if action.get("kind") not in ALLOWED_ACTION_KINDS:
            raise SubmissionError(f"{scenario['scenario_id']} action {index}: unknown action kind")
        if action.get("minutes", 0) < 0:
            raise SubmissionError(f"{scenario['scenario_id']} action {index}: negative minutes")


def replay_episode(world: Any, scenario: dict[str, Any], actions: list[dict[str, Any]]) -> dict[str, Any]:
    primary = next(agent for agent in scenario["agents"] if agent["agent_id"] == scenario["primary_agent"])
    state = runner.TraceState(
        scenario_id=scenario["scenario_id"],
        agent_id=primary["agent_id"],
        agent_type="submission",
        time=runner.parse_time(scenario["episode"]["start_time"]),
        end_time=runner.parse_time(scenario["episode"]["end_time"]),
        location=primary["start_location"],
        budget=float(primary["budget"]),
    )
    state.inside_location = state.location
    runner.record_visit(state, state.location, state.time, kind="start")
    runner.record_entry(state, state.location, state.time, kind="start")
    terminated = False
    for index, payload in enumerate(actions, 1):
        if terminated or state.time >= state.end_time:
            raise SubmissionError(f"{scenario['scenario_id']}: post-termination action at index {index}")
        action = runner.Action(**payload)
        runner.execute_action(world, scenario, state, action)
        terminated = action.kind in {"finish", "abandon"}
    scored = runner.score_trace(world, scenario, state)
    return {
        "scenario_id": scenario["scenario_id"],
        "world_id": scenario["world_id"],
        "construct_family": scenario["benchmark_metadata"]["construct_family"],
        "metrics": scored["metrics"],
        "failure_taxonomy": scored["failure_taxonomy"],
        "final_state": scored["final_state"],
    }


def macro_verified_completion(episodes: list[dict[str, Any]]) -> float:
    cells: dict[tuple[str, str], list[float]] = defaultdict(list)
    for item in episodes:
        key = (item["construct_family"], item["world_id"])
        cells[key].append(float(item["metrics"]["task_completion"]))
    cell_means = [sum(values) / len(values) for values in cells.values()]
    return round(sum(cell_means) / len(cell_means), 6) if cell_means else 0.0


def score_submission(root: Path, submission_path: Path, split: str) -> dict[str, Any]:
    manifest = load_json(root / "manifests" / "scenarios_manifest.json")
    if split not in manifest["split_hashes"]:
        raise SubmissionError(f"unknown split: {split}")
    split_hash = manifest["split_hashes"][split]
    scenarios = {
        item["scenario_id"]: item
        for item in (load_json(path) for path in sorted((root / "scenarios" / split).glob("*.json")))
    }
    rows = load_jsonl(submission_path)
    submitted_ids = [row.get("scenario_id") for row in rows]
    if len(submitted_ids) != len(set(submitted_ids)):
        raise SubmissionError("duplicate submitted scenario ids")
    missing = sorted(set(scenarios) - set(submitted_ids))
    extra = sorted(set(submitted_ids) - set(scenarios))
    if missing or extra:
        raise SubmissionError(f"episode set mismatch: missing={missing}, extra={extra}")

    config = load_json(root / "benchmark_config.json")
    worlds = runner.load_worlds(config, root)
    episodes = []
    for row in rows:
        scenario = scenarios[row["scenario_id"]]
        validate_episode_contract(row, scenario, split_hash)
        episodes.append(replay_episode(worlds[scenario["world_id"]], scenario, row["actions"]))
    metric_names = ("task_completion", "constraint_satisfaction", "trace_feasibility", "intention_consistency", "social_appropriateness")
    means = {
        metric: round(sum(float(item["metrics"][metric]) for item in episodes) / len(episodes), 6)
        for metric in metric_names
    }
    return {
        "schema_version": "cityintent_score_report_v1",
        "benchmark_version": "1.1.0",
        "split": split,
        "split_hash": split_hash,
        "episode_count": len(episodes),
        "official_ranking_metric": "macro_verified_task_completion",
        "macro_verified_task_completion": macro_verified_completion(episodes),
        "micro_metric_means": means,
        "episodes": episodes,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--submission", type=Path, required=True)
    parser.add_argument("--split", choices=("examples", "development", "public_test", "private_test"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = score_submission(args.root.resolve(), args.submission.resolve(), args.split)
    except SubmissionError as exc:
        raise SystemExit(f"submission rejected: {exc}") from exc
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"episode_count": report["episode_count"], "macro_verified_task_completion": report["macro_verified_task_completion"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
