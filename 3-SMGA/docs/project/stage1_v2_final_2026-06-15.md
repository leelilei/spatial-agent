# Stage 1 v2 Final: Clean Mechanism Result (10 seeds)

> Date: 2026-06-15
> Scope: 10 seeds (seed_0001–0010) × 5 conditions × 5 probes.
> Design: `stage1_v2_dual_session_design_2026-06-15.md`.
> History: v2a (first dual-session) → v2b (probe hardening) → v2c (probe_0003 as
>          flagged control). This is the final Stage 1 result.
> Status: completed; 50/50 judge summaries, 0 errors; concurrency (5-way) enabled.

## Headline (4 discriminating probes; probe_0003 is a flagged no-history control)

```text
condition          headline/40   rate   probe_0003 control
M0_GA                  7/40       18%        10/10
M0_prompted            4/40       10%        10/10
M2_memory_only        32/40       80%        10/10
M3_placebo            10/40       25%        10/10
M3_actionable         39/40       98%        10/10
```

Key contrasts:

```text
M3_actionable - M0_GA   +32/40   (memory vs no persistent memory)
placebo gap             +29/40   (current vs stale structured memory)
M3_actionable - M2      +7/40    (actionable structure beyond plain memory)
```

All three contrasts are now large and clean — the goal of the v2 redesign.

## Probe-Level (pass of 10 seeds)

```text
condition         p0001  p0002  p0004  p0005   | p0003 (control)
M0_GA              1      3      0      3       | 10
M0_prompted        1      2      0      1       | 10
M2_memory_only     2     10     10     10       | 10
M3_placebo         0      7      0      3       | 10
M3_actionable      9     10     10     10       | 10
```

```text
probe_0001: reduced-reliance planning  — M3 vs ALL incl. M2 (structure signal)
probe_0002: bounded privacy revision   — current memory content (M3=M2 high)
probe_0004: superseded routine lookup  — current vs stale memory
probe_0005: relationship rebuild       — memory-gated trust state
probe_0003: external-sharing restraint — NO-HISTORY CONTROL (everyone passes)
```

## Why The Numbers Move

- **The information gap (A) drives M3 vs M0.** M0 only sees the day-3 current
  session, so it lacks the session-1 history the decisions hinge on; it drops to
  18%. The memory conditions carry that history forward.
- **Currency-sensitive probes (B) drive the placebo gap.** Stale early-session
  memory falls into each probe's stale trap (old reliance, old routine location,
  pre-repair trust), so M3_placebo sits at 25%.
- **probe_0001 isolates actionable structure.** M3 9/10 vs M2 2/10 vs placebo
  0/10: only the structured, current, affordance-framed memory supports
  reduced-reliance planning. This is the M3-vs-M2 signal (+7 overall).
- **probe_0003 is a deliberate negative control.** Declining to leak a sensitive
  number to an outsider is default-cautious behavior; every condition (incl. M0)
  scores 10/10. It is flagged `no_history_solvability_flag: true` and excluded
  from the headline. Its value: it confirms M0's deficit on the other four probes
  is *memory-specific*, not a general handicap from the windowed context.

## Audit Trail Of The Two Fixes This Round

- **probe_0004 was a rubric bug, not a memory miss.** The memory module correctly
  formed the routine relocation as a `revised` routine_memory ("moves to the lab
  starting day 3") in all seeds, and M3 answers named the lab. Failures came from
  a forbidden marker that matched the *activity name* (e.g. "morning standup"),
  which is legitimately part of a correct handoff answer. Removing it lifted M3
  from 5/10 to 10/10 with M0/placebo still at 0/10.
- **probe_0005 was leaking history.** Its v2a prompt stated the missed deliverable
  and apology, so M0 answered from the prompt (10/10). Removing the leak dropped
  M0 to 3/10 while M3 stayed at 10/10 — it now discriminates via the gap.

## Stage 1 Verdict

The SMGA mechanism is decisively supported on a clean, information-gapped,
de-saturated 10-seed diagnostic:

```text
M3_actionable 98% vs M0_GA 18%   (+32/40)
placebo gap                       (+29/40)
M3 vs plain memory                (+7/40, probe_0001)
no-history control flat at 10/10  (M0 not generally handicapped)
```

Gate decision: GO for Stage 2 at 30–50 seeds. Remaining prep is only scale:
parametrize the seed generator beyond the 10 hand-written specs and budget the
larger run.
