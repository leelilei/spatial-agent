#!/usr/bin/env python3
"""Generate oracle-first CityIntent v1.1 pilot items for all eight constructs."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
V1_ROOT = ROOT.parent
V0_ROOT = V1_ROOT.parent
TOOLS = V0_ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
import run_baseline_traces as runner  # noqa: E402


CONSTRUCTS = (
    "disruption_recovery", "time_window_scheduling", "resource_budget_allocation",
    "poi_availability_service_evidence", "memory_conditioned_preference",
    "social_coordination_copresence", "multi_party_commitment", "compound_long_horizon",
)
WORLD_PATHS = tuple(sorted((V1_ROOT / "worlds" / "public").glob("*.json")))
METRICS = [
    "task_completion", "constraint_satisfaction", "goal_completion", "feasibility_violation",
    "replanning_success", "travel_efficiency", "budget_consistency", "intention_consistency",
    "social_appropriateness",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def role_map(world: dict[str, Any]) -> dict[str, str]:
    return {location["semantic_role"]: location["id"] for location in world["locations"]}


def fmt(minutes: int) -> str:
    return runner.format_time(minutes)


def condition(cid: str, kind: str, role: str, weight: float, **kwargs: Any) -> dict[str, Any]:
    return {"id": cid, "type": kind, "role": role, "weight": weight, **kwargs}


def base_scenario(world: dict[str, Any], construct: str, variant: int, max_steps: int = 14) -> dict[str, Any]:
    ids = role_map(world)
    scenario_id = f"ci11n_{construct[:4]}_{world['world_id']}_v{variant}"
    return {
        "scenario_id": scenario_id,
        "title": f"Native {construct.replace('_', ' ').title()} {variant}",
        "world_id": world["world_id"],
        "family": construct,
        "episode": {"start_time": "10:00", "end_time": "13:00", "max_steps": max_steps},
        "primary_agent": "aria",
        "agents": [{
            "agent_id": "aria", "persona": "A resident executing a private urban intention.",
            "start_location": ids["home_primary"], "budget": 100,
            "private_intention": "Complete every required outcome while respecting time, evidence, and resource constraints.",
            "known_locations": list(ids.values()), "memory_seeds": [],
        }],
        "public_context": "Only environment-observable action evidence counts as completion.",
        "events": [], "critical_locations": [ids["home_primary"]],
        "success_conditions": [], "scoring_metrics": METRICS,
        "architecture_probes": {
            "utility_planner": "Must produce explicit outcome evidence.",
            "llm_direct_actor": "May narrate success without the required action evidence.",
            "reactive_replanner": "Must preserve the intention while updating the plan.",
            "memory_reflection": "Must use relevant private memory without goal drift.",
        },
        "benchmark_metadata": {
            "benchmark_version": "1.1.0-native-pilot", "candidate_status": "hardened_v6_candidate",
            "split": "pilot", "construct_family": construct, "difficulty_tier": "medium" if variant == 0 else "hard",
            "template_id": f"native_{construct}", "instance_variant": variant,
            "seed": int(hashlib.sha256(scenario_id.encode()).hexdigest()[:12], 16),
            "generator_version": "cityintent-native-pilot-6.0.0", "world_visibility": "public",
            "observation_contract": "intent_only_v1", "expose_verifier_conditions": False,
        },
    }


def access(target: str) -> list[dict[str, Any]]:
    return [{"kind": "move", "target": target}, {"kind": "enter", "target": target}]


def build_item(world: dict[str, Any], construct: str, variant: int) -> tuple[dict[str, Any], dict[str, Any]]:
    ids = role_map(world)
    scenario = base_scenario(world, construct, variant)
    home = ids["home_primary"]
    finish = {"kind": "finish"}

    if construct == "disruption_recovery":
        closed, fallback = ids["quiet_cafe"], ids["coworking"]
        costs = {loc["id"]: loc.get("typical_cost", 0) or 0 for loc in world["locations"]}
        scenario["agents"][0]["budget"] = costs[fallback]
        scenario["events"] = [{"time": "10:05", "type": "preferred_workspace_closed", "location": closed, "visibility": "public", "effect": {"closed_until": "13:00"}}]
        scenario["agents"][0]["private_intention"] = f"Complete a 15-minute focused session in a quiet Wi-Fi workspace before 11:30. {closed} is the first choice, but if conditions change, recover at another suitable known site without exceeding the {costs[fallback]}-credit budget."
        scenario["critical_locations"] += [closed, fallback]
        scenario["success_conditions"] = [
            condition("fallback_presence", "visit_open_location", "outcome", .3, location_any_of=[ids["library"], fallback], time_window=["10:05", "11:30"]),
            condition("focus_block", "dwell_minutes", "outcome", .5, location_any_of=[ids["library"], fallback], min_minutes=15),
            condition("avoid_closed_site", "do_not_enter_closed_location", "constraint", .2, location=closed, time_window=["10:05", "13:00"]),
        ]
        oracle = access(fallback) + [{"kind": "use_service", "target": fallback, "service": "workspace_access", "minutes": 2}, {"kind": "dwell", "minutes": 15}, finish]
        negative = access(closed) + [{"kind": "buy", "target": closed, "item": "tea", "minutes": 2}, {"kind": "dwell", "minutes": 15}, finish]
    elif construct == "time_window_scheduling":
        pharmacy, cafe = ids["pharmacy"], ids["meeting_cafe"]
        city = runner.CityWorld(world)
        _, travel = city.shortest_path(home, pharmacy, scenario, 600)
        deadline = 600 + int(travel) + 8
        _, onward = city.shortest_path(pharmacy, cafe, scenario, deadline)
        arrival_after_purchase = 600 + int(travel) + 5 + int(onward)
        window_start = max(660, arrival_after_purchase + 5)
        window_end = window_start + 10
        scenario["agents"][0]["private_intention"] = f"Obtain the prescription at {pharmacy} no later than {fmt(deadline)}, either by purchase or pickup service. Then be present inside {cafe} during the narrow {fmt(window_start)}-{fmt(window_end)} arrival window. Finish by 13:00."
        scenario["critical_locations"] += [pharmacy, cafe]
        scenario["success_conditions"] = [
            condition("pickup_deadline", "obtain_at", "outcome", .4, location=pharmacy, item="prescription", service="prescription_pickup", deadline=fmt(deadline), minutes=5),
            condition("later_arrival_window", "visit_open_location", "outcome", .4, location_any_of=[cafe], time_window=[fmt(window_start), fmt(window_end)]),
            condition("finish_episode", "episode_complete_before", "constraint", .2, deadline="13:00"),
        ]
        wait_minutes = max(1, window_start - (arrival_after_purchase + 2))
        oracle = access(pharmacy) + [{"kind": "use_service", "target": pharmacy, "service": "prescription_pickup", "minutes": 5}] + access(cafe) + [{"kind": "buy", "target": cafe, "item": "coffee", "minutes": 2}, {"kind": "dwell", "minutes": wait_minutes}, finish]
        negative = access(cafe) + [{"kind": "buy", "target": cafe, "item": "coffee", "minutes": 2}, {"kind": "dwell", "minutes": 10}] + access(pharmacy) + [{"kind": "use_service", "target": pharmacy, "service": "prescription_pickup", "minutes": 5}, finish]
    elif construct == "resource_budget_allocation":
        pharmacy, diner = ids["pharmacy"], ids["budget_food"]
        costs = {loc["id"]: loc.get("typical_cost", 0) for loc in world["locations"]}
        scenario["agents"][0]["budget"] = costs[pharmacy] + costs[diner]
        scenario["agents"][0]["private_intention"] = f"With exactly {scenario['agents'][0]['budget']} credits, buy medicine at {pharmacy} and obtain a meal at {diner} without going negative."
        scenario["critical_locations"] += [pharmacy, diner]
        scenario["success_conditions"] = [
            condition("required_medicine", "buy_item", "outcome", .4, location=pharmacy, item="medicine", minutes=3),
            condition("required_meal", "use_service_at", "outcome", .4, location=diner, service="meal", minutes=5),
            condition("nonnegative_budget", "budget_at_least", "constraint", .2, agent="aria", min_remaining=0),
        ]
        oracle = access(pharmacy) + [{"kind": "buy", "target": pharmacy, "item": "medicine", "minutes": 3}] + access(diner) + [{"kind": "use_service", "target": diner, "service": "meal", "minutes": 5}, finish]
        negative = access(pharmacy) + [{"kind": "buy", "target": pharmacy, "item": "medicine", "minutes": 3}, finish]
    elif construct == "poi_availability_service_evidence":
        clinic, civic = ids["clinic"], ids["civic_service"]
        city = runner.CityWorld(world)
        _, first_leg = city.shortest_path(home, clinic, scenario, 600)
        clinic_deadline = 600 + int(first_leg) + 8
        _, second_leg = city.shortest_path(clinic, civic, scenario, clinic_deadline)
        civic_deadline = 600 + int(first_leg) + 5 + int(second_leg) + 8
        scenario["agents"][0]["private_intention"] = f"First enter {clinic} and explicitly complete medical check-in by {fmt(clinic_deadline)}. Then enter {civic} and complete the permit-application service by {fmt(civic_deadline)}. Arrival alone does not count at either place."
        scenario["critical_locations"] += [clinic, civic]
        scenario["success_conditions"] = [
            condition("complete_checkin", "use_service_at", "outcome", .4, location=clinic, deadline=fmt(clinic_deadline), minutes=5),
            condition("submit_permit", "use_service_at", "outcome", .4, location=civic, deadline=fmt(civic_deadline), minutes=5),
            condition("legal_trace", "no_feasibility_violation", "constraint", .2),
        ]
        oracle = access(clinic) + [{"kind": "use_service", "target": clinic, "service": "medical_check_in", "minutes": 5}] + access(civic) + [{"kind": "use_service", "target": civic, "service": "permit_application", "minutes": 5}, finish]
        negative = access(clinic) + [{"kind": "use_service", "target": clinic, "service": "medical_check_in", "minutes": 5}, finish]
    elif construct == "memory_conditioned_preference":
        old_preference, unavailable, preferred, library, decoy = ids["quiet_cafe"], ids["coworking"], ids["office"], ids["library"], ids["meeting_cafe"]
        scenario["agents"][0]["budget"] = 0
        scenario["agents"][0]["memory_seeds"] = [
            f"Older memory: {old_preference} used to be my default quiet workplace.",
            f"Later memory: construction noise at {old_preference} ruined two sessions; the busy {decoy} also does not work.",
            f"Recent memory: school groups made {library} noisy this week.",
            f"Most recent preference: {unavailable} works best, but when it is unavailable the free quiet focus room at {preferred} is my reliable fallback.",
        ]
        scenario["events"] = [{"time": "10:00", "type": "coworking_unavailable", "location": unavailable, "visibility": "public", "effect": {"closed_until": "13:00"}}]
        scenario["benchmark_metadata"]["memory_access_contract"] = "recall_required_v1"
        scenario["agents"][0]["private_intention"] = "Combine the ordered memories with current availability and today's zero budget. Use the remembered reliable fallback and complete a 10-minute focus block; do not choose an outdated or recently noisy place."
        scenario["critical_locations"] += [old_preference, unavailable, preferred, library, decoy]
        scenario["success_conditions"] = [
            condition("memory_recalled", "recall_memory", "process", .1, min_recalls=1),
            condition("latest_remembered_place", "visit_location", "outcome", .45, location=preferred),
            condition("remembered_focus", "dwell_minutes", "outcome", .35, location_any_of=[preferred], min_minutes=10),
            condition("avoid_outdated_unavailable_busy", "avoid_when_possible", "constraint", .1, avoid_locations=[old_preference, unavailable, library, decoy]),
        ]
        oracle = [{"kind": "recall", "query": "latest reliable fallback workspace"}] + access(preferred) + [{"kind": "dwell", "minutes": 10}, finish]
        negative = access(old_preference) + [{"kind": "buy", "target": old_preference, "item": "tea", "minutes": 2}, {"kind": "dwell", "minutes": 10}, finish]
    elif construct == "social_coordination_copresence":
        cafe = ids["meeting_cafe"]
        scenario["agents"].append({"agent_id": "ben", "persona": "A friend available for the confirmed meeting.", "start_location": cafe, "budget": 20, "private_intention": "Meet Aria.", "known_locations": [cafe], "memory_seeds": []})
        scenario["agents"][0]["budget"] = next((loc.get("typical_cost", 0) or 0 for loc in world["locations"] if loc["id"] == cafe), 0)
        scenario["agents"][0]["private_intention"] = f"Message Ben to confirm, enter {cafe}, buy one refreshment so waiting is permitted, and meet him inside during the narrow 11:00-11:10 window. Stay within the exact {scenario['agents'][0]['budget']}-credit budget."
        scenario["critical_locations"] += [cafe]
        scenario["success_conditions"] = [
            condition("confirm_ben", "send_message", "outcome", .15, to="ben"),
            condition("refreshment", "purchase_at", "outcome", .15, location=cafe, minutes=2),
            condition("meet_ben", "co_presence", "outcome", .5, agents=["aria", "ben"], location_any_of=[cafe], time_window=["11:00", "11:10"]),
            condition("legal_trace", "no_feasibility_violation", "constraint", .2),
        ]
        city = runner.CityWorld(world)
        _, travel = city.shortest_path(home, cafe, scenario, 600)
        wait_minutes = max(1, 660 - (600 + int(travel) + 2))
        oracle = [{"kind": "message", "to": "ben", "content": "Confirmed for 11:00."}] + access(cafe) + [{"kind": "buy", "target": cafe, "item": "refreshment", "minutes": 2}, {"kind": "dwell", "minutes": wait_minutes}, {"kind": "interact", "to": "ben", "minutes": 2}, finish]
        negative = [{"kind": "message", "to": "ben", "content": "Confirmed."}] + access(cafe) + [{"kind": "buy", "target": cafe, "item": "refreshment", "minutes": 2}, {"kind": "interact", "to": "ben", "minutes": 2}, finish]
    elif construct == "multi_party_commitment":
        cafe, park = ids["meeting_cafe"], ids["park"]
        for agent_id, location in (("ben", cafe), ("casey", park)):
            scenario["agents"].append({"agent_id": agent_id, "persona": "A coordination partner.", "start_location": location, "budget": 20, "private_intention": "Meet Aria.", "known_locations": [location], "memory_seeds": []})
        scenario["agents"][0]["private_intention"] = f"Confirm and actually meet Ben inside {cafe} before 12:30, then confirm and meet Casey inside {park} before 12:50. Do not drop either commitment."
        scenario["critical_locations"] += [cafe, park]
        scenario["success_conditions"] = [
            condition("message_ben", "send_message", "outcome", .16, to="ben"),
            condition("meet_ben", "co_presence", "outcome", .24, agents=["aria", "ben"], location_any_of=[cafe], time_window=["10:00", "12:30"]),
            condition("message_casey", "send_message", "outcome", .16, to="casey"),
            condition("meet_casey", "co_presence", "outcome", .24, agents=["aria", "casey"], location_any_of=[park], time_window=["10:00", "12:50"]),
            condition("legal_trace", "no_feasibility_violation", "constraint", .2),
        ]
        oracle = [{"kind": "message", "to": "ben", "content": "Confirmed."}] + access(cafe) + [{"kind": "interact", "to": "ben", "minutes": 2}, {"kind": "message", "to": "casey", "content": "Confirmed."}] + access(park) + [{"kind": "interact", "to": "casey", "minutes": 2}, finish]
        negative = [{"kind": "message", "to": "ben", "content": "Confirmed."}] + access(cafe) + [{"kind": "interact", "to": "ben", "minutes": 2}, finish]
    elif construct == "compound_long_horizon":
        pharmacy, diner = ids["pharmacy"], ids["budget_food"]
        scenario["agents"][0]["private_intention"] = f"Buy medicine at {pharmacy}, obtain a meal at {diner}, and then return inside home before 13:00. Complete all three outcomes."
        scenario["critical_locations"] += [pharmacy, diner]
        scenario["success_conditions"] = [
            condition("medicine", "buy_item", "outcome", .24, location=pharmacy, item="medicine", minutes=3),
            condition("meal", "use_service_at", "outcome", .28, location=diner, service="meal", minutes=5),
            condition("return_home", "visit_before", "outcome", .28, location=home, deadline="13:00", ignore_start=True),
            condition("legal_trace", "no_feasibility_violation", "constraint", .2),
        ]
        oracle = access(pharmacy) + [{"kind": "buy", "target": pharmacy, "item": "medicine", "minutes": 3}] + access(diner) + [{"kind": "use_service", "target": diner, "service": "meal", "minutes": 5}] + access(home) + [finish]
        negative = access(pharmacy) + [{"kind": "buy", "target": pharmacy, "item": "medicine", "minutes": 3}] + access(home) + [finish]
    else:
        raise ValueError(construct)

    return scenario, {"scenario_id": scenario["scenario_id"], "construct_family": construct, "oracle": oracle, "negative": negative}


def generate() -> dict[str, Any]:
    worlds = [load_json(path) for path in WORLD_PATHS]
    scenarios, plans = [], []
    for construct_index, construct in enumerate(CONSTRUCTS):
        for variant in range(2):
            world = worlds[(construct_index + variant) % len(worlds)]
            scenario, plan = build_item(world, construct, variant)
            scenarios.append(scenario)
            plans.append(plan)
    scenario_dir = ROOT / "scenarios"
    scenario_dir.mkdir(parents=True, exist_ok=True)
    for scenario in scenarios:
        (scenario_dir / f"{scenario['scenario_id']}.json").write_text(json.dumps(scenario, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (ROOT / "oracle_negative_plans.json").write_text(json.dumps(plans, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {"scenario_count": len(scenarios), "plan_count": len(plans)}


if __name__ == "__main__":
    print(json.dumps(generate(), sort_keys=True))
