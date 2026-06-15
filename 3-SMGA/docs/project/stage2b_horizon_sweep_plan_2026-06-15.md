# Phase 7 Plan: Horizon Sweep + Cost (Stage 2b primary secondary control)

> Date: 2026-06-15 (rewritten to account for 1M-token context models)
> Status: PLAN (not yet run). Builds on `stage2_main_40seed_2026-06-15.md`.
> Purpose: rebut the strongest reviewer objection to the Stage 2 result WITHOUT
>          betting the paper on "memory beats long context on accuracy".

## The Objection This Answers

Stage 2 creates the information gap by **session windowing**: M0 only sees the
day-3 current session. A reviewer can argue:

> "You did not show structured memory helps; you hid information from M0.
>  A single-session agent that kept the full history in its context would do fine —
>  especially with a 1M-token context window."

The 1M-context point is real and reshapes this experiment. We address it head-on.

## Why 1M Context Changes The Premise

M0 with the full history could fail for two distinct reasons. They are NOT the same
and the 1M context kills one of them:

```text
(1) Context overflow — the history literally does not fit.
    -> With gpt-5.4 at ~1M tokens, this does NOT happen at any feasible diagnostic
       horizon (~100 events is tens of thousands of tokens, orders of magnitude
       under 1M). Overflow is therefore NOT a mechanism we can claim. Dead.

(2) Reasoning degradation under load — even when everything fits, the model gets
    worse at tracking WHICH fact is current across many competing updates
    (lost-in-the-middle, distractor interference, retrieval-over-reasoning).
    -> This is independent of context size and is the only accuracy mechanism that
       survives a 1M window. But whether a strong long-context model actually
       degrades at feasible scales is an EMPIRICAL GAMBLE — it may resist.
```

So the naive "long history doesn't fit" framing is abandoned. We test mechanism (2)
empirically and, crucially, add a second axis that does not depend on it.

## Repositioning: What SMGA Buys In The 1M-Context Era

If a strong model can hold and correctly reason over the whole raw log, then
"structured memory is more accurate" is a fragile claim. SMGA's durable value is
not replacing long context — it is managing it:

```text
- What enters context: agents do not replay their entire history every decision
  (cost, multi-session, multi-agent). Structured memory IS the mechanism for
  deciding what to surface. The Stage 2 dual-session result already shows this and
  does NOT depend on any context limit.
- Cost / latency: re-reading and re-reasoning over a long raw log on every turn is
  expensive and slow; a compact structured memory is cheap. This grows MORE
  important as context windows grow, not less.
- Persistence / portability: distilled, updatable, shareable memory vs re-deriving
  from raw logs each time.
- Currency / auditability / privacy: explicit currency_status + evidence links are
  inspectable and can encode what is shareable; a raw log cannot be selectively
  exposed.
```

Consequence for the paper: the **main claim stays the dual-session result** (it is
about cross-session persistence and what-to-surface, not context size). The horizon
sweep is a **secondary, two-axis** experiment, and we pre-commit to a story that
holds even if the accuracy axis is null.

## Hypotheses

```text
Accuracy axis (mechanism 2, empirical gamble):
  H1: as competing-update density grows, full-context M0_GA accuracy on
      currency-sensitive probes decreases.
  H2: M3_actionable stays ~flat (currency is pre-resolved in the memory).
  H3: the M3 - M0 accuracy gap widens with load.

Cost axis (holds regardless of H1-H3):
  H4: input tokens and latency per decision for M0_GA_full grow roughly linearly
      with history length, while M3_actionable stays small and ~flat.
  H5: therefore accuracy-per-token (or accuracy-per-dollar) strongly favors
      M3_actionable at every nontrivial horizon, even if raw accuracy ties.
```

H4/H5 are the safety net: even if a 1M-context model never loses accuracy, SMGA
still wins decisively on cost. The deliverable cannot come back empty.

## Design

### Conditions (3, focused)

```text
M0_GA_full     : sees the FULL history (windowing DISABLED), no persistent memory
M2_memory_only : plain-text current memory
M3_actionable  : structured current memory (the treatment)
```

### Two axes

```text
Axis A (load):    interference density = {low, medium, high} competing updates
                  on distractor entities, with the probe-relevant fact + its single
                  latest revision held fixed. Optionally push a "very high" level to
                  search for the breaking point of 1M-context reasoning.
Axis B (cost):    record input tokens, output tokens, and wall-clock latency per
                  probe for every condition, at every load level.
```

Load is increased by adding competing revisions/contradictions on OTHER entities,
not by padding with inert filler — the test is interference, not length per se.
Because overflow is off the table, we do not need to approach 1M tokens; we need
enough *interfering currency updates* to stress mechanism (2).

### Held fixed

Same currency-sensitive probes, same gold facts for probed entities, same
memory-formation module (reads full history at every level). Only distractor-update
density changes. Validate that padding never touches the probed entities' gold facts.

### Scale

```text
3 conditions × 3 load levels × ~15 seeds × 4 headline probes
≈ 540 probe responses + 540 judge calls  (~1100 model calls)
Reuse the Stage 2 "low/short" cells where the seed is identical.
```

## Implementation Sketch

```text
1. generate_stage1_seeds.py: add --interference {low,medium,high} that injects N
   competing revision/contradiction events on distractor entities into session 1,
   leaving events 0001-0016 and all probed-entity facts intact.
2. baseline_harness.py: add a config/env flag to DISABLE windowing so M0_GA sees
   the full log for THIS experiment. Default stays windowed (Stage 2). The memory
   module already reads the full log, so M2/M3 are unchanged.
3. model_calling_runner.py: it already records elapsed_ms; also capture input/output
   token counts (from the API usage field) into the raw record for the cost axis.
4. Aggregate: accuracy per (load × condition) AND tokens/latency per (load × condition).
```

## Deliverables

```text
- Accuracy table + figure: accuracy vs interference level, one line per condition.
- Cost table + figure: input tokens & latency vs history length, per condition.
- The headline number: accuracy-per-token (or per-dollar) for M3 vs M0_full.
```

## Pre-Committed Interpretation (incl. the null)

```text
- If M0_GA_full degrades with load (H1-H3 hold): strongest result — structured
  memory is both more accurate AND cheaper; the windowing critique is fully answered.
- If M0_GA_full stays accurate even at high load (accuracy null): we report it
  honestly and lean on (a) the cost axis (H4/H5) and (b) the dual-session result.
  Framing becomes "with frontier long-context models, structured social memory's
  value is what-to-surface + persistence + cost + auditability, not raw accuracy
  under overflow." This is still a publishable, defensible contribution.
```

## Risks / Notes

```text
- Distractor updates must not contradict probe-relevant facts; assert this in
  validate_seed for interference-augmented seeds.
- Token-count capture depends on the provider returning a usage field; verify with
  the fhl Responses API before the full run.
- Keep judge and seeds frozen; only interference level (and windowing flag) vary.
```

## Sequencing

First Phase 7 item (`P7-00`), ahead of the M0_plus and GraphMemory architecture
controls, because it defends the central result. Run after the Stage 2 write-up.
The main paper claim does not depend on its outcome; it strengthens and future-
proofs the result against the long-context objection.
