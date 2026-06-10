# SMGA Memory Schema v0.1

> Project: **Structured Memory for Generative Agents (SMGA)**
> Status: draft engineering schema for Experiment 0
> Source plan: `docs/plans/SMGA-proposal-v4.6.md`
> Date: 2026-06-10

---

## 1. Purpose

This document freezes the first implementation-facing schema for SMGA's structured social memory.

The schema is designed for the v4.6 diagnostic benchmark:

```text
scripted event log
-> structured social memory
-> evidence-grounded planning interface
-> history-dependent probe behavior
```

It is not a universal memory ontology. It is the minimum schema needed to test whether typed, entity-grounded, evidence-verified, contradiction-aware, validity-scoped, planning-actionable memories improve long-horizon generative-agent behavior.

---

## 2. Core Objects

SMGA uses four linked object types:

```text
EventLogEntry
Entity
GoldSocialFact
StructuredSocialMemory
```

The experiment generator creates `EventLogEntry`, `Entity`, and `GoldSocialFact` objects before any model run. The memory module creates `StructuredSocialMemory` objects after replaying the scripted event log.

---

## 3. ID Conventions

IDs are stable strings, unique within a scenario package.

```text
scenario_id: scenario_0001
event_id: event_0001
chat_id: chat_0001
entity_id: person_maria, place_cafe, topic_paper_deadline
fact_id: fact_0001
memory_id: smem_0001
affordance_id: afford_0001
probe_id: probe_0001
```

Event-like IDs (`event_*`, `chat_*`) may both appear in evidence lists. All evidence IDs must resolve to an `EventLogEntry`.

---

## 4. EventLogEntry

Every scripted observation, dialogue act, relationship update, promise, norm violation, or repair event is represented as an event log entry.

### Required Fields

```json
{
  "event_id": "event_0042",
  "scenario_id": "scenario_0001",
  "time": "day_2_14:30",
  "event_type": "promise",
  "actors": ["person_klaus", "person_maria"],
  "location": "place_library",
  "topic": "topic_paper_deadline",
  "content": "Klaus promises Maria that he will send the experiment notes before dinner.",
  "mentioned_entities": ["person_klaus", "person_maria", "topic_paper_deadline"],
  "gold_fact_ids": ["fact_0017"]
}
```

### `event_type` Enum

```text
observation
dialogue
promise
promise_fulfilled
promise_broken
information_share
information_request
secret_share
norm_statement
norm_violation
relationship_positive
relationship_negative
relationship_repair
reputation_update
routine_observation
preference_statement
contradiction_update
```

### Validation Rules

- `event_id` must be unique.
- `actors` must contain valid person entities.
- `location` must be a valid place entity.
- `mentioned_entities` must include every named person, place, topic, norm, or information item central to the event.
- `gold_fact_ids` may be empty for distractor events.

---

## 5. Entity

Entities ground memories in concrete objects from the scenario package.

### Required Fields

```json
{
  "entity_id": "person_maria",
  "entity_type": "person",
  "display_name": "Maria",
  "aliases": ["Maria Chen"],
  "description": "A researcher working on the shared paper deadline."
}
```

### `entity_type` Enum

```text
person
place
topic
activity
relationship
group
norm
information_item
time_window
```

### Relationship Entity Convention

Relationship entities use deterministic pair IDs:

```text
rel_person_klaus__person_maria
```

The entity may represent a dyadic tie even if the current relationship state changes over time.

---

## 6. GoldSocialFact

Gold social facts are generated before model runs and provide the recall denominator for evaluation.

### Required Fields

```json
{
  "fact_id": "fact_0017",
  "fact_type": "commitment",
  "subject_entities": ["person_klaus", "person_maria"],
  "claim": "Klaus promised Maria that he would send the experiment notes before dinner.",
  "supporting_evidence_ids": ["event_0042"],
  "contradicting_evidence_ids": ["event_0061"],
  "current_status": "revised",
  "validity_scope": {
    "time_window": "day_2_14:30_to_day_2_18:00",
    "contexts": ["place_library", "topic_paper_deadline"]
  }
}
```

### `fact_type` Enum

```text
relationship
commitment
reputation
secret_or_privacy
norm
preference
routine
information_ownership
conflict_or_repair
```

### `current_status` Enum

```text
active
revised
contradicted
expired
unknown
```

---

## 7. StructuredSocialMemory

This is the main SMGA memory object.

### Required Fields

```json
{
  "memory_id": "smem_0042",
  "scenario_id": "scenario_0001",
  "memory_type": "relationship_memory",
  "subject_entities": ["person_klaus", "person_maria"],
  "claim": "Klaus and Maria have a recurring informal research-discussion relationship.",
  "supporting_evidence_ids": ["chat_0018", "event_0043", "chat_0077"],
  "contradicting_evidence_ids": ["event_0091"],
  "validity_scope": {
    "time_window": "day_1_to_day_3",
    "contexts": ["place_cafe", "place_library", "topic_research_discussion"]
  },
  "planning_affordances": [
    {
      "affordance_id": "afford_0042_01",
      "affordance_type": "seek_contact",
      "target_entities": ["person_maria"],
      "suggested_context": "place_library",
      "supporting_evidence_ids": ["chat_0018", "chat_0077"]
    }
  ],
  "currency_status": "current",
  "confidence": 0.72,
  "created_at": "day_3_18:00",
  "updated_at": "day_3_18:00",
  "used_in_plans": []
}
```

### `memory_type` Enum

```text
relationship_memory
commitment_memory
reputation_memory
secret_or_privacy_memory
norm_memory
preference_memory
routine_memory
information_ownership_memory
conflict_or_repair_memory
```

### `currency_status` Enum

```text
current
revised
contradicted
stale
superseded
uncertain
```

### Field Semantics

- `memory_id`: stable ID assigned by the memory module.
- `scenario_id`: scenario package that produced the memory.
- `memory_type`: typed social-memory class.
- `subject_entities`: entities the memory is primarily about.
- `claim`: natural-language atomic social claim.
- `supporting_evidence_ids`: event IDs that support the claim.
- `contradicting_evidence_ids`: event IDs that revise, contradict, narrow, or supersede the claim.
- `validity_scope`: time and context where the claim should be treated as valid.
- `planning_affordances`: controlled actions the planner may consider because of this memory.
- `currency_status`: whether the memory is current or outdated.
- `confidence`: exploratory only in v4.6; not used in headline metrics.
- `used_in_plans`: planning trace IDs that later used this memory.

---

## 8. Validity Scope

Validity scope prevents overgeneralization.

```json
{
  "time_window": "day_1_to_day_3",
  "contexts": ["place_cafe", "topic_research_discussion"],
  "excluded_contexts": ["place_faculty_meeting"],
  "valid_until_event_id": "event_0091"
}
```

### Rules

- `time_window` is required.
- `contexts` may include places, topics, activities, relationships, or norms.
- `excluded_contexts` is optional.
- `valid_until_event_id` is required when a later event revises or supersedes the memory.

---

## 9. Contradiction Representation

Contradiction is represented through both evidence links and currency status.

### Contradiction Types

```text
negation
revision
scope_narrowing
supersession
promise_broken
norm_violation
relationship_reversal
```

### Contradiction Object

When a contradiction is planted in the benchmark, the gold structure stores the pair explicitly:

```json
{
  "contradiction_id": "contra_0007",
  "original_fact_id": "fact_0017",
  "original_evidence_id": "event_0042",
  "contradicting_evidence_id": "event_0061",
  "contradiction_type": "promise_broken",
  "expected_current_status": "contradicted"
}
```

### Memory Update Rule

The memory module may either:

1. update the original memory in place, or
2. create a new memory that supersedes the old one.

In both cases, the final memory state must make the current fact recoverable and must not present the outdated claim as current.

---

## 10. Planning Affordance

Affordances are the bridge from memory to planning.

### Frozen `affordance_type` Vocabulary

```text
seek_contact
avoid_contact
seek_information
share_information
repair_relationship
maintain_privacy
choose_collaboration_context
follow_commitment
```

### Required Fields

```json
{
  "affordance_id": "afford_0042_01",
  "affordance_type": "seek_contact",
  "target_entities": ["person_maria"],
  "suggested_context": "place_library",
  "supporting_evidence_ids": ["chat_0018", "chat_0077"],
  "risk_evidence_ids": ["event_0091"]
}
```

### Rules

- `affordance_type` must be one of the frozen values above for headline evaluation.
- `target_entities` must resolve to valid entities.
- `supporting_evidence_ids` must be a subset of the parent memory's supporting evidence.
- `risk_evidence_ids` is optional but should include contradiction or privacy-risk evidence when relevant.
- Open-vocabulary affordances may be logged for debugging but are ignored in headline metrics.

---

## 11. Memory-Type Guidance

### `relationship_memory`

Captures recurring social ties, trust, tension, collaboration, avoidance, or repair.

Typical affordances:

```text
seek_contact
avoid_contact
repair_relationship
choose_collaboration_context
```

### `commitment_memory`

Captures promises, deadlines, favors, agreements, obligations, and broken commitments.

Typical affordances:

```text
follow_commitment
seek_contact
share_information
repair_relationship
```

### `secret_or_privacy_memory`

Captures restricted information, confidences, secrets, or privacy boundaries.

Typical affordances:

```text
maintain_privacy
avoid_contact
share_information
```

### `information_ownership_memory`

Captures who knows what, who needs what, and who is allowed to receive what.

Typical affordances:

```text
seek_information
share_information
maintain_privacy
```

### `norm_memory`

Captures explicit or implicit social rules.

Typical affordances:

```text
avoid_contact
repair_relationship
choose_collaboration_context
```

---

## 12. Minimum Validation Rules

A generated memory is valid only if:

1. `memory_id`, `scenario_id`, `memory_type`, `subject_entities`, `claim`, `supporting_evidence_ids`, `validity_scope`, `currency_status`, `created_at`, and `updated_at` are present.
2. `memory_type` is in the frozen enum.
3. every `subject_entities` item resolves to an `Entity`.
4. every evidence ID resolves to an `EventLogEntry`.
5. at least one supporting evidence event contains or entails the subject entities.
6. `contradicting_evidence_ids` is non-empty when the gold fact has a planted contradiction that should revise the memory.
7. `currency_status` is not `current` if unresolved contradiction evidence supersedes the claim.
8. every headline affordance uses the frozen affordance vocabulary.
9. `confidence` is logged but ignored for headline success criteria.

---

## 13. Planner Candidate Serialization

For the matched-candidate rule in v4.6, `M2_memory_only` and `M3_actionable` must receive the same top-k memory candidates.

### M2 Serialization

`M2_memory_only` receives the candidate memories as ordinary context:

```text
Memory: Klaus and Maria have a recurring informal research-discussion relationship.
Evidence: chat_0018, event_0043, chat_0077.
Possible relevance: seek_contact with Maria in the library.
Contradictions: event_0091.
```

### M3 Serialization

`M3_actionable` receives the same candidates as structured objects plus the planning contract.

The candidate set must not be expanded inside M3. M3 may annotate or rank the candidates, but it may not introduce new memories that M2 did not receive.

---

## 14. Evaluation Mapping

| Evaluation target | Schema fields used |
|---|---|
| grounded memory precision | `claim`, `subject_entities`, `supporting_evidence_ids`, gold log |
| grounded memory recall | `claim`, matched `GoldSocialFact` |
| contradiction awareness | `contradicting_evidence_ids`, `currency_status`, planted contradiction pairs |
| planning grounding | `planning_affordances`, required probe facts, plan rationale |
| auditability | `supporting_evidence_ids`, `contradicting_evidence_ids`, planning traces |
| social coherence | final response text, not internal schema fields |

---

## 15. Out of Scope for v0.1

The following are intentionally not frozen yet:

```text
embedding schema
retrieval index implementation
memory consolidation algorithm
memory decay policy
confidence calibration
cross-scenario memory transfer
live simulation update protocol
```

These can be added after the diagnostic benchmark and Stage 1 pilot stabilize.

