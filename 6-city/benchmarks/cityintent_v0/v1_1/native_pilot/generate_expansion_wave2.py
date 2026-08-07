#!/usr/bin/env python3
"""Generate Wave-2 mechanism-diverse public candidates for CityIntent v1.1."""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
V1_ROOT = ROOT.parent
OUTPUT_ROOT = ROOT / "expansion_wave2"
BASE_ITEM_GENERATOR_VERSION = "cityintent-native-expansion-wave2-1.0.0"
HARDENED3_ITEM_GENERATOR_VERSION = "cityintent-native-expansion-wave2-1.0.1"
GENERATOR_VERSION = "cityintent-native-expansion-wave2-1.0.3"
HARDENED4_ITEM_GENERATOR_VERSION = GENERATOR_VERSION
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import generate_native_pilot as pilot  # noqa: E402


MECHANISMS = {
    "disruption_recovery": "future_destination_relocation",
    "time_window_scheduling": "ordered_dual_free_windows",
    "resource_budget_allocation": "money_and_action_budget_joint_allocation",
    "poi_availability_service_evidence": "future_service_registry_update",
    "memory_conditioned_preference": "environment_cued_conditional_memory",
    "social_coordination_copresence": "confirmed_meeting_future_relocation",
    "multi_party_commitment": "overlap_requires_explicit_renegotiation",
    "compound_long_horizon": "purchase_meet_and_return_chain",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def costs(world: dict[str, Any]) -> dict[str, float]:
    return {loc["id"]: float(loc.get("typical_cost", 0) or 0) for loc in world["locations"]}


def set_metadata(scenario: dict[str, Any], mechanism: str, world: dict[str, Any]) -> None:
    metadata = scenario["benchmark_metadata"]
    metadata.update({
        "benchmark_version": "1.1.0-expansion-wave2",
        "candidate_status": "oracle_gate_pending",
        "split": "calibration_public",
        "difficulty_tier": "hard",
        "template_id": f"wave2_{mechanism}",
        "mechanism_id": mechanism,
        "generator_version": BASE_ITEM_GENERATOR_VERSION,
        "world_visibility": world["release_visibility"],
    })


def build_item(world: dict[str, Any], construct: str, variant: int) -> tuple[dict[str, Any], dict[str, Any]]:
    ids = pilot.role_map(world)
    scenario = pilot.base_scenario(world, construct, variant, max_steps=18)
    mechanism = MECHANISMS[construct]
    scenario["scenario_id"] = f"ci11w2_{construct[:4]}_{world['world_id']}_v{variant}"
    scenario["title"] = f"Wave 2 {mechanism.replace('_', ' ').title()}"
    set_metadata(scenario, mechanism, world)
    home = ids["home_primary"]
    finish = {"kind": "finish"}
    city = pilot.runner.CityWorld(world)
    world_costs = costs(world)

    if construct == "disruption_recovery":
        stale_target, target = ids["office"], ids["clinic"]
        event_time = 620
        scenario["events"] = [{
            "time": pilot.fmt(event_time), "type": "destination_relocation",
            "location": target, "visibility": "public",
            "effect": {"replacement_destination": target, "supersedes_destination": stale_target},
        }]
        scenario["agents"][0]["private_intention"] = (
            f"The usual destination is {stale_target}, but a disruption update at "
            f"{pilot.fmt(event_time)} may relocate the appointment. Do not finish before seeing "
            "that public update; recover by reaching and entering its replacement_destination by 11:30."
        )
        scenario["critical_locations"] += [stale_target, target]
        scenario["success_conditions"] = [
            pilot.condition("reach_relocated_target", "visit_before", "outcome", .80, location=target, deadline="11:30", ignore_start=True),
            pilot.condition("legal_trace", "no_feasibility_violation", "constraint", .20),
        ]
        oracle = [{"kind": "dwell", "minutes": event_time - 600}] + pilot.access(target) + [finish]
        negative = [{"kind": "dwell", "minutes": event_time - 600}] + pilot.access(stale_target) + [finish]

    elif construct == "time_window_scheduling":
        first, second = ids["library"], ids["office"]
        _, first_leg = city.shortest_path(home, first, scenario, 600)
        first_start = 600 + int(first_leg) + 3
        first_end = first_start + 5
        _, second_leg = city.shortest_path(first, second, scenario, first_start)
        second_start = first_start + int(second_leg) + 5
        second_end = second_start + 5
        scenario["agents"][0]["private_intention"] = (
            f"Be inside the free venue {first} during {pilot.fmt(first_start)}-{pilot.fmt(first_end)}, "
            f"then be inside {second} during {pilot.fmt(second_start)}-{pilot.fmt(second_end)}. "
            "The order is mandatory; arriving at only one window is incomplete."
        )
        scenario["critical_locations"] += [first, second]
        first_weight, second_weight = (.45, .35) if variant == 2 else (.40, .40)
        scenario["success_conditions"] = [
            pilot.condition("first_window", "visit_open_location", "outcome", first_weight, location_any_of=[first], time_window=[pilot.fmt(first_start), pilot.fmt(first_end)]),
            pilot.condition("second_window", "visit_open_location", "outcome", second_weight, location_any_of=[second], time_window=[pilot.fmt(second_start), pilot.fmt(second_end)]),
            pilot.condition("legal_trace", "no_feasibility_violation", "constraint", .20),
        ]
        if variant == 2:
            scenario["benchmark_metadata"]["generator_version"] = HARDENED4_ITEM_GENERATOR_VERSION
        wait_first = max(1, first_start - (600 + int(first_leg) + 1))
        after_first = first_start
        wait_second = max(1, second_start - (after_first + int(second_leg) + 1))
        oracle = pilot.access(first) + [{"kind": "dwell", "minutes": wait_first}] + pilot.access(second) + [{"kind": "dwell", "minutes": wait_second}, finish]
        negative = pilot.access(second) + [{"kind": "dwell", "minutes": 5}] + pilot.access(first) + [{"kind": "dwell", "minutes": 5}, finish]

    elif construct == "resource_budget_allocation":
        market, gym, temptation = ids["market"], ids["gym"], ids["meeting_cafe"]
        quiet_cafe = ids["quiet_cafe"]
        required_budget = world_costs[market] + world_costs[gym]
        scenario["agents"][0]["budget"] = required_budget
        scenario["episode"]["max_steps"] = 9
        no_detour_clause = (
            f" Do not enter either optional cafe {temptation} or {quiet_cafe}; "
            "avoiding that detour is part of preserving the action budget."
            if variant == 1 else ""
        )
        scenario["agents"][0]["private_intention"] = (
            f"With exactly {required_budget:g} credits, buy the required supplies at {market} "
            f"and complete the booked training service at {gym}. Do not spend at the tempting "
            f"optional cafe {temptation}; preserve enough money and finish within the nine-action limit. "
            "Return inside home after both errands. Any purchase label at the market and any paid "
            f"service label at the gym are acceptable.{no_detour_clause}"
        )
        scenario["critical_locations"] += [market, gym, temptation]
        if variant == 1:
            scenario["critical_locations"].append(quiet_cafe)
            scenario["success_conditions"] = [
                pilot.condition("supplies", "purchase_at", "outcome", .15, location=market, minutes=3),
                pilot.condition("training", "use_service_at", "outcome", .25, location=gym, minutes=5),
                pilot.condition("return_home", "visit_before", "outcome", .20, location=home, deadline="13:00", ignore_start=True),
                pilot.condition("no_optional_cafe_detour", "avoid_when_possible", "outcome", .20, avoid_locations=[temptation, quiet_cafe]),
                pilot.condition("budget", "budget_at_least", "constraint", .20, agent="aria", min_remaining=0),
            ]
            scenario["benchmark_metadata"]["generator_version"] = HARDENED4_ITEM_GENERATOR_VERSION
        else:
            scenario["success_conditions"] = [
                pilot.condition("supplies", "purchase_at", "outcome", .25, location=market, minutes=3),
                pilot.condition("training", "use_service_at", "outcome", .25, location=gym, minutes=5),
                pilot.condition("return_home", "visit_before", "outcome", .30, location=home, deadline="13:00", ignore_start=True),
                pilot.condition("budget", "budget_at_least", "constraint", .20, agent="aria", min_remaining=0),
            ]
        oracle = pilot.access(market) + [{"kind": "buy", "target": market, "item": "required_supplies", "minutes": 3}] + pilot.access(gym) + [{"kind": "use_service", "target": gym, "service": "booked_training", "minutes": 5}] + pilot.access(home) + [finish]
        negative = pilot.access(temptation) + [{"kind": "buy", "target": temptation, "item": "coffee", "minutes": 2}] + pilot.access(market) + [{"kind": "buy", "target": market, "item": "required_supplies", "minutes": 3}, finish]

    elif construct == "poi_availability_service_evidence":
        correct, decoy_a, decoy_b = ids["office"], ids["civic_service"], ids["clinic"]
        update_time = 610
        scenario["events"] = [{
            "time": pilot.fmt(update_time), "type": "service_registry_update",
            "location": correct, "visibility": "public",
            "effect": {"service": "identity_verification", "provider_location": correct},
        }]
        scenario["agents"][0]["private_intention"] = (
            f"Complete identity-verification service today. {correct}, {decoy_a}, and {decoy_b} "
            f"are all plausible and open. Wait until the public service-registry update at "
            f"{pilot.fmt(update_time)}, then use identity-verification at its provider_location. "
            "Do not guess from location type or count arrival alone."
        )
        scenario["critical_locations"] += [correct, decoy_a, decoy_b]
        scenario["success_conditions"] = [
            pilot.condition("identity_verification", "use_service_at", "outcome", .80, location=correct, service="identity_verification", deadline="12:00", minutes=5),
            pilot.condition("legal_trace", "no_feasibility_violation", "constraint", .20),
        ]
        oracle = [{"kind": "dwell", "minutes": update_time - 600}] + pilot.access(correct) + [{"kind": "use_service", "target": correct, "service": "identity_verification", "minutes": 5}, finish]
        negative = [{"kind": "dwell", "minutes": update_time - 600}] + pilot.access(decoy_a) + [{"kind": "use_service", "target": decoy_a, "service": "identity_verification", "minutes": 5}, finish]

    elif construct == "memory_conditioned_preference":
        outdoor, indoor, outdated = ids["park"], ids["office"], ids["quiet_cafe"]
        scenario["agents"][0]["budget"] = 0
        scenario["agents"][0]["memory_seeds"] = [
            f"Older preference: {outdated} was once my default reset spot.",
            f"Current rule: choose the free outdoor reset at {outdoor} when conditions are clear.",
            f"Conditional fallback: if an air-quality alert is active, avoid {outdoor} and use the free indoor room at {indoor}.",
        ]
        scenario["events"] = [{
            "time": "10:00", "type": "air_quality_alert", "location": outdoor,
            "visibility": "public", "effect": {"avoid_location": outdoor, "until": "13:00"},
        }]
        scenario["benchmark_metadata"]["memory_access_contract"] = "recall_required_v1"
        scenario["agents"][0]["private_intention"] = (
            "Recall the conditional place-choice rule, combine it with today's public conditions, "
            "and complete a 10-minute free reset at the correct location."
        )
        scenario["critical_locations"] += [outdoor, indoor, outdated]
        scenario["success_conditions"] = [
            pilot.condition("recall_rule", "recall_memory", "process", .15, min_recalls=1),
            pilot.condition("conditional_choice", "visit_location", "outcome", .40, location=indoor),
            pilot.condition("reset", "dwell_minutes", "outcome", .30, location_any_of=[indoor], min_minutes=10),
            pilot.condition("avoid_alert", "avoid_when_possible", "constraint", .15, avoid_locations=[outdoor, outdated]),
        ]
        oracle = [{"kind": "recall", "query": "conditional place rule under current alert"}] + pilot.access(indoor) + [{"kind": "dwell", "minutes": 10}, finish]
        negative = [{"kind": "recall", "query": "old default"}] + pilot.access(outdoor) + [{"kind": "dwell", "minutes": 10}, finish]

    elif construct == "social_coordination_copresence":
        stale, relocated = ids["office"], ids["library"]
        scenario["agents"].append({
            "agent_id": "ben", "persona": "A friend whose meeting venue changes.",
            "start_location": stale, "budget": 0, "private_intention": "Meet Aria at the updated venue.",
            "known_locations": [stale, relocated], "memory_seeds": [],
        })
        update_time = 630
        _, travel = city.shortest_path(home, relocated, scenario, update_time)
        window_start = update_time + int(travel) + 2
        window_end = window_start + 10
        scenario["events"] = [{
            "time": pilot.fmt(update_time), "type": "meeting_relocation",
            "location": relocated, "visibility": "public",
            "effect": {"agents_present": ["ben"], "optional_social_opportunity_minutes": window_end - update_time, "supersedes_venue": stale},
        }]
        scenario["agents"][0]["private_intention"] = (
            f"Message Ben to confirm. Do not commit to the usual venue {stale}: a public update at "
            f"{pilot.fmt(update_time)} will relocate the meeting. After seeing it, enter the updated "
            f"venue and meet Ben during {pilot.fmt(window_start)}-{pilot.fmt(window_end)}."
        )
        scenario["critical_locations"] += [stale, relocated]
        scenario["success_conditions"] = [
            pilot.condition("confirm", "send_message", "outcome", .20, to="ben"),
            pilot.condition("relocated_meeting", "co_presence", "outcome", .60, agents=["aria", "ben"], location_any_of=[relocated], time_window=[pilot.fmt(window_start), pilot.fmt(window_end)]),
            pilot.condition("legal_trace", "no_feasibility_violation", "constraint", .20),
        ]
        wait = max(1, update_time - 602)
        oracle = [{"kind": "message", "to": "ben", "content": "Confirmed; I will follow the update."}, {"kind": "dwell", "minutes": wait}] + pilot.access(relocated) + [{"kind": "dwell", "minutes": 1}, {"kind": "interact", "to": "ben", "minutes": 2}, finish]
        negative = [{"kind": "message", "to": "ben", "content": "Confirmed at the usual office."}] + pilot.access(stale) + [{"kind": "interact", "to": "ben", "minutes": 2}, finish]

    elif construct == "multi_party_commitment":
        cafe, park = ids["meeting_cafe"], ids["park"]
        for agent_id, location in (("ben", cafe), ("casey", park)):
            scenario["agents"].append({
                "agent_id": agent_id, "persona": "A coordination partner.",
                "start_location": location, "budget": 0, "private_intention": "Coordinate with Aria.",
                "known_locations": [location], "memory_seeds": [],
            })
        scenario["agents"][0]["budget"] = world_costs[cafe]
        scenario["agents"][0]["private_intention"] = (
            f"Ben and Casey requested overlapping meetings. Confirm and meet Ben inside {cafe} "
            "between 11:00-11:15. Explicitly message Casey to reschedule instead of silently "
            f"dropping that commitment; do not travel to {park} today."
        )
        scenario["critical_locations"] += [cafe, park]
        renegotiate_weight, legal_weight = (.15, .15) if variant == 2 else (.10, .20)
        scenario["success_conditions"] = [
            pilot.condition("confirm_ben", "send_message", "outcome", .20, to="ben"),
            pilot.condition("renegotiate_casey", "send_message", "outcome", renegotiate_weight, to="casey"),
            pilot.condition("meet_ben", "co_presence", "outcome", .50, agents=["aria", "ben"], location_any_of=[cafe], time_window=["11:00", "11:15"]),
            pilot.condition("legal_trace", "no_feasibility_violation", "constraint", legal_weight),
        ]
        if variant == 2:
            scenario["benchmark_metadata"]["generator_version"] = HARDENED4_ITEM_GENERATOR_VERSION
        _, travel = city.shortest_path(home, cafe, scenario, 604)
        wait = max(1, 660 - (604 + int(travel) + 1 + 2))
        oracle = [{"kind": "message", "to": "ben", "content": "Confirmed."}, {"kind": "message", "to": "casey", "content": "Please reschedule."}] + pilot.access(cafe) + [{"kind": "buy", "target": cafe, "item": "refreshment", "minutes": 2}, {"kind": "dwell", "minutes": wait}, {"kind": "interact", "to": "ben", "minutes": 2}, finish]
        negative = [{"kind": "message", "to": "casey", "content": "Confirmed."}] + pilot.access(park) + [{"kind": "interact", "to": "casey", "minutes": 2}, finish]

    elif construct == "compound_long_horizon":
        pharmacy, cafe = ids["pharmacy"], ids["meeting_cafe"]
        scenario["agents"].append({
            "agent_id": "ben", "persona": "A friend waiting for a short meeting.",
            "start_location": cafe, "budget": 0, "private_intention": "Meet Aria.",
            "known_locations": [cafe], "memory_seeds": [],
        })
        scenario["agents"][0]["budget"] = world_costs[pharmacy] + world_costs[cafe]
        scenario["agents"][0]["private_intention"] = (
            f"Buy medicine at {pharmacy}, message Ben, meet him inside {cafe} between 11:00-11:20, "
            f"and return inside {home} before 12:15. Preserve every link in the chain."
        )
        scenario["critical_locations"] += [pharmacy, cafe]
        medicine_weight, confirm_weight, meet_weight, return_weight = (
            (.15, .15, .40, .15) if variant == 2 else (.20, .12, .33, .20)
        )
        scenario["success_conditions"] = [
            pilot.condition("medicine", "buy_item", "outcome", medicine_weight, location=pharmacy, item="medicine", minutes=3),
            pilot.condition("confirm", "send_message", "outcome", confirm_weight, to="ben"),
            pilot.condition("meet", "co_presence", "outcome", meet_weight, agents=["aria", "ben"], location_any_of=[cafe], time_window=["11:00", "11:20"]),
            pilot.condition("return", "visit_before", "outcome", return_weight, location=home, deadline="12:15", ignore_start=True),
            pilot.condition("legal_trace", "no_feasibility_violation", "constraint", .15),
        ]
        if variant == 2:
            scenario["benchmark_metadata"]["generator_version"] = HARDENED3_ITEM_GENERATOR_VERSION
        _, leg1 = city.shortest_path(home, pharmacy, scenario, 600)
        _, leg2 = city.shortest_path(pharmacy, cafe, scenario, 600 + int(leg1) + 4)
        arrival = 600 + int(leg1) + 1 + 3 + 2 + int(leg2) + 1 + 2
        wait = max(1, 660 - arrival)
        oracle = pilot.access(pharmacy) + [{"kind": "buy", "target": pharmacy, "item": "medicine", "minutes": 3}, {"kind": "message", "to": "ben", "content": "Confirmed."}] + pilot.access(cafe) + [{"kind": "buy", "target": cafe, "item": "refreshment", "minutes": 2}, {"kind": "dwell", "minutes": wait}, {"kind": "interact", "to": "ben", "minutes": 2}] + pilot.access(home) + [finish]
        negative = pilot.access(pharmacy) + [{"kind": "buy", "target": pharmacy, "item": "medicine", "minutes": 3}] + pilot.access(home) + [finish]
    else:
        raise ValueError(construct)

    return scenario, {"scenario_id": scenario["scenario_id"], "construct_family": construct, "oracle": oracle, "negative": negative}


def generate(output_root: Path = OUTPUT_ROOT) -> dict[str, Any]:
    output_root = output_root.resolve()
    worlds = [load_json(path) for path in sorted((V1_ROOT / "worlds" / "public").glob("*.json"))]
    scenarios: list[dict[str, Any]] = []
    plans: list[dict[str, Any]] = []
    rejections: list[dict[str, Any]] = []
    for construct_index, construct in enumerate(pilot.CONSTRUCTS):
        for variant in range(3):
            world = worlds[(construct_index + variant) % 3]
            try:
                scenario, plan = build_item(world, construct, variant)
                scenarios.append(scenario)
                plans.append(plan)
            except Exception as exc:
                rejections.append({"construct": construct, "variant": variant, "world_id": world["world_id"], "reason": str(exc)})

    scenario_dir = output_root / "scenarios"
    scenario_dir.mkdir(parents=True, exist_ok=True)
    expected_paths = {scenario_dir / f"{scenario['scenario_id']}.json" for scenario in scenarios}
    stale_paths = set(scenario_dir.glob("*.json")) - expected_paths
    if stale_paths:
        raise RuntimeError(f"stale scenario files require explicit removal: {sorted(stale_paths)}")
    for scenario in scenarios:
        (scenario_dir / f"{scenario['scenario_id']}.json").write_text(json.dumps(scenario, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (output_root / "oracle_negative_plans.json").write_text(json.dumps(plans, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    rejection_dir = output_root / "rejection_logs"
    rejection_dir.mkdir(parents=True, exist_ok=True)
    (rejection_dir / "generation_rejections.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rejections), encoding="utf-8")
    world_paths = [str(path.resolve().relative_to(output_root, walk_up=True)) for path in sorted((V1_ROOT / "worlds" / "public").glob("*.json"))]
    agent_ids = ["utility_planner", "llm_direct_actor", "reactive_replanner", "memory_reflection"]
    config = {
        "benchmark_id": "cityintent_v1_1_expansion_wave2", "version": "1.1.0-expansion-wave2",
        "status": "oracle_gate_pending_candidate", "worlds": world_paths, "scenario_dir": "scenarios",
        "agents_under_test": [{"id": value} for value in agent_ids],
        "metrics": [{"id": value} for value in pilot.METRICS],
        "validation": {"min_scenarios": 24, "required_agent_ids": agent_ids, "required_metric_ids": ["task_completion", "constraint_satisfaction", "goal_completion", "feasibility_violation", "travel_efficiency", "budget_consistency", "intention_consistency"]},
    }
    (output_root / "benchmark_config.json").write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    manifest = {
        "schema_version": "cityintent_native_expansion_wave2_v1", "generator_version": GENERATOR_VERSION,
        "status": "oracle_gate_pending_candidate_not_release", "scenario_count": len(scenarios),
        "rejection_count": len(rejections), "construct_counts": dict(sorted(Counter(s["family"] for s in scenarios).items())),
        "mechanisms": MECHANISMS,
        "scenario_matrix_sha256": hashlib.sha256("\n".join(sorted(json.dumps(s, sort_keys=True, separators=(",", ":"), ensure_ascii=False) for s in scenarios)).encode()).hexdigest(),
    }
    (output_root / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


if __name__ == "__main__":
    print(json.dumps(generate(), sort_keys=True))
