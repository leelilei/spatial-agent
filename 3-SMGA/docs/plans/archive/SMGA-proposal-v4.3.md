# SMGA Proposal v4.3

## Structured Memory for Generative Agents

> Working title: **Structured Memory for Generative Agents: Evidence-Grounded Social Context for Long-Horizon Planning**
> Short name: **SMGA**
> Version: **0.4.3**
> Date: **2026-05-19**
> Status: v4.3 update: AGA-style narrative simplification; method reorganized into two modules; main ablation and mechanism analysis clarified
> Relation to v4.2: keeps the three claim-family hypothesis structure and LIFELONG-SOTOPIA / SOTOPIA-π-ME benchmark strategy, but rewrites the proposal in an Affordable-Generative-Agents-style frame: one bottleneck, two modules, one main ablation table, explicit cost reporting, and mechanism analysis.

---

## 0. One-Line Version

SMGA asks whether the main bottleneck in GA-style long-horizon social agents is not remembering per se, but **turning past social experience into reliable planning context**.

> **SMGA converts GA-style open-ended reflections into structured, evidence-grounded, planning-actionable social memories, so agents can use past social interactions more reliably in long-horizon planning.**

The central question:

> Under matched model, prompt, compute, interface, and scenario controls, do structured social memory objects improve history-dependent social planning and behavior beyond GA reflection, prompted reflection, placebo memory, and graph-memory baselines?

---

## 1. What Changed in v4.3

v4.3 keeps the v4.2 hypothesis organization and the v4.1 benchmark decision. The main change is **paper shape**. Inspired by the clarity of *Affordable Generative Agents* (AGA), v4.3 rewrites SMGA around one bottleneck, two modules, and a clean main ablation story.

AGA's structure is simple: GA is expensive; the paper identifies where cost arises; it introduces two modules; it shows cost drops while believability remains comparable. v4.3 adopts the same discipline without copying AGA's technical target:

```text
AGA:  GA has a cost bottleneck.
      Reduce repeated LLM inference while preserving believable behavior.

SMGA: GA has a social-memory-use bottleneck.
      Structure and ground social memory so it can support long-horizon planning.
```

| v4.3 issue | v4.3 change |
|---|---|
| The proposal still read like a large research program | §2 compresses the claim into one sentence: convert GA reflections into structured, evidence-grounded, planning-actionable social memory |
| The method was described as four engineering layers before the reader saw the paper idea | §7 now presents two modules first: **Structured Social Memory Formation** and **Evidence-Grounded Planning Interface**; L1–L4 remain as implementation layers |
| The ablation story was less visually simple than AGA's Lifestyle Policy / Social Memory / full AGA table | §8 adds an AGA-style main ablation table: `M0_GA`, `M0_prompted`, `M2_memory_only`, `M3_placebo`, `M3_actionable`, `GraphMemory_social_schema` |
| Cost was treated as reporting rather than as a central control against the “more LLM calls” objection | §10.5 and §14.2 make calls, tokens, latency, and cost-normalized success mandatory in main result tables |
| The proposal lacked an AGA-style mechanism analysis section | §12.5 adds error decomposition, load-bearing field ablations, and history-dependence taxonomy analysis |
| AGA also has a module called Social Memory, creating possible novelty confusion | §20 explicitly distinguishes AGA's cost-saving social impression memory from SMGA's evidence-grounded planning memory |

### v4.2 changes retained

v4.2 changed the hypothesis narrative from five parallel hypotheses to **three claim families** with operational sub-tests:

```text
social experience
→ evidence-grounded memory formation
→ structured abstraction
→ memory-grounded planning
→ history-dependent behavior
→ external lifelong-social validation
```

Claim Family 1 tests evidence-grounded social memory. Claim Family 2 tests memory-grounded planning and behavior. Claim Family 3 tests external lifelong-social validation.

### v4.1 changes retained

v4.1 updated the benchmark strategy after reviewing LIFELONG-SOTOPIA. The key retained decision is conceptual: LIFELONG-SOTOPIA is useful for SMGA only if it is treated as an **external behavioral testbed for memory architectures**, not as a model leaderboard. We compare memory frameworks under a fixed base model, fixed scenario chains, matched prompts, and fixed evaluation settings.

| v4.1 issue | v4.1 change retained in v4.3 |
|---|---|
| LIFELONG-SOTOPIA directly evaluates language agents/models, while SMGA evaluates memory architecture | §9 states that LIFELONG-SOTOPIA is used only for **fixed-base-model memory-framework comparison**: `M3_actionable` vs `M0_GA`, `M0_prompted`, `M3_placebo`, and `GraphMemory_social_schema` |
| External benchmark plan risked duplicating LIFELONG-SOTOPIA | §9 makes LIFELONG-SOTOPIA the **preferred external benchmark when runnable**, and keeps SOTOPIA-π-ME as the **fallback / controlled extension** |
| SOTOPIA-π-ME was large enough to look like a separate benchmark paper | §9.3 narrows it: in this proposal it is a deliverable only if needed for fallback or for evidence-grounded annotations unavailable in LIFELONG-SOTOPIA |
| Behavior metrics lacked explicit social-realism gates | §10.4 adds `GOAL`, `BEL`, and `BELEXT-adjusted BEL`; external success cannot be claimed if SMGA improves task success by degrading believability |

### v4 changes retained from v3 review

v3 addressed every major v2 concern (novelty boundary, schema circularity, compute confound, situated-cognition framing, evidence-grounding reliability, causal attribution, external benchmark). v4 addressed the remaining scope, graph-baseline, emergent-schema, external-benchmark, engineering, and partial-success concerns through tiered conditions, explicit memory contracts, a concrete emergent-schema protocol, staged execution, and downgrade rules.

## 2. Core Claim

> **SMGA converts GA-style open-ended reflections into structured, evidence-grounded, planning-actionable social memory objects, and tests whether those objects improve history-dependent planning and behavior beyond matched memory baselines.**

The claim is intentionally narrower than “better agents.” SMGA is a controlled architecture-and-evaluation study of whether social memories become more useful when they are typed, entity-grounded, provenance-checkable, contradiction-aware, validity-scoped, and exposed to planning through auditable affordances.

The main contrast is:

```text
GA-style memory stream + reflection
vs.
GA-style memory stream + structured social memory formation + evidence-grounded planning interface
```

Explicitly **not** claimed:

```text
SMGA is a universal memory SOTA for all LLM agents.
SMGA proves human-like situated cognition.
SMGA replaces GA reflection.
SMGA wins because it simply calls the LLM more often.
SMGA is a cost-reduction method like Affordable Generative Agents.
```

## 3. Research Gap


### 3.1 What GA contributes

GA established a working architecture: `observation → memory stream → retrieval → reflection → planning → action`. SMGA builds on this; it does not dismiss it.

AGA showed that GA can be optimized cleanly by identifying a concrete bottleneck and modifying only the relevant interaction pathways. SMGA follows that style, but targets a different bottleneck: not repeated LLM cost, but the weak conversion from past social experience to reliable planning context.

### 3.2 What remains unresolved

1. **Reflection exists but is not schema-enforced.** GA reflections are natural-language thoughts; they are not required to carry `memory_type`, `subject_entity`, `supporting_evidence_ids`, `contradicting_evidence_ids`, `validity_scope`, `planning_affordances`, or `update_history`. Downstream planning therefore cannot know *what kind* of memory a thought is or *how* to use it.

2. **Entity-indexed memory exists in graph systems, but behavior transfer is under-tested.** Most graph and agentic-memory systems are evaluated on retrieval and QA, not on the full chain `recall → abstraction → planning evidence → action → outcome`.

3. **Prompted reflection may be a strong baseline.** "Reflect about people, places, relationships, activities, routines" is cheap. If it matches structured memory, the contribution is prompt engineering, not architecture. v4 treats `M0_prompted` as a *required* baseline.

4. **Extra compute may explain gains.** More LLM calls = more thinking. v4 requires compute-matched baselines (`M0_plus`) and cost-normalized reporting.

5. **Evidence-grounding cannot be self-reported.** An LLM that produces both a claim and the evidence IDs is grading its own homework. v4 requires external human validation before any LLM-judge metric is trusted.

---

## 4. Definition

A **structured social memory object** satisfies four contracts:

1. **Typed** — belongs to a declared or discovered class (person / place / relationship / activity / routine / norm / information state).
2. **Entity-grounded** — links to concrete entities, events, agents, places, topics in the simulation log.
3. **Evidence-verified** — stores both **supporting** and **contradicting** evidence IDs that can be checked by non-agent evaluators against gold logs.
4. **Planning-actionable** — exposes affordances from a controlled vocabulary, each affordance independently grounded in evidence (not free-form planner invention).

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
  "calibrated_confidence": null,
  "created_at": "sim_day_3_18:00",
  "updated_at": "sim_day_3_18:00",
  "used_in_plans": []
}
```

The crucial point is that **every field except `claim` and `confidence` is auditable against the gold event log**. This is what makes structured memory falsifiable.

---

## 5. Research Questions

v4.2 keeps five research questions, but maps the hypotheses into three claim families so the paper is not framed as five unrelated claims. The dropped RQ from v3 (cost/model dependence) remains a reporting requirement rather than a primary question.

**RQ1 — Memory formation.** Does SMGA produce more accurate, evidence-supported structured social memories than GA reflection, prompted GA reflection, and graph memory with social schema?

**RQ2 — Schema contribution.** Does the proposed schema matter, or do coarse, emergent, or oracle schemas match it?

**RQ3 — Planning transfer.** Do structured social memories improve planning decisions beyond what recall and abstraction quality alone predict?

**RQ4 — Behavioral transfer.** Do agents using SMGA take better history-dependent actions, and is the change driven by *memory content* rather than interface or compute?

**RQ5 — External validity.** Does SMGA improve the performance of a **fixed-base-model agent** on an external history-dependent social benchmark, relative to memory-architecture baselines under matched model, scenario, prompt, and evaluation settings?

---

## 6. Claim Families and Operational Hypotheses

v4.2 no longer presents five hypotheses as five parallel paper claims. Instead, the experiments test a staged mechanism:

```text
social experience
→ evidence-grounded social memory
→ memory-grounded planning
→ history-dependent behavior
→ external lifelong-social validation
```

We therefore organize the hypotheses into **three claim families**. Each family has operational sub-tests with a **primary metric**, a **required contrast set**, and a **smallest effect of interest (SESOI)**. If the observed effect is below SESOI, the sub-test is treated as not supported even if statistically significant.

### Claim Family 1 — Evidence-grounded social memory

**Core claim.** SMGA produces more accurate, human-verifiable, evidence-supported structured social memories than prompted reflection and graph-memory baselines.

#### H1a — Evidence-supported structured recall

- Primary metric: `evidence-supported structured recall F1`
- Required: `M3 > M0_prompted` and `M3 > M0_plus`
- SESOI: +0.08 absolute over `M0_prompted`

#### H1b — Valid abstraction beyond prompted reflection

- Primary metric: `human-verified abstraction validity`
- Required: `M2 or M3 > M0_prompted` and `M2 or M3 > GraphMemory_social_schema`
- SESOI: +0.10 absolute over the stronger of the two baselines

**Interpretation.** H1a asks whether the right social information is recalled with valid evidence. H1b asks whether the system turns episodic facts into valid social abstractions. Together, they support the representation claim; alone, they do not prove behavioral improvement.

### Claim Family 2 — Memory-grounded planning and behavioral transfer

**Core claim.** SMGA improves history-dependent planning and behavior, and the improvement is driven by memory content rather than interface, prompt, or compute effects.

#### H2a — Evidence-supported planning

- Primary metric: `evidence-supported planning rate`
- Required: `M3 > M3_placebo` and `M3 > M0_prompted`
- SESOI: +0.10 absolute over `M0_prompted`

#### H2b — Target-consistent behavior

- Primary metric: `target-consistent behavior rate`
- Required: `M3 > M3_placebo` and `M3 > M0_prompted`
- SESOI: +0.08 absolute over `M0_prompted`

#### H2c — Memory-content sensitivity

- Primary metric: paired behavior gap between `M3_actionable` and `M3_placebo`
- Required: `M3_actionable > M3_placebo` on history-dependent probes under matched interface, prompt, and base model
- SESOI: +0.08 absolute over `M3_placebo`
- This is the main causal-control test. If `M3_placebo` matches `M3_actionable`, observed behavior changes are treated as interface or prompt effects, not memory-content effects.

**Interpretation.** H2a tests whether memory enters the planner as grounded evidence. H2b tests whether agent actions improve. H2c tests whether the improvement depends on the actual memory content.

### Claim Family 3 — External lifelong-social validation

**Core claim.** Under a fixed base model and matched evaluation setup, SMGA improves history-dependent social task success on an external lifelong-social benchmark without sacrificing social realism.

#### H3 — External benchmark improvement

- Primary metric: `history-dependent social task success` on LIFELONG-SOTOPIA when it is publicly runnable and compatible with custom memory architectures; otherwise on the SOTOPIA-π-ME fallback (see §9)
- Required: `M3 > strongest baseline` under a fixed base model and matched scenario/prompt/evaluator settings
- Social-realism gate: H3 is not supported if `M3` improves task success by significantly degrading `BEL` or `BELEXT-adjusted BEL`
- SESOI: +0.05 normalized score

**Interpretation.** H3 is an external-validity test, not the main mechanism proof. The mechanism proof comes from Claim Families 1 and 2 on the diagnostic benchmark.

## 7. Method Overview: Two SMGA Modules

v4.3 presents SMGA as two modules rather than starting from four low-level layers. The four layers remain, but they are now grouped by the paper's main causal story.

```text
GA baseline:
observation → memory stream → retrieval → reflection → planning → action

SMGA additions:
observation / dialogue / event log
→ Module A: Structured Social Memory Formation
→ Module B: Evidence-Grounded Planning Interface
→ action + auditable planning trace
```

A paper figure should mirror AGA's style: gray arrows for the GA baseline path and blue arrows for the SMGA additions. The figure should make clear that SMGA does not replace GA's memory stream or reflection; it constrains how social memories are formed and how they enter planning.

### 7.1 Module A — Structured Social Memory Formation

This module converts episodic experiences, dialogue history, and open-ended reflections into structured social memory objects. It implements:

- **L1 Episodic memory.** GA-compatible memory stream: `event_id`, text, time, actors, location, activity, topic, valence.
- **L2 Entity indexing.** Each episodic memory is indexed by people, places, relationships, activities, routines, norms, and information states.
- **L3 Typed social abstraction.** The system forms structured memory objects per §4. The schema is an experimental variable rather than an assumed truth (§8.3).

The key difference from GA reflection is not that SMGA reflects more, but that reflection outputs must become auditable objects with memory type, subject entity, evidence, contradiction awareness, validity scope, confidence, update history, and candidate planning affordances.

### 7.2 Module B — Evidence-Grounded Planning Interface

This module exposes structured memories to the planner in a controlled way and forces the planner to record how memory affected action choice. It implements:

- **L4 Planning-actionable memory.** Planning receives structured memory candidates with supporting and contradicting evidence.
- **Affordance interface.** The planner receives controlled-vocabulary affordances such as `seek_contact`, `repair_relationship`, `maintain_privacy`, or `follow_commitment` (§12).
- **Auditable planning trace.** Planner output must record `chosen_action`, `used_memory_ids`, `supporting_evidence_ids`, `negative_evidence_ids`, `rejected_memory_ids`, `rationale`, and `outcome`.

This interface is the main operational difference between “having memories” and “using memories for planning.” It also creates the data needed to test whether behavior changes are driven by memory content rather than prompt format or interface effects.

### 7.3 Ablatable implementation layers

The two modules decompose into four ablatable layers:

| Layer | Role | Primary diagnostic condition |
|---|---|---|
| L1 Episodic memory | GA-compatible event stream | `M0_GA` |
| L2 Entity indexing | entity retrieval over social logs | `M1_indexed` |
| L3 Typed abstraction | structured social memory objects | `M2_memory_only` / `M2_typed` |
| L4 Planning interface | affordance-conditioned planning with trace | `M3_actionable` |

The main treatment is `M3_actionable` = L1 + L2 + L3 + L4. The key ablation is `M2_memory_only`: structured memory exists and can be retrieved, but the planner does not receive the SMGA planning contract. This separates “better memory representation” from “better planning interface.”

## 8. Experimental Conditions (tiered)

v4.3 keeps the staged design but makes the main comparison more AGA-like: a compact ablation table showing baseline, partial modules, full SMGA, placebo, and architecture control.

### 8.1 Main diagnostic ablation conditions

These conditions are the main table for the diagnostic benchmark. They are designed to answer a simple question: does improvement come from prompting, memory representation, planning interface, memory content, or a graph-memory alternative?

| Condition | Description | Purpose |
|---|---|---|
| `M0_GA` | GA-style memory stream + retrieval + reflection | classic baseline |
| `M0_prompted` | GA reflection prompt explicitly asks about people / places / relationships / activities / routines / norms / information states | cheap-prompt control |
| `M2_memory_only` | SMGA structured memory formation is enabled, but the planner receives memories only as ordinary retrieved context, without the SMGA planning contract | representation-only ablation |
| `M3_placebo` | SMGA planning interface is enabled, but memory content is random, stale, or irrelevant under matched format | interface/placebo control |
| `M3_actionable` | full SMGA: structured memory formation + evidence-grounded planning interface | main treatment |
| `GraphMemory_social_schema` | graph memory with social schema, but without SMGA evidence/contradiction/validity/affordance/planning-trace contracts | architecture control vs graph memory |

This table is the SMGA analogue of AGA's “module only / module only / full system” table. The most important comparisons are:

```text
M3_actionable > M0_prompted              prompt control
M3_actionable > M2_memory_only           planning-interface contribution
M3_actionable > M3_placebo               memory-content sensitivity
M3_actionable > GraphMemory_social_schema architecture/contract contribution
```

### 8.2 External benchmark conditions

For LIFELONG-SOTOPIA or SOTOPIA-π-ME, the full external comparison uses the fixed-base-model setup from §9.2. The minimum external set is:

```text
M0_GA
M0_prompted
M3_actionable
M3_placebo
GraphMemory_social_schema
```

`M2_memory_only` is included externally if budget allows, but it is not required for the external-validity claim. Its main role is mechanism diagnosis on the controlled benchmark.

### 8.3 Secondary conditions (diagnostic only, reduced seeds)

| Condition | Purpose |
|---|---|
| `M0_plus` | reflection frequency / token budget / call count matched to M3 — compute control |
| `M1_indexed` | tests whether indexing alone explains gains |
| `GraphMemory_generic` | graph structure without social schema |
| field ablations | remove one SMGA contract at a time: evidence IDs, contradicting evidence, validity scope, planning affordances, update history |

### 8.4 Schema ablation (secondary)

| Schema | Description |
|---|---|
| `Schema_4` | coarse: person, place, relation, event |
| `Schema_7` | proposed: person, place, relationship, activity, routine, norm, information |
| `Schema_emergent` | LLM-proposed types from held-out logs, frozen before evaluation (§18) |
| `Schema_oracle` | human-designed after seeing task family — upper-bound only |

### 8.5 Held-out experience types

To prevent benchmark-schema circularity, the following social patterns are **withheld from schema examples and Phase-1 templates**:

```text
triadic mediation
indirect reputation transfer
failed promise
shared secret
norm violation
repair after conflict
```

At least one held-out type is included in every Phase-2 evaluation. Pre-registered: which types are train vs held out, locked before any model run.

## 9. Benchmark Strategy

v4.1 separates **mechanism validation** from **external behavioral validation**. The diagnostic benchmark remains the main tool for proving the SMGA mechanism. LIFELONG-SOTOPIA is used, when runnable, to test whether that mechanism transfers to an independently proposed lifelong social-interaction setting. SOTOPIA-π-ME remains the concrete fallback and controlled extension.

### 9.1 Diagnostic benchmark — primary mechanism validation

Self-authored, used for mechanism validation, schema ablation, placebo controls, provenance checking, and behavioral probes — **not** for headline external-benchmark claims.

Scale:

```text
agents: 6-10
locations/contexts: 6-10
simulation length: 3-5 days
seeds: minimum 50 for primary contrasts
phase 1 (controlled exposure) + phase 2 (planning/behavior probes)
```

Phase-1 safeguards: event templates generated before any model run; held-out types excluded from templates; distractor events included; same event log replayed across memory conditions for paired comparison.

The diagnostic benchmark is required because SMGA's central claims involve provenance and mechanism: whether memory claims are evidence-supported, whether contradictory evidence is represented, whether planning traces cite the right memories, and whether behavior changes are driven by memory content rather than interface or compute. LIFELONG-SOTOPIA-style BEL/GOAL scores alone cannot establish these mechanism claims.

### 9.2 Preferred external benchmark — LIFELONG-SOTOPIA, if runnable

**Preferred external behavioral testbed:** `LIFELONG-SOTOPIA`, when its data, code, and interface are publicly runnable and allow custom memory-architecture agents.

We do **not** use LIFELONG-SOTOPIA as a model leaderboard. Its original framing evaluates language agents/models over lifelong social interactions. Our use is different: we fix the base model, scenario chains, prompts, evaluator, and decoding settings, and vary only the memory architecture:

```text
M0_GA
M0_prompted
M3_actionable
M3_placebo
GraphMemory_social_schema
```

The external claim is therefore:

> Under the same base LLM and the same LIFELONG-SOTOPIA episode chains, an agent equipped with SMGA memory performs better than matched agents using GA reflection, prompted reflection, placebo memory, or graph memory.

Primary external outcomes:

```text
history-dependent GOAL / task success
BEL
BELEXT-adjusted BEL
GOAL-BEL tradeoff gate
```

H5 is supported only if SMGA improves history-dependent task success without a meaningful drop in social realism. This prevents a failure mode where the agent completes the task by acting unnaturally, exposing private goals, leaking internal memory objects, or using past history in a socially inappropriate way.

### 9.3 Fallback and controlled extension — SOTOPIA-π-ME

If LIFELONG-SOTOPIA is not runnable, does not expose enough hooks for custom memory architectures, or lacks the evidence annotations needed for SMGA's provenance checks, we use **SOTOPIA-π-ME** as the fallback external benchmark and release it as part of this work.

SOTOPIA-π-ME extends SOTOPIA-π scenarios into 3–5 paired episodes per scenario. The second-and-later episodes are designed to require use of earlier interaction history, such as:

```text
remembering prior interactions
tracking promises and commitments
adapting to changed relationships
using prior conflict or cooperation
maintaining persona-consistent social history
tracking information ownership and shared secrets
responding to norm violations and repair attempts
```

Unlike a generic multi-episode chain, SOTOPIA-π-ME includes explicit history-dependence annotations:

```text
required_prior_evidence_ids
required_memory_type
success_condition
failure_condition
contradicting_evidence_ids
acceptable_planning_affordances
no-history solvability flag
BEL / BELEXT social-realism gate
```

The fallback is deliberately scoped. SOTOPIA-π-ME may later support a separate benchmark paper, but in this proposal it is treated as an engineering deliverable that guarantees H3 remains executable and that the external setting can support SMGA's evidence-grounded evaluation needs.

### 9.4 SOTOPIA / SOTOPIA-hard — base environment and sanity check

Original SOTOPIA and SOTOPIA-hard remain useful for implementation sanity checks and custom-agent integration. They are not the primary external memory benchmark because their core tasks are not necessarily history-dependent across episodes.

---

## 10. Metrics (consolidated)

### 10.1 Recall and memory quality

`structured recall F1` · `unsupported memory claim rate` · `hallucinated provenance rate` · `contradiction awareness rate` · `calibration error`

### 10.2 Abstraction quality

`abstraction validity` (human-verified) · `overgeneralization rate` · `schema assignment accuracy` · `held-out type generalization`

### 10.3 Planning quality

`evidence-supported planning rate` · `negative-evidence use rate` · `memory-content sensitivity (M3 vs M3_placebo)` · `prompted-baseline gain (M3 vs M0_prompted)`

### 10.4 Behavior and social realism

`target-consistent behavior rate` · `history-dependent task success` · `relationship-consistency score` · `social coherence rating` (blinded, condition-hidden)

External social-interaction metrics:

```text
GOAL / history-dependent task success
BEL
BELEXT-adjusted BEL
GOAL-BEL tradeoff gate
no-history solvability filter
```

For LIFELONG-SOTOPIA or SOTOPIA-π-ME, SMGA is not treated as successful if it improves goal completion by producing less believable social behavior. BELEXT-style checks include repetition, persona confusion, current-goal confusion, failure to exit after goal resolution, verbatim private-goal disclosure, stalling, non-responsive dialogue, abrupt episode opening, internal-memory leakage, and socially inappropriate use of past history.

### 10.5 Cost and compute controls (required in every main table)

`input/output tokens` · `LLM calls` · `wall-clock latency` · `storage footprint` · `cost-normalized success`

Unlike AGA, SMGA does **not** claim lower cost. Cost is reported to rule out a simpler explanation: that SMGA wins only because it calls the LLM more often or passes longer prompts. Every main diagnostic and external result table must include raw performance and cost-normalized performance.

**Removed from v3:** standalone promise-follow-through section. Promise tracking is now a single secondary metric under 10.4, validated only if the detection pipeline passes the agreement threshold in §11.

---

## 11. Evidence-Grounding Protocol

### 11.1 Why this is necessary

A memory can cite an evidence ID that exists but does not actually support the claim. LLM judges grading other LLMs' provenance compounds the problem. Evidence-grounding is therefore validated **outside** the agent and **outside** the judge LLM, against the gold event log and human annotation.

### 11.2 Human annotation

Minimum requirement:

```text
sample size: ≥ 200 memory/planning claims, stratified across conditions and memory types
labels: supports / contradicts / irrelevant / insufficient
annotators: ≥ 2 independent, blinded to condition
agreement target: Cohen's κ ≥ 0.6 on a 50-claim pilot before scaling
```

**IRB and compensation.** Annotators are recruited under our institution's IRB-approved protocol for non-clinical text annotation. Compensation at or above local minimum wage equivalent. Annotation guidelines, examples, and edge cases are released as supplementary material.

### 11.3 LLM judge validation

LLM judges are used at scale **only after** human-LLM agreement is validated on the pilot set. Reported: human-LLM agreement (κ), disagreement analysis, precision/recall of support detection, hallucinated-provenance detection rate.

If human-LLM κ < 0.5, the LLM-judge metric is downgraded to exploratory.

### 11.4 Calibration

Raw confidence is logged but headline metrics use **calibrated** confidence. Calibration map is fit on a dev set (1000 claims) and frozen before test. Expected calibration error reported per condition.

### 11.5 Negative evidence

Every structured memory and every planning trace records `contradicting_evidence_ids` / `negative_evidence_ids` / `rejected_memory_ids`. A plan that cites only supporting evidence while ignoring strong contradictory evidence in the log is marked **biased evidence use** — a separate metric from "unsupported."

---

## 12. Planning Affordances

Free-form affordances explode; fixed lists limit generalization. v4 uses a **hybrid controlled vocabulary**:

```text
seek_contact · avoid_contact · seek_information · share_information
repair_relationship · maintain_privacy · choose_collaboration_context · follow_commitment
```

Primary metrics evaluate only this frozen vocabulary. Open-extension affordances are allowed but logged separately for exploratory analysis.

Affordances are generated from structured memory by constrained prompts or rule templates; the trace records whether each affordance was `rule-derived` / `LLM-derived under constrained vocabulary` / `human-validated`.

---

## 12.5 Mechanism Analysis

Following the AGA paper's style, SMGA should not only report that the method works; it should explain **when** and **why** it works. Mechanism analysis is diagnostic rather than a separate headline claim.

### 12.5.1 Error decomposition

For failed probes, annotate the earliest failure point in the causal chain:

```text
memory formation failure
evidence-grounding failure
abstraction / overgeneralization failure
retrieval failure
planning misuse
behavior execution failure
social-expression / BEL failure
```

This prevents vague post-hoc claims like “the agent failed to use memory.” The analysis should identify whether the memory was absent, unsupported, contradicted, not retrieved, ignored by the planner, or used in a socially unnatural way.

### 12.5.2 Load-bearing field ablations

Run reduced-seed ablations that remove one SMGA contract at a time:

```text
remove supporting_evidence_ids
remove contradicting_evidence_ids
remove validity_scope
remove planning_affordances
remove entity grounding
remove update_history
```

The goal is to test whether the bold contracts in §19 are actually load-bearing for planning and behavior, not just aesthetically cleaner memory records.

### 12.5.3 History-dependence taxonomy

Report results by social-history type:

```text
promise / commitment
relationship change
shared secret
indirect reputation
norm violation
repair after conflict
information ownership
prior cooperation or conflict
```

This analysis tells us where structured social memory helps most and where it still fails. It also makes the diagnostic benchmark useful beyond the SMGA method itself.

---

## 13. Statistical Analysis

### 13.1 Unit of analysis

Paired seeds: same agent profiles, initial states, scripted event log, task prompts, model configuration — only the memory architecture differs.

### 13.2 Primary mixed-effects model

```text
outcome ~ condition + task_type + schema_condition + model_family
        + (1 | seed) + (1 | agent) + (1 | scenario)
```

### 13.3 Fallback model

With 50 seeds × 8 agents × ~6 scenarios, the three crossed random effects may fail to converge. **Pre-registered fallback** (in order):

1. Drop `(1 | scenario)` if singular fit on scenario variance.
2. If still singular, drop `(1 | agent)` and use cluster-robust SEs at the agent level.
3. If still singular, switch to paired-difference tests on seed-level aggregated metrics with Holm correction across the 4 primary contrasts.

The choice between primary and fallback is **made on convergence diagnostics, not on the size of the effect**, and is logged in the results.

### 13.4 Main contrasts (FDR-controlled within family)

```text
M3 > M0_prompted        (cheap-prompt test)
M3 > M0_plus            (compute test — secondary scale)
M3 > M3_placebo         (memory-content test)
M3 > GraphMemory_social_schema   (architecture test)
```

---

## 14. Model Dependence and Cost

### 14.1 Model plan

Required: one frontier API model, one strong open-weight model. Optional: one smaller open model as stress test.

Reported per model: whether gains replicate, whether structured memory helps weaker models more or less, whether schema-following failures dominate weaker models.

If only the frontier model shows gains, the claim narrows to: *SMGA improves structured memory use for strong instruction-following LLM agents; model generality is limited.*

### 14.2 Cost

Every main result table reports cost (input tokens, output tokens, calls, latency, storage) alongside raw performance, plus a cost-normalized column. This is not because SMGA aims to beat AGA on affordability, but because compute is a major confound in memory-agent evaluation.

Interpretation guide:

| Pattern | Interpretation |
|---|---|
| SMGA better and cost-normalized better | strong architecture result |
| SMGA better but cost-normalized worse | reliability/auditability trade-off; claim must be framed as quality gain, not efficiency gain |
| SMGA better than `M0_GA` but not `M0_plus` | gain is from extra reasoning budget, not structure |
| SMGA improves only when context length is much larger | memory-format advantage is confounded with information volume |

---

## 15. Success Criteria

v4.3 evaluates success by **claim family**, not by a flat count of five parallel hypotheses. Operational sub-tests remain pre-registered, but the paper framing depends on which claim families hold.

### 15.1 Partial success

Partial success is publishable when at least one coherent claim family is supported, but broader claims are withdrawn.

| Pattern that holds | Reframing |
|---|---|
| Claim Family 1 only (`H1a + H1b`) | "structured memory as a high-fidelity, auditable representation of social experience" — recall/abstraction contribution; planning and behavioral claims withdrawn |
| Claim Family 1 + H2a only | "structured memory improves evidence-grounded planning rationales" — behavior claim withdrawn; useful for simulation, audit, and interpretability |
| H2a + H2b hold but H2c fails | planning/behavior change may be interface-driven; memory-content claim withdrawn |
| H2b or H2c hold without Claim Family 1 | likely confound or unobserved mechanism; result reframed as exploratory; main architecture claim not submitted |
| Claim Families 1 and 2 hold but H3 fails | strong diagnostic contribution; no external/SOTA claim |

Partial success plus H3 is publishable as a strong paper if the external social-realism gate is satisfied.

### 15.2 Minimum success

Minimum success requires **Claim Family 1** to hold: H1a and H1b both supported against `M0_prompted`, with H1b also beating `GraphMemory_social_schema`. Below this, the structured-memory representation claim is not supported.

### 15.3 Strong success

Strong success requires **Claim Families 1 and 2** to hold: evidence-grounded memory improves, planning becomes more evidence-supported, behavior improves on history-dependent probes, and `M3_actionable > M3_placebo` demonstrates memory-content sensitivity.

### 15.4 SOTA-level / external success

SOTA-level success requires strong success **plus Claim Family 3** on the preferred external benchmark (LIFELONG-SOTOPIA if runnable; SOTOPIA-π-ME fallback otherwise), with cost reporting, validated judge reliability, and no degradation on `BEL` / `BELEXT-adjusted BEL`.

Acceptable claim form: *SMGA achieves state-of-the-art performance on history-dependent social memory tasks under the evaluated benchmark and baseline set.* Anything broader is not claimed.

## 16. Downgrade Rules

| Result | Downgrade |
|---|---|
| `M0_prompted` matches `M3` | contribution is prompt-level guidance, not architecture |
| `M0_plus` matches `M3` | gains are extra reasoning, not structure |
| `M3_placebo` matches `M3` on behavior | behavior change is interface effect, not memory content |
| `GraphMemory_social_schema` matches `M3` | social graph memory is sufficient; SMGA's planning-interface contribution is not load-bearing |
| `Schema_4` matches `Schema_7` | fine schema not necessary |
| `Schema_emergent` outperforms `Schema_7` | hand-engineered schema is suboptimal — reframe around emergent schema |
| Recall improves but planning does not | memory-reporting improvement only |
| Planning improves but behavior does not | rationale improvement only |
| Evidence IDs fail human validation | evidence-grounding claim invalid; downgrade to recall-only paper |
| Human-LLM κ < 0.5 | LLM-judge metrics exploratory only |
| External benchmark fails, or task success improves only by degrading BEL / BELEXT-adjusted BEL | diagnostic-only contribution; no SOTA claim |
| Only one model shows gains | model-specific result |
| Cost-normalized performance much worse | reliability/audit trade-off, not efficiency gain |

---

## 17. Staged Execution Plan

To address R1 (scope feasibility), the project executes in three stages with explicit go/no-go gates.

### Stage 1 — Pilot (≈6 weeks)

Run the **6 main diagnostic ablation conditions** × **5 seeds** × **frontier model only** on the diagnostic benchmark. Validate:

- annotation pipeline (κ ≥ 0.6 on 50 claims)
- planning-trace logging is complete and parseable
- `M3_placebo` is operationally distinct from `M3` (no information leakage from interface)
- pilot effect direction on H1a/H1b and H2b/H2c

**Gate 1** — proceed to Stage 2 if:
- annotation κ ≥ 0.6
- `M3` shows directional improvement over `M0_GA` on at least one memory-quality sub-test (H1a or H1b) and one transfer sub-test (H2b or H2c)
- `M3_placebo` does **not** match `M3_actionable` on the H2c memory-content sensitivity check (otherwise architecture is suspect even at pilot)

If gate 1 fails, return to design iteration; do not scale.

### Stage 2 — Main diagnostic (≈10 weeks)

6 main diagnostic ablation conditions × **50 seeds** × **2 models** (frontier + open-weight) on diagnostic. Schema ablations (`Schema_4`, `Schema_7`, `Schema_emergent`) at 25 seeds each on the frontier model only.

**Gate 2** — proceed to Stage 3 if:
- at least two operational sub-tests across Claim Families 1–2 meet SESOI, including at least one memory-quality test (H1a or H1b) and one planning/behavior-transfer test (H2a, H2b, or H2c)
- evidence-grounding validation complete (`§11`)

### Stage 3 — External benchmark + secondary conditions (≈8 weeks)

Run the external behavioral validation on LIFELONG-SOTOPIA if it is publicly runnable and supports custom memory-architecture agents. Otherwise run SOTOPIA-π-ME as the fallback. In both cases, run the external minimum condition set with a fixed base model, matched scenario chains, matched prompts, matched evaluators, and full seed budget; include `M2_memory_only` externally if budget permits. Secondary conditions (`M0_plus`, `M1_indexed`, `M2_typed`, `GraphMemory_generic`) run at reduced seeds on diagnostic only.

**Final framing decision** after Stage 3 based on which success tier (§15) is reached, with the additional H3 gate that external task success must not come at the cost of degraded BEL / BELEXT-adjusted BEL.

### Stage budget summary

| Stage | LLM calls (order-of-magnitude) | Annotation cost | Duration |
|---|---|---|---|
| 1 — pilot | ~5×10⁴ | ~$1.5k | 6 weeks |
| 2 — main diagnostic | ~5×10⁵ | ~$4k (scaling to 200 claims) | 10 weeks |
| 3 — external + secondary | ~5×10⁵ | ~$2k (incremental) | 8 weeks |

Order-of-magnitude only; refined after Stage 1 pilot measures actual per-condition cost.

---

## 18. `Schema_emergent` Protocol (concrete)

To remove hand-engineering bias, v4 specifies the emergent-schema procedure:

1. **Input set.** 200 episodic memories sampled uniformly from a **schema-development simulation** that is **separate from any evaluation run**. The schema-development simulation uses agents and scenarios disjoint from Phase-2 probes.
2. **Prompt.** A constrained prompt asks the LLM: "Propose 5–10 memory types that organize these social experiences. For each type, give: name, one-sentence definition, 2 example claims drawn from the input. Avoid types that overlap by more than 50% in scope." The prompt is fixed and released.
3. **Replication.** Run the prompt **5 times** with temperature 0.7 on the frontier model.
4. **Stability criterion.** A proposed type is **retained** if a semantically equivalent type appears in ≥ 3 of 5 runs (semantic equivalence judged by a separate LLM call with chain-of-thought, validated against 30 human labels at κ ≥ 0.6).
5. **Freeze.** Retained types form `Schema_emergent`. Schema is frozen before any Phase-2 evaluation. Type definitions are not re-edited after seeing evaluation data.
6. **Overlap analysis.** Compute Jaccard-style overlap between `Schema_emergent` and `Schema_7` on (a) type names, (b) example-claim assignment. Report regardless of whether overlap is high or low — both outcomes are informative.

If `Schema_emergent` converges near `Schema_7`, that **supports** the proposed schema. If it diverges and outperforms, the paper reframes around the emergent schema (downgrade rule in §16). If it diverges and underperforms, the proposed schema is mildly validated; we report the schema-design risk honestly.

---

## 19. SMGA vs Graph Memory: Operational Differences

The v3 review correctly noted that "planning-actionable interface" is too vague to distinguish SMGA from graph memory as architectures. v4 specifies the operational difference as a contract on memory objects:

| Contract | Generic graph memory | `GraphMemory_social_schema` (A-MEM-like) | SMGA |
|---|---|---|---|
| Typed nodes | optional | required (social types) | required (social types) |
| Edges with relation type | yes | yes | n/a (record-based; relations stored as `related_entities`) |
| **`supporting_evidence_ids`** — required field linking to episodic IDs | optional | optional | **required** |
| **`contradicting_evidence_ids`** — required field for negative evidence | usually absent | usually absent | **required** |
| **`validity_scope`** — time window + context list | absent | absent | **required** |
| **Controlled-vocabulary `planning_affordances`** with per-affordance evidence | absent | absent | **required** |
| Planner contract: must log `used_memory_ids`, `supporting_evidence_ids`, `negative_evidence_ids`, `rejected_memory_ids` | not specified | not specified | **required** |
| External provenance audit interface (gold-log checkable) | not standard | not standard | **required** |
| Update history with reason and contradiction-driven revisions | optional | optional | **required** |

The architectural claim is: **the bold rows are the testable difference**. `GraphMemory_social_schema` could in principle adopt them, but in current practice does not — so comparing SMGA against a *baseline* `GraphMemory_social_schema` measures whether these fields and contracts are load-bearing.

**Falsifiability:** If we add the bold contracts to `GraphMemory_social_schema` and it then matches `M3`, the paper reframes: *the contribution is the contract set, not the data structure.* The architecture claim is replaced by a "memory contract" claim. This contingency is in the downgrade rules.

---

## 20. Related Work (compressed)

**Generative Agents.** Direct foundation. GA contributes memory stream, reflection, planning. SMGA asks whether reflections should be typed, evidence-verified, planning-actionable objects, and evaluates this under behavior transfer.

**CoALA.** Provides a cognitive-architecture frame for language agents. SMGA is a concrete memory architecture and evaluation protocol consistent with that frame.

**Affordable Generative Agents (AGA).** AGA optimizes GA by reducing the cost of repeated agent-environment and inter-agent interactions through Lifestyle Policy and Social Memory. SMGA is orthogonal. It does not aim to reduce cost; it aims to improve the reliability with which social experience becomes evidence-grounded planning context. AGA compresses and reuses interaction patterns to preserve believability at lower token cost. SMGA verifies, scopes, and operationalizes social memories for long-horizon planning, with cost reported as a confound rather than a headline claim.

**MemoryBank, MemGPT.** Long-term storage, retrieval, forgetting. SMGA focuses on how social experiences become structured planning context, not on storage capacity.

**Reflexion, Voyager.** Verbal reflection and skill libraries for future-task improvement. SMGA differs by targeting social memories, entity grounding, evidence verification, and history-dependent social behavior.

**A-MEM, AriGraph, G-Memory, generic graph memory.** Closest competitors. SMGA does not claim novelty from links, evidence, or entity indexing in isolation. The incremental contribution is the field/contract set in §19 plus behavior-transfer evaluation under matched controls. The headline comparison is **SMGA vs `GraphMemory_social_schema`** — if SMGA loses it, the architecture claim is withdrawn.

**SOTOPIA, SOTOPIA-π, and LIFELONG-SOTOPIA.** Social interaction benchmarks. LIFELONG-SOTOPIA is the preferred external behavioral testbed when runnable, but SMGA uses it to compare memory architectures under a fixed base model rather than to rank base models. SOTOPIA-π-ME is retained as a fallback and controlled extension with gold prior-evidence annotations for SMGA-specific provenance and planning-trace evaluation.

---

## 21. Open Science Commitment

Released as part of this work:

- code (agent loop, memory architectures M0–M3, graph-memory baselines)
- diagnostic benchmark (event templates, scenarios, gold logs)
- LIFELONG-SOTOPIA adapter/evaluation scripts when runnable; SOTOPIA-π-ME fallback multi-episode extension when needed
- judge prompts and calibration data
- human annotation guidelines and the labeled validation set (200+ claims)
- per-condition planning traces (with PII review)
- analysis scripts and pre-registration of contrasts, SESOI, and fallback model

Under permissive license. Pre-registration submitted before Stage 2.

---

## 22. Remaining Risks

| Risk | Mitigation in v4.3 |
|---|---|
| `M0_prompted` matches `M3` | Partial-success tier (§15.1); reframe as "prompt is enough"; not catastrophic |
| `GraphMemory_social_schema` with §19 contracts matches `M3` | Reframe as "memory contract" contribution (§19 falsifiability) |
| Scale infeasible inside the staged budget | Stage gates in §17 stop the project before sunk cost grows |
| Human-LLM judge agreement low | LLM-judge metrics downgraded to exploratory (§11.3); recall metrics from gold logs remain |
| LIFELONG-SOTOPIA unavailable or incompatible with custom memory agents | Use and release SOTOPIA-π-ME fallback (§9.3) |
| Statistical model non-convergent | Pre-registered fallback chain (§13.3) |
| Memory-content sensitivity (`M3_actionable > M3_placebo`) fails | This is the **most informative** failure; Claim Family 2 is weakened; paper reframed as recall/abstraction or planning-rationale contribution (§15.1) |
| External GOAL improves while BEL / BELEXT-adjusted BEL drops | H3 withdrawn; result reframed as task optimization at the cost of social realism |
| `M2_memory_only` matches `M3_actionable` | planning-interface contract is not load-bearing; reframe around structured memory formation and retrieval |
| Reviewers confuse SMGA with AGA's Social Memory | §20 clarifies that AGA compresses social impressions for cost, while SMGA verifies and operationalizes social memories for planning |

---

## 23. Final Position

> A staged, controlled architecture-and-evaluation study of whether two SMGA modules — structured social memory formation and an evidence-grounded planning interface — improve long-horizon, history-dependent planning in GA-style agents beyond reflection, prompted reflection, extra reasoning budget, placebo interfaces, and graph memory with social schema.

The strongest version of the paper does not claim memory is solved. It identifies, with falsifiable contrasts and pre-registered downgrade rules, **when structured social memory matters, when prompted reflection is enough, and which fields of a memory object are load-bearing for behavior transfer**.

Core claim-family contrasts:

```text
Claim Family 1:
M3 > M0_prompted and M3 > GraphMemory_social_schema on evidence-grounded memory quality

Claim Family 2:
M3_actionable > M0_prompted and M3_actionable > M3_placebo on planning/behavior transfer

Claim Family 3:
M3 > strongest baseline on LIFELONG-SOTOPIA if runnable, otherwise SOTOPIA-π-ME,
with no BEL / BELEXT-adjusted BEL degradation
```

If only Claim Family 1 holds, the paper is a structured-memory representation and audit paper. If Claim Families 1 and 2 hold, it is a strong SMGA architecture paper. If all three claim families hold, the paper claims SOTA on history-dependent social memory under the evaluated benchmark and baseline set — and nothing broader.
