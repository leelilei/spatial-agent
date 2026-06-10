# SMGA Scenario Package Schema v0.1

> Project: **Structured Memory for Generative Agents (SMGA)**
> Status: draft schema for Experiment 0
> Source plan: `docs/plans/SMGA-proposal-v4.6.md`
> Related schema: `docs/project/smga_memory_schema_v0.1.md`
> Date: 2026-06-10

---

## 1. Purpose

A scenario package is the smallest fully specified benchmark unit for SMGA.

It defines:

```text
what happened in Phase 1
what the gold social facts are
which facts were revised or contradicted
which Phase-2 probes test history-dependent behavior
how each probe is scored mechanically
```

All conditions consume the same scenario package. The package is generated and locked before any model run.

---

## 2. Directory Layout

Each seed lives in its own directory:

```text
benchmarks/diagnostic_v0/seeds/seed_0001/
├── metadata.json
├── entities.json
├── event_log.jsonl
├── gold_facts.json
├── contradictions.json
└── probes.json
```

The package must be self-contained: no scorer should need hidden hand-authored data outside these files.

---

## 3. `metadata.json`

`metadata.json` describes the seed and experimental assumptions.

```json
{
  "scenario_id": "scenario_0001",
  "seed_id": "seed_0001",
  "benchmark_id": "diagnostic_v0",
  "schema_version": "0.1",
  "phase_1_design": "scripted_replay",
  "simulated_horizon": "2_days",
  "agent_count": 6,
  "location_count": 4,
  "held_out_patterns": [
    "failed_promise",
    "shared_secret",
    "norm_violation",
    "repair_after_conflict",
    "indirect_reputation",
    "relationship_change"
  ],
  "notes": "Minimal hand-authored seed for Experiment 0 validation."
}
```

### Required Fields

```text
scenario_id
seed_id
benchmark_id
schema_version
phase_1_design
simulated_horizon
agent_count
location_count
held_out_patterns
```

---

## 4. `entities.json`

`entities.json` contains every person, place, topic, norm, information item, relationship, and routine used by the seed.

Top-level shape:

```json
{
  "scenario_id": "scenario_0001",
  "entities": []
}
```

Each entity follows `smga_memory_schema_v0.1.md`.

### Minimum Entity Types

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

### Validation Rules

- Every entity referenced by any event, fact, contradiction, or probe must exist in `entities.json`.
- Person names used in event content must map to person entities.
- Relationship entities should use deterministic pair IDs such as `rel_person_klaus__person_maria`.

---

## 5. `event_log.jsonl`

`event_log.jsonl` is the scripted Phase-1 replay input.

Each line is one JSON object:

```json
{
  "event_id": "event_0001",
  "scenario_id": "scenario_0001",
  "time": "day_1_09:00",
  "event_type": "dialogue",
  "actors": ["person_klaus", "person_maria"],
  "location": "place_cafe",
  "topic": "topic_paper_deadline",
  "content": "Klaus and Maria discuss the shared paper deadline over coffee.",
  "mentioned_entities": ["person_klaus", "person_maria", "topic_paper_deadline", "place_cafe"],
  "gold_fact_ids": ["fact_0001"]
}
```

### Requirements

- Event order is chronological.
- All `event_id` values are unique.
- Every referenced entity exists in `entities.json`.
- Distractor events are allowed and should use an empty `gold_fact_ids` list.
- Planted contradiction events must link to a `GoldSocialFact` and appear in `contradictions.json`.

---

## 6. `gold_facts.json`

`gold_facts.json` defines the social facts a perfect memory system should recover.

Top-level shape:

```json
{
  "scenario_id": "scenario_0001",
  "gold_facts": []
}
```

Each fact uses the `GoldSocialFact` schema from `smga_memory_schema_v0.1.md`.

### Required Fields Per Fact

```text
fact_id
fact_type
subject_entities
claim
supporting_evidence_ids
contradicting_evidence_ids
current_status
validity_scope
```

### Benchmark Requirement

At least 25% of gold facts should have planted contradictions in full benchmark generation. For the minimal hand-authored seed, at least two contradiction pairs are included.

---

## 7. `contradictions.json`

`contradictions.json` explicitly records planted contradiction or revision pairs.

Top-level shape:

```json
{
  "scenario_id": "scenario_0001",
  "contradictions": []
}
```

Each contradiction object:

```json
{
  "contradiction_id": "contra_0001",
  "original_fact_id": "fact_0002",
  "original_evidence_id": "event_0003",
  "contradicting_evidence_id": "event_0008",
  "contradiction_type": "promise_broken",
  "expected_current_status": "contradicted"
}
```

### Validation Rules

- `original_fact_id` must exist in `gold_facts.json`.
- both evidence IDs must exist in `event_log.jsonl`.
- `contradicting_evidence_id` must appear later than `original_evidence_id`.
- `expected_current_status` must match the final status of the affected gold fact.

---

## 8. `probes.json`

`probes.json` defines Phase-2 behavior and planning probes.

Top-level shape:

```json
{
  "scenario_id": "scenario_0001",
  "probes": []
}
```

Each probe:

```json
{
  "probe_id": "probe_0001",
  "probe_type": "planning",
  "acting_agent": "person_klaus",
  "prompt": "You are Klaus. It is day_2_18:30. What should you do next about Maria?",
  "required_prior_evidence_ids": ["event_0003", "event_0008"],
  "required_fact_ids": ["fact_0002"],
  "success_condition": {
    "acceptable_affordance_types": ["repair_relationship", "seek_contact"],
    "required_target_entities": ["person_maria"],
    "required_current_status": ["contradicted"],
    "required_response_markers": ["apologize", "repair", "notes"]
  },
  "failure_condition": {
    "forbidden_affordance_types": ["ignore_commitment"],
    "forbidden_response_markers": ["already sent", "no issue"]
  },
  "no_history_solvability_flag": false
}
```

### `probe_type` Enum

```text
planning
behavior
privacy
information_request
relationship_repair
norm_response
```

### Success Condition Rules

- Success conditions must be authored before any model run.
- The scorer must be able to evaluate success without an LLM judge.
- `required_prior_evidence_ids` must include the specific events needed to solve the probe.
- `required_fact_ids` must link to gold facts.
- If `no_history_solvability_flag` is true, the probe is excluded from headline behavior metrics.

---

## 9. Package-Level Validation Checklist

A scenario package is valid when:

```text
metadata.json is present and parseable
entities.json is present and all entity IDs are unique
event_log.jsonl is present, chronological, and parseable line by line
gold_facts.json is present and every evidence ID resolves
contradictions.json is present and every pair resolves
probes.json is present and every probe has a machine-checkable success condition
all referenced entities exist
all referenced facts exist
all referenced evidence IDs exist
no headline probe is marked no-history solvable
```

---

## 10. Minimal Experiment 0 Deliverable

The first deliverable is one complete hand-authored seed:

```text
benchmarks/diagnostic_v0/seeds/seed_0001/
```

It should include at least:

```text
6 agents
4 locations
6-8 gold social facts
2 planted contradictions
4-6 probes
all v4.6 held-out pattern classes represented at least once
```

This single seed is not for quantitative claims. It is for validating parsing, memory formation, probe scoring, and experiment harness wiring.

