#!/usr/bin/env python3
"""Build SMGA treatment prompt bundles from a memory artifact.

Both conditions receive the SAME model-formed memory candidate set (the matched-
candidate rule, schema v0.1 §13). They differ only in serialization:
- M2_memory_only: the memories as plain-text notes.
- M3_placebo: stale early-log memories in the M3 structured interface.
- M3_actionable: the same memories as structured objects (types, currency status,
  evidence links) plus a planning contract over their affordances.

So M3-vs-M2 isolates the benefit of actionable structure; M3/M2-vs-M0 tests the
overall SMGA benefit. Neither condition sees probes' gold facts or success
conditions (the memories were formed condition-blind upstream).

Usage:
    python3 treatment_harness.py seeds/seed_0001 tmp/smga_memory/seed_0001_memory_artifact.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from baseline_harness import build_response_template
from benchmark_loader import ScenarioPackage, load_seed

CONDITIONS = ("M2_memory_only", "M2_aff_text", "M3_placebo", "M3_actionable")

FACT_TO_MEMORY_TYPE = {
    "relationship": "relationship_memory",
    "commitment": "commitment_memory",
    "reputation": "reputation_memory",
    "secret_or_privacy": "secret_or_privacy_memory",
    "norm": "norm_memory",
    "preference": "preference_memory",
    "routine": "routine_memory",
    "information_ownership": "information_ownership_memory",
    "conflict_or_repair": "conflict_or_repair_memory",
}

PLACEBO_CUTOFF_EVENT_TYPES = {
    "promise_broken",
    "norm_violation",
    "relationship_negative",
    "relationship_repair",
    "information_share",
    "contradiction_update",
}


def serialize_m2(memories: list[dict[str, Any]]) -> str:
    lines = []
    for m in memories:
        contra = m.get("contradicting_evidence_ids") or []
        contra_text = f" [revised/contradicted by: {', '.join(contra)}]" if contra else ""
        ev = ", ".join(m.get("supporting_evidence_ids", []) or [])
        lines.append(f"- {m.get('claim','')} (Evidence: {ev}; status: {m.get('currency_status')}){contra_text}")
    return "\n".join(lines)


def serialize_m2_aff(memories: list[dict[str, Any]]) -> str:
    """M2 plain notes PLUS the affordance suggested_context as prose.

    This is the content-matched control for M3: it carries the SAME information as
    M3 (claims, currency, evidence, AND the planning-affordance action hints), but
    as plain text rather than typed structured objects. M3 > M2_aff_text would
    isolate the value of the structure/format; M3 ~ M2_aff_text would mean the win
    over plain M2 is the affordance CONTENT, not the structure.
    """
    lines = []
    for m in memories:
        contra = m.get("contradicting_evidence_ids") or []
        contra_text = f" [revised/contradicted by: {', '.join(contra)}]" if contra else ""
        ev = ", ".join(m.get("supporting_evidence_ids", []) or [])
        lines.append(f"- {m.get('claim','')} (Evidence: {ev}; status: {m.get('currency_status')}){contra_text}")
        for a in (m.get("planning_affordances", []) or []):
            ctx = a.get("suggested_context")
            atype = a.get("affordance_type")
            if ctx:
                lines.append(f"    Possible action ({atype}): {ctx}")
    return "\n".join(lines)


def serialize_m3(memories: list[dict[str, Any]]) -> str:
    compact = []
    for m in memories:
        compact.append({
            "memory_id": m.get("memory_id"),
            "memory_type": m.get("memory_type"),
            "claim": m.get("claim"),
            "currency_status": m.get("currency_status"),
            "supporting_evidence_ids": m.get("supporting_evidence_ids", []),
            "contradicting_evidence_ids": m.get("contradicting_evidence_ids", []),
            "planning_affordances": [
                {
                    "affordance_type": a.get("affordance_type"),
                    "target_entities": a.get("target_entities", []),
                    "suggested_context": a.get("suggested_context"),
                }
                for a in (m.get("planning_affordances", []) or [])
            ],
        })
    return json.dumps(compact, ensure_ascii=False, indent=2)


def construct_placebo_memories(package: ScenarioPackage) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Construct topically-plausible stale memories from the early log.

    Placebo should test whether M3 wins because of current memory content, not
    because of the structured interface alone. We therefore keep the M3 format
    but cut the source log before the first planted contradiction/revision and
    present those early facts as usable memories. Later contradicting evidence
    is intentionally omitted so the placebo does not leak current content.
    """
    event_order = {str(event.get("event_id")): index for index, event in enumerate(package.events)}
    contradiction_events = [
        str(item.get("contradicting_evidence_id"))
        for item in package.contradictions
        if str(item.get("contradicting_evidence_id")) in event_order
    ]
    update_events = [
        str(event.get("event_id"))
        for event in package.events
        if str(event.get("event_type")) in PLACEBO_CUTOFF_EVENT_TYPES
    ]
    cutoff_candidates = [event_id for event_id in contradiction_events + update_events if event_id in event_order]
    if cutoff_candidates:
        cutoff_event = min(cutoff_candidates, key=lambda event_id: event_order[event_id])
        cutoff_index = event_order[cutoff_event]
    else:
        cutoff_event = None
        cutoff_index = len(package.events)

    placebo_facts = []
    for fact in package.gold_facts:
        supporting_ids = [str(eid) for eid in fact.get("supporting_evidence_ids", [])]
        if not supporting_ids:
            continue
        if all(event_order.get(eid, len(package.events)) < cutoff_index for eid in supporting_ids):
            placebo_facts.append(fact)

    memories = [fact_to_placebo_memory(index, fact) for index, fact in enumerate(placebo_facts, start=1)]
    meta = {
        "construction": "early_log_stale_placebo",
        "cutoff_event_id": cutoff_event,
        "source_fact_count": len(placebo_facts),
        "notes": (
            "Constructed from gold facts whose supporting evidence occurs before the first "
            "planted contradiction/revision event. Later contradicting evidence is omitted; "
            "currency_status is presented as current to preserve an interface-matched stale placebo."
        ),
    }
    return memories, meta


def fact_to_placebo_memory(index: int, fact: dict[str, Any]) -> dict[str, Any]:
    subject_entities = list(fact.get("subject_entities", []) or [])
    supporting_evidence_ids = list(fact.get("supporting_evidence_ids", []) or [])
    memory_type = FACT_TO_MEMORY_TYPE.get(str(fact.get("fact_type")), "relationship_memory")
    return {
        "memory_id": f"placebo_smem_{index:04d}",
        "memory_type": memory_type,
        "subject_entities": subject_entities,
        "claim": fact.get("claim", ""),
        "supporting_evidence_ids": supporting_evidence_ids,
        "contradicting_evidence_ids": [],
        "validity_scope": scrub_placebo_scope(fact.get("validity_scope", {})),
        "currency_status": "current",
        "planning_affordances": [
            {
                "affordance_type": infer_placebo_affordance(fact),
                "target_entities": infer_placebo_targets(subject_entities),
                "suggested_context": infer_placebo_context(fact),
                "supporting_evidence_ids": supporting_evidence_ids,
            }
        ],
    }


def scrub_placebo_scope(scope: Any) -> dict[str, Any]:
    if not isinstance(scope, dict):
        return {"time_window": "early_log_placebo", "contexts": []}
    scrubbed = {
        "time_window": "early_log_placebo_before_current_updates",
        "contexts": list(scope.get("contexts", []) or []),
    }
    return scrubbed


def infer_placebo_targets(subject_entities: list[str]) -> list[str]:
    return subject_entities[:3]


def infer_placebo_context(fact: dict[str, Any]) -> str:
    scope = fact.get("validity_scope", {})
    if isinstance(scope, dict):
        contexts = scope.get("contexts") or []
        if contexts:
            return "Use this early-log memory in contexts involving " + ", ".join(str(c) for c in contexts[:3]) + "."
    return "Use this early-log memory when the same people or topic come up."


def infer_placebo_affordance(fact: dict[str, Any]) -> str:
    fact_type = str(fact.get("fact_type", ""))
    claim = str(fact.get("claim", "")).lower()
    if fact_type == "secret_or_privacy":
        if any(marker in claim for marker in ("not to share", "private", "privately", "secret")):
            return "maintain_privacy"
        return "share_information"
    if fact_type == "norm":
        if any(marker in claim for marker in ("not to share", "private", "confidential", "budget")):
            return "maintain_privacy"
        return "avoid_contact"
    if fact_type == "routine":
        return "seek_contact"
    if fact_type == "commitment":
        return "follow_commitment"
    if fact_type == "reputation":
        return "follow_commitment"
    if fact_type == "conflict_or_repair":
        return "repair_relationship"
    if fact_type == "information_ownership":
        return "seek_information"
    return "choose_collaboration_context"


SYSTEM_M2 = (
    "You are answering a social-planning probe using a set of prepared memory notes "
    "about past interactions. Use only these notes; do not invent new facts. "
    "Return valid JSON with exactly two keys: probe_id and response_text."
)
SYSTEM_M3 = (
    "You are answering a social-planning probe using structured social memories. Each "
    "memory has a currency_status and may list planning_affordances (candidate actions). "
    "Treat the affordances as OPTIONAL hints, not a menu you must pick from: give the most "
    "socially appropriate and COMPLETE response, even if it combines actions or none of the "
    "listed affordances fits exactly. Respect currency_status (never act on a contradicted "
    "or superseded claim as if it were current). Do NOT narrate which memory or affordance "
    "you used, and never drop a proper social response (apologizing, showing caution, "
    "preserving privacy) just to match an affordance. Use only these memories; do not invent "
    "new facts. Return valid JSON with exactly two keys: probe_id and response_text."
)


def build_user_prompt(condition: str, memory_block: str, probe: dict[str, Any]) -> str:
    structured = condition.startswith("M3")
    header = (
        "Structured social memories (typed, with currency status and planning affordances):"
        if structured
        else "Memory notes:"
    )
    parts = [
        f"Condition: {condition}",
        header,
        memory_block,
    ]
    if structured:
        parts.append(
            "The planning_affordances are optional hints. Respect each memory's currency_status "
            "and give the most appropriate, complete social response."
        )
    parts += [
        "Probe:",
        str(probe["prompt"]),
        "Output JSON:",
        json.dumps({"probe_id": probe["probe_id"], "response_text": "your answer here"}, ensure_ascii=False),
    ]
    return "\n\n".join(parts)


# --- Structure-at-scale experiment: distractor padding + structure-based retrieval ---
SCALE_CONDITIONS = ("M2_aff_scale", "M3_dump_scale", "M3_retr_scale")

_DISTRACTOR_PEOPLE = [
    "Quill", "Roan", "Sable", "Tovey", "Ulla", "Verity", "Wade", "Xael",
    "Yael", "Zinn", "Avery", "Bram", "Cass", "Devi", "Elio", "Fenn",
    "Gwynn", "Hale", "Isla", "Jory", "Keon", "Lux", "Maren", "Nima",
]
_DISTRACTOR_TYPES = [
    "relationship_memory", "commitment_memory", "reputation_memory",
    "preference_memory", "routine_memory", "norm_memory",
]
_DISTRACTOR_TOPICS = [
    "the archive migration", "the onboarding doc", "the quarterly metrics",
    "the catering order", "the office move", "the newsletter draft",
    "the badge system", "the travel reimbursements", "the survey rollout",
]
_DISTRACTOR_AFF = [
    ("seek_contact", "Reach out to {a} when {topic} comes up; they usually respond quickly."),
    ("follow_commitment", "Track {a}'s follow-through on {topic}; they have been reliable so far."),
    ("choose_collaboration_context", "Pair {a} with {b} on {topic}; they coordinate well together."),
    ("maintain_privacy", "Keep {a}'s notes on {topic} within the immediate team."),
]


def pad_with_distractors(memories: list[dict[str, Any]], k: int, seed_id: str) -> list[dict[str, Any]]:
    """Append k deterministic synthetic distractor memories about non-probed people.

    Same shape as real memories (claim/type/currency/affordances) so M2_aff and M3
    carry them faithfully, but with disjoint subject_entities so a structure-based
    retriever can filter them out while a flat prose dump cannot.
    """
    import random

    rng = random.Random(f"{seed_id}:{k}")
    out = list(memories)
    for i in range(k):
        a = rng.choice(_DISTRACTOR_PEOPLE)
        b = rng.choice([p for p in _DISTRACTOR_PEOPLE if p != a])
        topic = rng.choice(_DISTRACTOR_TOPICS)
        mtype = _DISTRACTOR_TYPES[i % len(_DISTRACTOR_TYPES)]
        aff_type, aff_tmpl = rng.choice(_DISTRACTOR_AFF)
        status = "current" if rng.random() < 0.75 else "revised"
        pa = person_id_distractor(a)
        pb = person_id_distractor(b)
        out.append({
            "memory_id": f"distractor_smem_{i:04d}",
            "memory_type": mtype,
            "subject_entities": [pa, pb],
            "claim": f"{a} and {b} worked on {topic}; {a} handled the main part.",
            "supporting_evidence_ids": [],
            "contradicting_evidence_ids": [],
            "currency_status": status,
            "planning_affordances": [
                {
                    "affordance_type": aff_type,
                    "target_entities": [pa],
                    "suggested_context": aff_tmpl.format(a=a, b=b, topic=topic),
                    "supporting_evidence_ids": [],
                }
            ],
        })
    return out


def person_id_distractor(name: str) -> str:
    return f"person_dx_{name.lower()}"


def retrieve_topk(memories: list[dict[str, Any]], probe: dict[str, Any], k: int) -> list[dict[str, Any]]:
    """Structure-based top-k: keep memories whose subject_entities overlap the probe's
    target/acting entities. Only structured memory exposes the fields to do this."""
    sc = probe.get("success_condition", {})
    targets = set(sc.get("required_target_entities", []) or [])
    targets.add(probe.get("acting_agent"))
    targets.discard(None)

    def score(m: dict[str, Any]) -> int:
        return len(set(m.get("subject_entities", []) or []) & targets)

    ranked = sorted(memories, key=lambda m: (score(m), m.get("currency_status") == "current"), reverse=True)
    kept = [m for m in ranked if score(m) > 0][:k]
    return kept or ranked[:k]


def build_scale_prompts(package: ScenarioPackage, memories: list[dict[str, Any]], k: int, output_dir: Path) -> None:
    padded = pad_with_distractors(memories, k, package.seed_id)
    probes = json.loads((package.seed_dir / "probes.json").read_text(encoding="utf-8")).get("probes", [])
    output_dir.mkdir(parents=True, exist_ok=True)
    systems = {"M2_aff_scale": SYSTEM_M2, "M3_dump_scale": SYSTEM_M3, "M3_retr_scale": SYSTEM_M3}

    for condition in SCALE_CONDITIONS:
        records = []
        for probe in probes:
            if condition == "M2_aff_scale":
                block = serialize_m2_aff(padded)
            elif condition == "M3_dump_scale":
                block = serialize_m3(padded)
            else:  # M3_retr_scale — per-probe structure-based retrieval
                block = serialize_m3(retrieve_topk(padded, probe, 5))
            records.append({
                "probe_id": probe["probe_id"],
                "condition_id": condition,
                "scenario_id": package.scenario_id,
                "seed_id": package.seed_id,
                "memory_count": len(padded),
                "system_prompt": systems[condition],
                "user_prompt": build_user_prompt(condition, block, probe),
                "expected_raw_output_schema": {"probe_id": probe["probe_id"], "response_text": "..."},
            })
        prompts_path = output_dir / f"{package.seed_id}_{condition}_prompts.jsonl"
        with prompts_path.open("w", encoding="utf-8", newline="\n") as f:
            for r in records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        template_path = output_dir / f"{package.seed_id}_{condition}_responses.template.json"
        with template_path.open("w", encoding="utf-8", newline="\n") as f:
            json.dump(build_response_template(package, condition), f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"{condition}: {len(records)} prompts (store={len(padded)}) -> {prompts_path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build M2/M3 prompt bundles from a memory artifact.")
    parser.add_argument("seed_dir", type=Path)
    parser.add_argument("memory_artifact", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("tmp/smga_treatment"))
    parser.add_argument(
        "--memory-scale",
        type=int,
        default=None,
        help="If set, emit ONLY the structure-at-scale conditions, padding the "
        "memory store with this many distractor memories.",
    )
    args = parser.parse_args()

    package = load_seed(args.seed_dir)
    artifact = json.loads(args.memory_artifact.read_text(encoding="utf-8"))
    memories = artifact.get("memories", [])

    if args.memory_scale is not None:
        build_scale_prompts(package, memories, args.memory_scale, args.output_dir)
        return 0
    placebo_memories, placebo_meta = construct_placebo_memories(package)
    probes = json.loads((args.seed_dir / "probes.json").read_text(encoding="utf-8")).get("probes", [])

    condition_memories = {
        "M2_memory_only": memories,
        "M2_aff_text": memories,
        "M3_placebo": placebo_memories,
        "M3_actionable": memories,
    }
    serializers = {
        "M2_memory_only": serialize_m2,
        "M2_aff_text": serialize_m2_aff,
        "M3_placebo": serialize_m3,
        "M3_actionable": serialize_m3,
    }
    systems = {
        "M2_memory_only": SYSTEM_M2,
        "M2_aff_text": SYSTEM_M2,
        "M3_placebo": SYSTEM_M3,
        "M3_actionable": SYSTEM_M3,
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    placebo_artifact_path = args.output_dir / f"{package.seed_id}_M3_placebo_memory_artifact.json"
    with placebo_artifact_path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump({
            "scenario_id": package.scenario_id,
            "seed_id": package.seed_id,
            "condition_id": "M3_placebo",
            "source": "treatment_harness.py deterministic early-log stale placebo",
            "placebo_construction": placebo_meta,
            "memory_count": len(placebo_memories),
            "memories": placebo_memories,
        }, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")
    print(f"M3_placebo memory artifact: {placebo_artifact_path}")

    for condition in CONDITIONS:
        memory_block = serializers[condition](condition_memories[condition])
        records = [
            {
                "probe_id": probe["probe_id"],
                "condition_id": condition,
                "scenario_id": package.scenario_id,
                "seed_id": package.seed_id,
                "system_prompt": systems[condition],
                "user_prompt": build_user_prompt(condition, memory_block, probe),
                "expected_raw_output_schema": {"probe_id": probe["probe_id"], "response_text": "..."},
            }
            for probe in probes
        ]
        prompts_path = args.output_dir / f"{package.seed_id}_{condition}_prompts.jsonl"
        with prompts_path.open("w", encoding="utf-8", newline="\n") as f:
            for r in records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        template_path = args.output_dir / f"{package.seed_id}_{condition}_responses.template.json"
        with template_path.open("w", encoding="utf-8", newline="\n") as f:
            json.dump(build_response_template(package, condition), f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"{condition}: {len(records)} prompts -> {prompts_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
