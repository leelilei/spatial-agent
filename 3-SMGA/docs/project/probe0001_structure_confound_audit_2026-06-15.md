# Audit: The M3-vs-M2 Gap Has a Content/Structure Confound

> Date: 2026-06-15
> Scope: why M3_actionable beats M2_memory_only on probe_0001 (the only probe that
>        separates them, and the load-bearing evidence for "actionable structure").
> Status: confound identified; `M2_aff_text` ablation launched to resolve it.

## Why This Matters

The whole novelty of SMGA over "just give the model memory" rests on
**M3_actionable > M2_memory_only**. In Stage 2 that gap is +15 pp overall, and it
is concentrated entirely in **probe_0001** (reduced-reliance planning):

```text
probe_0001 (pass/40):  M3 34   M2 10   placebo 0   M0 2
```

If this single contrast is an artifact, the paper's distinctive claim collapses to
"memory content helps" (already known). So it must be audited.

## What The Models Actually Do

On the 26/40 seeds where M3 passes and M2 fails probe_0001:

- **M2 already has the facts and the right disposition.** It recalls the missed
  deadline, the apology, the offer to take the pass, and explicitly says trust is
  "only partially repaired" / "I should not rely on her without caution."
- **M2 stops at attitude.** It does not convert reduced trust into a concrete
  safeguard. Judge rationales: "lacks explicit check-ins or a concrete
  verification/check of the deliverable."
- **M3 produces the concrete action.** "Set explicit checkpoints," "confirm the
  deliverable, deadline, and handoff points," "ask for visible follow-through."

So the surface story is appealing — structure turns understanding into action.

## The Confound

The M3 memory's `planning_affordances.suggested_context` **already contains the
operational answer**:

```text
reputation_memory affordance:
  "Use Maria for important deadline work WITH VERIFICATION CHECKPOINTS ..."
conflict_or_repair affordance:
  "... visible follow-through ..."  /  "pair it with CONFIRMATION STEPS because
  trust is only partially restored."
```

And the M2 serialization (`serialize_m2`) emits **only** claim + evidence +
currency status — it never shows the affordances. Confirmed on the actual prompts:
the M2 block for probe_0001 contains no "checkpoint/verification/confirmation"
text, while M3's does.

Therefore:

```text
M3 > M2 is NOT "same information, better structure".
M3 receives strictly MORE information — the pre-computed affordance action hints
that happen to contain exactly what the rubric rewards. M2 never sees them.
```

A reviewer who finds this reduces the "actionable structure" claim to "we wrote
the answer into the affordance and showed it to M3 but not M2."

## Two Readings, One Decisive Test

```text
Reading A (affordance-content): SMGA's thesis is that memory should STORE
  affordances (candidate actions). Then M3 > M2 validly = "affordance-augmented
  memory beats fact-only memory." Legitimate and central — but the word should be
  "affordances", not "structure".

Reading B (structure/format): the typed, currency-tagged structured FORMAT helps
  beyond the affordance content. Unproven.
```

Decisive ablation — **`M2_aff_text`**: give M2 the SAME affordance
`suggested_context` as plain prose (content-matched to M3, differing only in
format). Then:

```text
M3 ~ M2_aff_text  ->  the win is affordance CONTENT (Reading A). Reframe the
                      claim to "memory should store affordances", drop "structure".
M3 >  M2_aff_text ->  the typed structure/format itself helps (Reading B). The
                      strong structure claim survives.
```

`M2_aff_text` is implemented in `treatment_harness.py` (`serialize_m2_aff`): M2
plain notes plus `Possible action (<type>): <suggested_context>` lines, under the
plain "Memory notes:" header, with no JSON structure. Verified content-matched to
M3 and format-distinct.

## Result (10 seeds) — Reading A confirmed

```text
probe_0001 (pass/10):   M2_memory_only 2   M2_aff_text 9   M3_actionable 9
all 4 headline (/40):   M2 32            M2_aff_text 39    M3_actionable 39
```

**M3 ~ M2_aff_text (9 = 9), both >> M2 (2).** Per-seed the two agree on 9/10
(only seed_0003 and seed_0006 diverge, and they cancel). The structured JSON
format adds no measurable benefit once M2 sees the same affordance hints as prose.

Conclusion:

```text
- The "structured FORMAT helps" claim (Reading B) is NOT supported. Drop it.
- The win over fact-only memory is the affordance CONTENT (Reading A): memory that
  stores pre-computed, condition-blind planning affordances beats memory that
  stores only facts, regardless of serialization.
```

### Reframed thesis (resolves the #0 thesis-lock)

> SMGA's contribution is **amortized affordance formation**: the memory module
> distills actionable social affordances ("track follow-through with verification
> checkpoints") from the history at formation time, condition-blind. Fact-only
> memory (M2) forces the planner to re-derive this at decision time and it often
> stops at disposition ("be cautious") without operationalizing. The benefit is the
> affordance content, NOT the typed/structured serialization.

This is honest, still novel, and a sharper mechanism than "structure helps".

### Follow-ups

```text
1. Extend M2_aff_text to all 40 seeds for the paper's ablation table (10-seed
   result is already decisive; 40 is for reporting symmetry / CIs).
2. Rename the condition framing in the paper: M3 = "affordance-bearing memory",
   the M3-vs-M2 gap = "affordances vs facts", and report M2_aff_text as the
   format-control showing structure is not the driver.
3. Revisit whether the "currency_status" structure carries weight elsewhere
   (probe_0004 currency tracking) — that may be where format/typing still matters,
   separate from the affordance-content result here.
```
