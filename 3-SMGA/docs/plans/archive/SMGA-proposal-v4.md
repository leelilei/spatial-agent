# SMGA Proposal v4

## Structured Memory for Generative Agents

> Working title: **Structured Memory for Generative Agents: Evidence-Grounded Social Context for Long-Horizon Planning**
> Short name: **SMGA**
> Version: **0.4**
> Date: **2026-05-19**
> Status: tightened-scope proposal after v3 review
> Relation to v3: trims secondary conditions and metrics by ~30%; commits to a specific external benchmark with a concrete fallback we will deliver ourselves; sharpens the operational difference between SMGA and graph-memory baselines; concretizes the `Schema_emergent` protocol; adds a staged execution plan; adds a *partial success* tier; adds open-science and IRB commitments.

---

## 0. One-Line Version

SMGA studies whether **GA-style memory stream plus reflection is sufficient for long-horizon, history-dependent social behavior**, and proposes a structured memory framework that converts episodic experiences and open-ended reflections into **typed, entity-grounded, evidence-verified, and planning-actionable social context**.

The central question:

> Beyond remembering and reflecting, can LLM generative agents maintain structured social memories about people, places, relationships, activities, routines, norms, and information states, and use those memories to improve future planning and behavior — under matched compute, prompt, schema, and memory-content controls?

---

## 1. What Changed in v4

v3 addressed every major v2 concern (novelty boundary, schema circularity, compute confound, situated-cognition framing, evidence-grounding reliability, causal attribution, external benchmark). v3 review identified six residual issues. v4 addresses each:

| Residual issue | v4 change |
|---|---|
| **R1 Scope feasibility** — 9 conditions × 4 schemas × ≥2 models × ≥50 seeds × 2 benchmarks is undeliverable | §8 tiers conditions into **Primary / Secondary / Exploratory**; §17 adds a **staged execution plan** with go/no-go gates |
| **R2 SMGA vs `GraphMemory_social_schema` looks like an evaluation difference, not an architectural one** | §19 adds an **operational difference table**: required fields, contracts, and interfaces that distinguish SMGA from graph memory beyond schema |
| **R3 `Schema_emergent` protocol is too thin** | §18 specifies the full emergent-schema procedure: input set, prompt, run count, stability criterion, freeze point, and overlap analysis with `Schema_7` |
| **R4 External benchmark commitment is still hedged** | §9 commits to **SOTOPIA-π** as primary, with a **multi-episode extension we will release** as the concrete fallback — no dependency on third-party publication |
| **R5 Engineering details missing (IRB, open-source, statistical fallback)** | §11.2 adds annotator IRB and compensation; §13 adds a simpler fallback mixed-effects model; §21 commits to releasing code, traces, benchmark, and judge prompts |
| **R6 No partial-success tier** | §15 adds **partial success**: specific reframings if 2/4 or 3/4 primary contrasts hold |

v4 also **cuts**: the standalone "Promise tracking" section (folded into metrics as secondary), the full paper-structure outline (compressed to one paragraph), redundant prose in §1–§3, and a separate "Response to Reviewers" section (the changes table above replaces it).

---

## 2. Core Claim

> GA-style reflection produces useful high-level thoughts, but open-ended reflection alone is not a reliable mechanism for converting social experience into evidence-grounded, reusable, planning-actionable memory. SMGA tests whether structured social memory objects improve history-dependent social planning and behavior beyond **prompted reflection** (cheap baseline), **budget-matched reasoning** (compute control), **placebo memory** (interface control), and **graph memory with social schema** (architecture control).

Explicitly **not** claimed:

```text
SMGA is a universal memory SOTA for all LLM agents.
SMGA proves human-like situated cognition.
SMGA replaces GA reflection.
SMGA wins because it simply calls the LLM more often.
```

---

## 3. Research Gap

### 3.1 What GA contributes

GA established a working architecture: `observation → memory stream → retrieval → reflection → planning → action`. SMGA builds on this; it does not dismiss it.

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

v4 trims from 6 to 5 RQs; the dropped RQ (cost/model dependence) becomes a reporting requirement rather than a primary question.

**RQ1 — Memory formation.** Does SMGA produce more accurate, evidence-supported structured social memories than GA reflection, prompted GA reflection, and graph memory with social schema?

**RQ2 — Schema contribution.** Does the proposed schema matter, or do coarse, emergent, or oracle schemas match it?

**RQ3 — Planning transfer.** Do structured social memories improve planning decisions beyond what recall and abstraction quality alone predict?

**RQ4 — Behavioral transfer.** Do agents using SMGA take better history-dependent actions, and is the change driven by *memory content* rather than interface or compute?

**RQ5 — External validity.** Does SMGA improve performance on an external history-dependent social benchmark, not only on a self-authored diagnostic?

---

## 6. Hypotheses

Each hypothesis has a **primary metric**, a **required contrast set** (must all hold), and a **smallest effect of interest (SESOI)**. If the observed effect is below SESOI, the hypothesis is treated as not supported even if statistically significant.

### H1 — Evidence-supported structured recall

- Primary metric: `evidence-supported structured recall F1`
- Required: `M3 > M0_prompted` and `M3 > M0_plus`
- SESOI: +0.08 absolute over `M0_prompted`

### H2 — Valid abstraction beyond prompted reflection

- Primary metric: `human-verified abstraction validity`
- Required: `M2 or M3 > M0_prompted` and `M2 or M3 > GraphMemory_social_schema`
- SESOI: +0.10 absolute over the stronger of the two baselines

### H3 — Evidence-supported planning

- Primary metric: `evidence-supported planning rate`
- Required: `M3 > M3_placebo` and `M3 > M0_prompted`
- SESOI: +0.10 absolute over `M0_prompted`

### H4 — Behavior change driven by memory content

- Primary metric: `target-consistent behavior rate`
- Required: `M3 > M3_placebo` and `M3 > M0_prompted`
- SESOI: +0.08 absolute over `M0_prompted`
- This is the strongest hypothesis. `M3 > M3_placebo` is the **memory-content sensitivity** test.

### H5 — External benchmark improvement

- Primary metric: `history-dependent social task success` on SOTOPIA-π multi-episode extension (see §9.1)
- Required: `M3 > strongest baseline`
- SESOI: +0.05 normalized score

---

## 7. Architecture

Four ablatable layers.

**L1 Episodic memory.** GA-compatible memory stream (event_id, text, time, actors, location, activity, topic, valence).

**L2 Entity indexing.** Each episodic memory is indexed by people, places, relationships, activities, routines, norms, information states. Indexing alone is not the main contribution — it is a required intermediate condition (`M1_indexed`).

**L3 Typed social abstraction.** Structured memory objects per §4 definition. v4 no longer presents one schema as canonical; the schema itself is an experimental variable (§8.2).

**L4 Planning-actionable memory.** Planning receives structured memory candidates with both supporting and contradicting evidence. Planner output must record `chosen_action`, `used_memory_ids`, `supporting_evidence_ids`, `negative_evidence_ids`, `rejected_memory_ids`, `rationale`, `outcome`. Affordances are drawn from a controlled vocabulary (§12).

---

## 8. Experimental Conditions (tiered)

v4 tiers conditions to make scope tractable. Primary conditions run with full seed budget on both benchmarks. Secondary conditions run only on diagnostic. Exploratory conditions run only at pilot scale.

### 8.1 Primary conditions (must run at full scale)

| Condition | Description | Purpose |
|---|---|---|
| `M0_GA` | GA-style memory + reflection | classic baseline |
| `M0_prompted` | GA reflection prompt explicitly asks about people / places / relationships / activities / routines / norms / information | cheap-prompt control |
| `M3_actionable` | full SMGA (L1+L2+L3+L4) | main treatment |
| `M3_placebo` | M3 interface with random/irrelevant memory content | memory-content control |
| `GraphMemory_social_schema` | graph memory with social schema, no SMGA planning interface | architecture control vs A-MEM-style |

**These 5 are the minimum publishable set.** Every primary hypothesis is decided by contrasts among these.

### 8.2 Secondary conditions (diagnostic only, reduced seeds)

| Condition | Purpose |
|---|---|
| `M0_plus` | reflection frequency / token budget / call count matched to M3 — compute control |
| `M1_indexed` | tests whether indexing alone explains gains |
| `M2_typed` | isolates typed abstraction from planning interface |
| `GraphMemory_generic` | graph structure without social schema |

### 8.3 Schema ablation (secondary)

| Schema | Description |
|---|---|
| `Schema_4` | coarse: person, place, relation, event |
| `Schema_7` | proposed: person, place, relationship, activity, routine, norm, information |
| `Schema_emergent` | LLM-proposed types from held-out logs, frozen before evaluation (§18) |
| `Schema_oracle` | human-designed after seeing task family — upper-bound only |

### 8.4 Held-out experience types

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

---

## 9. Benchmark Strategy

### 9.1 External benchmark — committed

**Primary external benchmark:** `SOTOPIA-π multi-episode extension` (SOTOPIA-π-ME).

If a public *Lifelong-SOTOPIA* benchmark exists at submission time and is broader, we use it. Otherwise SOTOPIA-π-ME is **a deliverable of this project**: we extend SOTOPIA-π scenarios into 3–5 paired episodes per scenario, with the second-and-later episodes requiring use of first-episode interaction history (commitments, relationships, conflicts, information ownership). We release the extension as part of this work.

This removes the v3 hedge: the external benchmark exists either way, because we ship it.

Eligible task subsets emphasize:

```text
remembering prior interactions
tracking promises and commitments
adapting to changed relationships
using prior conflict or cooperation
maintaining persona-consistent social history
```

### 9.2 Diagnostic benchmark

Self-authored, used for mechanism validation, schema ablation, placebo controls, provenance checking, and behavioral probes — **not** for headline SOTA claims.

Scale:

```text
agents: 6-10
locations/contexts: 6-10
simulation length: 3-5 days
seeds: minimum 50 for primary contrasts
phase 1 (controlled exposure) + phase 2 (planning/behavior probes)
```

Phase-1 safeguards: event templates generated before any model run; held-out types excluded from templates; distractor events included; same event log replayed across memory conditions for paired comparison.

---

## 10. Metrics (consolidated)

### 10.1 Recall and memory quality

`structured recall F1` · `unsupported memory claim rate` · `hallucinated provenance rate` · `contradiction awareness rate` · `calibration error`

### 10.2 Abstraction quality

`abstraction validity` (human-verified) · `overgeneralization rate` · `schema assignment accuracy` · `held-out type generalization`

### 10.3 Planning quality

`evidence-supported planning rate` · `negative-evidence use rate` · `memory-content sensitivity (M3 vs M3_placebo)` · `prompted-baseline gain (M3 vs M0_prompted)`

### 10.4 Behavior

`target-consistent behavior rate` · `history-dependent task success` · `relationship-consistency score` · `social coherence rating` (blinded, condition-hidden)

### 10.5 Cost (required reporting on every table)

`input/output tokens` · `LLM calls` · `wall-clock latency` · `cost-normalized success`

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

Every result table reports cost (tokens, calls, latency, storage) alongside raw performance, plus a cost-normalized column. Interpretation guide:

| Pattern | Interpretation |
|---|---|
| SMGA better and cost-normalized better | strong architecture result |
| SMGA better but cost-normalized worse | trade-off; useful when reliability/auditability matters |
| SMGA better than M0_GA but not M0_plus | gain is from extra reasoning, not structure |

---

## 15. Success Criteria

### 15.1 Partial success (new in v4)

If 2 of 4 primary contrasts (H1–H4) hold, the paper reframes around what *did* work:

| Pattern that holds | Reframing |
|---|---|
| H1 + H2 only | "structured memory as a high-fidelity, auditable representation of social experience" — recall/abstraction contribution, behavioral claim withdrawn |
| H2 + H3 only | "structured memory improves planning-rationale quality" — behavior claim withdrawn, useful for simulation and audit |
| H3 + H4 only | "structured memory affects behavior even when recall is comparable" — abstraction claim secondary |
| H4 alone with H1–H3 null | likely confound; result reframed as exploratory; main paper not submitted |

Partial success is publishable; partial+H5 is publishable as a strong paper.

### 15.2 Minimum success

H1 + H2 hold, both against `M0_prompted` and against `GraphMemory_social_schema`. Below this, the architecture claim is not supported.

### 15.3 Strong success

H1 + H2 + H3 + H4 hold against all required baselines.

### 15.4 SOTA-level success

Strong success **plus** H5 on the external benchmark **plus** cost reporting **plus** validated judge reliability.

Acceptable claim form: *SMGA achieves state-of-the-art performance on history-dependent social memory tasks under the evaluated benchmark and baseline set.* Anything broader is not claimed.

---

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
| External benchmark fails | diagnostic-only contribution; no SOTA claim |
| Only one model shows gains | model-specific result |
| Cost-normalized performance much worse | reliability/audit trade-off, not efficiency gain |

---

## 17. Staged Execution Plan

To address R1 (scope feasibility), the project executes in three stages with explicit go/no-go gates.

### Stage 1 — Pilot (≈6 weeks)

Run **5 primary conditions** × **5 seeds** × **frontier model only** on the diagnostic benchmark. Validate:

- annotation pipeline (κ ≥ 0.6 on 50 claims)
- planning-trace logging is complete and parseable
- `M3_placebo` is operationally distinct from `M3` (no information leakage from interface)
- pilot effect direction on H1 and H4

**Gate 1** — proceed to Stage 2 if:
- annotation κ ≥ 0.6
- `M3` shows directional improvement over `M0_GA` on at least one of H1, H4
- `M3_placebo` does **not** match `M3` on H4 (otherwise architecture is suspect even at pilot)

If gate 1 fails, return to design iteration; do not scale.

### Stage 2 — Main diagnostic (≈10 weeks)

5 primary conditions × **50 seeds** × **2 models** (frontier + open-weight) on diagnostic. Schema ablations (`Schema_4`, `Schema_7`, `Schema_emergent`) at 25 seeds each on the frontier model only.

**Gate 2** — proceed to Stage 3 if:
- at least 2 of the 4 primary contrasts (H1–H4) hold against `M0_prompted` with SESOI met
- evidence-grounding validation complete (`§11`)

### Stage 3 — External benchmark + secondary conditions (≈8 weeks)

SOTOPIA-π-ME on the 5 primary conditions, frontier model, full seed budget. Secondary conditions (`M0_plus`, `M1_indexed`, `M2_typed`, `GraphMemory_generic`) at reduced seeds on diagnostic only.

**Final framing decision** after Stage 3 based on which success tier (§15) is reached.

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

**MemoryBank, MemGPT.** Long-term storage, retrieval, forgetting. SMGA focuses on how social experiences become structured planning context, not on storage capacity.

**Reflexion, Voyager.** Verbal reflection and skill libraries for future-task improvement. SMGA differs by targeting social memories, entity grounding, evidence verification, and history-dependent social behavior.

**A-MEM, AriGraph, G-Memory, generic graph memory.** Closest competitors. SMGA does not claim novelty from links, evidence, or entity indexing in isolation. The incremental contribution is the field/contract set in §19 plus behavior-transfer evaluation under matched controls. The headline comparison is **SMGA vs `GraphMemory_social_schema`** — if SMGA loses it, the architecture claim is withdrawn.

**SOTOPIA, SOTOPIA-π.** Social interaction benchmarks. SMGA extends to multi-episode (SOTOPIA-π-ME) for history-dependent evaluation and releases the extension.

---

## 21. Open Science Commitment

Released as part of this work:

- code (agent loop, memory architectures M0–M3, graph-memory baselines)
- diagnostic benchmark (event templates, scenarios, gold logs)
- SOTOPIA-π-ME multi-episode extension
- judge prompts and calibration data
- human annotation guidelines and the labeled validation set (200+ claims)
- per-condition planning traces (with PII review)
- analysis scripts and pre-registration of contrasts, SESOI, and fallback model

Under permissive license. Pre-registration submitted before Stage 2.

---

## 22. Remaining Risks

| Risk | Mitigation in v4 |
|---|---|
| `M0_prompted` matches `M3` | Partial-success tier (§15.1); reframe as "prompt is enough"; not catastrophic |
| `GraphMemory_social_schema` with §19 contracts matches `M3` | Reframe as "memory contract" contribution (§19 falsifiability) |
| Scale infeasible inside the staged budget | Stage gates in §17 stop the project before sunk cost grows |
| Human-LLM judge agreement low | LLM-judge metrics downgraded to exploratory (§11.3); recall metrics from gold logs remain |
| External benchmark unavailable | We ship SOTOPIA-π-ME ourselves (§9.1) |
| Statistical model non-convergent | Pre-registered fallback chain (§13.3) |
| Memory-content sensitivity (`M3 > M3_placebo`) fails | This is the **most informative** failure; H4 withdrawn; paper reframed as recall/abstraction contribution (§15.1) |

---

## 23. Final Position

> A staged, controlled architecture-and-evaluation study of whether structured, evidence-verified social memory improves long-horizon, history-dependent planning in GA-style agents — beyond reflection, prompted reflection, extra reasoning budget, placebo interfaces, and graph memory with social schema.

The strongest version of the paper does not claim memory is solved. It identifies, with falsifiable contrasts and pre-registered downgrade rules, **when structured social memory matters, when prompted reflection is enough, and which fields of a memory object are load-bearing for behavior transfer**.

Primary make-or-break contrasts:

```text
M3 > M0_prompted        — architecture vs cheap prompt
M3 > M3_placebo         — memory content vs interface
M3 > GraphMemory_social_schema   — SMGA contracts vs graph memory
M3 > strongest baseline on SOTOPIA-π-ME   — external validity
```

If 2 of 4 hold with SESOI, the paper is publishable under the partial-success framing. If all 4 hold, the paper claims SOTA on history-dependent social memory under the evaluated benchmark and baseline set — and nothing broader.
