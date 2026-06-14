# Stage 2 Main Experiment: 40-Seed Result

> Date: 2026-06-15
> Scope: 40 seeds × 5 conditions × 5 probes (200 condition cells, 1000 probe judgments).
> Design: `stage1_v2_dual_session_design_2026-06-15.md` + probe hardening
>         (`stage1_v2_final_2026-06-15.md`). seed_0001–0010 hand/migrated,
>         seed_0011–0040 generated from name/theme pools.
> Status: completed; 200/200 judge summaries, 0 failed seeds; concurrency (5-way).

## Headline (4 discriminating probes; probe_0003 is a flagged no-history control)

```text
condition          headline/160   rate    probe_0003 control
M0_GA                  15/160       9%         40/40
M0_prompted            15/160       9%         39/40
M2_memory_only        127/160      79%         40/40
M3_placebo             36/160       22%         40/40
M3_actionable         151/160      94%         40/40
```

Key contrasts:

```text
M3_actionable - M0_GA        +136/160   (+85 pp)   memory vs no persistent memory
placebo gap (M3 - M3_placebo) +115/160   (+72 pp)   current vs stale structured memory
M3_actionable - M2           +24/160    (+15 pp)   actionable structure beyond plain memory
M2 - M0_GA                   +112/160              memory content itself helps once M0 is windowed
```

All three treatment contrasts are large, clean, and stable from the 10-seed
pilot (which showed +32/40, +29/40, +7/40 respectively — the same picture).

## Probe-Level (pass of 40)

```text
condition         p0001  p0002  p0004  p0005  | p0003 (control)
M0_GA               2     9      1      3      |  40
M0_prompted         2    10      2      1      |  39
M2_memory_only     10    37     40     40      |  40
M3_placebo          0    19      0     17      |  40
M3_actionable      34    39     39     39      |  40
```

```text
probe_0001 reduced-reliance planning  — M3 34 vs M2 10 vs placebo 0 vs M0 2
probe_0002 bounded privacy revision   — current memory content (M3 39 ~ M2 37)
probe_0004 superseded routine lookup  — current vs stale (M3 39, M2 40, M0/plc ~0)
probe_0005 relationship rebuild       — memory-gated trust state (M3 39, M0 3)
probe_0003 external-sharing restraint — NO-HISTORY CONTROL (all ~40/40)
```

Per-seed: M3_actionable scores a perfect 4/4 on 32/40 seeds and ≥3/4 on 39/40.
M0_GA scores 0/4 on 27/40 seeds.

## Interpretation

1. **The mechanism is decisively supported at scale.** M3_actionable 94% vs M0_GA
   9% (+85 pp) on a clean, information-gapped, de-saturated benchmark. The 10-seed
   pilot was not a small-sample fluke — every contrast held at 40 seeds.

2. **The placebo gap rules out the "structured interface alone" explanation.**
   M3_actionable beats the interface-matched stale-memory placebo by +72 pp. Both
   conditions get the identical structured memory interface; they differ only in
   whether the content is current. So the win comes from current memory content
   plus its currency tracking, not from the format.

3. **probe_0001 isolates actionable structure (the M3-vs-M2 story).** The entire
   +15 pp M3-over-M2 gap is concentrated in reduced-reliance planning: M3 34/40 vs
   M2 10/40 (placebo 0/40, M0 2/40). Plain memory notes (M2) carry the same facts
   but do not reliably produce the reduced-reliance plan; the typed memories with
   planning affordances do. This is the cleanest evidence that the *actionable
   structure*, not just the content, does work.

4. **The no-history control validates the comparison.** Every condition, including
   M0, scores ~40/40 on probe_0003 (declining to leak a sensitive number to an
   outsider — default-cautious behavior). M0 is therefore not generally
   handicapped by the windowed context; its deficit on the other four probes is
   specifically about lacking persistent social memory.

## Stage 2 Verdict

```text
M3_actionable 94% vs M0_GA 9%          (+85 pp, n=40 seeds)
placebo gap                             (+72 pp)
actionable structure over plain memory  (+15 pp, probe_0001)
no-history control flat at ~40/40       (M0 not generally handicapped)
```

The core SMGA claim — that current, structured, actionable social memory improves
social-planning decisions over both a no-persistent-memory baseline and a
stale-memory placebo — is supported with a large effect on the 40-seed main set.

## Known Limitations / Next

```text
1. The information gap is created by session windowing. A reviewer may argue M0
   was simply denied context. The placebo gap already answers part of this, but
   the strongest rebuttal is a HORIZON SWEEP (Phase 7): give M0 the full but long
   history and show its currency-tracking degrades while M3 stays high, with the
   M3-M0 gap WIDENING as horizon grows.
2. Memory is formed one-shot from full history. An incremental/online memory
   variant is a more realistic mechanism but a larger build; defer unless needed.
3. probe_0002 shows M3 ~ M2 (content, not structure) and probe_0004 shows M3 ~ M2
   (currency, not structure). Only probe_0001 separates M3 from M2. A second
   structure-sensitive probe would strengthen the M3-vs-M2 claim.
4. Single judge model (gpt-5.4). A cross-model judge or human spot-check would
   harden the measurement for the paper.
```
