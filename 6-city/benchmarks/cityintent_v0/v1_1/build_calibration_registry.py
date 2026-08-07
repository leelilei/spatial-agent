#!/usr/bin/env python3
"""Build the audited public calibration-template registry.

Calibration evidence is deliberately separate from release acceptance. Passing
this registry never increments the 144-item release benchmark count.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCES = (
    (
        ROOT / "native_pilot" / "time_v7" / "public_cross_variant_promotion_manifest.json",
        ROOT / "native_pilot" / "time_v7" / "public_matrix" / "scenarios",
    ),
    (
        ROOT / "native_pilot" / "expansion_wave2" / "public_cross_variant_promotion_manifest.json",
        ROOT / "native_pilot" / "expansion_wave2" / "scenarios",
    ),
    (
        ROOT / "native_pilot" / "expansion_wave3" / "public_cross_variant_promotion_manifest.json",
        ROOT / "native_pilot" / "expansion_wave3" / "scenarios",
    ),
)
DEFAULT_OUTPUT = ROOT / "manifests" / "calibration_template_registry.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path.resolve())


def build_registry(
    sources: tuple[tuple[Path, Path], ...] = DEFAULT_SOURCES,
) -> dict[str, Any]:
    release_spec = load_json(ROOT / "release_spec.json")
    required_constructs = set(
        release_spec["scenarios"]["required_constructs"]
    )

    errors: list[str] = []
    templates = []
    scenario_ids: set[str] = set()
    scenario_hashes: set[str] = set()
    source_records = []
    for promotion_path, scenario_dir in sources:
        promotion_path = promotion_path.resolve()
        scenario_dir = scenario_dir.resolve()
        promotion = load_json(promotion_path)
        if promotion.get("status") != "calibration_template_pool_not_release":
            errors.append(f"invalid promotion status: {promotion_path}")
        if promotion.get("accepted_template_count") != len(required_constructs):
            errors.append(f"incomplete template source: {promotion_path}")
        if promotion.get("accepted_item_count") != 24:
            errors.append(f"incomplete instance source: {promotion_path}")
        source_records.append({
            "path": relative_path(promotion_path),
            "sha256": sha256(promotion_path),
        })
        for decision in promotion.get("decisions", []):
            construct = decision["construct"]
            if decision["decision"] != "calibration_template_accepted":
                errors.append(f"template is not accepted: {construct}")
            if construct not in required_constructs:
                errors.append(f"unknown construct: {construct}")
            if len(decision["items"]) != 3:
                errors.append(f"template does not have three public variants: {construct}")
            instances = []
            template_id = None
            for item in decision["items"]:
                scenario_id = item["scenario_id"]
                scenario_path = scenario_dir / f"{scenario_id}.json"
                if not scenario_path.exists():
                    errors.append(f"missing scenario: {scenario_id}")
                    continue
                scenario = load_json(scenario_path)
                metadata = scenario.get("benchmark_metadata", {})
                template_id = metadata.get("template_id")
                actual_hash = sha256(scenario_path)
                if item["decision"] != "accepted":
                    errors.append(f"instance is not accepted: {scenario_id}")
                if actual_hash != item["scenario_sha256"]:
                    errors.append(f"scenario hash drift: {scenario_id}")
                if metadata.get("world_visibility") != "public":
                    errors.append(f"non-public calibration instance: {scenario_id}")
                if metadata.get("split") not in {"calibration_public", "calibration_expansion"}:
                    errors.append(f"unexpected calibration split: {scenario_id}")
                if scenario.get("family") != construct:
                    errors.append(f"construct mismatch: {scenario_id}")
                if scenario_id in scenario_ids:
                    errors.append(f"duplicate scenario id: {scenario_id}")
                if actual_hash in scenario_hashes:
                    errors.append(f"duplicate scenario hash: {scenario_id}")
                scenario_ids.add(scenario_id)
                scenario_hashes.add(actual_hash)
                instances.append({
                    "variant": item["variant"],
                    "scenario_id": scenario_id,
                    "world_id": scenario["world_id"],
                    "generator_version": metadata["generator_version"],
                    "scenario_sha256": actual_hash,
                    "oracle_task_completion": item["oracle_task_completion"],
                    "matched_negative_headroom": item["matched_negative_headroom"],
                    "systems_observed": item["systems_observed"],
                    "mean_task": item["mean_task"],
                    "range": item["range"],
                    "corrected_item_total_correlation": item[
                        "corrected_item_total_correlation"
                    ],
                })
            templates.append({
                "construct": construct,
                "template_id": template_id,
                "status": "calibration_template_accepted",
                "source_manifest": relative_path(promotion_path),
                "public_instances": sorted(instances, key=lambda row: row["variant"]),
            })

    observed_constructs = {row["construct"] for row in templates}
    if observed_constructs != required_constructs:
        errors.append("registry construct set does not match release specification")
    expected_templates = len(sources) * len(required_constructs)
    expected_instances = expected_templates * 3
    if len(templates) != expected_templates:
        errors.append(f"registry does not contain {expected_templates} mechanism templates")
    if len(scenario_ids) != expected_instances:
        errors.append(f"registry does not contain {expected_instances} unique public instances")
    if errors:
        raise ValueError("; ".join(errors))

    templates_per_construct = Counter(row["construct"] for row in templates)
    instances_per_construct = Counter(
        template["construct"]
        for template in templates
        for row in template["public_instances"]
    )
    planned_public_templates_per_construct = 4
    return {
        "schema_version": "cityintent_calibration_template_registry_v1",
        "benchmark_version": release_spec["target_version"],
        "status": "calibration_template_pool_not_release",
        "evidence_scope": "public_world_calibration_only",
        "release_target": release_spec["scenarios"]["minimum_total"],
        "release_accepted_count": 0,
        "calibration_template_count": len(templates),
        "calibration_public_instance_count": len(scenario_ids),
        "source_promotion_manifests": source_records,
        "thresholds": promotion["thresholds"],
        "construction_gap": {
            "planned_public_mechanism_templates_per_construct": (
                planned_public_templates_per_construct
            ),
            "planned_public_instances_per_construct": 12,
            "planned_private_instances_per_construct": 6,
            "private_transfer_templates_required_per_construct": 3,
            "calibrated_public_templates_per_construct": dict(
                sorted(templates_per_construct.items())
            ),
            "calibrated_public_instances_per_construct": dict(
                sorted(instances_per_construct.items())
            ),
            "remaining_public_templates_per_construct": {
                construct: planned_public_templates_per_construct - count
                for construct, count in sorted(templates_per_construct.items())
            },
            "remaining_public_instances_per_construct": {
                construct: 12 - instances_per_construct[construct]
                for construct in sorted(required_constructs)
            },
            "next_required_waves": ["wave4"],
        },
        "templates": sorted(templates, key=lambda row: row["construct"]),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    registry = build_registry()
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(registry, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "status": registry["status"],
        "calibration_templates": registry["calibration_template_count"],
        "calibration_public_instances": registry[
            "calibration_public_instance_count"
        ],
        "release_accepted": registry["release_accepted_count"],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
