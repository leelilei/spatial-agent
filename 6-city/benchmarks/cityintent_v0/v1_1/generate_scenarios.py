#!/usr/bin/env python3
"""Generate the 144-item CityIntent v1.1 candidate scenario matrix.

Items produced here are candidates, not accepted benchmark items. Oracle,
negative-control, leakage, and empirical discrimination gates promote them.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
V0_ROOT = ROOT.parent
TEMPLATE_ROOT = ROOT / "templates" if (ROOT / "templates").exists() else V0_ROOT
GENERATOR_VERSION = "cityintent-scenariogen-1.0.0"

CONSTRUCT_TEMPLATES = {
    "disruption_recovery": [
        "commute_disruption", "detour_commute_midroute_block", "paired_commute_b", "paired_pickup_b"
    ],
    "time_window_scheduling": [
        "lunch_meeting_time_pressure", "school_pickup_social_detour", "hard_deadline_then_meet", "paired_pickup_a"
    ],
    "resource_budget_allocation": [
        "budget_errand_chain", "hard_budget_entangled_meet", "hard_full_evening_chain", "social_copresence_with_errand"
    ],
    "poi_availability_service_evidence": [
        "closed_poi_replacement", "closed_study_spot_replacement", "paired_study_a", "avoid_crowd_event"
    ],
    "memory_conditioned_preference": [
        "memory_dependent_place_choice", "hard_stale_plan_override", "unexpected_friend_encounter"
    ],
    "social_coordination_copresence": [
        "social_copresence_two_party", "social_copresence_open_meet", "social_copresence_event_window", "social_copresence_decoy_location"
    ],
    "multi_party_commitment": [
        "conflicting_social_obligation", "meeting_wait_trap", "hard_three_meeting_relay", "social_copresence_message_gated"
    ],
    "compound_long_horizon": [
        "hard_overlapping_windows", "paired_commute_a", "paired_study_b"
    ],
}

LOCATION_ROLE = {
    "home_aria": "home_primary",
    "home_ben": "home_friend",
    "office": "office",
    "transit_hub": "transit_hub",
    "plaza": "plaza",
    "cafe_central": "meeting_cafe",
    "quiet_cafe": "quiet_cafe",
    "library": "library",
    "coworking": "coworking",
    "city_hall": "civic_service",
    "park": "park",
    "gym": "gym",
    "market": "market",
    "pharmacy": "pharmacy",
    "clinic": "clinic",
    "budget_diner": "budget_food",
    "school": "school",
    "theatre": "culture",
    "bookstore": "bookstore",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def stable_seed(*parts: str) -> int:
    digest = hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()
    return int(digest[:12], 16)


def _rewrite(value: Any, id_map: dict[str, str], name_map: dict[str, str]) -> Any:
    if isinstance(value, dict):
        return {key: _rewrite(item, id_map, name_map) for key, item in value.items()}
    if isinstance(value, list):
        return [_rewrite(item, id_map, name_map) for item in value]
    if isinstance(value, str):
        if value in id_map:
            return id_map[value]
        rewritten = value
        for old_name, new_name in sorted(name_map.items(), key=lambda row: -len(row[0])):
            rewritten = rewritten.replace(old_name, new_name)
        return rewritten
    return value


def instantiate(
    source: dict[str, Any],
    source_world: dict[str, Any],
    target_world: dict[str, Any],
    construct: str,
    split: str,
    variant: int,
    ordinal: int,
) -> dict[str, Any]:
    role_to_target = {loc["semantic_role"]: loc for loc in target_world["locations"]}
    id_map = {old_id: role_to_target[role]["id"] for old_id, role in LOCATION_ROLE.items()}
    old_names = {loc["id"]: loc["name"] for loc in source_world["locations"]}
    name_map = {old_names[old_id]: role_to_target[role]["name"] for old_id, role in LOCATION_ROLE.items()}
    scenario = _rewrite(copy.deepcopy(source), id_map, name_map)
    source_pair = scenario.pop("perturbation_pair", None)
    template_id = source["scenario_id"]
    seed = stable_seed(GENERATOR_VERSION, construct, template_id, target_world["world_id"], str(variant))
    scenario_id = f"ci11_{construct[:4]}_{template_id}_{target_world['world_id']}_{variant}"
    scenario["scenario_id"] = scenario_id
    scenario["world_id"] = target_world["world_id"]
    scenario["family"] = construct
    scenario["benchmark_metadata"] = {
        "benchmark_version": "1.1.0",
        "candidate_status": "pending_acceptance_gates",
        "split": split,
        "construct_family": construct,
        "difficulty_tier": ("easy", "medium", "hard")[ordinal % 3],
        "difficulty_status": "provisional_pending_baseline_calibration",
        "template_id": template_id,
        "instance_variant": variant,
        "seed": seed,
        "generator_version": GENERATOR_VERSION,
        "source_version": "1.0-rc1",
        "source_family": source.get("family"),
        "source_perturbation_pair": source_pair,
        "world_visibility": target_world["release_visibility"],
    }
    if variant:
        # A transparent easier parameterization, used only where three source
        # templates cannot fill the 12 public instances without duplication.
        scenario["episode"]["max_steps"] += 1
        scenario["agents"][0]["budget"] += 3
        scenario["benchmark_metadata"]["parameterization"] = "one_extra_step_and_three_extra_credits"
    return scenario


def _public_split(index: int, construct_index: int) -> str:
    quotas = (3, 5, 4) if construct_index % 2 == 0 else (3, 4, 5)
    if index < quotas[0]:
        return "examples"
    if index < quotas[0] + quotas[1]:
        return "development"
    return "public_test"


def build_candidates(include_private: bool = True) -> list[dict[str, Any]]:
    source_world = load_json(TEMPLATE_ROOT / "worlds" / "micro_city.json")
    source_scenarios = {
        path.stem: load_json(path) for path in sorted((TEMPLATE_ROOT / "scenarios").glob("*.json"))
    }
    public_worlds = [load_json(path) for path in sorted((ROOT / "worlds" / "public").glob("*.json"))]
    private_worlds = [load_json(path) for path in sorted((ROOT / "worlds" / "private").glob("*.json"))]
    if len(public_worlds) != 3:
        raise RuntimeError("generate_worlds.py must produce exactly three public worlds first")
    if include_private and len(private_worlds) != 2:
        raise RuntimeError("organizer generation requires exactly two private worlds")

    candidates: list[dict[str, Any]] = []
    for construct_index, (construct, template_ids) in enumerate(CONSTRUCT_TEMPLATES.items()):
        missing = [template_id for template_id in template_ids if template_id not in source_scenarios]
        if missing:
            raise RuntimeError(f"missing source templates: {missing}")
        public_specs = [(template_id, world, 0) for template_id in template_ids for world in public_worlds]
        if len(public_specs) == 9:
            public_specs.extend((template_ids[i], public_worlds[i], 1) for i in range(3))
        assert len(public_specs) == 12
        for index, (template_id, world, variant) in enumerate(public_specs):
            candidates.append(
                instantiate(source_scenarios[template_id], source_world, world, construct, _public_split(index, construct_index), variant, index)
            )
        if include_private:
            private_templates = template_ids[:3]
            for index, (template_id, world) in enumerate(
                (item for template_id in private_templates for item in ((template_id, private_worlds[0]), (template_id, private_worlds[1])))
            ):
                candidates.append(
                    instantiate(source_scenarios[template_id], source_world, world, construct, "private_test", 0, index + 12)
                )
    return candidates


def generate_pack(output_root: Path = ROOT, include_private: bool = True) -> dict[str, Any]:
    candidates = build_candidates(include_private=include_private)
    for scenario in candidates:
        split = scenario["benchmark_metadata"]["split"]
        output_path = output_root / "scenarios" / split / f"{scenario['scenario_id']}.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(scenario, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    split_counts = Counter(item["benchmark_metadata"]["split"] for item in candidates)
    construct_counts = Counter(item["benchmark_metadata"]["construct_family"] for item in candidates)
    difficulty_counts = Counter(item["benchmark_metadata"]["difficulty_tier"] for item in candidates)
    entries = [
        {
            "scenario_id": item["scenario_id"],
            "split": item["benchmark_metadata"]["split"],
            "world_id": item["world_id"],
            "construct_family": item["benchmark_metadata"]["construct_family"],
            "difficulty_tier": item["benchmark_metadata"]["difficulty_tier"],
            "template_id": item["benchmark_metadata"]["template_id"],
            "seed": item["benchmark_metadata"]["seed"],
            "sha256": hashlib.sha256(json.dumps(item, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest(),
            "candidate_status": "pending_acceptance_gates",
        }
        for item in candidates
    ]
    split_hashes = {}
    for split in sorted(split_counts):
        split_entries = sorted(
            (entry for entry in entries if entry["split"] == split),
            key=lambda entry: entry["scenario_id"],
        )
        split_hashes[split] = hashlib.sha256(
            "\n".join(entry["sha256"] for entry in split_entries).encode("ascii")
        ).hexdigest()
    manifest = {
        "schema_version": "cityintent_scenario_manifest_v1",
        "benchmark_version": "1.1.0",
        "generator_version": GENERATOR_VERSION,
        "candidate_count": len(entries),
        "accepted_count": 0,
        "split_counts": dict(sorted(split_counts.items())),
        "construct_counts": dict(sorted(construct_counts.items())),
        "difficulty_counts": dict(sorted(difficulty_counts.items())),
        "split_hashes": split_hashes,
        "scenarios": entries,
    }
    manifest_path = output_root / "manifests" / "scenarios_manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    rejection_path = output_root / "rejection_logs" / "generation_rejections.jsonl"
    rejection_path.parent.mkdir(parents=True, exist_ok=True)
    rejection_path.touch(exist_ok=True)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=ROOT)
    parser.add_argument("--public-only", action="store_true")
    args = parser.parse_args()
    manifest = generate_pack(args.output_root.resolve(), include_private=not args.public_only)
    print(json.dumps({key: manifest[key] for key in ("candidate_count", "accepted_count", "split_counts", "construct_counts", "difficulty_counts")}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
