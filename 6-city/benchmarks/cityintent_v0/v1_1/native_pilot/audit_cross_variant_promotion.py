#!/usr/bin/env python3
"""Audit native calibration templates across independently generated variants.

An item is not sufficient evidence for promoting a generator template.  This
gate accepts a construct only when every supplied variant independently passes
the oracle, coverage, difficulty, discrimination, and item-total checks.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


THRESHOLDS = {
    "required_variants": 2,
    "required_systems_per_variant": 6,
    "min_range": 0.15,
    "min_corrected_item_total_correlation": 0.20,
    "min_mean_task": 0.20,
    "max_mean_task": 0.90,
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def variant_id(scenario_id: str) -> str:
    match = re.search(r"_v(\d+)$", scenario_id)
    if not match:
        raise ValueError(f"scenario id has no terminal variant suffix: {scenario_id}")
    return f"v{match.group(1)}"


def item_reasons(item: dict[str, Any], oracle_row: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    if not oracle_row["passed"]:
        reasons.append("two_sided_oracle_gate_failed")
    if item["systems_observed"] != THRESHOLDS["required_systems_per_variant"]:
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
    return reasons


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--analysis", type=Path, action="append", required=True)
    parser.add_argument("--oracle-report", type=Path, required=True)
    parser.add_argument("--scenario-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if len(args.analysis) < THRESHOLDS["required_variants"]:
        parser.error(
            f"at least {THRESHOLDS['required_variants']} --analysis inputs are required"
        )

    analysis_paths = [path.resolve() for path in args.analysis]
    oracle_path = args.oracle_report.resolve()
    scenario_dir = args.scenario_dir.resolve()
    oracle = {row["scenario_id"]: row for row in load_json(oracle_path)["results"]}

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    seen_scenarios: set[str] = set()
    for analysis_path in analysis_paths:
        analysis = load_json(analysis_path)
        if not analysis["coverage_complete"]:
            raise ValueError(f"analysis coverage is incomplete: {analysis_path}")
        for item in analysis["item_analysis"]:
            scenario_id = item["scenario_id"]
            if scenario_id in seen_scenarios:
                raise ValueError(f"duplicate scenario across analyses: {scenario_id}")
            seen_scenarios.add(scenario_id)
            grouped[item["construct"]].append(item)

    decisions = []
    for construct, items in sorted(grouped.items()):
        rows = []
        template_reasons: list[str] = []
        observed_variants = {variant_id(item["scenario_id"]) for item in items}
        if len(observed_variants) < THRESHOLDS["required_variants"]:
            template_reasons.append("insufficient_independent_variants")
        if len(items) != len(observed_variants):
            template_reasons.append("duplicate_variant_for_construct")

        for item in sorted(items, key=lambda row: variant_id(row["scenario_id"])):
            scenario_id = item["scenario_id"]
            if scenario_id not in oracle:
                raise KeyError(f"scenario absent from oracle report: {scenario_id}")
            scenario_path = scenario_dir / f"{scenario_id}.json"
            if not scenario_path.exists():
                raise FileNotFoundError(scenario_path)
            reasons = item_reasons(item, oracle[scenario_id])
            if reasons:
                template_reasons.append(f"{variant_id(scenario_id)}_failed_item_gate")
            rows.append({
                "variant": variant_id(scenario_id),
                "scenario_id": scenario_id,
                "decision": "accepted" if not reasons else "rejected",
                "reasons": reasons,
                "oracle_task_completion": oracle[scenario_id]["oracle_task_completion"],
                "matched_negative_headroom": oracle[scenario_id]["headroom"],
                "systems_observed": item["systems_observed"],
                "mean_task": item["mean_task"],
                "range": item["range"],
                "corrected_item_total_correlation": item[
                    "corrected_item_total_correlation"
                ],
                "scenario_sha256": sha256(scenario_path),
            })

        template_reasons = sorted(set(template_reasons))
        decisions.append({
            "construct": construct,
            "decision": "calibration_template_accepted" if not template_reasons else "rejected",
            "reasons": template_reasons,
            "variants_observed": sorted(observed_variants),
            "items": rows,
        })

    accepted = [
        row for row in decisions if row["decision"] == "calibration_template_accepted"
    ]
    accepted_item_count = sum(len(row["items"]) for row in accepted)
    report = {
        "schema_version": "cityintent_cross_variant_promotion_v1",
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "status": "calibration_template_pool_not_release",
        "thresholds": THRESHOLDS,
        "analysis_inputs": [
            {"path": str(path), "sha256": sha256(path)} for path in analysis_paths
        ],
        "oracle_report_path": str(oracle_path),
        "oracle_report_sha256": sha256(oracle_path),
        "accepted_template_count": len(accepted),
        "evaluated_template_count": len(decisions),
        "accepted_item_count": accepted_item_count,
        "evaluated_item_count": sum(len(row["items"]) for row in decisions),
        "release_target": 144,
        "decisions": decisions,
    }
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "accepted_templates": len(accepted),
        "evaluated_templates": len(decisions),
        "accepted_items": accepted_item_count,
        "status": report["status"],
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
