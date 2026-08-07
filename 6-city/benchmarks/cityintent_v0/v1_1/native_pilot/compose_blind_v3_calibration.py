#!/usr/bin/env python3
"""Compose the final eight-construct blind-v3 calibration without rerunning unchanged items."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


UNCHANGED_FAMILIES = {
    "compound_long_horizon",
    "multi_party_commitment",
    "resource_budget_allocation",
    "time_window_scheduling",
}
HARDENED_FAMILIES = {
    "disruption_recovery",
    "memory_conditioned_preference",
    "poi_availability_service_evidence",
    "social_coordination_copresence",
}


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def model_id(row: dict[str, Any]) -> str:
    return str((row.get("model_info") or {}).get("model", "unknown"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--legacy-run-dir", action="append", type=Path, default=[])
    parser.add_argument("--hardened-run-dir", action="append", type=Path, default=[])
    parser.add_argument("--supplement-run-dir", action="append", type=Path, default=[])
    parser.add_argument("--base-run-dir", action="append", type=Path, default=[])
    parser.add_argument("--time-v4-run-dir", action="append", type=Path, default=[])
    parser.add_argument("--time-v7-run-dir", action="append", type=Path, default=[])
    parser.add_argument("--base-stable-run-dir", action="append", type=Path, default=[])
    parser.add_argument("--memory-v6-run-dir", action="append", type=Path, default=[])
    parser.add_argument("--poi-v5-run-dir", action="append", type=Path, default=[])
    parser.add_argument("--replacement-base-run-dir", action="append", type=Path, default=[])
    parser.add_argument("--family-replacement-run-dir", action="append", type=Path, default=[])
    parser.add_argument("--replace-family", action="append", default=[])
    parser.add_argument("--replacement-variant", type=int, choices=(0, 1, 2))
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    selected: list[dict[str, Any]] = []
    sources = []
    all_families = UNCHANGED_FAMILIES | HARDENED_FAMILIES
    replace_families = set(args.replace_family)
    if (args.replacement_base_run_dir or args.family_replacement_run_dir) and not replace_families:
        parser.error("--replace-family is required with generic family replacement inputs")
    unknown_replace_families = replace_families - all_families
    if unknown_replace_families:
        parser.error(f"unknown --replace-family values: {sorted(unknown_replace_families)}")
    source_groups = [
        ("legacy_unchanged", args.legacy_run_dir, UNCHANGED_FAMILIES),
        ("hardened_v3", args.hardened_run_dir, HARDENED_FAMILIES),
        ("supplement", args.supplement_run_dir, UNCHANGED_FAMILIES),
        (
            "base_without_time",
            args.base_run_dir,
            (UNCHANGED_FAMILIES | HARDENED_FAMILIES) - {"time_window_scheduling"},
        ),
        ("time_v4", args.time_v4_run_dir, {"time_window_scheduling"}),
        ("time_v7", args.time_v7_run_dir, {"time_window_scheduling"}),
        (
            "base_without_memory_poi",
            args.base_stable_run_dir,
            (UNCHANGED_FAMILIES | HARDENED_FAMILIES)
            - {"memory_conditioned_preference", "poi_availability_service_evidence"},
        ),
        ("memory_v6", args.memory_v6_run_dir, {"memory_conditioned_preference"}),
        ("poi_v5", args.poi_v5_run_dir, {"poi_availability_service_evidence"}),
        ("base_without_generic_replacements", args.replacement_base_run_dir, all_families - replace_families),
        ("generic_family_replacements", args.family_replacement_run_dir, replace_families),
    ]
    for role, directories, families in source_groups:
        for directory in directories:
            trace_path = directory.resolve() / "traces.json"
            rows = json.loads(trace_path.read_text(encoding="utf-8"))
            retained = [row for row in rows if row["family"] in families]
            if role in {"memory_v6", "poi_v5", "time_v7"} and args.replacement_variant is not None:
                suffix = f"_v{args.replacement_variant}"
                retained = [
                    row for row in retained if row["scenario_id"].endswith(suffix)
                ]
            selected.extend(retained)
            sources.append({
                "role": role,
                "run_dir": str(directory.resolve()),
                "traces_sha256": file_sha256(trace_path),
                "input_count": len(rows),
                "retained_count": len(retained),
                "families": sorted(families),
            })

    keys = [(model_id(row), row["agent_type"], row["scenario_id"]) for row in selected]
    duplicates = [key for key, count in Counter(keys).items() if count > 1]
    if duplicates:
        raise SystemExit(f"duplicate system-item traces: {duplicates}")
    scenario_counts = Counter(row["scenario_id"] for row in selected)
    incomplete = {key: value for key, value in scenario_counts.items() if value != 6}
    if len(selected) != 48 or len(scenario_counts) != 8 or incomplete:
        raise SystemExit(
            f"incomplete composite: traces={len(selected)}, items={len(scenario_counts)}, "
            f"non_six_system_items={incomplete}"
        )

    selected.sort(key=lambda row: (row["scenario_id"], model_id(row), row["agent_type"]))
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    trace_path = output / "traces.json"
    trace_path.write_text(
        json.dumps(selected, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    manifest = {
        "schema_version": "cityintent_blind_v3_composite_v1",
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "status": "complete",
        "composition_rule": {
            "unchanged_families_from": "blind_v1",
            "hardened_families_from": "hardened_v3",
            "missing_deepseek_time_from": "supplement",
            "optional_v4_rule": "base composite excluding time plus v4 time replacement",
            "optional_v6_rule": "base excluding memory/POI plus v6 memory and v5 POI replacements",
            "optional_v7_rule": "base excluding time plus time-v7 replacement for one public variant",
            "generic_replacement_rule": "base excluding --replace-family plus replacement archives",
        },
        "trace_count": len(selected),
        "scenario_count": len(scenario_counts),
        "systems_per_scenario": dict(sorted(scenario_counts.items())),
        "models": sorted({model_id(row) for row in selected}),
        "agents": sorted({row["agent_type"] for row in selected}),
        "sources": sources,
        "composite_traces_sha256": file_sha256(trace_path),
    }
    (output / "composition_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"traces": len(selected), "scenarios": len(scenario_counts)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
