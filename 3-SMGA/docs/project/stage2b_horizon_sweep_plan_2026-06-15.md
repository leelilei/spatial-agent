# Phase 7 Plan: Horizon Sweep (Stage 2b primary secondary control)

> Date: 2026-06-15
> Status: PLAN (not yet run). Builds on `stage2_main_40seed_2026-06-15.md`.
> Purpose: rebut the strongest reviewer objection to the Stage 2 result.

## The Objection This Answers

Stage 2 creates the information gap by **session windowing**: M0 only sees the
day-3 current session, so it lacks the session-1 history. A reviewer can argue:

> "You did not show structured memory helps; you just hid information from M0.
>  A single-session agent that kept the full history in its context would do fine."

The Stage 2 placebo gap partly answers this (M3 beats a structured-but-stale
memory), but the decisive rebuttal is a setting where M0 has the **full** history
and still fails because the history is **too long to track currency over**.

## Hypothesis

As the interaction horizon (length of past history) grows:

```text
H1: full-context M0_GA accuracy on currency-sensitive probes DECREASES
    (it cannot reliably track which facts are current across a long log).
H2: M3_actionable accuracy stays ~flat (compressed, typed, currency-tagged memory).
H3: the M3 - M0 gap WIDENS with horizon.
```

H3 is the headline figure: a line plot, x = horizon, y = headline accuracy, with
the M3 and M0 curves diverging. If it holds, "you just hid info from M0" is dead:
here M0 sees everything and still degrades.

## Design

### Conditions (3, not 5 — keep it cheap and focused)

```text
M0_GA_full     : sees the FULL history (windowing DISABLED), no persistent memory
M2_memory_only : plain-text current memory
M3_actionable  : structured current memory (the treatment)
```

Drop M0_prompted and M3_placebo here — the placebo's job (interface-matched
control) is already done in Stage 2; this experiment is about horizon scaling.

### Horizon levels (history depth)

```text
short  : ~13 session-1 events   (= current Stage 2 seeds)
medium : ~45 events             (pad with distractor + competing-update events)
long   : ~110 events            (deeper burial of the deciding facts)
```

Padding must add **genuine currency-tracking load**, not filler: interleave extra
relationships, commitments, and *revisions/contradictions on distractor entities*
so the model must distinguish the probe-relevant current fact from many similar
updates. The probe's deciding fact and its single latest revision stay fixed; only
the surrounding volume of competing updates grows.

### Held fixed across levels

Same 5 currency-sensitive probes, same gold facts for the probed entities, same
memory-formation module (reads full history at every level). Only the session-1
event count and distractor-update density change.

### Scale

```text
3 horizons × 3 conditions × ~15 seeds × 5 probes
= ~675 probe responses + ~675 judge calls  (~1350 model calls)
```

Reuse the Stage 2 "short" cells where the seed is identical to avoid recompute.

## Implementation Sketch

```text
1. generate_stage1_seeds.py: add --horizon {short,medium,long} that pads
   session_1 with N distractor/update events (deterministic from a distractor
   pool) while keeping events 0001-0016 and the probe-relevant facts intact.
2. baseline_harness.py: add a flag (env or config) to DISABLE windowing so
   M0_GA sees the full log for this experiment. Default stays windowed (Stage 2).
   The memory module already reads the full log, so M2/M3 are unchanged.
3. Watch context length: at "long", M0's full-history prompt may approach the
   model context window. Record token counts; if needed cap distractor verbosity
   rather than truncating probe-relevant events.
4. run + progress_monitor.py work as-is; aggregate per-horizon headline accuracy.
```

## Metrics / Deliverable

```text
- Table: headline accuracy per (horizon × condition).
- Figure: accuracy vs horizon, one line per condition (the divergence plot).
- The number that matters: M3_actionable - M0_GA_full at short vs long.
  Predicted: small-to-moderate at short, large at long.
```

## Risks / Notes

```text
- If M0_GA_full stays high even at long horizon, the windowing critique has teeth
  and the paper should foreground the placebo gap instead of the M0 gap. Either
  way the experiment is informative.
- Distractor updates must not accidentally contradict the probe-relevant facts
  (validate that gold facts for probed entities are untouched by padding).
- Keep the judge and seeds frozen; only horizon varies, so differences are
  attributable to history length.
```

## Sequencing

Run after the Stage 2 main result is written up. This is the first Phase 7 item
(`P7-00`), ahead of the M0_plus and GraphMemory architecture controls, because it
defends the central result rather than widening the architecture comparison.
