#!/usr/bin/env python3
"""Generate Wave-3 mechanism candidates from the audited Wave-2 action core.

Wave-3 is an oracle-first public calibration pool. Its mechanism contracts are
new and explicitly recorded; empirical promotion is a separate later gate.
"""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
V1_ROOT = ROOT.parent
OUTPUT_ROOT = ROOT / "expansion_wave3"
GENERATOR_VERSION = "cityintent-native-expansion-wave3-1.0.0-design-review"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import generate_expansion_wave2 as wave2  # noqa: E402


MECHANISMS = {
    "disruption_recovery": {
        "id": "resource_aware_fallback_substitution",
        "parameter": "fallback must preserve budget and session duration after closure",
    },
    "time_window_scheduling": {
        "id": "rolling_window_commitment_update",
        "parameter": "agent must defer commitment until a future public window update",
    },
    "resource_budget_allocation": {
        "id": "irreversible_budget_reservation",
        "parameter": "reservation consumes budget before a later required service",
    },
    "poi_availability_service_evidence": {
        "id": "service_evidence_chain",
        "parameter": "arrival, registry evidence, and service completion are distinct",
    },
    "memory_conditioned_preference": {
        "id": "recency_weighted_memory_revision",
        "parameter": "recent memory revises an older preference under current conditions",
    },
    "social_coordination_copresence": {
        "id": "confirmation_then_copresence",
        "parameter": "message confirmation must precede timed co-presence",
    },
    "multi_party_commitment": {
        "id": "priority_aware_commitment_repair",
        "parameter": "one commitment is fulfilled while another is explicitly rescheduled",
    },
    "compound_long_horizon": {
        "id": "dependency_ordered_chain",
        "parameter": "later meeting and return depend on completion of an earlier errand",
    },
}

MECHANISM_CONTRACTS = {
    "disruption_recovery": {
        "state_transition": "public_route_closure_requires_replan",
        "required_evidence": ["replan_after_event", "avoid_blocked_edge", "reach_relocated_target"],
        "negative_failure": "continuing_on_the_pre_event_shortest_path",
    },
    "time_window_scheduling": {
        "state_transition": "future_window_is_not_known_until_update",
        "required_evidence": ["first_window", "second_window", "episode_complete_before"],
        "negative_failure": "committing_to_stale_window_order",
    },
    "resource_budget_allocation": {
        "state_transition": "reservation_consumes_budget_before_service",
        "required_evidence": ["reservation_token", "training", "budget"],
        "negative_failure": "spending_reserved_budget_on_optional_item",
    },
    "poi_availability_service_evidence": {
        "state_transition": "registry_evidence_precedes_service_completion",
        "required_evidence": ["registry_evidence", "identity_verification"],
        "negative_failure": "arrival_without_registered_service",
    },
    "memory_conditioned_preference": {
        "state_transition": "recent_conditional_memory_overrides_old_default",
        "required_evidence": ["recall_rule", "conditional_choice", "reset"],
        "negative_failure": "using_stale_default_under_alert",
    },
    "social_coordination_copresence": {
        "state_transition": "confirmation_precedes_timed_copresence",
        "required_evidence": ["confirm", "relocated_meeting"],
        "negative_failure": "arriving_without_confirmation_at_stale_venue",
    },
    "multi_party_commitment": {
        "state_transition": "priority_commitment_fulfilled_and_competing_one_rescheduled",
        "required_evidence": ["confirm_ben", "renegotiate_casey", "meet_ben"],
        "negative_failure": "silent_drop_of_competing_commitment",
    },
    "compound_long_horizon": {
        "state_transition": "gated_prerequisite_unlocks_later_meeting_and_return",
        "required_evidence": ["medicine", "confirm", "meet", "return"],
        "negative_failure": "meeting_or_return_without_prerequisite",
    },
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def build_item(world: dict[str, Any], construct: str, variant: int) -> tuple[dict[str, Any], dict[str, Any]]:
    scenario, plan = wave2.build_item(world, construct, variant)
    scenario = copy.deepcopy(scenario)
    plan = copy.deepcopy(plan)
    mechanism = MECHANISMS[construct]
    scenario["scenario_id"] = f"ci11w3_{construct[:4]}_{world['world_id']}_v{variant}"
    scenario["title"] = f"Wave 3 {mechanism['id'].replace('_', ' ').title()}"
    metadata = scenario["benchmark_metadata"]
    metadata.update({
        "benchmark_version": "1.1.0-expansion-wave3",
        "candidate_status": "mechanism_distinctness_review_pending",
        "split": "calibration_public",
        "difficulty_tier": ("medium", "hard", "hard")[variant],
        "template_id": f"wave3_{mechanism['id']}",
        "mechanism_id": mechanism["id"],
        "mechanism_parameter": mechanism["parameter"],
        "generator_version": GENERATOR_VERSION,
        "parent_generator_version": metadata.get("generator_version"),
        "world_visibility": world["release_visibility"],
        "seed": int(hashlib.sha256(
            f"{GENERATOR_VERSION}|{construct}|{world['world_id']}|{variant}".encode()
        ).hexdigest()[:12], 16),
        "mechanism_contract": copy.deepcopy(MECHANISM_CONTRACTS[construct]),
    })
    scenario["public_context"] = (
        scenario.get("public_context", "")
        + " Mechanism contract: "
        + mechanism["parameter"]
        + "."
    )
    scenario["agents"][0]["private_intention"] += (
        " The decision must preserve the mechanism contract: "
        + mechanism["parameter"]
        + "."
    )

    # Wave-3 changes the state/evidence contract, rather than only relabeling
    # the Wave-2 item. These edits remain within the native trace protocol.
    if construct == "disruption_recovery":
        city = wave2.pilot.runner.CityWorld(world)
        home = wave2.pilot.role_map(world)["home_primary"]
        target = wave2.pilot.role_map(world)["clinic"]
        path, _ = city.shortest_path(home, target, scenario, 620, avoid_active_blocks=False)
        blocked_edge = None
        for edge in zip(path, path[1:]):
            probe = copy.deepcopy(scenario)
            probe["events"] = [{"time": "10:20", "effect": {"blocked_edge": list(edge), "until": "12:00"}}]
            _, alternate_minutes = city.shortest_path(home, target, probe, 620)
            if alternate_minutes != float("inf"):
                blocked_edge = edge
                break
        if blocked_edge:
            scenario["events"] = [{
                "time": "10:20", "type": "route_closure", "location": blocked_edge[1],
                "visibility": "public", "effect": {
                    "blocked_edge": list(blocked_edge), "until": "12:00",
                    "replacement_destination": target,
                },
            }]
            scenario["success_conditions"] = [
                wave2.pilot.condition("replan_after_event", "replan_after_event", "process", .25, event_id="route_closure"),
                wave2.pilot.condition("avoid_blocked_edge", "avoid_blocked_edge", "constraint", .20, edge=list(blocked_edge), time_window=["10:20", "12:00"]),
                wave2.pilot.condition("reach_relocated_target", "visit_before", "outcome", .35, location=target, deadline="11:30", ignore_start=True),
                wave2.pilot.condition("legal_trace", "no_feasibility_violation", "constraint", .20),
            ]
            plan["oracle"] = [{"kind": "dwell", "minutes": 20}] + wave2.pilot.access(target) + [{"kind": "finish"}]
            plan["negative"] = [{"kind": "dwell", "minutes": 20}, {"kind": "finish"}]
        else:
            raise ValueError(f"world {world['world_id']} has no reroutable edge to {target}")
    elif construct == "resource_budget_allocation":
        role_ids = wave2.pilot.role_map(world)
        market, gym = role_ids["market"], role_ids["gym"]
        decoys = [role_ids["pharmacy"], role_ids["quiet_cafe"]]
        scenario["critical_locations"] = list(dict.fromkeys(scenario["critical_locations"] + [market, gym, *decoys]))
        scenario["success_conditions"] = [
            wave2.pilot.condition(
                "reservation_token",
                "purchase_after_time",
                "outcome", .35, location=market, item="reservation_token", minutes=1,
                after="10:10",
            ),
            wave2.pilot.condition(
                "training", "use_service_at", "outcome", .35, location=gym,
                minutes=5,
            ),
            wave2.pilot.condition("return_home", "visit_before", "outcome", .15, location=role_ids["home_primary"], deadline="13:00", ignore_start=True),
            wave2.pilot.condition("budget", "budget_at_least", "constraint", .15, agent="aria", min_remaining=0),
        ]
        plan["oracle"] = wave2.pilot.access(market) + [{"kind": "buy", "target": market, "item": "reservation_token", "minutes": 1}] + wave2.pilot.access(gym) + [{"kind": "use_service", "target": gym, "service": "booked_training", "minutes": 5}] + wave2.pilot.access(role_ids["home_primary"]) + [{"kind": "finish"}]
        plan["negative"] = wave2.pilot.access(market) + [{"kind": "buy", "target": market, "item": "optional", "minutes": 2}] + wave2.pilot.access(gym) + [{"kind": "use_service", "target": gym, "service": "booked_training", "minutes": 5}, {"kind": "finish"}]
        scenario["benchmark_metadata"]["candidate_status"] = "actor_hardened_resource_update"
        scenario["events"] = [{
            "time": "10:10", "type": "reservation_price_update", "location": market,
            "visibility": "public", "effect": {
                "reservation_allowed": True, "reservation_location": market,
            },
        }]
        scenario["agents"][0]["private_intention"] = (
            "Wait for the public reservation-price update at 10:10. It will identify the "
            f"reservation_location from the plausible candidates {market}, {decoys[0]}, and {decoys[1]}. "
            "After the update, buy an item explicitly labeled reservation_token at its "
            f"reservation_location, complete a training service at {gym}, and return inside "
            f"{role_ids['home_primary']} before 13:00 without exceeding the budget."
        )
        plan["oracle"] = [{"kind": "dwell", "minutes": 10}] + plan["oracle"]
    elif construct == "poi_availability_service_evidence":
        correct = wave2.pilot.role_map(world)["office"]
        scenario["success_conditions"] = [
            wave2.pilot.condition("registry_evidence", "obtain_at", "process", .25, location=correct, service="identity_verification", deadline="12:00"),
            wave2.pilot.condition("identity_verification", "use_service_at", "outcome", .55, location=correct, service="identity_verification", deadline="12:00", minutes=5),
            wave2.pilot.condition("legal_trace", "no_feasibility_violation", "constraint", .20),
        ]
        plan["oracle"] = [{"kind": "dwell", "minutes": 10}] + wave2.pilot.access(correct) + [{"kind": "use_service", "target": correct, "service": "identity_verification", "minutes": 5}, {"kind": "finish"}]
        plan["negative"] = [{"kind": "dwell", "minutes": 10}] + wave2.pilot.access(correct) + [{"kind": "finish"}]
    elif construct == "time_window_scheduling":
        scenario["events"] = [{
            "time": "10:05", "type": "rolling_window_update", "location": None,
            "visibility": "public", "effect": {"window_policy": "ordered_after_update"},
        }]
        scenario["success_conditions"].append(
            wave2.pilot.condition("finish_episode", "episode_complete_before", "constraint", .10, deadline="13:00")
        )
        # Keep the original two-window weights coherent after adding the deadline.
        for condition in scenario["success_conditions"]:
            if condition["id"] in {"first_window", "second_window"}:
                condition["weight"] = .35
            elif condition["id"] == "legal_trace":
                condition["weight"] = .20
        if variant == 1:
            scenario["agents"][0]["private_intention"] = scenario["agents"][0]["private_intention"].replace(
                "10:29-10:34", "10:29-10:30"
            )
            next(condition for condition in scenario["success_conditions"] if condition["id"] == "second_window")["time_window"] = ["10:29", "10:30"]
            scenario["benchmark_metadata"]["candidate_status"] = "actor_hardened_v1"
            last_dwell = max(index for index, action in enumerate(plan["oracle"]) if action.get("kind") == "dwell")
            minutes = int(plan["oracle"][last_dwell]["minutes"])
            plan["oracle"][last_dwell:last_dwell + 1] = [
                {"kind": "dwell", "minutes": 1},
                {"kind": "dwell", "minutes": max(1, minutes - 1)},
            ]
    elif construct == "memory_conditioned_preference":
        scenario["success_conditions"] = [
            wave2.pilot.condition("recall_rule", "recall_memory", "process", .20, min_recalls=2),
            wave2.pilot.condition("conditional_choice", "visit_location", "outcome", .35, location=wave2.pilot.role_map(world)["office"]),
            wave2.pilot.condition("reset", "dwell_minutes", "outcome", .30, location_any_of=[wave2.pilot.role_map(world)["office"]], min_minutes=10),
            wave2.pilot.condition("avoid_alert", "avoid_when_possible", "constraint", .15, avoid_locations=[wave2.pilot.role_map(world)["park"], wave2.pilot.role_map(world)["quiet_cafe"]]),
        ]
        scenario["agents"][0]["memory_seeds"].append("Revision note: apply the conditional rule only after recalling both the trigger and the fallback.")
        plan["oracle"] = [
            {"kind": "recall", "query": "conditional place rule under current alert"},
            {"kind": "recall", "query": "alert fallback indoor location"},
        ] + wave2.pilot.access(wave2.pilot.role_map(world)["office"]) + [{"kind": "dwell", "minutes": 10}, {"kind": "finish"}]
        plan["negative"] = [{"kind": "recall", "query": "old default"}] + wave2.pilot.access(wave2.pilot.role_map(world)["park"]) + [{"kind": "dwell", "minutes": 10}, {"kind": "finish"}]
    elif construct == "compound_long_horizon":
        pharmacy = wave2.pilot.role_map(world)["pharmacy"]
        scenario["success_conditions"] = [
            wave2.pilot.condition("medicine", "use_service_at", "outcome", .20, location=pharmacy, service="medication_pickup", minutes=3),
            *[condition for condition in scenario["success_conditions"] if condition["id"] in {"confirm", "meet", "return", "legal_trace"}],
        ]
        scenario["agents"][0]["private_intention"] = scenario["agents"][0]["private_intention"].replace("Buy medicine", "Complete the medication-pickup service")
        if variant == 1:
            scenario["agents"][0]["private_intention"] = scenario["agents"][0]["private_intention"].replace(
                "11:00-11:20", "11:00-11:30"
            )
            next(condition for condition in scenario["success_conditions"] if condition["id"] == "meet")["time_window"] = ["11:00", "11:30"]
            scenario["benchmark_metadata"]["candidate_status"] = "actor_hardened_v1"
        for action in plan["oracle"]:
            if action.get("kind") == "buy" and action.get("target") == pharmacy:
                action.update({"kind": "use_service", "service": "medication_pickup"})
        for action in plan["negative"]:
            if action.get("kind") == "buy" and action.get("target") == pharmacy:
                action.update({"kind": "use_service", "service": "medication_pickup"})
    elif construct == "social_coordination_copresence":
        scenario["events"].append({
            "time": "10:25", "type": "confirmation_deadline", "location": None,
            "visibility": "public", "effect": {"required_before": "timed_copresence", "recipient": "ben"},
        })
        scenario["benchmark_metadata"]["ordering_contract"] = "message_confirmation_before_interaction"
        for condition in scenario["success_conditions"]:
            if condition["id"] == "confirm":
                condition["type"] = "message_before_interaction"
    elif construct == "multi_party_commitment":
        scenario["events"].append({
            "time": "10:30", "type": "commitment_priority_update", "location": None,
            "visibility": "public", "effect": {"priority_agent": "ben", "reschedule_agent": "casey"},
        })
        scenario["benchmark_metadata"]["ordering_contract"] = "fulfill_priority_then_reschedule_competing_commitment"
        for condition in scenario["success_conditions"]:
            if condition["id"] in {"confirm_ben", "renegotiate_casey"}:
                condition["type"] = "send_message_after"
                condition["after"] = "10:30"
        for action in plan["oracle"]:
            if action.get("kind") == "dwell":
                action["minutes"] = max(1, int(action["minutes"]) - 30)
        plan["oracle"] = [{"kind": "dwell", "minutes": 30}] + plan["oracle"]
    plan["scenario_id"] = scenario["scenario_id"]
    return scenario, plan


def generate(output_root: Path = OUTPUT_ROOT) -> dict[str, Any]:
    output_root = output_root.resolve()
    worlds = [load_json(path) for path in sorted((V1_ROOT / "worlds" / "public").glob("*.json"))]
    scenarios: list[dict[str, Any]] = []
    plans: list[dict[str, Any]] = []
    for construct_index, construct in enumerate(wave2.pilot.CONSTRUCTS):
        for variant in range(3):
            world = worlds[(construct_index + variant) % len(worlds)]
            scenario, plan = build_item(world, construct, variant)
            scenarios.append(scenario)
            plans.append(plan)

    scenario_dir = output_root / "scenarios"
    scenario_dir.mkdir(parents=True, exist_ok=True)
    expected = {scenario_dir / f"{row['scenario_id']}.json" for row in scenarios}
    stale = set(scenario_dir.glob("*.json")) - expected
    if stale:
        raise RuntimeError(f"stale scenario files require explicit removal: {sorted(stale)}")
    for scenario in scenarios:
        (scenario_dir / f"{scenario['scenario_id']}.json").write_text(
            json.dumps(scenario, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
    (output_root / "oracle_negative_plans.json").write_text(
        json.dumps(plans, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    config = {
        "benchmark_id": "cityintent_v1_1_expansion_wave3",
        "version": "1.1.0-expansion-wave3",
        "status": "mechanism_distinctness_review_pending_not_release",
        "worlds": [str(path.resolve().relative_to(output_root, walk_up=True)) for path in sorted((V1_ROOT / "worlds" / "public").glob("*.json"))],
        "scenario_dir": "scenarios",
        "agents_under_test": [{"id": value} for value in ("utility_planner", "llm_direct_actor", "reactive_replanner", "memory_reflection")],
        "validation": {"min_scenarios": 24},
    }
    (output_root / "benchmark_config.json").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    manifest = {
        "schema_version": "cityintent_native_expansion_wave3_v1",
        "generator_version": GENERATOR_VERSION,
        "status": "mechanism_distinctness_review_pending_not_release",
        "scenario_count": len(scenarios),
        "construct_counts": dict(sorted(Counter(row["family"] for row in scenarios).items())),
        "mechanisms": {key: value["id"] for key, value in MECHANISMS.items()},
        "mechanism_contracts": copy.deepcopy(MECHANISM_CONTRACTS),
        "scenario_matrix_sha256": hashlib.sha256("\n".join(sorted(json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=False) for row in scenarios)).encode()).hexdigest(),
    }
    (output_root / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


if __name__ == "__main__":
    print(json.dumps(generate(), sort_keys=True))
