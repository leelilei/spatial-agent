# SMGA Proposal v4.6

> 版本：v4.6 ｜ 更新：2026-06-14 ｜ 状态：active
> 历史版本见 docs/plans/archive/。

## Structured Memory for Generative Agents

> Working title: **Structured Memory for Generative Agents: Evidence-Grounded Social Context for Long-Horizon Planning**
> Short name: **SMGA**
> Version: **0.4.6**
> Date: **2026-06-10**
> Status: implementation-oriented execution plan, hardened after v4.5-lite review
> Relation to v4.5-lite: keeps the lite scope (one causal chain, one diagnostic benchmark, one model, five main conditions), but fixes the logical holes the lite cut introduced: format-coupled metrics, a behavior success criterion that never required beating a real baseline, the dropped compute control, the "optional critical" graph baseline contradiction, and several underspecified benchmark requirements.
> Relation to v4.4: v4.4 remains the full research blueprint. Everything demoted there stays demoted unless explicitly restored here.

---

## 0. One-Line Version

SMGA studies whether long-horizon GA-style agents benefit from an explicit **social-memory-to-planning contract**: structured social memories that are typed, entity-grounded, evidence-supported, contradiction-aware, validity-scoped, and exposed to planning through auditable affordances.

The first-paper question is:

> Under matched model, prompt, interface, candidate-set, and scenario controls, does SMGA improve **format-neutrally measured** memory quality, history-grounded planning, and history-dependent probe behavior beyond GA reflection, prompted reflection, representation-only memory, compute-matched reflection, and placebo memory?

---

## 1. What Changed in v4.6

v4.5-lite focused the project correctly but cut conditions without retightening the claims and metrics that depended on them. v4.6 keeps the lite scope and repairs the following:

| # | v4.5-lite problem | v4.6 fix |
|---|---|---|
| 1 | Two of three headline metrics were defined by the treatment's output format: baselines without evidence-ID fields lose by construction | New **format-neutral claim-level evaluation protocol** (§8). All conditions are graded on extracted atomic claims against the gold log. Trace-field metrics are demoted to descriptive auditability reporting, not headline contrasts |
| 2 | Behavior success only required beating `M3_placebo` — SMGA could lose to plain GA on behavior and still claim "strong success" | New primary contrast `C4: M3 > M0_prompted` on history-dependent probe success. Strong success requires beating a real baseline on behavior, not just the placebo (§9.3, §13) |
| 3 | `M0_plus` (compute-matched control) dropped entirely; cost reporting alone does not control the compute confound | `M0_plus` restored as a **required secondary condition** at reduced seeds (§6.2). Downgrade rule restored |
| 4 | `GraphMemory_social_schema` labeled "optional critical baseline" — an oxymoron, and inconsistent with v4.4 calling it the headline comparison | Resolved by tying the claim to the condition: Stage 2b is **required for any architecture claim**. If Stage 2b is not run, the paper's claim automatically narrows to a memory-contract + evaluation-protocol contribution and makes no architecture-vs-graph-memory statement (§6.2, §13) |
| 5 | Ambiguity between "2–3 day simulation" and "same scripted event log replayed" | Pinned: **Phase 1 is scripted replay** from template-generated logs. No live Phase-1 simulation. The behavioral claim is correspondingly narrowed to *history-dependent responses to probes* (§7.1) |
| 6 | `contradiction awareness rate` had no denominator: no planted contradictions in the benchmark spec | Benchmark must include **planted contradiction events with gold labels** (§7.3) |
| 7 | `M3 vs M2` conflated memory selection with the planning contract | **Matched-candidate rule**: M2 and M3 receive the identical top-k memory candidate set per probe; only presentation and planner contract differ (§6.3) |
| 8 | Behavior probes had no specified scoring mechanism after BEL machinery was cut | Every Phase-2 probe ships with a **pre-registered, machine-checkable success condition** authored at benchmark construction time (§7.4) |
| 9 | "Social coherence gate" was a bare noun | Defined: blinded, condition-hidden coherence rating on a stratified sample with a pre-registered non-inferiority margin (§9.4) |
| 10 | SESOI dropped; "30–50 seeds" had no basis; "seed" undefined | SESOI restored per contrast (§9); **seed** defined as an instantiated scenario package (§11.1) |
| 11 | If human–LLM agreement failed, both non-behavior headline metrics collapsed with no contingency | Evidence checking split into a **mechanical layer** (fully automatic against gold log) and a **semantic layer** (judge, human-validated). κ failure degrades only the semantic layer (§10) |
| 12 | No timeline, budget, or pre-registration in an "execution plan" | Restored at lite scale (§12, §15) |

Smaller pinned decisions: placebo variant fixed to **stale** (§6.4); `confidence` field demoted to exploratory (§3); model version pinned before Stage 1 (§12); downgrade table cleaned of rows referring to conditions not in scope (§14).

---

## 2. Core Claim

SMGA addresses a **memory-reliability bottleneck** in long-horizon generative agents: past social experience must be converted into auditable, contradiction-aware, planning-actionable context before it can reliably guide future behavior.

The claim is not that GA lacks memory. GA already has memory streams, retrieval, reflection, and planning. The claim is narrower:

> Standard GA-style reflection does not require social memories to be typed, entity-grounded, evidence-checkable, contradiction-aware, validity-scoped, or exposed to the planner through explicit affordances and traces.

SMGA tests whether adding that contract improves:

1. memory quality, measured format-neutrally at the claim level,
2. history-grounded planning, measured format-neutrally against gold required evidence,
3. history-dependent probe behavior, measured against pre-registered success conditions.

Because Phase-1 exposure is scripted replay (§7.1), the behavioral claim is explicitly scoped:

> SMGA improves **history-dependent responses to planning and behavior probes**, not the agent's ongoing simulated social life. Effects on live multi-agent social dynamics are future work.

Explicitly not claimed in the first paper:

```text
SMGA is a universal memory SOTA.
SMGA beats every graph-memory system. (claimed only if Stage 2b runs and wins)
SMGA proves an optimal social-memory schema.
SMGA reduces cost.
SMGA requires a new external benchmark.
SMGA generalizes across model families before replication.
SMGA improves emergent social dynamics in live simulation.

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
**`confidence` is exploratory in the first paper.** Calibration was cut with v4.5-lite, and an uncalibrated self-reported confidence carries no evidential weight. The field is logged and analyzed descriptively; no headline metric or success criterion uses it.
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
- L3 typed abstraction: structured social memory objects with evidence, contradictions, validity scope.
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

Controlled planning affordances (frozen vocabulary):
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
**Role of the trace in evaluation.** The planning trace is SMGA's *auditability capability*: it is reported descriptively (trace completeness, provenance validity). It is **not** used as a headline contrastive metric against conditions whose interface does not produce traces — that comparison would be true by construction (§8).
---
## 5. Research Questions
**RQ1 — Memory quality.** Does SMGA produce social memories whose extracted claims are more grounded in actual experience (higher claim-level precision and recall against the gold log) than GA reflection and prompted reflection?
**RQ2 — Planning use.** Does the SMGA planning interface cause plans to be grounded in the *required* prior history, beyond representation-only memory with an identical candidate set?
**RQ3 — Behavioral transfer.** Does SMGA improve history-dependent probe behavior over real baselines, and is the improvement driven by memory content rather than interface format **or extra compute**?
External benchmark validity and schema optimality are not first-paper research questions.
---
## 6. Experimental Conditions
### 6.1 Main conditions (full seeds, Stage 2)
| Condition | Description | Purpose |
|---|---|---|
| `M0_GA` | GA-style memory stream + retrieval + reflection | Classic baseline |
| `M0_prompted` | GA reflection prompt explicitly asks about people, places, relationships, activities, routines, norms, and information states | Strong cheap-prompt control |
| `M2_memory_only` | SMGA structured memory is formed, but planning receives it only as ordinary retrieved context without the SMGA planning contract | Representation-only ablation |
| `M3_placebo` | SMGA planning interface enabled; memory content replaced by **stale** memories (see §6.4) under matched format | Interface/placebo control |
| `M3_actionable` | Full SMGA: structured memory formation + evidence-grounded planning interface | Main treatment |
Primary contrasts (Holm-corrected as a family, §11):
```text
C1: M3_actionable > M0_prompted on grounded memory F1 (prompt control)
C2: M3_actionable > M2_memory_only on history-grounded planning (planning-interface test)
C3: M3_actionable > M3_placebo on probe behavior success (memory-content test)
C4: M3_actionable > M0_prompted on probe behavior success (real-baseline behavior test)

```

C4 is the repair for the v4.5-lite hole: beating a placebo fed stale content is necessary for the mechanism story but not sufficient for a behavioral claim. The behavioral claim requires beating a real baseline.
### 6.2 Required secondary conditions (reduced seeds, Stage 2b)
| Condition | Seeds | Purpose | Claim it gates |
|---|---|---|---|
| `M0_plus` | 15 | GA reflection with token/call budget matched to `M3_actionable` | If `M0_plus` matches `M3`, gains are extra reasoning budget, not structure. Without this condition, the compute confound is only *reported*, not *controlled* — so it is required, at reduced scale |
| `GraphMemory_social_schema` | 15 | Graph memory with social node/edge types, without SMGA evidence/contradiction/scope/affordance/trace contracts | **Gates the architecture claim.** If this condition is not completed, the paper claims a memory-contract + evaluation-protocol contribution and makes no architecture-vs-graph-memory statement. There is no "optional critical" middle ground |
Secondary contrasts (reported with CIs, not part of the primary Holm family):
```text
S1: M3_actionable vs M0_plus on all three headline metrics
S2: M3_actionable vs GraphMemory_social_schema on all three headline metrics

```

### 6.3 Matched-candidate rule for M2 vs M3
To isolate the planning contract from memory selection effects:
- For each probe, a shared retrieval step produces one top-k structured-memory candidate set.
- `M2_memory_only` receives the candidate set serialized as ordinary context.
- `M3_actionable` receives the identical candidate set through the SMGA planning interface.
- Affordance-based filtering or re-ranking inside M3 may *annotate* but must not *expand* the candidate set.
Any difference between M2 and M3 is then attributable to the contract and presentation, not to which memories were available.
### 6.4 Placebo specification
The placebo variant is pinned to **stale**: structured memory objects formed from an earlier, superseded portion of the scripted log (before relationship changes, promise updates, or contradiction events), with timestamps and format matched to `M3_actionable`. Stale is chosen over random/irrelevant because it is the least strawman-like: the placebo remains topically plausible and format-identical, so the M3-vs-placebo gap measures *content currency*, not garbage detection.
Pilot must verify the placebo does not leak current content (§12, Stage 1 checks).
---
## 7. Diagnostic Benchmark
### 7.1 Pinned design decision: scripted replay, no live Phase-1 simulation
Phase 1 (social exposure) is **fully scripted**: event logs are generated from templates before any model run and replayed identically to every condition as an observation stream. Agents do not act during Phase 1; they only form memory. Phase 2 presents history-dependent planning/behavior probes.
Consequences accepted and stated in the paper:
- Memory formation across conditions operates on byte-identical inputs — maximal control, clean pairing.
- SMGA's effect on *ongoing* social life is not tested; the behavioral claim is about probe responses (§2).
- No GA simulation environment is needed; the engineering surface shrinks to: log generator, memory modules, planner harness, probe runner, scorers.
### 7.2 Scale
```text
agents per scenario: 6-8
contexts / locations: 4-6
scripted exposure horizon: equivalent of 2-3 simulated days
seeds: 40 for the main experiment (paired across all 5 main conditions)
model: one strong instruction-following frontier model, version pinned before Stage 1

```

### 7.3 Gold structure requirements
Each generated scenario package must contain, before any model run:
1. **Gold event log** — the scripted Phase-1 events with entities, time, location, topic.
2. **Gold social facts** — the template-derived list of true social facts (relationships, promises, secrets, norms, reputations, information ownership) that a perfect memory system should capture. This is the recall denominator for §8.
3. **Planted contradiction events** — for a pre-registered fraction of gold facts (target: ≥ 25%), the log contains a later event that revises or contradicts the earlier fact, with gold labels linking the pair. This is the denominator for contradiction-awareness metrics.
4. **Distractor events** — socially plausible events irrelevant to any probe.
5. **No-history solvability flag** — each probe is labeled for whether it can be solved without Phase-1 history; flagged probes are excluded from headline behavior metrics.
### 7.4 Probe requirements
Every Phase-2 probe ships with:
```text
probe_id
required_prior_evidence_ids (gold: which Phase-1 events the correct response depends on)
required_fact_ids (gold: which gold social facts must be used)
success_condition (machine-checkable predicate over the agent's response:
chosen affordance ∈ acceptable set, target entity correct,
commitment honored / secret kept / repair attempted, etc.)
failure_condition (explicit wrong behaviors, including outdated-fact use)
no_history_solvability_flag

```

Success conditions are authored at benchmark construction time and **locked before any model run**. Behavior scoring is therefore mechanical for the headline metric; LLM judges are not load-bearing for §9.3.
### 7.5 Held-out social patterns (hardened)
The following patterns are **withheld from all schema examples, few-shot prompts, and module-development materials**, pre-registered and locked before Stage 1:
```text
failed promise
shared secret
norm violation
repair after conflict
indirect reputation
relationship change

```

At least two held-out patterns appear in every seed's Phase-2 probe set. "Not overused" (v4.5-lite wording) is replaced by full withholding: method development may not touch these patterns at all.
---
## 8. Format-Neutral Evaluation Protocol
This section is the core methodological addition of v4.6. The principle:
> **No headline metric may be computable only from the treatment's output format.** Every condition is graded on what it *knows* and *uses*, not on whether it emits SMGA fields.
### 8.1 Claim extraction (all conditions)
For each condition and seed, collect the memory artifacts at the end of Phase 1:
- `M0_GA`, `M0_prompted`, `M0_plus`: reflection texts.
- `M2`, `M3`, placebo, graph memory: structured objects (their `claim` fields and serializations).
A fixed, condition-blind extractor (one frozen LLM prompt, identical across conditions) decomposes each artifact into **atomic social claims** of the form (subject entities, predicate, scope). The extractor is validated once on a 50-artifact pilot against human extraction (coverage and fidelity), then frozen.
### 8.2 Two-layer grading
Each atomic claim is graded against the gold structures of §7.3 in two layers:
**Mechanical layer (fully automatic, no judge):**
```text
entity existence — do the referenced entities exist in the gold log?
event existence — do any cited / linked evidence IDs exist?
participant match — do cited events involve the claimed entities?
currency check — does the claim contradict a planted later revision? (gold pair lookup)

```

**Semantic layer (LLM judge, human-validated per §10):**
```text
support — does the gold log actually support the claim?
match-to-gold-fact — does the claim correspond to a gold social fact (for recall)?

```

### 8.3 Headline metric definitions
**Grounded memory F1 (RQ1, contrast C1).**
Precision = fraction of extracted claims passing mechanical checks *and* judged supported by the log. Recall = fraction of gold social facts matched by at least one supported claim. F1 combines them. Computable identically for free-text reflection and structured objects.
**Contradiction awareness rate (RQ1, secondary).**
Among gold facts with planted contradictions, the fraction for which the condition's final memory state reflects the revision (mechanical currency check on extracted claims). Free-text conditions are graded on whether their reflections state the revised fact.
**History-grounded planning rate (RQ2, contrast C2).**
For each probe, a condition-blind judge grades whether the plan's rationale and chosen action correctly reflect the probe's `required_fact_ids` — regardless of whether the plan cites IDs. A plan that uses the right history in prose scores; a plan that emits IDs but uses outdated facts does not. This makes M2 (no trace contract) gradable on equal terms with M3.
**History-dependent probe success (RQ3, contrasts C3 and C4).**
Mechanical evaluation of `success_condition` / `failure_condition` per §7.4. No judge in the loop.
### 8.4 SMGA-specific auditability metrics (descriptive only)
Reported for SMGA conditions, never as a baseline contrast:
```text
trace completeness rate — planner traces with all required fields
provenance validity rate — cited evidence IDs that pass mechanical + semantic checks
hallucinated provenance rate — cited IDs that fail existence or support
biased evidence use rate — plans citing support while a gold contradiction was in the candidate set

```

These quantify the auditability *capability* the contract buys; they do not feed success criteria.
---
## 9. Metrics and SESOI
### 9.1 Headline metric 1 — Grounded memory F1
- Contrast: `M3_actionable > M0_prompted` (C1)
- **SESOI: +0.08 absolute F1.** Below SESOI, the sub-test is not supported even if statistically significant.
### 9.2 Headline metric 2 — History-grounded planning rate
- Contrast: `M3_actionable > M2_memory_only` (C2), under the matched-candidate rule (§6.3)
- **SESOI: +0.10 absolute.**
### 9.3 Headline metric 3 — History-dependent probe success
- Contrasts: `M3_actionable > M3_placebo` (C3) **and** `M3_actionable > M0_prompted` (C4)
- **SESOI: +0.08 absolute each.**
- The behavioral claim requires **both**: C3 establishes memory-content sensitivity; C4 establishes improvement over a real baseline. C3 alone is reported as a mechanism result, not a behavioral improvement.
### 9.4 Social-coherence gate (defined)
Failure mode to prevent: an agent with explicit memory objects wins probes by behaving like a database query bot ("according to evidence chat_018...") — task-successful but socially unnatural.
Procedure:
```text
sample: 200 probe responses, stratified across {M0_prompted, M2, M3_placebo, M3} and probe types
raters: 2, blinded to condition, randomized order
scale: 1-5 social coherence (naturalness, persona consistency, no internal-machinery leakage)
gate: mean(M3) >= mean(M0_prompted) - 0.25 (non-inferiority margin, pre-registered)

```

If the gate fails, behavioral success (C3/C4) cannot be claimed regardless of probe-success numbers; the result is reframed as task optimization at the cost of social naturalness.
### 9.5 Secondary metrics
```text
contradiction awareness rate (format-neutral, §8.3)
overgeneralization rate (claims whose scope exceeds gold support)
relationship-consistency score
auditability metrics (§8.4, SMGA-descriptive)
input/output tokens · LLM calls · wall-clock latency · storage footprint

```

Cost is reported in every main table. It is a confound check; with `M0_plus` restored, it is also *controlled* (S1), not merely reported.
---
## 10. Evidence Validation and Annotation
### 10.1 Division of labor
The mechanical layer (§8.2) needs no annotation: existence, participant, and currency checks run against gold structures. Only the **semantic layer** (support, match-to-gold-fact, history-grounded planning judgment) uses an LLM judge, and the judge must be human-validated before scaling.
### 10.2 Annotation plan
```text
sample: 150-200 semantic judgments, stratified across conditions, claim types, and probe types
annotators: 2 independent, blinded to condition
labels: supports / contradicts / irrelevant / insufficient (claims)
grounded / partially grounded / ungrounded (planning judgments)
pilot agreement target: Cohen's kappa >= 0.6 on 50 items before scaling
judge gate: human-LLM kappa >= 0.6 on the pilot; below 0.5 the judge is exploratory

```

### 10.3 Contingency if the judge fails validation
Because the metrics are layered, judge failure is no longer fatal:
| Surviving evidence | Resulting claim |
|---|---|
| Mechanical layer only (precision drops semantic support; recall unavailable) | grounded-claim *plausibility* + contradiction currency + behavior; memory-quality claim weakened to mechanical grounding |
| Behavior metrics (always mechanical) | behavioral result stands on C3/C4 regardless of judge status |
This replaces the v4.5-lite situation where κ failure silently destroyed two of three headline metrics.
---
## 11. Statistical Analysis
### 11.1 Unit of analysis: seed defined
A **seed** is one instantiated scenario package:
```text
(a) event-log instance generated from templates with seed-specific entity bindings,
event orderings, distractors, and planted contradictions
(b) the probe set derived from that instance, with locked success conditions
(c) a fixed decoding seed for all model calls in that package

```

All conditions run on identical packages (paired design). Seeds differ in (a)-(c), so cross-seed variation is real scenario + sampling variation, not decoding noise alone.
### 11.2 Primary analysis
```text
paired condition differences by seed on each headline metric
bootstrap confidence intervals (seed-level resampling, 10k draws)
Holm correction across the four primary contrasts C1-C4
SESOI applied after significance: an effect below SESOI is "not supported"

```

### 11.3 Secondary robustness
```text
mixed-effects model: outcome ~ condition + probe_type + (1 | seed) + (1 | agent)

```

Convergence fallback (pre-registered, chosen on diagnostics not effect size): drop `(1 | agent)` → cluster-robust SEs at seed level. The paper's interpretability must not depend on the mixed model.
### 11.4 Power note
With 40 paired seeds and rate-type outcomes aggregated per seed, a paired design detects ~0.08–0.10 absolute differences at conventional power if seed-level SD ≤ ~0.15. Stage 1 measures actual seed-level variance; if it is materially higher, the Stage 2 seed budget rises to 50 before launch (decided at Gate 1, pre-registered).
---
## 12. Staged Execution Plan
Model and decoding settings are pinned (provider, exact model version string, temperature) before Stage 1 and held fixed through Stage 2b.
### Stage 1 — Pilot (~4 weeks)
Run:
```text
4 conditions × 5 seeds: M0_GA, M0_prompted, M3_placebo, M3_actionable

```

Validate:
- log generator produces gold facts, planted contradictions, and locked success conditions correctly,
- memory and planning traces complete and parseable,
- claim extractor passes the 50-artifact human pilot,
- placebo does not leak current content (manual audit of 20 placebo memory sets),
- annotation pilot reaches κ ≥ 0.6; judge reaches human-LLM κ ≥ 0.6,
- `M3_actionable` shows directional improvement on ≥ 1 memory metric and ≥ 1 planning/behavior metric,
- seed-level variance measured for the §11.4 power decision.
**Gate 1:** all of the above, else revise before scaling.
### Stage 2 — Main experiment (~8 weeks)
```text
5 conditions × 40 seeds (50 if Gate 1 variance check requires)
M0_GA, M0_prompted, M2_memory_only, M3_placebo, M3_actionable

```

This produces the main paper table: C1–C4 with Holm correction and SESOI.
### Stage 2b — Required secondary conditions (~3 weeks, overlaps Stage 2 tail)
```text
M0_plus × 15 seeds
GraphMemory_social_schema × 15 seeds

```

`M0_plus` is unconditionally required (compute control). `GraphMemory_social_schema` gates the architecture claim per §6.2: not completed → claim narrows, stated in the paper.
### Stage 3 — Optional (only if Stages 1–2b leave budget)
One of:
```text
second-model reduced replication (5 conditions × 15 seeds)
external benchmark sanity check (LIFELONG-SOTOPIA adapter, if runnable)

```

Neither is required for first-paper success.
### Budget (order of magnitude, refined after Stage 1)
| Stage | LLM calls | Annotation | Duration |
|---|---|---|---|
| 1 — pilot | ~3×10⁴ | ~$1k | 4 weeks |
| 2 — main | ~2×10⁵ | ~$1.5k | 8 weeks |
| 2b — secondary | ~6×10⁴ | — | 3 weeks (overlapping) |
| analysis + writing | — | — | 4 weeks |
Total: ~4.5–5 months to submission, excluding Stage 3.
---
## 13. Success Criteria
### Minimum Success
```text
C1 holds (grounded memory F1, M3 > M0_prompted, ≥ SESOI)
and at least one of:
C2 holds (planning use)
C3 and C4 both hold (behavior, with coherence gate passed)

```

Interpretation:
> SMGA measurably improves the grounding of social memory under format-neutral evaluation, and there is evidence that this memory enters planning or behavior.
Note the behavior arm of minimum success requires C3 **and** C4: placebo-only behavior wins do not count toward any success tier.
### Strong Success
```text
C1, C2, C3, C4 all hold at SESOI, coherence gate passed,
and S1 (M0_plus) does not erase the M3 advantage

```

Interpretation:
> SMGA improves memory grounding, makes memory more usable for planning under matched candidates, and improves history-dependent probe behavior over both placebo and a real prompted baseline — and the gains are not explained by extra compute.
### Expanded Success
Strong success plus at least one of:
```text
S2: M3 > GraphMemory_social_schema on ≥ 2 headline metrics → architecture claim permitted
second-model replication (Stage 3) → generality claim strengthened
external benchmark improvement without coherence degradation → external validity noted

```

---
## 14. Downgrade Rules
| Result | Downgrade |
|---|---|
| `M0_prompted` matches `M3` on C1 | contribution is prompt-level guidance, not architecture |
| `M0_plus` matches `M3` on headline metrics | gains are extra reasoning budget, not structure; structure claim withdrawn |
| `M2_memory_only` matches `M3` on C2 | planning contract not load-bearing; reframe around structured memory formation |
| `M3_placebo` matches `M3` on C3 | behavior change is interface effect; behavioral claim withdrawn |
| C3 holds but C4 fails | mechanism shown but no improvement over real baselines; behavior framed as sensitivity analysis only |
| Coherence gate fails | behavioral success not claimable; reframed as task optimization at the cost of social naturalness |
| Memory improves but planning and behavior do not | grounding/auditability contribution only |
| Planning improves but behavior does not | planning-rationale / interpretability contribution only |
| Semantic judge fails validation (κ < 0.5) | semantic-layer metrics exploratory; claims rest on mechanical layer + behavior (§10.3) |
| `GraphMemory_social_schema` matches `M3` | architecture claim withdrawn; contribution reframed as memory contract + evaluation protocol |
| Stage 2b graph baseline not completed | no architecture-vs-graph statement appears in the paper, in either direction |
---
## 15. Pre-Registration and Release
Locked **before Stage 2 launch** (after Gate 1, before any main-experiment model call):
```text
probe sets and success/failure conditions for all Stage-2 seeds
held-out pattern list and withholding attestation
primary contrasts C1-C4, SESOI values, Holm family
coherence-gate margin
placebo construction procedure
claim-extractor prompt and judge prompts (frozen)
analysis scripts (paired bootstrap + mixed-model fallback chain)
seed budget decision rule (40 vs 50)

```

Released with the paper:
```text
log/probe generator and all scenario templates
gold structures (facts, contradiction pairs, success conditions)
memory architectures M0-M3 and the placebo/graph baselines
extractor and judge prompts, human annotation guidelines, labeled validation set
per-condition planning traces and analysis scripts

```

---
## 16. Out of Scope for the First Paper
Unchanged from v4.5-lite, with two restorations noted:
```text
RESTORED in v4.6: M0_plus (required secondary — compute control)
RESTORED in v4.6: GraphMemory_social_schema (required for the architecture claim; Stage 2b)

Still demoted:
M1_indexed
GraphMemory_generic
Schema_4 / Schema_emergent / Schema_oracle ablations
field-by-field contract ablations
1000-claim calibration and calibrated-confidence headline metrics
mandatory two-model main experiment
mandatory LIFELONG-SOTOPIA / SOTOPIA-pi-ME validation
SOTA-level external benchmark claims
live-simulation social-dynamics claims

```

These remain valid future work or appendix diagnostics per the v4.4 blueprint.
---
## 17. Final Position
v4.6 positions the first SMGA paper as a **method and mechanism paper with a defensible evaluation protocol**:
> Structured, evidence-grounded social memory can make past social experience more reliable as planning context for long-horizon generative agents — measured format-neutrally, controlled for prompt, interface, candidate set, and compute, and gated on social naturalness.
The lite philosophy stands: one causal chain, one diagnostic benchmark, one pinned model, a small condition set. What v4.6 adds is the discipline the cuts had silently removed — every remaining claim is now backed by a contrast that can actually falsify it:
```text
prompt is enough? → C1 vs M0_prompted
just more compute? → S1 vs M0_plus
just the interface format? → C3 vs M3_placebo
just better serialization? → C2 vs M2 under matched candidates
better than real GA? → C4 vs M0_prompted on behavior
graph memory suffices? → S2, or the architecture claim is not made
unnatural task-bot? → coherence gate
metric rigged for SMGA? → format-neutral claim-level protocol

```

If the chain holds, the paper claims exactly that chain — and nothing broader.
