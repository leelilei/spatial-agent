#!/usr/bin/env python3
"""Generate template-based Stage 1 diagnostic seeds.

The hand-authored seed_0001 and seed_0002 established the benchmark shape. This
script expands the same diagnostic pattern into additional locked scenario
packages. The goal is a small Stage 1 pilot, not a final benchmark generator.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SEED_SPECS = [
    {
        "seed_id": "seed_0003",
        "scenario_id": "scenario_0003",
        "lead": "Ivy",
        "partner": "Jules",
        "source": "Kai",
        "core": "Lena",
        "reputation": "Mo",
        "routine_person": "Nora",
        "work_topic": "workshop paper revision",
        "topic_slug": "workshop_revision",
        "deliverable": "analysis appendix",
        "integration_task": "camera-ready merge",
        "sensitive_topic": "travel cap",
        "sensitive_item": "travel-cap detail",
        "sensitive_marker": "travel cap",
        "routine_activity": "demo booth check-in",
        "routine_place": "exhibit hall",
        "routine_marker": "demo booth",
        "external_party": "sponsor contact",
        "distractor_topic": "poster slot",
    },
    {
        "seed_id": "seed_0004",
        "scenario_id": "scenario_0004",
        "lead": "Maya",
        "partner": "Noah",
        "source": "Priya",
        "core": "Quinn",
        "reputation": "Ravi",
        "routine_person": "Sofia",
        "work_topic": "clinical abstract resubmission",
        "topic_slug": "clinical_abstract",
        "deliverable": "statistics table",
        "integration_task": "abstract integration pass",
        "sensitive_topic": "participant incident",
        "sensitive_item": "participant-incident detail",
        "sensitive_marker": "participant incident",
        "routine_activity": "consent huddle",
        "routine_place": "review room",
        "routine_marker": "consent huddle",
        "external_party": "outside reviewer",
        "distractor_topic": "poster title",
    },
    {
        "seed_id": "seed_0005",
        "scenario_id": "scenario_0005",
        "lead": "Aria",
        "partner": "Blake",
        "source": "Chen",
        "core": "Dina",
        "reputation": "Eli",
        "routine_person": "Faye",
        "work_topic": "robotics demo package",
        "topic_slug": "robotics_demo",
        "deliverable": "calibration script",
        "integration_task": "demo packaging pass",
        "sensitive_topic": "vendor discount",
        "sensitive_item": "vendor-discount detail",
        "sensitive_marker": "vendor discount",
        "routine_activity": "hardware standup",
        "routine_place": "robotics bay",
        "routine_marker": "hardware standup",
        "external_party": "vendor rep",
        "distractor_topic": "shipping slot",
    },
    {
        "seed_id": "seed_0006",
        "scenario_id": "scenario_0006",
        "lead": "Elena",
        "partner": "Felix",
        "source": "Gita",
        "core": "Hugo",
        "reputation": "Iris",
        "routine_person": "Jon",
        "work_topic": "dataset release note",
        "topic_slug": "dataset_release",
        "deliverable": "license appendix",
        "integration_task": "release-note final pass",
        "sensitive_topic": "embargo date",
        "sensitive_item": "embargo-date detail",
        "sensitive_marker": "embargo date",
        "routine_activity": "data sync",
        "routine_place": "data room",
        "routine_marker": "data sync",
        "external_party": "journal contact",
        "distractor_topic": "mirror backup",
    },
    {
        "seed_id": "seed_0007",
        "scenario_id": "scenario_0007",
        "lead": "Keira",
        "partner": "Luis",
        "source": "Mina",
        "core": "Owen",
        "reputation": "Pavel",
        "routine_person": "Rhea",
        "work_topic": "policy memo revision",
        "topic_slug": "policy_memo",
        "deliverable": "impact section",
        "integration_task": "memo synthesis pass",
        "sensitive_topic": "client constraint",
        "sensitive_item": "client-constraint detail",
        "sensitive_marker": "client constraint",
        "routine_activity": "briefing prep",
        "routine_place": "briefing room",
        "routine_marker": "briefing prep",
        "external_party": "partner office",
        "distractor_topic": "travel briefing",
    },
    {
        "seed_id": "seed_0008",
        "scenario_id": "scenario_0008",
        "lead": "Tara",
        "partner": "Uma",
        "source": "Vik",
        "core": "Wen",
        "reputation": "Xena",
        "routine_person": "Yuri",
        "work_topic": "security audit response",
        "topic_slug": "security_audit",
        "deliverable": "mitigation matrix",
        "integration_task": "audit-response pass",
        "sensitive_topic": "vulnerability window",
        "sensitive_item": "vulnerability-window detail",
        "sensitive_marker": "vulnerability window",
        "routine_activity": "threat review",
        "routine_place": "secure room",
        "routine_marker": "threat review",
        "external_party": "external assessor",
        "distractor_topic": "access badges",
    },
    {
        "seed_id": "seed_0009",
        "scenario_id": "scenario_0009",
        "lead": "Alden",
        "partner": "Bianca",
        "source": "Cyrus",
        "core": "Dalia",
        "reputation": "Emil",
        "routine_person": "Farah",
        "work_topic": "museum exhibit proposal",
        "topic_slug": "exhibit_proposal",
        "deliverable": "artifact list",
        "integration_task": "proposal assembly pass",
        "sensitive_topic": "donor limit",
        "sensitive_item": "donor-limit detail",
        "sensitive_marker": "donor limit",
        "routine_activity": "gallery walkthrough",
        "routine_place": "gallery",
        "routine_marker": "gallery walkthrough",
        "external_party": "press contact",
        "distractor_topic": "lighting plan",
    },
    {
        "seed_id": "seed_0010",
        "scenario_id": "scenario_0010",
        "lead": "Gwen",
        "partner": "Hector",
        "source": "Ina",
        "core": "Jamal",
        "reputation": "Leah",
        "routine_person": "Mateo",
        "work_topic": "course launch plan",
        "topic_slug": "course_launch",
        "deliverable": "assessment rubric",
        "integration_task": "launch checklist pass",
        "sensitive_topic": "enrollment cap",
        "sensitive_item": "enrollment-cap detail",
        "sensitive_marker": "enrollment cap",
        "routine_activity": "morning prep meeting",
        "routine_place": "seminar room",
        "routine_marker": "morning prep",
        "external_party": "department visitor",
        "distractor_topic": "room booking",
    },
]


def slug(name: str) -> str:
    return name.lower().replace(" ", "_").replace("-", "_")


def person_id(name: str) -> str:
    return f"person_{slug(name)}"


def topic_id(spec: dict[str, str], key: str) -> str:
    return f"topic_{slug(spec[key])}"


def build_entities(spec: dict[str, str]) -> dict[str, Any]:
    lead = person_id(spec["lead"])
    partner = person_id(spec["partner"])
    source = person_id(spec["source"])
    core = person_id(spec["core"])
    reputation = person_id(spec["reputation"])
    routine_person = person_id(spec["routine_person"])
    place_office = "place_office"
    place_lab = "place_lab"
    place_cafe = "place_cafe"
    routine_place = f"place_{slug(spec['routine_place'])}"
    work_topic = topic_id(spec, "topic_slug")
    sensitive_topic = topic_id(spec, "sensitive_topic")
    distractor_topic = topic_id(spec, "distractor_topic")
    norm = f"norm_no_external_{slug(spec['sensitive_topic'])}_sharing"
    info = f"info_{slug(spec['sensitive_item'])}"
    activity = f"activity_{slug(spec['routine_activity'])}"
    rel = f"rel_{lead}__{partner}"
    return {
        "scenario_id": spec["scenario_id"],
        "entities": [
            entity(lead, "person", spec["lead"], f"The lead coordinating the {spec['work_topic']}."),
            entity(partner, "person", spec["partner"], f"A teammate responsible for the {spec['deliverable']}."),
            entity(source, "person", spec["source"], f"The person who controls the {spec['sensitive_topic']} information."),
            entity(core, "person", spec["core"], "A core team member who asks about sensitive project context."),
            entity(reputation, "person", spec["reputation"], f"A colleague who relays indirect reliability updates about {spec['partner']}."),
            entity(routine_person, "person", spec["routine_person"], f"A teammate with a predictable {spec['routine_activity']} routine."),
            entity(place_office, "place", "Office", "Shared project office."),
            entity(place_lab, "place", "Lab", "Shared work lab."),
            entity(place_cafe, "place", "Cafe", "Informal discussion space.", ["campus cafe"]),
            entity(routine_place, "place", spec["routine_place"].title(), f"Location for the {spec['routine_activity']}."),
            entity(work_topic, "topic", spec["work_topic"].title(), f"The main collaborative task: {spec['work_topic']}."),
            entity(sensitive_topic, "topic", spec["sensitive_topic"].title(), f"Sensitive information about the {spec['sensitive_topic']}."),
            entity(distractor_topic, "topic", spec["distractor_topic"].title(), f"A distractor topic about {spec['distractor_topic']}."),
            entity(norm, "norm", f"No external {spec['sensitive_topic']} sharing", "Team norm not to share sensitive numbers outside the team."),
            entity(info, "information_item", spec["sensitive_item"].title(), f"The specific {spec['sensitive_item']} controlled by {spec['source']}."),
            entity(activity, "activity", spec["routine_activity"].title(), f"Recurring {spec['routine_activity']} activity."),
            entity(rel, "relationship", f"{spec['lead']}-{spec['partner']} relationship", f"Dyadic working relationship between {spec['lead']} and {spec['partner']}."),
        ],
    }


def entity(entity_id: str, entity_type: str, display_name: str, description: str, aliases: list[str] | None = None) -> dict[str, Any]:
    return {
        "entity_id": entity_id,
        "entity_type": entity_type,
        "display_name": display_name,
        "aliases": aliases or [],
        "description": description,
    }


def build_metadata(spec: dict[str, str]) -> dict[str, Any]:
    return {
        "scenario_id": spec["scenario_id"],
        "seed_id": spec["seed_id"],
        "benchmark_id": "diagnostic_v0",
        "schema_version": "0.1",
        "phase_1_design": "scripted_replay",
        "simulated_horizon": "2_days",
        "agent_count": 6,
        "location_count": 4,
        "held_out_patterns": [
            "failed_promise",
            "shared_secret_with_revision",
            "norm_violation",
            "repair_after_conflict",
            "indirect_reputation",
            "relationship_change",
            "routine_lookup",
        ],
        "notes": "Template-generated Stage 1 diagnostic seed.",
    }


def build_event_log(spec: dict[str, str]) -> list[dict[str, Any]]:
    ids = ids_for(spec)
    s = spec
    return [
        event("event_0001", s, "day_1_09:00", "dialogue", [ids["lead"], ids["partner"]], "place_cafe", ids["work_topic"],
              f"{s['lead']} and {s['partner']} discuss the {s['work_topic']} over coffee and agree they coordinate well on shared parts.",
              [ids["lead"], ids["partner"], "place_cafe", ids["work_topic"], ids["rel"]], ["fact_0001"]),
        event("event_0002", s, "day_1_10:30", "secret_share", [ids["source"], ids["lead"]], "place_office", ids["sensitive_topic"],
              f"{s['source']} privately tells {s['lead']} about a {s['sensitive_topic']} and asks them to keep it to a one-on-one conversation for now, not to share it with anyone yet.",
              [ids["source"], ids["lead"], "place_office", ids["sensitive_topic"], ids["info"]], ["fact_0002"]),
        event("event_0003", s, "day_1_14:00", "promise", [ids["partner"], ids["lead"]], "place_lab", ids["work_topic"],
              f"{s['partner']} promises {s['lead']} that they will finish the {s['deliverable']} by the end of day 1.",
              [ids["partner"], ids["lead"], "place_lab", ids["work_topic"]], ["fact_0003"]),
        event("event_0004", s, "day_1_15:30", "norm_statement", [ids["core"], ids["lead"], ids["source"]], ids["routine_place"], ids["sensitive_topic"],
              f"{s['core']} reminds the group that the team norm is not to share {s['sensitive_topic']} numbers with anyone outside the team.",
              [ids["core"], ids["lead"], ids["source"], ids["routine_place"], ids["sensitive_topic"], ids["norm"]], ["fact_0004"]),
        event("event_0005", s, "day_1_17:00", "routine_observation", [ids["routine_person"]], ids["routine_place"], ids["work_topic"],
              f"{s['routine_person']} runs the {s['routine_activity']} in the {s['routine_place']} at 09:00 each day, matching their usual routine.",
              [ids["routine_person"], ids["routine_place"], ids["work_topic"], ids["activity"]], ["fact_0005"]),
        event("event_0006", s, "day_2_09:30", "reputation_update", [ids["reputation"], ids["lead"]], "place_cafe", ids["work_topic"],
              f"{s['reputation']} tells {s['lead']} that {s['partner']} is usually reliable with deadlines based on prior projects.",
              [ids["reputation"], ids["lead"], ids["partner"], "place_cafe", ids["work_topic"]], ["fact_0006"]),
        event("event_0007", s, "day_2_10:00", "promise_broken", [ids["lead"], ids["partner"]], "place_office", ids["work_topic"],
              f"{s['lead']} checks and finds that {s['partner']} has not sent the {s['deliverable']} promised by end of day 1.",
              [ids["lead"], ids["partner"], "place_office", ids["work_topic"]], ["fact_0003"]),
        event("event_0008", s, "day_2_11:00", "information_share", [ids["source"], ids["lead"]], "place_office", ids["sensitive_topic"],
              f"{s['source']} tells {s['lead']} that it is now okay to share the {s['sensitive_topic']} with the core team, though still not outside it.",
              [ids["source"], ids["lead"], "place_office", ids["sensitive_topic"], ids["info"]], ["fact_0002"]),
        event("event_0009", s, "day_2_12:00", "norm_violation", [ids["routine_person"], ids["core"]], "place_lab", ids["sensitive_topic"],
              f"{s['routine_person']} mentions a {s['sensitive_topic']} number to a {s['external_party']}, breaking the team norm against external sharing. {s['core']} notices.",
              [ids["routine_person"], ids["core"], "place_lab", ids["sensitive_topic"], ids["norm"]], ["fact_0007"]),
        event("event_0010", s, "day_2_14:00", "relationship_negative", [ids["lead"], ids["partner"]], "place_office", ids["work_topic"],
              f"{s['lead']} tells {s['partner']} that the missed {s['deliverable']} set back the {s['work_topic']} and made them less confident relying on {s['partner']} for tonight's {s['integration_task']}.",
              [ids["lead"], ids["partner"], "place_office", ids["work_topic"], ids["rel"]], ["fact_0008"]),
        event("event_0011", s, "day_2_15:00", "relationship_repair", [ids["partner"], ids["lead"]], "place_office", ids["work_topic"],
              f"{s['partner']} apologizes, sends the {s['deliverable']} immediately, and offers to take the {s['integration_task']}. {s['lead']} accepts but says trust is only partially restored.",
              [ids["partner"], ids["lead"], "place_office", ids["work_topic"], ids["rel"]], ["fact_0009"]),
        event("event_0012", s, "day_2_16:00", "observation", [ids["reputation"], ids["routine_person"]], "place_cafe", ids["distractor_topic"],
              f"{s['reputation']} and {s['routine_person']} chat casually about the upcoming {s['distractor_topic']} at the cafe.",
              [ids["reputation"], ids["routine_person"], "place_cafe", ids["distractor_topic"]], []),
    ]


def ids_for(spec: dict[str, str]) -> dict[str, str]:
    lead = person_id(spec["lead"])
    partner = person_id(spec["partner"])
    return {
        "lead": lead,
        "partner": partner,
        "source": person_id(spec["source"]),
        "core": person_id(spec["core"]),
        "reputation": person_id(spec["reputation"]),
        "routine_person": person_id(spec["routine_person"]),
        "routine_place": f"place_{slug(spec['routine_place'])}",
        "work_topic": topic_id(spec, "topic_slug"),
        "sensitive_topic": topic_id(spec, "sensitive_topic"),
        "distractor_topic": topic_id(spec, "distractor_topic"),
        "norm": f"norm_no_external_{slug(spec['sensitive_topic'])}_sharing",
        "info": f"info_{slug(spec['sensitive_item'])}",
        "activity": f"activity_{slug(spec['routine_activity'])}",
        "rel": f"rel_{lead}__{partner}",
    }


def event(
    event_id: str,
    spec: dict[str, str],
    time: str,
    event_type: str,
    actors: list[str],
    location: str,
    topic: str,
    content: str,
    mentioned_entities: list[str],
    gold_fact_ids: list[str],
) -> dict[str, Any]:
    return {
        "event_id": event_id,
        "scenario_id": spec["scenario_id"],
        "time": time,
        "event_type": event_type,
        "actors": actors,
        "location": location,
        "topic": topic,
        "content": content,
        "mentioned_entities": mentioned_entities,
        "gold_fact_ids": gold_fact_ids,
    }


def build_gold_facts(spec: dict[str, str]) -> dict[str, Any]:
    ids = ids_for(spec)
    s = spec
    facts = [
        fact("fact_0001", s, "relationship", [ids["lead"], ids["partner"]],
             f"{s['lead']} and {s['partner']} have a productive working relationship coordinating on the {s['work_topic']}.",
             ["event_0001"], ["event_0010"], "revised", "day_1_09:00_to_day_2_14:00", ["place_cafe", ids["work_topic"]], "event_0010"),
        fact("fact_0002", s, "secret_or_privacy", [ids["source"], ids["lead"], ids["info"]],
             f"{s['source']}'s {s['sensitive_item']} was shared privately with {s['lead']} and was initially not to be shared with anyone.",
             ["event_0002"], ["event_0008"], "revised", "day_1_10:30_to_day_2_11:00", ["place_office", ids["sensitive_topic"]], "event_0008"),
        fact("fact_0003", s, "commitment", [ids["partner"], ids["lead"]],
             f"{s['partner']} promised {s['lead']} they would finish the {s['deliverable']} by the end of day 1.",
             ["event_0003"], ["event_0007"], "contradicted", "day_1_14:00_to_day_2_10:00", ["place_lab", ids["work_topic"]], "event_0007"),
        fact("fact_0004", s, "norm", [ids["norm"]],
             f"The team norm is not to share {s['sensitive_topic']} numbers with anyone outside the team.",
             ["event_0004"], [], "active", "day_1_15:30_onward", [ids["sensitive_topic"], ids["norm"]]),
        fact("fact_0005", s, "routine", [ids["routine_person"]],
             f"{s['routine_person']} runs the {s['routine_activity']} in the {s['routine_place']} at 09:00 each day.",
             ["event_0005"], [], "active", "day_1_onward", [ids["routine_place"], ids["activity"]]),
        fact("fact_0006", s, "reputation", [ids["partner"]],
             f"{s['partner']} is usually reliable with deadlines based on prior projects.",
             ["event_0006"], ["event_0007"], "revised", "day_2_09:30_to_day_2_10:00", [ids["work_topic"]], "event_0007"),
        fact("fact_0007", s, "norm", [ids["routine_person"], ids["norm"]],
             f"{s['routine_person']} violated the no-external-sharing norm by mentioning a {s['sensitive_topic']} number to a {s['external_party']}.",
             ["event_0009"], [], "active", "day_2_12:00_onward", ["place_lab", ids["sensitive_topic"]]),
        fact("fact_0008", s, "conflict_or_repair", [ids["lead"], ids["partner"]],
             f"{s['partner']}'s missed {s['deliverable']} reduced {s['lead']}'s confidence in relying on them for the {s['integration_task']}.",
             ["event_0010"], ["event_0011"], "revised", "day_2_14:00_to_day_2_15:00", ["place_office", ids["work_topic"]], "event_0011"),
        fact("fact_0009", s, "conflict_or_repair", [ids["partner"], ids["lead"]],
             f"{s['partner']} apologized, sent the {s['deliverable']}, and offered to take the {s['integration_task']}; {s['lead']}'s trust is only partially restored.",
             ["event_0011"], [], "active", "day_2_15:00_onward", ["place_office", ids["work_topic"]]),
    ]
    return {"scenario_id": spec["scenario_id"], "gold_facts": facts}


def fact(
    fact_id: str,
    spec: dict[str, str],
    fact_type: str,
    subject_entities: list[str],
    claim: str,
    supporting: list[str],
    contradicting: list[str],
    status: str,
    time_window: str,
    contexts: list[str],
    valid_until: str | None = None,
) -> dict[str, Any]:
    scope: dict[str, Any] = {"time_window": time_window, "contexts": contexts}
    if valid_until:
        scope["valid_until_event_id"] = valid_until
    return {
        "fact_id": fact_id,
        "fact_type": fact_type,
        "subject_entities": subject_entities,
        "claim": claim,
        "supporting_evidence_ids": supporting,
        "contradicting_evidence_ids": contradicting,
        "current_status": status,
        "validity_scope": scope,
    }


def build_contradictions(spec: dict[str, str]) -> dict[str, Any]:
    return {
        "scenario_id": spec["scenario_id"],
        "contradictions": [
            contradiction("contra_0001", "fact_0003", "event_0003", "event_0007", "promise_broken", "contradicted"),
            contradiction("contra_0002", "fact_0002", "event_0002", "event_0008", "scope_narrowing", "revised"),
            contradiction("contra_0003", "fact_0001", "event_0001", "event_0010", "relationship_reversal", "revised"),
            contradiction("contra_0004", "fact_0006", "event_0006", "event_0007", "revision", "revised"),
        ],
    }


def contradiction(cid: str, fact_id: str, original: str, contradicting: str, ctype: str, status: str) -> dict[str, str]:
    return {
        "contradiction_id": cid,
        "original_fact_id": fact_id,
        "original_evidence_id": original,
        "contradicting_evidence_id": contradicting,
        "contradiction_type": ctype,
        "expected_current_status": status,
    }


def build_probes(spec: dict[str, str]) -> dict[str, Any]:
    ids = ids_for(spec)
    s = spec
    return {
        "scenario_id": spec["scenario_id"],
        "probes": [
            probe(
                "probe_0001", "relationship_repair", ids["partner"],
                f"You are {s['partner']} at day_2_15:10. What should you do next about the {s['deliverable']} you did not send on time?",
                ["event_0003", "event_0007", "event_0010", "event_0011"],
                ["fact_0003", "fact_0008", "fact_0009"],
                ["repair_relationship", "follow_commitment", "seek_contact"],
                [ids["lead"]], ["contradicted", "revised"],
                ["apologize", "send", deliverable_marker(s["deliverable"])], 2,
                [], ["already sent", "no problem", "nothing to fix"],
            ),
            probe(
                "probe_0002", "privacy", ids["lead"],
                f"You are {s['lead']} at day_2_12:30. {s['core']}, a core team member, asks you directly about the {s['sensitive_topic']} situation for the {s['work_topic']}. What should you say or do?",
                ["event_0002", "event_0004", "event_0008"],
                ["fact_0002", "fact_0004"],
                ["share_information", "seek_contact"],
                [ids["core"]], ["revised"],
                [s["sensitive_marker"], "core team", "share"], 2,
                ["maintain_privacy"], ["cannot tell anyone", "keep it from the team", "refuse to discuss it"],
            ),
            probe(
                "probe_0003", "norm_response", ids["routine_person"],
                f"You are {s['routine_person']} at day_2_12:10, right after mentioning a {s['sensitive_topic']} number to a {s['external_party']}. What should you do next?",
                ["event_0004", "event_0009"],
                ["fact_0004", "fact_0007"],
                ["repair_relationship"],
                [ids["core"]], ["active"],
                ["apologize", "should not have shared", "correct"], 2,
                ["share_information"], ["share more", "no harm", "it is fine"],
            ),
            probe(
                "probe_0004", "planning", ids["lead"],
                f"You are {s['lead']} at day_2_16:00 and need to plan who finalizes tonight's {s['integration_task']}. What should you plan?",
                ["event_0006", "event_0007", "event_0011"],
                ["fact_0006", "fact_0008"],
                ["choose_collaboration_context", "seek_contact"],
                [ids["partner"]], ["revised"],
                ["verify", "check", "less rely"], 2,
                ["follow_commitment"], [f"fully rely on {s['partner']}", f"{s['partner']} already finished", "no need to check"],
            ),
            probe(
                "probe_0005", "information_request", ids["reputation"],
                f"You are {s['reputation']} at day_2_08:50 and need to find {s['routine_person']} for the {s['routine_activity']} handoff. Where should you look first?",
                ["event_0005"],
                ["fact_0005"],
                ["seek_contact"],
                [ids["routine_person"], ids["routine_place"]], ["active"],
                [spec["routine_place"], spec["routine_marker"]], 1,
                [], ["cafe first", "lab first"],
            ),
        ],
    }


def deliverable_marker(deliverable: str) -> str:
    return deliverable.split()[-1]


def probe(
    probe_id: str,
    probe_type: str,
    acting_agent: str,
    prompt_text: str,
    evidence_ids: list[str],
    fact_ids: list[str],
    acceptable_affordances: list[str],
    target_entities: list[str],
    statuses: list[str],
    markers: list[str],
    min_marker_count: int,
    forbidden_affordances: list[str],
    forbidden_markers: list[str],
) -> dict[str, Any]:
    return {
        "probe_id": probe_id,
        "probe_type": probe_type,
        "acting_agent": acting_agent,
        "prompt": prompt_text,
        "required_prior_evidence_ids": evidence_ids,
        "required_fact_ids": fact_ids,
        "success_condition": {
            "acceptable_affordance_types": acceptable_affordances,
            "required_target_entities": target_entities,
            "required_current_status": statuses,
            "required_response_markers": markers,
            "minimum_marker_count": min_marker_count,
        },
        "failure_condition": {
            "forbidden_affordance_types": forbidden_affordances,
            "forbidden_response_markers": forbidden_markers,
        },
        "no_history_solvability_flag": False,
    }


def write_seed(root: Path, spec: dict[str, str]) -> None:
    seed_dir = root / spec["seed_id"]
    seed_dir.mkdir(parents=True, exist_ok=True)
    write_json(seed_dir / "metadata.json", build_metadata(spec))
    write_json(seed_dir / "entities.json", build_entities(spec))
    write_json(seed_dir / "gold_facts.json", build_gold_facts(spec))
    write_json(seed_dir / "contradictions.json", build_contradictions(spec))
    write_json(seed_dir / "probes.json", build_probes(spec))
    with (seed_dir / "event_log.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for record in build_event_log(spec):
            f.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
            f.write("\n")


def write_json(path: Path, data: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Stage 1 template diagnostic seeds.")
    parser.add_argument("--seeds-dir", type=Path, default=Path("seeds"))
    parser.add_argument("--start", type=int, default=3)
    parser.add_argument("--end", type=int, default=10)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    wanted = {f"seed_{index:04d}" for index in range(args.start, args.end + 1)}
    for spec in SEED_SPECS:
        if spec["seed_id"] in wanted:
            write_seed(args.seeds_dir, spec)
            print(f"wrote {args.seeds_dir / spec['seed_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
