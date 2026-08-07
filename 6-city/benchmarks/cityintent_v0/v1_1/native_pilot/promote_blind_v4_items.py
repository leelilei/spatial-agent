#!/usr/bin/env python3
"""Promote empirically calibrated native items into the accepted seed pool."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any


THRESHOLDS = {
    "required_systems": 6,
    "min_range": 0.15,
    "min_corrected_item_total_correlation": 0.20,
    "min_mean_task": 0.20,
    "max_mean_task": 0.90,
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--analysis", type=Path, required=True)
    parser.add_argument("--oracle-report", type=Path, required=True)
    parser.add_argument("--scenario-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    analysis_path = args.analysis.resolve()
    oracle_path = args.oracle_report.resolve()
    analysis = load_json(analysis_path)
    oracle = {
        row["scenario_id"]: row
        for row in load_json(oracle_path)["results"]
    }
    decisions = []
    for item in analysis["item_analysis"]:
        scenario_id = item["scenario_id"]
        oracle_row = oracle[scenario_id]
        reasons = []
        if not oracle_row["passed"]:
            reasons.append("two_sided_oracle_gate_failed")
        if item["systems_observed"] != THRESHOLDS["required_systems"]:
            reasons.append("incomplete_system_coverage")
        if item["range"] < THRESHOLDS["min_range"]:
            reasons.append("insufficient_range")
        correlation = item["corrected_item_total_correlation"]
        if correlation is None or correlation < THRESHOLDS["min_corrected_item_total_correlation"]:
            reasons.append("weak_or_negative_item_total")
        if not THRESHOLDS["min_mean_task"] <= item["mean_task"] <= THRESHOLDS["max_mean_task"]:
            reasons.append("difficulty_outside_acceptance_band")
        if item["all_observed_ceiling"] or item["all_observed_floor"]:
            reasons.append("ceiling_or_floor")
        scenario_path = args.scenario_dir.resolve() / f"{scenario_id}.json"
        decisions.append({
            "scenario_id": scenario_id,
            "construct": item["construct"],
            "decision": "calibration_accepted" if not reasons else "rejected",
            "reasons": reasons,
            "oracle_task_completion": oracle_row["oracle_task_completion"],
            "matched_negative_headroom": oracle_row["headroom"],
            "systems_observed": item["systems_observed"],
            "mean_task": item["mean_task"],
            "range": item["range"],
            "corrected_item_total_correlation": correlation,
            "scenario_sha256": sha256(scenario_path),
        })

    accepted = [row for row in decisions if row["decision"] == "calibration_accepted"]
    report = {
        "schema_version": "cityintent_item_promotion_v1",
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "status": "calibration_seed_pool_not_release",
        "thresholds": THRESHOLDS,
        "analysis_path": str(analysis_path),
        "analysis_sha256": sha256(analysis_path),
        "oracle_report_path": str(oracle_path),
        "oracle_report_sha256": sha256(oracle_path),
        "accepted_count": len(accepted),
        "evaluated_count": len(decisions),
        "release_target": 144,
        "decisions": decisions,
    }
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "accepted": len(accepted),
        "evaluated": len(decisions),
        "status": report["status"],
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
