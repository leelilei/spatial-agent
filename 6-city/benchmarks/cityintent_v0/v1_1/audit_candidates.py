#!/usr/bin/env python3
"""Audit v1.1 candidate splits, leakage, and baseline discrimination."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_strings(value: Any):
    if isinstance(value, dict):
        for item in value.values():
            yield from iter_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from iter_strings(item)
    elif isinstance(value, str):
        yield value


def payload_hash(scenario: dict[str, Any]) -> str:
    payload = {
        key: value
        for key, value in scenario.items()
        if key not in {"scenario_id", "benchmark_metadata"}
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def audit(root: Path, traces_path: Path | None = None, oracle_path: Path | None = None) -> dict[str, Any]:
    manifest = load_json(root / "manifests" / "scenarios_manifest.json")
    scenarios = [
        load_json(path) for path in sorted((root / "scenarios").rglob("*.json"))
    ]
    private_worlds = [load_json(path) for path in sorted((root / "worlds" / "private").glob("*.json"))]
    private_tokens = {world["world_id"] for world in private_worlds}
    private_tokens.update(location["id"] for world in private_worlds for location in world["locations"])

    ids = [item["scenario_id"] for item in scenarios]
    seeds = [item["benchmark_metadata"]["seed"] for item in scenarios]
    hashes = [payload_hash(item) for item in scenarios]
    errors: list[str] = []
    if len(scenarios) != manifest["candidate_count"]:
        errors.append("scenario file count does not match manifest")
    if len(ids) != len(set(ids)):
        errors.append("duplicate scenario ids")
    if len(seeds) != len(set(seeds)):
        errors.append("duplicate generator seeds")
    if len(hashes) != len(set(hashes)):
        errors.append("duplicate normalized scenario payloads")

    leakage_items = []
    for item in scenarios:
        metadata = item["benchmark_metadata"]
        is_private = metadata["split"] == "private_test"
        if is_private != (metadata["world_visibility"] == "private"):
            leakage_items.append(item["scenario_id"])
            continue
        if not is_private:
            strings = set(iter_strings(item))
            if strings.intersection(private_tokens):
                leakage_items.append(item["scenario_id"])
    if leakage_items:
        errors.append(f"private asset leakage in {len(leakage_items)} public items")

    baseline_rows: dict[str, list[dict[str, Any]]] = defaultdict(list)
    if traces_path is not None:
        for row in load_json(traces_path):
            baseline_rows[row["scenario_id"]].append(row)
    oracle_rows = {}
    if oracle_path is not None:
        oracle_rows = {item["scenario_id"]: item for item in load_json(oracle_path)["results"]}

    dispositions = []
    reason_counts: Counter[str] = Counter()
    for item in scenarios:
        scenario_id = item["scenario_id"]
        reasons = []
        oracle = oracle_rows.get(scenario_id)
        if oracle is None:
            reasons.append("oracle_not_run")
            reasons.append("mechanism_matched_negative_control_not_run")
        else:
            if not oracle["oracle_passed"]:
                reasons.append("oracle_failed")
            if not oracle["negative_control_available"]:
                reasons.append("mechanism_matched_negative_control_not_run")
            elif not oracle["negative_control_passed"]:
                reasons.append("negative_control_headroom_failed")
        rows = baseline_rows.get(scenario_id, [])
        task_scores = [float(row["metrics"]["task_completion"]) for row in rows]
        if rows:
            if min(task_scores) >= 0.95:
                reasons.append("baseline_ceiling")
            if max(task_scores) <= 0.05:
                reasons.append("baseline_floor")
            if max(task_scores) - min(task_scores) < 0.15:
                reasons.append("insufficient_provisional_baseline_headroom")
        else:
            reasons.append("baseline_screen_not_run")
        if scenario_id in leakage_items:
            reasons.append("private_asset_leakage")
        for reason in reasons:
            reason_counts[reason] += 1
        dispositions.append(
            {
                "scenario_id": scenario_id,
                "status": "passes_current_automated_gates" if not reasons else "blocked_from_acceptance",
                "reasons": reasons,
                "baseline_task_min": min(task_scores) if task_scores else None,
                "baseline_task_max": max(task_scores) if task_scores else None,
                "baseline_task_range": round(max(task_scores) - min(task_scores), 6) if task_scores else None,
            }
        )

    current_gate_pass_count = sum(not item["reasons"] for item in dispositions)
    return {
        "schema_version": "cityintent_candidate_audit_v1",
        "benchmark_version": "1.1.0-candidate",
        "machine_audit_passed": not errors,
        "machine_errors": errors,
        "candidate_count": len(scenarios),
        "accepted_count": 0,
        "current_automated_gate_pass_count": current_gate_pass_count,
        "acceptance_blocked_count": len(dispositions),
        "reason_counts": dict(sorted(reason_counts.items())),
        "private_leakage_count": len(leakage_items),
        "dispositions": dispositions,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--traces", type=Path)
    parser.add_argument("--oracle-evidence", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve() if args.output else root / "manifests" / "candidate_audit.json"
    report = audit(
        root,
        args.traces.resolve() if args.traces else None,
        args.oracle_evidence.resolve() if args.oracle_evidence else None,
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    rejection_path = root / "rejection_logs" / "candidate_acceptance_blockers.jsonl"
    rejection_path.parent.mkdir(parents=True, exist_ok=True)
    rejection_path.write_text(
        "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in report["dispositions"]),
        encoding="utf-8",
    )
    print(json.dumps({key: report[key] for key in ("machine_audit_passed", "candidate_count", "accepted_count", "reason_counts")}, sort_keys=True))
    return 0 if report["machine_audit_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
