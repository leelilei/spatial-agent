# SMGA Proposal v3

## Structured Memory for Generative Agents

> Working title: **Structured Memory for Generative Agents: Evidence-Grounded Social Context for Long-Horizon Planning**  
> Short name: **SMGA**  
> Version: **0.3**  
> Date: **2026-05-19**  
> Status: major-revision proposal after reviewer feedback  
> Relation to v2: addresses novelty, schema bias, budget-matched baselines, prompted-GA baselines, placebo-memory controls, evidence-grounding reliability, external benchmarks, cost/latency, and model-dependence.

---

## 0. One-Line Version

SMGA studies whether **Generative-Agent-style memory stream plus reflection is sufficient for long-horizon, history-dependent social behavior**, and proposes a structured memory framework that converts episodic experiences and open-ended reflections into **typed, entity-grounded, evidence-verified, and planning-actionable social context**.

The central question is:

> Beyond simply remembering and reflecting, can LLM generative agents maintain structured social memories about people, places, relationships, activities, routines, norms, and information states, and use those memories to improve future planning and behavior under matched compute, prompt, and memory-content controls?

---

## 1. Core Reframing from v2

### 1.1 What v2 got right

v2 correctly avoided the strawman that Generative Agents lack abstraction. GA already includes reflection: agents periodically synthesize higher-level thoughts from memory stream entries, and those thoughts can affect later behavior.

The correct contrast is not:

```text
GA: no reflection
SMGA: reflection
```

The correct contrast is:

```text
GA: open-ended textual reflection over a memory stream
SMGA: structured social memory objects with schema, provenance, retrieval targets,
      negative evidence, update history, and planning interfaces
```

### 1.2 What v3 changes

Reviewer feedback identified three weaknesses in v2:

1. The novelty boundary against A-MEM, graph memory, and prompted GA was not sharp enough.
2. The evaluation risked favoring SMGA through hand-engineered schemas and scripted ground truth.
3. The causal claim was confounded by extra compute, extra prompts, and LLM-as-judge evidence scoring.

v3 therefore makes five major changes:

1. **Terminology narrowed:** SMGA now stands for **Structured Memory for Generative Agents**. We avoid relying on a strong cognitive-science claim about situated cognition. “Situated” may still be used descriptively, but the technical contribution is structured, social, entity-grounded, and planning-actionable memory.
2. **Novelty clarified:** SMGA is not “A-MEM plus social tags.” Its contribution is a GA-specific, behaviorally evaluated pipeline from experience to typed memory to planning to action, with matched compute/prompt controls.
3. **Baselines strengthened:** Adds `M0+`, `M0_prompted`, `M3_placebo`, `M3_budget_matched`, and generic graph-memory baselines.
4. **Schema risks controlled:** Adds schema ablations: 4-type coarse schema, 7-type proposed schema, emergent-type schema, and held-out experience types.
5. **Evidence-grounding validated:** Adds human annotation, LLM-human agreement, provenance hallucination checks, confidence calibration, and negative evidence tracking.

---

## 2. Revised Core Claim

The strongest defensible claim is:

> GA-style reflection can produce useful high-level thoughts, but open-ended reflection alone is not a reliable mechanism for converting social experience into evidence-grounded, reusable, and planning-actionable memory. SMGA tests whether structured social memory objects improve history-dependent social planning and behavior beyond prompted reflection, budget-matched reasoning, and generic graph memory.

The claim is explicitly not:

```text
SMGA is a universal memory SOTA for all LLM agents.
SMGA proves human-like situated cognition.
SMGA replaces GA reflection.
SMGA wins because it simply calls the LLM more often.
```

The intended claim is narrower:

```text
SMGA improves long-horizon, history-dependent social behavior in GA-style agents
when the task requires recalling, abstracting, and acting on prior social context.
```

---

## 3. Research Gap

### 3.1 What GA already contributes

Generative Agents established a practical architecture for believable agents:

```text
observation
-> memory stream
-> retrieval
-> reflection
-> planning
-> action / reaction / dialogue
```

Its strengths include:

- natural-language episodic memory;
- retrieval using relevance, recency, and importance;
- reflection that creates higher-level thoughts;
- planning that uses memories and reflections;
- believable social simulation.

SMGA builds on this rather than dismissing it.

### 3.2 What remains unresolved after GA

#### Gap 1: Reflection exists, but is not schema-enforced

GA reflection can produce high-level statements, but those statements are not required to become typed objects with fields such as:

```text
memory_type
subject_entity
related_entities
supporting_evidence_ids
contradicting_evidence_ids
validity_scope
planning_affordances
confidence_calibration
update_history
used_in_plans
```

This matters because future planning requires knowing **what kind of memory** a reflection is and **how it should be used**.

#### Gap 2: Entity-indexed memory exists in related work, but behavior transfer is under-tested

Graph memory and agentic memory systems can link memories to entities. But many are evaluated primarily on retrieval, QA, or knowledge access. SMGA focuses on the full behavior chain:

```text
recall -> abstraction -> planning evidence -> action -> outcome
```

The contribution is not simply graph structure. It is **behavioral transfer under controlled memory architecture ablations**.

#### Gap 3: Prompted reflection may be a strong baseline

A reviewer correctly notes that a cheap baseline might be:

```text
Reflect about people, places, relationships, activities, and routines.
```

If this baseline matches SMGA, then the contribution is prompt engineering, not memory architecture. v3 therefore treats `M0_prompted` as a required baseline.

#### Gap 4: Extra compute may explain gains

If SMGA uses more LLM calls, tokens, or reflection rounds, gains may come from “more thinking,” not structure. v3 therefore requires compute-matched baselines.

#### Gap 5: Evidence-grounding must be independently verified

Evidence links cannot be trusted merely because an LLM reports them. v3 requires human annotation, LLM-human agreement, calibration analysis, and hallucinated-provenance detection.

---

## 4. Terminology and Definition

### 4.1 Why not rely on “situated cognition” as the main term

In cognitive science, situated cognition has a stronger meaning involving embodiment, context-dependence, distributed cognition, and action in the world. SMGA does not need to claim that full sense.

Therefore v3 uses:

> **Structured social memory**

instead of treating “situated cognition” as the main theoretical claim.

### 4.2 Operational definition

A **structured social memory object** is a memory object that satisfies four properties:

1. **Typed:** it belongs to a declared or discovered class such as person, place, relationship, activity, routine, norm, or information state.
2. **Entity-grounded:** it links to concrete entities, events, agents, places, and topics in the simulation log.
3. **Evidence-verified:** it stores supporting and contradicting evidence IDs that can be checked by non-agent evaluators.
4. **Planning-actionable:** it exposes affordances that a planner may use, but those affordances must be grounded in evidence rather than free-form invention.

Example:

```json
{
  "memory_id": "smem_0042",
  "memory_type": "relationship_memory",
  "subject_entity": "Klaus-Maria",
  "claim": "Klaus and Maria have developed a recurring informal research-discussion relationship.",
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
  "calibrated_confidence": null,
  "created_at": "sim_day_3_18:00",
  "updated_at": "sim_day_3_18:00",
  "used_in_plans": []
}
```

---

## 5. Research Questions

### RQ1: Structured memory formation

> Does SMGA produce more accurate, evidence-supported structured social memories than GA reflection, prompted GA reflection, and generic graph memory?

### RQ2: Schema contribution

> Does schema design matter, or can coarse, emergent, or generic graph schemas match the proposed SMGA schema?

### RQ3: Planning transfer

> Do structured social memories improve planning decisions beyond recall and abstraction quality?

### RQ4: Behavioral transfer

> Do agents using SMGA take better history-dependent actions than agents using GA reflection, prompted reflection, or compute-matched reflection?

### RQ5: External social-interaction performance

> Does SMGA improve performance on an external history-dependent social benchmark, rather than only on a self-authored diagnostic benchmark?

### RQ6: Cost and model dependence

> Are SMGA gains robust across model families and worth the additional cost and latency?

---

## 6. Revised Hypotheses

### H1: Evidence-supported structured recall

SMGA improves evidence-supported structured recall over GA, prompted-GA, and budget-matched GA.

Primary metric:

```text
evidence-supported structured recall F1
```

Minimum contrast:

```text
M3 > M0_prompted
M3 > M0_plus
```

### H2: Valid abstraction beyond prompted reflection

SMGA improves abstraction validity over prompted reflection and generic graph memory.

Primary metric:

```text
human-verified abstraction validity
```

Minimum contrast:

```text
M2 or M3 > M0_prompted
M2 or M3 > GraphMemory_social_schema
```

### H3: Evidence-supported planning

SMGA improves the rate at which future plans use relevant, correctly supported memory.

Primary metric:

```text
evidence-supported planning rate
```

Required control:

```text
M3 > M3_placebo
```

### H4: Behavior change due to memory content

SMGA changes future behavior because of relevant memory content, not merely because of extra prompt structure.

Primary metric:

```text
target-consistent behavior rate
```

Required contrast:

```text
M3 > M3_placebo
M3 > M0_prompted
```

### H5: External benchmark improvement

SMGA improves history-dependent social task performance on an external benchmark.

Primary candidate:

```text
Lifelong SOTOPIA / SOTOPIA-style long-horizon social interaction tasks
```

Primary metric:

```text
history-dependent social task success score
```

### H6: Efficiency-adjusted improvement

SMGA remains useful after accounting for additional calls, tokens, latency, and trace-storage overhead.

Primary metric:

```text
performance-per-1k-token or cost-normalized task success
```

---

## 7. Architecture

SMGA has four layers. Each layer can be ablated.

### 7.1 Layer 1: Episodic memory

This is the GA-compatible memory stream.

```json
{
  "event_id": "event_012",
  "text": "Maria told Klaus about the public meeting in Room B.",
  "time": "Day 1 15:30",
  "actors": ["Maria", "Klaus"],
  "location": "Room B",
  "activity": "conversation",
  "topic": "public meeting",
  "valence": "neutral-positive"
}
```

### 7.2 Layer 2: Entity indexing

Episodic memories are indexed by people, places, relationships, activities, routines, norms, and information states.

Important: indexing alone is not the main contribution. It is a required intermediate condition.

### 7.3 Layer 3: Typed social abstraction

The system creates typed memory objects, but v3 no longer assumes one schema is obviously correct. It tests schema alternatives.

Default proposed schema:

```text
person_memory
place_memory
relationship_memory
activity_memory
routine_memory
social_norm_memory
information_state_memory
```

The default schema is motivated by the recurring entities in GA-style social simulation, not claimed as exhaustive.

### 7.4 Layer 4: Planning-actionable memory

Planning receives structured memory candidates with both supporting and contradicting evidence.

Example planner input:

```json
{
  "goal": "find Maria",
  "candidate_memories": [
    {
      "memory_type": "place_memory",
      "claim": "Maria has repeatedly appeared in Room B in the afternoon.",
      "supporting_evidence_ids": ["event_012", "event_041"],
      "contradicting_evidence_ids": ["event_077"],
      "planning_affordance": "visit Room B in the afternoon if seeking Maria"
    }
  ]
}
```

Planning output must record:

```text
chosen_action
used_memory_ids
supporting_evidence_ids
negative_evidence_ids
rejected_memory_ids
rationale
outcome
```

---

## 8. Experimental Conditions

### 8.1 Core memory conditions

| Condition | Description | Purpose |
|---|---|---|
| `M0_GA` | GA-style memory stream + reflection | original-style baseline |
| `M0_plus` | GA-style memory with reflection frequency, token budget, and LLM calls matched to M3 | controls compute and “more thinking” |
| `M0_prompted` | GA reflection prompt explicitly asks about people, places, relationships, activities, routines, norms, information | controls cheap prompt engineering |
| `M1_indexed` | GA + entity indexing | tests indexing alone |
| `M2_typed` | M1 + typed structured abstractions | tests typed memory objects |
| `M3_actionable` | M2 + planning-time structured memory interface | main treatment |
| `M3_placebo` | M3 interface with random/irrelevant memory content | controls prompt/interface effect |
| `GraphMemory_generic` | generic graph memory with nodes/edges but no SMGA planning schema | controls graph structure |
| `GraphMemory_social_schema` | graph memory with social schema but no planning-actionable interface | controls “A-MEM + social tags” |

### 8.2 Schema ablation conditions

| Schema condition | Description | Purpose |
|---|---|---|
| `Schema_4` | coarse schema: person, place, relation, event | tests whether fine schema is needed |
| `Schema_7` | proposed schema: person, place, relationship, activity, routine, norm, information | main schema |
| `Schema_emergent` | LLM proposes memory types from logs, then frozen before evaluation | tests hand-engineering risk |
| `Schema_oracle` | upper-bound human-designed schema after seeing task family | upper-bound only; not main comparison |

### 8.3 Held-out experience types

To avoid benchmark-schema circularity, some social patterns are withheld from schema prompt examples and Phase 1 templates.

Examples:

```text
triadic mediation
indirect reputation transfer
failed promise
shared secret
norm violation
repair after conflict
```

The main test includes at least one held-out type not used when designing prompts or schema examples.

---

## 9. Benchmark Strategy

### 9.1 External benchmark is primary for headline claims

v3 elevates external evaluation from optional to required.

Primary external target:

```text
Lifelong SOTOPIA / SOTOPIA-style long-horizon social interaction tasks
```

Use cases:

```text
remembering prior interactions
tracking promises and commitments
adapting to changed relationships
using prior conflict or cooperation
maintaining persona-consistent social history
```

If full Lifelong SOTOPIA integration is unavailable, the paper must use a public SOTOPIA-style long-horizon task suite or release the diagnostic benchmark as an externalizable benchmark artifact. It cannot make strong SOTA claims from private diagnostic tasks alone.

### 9.2 Diagnostic benchmark remains necessary

A self-authored diagnostic benchmark is still useful because it allows causal control and gold logs.

But its role is diagnostic:

```text
mechanism validation
schema ablation
placebo controls
provenance checking
behavioral probes
```

It is not the only basis for headline performance claims.

### 9.3 Minimum diagnostic scale

Recommended diagnostic scale:

```text
agents: 6-10
locations/contexts: 6-10
simulation length: 3-5 days
seeds: minimum 50 for main diagnostic contrasts
conditions: M0_GA, M0_plus, M0_prompted, M3_actionable, M3_placebo
```

Secondary conditions can use fewer seeds after power analysis, but the main treatment comparisons require sufficient seed count.

### 9.4 Two-stage diagnostic design

#### Phase 1: controlled experience exposure

Agents experience matched scripted and semi-scripted events across conditions.

Important safeguards:

- event templates are generated before seeing model outputs;
- a subset of event types is held out;
- schema examples cannot include held-out patterns;
- Phase 1 includes distractor events that should not support the tested claim;
- the same event log is used across memory conditions for paired comparison.

#### Phase 2: planning and behavior probes

Agents face goals that require using prior context.

Examples:

```text
find a person encountered before
avoid a person after conflict
follow through on a prior commitment
seek information from likely source
choose context for private vs public conversation
repair a damaged relationship
```

---

## 10. Metrics

### 10.1 Recall and memory quality

| Metric | Definition |
|---|---|
| structured recall F1 | correct retrieval of relevant person/place/relationship/activity/norm/information memories |
| unsupported memory claim rate | fraction of claims not supported by logs |
| hallucinated provenance rate | fraction of cited evidence IDs that do not support the claim |
| contradiction awareness rate | fraction of claims that include relevant negative evidence when available |
| calibration error | expected calibration error between stated confidence and human-verified correctness |

### 10.2 Abstraction quality

| Metric | Definition |
|---|---|
| abstraction validity | human-verified correctness of structured memory claim |
| abstraction usefulness | later use in valid planning decisions |
| overgeneralization rate | claim goes beyond evidence scope |
| schema assignment accuracy | whether memory type matches human label |
| held-out type generalization | performance on unseen social pattern types |

### 10.3 Planning quality

| Metric | Definition |
|---|---|
| evidence-supported planning rate | chosen plan cites relevant supporting evidence |
| negative-evidence use rate | plan acknowledges evidence against chosen action |
| memory-content sensitivity | M3 outperforms M3_placebo |
| prompted-baseline gain | M3 outperforms M0_prompted |
| budget-matched gain | M3 outperforms M0_plus |

### 10.4 Behavior and outcomes

| Metric | Definition |
|---|---|
| target-consistent behavior rate | action matches goal and relevant memory |
| history-dependent task success | task success requiring prior interaction history |
| promise follow-through rate | commitments detected by rule+human-validated labels are later satisfied |
| relationship-consistency score | later behavior remains consistent with interaction history |
| social coherence rating | blinded human/LLM judge rating with condition-hidden traces |

### 10.5 Cost and scaling

| Metric | Definition |
|---|---|
| input/output tokens | total tokens by condition |
| LLM calls | number of calls by module |
| latency | wall-clock runtime per simulated day / task |
| trace storage | size of memory and evidence logs |
| cost-normalized success | task success per token or per dollar-equivalent budget |

---

## 11. Evidence-Grounding Protocol

### 11.1 Why this is necessary

Evidence IDs generated by the agent are not automatically trustworthy. A memory can cite evidence that exists but does not support the claim.

Therefore evidence-grounding is evaluated outside the agent.

### 11.2 Human annotation

Minimum requirement:

```text
sample size: at least 200 memory/planning claims
labels: supports / contradicts / irrelevant / insufficient
annotators: at least 2 independent annotators
agreement target: Cohen's kappa >= 0.6 before relying on LLM judge at scale
```

### 11.3 LLM judge validation

LLM judges may be used for scale only after validation.

Report:

```text
human-LLM agreement
disagreement analysis
precision/recall of support detection
hallucinated provenance detection rate
confidence calibration
```

### 11.4 Confidence calibration

Each structured memory may include raw confidence, but headline metrics use calibrated confidence.

Calibration procedure:

```text
bin predictions by confidence
estimate empirical correctness by bin
report expected calibration error
optionally learn calibration map on validation set
freeze before test set
```

### 11.5 Negative evidence

Every planning trace includes:

```text
supporting_evidence_ids
negative_evidence_ids
rejected_memory_ids
```

A plan that only cites supporting evidence while ignoring strong contradictory evidence is marked as incomplete or biased evidence use.

---

## 12. Planning Affordances

### 12.1 Concern

Free-form planning affordances can explode. A fixed list can limit generalization.

### 12.2 v3 solution: hybrid controlled vocabulary + open extension

Use a small controlled vocabulary for primary metrics:

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

Allow open extensions for exploratory analysis, but primary metrics only evaluate the frozen vocabulary.

### 12.3 How affordances are generated

Affordances are generated from structured memory claims using a constrained prompt or rule template. They are not free-form planner inventions.

Example:

```text
If memory_type = relationship_memory and claim implies positive recurring contact,
possible affordance = seek_contact.
```

The system records whether each affordance was:

```text
rule-derived
LLM-derived under constrained vocabulary
human-validated
```

---

## 13. Promise and Commitment Tracking

Promise follow-through is hard. v3 treats it as a secondary metric unless the detection protocol passes validation.

Detection pipeline:

```text
1. candidate promise extraction by rule + LLM
2. human validation subset
3. commitment object creation
4. later event matching
5. follow-through classification
```

Primary claims do not depend solely on promise metrics.

---

## 14. Statistical Analysis

### 14.1 Unit of analysis

Use paired seeds as primary design.

```text
same agent profiles
same initial states
same scripted experience log
same task prompts
same model configuration
changed memory architecture
```

### 14.2 Mixed-effects models

Example:

```text
outcome ~ condition + task_type + schema_condition + model_family
        + (1 | seed) + (1 | agent) + (1 | scenario)
```

For external benchmark tasks, scenario/task is treated as a random effect when appropriate.

### 14.3 Main contrasts

Required contrasts:

```text
M3_actionable > M0_GA
M3_actionable > M0_plus
M3_actionable > M0_prompted
M3_actionable > M3_placebo
M3_actionable > GraphMemory_social_schema
```

### 14.4 Effect-size expectations

The paper should predefine smallest effects of interest.

Proposed SESOI:

```text
structured recall F1: +0.08 absolute over M0_prompted
evidence-supported planning: +0.10 absolute over M0_prompted
target-consistent behavior: +0.08 absolute over M0_prompted
history-dependent external score: +0.05 normalized score over strongest baseline
```

If gains are below these thresholds, the contribution is framed as engineering or diagnostic rather than a strong architecture result.

### 14.5 Power

Main diagnostic tests should target at least 50 seeds unless pilot variance supports fewer.

Network-level metrics are secondary unless powered separately.

---

## 15. Model Dependence

SMGA should not claim model-general improvement from one model.

Minimum model plan:

```text
primary strong model: one frontier or high-performing API model
open-weight model: one strong open model
smaller model: optional stress test
```

Report:

```text
whether gains replicate across models
whether structured memory helps weaker models more or less
whether schema-following failures dominate weaker models
```

If only the strongest model works, the claim becomes:

> SMGA improves structured memory use for strong instruction-following LLM agents, but model generality remains limited.

---

## 16. Cost and Latency

Every result table should report:

```text
LLM calls
input tokens
output tokens
wall-clock latency
memory-store size
trace-store size
```

Main result tables should include both raw performance and cost-normalized performance.

Possible outcomes:

| Pattern | Interpretation |
|---|---|
| SMGA better and cost-normalized better | strong architecture result |
| SMGA better but cost-normalized worse | trade-off; useful when reliability matters |
| SMGA only better than unmatched baselines | not valid; likely compute effect |
| SMGA matched by M0_plus | structure not necessary; more reasoning suffices |

---

## 17. Success Criteria

### 17.1 Minimum success

Minimum publishable success now requires both:

```text
H1: structured recall/evidence support improves over M0_prompted or M0_plus
H2: abstraction validity improves over M0_prompted or graph-memory baseline
```

Recall alone is not sufficient.

### 17.2 Strong success

Strong success requires:

```text
H1 + H2 + H3
```

That is, SMGA improves recall, abstraction, and evidence-supported planning beyond strong baselines.

### 17.3 SOTA-level success

SOTA-level claim requires:

```text
external benchmark improvement
+ strongest baseline comparison
+ cost reporting
+ judge reliability validation
```

Acceptable claim:

> SMGA achieves state-of-the-art or best-reported performance on history-dependent social memory tasks under the evaluated benchmark and baseline set.

Unacceptable claim:

> SMGA is the state-of-the-art memory framework for all LLM agents.

---

## 18. Downgrade Rules

| Result pattern | Downgrade |
|---|---|
| M0_prompted matches M3 | contribution is prompt-level guidance, not architecture |
| M0_plus matches M3 | gains come from extra reasoning budget |
| M3_placebo changes behavior similarly to M3 | behavior change comes from interface/prompt, not memory content |
| GraphMemory_social_schema matches M3 | SMGA is not stronger than A-MEM/social graph style memory |
| Recall improves but planning does not | memory reporting improvement only |
| Planning improves but behavior does not | planning-rationale improvement only |
| Evidence IDs fail human validation | evidence-grounding claim invalid |
| Human-LLM agreement below threshold | LLM-judge metrics downgraded to exploratory |
| External benchmark fails | diagnostic-only contribution |
| Only one model shows gains | model-specific result |
| Cost-normalized performance worse by large margin | reliability-cost trade-off, not efficiency gain |

---

## 19. Relation to Prior Work

### 19.1 Generative Agents

SMGA builds directly on GA. GA contributes memory stream, reflection, and planning. SMGA asks whether reflections should become typed, evidence-verified, planning-actionable memory objects, and evaluates this under behavior-transfer tests.

### 19.2 CoALA and cognitive architectures

CoALA-style frameworks show that memory components are central to language-agent architecture. SMGA is a concrete memory architecture and evaluation protocol for GA-style social agents.

### 19.3 MemoryBank and MemGPT

Long-term memory systems handle persistence, retrieval, context management, and forgetting. SMGA focuses on how social experiences become structured planning context.

### 19.4 Reflexion and Voyager

Reflection and experience abstraction can improve future behavior. SMGA differs by focusing on long-horizon social memories, entity grounding, evidence verification, and behavior transfer in social interaction.

### 19.5 A-MEM, graph memory, AriGraph, and G-Memory

These are the closest competitors.

SMGA must not claim novelty merely from using links, evidence, or entity indexing.

The proposed incremental contribution is:

```text
GA-specific memory architecture
+ typed social memory schema alternatives
+ planning-actionable affordance interface
+ budget/prompt/placebo-controlled evaluation
+ evidence-provenance validation
+ behavior-transfer metrics
+ external history-dependent social benchmark
```

The strongest comparison is:

```text
SMGA vs GraphMemory_social_schema
```

If SMGA does not beat this comparison, the paper should frame the result as showing that social graph memory is sufficient.

### 19.6 Social interaction benchmarks

SOTOPIA-style benchmarks are important because they evaluate social interaction rather than only memory QA. SMGA uses external history-dependent social tasks to avoid overfitting to self-authored diagnostic settings.

---

## 20. Implementation Requirements

### 20.1 Memory object schema

Required fields:

```text
memory_id
memory_type
subject_entity
related_entities
claim
supporting_evidence_ids
contradicting_evidence_ids
negative_evidence_ids
validity_scope
planning_affordances
confidence
calibrated_confidence
created_at
updated_at
source_episode_ids
update_history
used_in_plans
outcome_feedback
```

### 20.2 Planning trace schema

Required fields:

```text
plan_id
agent_id
goal
candidate_actions
chosen_action
used_memory_ids
supporting_evidence_ids
negative_evidence_ids
rejected_memory_ids
rationale
condition
model
seed
token_cost
latency_ms
outcome
```

### 20.3 Evaluation output schema

Required outputs:

```text
results/smga/{benchmark}/{condition}/{seed}/events.jsonl
results/smga/{benchmark}/{condition}/{seed}/episodic_memory.jsonl
results/smga/{benchmark}/{condition}/{seed}/structured_memory.jsonl
results/smga/{benchmark}/{condition}/{seed}/retrieval_calls.jsonl
results/smga/{benchmark}/{condition}/{seed}/planning_traces.jsonl
results/smga/{benchmark}/{condition}/{seed}/judge_labels.jsonl
results/smga/{benchmark}/{condition}/{seed}/human_labels.jsonl
results/smga/{benchmark}/{condition}/{seed}/metrics.json
results/smga/{benchmark}/{condition}/{seed}/cost_latency.json
```

---

## 21. Revised Paper Structure

```text
1. Introduction
   - GA has memory and reflection, but reflection is not necessarily structured, verified, or planning-actionable.
   - Social agents need memory that transfers from experience to action.
   - We introduce SMGA and evaluate it against prompted, budget-matched, placebo, and graph-memory baselines.

2. Background and Related Work
   - Generative Agents
   - LLM agent memory
   - Reflection and experience abstraction
   - Agentic/graph memory
   - Social interaction benchmarks

3. SMGA Framework
   - structured social memory definition
   - schema alternatives
   - evidence and negative evidence
   - planning-actionable interface

4. Evaluation Design
   - external benchmark
   - diagnostic benchmark
   - memory conditions
   - schema ablations
   - placebo and compute controls

5. Evidence-Grounding Validation
   - human annotation
   - LLM-human agreement
   - provenance hallucination
   - calibration

6. Experiments
   - recall and abstraction
   - planning use
   - behavior transfer
   - external benchmark
   - model and cost analysis

7. Results
   - main contrasts
   - schema ablation
   - benchmark transfer
   - downgrade-rule checklist

8. Discussion
   - what structured memory improves
   - when prompted reflection is enough
   - limitations and costs

9. Conclusion
```

---

## 22. Response to Reviewer Concerns

### C1: Novelty boundary

Accepted. v3 no longer claims novelty from links, evidence, or entity indexing alone. The novelty is now framed as the combination of GA-specific structured social memory, planning-actionable affordances, behavior-transfer evaluation, and strong controls against prompted reflection, extra compute, placebo memory, and graph-memory baselines.

Added:

```text
GraphMemory_generic
GraphMemory_social_schema
schema ablations
main contrast against A-MEM-like social graph memory
```

### C2: Hand-engineered schema and circularity

Accepted. v3 adds:

```text
Schema_4
Schema_7
Schema_emergent
Schema_oracle
held-out experience types
```

The default schema is no longer claimed as exhaustive. It is an experimental condition.

### C3: Compute/call-count confound

Accepted. v3 adds:

```text
M0_plus
M0_prompted
cost-normalized metrics
LLM calls and token reporting
```

SMGA must beat these baselines to support the architecture claim.

### C4: “Situated” terminology

Accepted. v3 renames the technical focus to **Structured Memory for Generative Agents** and defines structured social memory operationally. The term “situated” is retained only as descriptive, not as a strong cognitive-science claim.

### C5: Evidence-grounding reliability

Accepted. v3 adds:

```text
human annotation of at least 200 claims
human-LLM agreement target
confidence calibration
hallucinated provenance detection
negative evidence tracking
```

### C6: Causal attribution of behavior change

Accepted. v3 adds:

```text
M3_placebo
memory-content sensitivity metric
required contrast M3 > M3_placebo
```

### C7: External benchmark and scale

Accepted. v3 makes external history-dependent social benchmark evaluation required for headline claims. Diagnostic benchmark remains a mechanism test. Main diagnostic contrasts use at least 50 seeds unless power analysis justifies fewer.

### Minor concerns

Addressed by:

```text
controlled planning-affordance vocabulary
promise detection protocol downgraded to secondary unless validated
minimum success raised to H1 + H2
cost/latency reporting
model-dependence analysis
negative_evidence_ids in trace schema
```

---

## 23. Remaining Risks

### Risk 1: Prompted GA may match SMGA

If `M0_prompted` matches M3, the architecture contribution weakens. The paper should then become a result about strong prompt-level reflection being sufficient for these tasks.

### Risk 2: Graph memory may match SMGA

If `GraphMemory_social_schema` matches SMGA, the contribution becomes evaluation and benchmarking rather than a new architecture.

### Risk 3: Evidence validation may be noisy

If human agreement is low, evidence-grounding metrics are unstable. The paper must report this honestly and rely on more objective task outcomes.

### Risk 4: Cost may be too high

If SMGA improves performance but at much higher cost, the system is useful mainly for high-stakes simulation and audit settings rather than large-scale deployment.

### Risk 5: External benchmark may not need structured memory

Some social tasks may be solvable by strong LLM priors. The benchmark subset must emphasize history-dependent tasks where past interaction context is necessary.

---

## 24. Final v3 Position

SMGA v3 is strongest if framed as:

> A controlled architecture and evaluation study of whether structured, evidence-verified social memory improves long-horizon, history-dependent planning in GA-style agents beyond reflection, prompted reflection, extra reasoning budget, placebo interfaces, and generic graph memory.

The project is worth pursuing if it can show:

```text
M3 > M0_prompted
M3 > M0_plus
M3 > M3_placebo
M3 > GraphMemory_social_schema
```

on at least:

```text
evidence-supported recall
abstraction validity
evidence-supported planning
history-dependent behavior
```

The strongest paper is not one that claims all memory is solved. It is one that carefully identifies when structured social memory matters, when prompted reflection is enough, and how future generative agents should connect memory, evidence, and planning.
