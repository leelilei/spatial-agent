# SMGA Normalized Probe Response Schema v0.1

> Project: **Structured Memory for Generative Agents (SMGA)**
> Status: draft response schema for Experiment 0
> Source plan: `docs/plans/SMGA-proposal-v4.6.md`
> Related benchmark: `benchmarks/diagnostic_v0`
> Date: 2026-06-11

---

## 1. Purpose

This document freezes the first scorer-facing response format for SMGA
diagnostic probes.

The schema is intentionally small. Its job is to let every condition
(`M0_GA`, `M0_prompted`, `M2_memory_only`, `M3_placebo`, `M3_actionable`) emit
probe responses that can be scored mechanically against locked benchmark
success and failure conditions.

The schema evaluates the final response, not the internal memory format. That
keeps the v4.6 behavior metric format-neutral.

---

## 2. Top-Level Shape

```json
{
  "scenario_id": "scenario_0001",
  "seed_id": "seed_0001",
  "condition_id": "M0_prompted",
  "model_config": {
    "provider": "openai",
    "model": "MODEL_VERSION_TO_PIN_BEFORE_STAGE_1",
    "temperature": 0
  },
  "responses": []
}
```

### Required Fields

```text
scenario_id
condition_id
responses
```

### Recommended Fields

```text
seed_id
model_config
run_id
created_at
```

`seed_id` is recommended because Stage 1 and Stage 2 analyses are paired by
seed. Experiment 0 examples may still score without it because the seed is also
provided by the scorer command line.

---

## 3. Probe Response Object

Each item in `responses` is one model output normalized for one probe.

```json
{
  "probe_id": "probe_0001",
  "response_text": "I should apologize to Maria, send the missing experiment notes now, and repair the missed commitment.",
  "chosen_affordance_type": "repair_relationship",
  "target_entities": ["person_maria"],
  "current_status_used": ["contradicted", "revised"]
}
```

### Required Fields

```text
probe_id
response_text
chosen_affordance_type
target_entities
current_status_used
```

### Optional Fields

```text
rationale
used_fact_ids
used_evidence_ids
used_memory_ids
raw_model_output
normalization_notes
```

The optional fields are useful for later memory and planning analysis. They are
not required by the Experiment 0 probe-success scorer.

---

## 4. Field Semantics

### `probe_id`

Stable probe ID from `probes.json`.

Rules:

- Must match exactly one probe in the scenario package.
- Each `probe_id` should appear at most once per response file.

### `response_text`

Natural-language response to the probe after any condition-specific planning or
normalization.

Rules:

- Must be a string.
- Used by the mechanical scorer for required and forbidden response markers.
- Should not expose internal evidence IDs to the user-facing agent response
  unless a condition is explicitly being debugged.

### `chosen_affordance_type`

Single normalized action label chosen for the response.

Allowed values for headline scoring:

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

Rules:

- Must be a string.
- Must use the frozen affordance vocabulary above for headline scoring.
- If the model gives multiple actions, the normalizer should choose the primary
  action that best describes the response.

### `target_entities`

Entities the response acts on, protects, contacts, avoids, or uses as a
location target.

Rules:

- Must be a list of entity IDs.
- IDs must resolve in `entities.json`.
- Include all entities required by the action, including place targets when the
  probe asks where to go.

### `current_status_used`

Gold-status labels represented by the response.

Allowed values:

```text
active
revised
contradicted
expired
unknown
```

Rules:

- Must be a list of strings.
- The scorer checks whether at least one required status from the probe's
  success condition is represented.
- For baseline conditions, this field is produced by the response normalizer,
  not by assuming the model has explicit SMGA state.

---

## 5. Normalization Contract

Raw model output should be normalized into this schema before scoring.

Minimum normalizer responsibilities:

1. Preserve the model's substantive answer in `response_text`.
2. Map the main intended action to one `chosen_affordance_type`.
3. Extract entity IDs into `target_entities`.
4. Extract status labels into `current_status_used` only when the response
   clearly depends on that current state.
5. Leave ambiguous fields empty instead of adding unsupported gold labels.

This normalizer must be condition-blind for headline runs. It may know the
scenario package and probe metadata, but it must not use the condition label to
make a baseline look better or worse.

---

## 6. Valid Example

```json
{
  "scenario_id": "scenario_0001",
  "seed_id": "seed_0001",
  "condition_id": "example_oracle",
  "responses": [
    {
      "probe_id": "probe_0001",
      "response_text": "I should apologize to Maria, send the missing experiment notes now, and repair the missed commitment by taking the next revision pass.",
      "chosen_affordance_type": "repair_relationship",
      "target_entities": ["person_maria"],
      "current_status_used": ["contradicted", "revised"]
    }
  ]
}
```

---

## 7. Invalid Examples

### Missing Target Entity

```json
{
  "probe_id": "probe_0001",
  "response_text": "I should apologize and send the notes.",
  "chosen_affordance_type": "repair_relationship",
  "target_entities": [],
  "current_status_used": ["contradicted"]
}
```

Why invalid for success: `probe_0001` requires `person_maria` as a target.

### Outdated Status

```json
{
  "probe_id": "probe_0004",
  "response_text": "Maria should fully trust Klaus because he is careful with notes.",
  "chosen_affordance_type": "follow_commitment",
  "target_entities": ["person_klaus"],
  "current_status_used": ["active"]
}
```

Why invalid for success: the relevant Klaus trust fact has been revised.

---

## 8. Scorer Mapping

`benchmarks/diagnostic_v0/probe_success_scorer.py` currently uses:

| Response field | Probe condition checked |
|---|---|
| `chosen_affordance_type` | `acceptable_affordance_types`, `forbidden_affordance_types` |
| `target_entities` | `required_target_entities` |
| `current_status_used` | `required_current_status` |
| `response_text` | `required_response_markers`, `forbidden_response_markers` |

Headline probe success is true only when all required checks pass and no
failure condition fires.

---

## 9. Relation to Future Metrics

This schema supports the Experiment 0 behavior-success scorer. Later stages
will add adjacent artifacts instead of overloading this response file:

```text
memory artifacts -> grounded memory F1
planning traces -> history-grounded planning and SMGA auditability
normalization logs -> extraction reliability checks
```

The response schema may gain optional fields in v0.2, but v0.1 headline scoring
should remain backward compatible.
