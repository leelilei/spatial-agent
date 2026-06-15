# Experiment Design: Does Structure Help At Memory Scale?

> Date: 2026-06-15
> Motivation: the `M2_aff_text` ablation showed M3 ~ M2_aff at ~10 memories — i.e.
>   structured FORMAT adds nothing when there are few memories read in one shot.
>   But structure's real job is selection/retrieval/currency-resolution AT SCALE.
>   We were testing the wrong regime. This experiment tests structure where it
>   should earn its keep: many memories.
> Status: DESIGN + minimal 10-seed pilot.

## The Question

A long-lived agent accumulates many social memories. When the memory store is
large, does structured memory (typed, currency-tagged, retrievable) beat the same
content as a flat prose dump — on accuracy, on cost, or both?

This separates two effects that the 10-memory test could not:

```text
- FORMAT at scale:    structured vs prose, both dumping ALL memories.
- SELECTION at scale: structure lets you retrieve only the relevant memories;
                      flat prose must dump everything. This is structure's real job
                      and maps directly to the "what enters context" thesis.
```

## Conditions (memory store inflated to N memories per seed)

```text
M2_aff_scale  : flat prose, ALL N memories (real probe-relevant + distractors).
                This is the flat-memory stress condition.
M3_dump_scale : structured objects, ALL N memories. Isolates FORMAT at scale.
M3_retr_scale : structured + deterministic top-k retrieval (keep the memories whose
                subject_entities overlap the probe's target/acting entities), send
                only those. Isolates SELECTION that structure enables.
```

Reference points already measured (small store, ~10 memories):
`M2_memory_only` (facts only), `M2_aff_text` (facts+affordances prose),
`M3_actionable` (facts+affordances structured) — all ~39/40, format-neutral.

## Memory Inflation (the scale knob)

Pad each seed's real memory artifact with K synthetic **distractor memories** about
non-probed entities (other people, other commitments/routines/norms), each with a
claim, type, currency_status, and affordances — same shape as real memories, so
both M2_aff and M3 carry them faithfully. The probe-relevant memories and their
latest revisions are left intact and discoverable. Distractors are deterministic
per seed (reproducible).

```text
scale levels: K = 0 (control, = current result), 25, 50
```

We pad memories directly rather than re-running formation on a giant history:
cheaper, exact control of the distractor count, and it isolates the store size
from the formation step.

## Retriever (structure-enabled, flat memory cannot do this)

```text
score(memory) = | subject_entities(memory) ∩ {probe.required_target_entities,
                                               probe.acting_agent} |
keep top-k (k = 5) by score, ties broken by current-status priority then recency.
```

Only structured memory exposes `subject_entities` to retrieve by; the flat prose
condition has no addressable fields, so it must send everything.

## Metrics

```text
- accuracy per probe (same LLM judge, frozen).
- input tokens per call (cost). M3_retr sends k memories; M2_aff_scale sends N.
```

## Hypotheses

```text
H1 (format null persists): M3_dump_scale ~ M2_aff_scale on accuracy at every K.
   (structured format alone still does not help, consistent with the 10-mem test.)
H2 (selection helps accuracy): M3_retr_scale > M2_aff_scale as K grows, IF the flat
   dump drowns the relevant current memory among distractors (lost-in-the-middle).
H3 (selection helps cost): M3_retr_scale uses far fewer input tokens than
   M2_aff_scale at equal-or-better accuracy — the precision/cost win.
```

## Decision Rules (what each outcome lets the paper claim)

```text
- H2 holds (accuracy):  structure earns a real accuracy claim — "structured memory
  enables selective retrieval that flat memory cannot, and this matters at scale."
  Strongest outcome; structure is not a compromise.
- Only H3 holds (cost): structure's value is precision/cost — "same accuracy at a
  fraction of the context budget." A legitimate systems claim, unifies with the
  what-enters-context thesis.
- Neither (M2_aff_scale keeps up on accuracy AND tokens are not the story): THEN the
  affordance-content reframe is earned, not a compromise — structure genuinely does
  not help even in its home regime.
```

## Scale / Cost Of The Pilot

```text
3 conditions × 3 K-levels × 10 seeds × 4 headline probes
≈ 360 probe responses + 360 judge calls (~720 calls). Memory formation reused.
Start with K ∈ {0, 50} × {M2_aff_scale, M3_dump_scale, M3_retr_scale} for a fast
read, then fill K=25 if the trend is interesting.
```

## Implementation Sketch

```text
1. treatment_harness.py: add pad_with_distractors(memories, k, seed) producing
   deterministic synthetic distractor memories from the name/theme vocabulary.
2. Add conditions M2_aff_scale / M3_dump_scale / M3_retr_scale; for the retrieval
   condition build the memory block PER PROBE (retrieve top-k for that probe).
3. model_calling_runner.py: record input token count (usage field) per call.
4. A --memory-scale K flag threaded from run_stage1_pilot; aggregate accuracy AND
   mean input tokens per (condition × K).
```

## Why This Is The Right Next Step

It refuses to settle for an under-powered null. If structure matters, this is the
regime that shows it (selection at scale). If it does not even here, the
affordance-content claim becomes an earned finding rather than a rationalization.
Either way it also produces the cost/precision axis that future-proofs the result
against long-context models.
