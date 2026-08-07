#!/usr/bin/env python3
"""Build a public calibration matrix with a deconfounded time-window template."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
V1_ROOT = ROOT.parent
EXPANSION_ROOT = ROOT / "expansion_wave1"
OUTPUT_ROOT = ROOT / "time_v7" / "public_matrix"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import generate_native_pilot as pilot  # noqa: E402


GENERATOR_VERSION = "cityintent-time-window-7.0.0"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def build_time_item(world: dict[str, Any], variant: int) -> tuple[dict[str, Any], dict[str, Any]]:
    ids = pilot.role_map(world)
    scenario = pilot.base_scenario(world, "time_window_scheduling", variant)
    scenario["scenario_id"] = f"ci11n_time7_{world['world_id']}_v{variant}"
    scenario["title"] = f"Native Time Window Scheduling v7 {variant}"
    pharmacy = ids["pharmacy"]
    stale_venue = ids["office"]
    announced_venue = ids["library"]
    home = ids["home_primary"]
    city = pilot.runner.CityWorld(world)
    _, first_leg = city.shortest_path(home, pharmacy, scenario, 600)
    service_end = 600 + int(first_leg) + 1 + 5
    pickup_deadline = service_end + 1
    update_time = service_end + 3
    _, second_leg = city.shortest_path(pharmacy, announced_venue, scenario, update_time)
    window_start = update_time + int(second_leg) + 2
    window_end = window_start + 6

    scenario["agents"][0]["private_intention"] = (
        f"Obtain the prescription at {pharmacy} by {pilot.fmt(pickup_deadline)}. "
        f"Do not assume the usual appointment venue {stale_venue}: at "
        f"{pilot.fmt(update_time)} a public same-day update will announce the free venue. "
        f"Wait for that update, then be inside the announced venue during "
        f"{pilot.fmt(window_start)}-{pilot.fmt(window_end)}. Finish by 13:00."
    )
    scenario["public_context"] = (
        "Future public updates are observable only after their timestamp. "
        "The appointment venue is the location named by the update's announced_venue field."
    )
    scenario["events"] = [{
        "time": pilot.fmt(update_time),
        "type": "appointment_venue_update",
        "location": announced_venue,
        "visibility": "public",
        "effect": {
            "announced_venue": announced_venue,
            "supersedes_venue": stale_venue,
        },
    }]
    scenario["critical_locations"] += [pharmacy, stale_venue, announced_venue]
    scenario["success_conditions"] = [
        pilot.condition(
            "pickup_deadline", "obtain_at", "outcome", .35,
            location=pharmacy, item="prescription", service="prescription_pickup",
            deadline=pilot.fmt(pickup_deadline), minutes=5,
        ),
        pilot.condition(
            "updated_venue_window", "visit_open_location", "outcome", .45,
            location_any_of=[announced_venue],
            time_window=[pilot.fmt(window_start), pilot.fmt(window_end)],
        ),
        pilot.condition("finish_episode", "episode_complete_before", "constraint", .20, deadline="13:00"),
    ]
    metadata = scenario["benchmark_metadata"]
    metadata.update({
        "benchmark_version": "1.1.0-time-v7-calibration",
        "candidate_status": "oracle_gate_pending",
        "split": "calibration_public",
        "difficulty_tier": "hard",
        "template_id": "native_time_window_public_update_v7",
        "generator_version": GENERATOR_VERSION,
        "world_visibility": world["release_visibility"],
        "temporal_information_contract": "future_public_update_v1",
    })

    wait_for_update = max(1, update_time - service_end)
    wait_for_window = max(1, window_start - (update_time + int(second_leg) + 1))
    oracle = (
        pilot.access(pharmacy)
        + [{"kind": "use_service", "target": pharmacy, "service": "prescription_pickup", "minutes": 5}]
        + [{"kind": "dwell", "minutes": wait_for_update}]
        + pilot.access(announced_venue)
        + [{"kind": "dwell", "minutes": wait_for_window}, {"kind": "finish"}]
    )
    negative = (
        pilot.access(pharmacy)
        + [{"kind": "use_service", "target": pharmacy, "service": "prescription_pickup", "minutes": 5}]
        + [{"kind": "dwell", "minutes": wait_for_update}]
        + pilot.access(stale_venue)
        + [{"kind": "dwell", "minutes": 3}, {"kind": "finish"}]
    )
    return scenario, {
        "scenario_id": scenario["scenario_id"],
        "construct_family": "time_window_scheduling",
        "oracle": oracle,
        "negative": negative,
    }


def generate(output_root: Path = OUTPUT_ROOT) -> dict[str, Any]:
    output_root = output_root.resolve()
    expansion_plans = {
        row["scenario_id"]: row
        for row in load_json(EXPANSION_ROOT / "oracle_negative_plans.json")
    }
    scenarios: list[dict[str, Any]] = []
    plans: list[dict[str, Any]] = []
    for path in sorted((EXPANSION_ROOT / "scenarios").glob("*.json")):
        scenario = load_json(path)
        metadata = scenario["benchmark_metadata"]
        if metadata["world_visibility"] != "public" or scenario["family"] == "time_window_scheduling":
            continue
        scenarios.append(scenario)
        plans.append(expansion_plans[scenario["scenario_id"]])

    public_worlds = [
        load_json(path) for path in sorted((V1_ROOT / "worlds" / "public").glob("*.json"))
    ]
    # Preserve the pilot rotation for time: metro=v0, suburb=v1, harbor=v2.
    for variant in range(3):
        world = public_worlds[(1 + variant) % 3]
        scenario, plan = build_time_item(world, variant)
        scenarios.append(scenario)
        plans.append(plan)

    scenario_dir = output_root / "scenarios"
    scenario_dir.mkdir(parents=True, exist_ok=True)
    expected = set()
    for scenario in scenarios:
        path = scenario_dir / f"{scenario['scenario_id']}.json"
        expected.add(path)
        path.write_text(json.dumps(scenario, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    stale = set(scenario_dir.glob("*.json")) - expected
    if stale:
        raise RuntimeError(f"stale files require explicit removal: {sorted(stale)}")
    (output_root / "oracle_negative_plans.json").write_text(
        json.dumps(plans, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    world_paths = [
        str(path.resolve().relative_to(output_root, walk_up=True))
        for path in sorted((V1_ROOT / "worlds" / "public").glob("*.json"))
    ]
    agent_ids = ["utility_planner", "llm_direct_actor", "reactive_replanner", "memory_reflection"]
    config = {
        "benchmark_id": "cityintent_v1_1_time_v7_public_matrix",
        "version": "1.1.0-time-v7-calibration",
        "status": "oracle_gate_pending_candidate",
        "worlds": world_paths,
        "scenario_dir": "scenarios",
        "agents_under_test": [{"id": value} for value in agent_ids],
        "metrics": [{"id": value} for value in pilot.METRICS],
        "validation": {
            "min_scenarios": 24,
            "required_agent_ids": agent_ids,
            "required_metric_ids": [
                "task_completion", "constraint_satisfaction", "goal_completion",
                "feasibility_violation", "travel_efficiency", "budget_consistency",
                "intention_consistency",
            ],
        },
    }
    (output_root / "benchmark_config.json").write_text(
        json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    manifest = {
        "schema_version": "cityintent_time_v7_public_matrix_v1",
        "generator_version": GENERATOR_VERSION,
        "status": "oracle_gate_pending_candidate_not_release",
        "scenario_count": len(scenarios),
        "time_scenario_ids": sorted(
            scenario["scenario_id"] for scenario in scenarios
            if scenario["family"] == "time_window_scheduling"
        ),
    }
    (output_root / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return manifest


if __name__ == "__main__":
    print(json.dumps(generate(), sort_keys=True))
