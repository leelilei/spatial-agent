# SMGA Proposal v4.5-lite

## Structured Memory for Generative Agents

> Working title: **Structured Memory for Generative Agents: Evidence-Grounded Social Context for Long-Horizon Planning**
> Short name: **SMGA**
> Version: **0.4.5-lite**
> Date: **2026-06-07**
> Status: implementation-oriented lite plan
> Relation to v4.4: keeps the memory-reliability claim, two-module method, and AGA-style ablation logic, but reduces the first-paper experiment from a full defense-oriented blueprint to a runnable diagnostic method study.

---

## 0. One-Line Version

SMGA studies whether long-horizon GA-style agents benefit from an explicit **social-memory-to-planning contract**: structured social memories that are typed, entity-grounded, evidence-supported, contradiction-aware, validity-scoped, and exposed to planning through auditable affordances.

The first-paper question is:

> Under matched model, prompt, interface, and scenario controls, does SMGA improve evidence-grounded memory quality, planning use, and history-dependent behavior beyond GA reflection, prompted reflection, representation-only memory, and placebo memory?

v4.5-lite treats v4.4 as the full research blueprint. This document is the **execution plan for the first SMGA paper**.

---

## 1. Why v4.5-lite

v4.4 was intentionally defensive. It anticipated reviewer concerns about prompt baselines, graph memory, schema circularity, compute confounds, external benchmarks, model dependence, human annotation, calibration, field ablations, and SOTA claims.

That makes v4.4 useful as a long-term roadmap, but too heavy as an implementation target. It risks turning one method paper into four projects:

```text
SMGA method paper
+ schema-ablation paper
+ benchmark-construction paper
+ graph-memory comparison paper
+ judge-validation study
```

v4.5-lite narrows the first paper to one causal chain:

```text
social experience
→ evidence-grounded structured memory
→ evidence-supported planning
→ history-dependent behavior
```

Everything that does not directly test this chain becomes optional, appendix-only, or future work.

---

## 2. Core Claim

SMGA addresses a **memory-reliability bottleneck** in long-horizon generative agents: past social experience must be converted into auditable, contradiction-aware, planning-actionable context before it can reliably guide future behavior.

The claim is not that GA lacks memory. GA already has memory streams, retrieval, reflection, and planning. The claim is narrower:

> Standard GA-style reflection does not require social memories to be typed, entity-grounded, evidence-checkable, contradiction-aware, validity-scoped, or exposed to the planner through explicit affordances and traces.

SMGA tests whether adding that contract improves:

1. memory quality,
2. memory use in planning,
3. history-dependent behavior.

Explicitly not claimed in the first paper:

```text
SMGA is a universal memory SOTA.
SMGA beats every graph-memory system.
SMGA proves an optimal social-memory schema.
SMGA reduces cost.
SMGA requires a new external benchmark.
SMGA generalizes across all model families before replication.
```

---

## 3. SMGA Definition

A **structured social memory object** satisfies four contracts:

1. **Typed**: belongs to a declared social-memory class.
2. **Entity-grounded**: links to concrete agents, places, topics, events, relationships, or routines in the log.
3. **Evidence-verified**: stores supporting and contradicting evidence IDs that can be checked against a gold event log.
4. **Planning-actionable**: exposes controlled-vocabulary affordances for downstream planning.

Example:

```json
{
  "memory_id": "smem_0042",
  "memory_type": "relationship_memory",
  "subject_entity": "Klaus-Maria",
  "claim": "Klaus and Maria have a recurring informal research-discussion relationship.",
  "supporting_evidence_ids": ["chat_018", "event_043", "chat_077"],
  "contradicting_evidence_ids": ["event_091"],
  "validity_scope": {
    "time_window": "Day 1-Day 3",
    "contexts": ["cafe", "library", "research discussion"]
  },
  "planning_affordances": [
    {
      "affordance_type": "seek_contact",
      "target": "Maria",
      "suggested_context": "library or cafe",
      "supporting_evidence_ids": ["chat_018", "chat_077"]
    }
  ],
  "confidence": 0.72,
  "created_at": "sim_day_3_18:00",
  "updated_at": "sim_day_3_18:00",
  "used_in_plans": []
}
```

The key point is auditability: the evidence, contradiction, scope, entity, and affordance fields are checkable against logs or traces.

---

## 4. Method Overview

SMGA adds two modules to a GA-style agent loop.

```text
GA baseline:
observation → memory stream → retrieval → reflection → planning → action

SMGA:
observation / dialogue / event log
→ Module A: Structured Social Memory Formation
→ Module B: Evidence-Grounded Planning Interface
→ action + auditable planning trace
```

### Module A — Structured Social Memory Formation

Module A converts episodic experiences, dialogue history, and reflection outputs into structured social memory objects.

Minimum implementation:

- L1 episodic memory stream: `event_id`, text, time, actors, location, activity, topic.
- L2 entity indexing: people, places, relationships, activities, routines, norms, information states.
- L3 typed abstraction: structured social memory objects with evidence, contradictions, validity scope, and confidence.

### Module B — Evidence-Grounded Planning Interface

Module B exposes structured memories to the planner and forces planning traces to record how memories affected action choice.

Minimum planning trace:

```json
{
  "chosen_action": "...",
  "used_memory_ids": ["smem_0042"],
  "supporting_evidence_ids": ["chat_018", "chat_077"],
  "negative_evidence_ids": ["event_091"],
  "rejected_memory_ids": [],
  "rationale": "...",
  "outcome": null
}
```

Controlled planning affordances:

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

Open affordances may be logged, but headline metrics use only the frozen vocabulary above.

---

## 5. Research Questions

v4.5-lite uses three research questions.

**RQ1 — Memory quality.** Does SMGA produce more evidence-supported structured social memories than GA reflection and prompted reflection?

**RQ2 — Planning use.** Does the SMGA planning interface cause relevant memories to enter plans as grounded evidence, beyond representation-only memory?

**RQ3 — Behavioral transfer.** Does SMGA improve history-dependent behavior, and is the improvement driven by memory content rather than interface format?

External benchmark validity and schema optimality are not first-paper research questions.

---

## 6. Main Experimental Conditions

The first-paper main experiment uses five conditions.

| Condition | Description | Purpose |
|---|---|---|
| `M0_GA` | GA-style memory stream + retrieval + reflection | Classic baseline |
| `M0_prompted` | GA reflection prompt explicitly asks about people, places, relationships, activities, routines, norms, and information states | Strong cheap-prompt control |
| `M2_memory_only` | SMGA structured memory is formed, but planning receives it only as ordinary retrieved context without the SMGA planning contract | Representation-only ablation |
| `M3_placebo` | SMGA planning interface is enabled, but memory content is random, stale, or irrelevant under matched format | Interface/placebo control |
| `M3_actionable` | Full SMGA: structured memory formation + evidence-grounded planning interface | Main treatment |

Primary contrasts:

```text
M3_actionable > M0_prompted       prompt-control test
M3_actionable > M2_memory_only    planning-interface test
M3_actionable > M3_placebo        memory-content test
```

Optional critical baseline:

```text
M3_actionable > GraphMemory_social_schema
```

`GraphMemory_social_schema` is important, but it is not required for the first implementation milestone. If it is ready without delaying the main experiment, include it as Stage 2b. Otherwise, report it as a planned critical baseline.

---

## 7. Diagnostic Benchmark

The first paper uses a controlled diagnostic benchmark rather than committing to a new external benchmark.

Scale target:

```text
agents: 6-8
contexts / locations: 4-6
simulation length: 2-3 days
seeds: 30-50 for the main experiment
model: one strong instruction-following frontier model
```

Benchmark structure:

```text
Phase 1: controlled social exposure
Phase 2: history-dependent planning / behavior probes
```

Required safeguards:

- same scripted event log replayed across memory conditions,
- distractor events included,
- probes require prior social history,
- no-history solvability flagged,
- held-out social patterns included in Phase 2 but not overused in templates.

Recommended held-out patterns:

```text
failed promise
shared secret
norm violation
repair after conflict
indirect reputation
relationship change
```

The diagnostic benchmark is used to establish mechanism. External benchmark claims are deferred.

---

## 8. Metrics

v4.5-lite has three headline metrics.

### 8.1 Evidence-Supported Memory Quality

Measures whether structured social memories are correct and auditable.

Primary components:

```text
evidence-supported memory F1
unsupported claim rate
contradiction awareness rate
```

Headline comparison:

```text
M3_actionable > M0_prompted
```

### 8.2 Evidence-Supported Planning Rate

Measures whether memory becomes grounded planning context.

Primary components:

```text
used relevant memory IDs
cites supporting evidence IDs
records negative / contradicting evidence when relevant
chooses an affordance consistent with evidence
```

Headline comparison:

```text
M3_actionable > M2_memory_only
```

### 8.3 History-Dependent Behavior Success

Measures whether the agent takes better actions on probes that require prior social history.

Primary components:

```text
target-consistent behavior
history-dependent task success
social coherence gate
```

Headline comparison:

```text
M3_actionable > M3_placebo
```

### 8.4 Secondary Metrics

Reported as diagnostics:

```text
relationship-consistency score
overgeneralization rate
hallucinated provenance rate
negative-evidence use rate
input tokens
output tokens
LLM calls
wall-clock latency
storage footprint
```

Cost is reported as a confound check, not as a claim of efficiency.

---

## 9. Evidence Validation

The first paper needs enough human validation to make evidence-grounding credible, but not a full judge-validation study.

Minimum annotation plan:

```text
sample: 100-200 memory/planning claims
annotators: 2 independent annotators
labels: supports / contradicts / irrelevant / insufficient
pilot agreement target: Cohen's kappa >= 0.6 on 50 claims
```

LLM judges may be used for scaling only after pilot human agreement is acceptable. If human-LLM agreement is weak, LLM-judge results are exploratory.

Removed from the first-paper requirement:

```text
1000-claim calibration dev set
headline calibrated-confidence metrics
full judge-validation study
```

---

## 10. Statistical Analysis

Use paired-seed evaluation as the primary analysis.

Design:

```text
same agent profiles
same initial states
same scripted exposure logs
same probe prompts
same model and decoding settings
different memory architecture only
```

Primary analysis:

```text
paired condition differences by seed
bootstrap confidence intervals
Holm correction across the three primary contrasts
```

Secondary robustness:

```text
mixed-effects model with condition + task_type and random intercepts for seed / agent / scenario
```

The mixed model is useful, but the first paper should not depend on a complex model to make the result interpretable.

---

## 11. Staged Execution Plan

### Stage 1 — Pilot

Run:

```text
4 conditions × 5 seeds × 1 frontier model
M0_GA
M0_prompted
M3_placebo
M3_actionable
```

Validate:

- memory and planning traces are complete and parseable,
- `M3_placebo` does not leak useful memory content,
- annotation guidelines reach kappa >= 0.6 on a 50-claim pilot,
- `M3_actionable` shows directional improvement on at least one memory metric and one planning/behavior metric.

If Stage 1 fails, revise memory formation, planning trace, or probes before scaling.

### Stage 2 — Main Diagnostic Experiment

Run:

```text
5 conditions × 30-50 seeds × 1 frontier model
M0_GA
M0_prompted
M2_memory_only
M3_placebo
M3_actionable
```

This is the main paper table.

Proceed to paper framing if:

- `M3_actionable > M0_prompted` on evidence-supported memory quality,
- and `M3_actionable > M2_memory_only` on planning use or `M3_actionable > M3_placebo` on behavior success.

### Stage 2b — Critical Graph Baseline

Run only if implementation is ready without delaying Stage 2:

```text
GraphMemory_social_schema
```

Compare:

```text
M3_actionable > GraphMemory_social_schema
```

If graph memory matches SMGA, reframe the contribution as a memory-contract / evaluation-protocol result rather than an architecture result.

### Stage 3 — Optional Replication

Choose one optional validation depending on time and budget:

```text
second-model reduced replication
or
external benchmark sanity check
```

External benchmarks are optional for the first paper. `LIFELONG-SOTOPIA`, SOTOPIA, SOTOPIA-hard, or a future SOTOPIA-pi-ME extension can support follow-up work, but they are not required for v4.5-lite success.

---

## 12. Success Criteria

### Minimum Success

The minimum publishable result is:

```text
M3_actionable improves evidence-supported memory quality over M0_prompted
and
M3_actionable improves planning use or behavior over the relevant SMGA control
```

Interpretation:

> SMGA improves the reliability and auditability of social memory and shows evidence that this memory enters planning or behavior.

### Strong Success

Strong success requires:

```text
M3_actionable > M0_prompted on memory quality
M3_actionable > M2_memory_only on planning use
M3_actionable > M3_placebo on behavior success
```

Interpretation:

> SMGA improves memory quality, makes memory more usable for planning, and changes history-dependent behavior because of memory content rather than interface format.

### Expanded Success

Expanded success adds:

```text
M3_actionable > GraphMemory_social_schema
or
replication on a second model
or
external benchmark improvement without social-coherence degradation
```

This supports a broader claim, but is not required for the first SMGA paper.

---

## 13. Downgrade Rules

| Result | Downgrade |
|---|---|
| `M0_prompted` matches `M3_actionable` | contribution is prompt-level guidance, not architecture |
| `M2_memory_only` matches `M3_actionable` on planning | planning interface is not load-bearing |
| `M3_placebo` matches `M3_actionable` on behavior | behavior change is interface effect, not memory-content effect |
| memory quality improves but planning and behavior do not | recall / auditability contribution only |
| planning trace improves but behavior does not | planning-rationale / interpretability contribution only |
| evidence IDs fail human validation | evidence-grounding claim withdrawn |
| graph memory matches SMGA | reframe as memory-contract and evaluation contribution |
| second model fails replication | model-specific result |
| external benchmark fails | diagnostic method contribution only |

---

## 14. Demoted From v4.4

The following are no longer part of the first-paper main experiment:

```text
M0_plus
M1_indexed
GraphMemory_generic
Schema_4
Schema_emergent
Schema_oracle
field-by-field ablations
1000-claim calibration
mandatory two-model main experiment
mandatory LIFELONG-SOTOPIA / SOTOPIA-pi-ME validation
SOTA-level external benchmark claim
```

These remain valid future work or appendix diagnostics.

---

## 15. Final Position

v4.5-lite positions SMGA as a **method and mechanism paper**:

> Structured, evidence-grounded social memory can make past social experience more reliable as planning context for long-horizon generative agents.

The paper succeeds if it cleanly demonstrates the memory-to-planning-to-behavior chain under controlled diagnostic conditions. It does not need to solve schema optimality, graph-memory generality, cross-model robustness, and external benchmark SOTA in the first submission.
