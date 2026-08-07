#!/usr/bin/env python3
"""Generate Wave-4 mechanism candidates from the audited Wave-4 design contract.

Wave-4 supplies the fourth independent public mechanism for every construct
family. Unlike Wave-3, these items are built directly on the native base
scenario rather than by mutating a prior wave, because every mechanism
introduces a state transition that has no Wave-2/Wave-3 counterpart.

This module is oracle-first: each item ships a deterministic oracle plan and a
mechanism-matched negative plan, and it is only calibration evidence until the
public six-system gate and the cross-world promotion audit accept it.
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
OUTPUT_ROOT = ROOT / "expansion_wave4"
GENERATOR_VERSION = "cityintent-native-expansion-wave4-1.0.0-design-review"
DESIGN_PATH = ROOT / "wave4_mechanism_design.json"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import generate_native_pilot as pilot  # noqa: E402


EPISODE_START = 600


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


DESIGN = load_json(DESIGN_PATH)


def costs(world: dict[str, Any]) -> dict[str, float]:
    return {
        location["id"]: float(location.get("typical_cost") or 0)
        for location in world["locations"]
    }


def set_metadata(scenario: dict[str, Any], construct: str, world: dict[str, Any], variant: int) -> None:
    design = DESIGN["constructs"][construct]
    metadata = scenario["benchmark_metadata"]
    metadata.update({
        "benchmark_version": "1.1.0-expansion-wave4",
        "candidate_status": "mechanism_distinctness_review_pending",
        "split": "calibration_public",
        "difficulty_tier": ("medium", "hard", "hard")[variant],
        "template_id": f"wave4_{design['mechanism_id']}",
        "mechanism_id": design["mechanism_id"],
        "mechanism_parameter": design["state_transition"],
        "generator_version": GENERATOR_VERSION,
        "parent_generator_version": metadata.get("generator_version"),
        "world_visibility": world["release_visibility"],
        "seed": int(hashlib.sha256(
            f"{GENERATOR_VERSION}|{construct}|{world['world_id']}|{variant}".encode()
        ).hexdigest()[:12], 16),
        "mechanism_contract": {
            "state_transition": design["state_transition"],
            "required_actions": list(design["required_actions"]),
            "required_conditions": list(design["required_conditions"]),
            "negative_failure": design["negative_failure"],
            "novelty_against": copy.deepcopy(design["novelty_against"]),
        },
    })


def travel(city: Any, scenario: dict[str, Any], start: str, goal: str, at_time: int) -> int:
    _, minutes = city.shortest_path(start, goal, scenario, at_time)
    if minutes == float("inf"):
        raise ValueError(f"no route from {start} to {goal}")
    return int(minutes)


def build_item(world: dict[str, Any], construct: str, variant: int) -> tuple[dict[str, Any], dict[str, Any]]:
    ids = pilot.role_map(world)
    scenario = pilot.base_scenario(world, construct, variant, max_steps=18)
    scenario["scenario_id"] = f"ci11w4_{construct[:4]}_{world['world_id']}_v{variant}"
    design = DESIGN["constructs"][construct]
    scenario["title"] = f"Wave 4 {design['mechanism_id'].replace('_', ' ').title()}"
    set_metadata(scenario, construct, world, variant)
    home = ids["home_primary"]
    finish = {"kind": "finish"}
    city = pilot.runner.CityWorld(world)
    world_costs = costs(world)

    if construct == "disruption_recovery":
        # A required service goes down and later recovers. Arriving on the naive
        # schedule lands inside the outage; the only winning move is to wait for
        # the recovery update and still beat the deadline.
        service_location = ids["clinic"]
        leg = travel(city, scenario, home, service_location, EPISODE_START)
        naive_entry = EPISODE_START + leg + 1
        outage_start = naive_entry + 1
        recovery = outage_start + 30
        wait = recovery - (EPISODE_START + leg + 1)
        completion = EPISODE_START + wait + leg + 1 + 5
        deadline = completion + 15
        scenario["agents"][0]["budget"] = world_costs[service_location]
        scenario["events"] = [{
            "time": pilot.fmt(outage_start), "type": "service_outage",
            "location": service_location, "visibility": "public",
            "effect": {
                "closed_until": pilot.fmt(recovery),
                "service_unavailable": "appointment",
                "recovers_at": pilot.fmt(recovery),
            },
        }]
        scenario["agents"][0]["private_intention"] = (
            f"Complete the appointment service inside {service_location}. A public outage "
            f"at {pilot.fmt(outage_start)} takes that service down until {pilot.fmt(recovery)}; "
            f"travelling straight there arrives inside the outage. Wait for the recovery, then "
            f"produce appointment-service evidence at {service_location} no later than "
            f"{pilot.fmt(deadline)}. Service evidence produced before the recovery does not count."
        )
        scenario["critical_locations"] += [service_location]
        scenario["success_conditions"] = [
            pilot.condition(
                "recovered_service", "service_after_recovery", "outcome", .55,
                location=service_location, service="appointment",
                after=pilot.fmt(recovery), deadline=pilot.fmt(deadline), minutes=5,
            ),
            pilot.condition("finish_episode", "episode_complete_before", "constraint", .25, deadline=pilot.fmt(deadline)),
            pilot.condition("legal_trace", "no_feasibility_violation", "constraint", .20),
        ]
        oracle = (
            [{"kind": "dwell", "minutes": wait}]
            + pilot.access(service_location)
            + [{"kind": "use_service", "target": service_location, "service": "appointment", "minutes": 5}, finish]
        )
        negative = (
            pilot.access(service_location)
            + [{"kind": "use_service", "target": service_location, "service": "appointment", "minutes": 5}, finish]
        )

    elif construct == "time_window_scheduling":
        # A broad arrival window contains a narrower interval inside which a
        # minimum dwell must accumulate. Arriving early is not enough.
        venue = ids["library"]
        leg = travel(city, scenario, home, venue, EPISODE_START)
        arrival = EPISODE_START + leg + 1
        narrow_start = arrival + 10
        narrow_end = narrow_start + 20
        broad_start = arrival
        broad_end = narrow_end + 20
        min_minutes = 15
        scenario["agents"][0]["budget"] = 0
        scenario["agents"][0]["private_intention"] = (
            f"Be inside the free venue {venue} at some point during the broad window "
            f"{pilot.fmt(broad_start)}-{pilot.fmt(broad_end)}, and accumulate at least "
            f"{min_minutes} minutes of dwell inside the narrower interval "
            f"{pilot.fmt(narrow_start)}-{pilot.fmt(narrow_end)}. Dwell before "
            f"{pilot.fmt(narrow_start)} does not count toward the requirement."
        )
        scenario["critical_locations"] += [venue]
        scenario["success_conditions"] = [
            pilot.condition(
                "broad_arrival", "visit_open_location", "outcome", .25,
                location_any_of=[venue], time_window=[pilot.fmt(broad_start), pilot.fmt(broad_end)],
            ),
            pilot.condition(
                "nested_duration", "dwell_within_window", "outcome", .55,
                location=venue, time_window=[pilot.fmt(narrow_start), pilot.fmt(narrow_end)],
                min_minutes=min_minutes,
            ),
            pilot.condition("legal_trace", "no_feasibility_violation", "constraint", .20),
        ]
        oracle = pilot.access(venue) + [
            {"kind": "dwell", "minutes": narrow_start - arrival},
            {"kind": "dwell", "minutes": min_minutes},
            finish,
        ]
        negative = pilot.access(venue) + [{"kind": "dwell", "minutes": min_minutes}, finish]

    elif construct == "resource_budget_allocation":
        # The first purchase consumes the only inventory claim. Spending it on the
        # decoy leaves the downstream service unaffordable.
        market, gym = ids["market"], ids["gym"]
        budget = world_costs[market] + world_costs[gym]
        decoys = sorted(
            (world_costs[ids[role]], ids[role])
            for role in (
                "meeting_cafe", "coworking", "clinic", "quiet_cafe",
                "budget_food", "pharmacy", "bookstore", "culture",
            )
            if world_costs[ids[role]] <= budget
            and budget - world_costs[ids[role]] < world_costs[gym]
            and city.is_open(ids[role], EPISODE_START + 30, scenario)
        )
        if not decoys:
            raise ValueError(f"world {world['world_id']} has no affordability-breaking open decoy")
        decoy_cost, decoy = decoys[0]
        scenario["agents"][0]["budget"] = budget
        scenario["agents"][0]["private_intention"] = (
            f"You hold exactly {budget:g} credits and one inventory claim. Buy the item labeled "
            f"inventory_claim at {market}, then complete the booked_training service at {gym}. "
            f"Spending the claim at {decoy} (which costs {decoy_cost:g}) leaves too little for the "
            "training, so the first purchase decides whether the second step is still affordable. "
            "Keep the remaining budget at or above zero."
        )
        scenario["critical_locations"] += [market, gym, decoy]
        scenario["success_conditions"] = [
            pilot.condition("inventory_claim", "buy_item", "outcome", .30, location=market, item="inventory_claim", minutes=3),
            pilot.condition("downstream_training", "use_service_at", "outcome", .30, location=gym, service="booked_training", minutes=5),
            pilot.condition("budget", "budget_at_least", "constraint", .20, agent="aria", min_remaining=0),
            pilot.condition("legal_trace", "no_feasibility_violation", "constraint", .20),
        ]
        oracle = (
            pilot.access(market)
            + [{"kind": "buy", "target": market, "item": "inventory_claim", "minutes": 3}]
            + pilot.access(gym)
            + [{"kind": "use_service", "target": gym, "service": "booked_training", "minutes": 5}, finish]
        )
        negative = (
            pilot.access(decoy)
            + [{"kind": "buy", "target": decoy, "item": "inventory_claim", "minutes": 3}]
            + pilot.access(gym)
            + [{"kind": "use_service", "target": gym, "service": "booked_training", "minutes": 5}, finish]
        )

    elif construct == "poi_availability_service_evidence":
        # A referral service produces the evidence that unlocks a second provider
        # service elsewhere. Order is the mechanism.
        referral, provider = ids["civic_service"], ids["office"]
        leg1 = travel(city, scenario, home, referral, EPISODE_START)
        after_referral = EPISODE_START + leg1 + 1 + 4
        leg2 = travel(city, scenario, referral, provider, after_referral)
        completion = after_referral + leg2 + 1 + 5
        deadline = completion + 15
        scenario["agents"][0]["budget"] = 0
        scenario["agents"][0]["private_intention"] = (
            f"Complete the provider service at {provider}, which is only valid once a referral "
            f"exists. First obtain the referral service at {referral}, then use the "
            f"provider_consultation service at {provider} no later than {pilot.fmt(deadline)}. "
            "Using the provider without prior referral evidence does not count."
        )
        scenario["critical_locations"] += [referral, provider]
        scenario["success_conditions"] = [
            pilot.condition(
                "referral_then_provider", "ordered_service_chain", "outcome", .55,
                steps=[
                    {"location": referral, "service": "referral"},
                    {"location": provider, "service": "provider_consultation"},
                ],
            ),
            pilot.condition(
                "provider_evidence", "use_service_at", "outcome", .25,
                location=provider, service="provider_consultation",
                deadline=pilot.fmt(deadline), minutes=5,
            ),
            pilot.condition("legal_trace", "no_feasibility_violation", "constraint", .20),
        ]
        oracle = (
            pilot.access(referral)
            + [{"kind": "use_service", "target": referral, "service": "referral", "minutes": 4}]
            + pilot.access(provider)
            + [{"kind": "use_service", "target": provider, "service": "provider_consultation", "minutes": 5}, finish]
        )
        negative = (
            pilot.access(provider)
            + [{"kind": "use_service", "target": provider, "service": "provider_consultation", "minutes": 5}, finish]
        )

    elif construct == "memory_conditioned_preference":
        # Two recalled memories conflict. The reliable-tagged source wins, even
        # though the unreliable one is more recent.
        # Both candidates are free study spaces, so the negative fails purely on
        # source arbitration rather than on an incidental budget violation.
        reliable, unreliable = ids["library"], ids["office"]
        scenario["agents"][0]["budget"] = 0
        scenario["agents"][0]["memory_seeds"] = [
            f"Verified notice (source: city service bulletin, tagged reliable): the quiet study "
            f"room is at {reliable} today.",
            f"Later chat message (source: unverified group thread, tagged unreliable): someone "
            f"said the study room moved to {unreliable}.",
            "Arbitration rule: when two recalled sources conflict, follow the source tagged "
            "reliable, even if the unreliable one is more recent.",
        ]
        scenario["benchmark_metadata"]["memory_access_contract"] = "recall_required_v1"
        scenario["agents"][0]["private_intention"] = (
            "Recall both the verified notice and the later unverified message, apply the "
            "arbitration rule, and complete a 10-minute free study session at the location named "
            "by the reliable source. The more recent unreliable source must not be followed."
        )
        scenario["critical_locations"] += [reliable, unreliable]
        scenario["success_conditions"] = [
            pilot.condition("recall_both_sources", "recall_memory", "process", .20, min_recalls=2),
            pilot.condition("reliable_source_choice", "visit_location", "outcome", .35, location=reliable),
            pilot.condition("study_session", "dwell_minutes", "outcome", .30, location_any_of=[reliable], min_minutes=10),
            pilot.condition("reject_unreliable", "avoid_when_possible", "constraint", .15, avoid_locations=[unreliable]),
        ]
        oracle = [
            {"kind": "recall", "query": "verified notice about the study room"},
            {"kind": "recall", "query": "later unverified message about the study room"},
        ] + pilot.access(reliable) + [{"kind": "dwell", "minutes": 10}, finish]
        # The negative does the recall work and still follows the newer,
        # explicitly unreliable source: an arbitration failure, not a lazy one.
        negative = [
            {"kind": "recall", "query": "verified notice about the study room"},
            {"kind": "recall", "query": "later unverified message about the study room"},
        ] + pilot.access(unreliable) + [{"kind": "dwell", "minutes": 10}, finish]

    elif construct == "social_coordination_copresence":
        # A confirmation message authorizes a timed physical handoff. Meeting
        # without the item is not the outcome.
        market, venue = ids["market"], ids["plaza"]
        scenario["agents"].append({
            "agent_id": "ben", "persona": "A friend waiting for a parcel handoff.",
            "start_location": venue, "budget": 0,
            "private_intention": "Receive the parcel from Aria at the agreed spot.",
            "known_locations": [venue], "memory_seeds": [],
        })
        scenario["agents"][0]["budget"] = world_costs[market]
        leg1 = travel(city, scenario, home, market, EPISODE_START + 2)
        after_buy = EPISODE_START + 2 + leg1 + 1 + 3
        leg2 = travel(city, scenario, market, venue, after_buy)
        arrival = after_buy + leg2 + 1
        window_start = arrival
        window_end = arrival + 20
        scenario["events"] = [{
            "time": pilot.fmt(window_start), "type": "handoff_window",
            "location": venue, "visibility": "public",
            "effect": {"agents_present": ["ben"], "requires_item": "parcel"},
        }]
        scenario["agents"][0]["private_intention"] = (
            f"Message Ben to acknowledge the handoff, buy the item labeled parcel at {market}, "
            f"then hand it over in person at {venue} during "
            f"{pilot.fmt(window_start)}-{pilot.fmt(window_end)}. The acknowledgement must be sent "
            "before the meeting, and meeting Ben without having acquired the parcel is not the "
            "required outcome."
        )
        scenario["critical_locations"] += [market, venue]
        scenario["success_conditions"] = [
            pilot.condition("acknowledge_first", "message_before_interaction", "process", .20, to="ben"),
            pilot.condition(
                "parcel_handoff", "handoff_evidence", "outcome", .35,
                item_location=market, item="parcel", to="ben", interaction_location=venue,
            ),
            pilot.condition(
                "handoff_copresence", "co_presence", "outcome", .30,
                agents=["aria", "ben"], location_any_of=[venue],
                time_window=[pilot.fmt(window_start), pilot.fmt(window_end)],
            ),
            pilot.condition("legal_trace", "no_feasibility_violation", "constraint", .15),
        ]
        oracle = (
            [{"kind": "message", "to": "ben", "content": "Acknowledged; bringing the parcel."}]
            + pilot.access(market)
            + [{"kind": "buy", "target": market, "item": "parcel", "minutes": 3}]
            + pilot.access(venue)
            + [{"kind": "interact", "to": "ben", "minutes": 2}, finish]
        )
        negative = (
            [{"kind": "message", "to": "ben", "content": "Acknowledged; on my way."}]
            + pilot.access(venue)
            + [{"kind": "dwell", "minutes": max(1, window_start - (EPISODE_START + 2 + travel(city, scenario, home, venue, EPISODE_START + 2) + 1))},
               {"kind": "interact", "to": "ben", "minutes": 2}, finish]
        )

    elif construct == "multi_party_commitment":
        # Evidence from the first timed meeting must be carried into a second
        # meeting with another partner. Order is the mechanism.
        first_venue, second_venue = ids["office"], ids["plaza"]
        for agent_id, location, role in (("ben", first_venue, "first"), ("casey", second_venue, "second")):
            scenario["agents"].append({
                "agent_id": agent_id, "persona": f"The {role} relay partner.",
                "start_location": location, "budget": 0,
                "private_intention": f"Complete the relay step with Aria at {location}.",
                "known_locations": [location], "memory_seeds": [],
            })
        scenario["agents"][0]["budget"] = 0
        leg1 = travel(city, scenario, home, first_venue, EPISODE_START + 2)
        first_arrival = EPISODE_START + 2 + leg1 + 1
        first_end = first_arrival + 2
        leg2 = travel(city, scenario, first_venue, second_venue, first_end)
        second_arrival = first_end + leg2 + 1
        first_window = [pilot.fmt(first_arrival), pilot.fmt(first_arrival + 20)]
        second_window = [pilot.fmt(second_arrival), pilot.fmt(second_arrival + 20)]
        deadline = second_arrival + 30
        scenario["events"] = [
            {
                "time": pilot.fmt(first_arrival), "type": "relay_first_leg",
                "location": first_venue, "visibility": "public",
                "effect": {"agents_present": ["ben"], "relay_step": "collect_confirmation"},
            },
            {
                "time": pilot.fmt(second_arrival), "type": "relay_second_leg",
                "location": second_venue, "visibility": "public",
                "effect": {"agents_present": ["casey"], "relay_step": "deliver_confirmation"},
            },
        ]
        scenario["agents"][0]["private_intention"] = (
            f"Run a two-party relay in order. Message both partners, meet Ben inside "
            f"{first_venue} during {first_window[0]}-{first_window[1]} to collect the "
            f"confirmation, then carry it to Casey inside {second_venue} during "
            f"{second_window[0]}-{second_window[1]} and finish before {pilot.fmt(deadline)}. "
            "Completing only one meeting, or reversing the relay order, fails the relay."
        )
        scenario["critical_locations"] += [first_venue, second_venue]
        scenario["success_conditions"] = [
            pilot.condition(
                "relay_order", "ordered_interaction_chain", "outcome", .45,
                steps=[
                    {"to": "ben", "location": first_venue, "time_window": first_window},
                    {"to": "casey", "location": second_venue, "time_window": second_window},
                ],
            ),
            pilot.condition(
                "relay_second_meeting", "co_presence", "outcome", .20,
                agents=["aria", "casey"], location_any_of=[second_venue],
                time_window=second_window,
            ),
            pilot.condition(
                "relay_first_meeting", "co_presence", "outcome", .15,
                agents=["aria", "ben"], location_any_of=[first_venue],
                time_window=first_window,
            ),
            pilot.condition("finish_episode", "episode_complete_before", "constraint", .10, deadline=pilot.fmt(deadline)),
            pilot.condition("legal_trace", "no_feasibility_violation", "constraint", .10),
        ]
        oracle = (
            [{"kind": "message", "to": "ben", "content": "Confirmed; collecting first."},
             {"kind": "message", "to": "casey", "content": "Confirmed; delivering after Ben."}]
            + pilot.access(first_venue)
            + [{"kind": "interact", "to": "ben", "minutes": 2}]
            + pilot.access(second_venue)
            + [{"kind": "interact", "to": "casey", "minutes": 2}, finish]
        )
        negative = (
            [{"kind": "message", "to": "ben", "content": "Confirmed."},
             {"kind": "message", "to": "casey", "content": "Confirmed."}]
            + pilot.access(first_venue)
            + [{"kind": "interact", "to": "ben", "minutes": 2}, finish]
        )

    elif construct == "compound_long_horizon":
        # A credential unlocks a labeled purchase, which unlocks a timed service
        # before the return leg. Every link is required, in order.
        credential, purchase, service = ids["civic_service"], ids["market"], ids["gym"]
        scenario["agents"][0]["budget"] = world_costs[purchase] + world_costs[service]
        leg1 = travel(city, scenario, home, credential, EPISODE_START)
        after_credential = EPISODE_START + leg1 + 1 + 4
        leg2 = travel(city, scenario, credential, purchase, after_credential)
        after_purchase = after_credential + leg2 + 1 + 3
        leg3 = travel(city, scenario, purchase, service, after_purchase)
        after_service = after_purchase + leg3 + 1 + 5
        leg4 = travel(city, scenario, service, home, after_service)
        return_deadline = after_service + leg4 + 1 + 20
        scenario["agents"][0]["private_intention"] = (
            f"Execute the full chain in order: obtain the credential service at {credential}, "
            f"use it to buy the item labeled permit at {purchase}, complete the booked_training "
            f"service at {service}, and return inside {home} before "
            f"{pilot.fmt(return_deadline)}. Skipping the credential, or running the "
            "purchase/service steps out of order, breaks the chain."
        )
        scenario["critical_locations"] += [credential, purchase, service]
        scenario["success_conditions"] = [
            pilot.condition(
                "credential_chain", "ordered_evidence_chain", "outcome", .50,
                steps=[
                    {"kind": "use_service", "location": credential, "label": "credential"},
                    {"kind": "buy", "location": purchase, "label": "permit"},
                    {"kind": "use_service", "location": service, "label": "booked_training"},
                ],
            ),
            pilot.condition("return_home", "visit_before", "outcome", .25, location=home, deadline=pilot.fmt(return_deadline), ignore_start=True),
            pilot.condition("budget", "budget_at_least", "constraint", .10, agent="aria", min_remaining=0),
            pilot.condition("legal_trace", "no_feasibility_violation", "constraint", .15),
        ]
        oracle = (
            pilot.access(credential)
            + [{"kind": "use_service", "target": credential, "service": "credential", "minutes": 4}]
            + pilot.access(purchase)
            + [{"kind": "buy", "target": purchase, "item": "permit", "minutes": 3}]
            + pilot.access(service)
            + [{"kind": "use_service", "target": service, "service": "booked_training", "minutes": 5}]
            + pilot.access(home)
            + [finish]
        )
        negative = (
            pilot.access(purchase)
            + [{"kind": "buy", "target": purchase, "item": "permit", "minutes": 3}]
            + pilot.access(service)
            + [{"kind": "use_service", "target": service, "service": "booked_training", "minutes": 5}]
            + pilot.access(home)
            + [finish]
        )

    else:
        raise ValueError(construct)

    plan = {
        "scenario_id": scenario["scenario_id"],
        "construct_family": construct,
        "oracle": oracle,
        "negative": negative,
    }
    return scenario, plan


def generate(output_root: Path = OUTPUT_ROOT) -> dict[str, Any]:
    output_root = output_root.resolve()
    world_paths = sorted((V1_ROOT / "worlds" / "public").glob("*.json"))
    worlds = [load_json(path) for path in world_paths]
    if len(worlds) != 3:
        raise RuntimeError(f"expected exactly three public worlds, found {len(worlds)}")
    scenarios: list[dict[str, Any]] = []
    plans: list[dict[str, Any]] = []
    rejections: list[dict[str, Any]] = []
    for construct_index, construct in enumerate(pilot.CONSTRUCTS):
        for variant in range(3):
            world = worlds[(construct_index + variant) % len(worlds)]
            try:
                scenario, plan = build_item(world, construct, variant)
            except Exception as exc:  # retained, never silently dropped
                rejections.append({
                    "construct": construct, "variant": variant,
                    "world_id": world["world_id"], "reason": str(exc),
                })
                continue
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
    (output_root / "rejection_log.json").write_text(
        json.dumps(rejections, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    config = {
        "benchmark_id": "cityintent_v1_1_expansion_wave4",
        "version": "1.1.0-expansion-wave4",
        "status": "mechanism_distinctness_review_pending_not_release",
        "worlds": [
            str(path.resolve().relative_to(output_root, walk_up=True))
            for path in world_paths
        ],
        "scenario_dir": "scenarios",
        "agents_under_test": [
            {"id": value}
            for value in ("utility_planner", "llm_direct_actor", "reactive_replanner", "memory_reflection")
        ],
        "validation": {"min_scenarios": 24},
    }
    (output_root / "benchmark_config.json").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    manifest = {
        "schema_version": "cityintent_native_expansion_wave4_v1",
        "generator_version": GENERATOR_VERSION,
        "status": "mechanism_distinctness_review_pending_not_release",
        "design_contract": str(DESIGN_PATH.name),
        "scenario_count": len(scenarios),
        "rejection_count": len(rejections),
        "construct_counts": dict(sorted(Counter(row["family"] for row in scenarios).items())),
        "mechanisms": {
            construct: row["mechanism_id"] for construct, row in DESIGN["constructs"].items()
        },
        "mechanism_contracts": {
            construct: {
                "state_transition": row["state_transition"],
                "required_actions": list(row["required_actions"]),
                "required_conditions": list(row["required_conditions"]),
                "negative_failure": row["negative_failure"],
            }
            for construct, row in DESIGN["constructs"].items()
        },
        "scenario_matrix_sha256": hashlib.sha256("\n".join(sorted(
            json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
            for row in scenarios
        )).encode()).hexdigest(),
    }
    (output_root / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


if __name__ == "__main__":
    print(json.dumps(generate(), sort_keys=True))
