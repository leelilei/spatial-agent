#!/usr/bin/env python3
"""Generate the first cross-topology expansion wave from hardened v6 templates.

This is an oracle-first 40-item candidate pool (8 constructs x 5 worlds), not
the 144-item release matrix.  The first two public-world variants exactly
preserve the calibrated pilot allocation; one new public and two private-world
instances are added per construct.
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
V1_ROOT = ROOT.parent
OUTPUT_ROOT = ROOT / "expansion_wave1"
GENERATOR_VERSION = "cityintent-native-expansion-6.1.0"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import generate_native_pilot as pilot  # noqa: E402


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_hash(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def generate(output_root: Path = OUTPUT_ROOT) -> dict[str, Any]:
    output_root = output_root.resolve()
    public_worlds = [
        load_json(path) for path in sorted((V1_ROOT / "worlds" / "public").glob("*.json"))
    ]
    private_worlds = [
        load_json(path) for path in sorted((V1_ROOT / "worlds" / "private").glob("*.json"))
    ]
    if len(public_worlds) != 3 or len(private_worlds) != 2:
        raise RuntimeError("expansion wave requires exactly three public and two private worlds")

    scenarios: list[dict[str, Any]] = []
    plans: list[dict[str, Any]] = []
    for construct_index, construct in enumerate(pilot.CONSTRUCTS):
        rotated_public = [
            public_worlds[(construct_index + variant) % len(public_worlds)]
            for variant in range(len(public_worlds))
        ]
        for variant, world in enumerate(rotated_public + private_worlds):
            scenario, plan = pilot.build_item(world, construct, variant)
            metadata = scenario["benchmark_metadata"]
            metadata.update({
                "benchmark_version": "1.1.0-expansion-wave1",
                "candidate_status": "oracle_gate_pending",
                "split": "calibration_expansion",
                "difficulty_tier": ("medium", "hard", "hard", "medium", "hard")[variant],
                "generator_version": GENERATOR_VERSION,
                "parent_generator_version": "cityintent-native-pilot-6.0.0",
                "world_visibility": world["release_visibility"],
            })
            scenarios.append(scenario)
            plans.append(plan)

    scenario_ids = [scenario["scenario_id"] for scenario in scenarios]
    if len(scenario_ids) != len(set(scenario_ids)):
        raise RuntimeError("duplicate scenario id in expansion wave")
    payload_hashes = [canonical_hash(scenario) for scenario in scenarios]
    if len(payload_hashes) != len(set(payload_hashes)):
        raise RuntimeError("duplicate normalized scenario payload in expansion wave")

    scenario_dir = output_root / "scenarios"
    scenario_dir.mkdir(parents=True, exist_ok=True)
    expected_paths = set()
    for scenario in scenarios:
        path = scenario_dir / f"{scenario['scenario_id']}.json"
        expected_paths.add(path)
        path.write_text(json.dumps(scenario, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    stale = set(scenario_dir.glob("*.json")) - expected_paths
    if stale:
        raise RuntimeError(f"stale scenario files must be removed explicitly: {sorted(stale)}")

    plans_path = output_root / "oracle_negative_plans.json"
    plans_path.write_text(json.dumps(plans, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    world_paths = [
        str(path.resolve().relative_to(output_root, walk_up=True))
        for path in sorted((V1_ROOT / "worlds" / "public").glob("*.json"))
    ] + [
        str(path.resolve().relative_to(output_root, walk_up=True))
        for path in sorted((V1_ROOT / "worlds" / "private").glob("*.json"))
    ]
    config = {
        "benchmark_id": "cityintent_v1_1_native_expansion_wave1",
        "version": "1.1.0-expansion-wave1",
        "status": "oracle_gate_pending_candidate",
        "worlds": world_paths,
        "scenario_dir": "scenarios",
        "agents_under_test": [{"id": agent_id} for agent_id in (
            "utility_planner", "llm_direct_actor", "reactive_replanner", "memory_reflection"
        )],
        "metrics": [{"id": metric} for metric in pilot.METRICS],
        "validation": {
            "min_scenarios": len(scenarios),
            "required_agent_ids": [
                "utility_planner", "llm_direct_actor", "reactive_replanner", "memory_reflection"
            ],
            "required_metric_ids": [
                "task_completion", "constraint_satisfaction", "goal_completion",
                "feasibility_violation", "travel_efficiency", "budget_consistency",
                "intention_consistency",
            ],
        },
    }
    config_path = output_root / "benchmark_config.json"
    config_path.write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    manifest = {
        "schema_version": "cityintent_native_expansion_manifest_v1",
        "generator_version": GENERATOR_VERSION,
        "status": "oracle_gate_pending_candidate_not_release",
        "scenario_count": len(scenarios),
        "construct_counts": dict(sorted(Counter(s["family"] for s in scenarios).items())),
        "world_counts": dict(sorted(Counter(s["world_id"] for s in scenarios).items())),
        "visibility_counts": dict(sorted(Counter(
            s["benchmark_metadata"]["world_visibility"] for s in scenarios
        ).items())),
        "scenario_ids": sorted(scenario_ids),
        "scenario_matrix_sha256": hashlib.sha256("\n".join(sorted(payload_hashes)).encode()).hexdigest(),
    }
    (output_root / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return manifest


if __name__ == "__main__":
    result = generate()
    print(json.dumps({
        "scenario_count": result["scenario_count"],
        "construct_counts": result["construct_counts"],
        "world_counts": result["world_counts"],
        "status": result["status"],
    }, sort_keys=True))
