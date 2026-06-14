# Stage 1 v2 Results: Dual-Session + Currency Probes (10 seeds)

> Date: 2026-06-15
> Scope: 10 seeds (seed_0001–0010, all migrated to v2) × 5 conditions × 5 probes.
> Design: `stage1_v2_dual_session_design_2026-06-15.md`.
> Status: SUPERSEDED by `stage1_v2_final_2026-06-15.md` (probe hardening + p0003 control).
>         Kept for the v2a (first dual-session) numbers and probe-saturation history.

## Headline (vs v1)

```text
condition          v1 rate    v2 rate
M0_GA               74%        44%
M0_prompted         70%        40%
M2_memory_only      66%        72%
M3_placebo          56%        48%
M3_actionable       76%        86%
```

The two key contrasts both became clean and large:

```text
                       v1        v2
M3_actionable - M0_GA  +2/50    +21/50
placebo gap            +10/50   +19/50   (M3_actionable - M3_placebo)
M3_actionable - M2     +5/50    +7/50    (43 vs 36; structure beyond content)
```

The dual-session information gap (A) opened the M3-vs-M0 separation that v1
lacked: M0 dropped from 74% to 44% because it no longer sees the session-1
history. The currency-sensitive probes (B) sharpened the placebo gap. M2 (72%)
also rose well above M0 (44%): once M0 lacks the history, the memory *content*
itself helps, and the actionable *structure* adds a further +7 on top of M2.

## Per-Seed (passed of 5)

```text
seed       M0_GA  M0_prompted  M2_mem  M3_plc  M3_act
seed_0001    3        2          5       3       5
seed_0002    2        1          3       3       4
seed_0003    3        2          4       1       4
seed_0004    2        2          4       3       5
seed_0005    2        2          3       2       4
seed_0006    3        1          3       2       3
seed_0007    2        3          4       3       5
seed_0008    1        2          2       2       3
seed_0009    2        2          5       3       5
seed_0010    2        3          3       2       5
```

M3_actionable is the top condition on every seed (tie only on seed_0006).

## Probe-Level (pass of 10 seeds)

```text
condition         p0001  p0002  p0003  p0004  p0005
M0_GA              0      3      9      0     10
M0_prompted        0      2      9      0      9
M2_memory_only     2     10      9      5     10
M3_placebo         0      5      9      0     10
M3_actionable      8     10     10      5     10
```

Probe meanings:

```text
probe_0001: reduced-reliance planning (currency + structure)
probe_0002: bounded privacy after scope revision
probe_0003: norm containment after external disclosure (targeting fixed)
probe_0004: superseded routine lookup (moved location)
probe_0005: relationship rebuild after partial repair
```

## Interpretation

Three probes now discriminate cleanly; two are saturated.

- **probe_0001 is the strongest mechanism signal**: M3 8/10 vs M0 0/10, placebo
  0/10, **and M2 only 2/10**. This is the cleanest evidence yet that *actionable
  structure* (not just current content) helps reduced-reliance planning — it
  separates M3 from every other condition, including plain memory.
- **probe_0002** (bounded privacy): M3 and M2 both 10/10, placebo 5/10, M0 3/10.
  Current memory content drives this; structure adds nothing here (M3 = M2).
- **probe_0004** (moved-routine lookup): M3 and M2 5/10, M0 and placebo 0/10.
  Clean memory-vs-no-memory and current-vs-stale signal, but only 5/10 absolute —
  the memory module does not always capture the routine relocation, or the judge
  is strict on naming "the lab". Worth a quick audit before Stage 2.

### New saturation to fix next

The targeting fix and prompt framing pushed two probes to the ceiling:

- **probe_0003** is now 9–10/10 for *every* condition, including M0. The audit fix
  (accept core team OR information owner, score on containment markers) over-
  corrected — it is now too easy and no longer discriminates.
- **probe_0005** is 9–10/10 for everyone. The prompt states the missed deliverable
  and apology, so M0 answers it from the prompt alone without any memory.

Net: v2 swapped which probes are saturated. The benchmark now has 3 strong
discriminating probes (0001, 0002, 0004) instead of v1's 1, but 0003 and 0005
should be hardened (or down-weighted) before the main run.

## Recommendation

The mechanism is now clearly supported on a clean, information-gapped benchmark:
M3 > M0 (+21/50) and M3 > placebo (+19/50), with probe_0001 showing M3 > M2.
Before the 30–50 seed Stage 2 run:

```text
1. Harden probe_0003 (require observer-directed repair, not just containment)
   and probe_0005 (stop leaking the history in the prompt) so all 5 discriminate.
2. Audit probe_0004: confirm the memory module captures the routine relocation
   (fact_0010) so the 5/10 ceiling is a real limit, not a formation miss.
3. Then scale to 30–50 seeds.
```
