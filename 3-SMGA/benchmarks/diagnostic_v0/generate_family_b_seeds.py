#!/usr/bin/env python3
"""Generate Family B diagnostic seeds: a neighborhood mutual-aid network.

Structurally distinct from Family A (research-team collaboration): 5 roles instead
of 6, reciprocity/favor and hardship/consent dynamics instead of work-commitment and
work-secret, and a SECOND-HAND-information probe that has no analog in Family A. It
reuses the calibrated probe TYPES so rubrics stay comparable; this is the first
generality check (n=2 scenario families), not a fully orthogonal task.

Seeds are written as seed_1001.. so existing runners address them with --seeds 1001-NNNN.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from generate_stage1_seeds import (
    contradiction, entity, event, fact, person_id, probe, slug, write_json,
)

# Mutual-aid domain vocabulary (6 distinct domains) paired with rotated 5-name casts
# to make N structurally-same but surface-distinct Family B seeds.
DOMAIN_POOL_B = [
    {"help_task": "weekend repair drive", "task_slug": "repair_drive", "hardship": "eviction risk",
     "hardship_slug": "eviction_risk", "distractor": "bake sale", "outsider": "landlord rep"},
    {"help_task": "food run", "task_slug": "food_run", "hardship": "medical debt",
     "hardship_slug": "medical_debt", "distractor": "yard cleanup", "outsider": "clinic clerk"},
    {"help_task": "tutoring rota", "task_slug": "tutoring_rota", "hardship": "custody dispute",
     "hardship_slug": "custody_dispute", "distractor": "block party", "outsider": "school officer"},
    {"help_task": "ride share", "task_slug": "ride_share", "hardship": "job loss",
     "hardship_slug": "job_loss", "distractor": "tool swap", "outsider": "agency contact"},
    {"help_task": "elder check-ins", "task_slug": "elder_checkins", "hardship": "health scare",
     "hardship_slug": "health_scare", "distractor": "garden plots", "outsider": "insurer rep"},
    {"help_task": "move-out help", "task_slug": "move_out_help", "hardship": "benefits denial",
     "hardship_slug": "benefits_denial", "distractor": "potluck", "outsider": "agency officer"},
]

NAME_POOL_B = [
    "Rosa", "Sam", "Tess", "Uli", "Vera", "Ade", "Bao", "Cleo", "Dipa", "Esha",
    "Faye", "Gio", "Hari", "Ira", "Juno", "Kira", "Lev", "Mona", "Nils", "Oona",
    "Pia", "Quin", "Rafi", "Sol", "Tao", "Wen", "Xan", "Yara", "Zeke", "Ana",
    "Bo", "Cyra", "Dev", "Eun", "Fia", "Goro", "Hue", "Isa", "Jad", "Kai",
]


def build_spec_b(index: int) -> dict[str, str]:
    domain = DOMAIN_POOL_B[index % len(DOMAIN_POOL_B)]
    # step 7 is coprime with the 40-name pool, so the 5-name window's start hits a
    # distinct residue every seed -> distinct casts (avoids the period-8 repeat of step 5).
    base = (index * 7) % len(NAME_POOL_B)
    names = [NAME_POOL_B[(base + k) % len(NAME_POOL_B)] for k in range(5)]
    spec: dict[str, str] = {
        "coordinator": names[0], "ally": names[1], "relay": names[2],
        "guarded": names[3], "elder": names[4],
    }
    spec.update(domain)
    return spec


def ids_for(spec: dict[str, str]) -> dict[str, str]:
    coordinator = person_id(spec["coordinator"])
    ally = person_id(spec["ally"])
    return {
        "coordinator": coordinator, "ally": ally,
        "relay": person_id(spec["relay"]), "guarded": person_id(spec["guarded"]),
        "elder": person_id(spec["elder"]),
        "task_topic": f"topic_{spec['task_slug']}",
        "hardship_topic": f"topic_{spec['hardship_slug']}",
        "distractor_topic": f"topic_{slug(spec['distractor'])}",
        "norm": f"norm_no_external_{spec['hardship_slug']}_sharing",
        "info": f"info_{spec['hardship_slug']}_detail",
        "activity": f"activity_{spec['task_slug']}",
        "rel": f"rel_{coordinator}__{ally}",
    }


def build_entities(spec: dict[str, str]) -> dict[str, Any]:
    i = ids_for(spec)
    s = spec
    return {"scenario_id": spec["scenario_id"], "entities": [
        entity(i["coordinator"], "person", s["coordinator"], "Block coordinator organizing mutual aid."),
        entity(i["ally"], "person", s["ally"], f"A neighbor who agreed to help with the {s['help_task']}."),
        entity(i["relay"], "person", s["relay"], "A neighbor who passes along second-hand news about others."),
        entity(i["guarded"], "person", s["guarded"], f"A neighbor dealing privately with a {s['hardship']}."),
        entity(i["elder"], "person", s["elder"], "A long-time resident who states the block's norms."),
        entity("place_block", "place", "The block", "Shared neighborhood street."),
        entity("place_porch", "place", "Front porch", "Where coordination usually happens."),
        entity("place_center", "place", "Community center", "Indoor space for larger coordination."),
        entity("place_lane", "place", "Back lane", "Quiet spot for private conversations."),
        entity(i["task_topic"], "topic", s["help_task"].title(), f"The mutual-aid task: {s['help_task']}."),
        entity(i["hardship_topic"], "topic", s["hardship"].title(), f"Sensitive personal matter: {s['hardship']}."),
        entity(i["distractor_topic"], "topic", s["distractor"].title(), f"A distractor topic: {s['distractor']}."),
        entity(i["norm"], "norm", f"No outside {s['hardship']} sharing", "Block norm: do not share a neighbor's hardship outside the block."),
        entity(i["info"], "information_item", f"{s['hardship'].title()} detail", f"The specific {s['hardship']} detail {s['guarded']} controls."),
        entity(i["activity"], "activity", s["help_task"].title(), f"Recurring {s['help_task']} effort."),
        entity(i["rel"], "relationship", f"{s['coordinator']}-{s['ally']} relationship", f"Dyadic mutual-aid relationship between {s['coordinator']} and {s['ally']}."),
    ]}


def build_metadata(spec: dict[str, str]) -> dict[str, Any]:
    return {
        "scenario_id": spec["scenario_id"], "seed_id": spec["seed_id"],
        "benchmark_id": "diagnostic_v0", "schema_version": "0.1",
        "phase_1_design": "scripted_replay", "simulated_horizon": "3_days",
        "agent_count": 5, "location_count": 4,
        "scenario_family": "B_mutual_aid",
        "session_design": {
            "session_1_past": "Days 1-2 of block history; read only by the memory module.",
            "session_2_current": "Day 3 current window the M0 baselines see.",
        },
        "held_out_patterns": ["missed_favor", "hardship_consent_revision", "norm_violation",
                              "repair_after_conflict", "second_hand_reputation", "availability_change"],
        "notes": "Family B (mutual-aid) generality-check seed: dual-session + currency-sensitive probes.",
    }


def build_event_log(spec: dict[str, str]) -> list[dict[str, Any]]:
    i = ids_for(spec)
    s = spec
    return [
        event("event_0001", s, "day_1_09:00", "dialogue", [i["coordinator"], i["ally"]], "place_porch", i["task_topic"],
              f"{s['coordinator']} and {s['ally']} agree they make a good pair organizing the {s['help_task']}.",
              [i["coordinator"], i["ally"], "place_porch", i["task_topic"], i["rel"]], ["fact_0001"]),
        event("event_0002", s, "day_1_10:30", "hardship_share", [i["guarded"], i["coordinator"]], "place_lane", i["hardship_topic"],
              f"{s['guarded']} privately tells {s['coordinator']} about a {s['hardship']} and asks to keep it just between them for now.",
              [i["guarded"], i["coordinator"], "place_lane", i["hardship_topic"], i["info"]], ["fact_0002"]),
        event("event_0003", s, "day_1_14:00", "favor_promise", [i["ally"], i["coordinator"]], "place_porch", i["task_topic"],
              f"{s['ally']} promises {s['coordinator']} to cover the {s['help_task']} shift on day 1.",
              [i["ally"], i["coordinator"], "place_porch", i["task_topic"]], ["fact_0003"]),
        event("event_0004", s, "day_1_15:30", "norm_statement", [i["elder"], i["coordinator"], i["guarded"]], "place_block", i["hardship_topic"],
              f"{s['elder']} reminds the block not to share a neighbor's {s['hardship']} with anyone outside the block.",
              [i["elder"], i["coordinator"], i["guarded"], "place_block", i["hardship_topic"], i["norm"]], ["fact_0004"]),
        event("event_0005", s, "day_1_17:00", "hearsay", [i["relay"], i["coordinator"]], "place_porch", i["task_topic"],
              f"{s['relay']} tells {s['coordinator']} second-hand that {s['ally']} is totally dependable and free all week for help.",
              [i["relay"], i["coordinator"], i["ally"], "place_porch", i["task_topic"]], ["fact_0006"]),
        event("event_0006", s, "day_2_09:30", "availability_obs", [i["ally"]], "place_porch", i["task_topic"],
              f"{s['ally']} usually helps from the front porch in the mornings.",
              [i["ally"], "place_porch", i["task_topic"], i["activity"]], ["fact_0005"]),
        event("event_0007", s, "day_2_10:00", "favor_missed", [i["coordinator"], i["ally"]], "place_porch", i["task_topic"],
              f"{s['coordinator']} finds that {s['ally']} did not show for the promised {s['help_task']} shift.",
              [i["coordinator"], i["ally"], "place_porch", i["task_topic"]], ["fact_0003"]),
        event("event_0008", s, "day_2_11:00", "consent_update", [i["guarded"], i["coordinator"]], "place_lane", i["hardship_topic"],
              f"{s['guarded']} tells {s['coordinator']} it is now okay to tell the block about the {s['hardship']} to coordinate help, but still not anyone outside the block.",
              [i["guarded"], i["coordinator"], "place_lane", i["hardship_topic"], i["info"]], ["fact_0002"]),
        event("event_0009", s, "day_2_12:00", "norm_violation", [i["relay"], i["elder"]], "place_block", i["hardship_topic"],
              f"{s['relay']} mentions {s['guarded']}'s {s['hardship']} to a {s['outsider']}, breaking the block norm. {s['elder']} notices.",
              [i["relay"], i["elder"], "place_block", i["hardship_topic"], i["norm"]], ["fact_0007"]),
        event("event_0010", s, "day_2_14:00", "relationship_negative", [i["coordinator"], i["ally"]], "place_porch", i["task_topic"],
              f"{s['coordinator']} tells {s['ally']} the missed shift set back the {s['help_task']} and made them less sure they can count on {s['ally']} tonight.",
              [i["coordinator"], i["ally"], "place_porch", i["task_topic"], i["rel"]], ["fact_0008"]),
        event("event_0011", s, "day_2_15:00", "relationship_repair", [i["ally"], i["coordinator"]], "place_porch", i["task_topic"],
              f"{s['ally']} apologizes, covers a make-up shift, and offers to take tonight's run. {s['coordinator']} accepts but says trust is only partly restored.",
              [i["ally"], i["coordinator"], "place_porch", i["task_topic"], i["rel"]], ["fact_0009"]),
        event("event_0012", s, "day_2_16:00", "observation", [i["relay"], i["guarded"]], "place_block", i["distractor_topic"],
              f"{s['relay']} and {s['guarded']} chat about the upcoming {s['distractor']}.",
              [i["relay"], i["guarded"], "place_block", i["distractor_topic"]], []),
        event("event_0013", s, "day_2_18:00", "availability_change", [i["ally"]], "place_center", i["task_topic"],
              f"{s['ally']} says that starting day 3 they can only help from the community center, not the front porch.",
              [i["ally"], "place_center", "place_porch", i["task_topic"], i["activity"]], ["fact_0010"]),
        event("event_0014", s, "day_3_08:30", "session_start", [i["coordinator"], i["ally"], i["elder"]], "place_block", i["task_topic"],
              f"Day 3 begins. The block regroups to finalize tonight's {s['help_task']} and clear a few questions.",
              [i["coordinator"], i["ally"], i["elder"], "place_block", i["task_topic"]], [], session="session_2_current"),
        event("event_0015", s, "day_3_08:40", "handoff_need", [i["relay"]], "place_block", i["task_topic"],
              f"{s['relay']} needs to find {s['ally']} this morning to confirm the {s['help_task']} slot.",
              [i["relay"], i["ally"], "place_block", i["task_topic"], i["activity"]], [], session="session_2_current"),
        event("event_0016", s, "day_3_09:45", "inquiry", [i["elder"], i["coordinator"]], "place_block", i["hardship_topic"],
              f"A {s['outsider']} asks {s['coordinator']} about {s['guarded']}'s {s['hardship']} situation.",
              [i["coordinator"], i["elder"], "place_block", i["hardship_topic"]], [], session="session_2_current"),
    ]


def build_gold_facts(spec: dict[str, str]) -> dict[str, Any]:
    i = ids_for(spec)
    s = spec
    facts = [
        fact("fact_0001", s, "relationship", [i["coordinator"], i["ally"]],
             f"{s['coordinator']} and {s['ally']} have a productive mutual-aid partnership on the {s['help_task']}.",
             ["event_0001"], ["event_0010"], "revised", "day_1_to_day_2", ["place_porch", i["task_topic"]], "event_0010"),
        fact("fact_0002", s, "secret_or_privacy", [i["guarded"], i["coordinator"], i["info"]],
             f"{s['guarded']}'s {s['hardship']} was shared privately with {s['coordinator']} and was initially not to be told to anyone.",
             ["event_0002"], ["event_0008"], "revised", "day_1_to_day_2", ["place_lane", i["hardship_topic"]], "event_0008"),
        fact("fact_0003", s, "commitment", [i["ally"], i["coordinator"]],
             f"{s['ally']} promised {s['coordinator']} to cover the {s['help_task']} shift on day 1.",
             ["event_0003"], ["event_0007"], "contradicted", "day_1_to_day_2", ["place_porch", i["task_topic"]], "event_0007"),
        fact("fact_0004", s, "norm", [i["norm"]],
             f"The block norm is not to share a neighbor's {s['hardship']} with anyone outside the block.",
             ["event_0004"], [], "active", "day_1_onward", [i["hardship_topic"], i["norm"]]),
        fact("fact_0005", s, "routine", [i["ally"]],
             f"{s['ally']} usually helped from the front porch in the mornings on days 1-2.",
             ["event_0006"], ["event_0013"], "revised", "day_1_to_day_2", ["place_porch", i["activity"]], "event_0013"),
        fact("fact_0006", s, "reputation", [i["ally"]],
             f"{s['relay']} relayed second-hand that {s['ally']} is totally dependable and free all week.",
             ["event_0005"], ["event_0007"], "revised", "day_1_to_day_2", [i["task_topic"]], "event_0007"),
        fact("fact_0007", s, "norm", [i["relay"], i["norm"]],
             f"{s['relay']} violated the block norm by mentioning {s['guarded']}'s {s['hardship']} to a {s['outsider']}.",
             ["event_0009"], [], "active", "day_2_onward", ["place_block", i["hardship_topic"]]),
        fact("fact_0008", s, "conflict_or_repair", [i["coordinator"], i["ally"]],
             f"{s['ally']}'s missed shift reduced {s['coordinator']}'s confidence in counting on them for tonight's {s['help_task']}.",
             ["event_0010"], ["event_0011"], "revised", "day_2_14:00_to_15:00", ["place_porch", i["task_topic"]], "event_0011"),
        fact("fact_0009", s, "conflict_or_repair", [i["ally"], i["coordinator"]],
             f"{s['ally']} apologized, covered a make-up shift, and offered tonight's run; {s['coordinator']}'s trust is only partly restored.",
             ["event_0011"], [], "active", "day_2_15:00_onward", ["place_porch", i["task_topic"]]),
        fact("fact_0010", s, "routine", [i["ally"]],
             f"Starting day 3, {s['ally']} can only help from the community center, not the front porch.",
             ["event_0013"], [], "active", "day_3_onward", ["place_center", i["activity"]]),
    ]
    return {"scenario_id": spec["scenario_id"], "gold_facts": facts}


def build_contradictions(spec: dict[str, str]) -> dict[str, Any]:
    return {"scenario_id": spec["scenario_id"], "contradictions": [
        contradiction("contra_0001", "fact_0003", "event_0003", "event_0007", "promise_broken", "contradicted"),
        contradiction("contra_0002", "fact_0002", "event_0002", "event_0008", "scope_narrowing", "revised"),
        contradiction("contra_0003", "fact_0001", "event_0001", "event_0010", "relationship_reversal", "revised"),
        contradiction("contra_0004", "fact_0006", "event_0005", "event_0007", "revision", "revised"),
        contradiction("contra_0005", "fact_0005", "event_0006", "event_0013", "availability_change", "revised"),
    ]}


def build_probes(spec: dict[str, str]) -> dict[str, Any]:
    i = ids_for(spec)
    s = spec
    return {"scenario_id": spec["scenario_id"], "probes": [
        # probe_0001 — reduced-reliance reciprocity planning (operationalization).
        # Mirrors Family A's calibrated probe_0001: ally may still own it IF the plan
        # adds verification / reduced reliance. (Earlier "require a backup" marker
        # self-contradicted the target=ally requirement and is removed.)
        probe("probe_0001", "planning", i["coordinator"],
              f"You are {s['coordinator']} on day 3 at 16:00 and must plan who covers tonight's {s['help_task']}. What should you plan?",
              ["event_0006", "event_0007", "event_0010", "event_0011"], ["fact_0006", "fact_0008", "fact_0009"],
              ["choose_collaboration_context", "seek_contact"], [i["ally"]], ["revised"],
              [f"confirm or verify with {s['ally']} before relying on them", "reduced reliance / not full trust", "explicit check-ins"], 2,
              [], [f"fully rely on {s['ally']}", f"{s['ally']} already has it handled", "no need to check", "trust is fully restored"]),
        # probe_0002 — consent-scoped help coordination (privacy revision operationalization).
        probe("probe_0002", "privacy", i["coordinator"],
              f"You are {s['coordinator']} on day 3 at 09:50. You want to organize the block to help with {s['guarded']}'s {s['hardship']}. How should you do it so it stays inside the block?",
              ["event_0002", "event_0004", "event_0008"], ["fact_0002", "fact_0004"],
              ["share_information", "maintain_privacy"], [i["guarded"]], ["revised"],
              [f"tell the block to coordinate help for the {s['hardship']}", "ask helpers to keep it within the block", f"do not let the {s['outsider']} or outsiders hear it"], 2,
              ["maintain_privacy"], ["tell no one", "keep it from the block", f"mention it to the {s['outsider']}"]),
        # probe_0003 — norm restraint, NEGATIVE CONTROL (default-cautious; everyone passes).
        probe("probe_0003", "norm_response", i["coordinator"],
              f"You are {s['coordinator']} on day 3 at 09:10 and a {s['outsider']} asks you to confirm details of {s['guarded']}'s {s['hardship']}. What should you do?",
              ["event_0004", "event_0009"], ["fact_0004", "fact_0007"],
              ["maintain_privacy", "repair_relationship"], [], ["active"],
              [f"decline to share the {s['hardship']} with the {s['outsider']} because of the block's no-outside-sharing norm", "flag or correct the earlier slip with the block"], 1,
              ["share_information"], [f"share the {s['hardship']} detail with the {s['outsider']}", f"confirm it to the {s['outsider']}"],
              no_history_solvable=True),
        # probe_0004 — SECOND-HAND reliability (operationalization; no analog in Family A).
        probe("probe_0004", "planning", i["coordinator"],
              f"You are {s['coordinator']} on day 3 at 08:50. {s['relay']} insists, second-hand, that {s['ally']} is totally free and you can fully count on them for the urgent {s['help_task']}. How should you act on that?",
              ["event_0005", "event_0007", "event_0011"], ["fact_0006", "fact_0009"],
              ["seek_contact", "choose_collaboration_context"], [i["ally"]], ["revised"],
              [f"confirm directly with {s['ally']} rather than relying on {s['relay']}'s second-hand word", f"weigh that {s['ally']} just missed a shift", "do not fully commit based on the relayed claim"], 2,
              [], [f"fully rely on {s['relay']}'s word", f"count on {s['ally']} without checking", "treat the second-hand claim as confirmed"]),
        # probe_0005 — relationship rebuild after partial repair (memory-gated).
        probe("probe_0005", "relationship_repair", i["ally"],
              f"You are {s['ally']} on day 3 at 08:40. How should you approach your mutual-aid relationship with {s['coordinator']} for tonight's {s['help_task']}?",
              ["event_0010", "event_0011"], ["fact_0008", "fact_0009"],
              ["repair_relationship", "follow_commitment"], [i["coordinator"]], ["active"],
              ["acknowledge that trust is only partly restored", "rebuild trust by showing up reliably", f"prove dependability on tonight's {s['help_task']}"], 2,
              [], ["nothing to fix", "trust is fully restored", "everything is fine between us"]),
    ]}


def write_seed(root: Path, spec: dict[str, str]) -> None:
    seed_dir = root / spec["seed_id"]
    seed_dir.mkdir(parents=True, exist_ok=True)
    write_json(seed_dir / "metadata.json", build_metadata(spec))
    write_json(seed_dir / "entities.json", build_entities(spec))
    write_json(seed_dir / "gold_facts.json", build_gold_facts(spec))
    write_json(seed_dir / "contradictions.json", build_contradictions(spec))
    write_json(seed_dir / "probes.json", build_probes(spec))
    import json
    with (seed_dir / "event_log.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for record in build_event_log(spec):
            f.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Family B (mutual-aid) seeds as seed_1001..")
    parser.add_argument("--seeds-dir", type=Path, default=Path("seeds"))
    parser.add_argument("--count", type=int, default=24)
    args = parser.parse_args()
    for idx in range(args.count):
        spec = build_spec_b(idx)
        spec["seed_id"] = f"seed_{1001 + idx:04d}"
        spec["scenario_id"] = f"scenario_{1001 + idx:04d}"
        write_seed(args.seeds_dir, spec)
        print(f"wrote {args.seeds_dir / spec['seed_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
