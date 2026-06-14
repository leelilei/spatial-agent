# Stage 1 Pilot Alpha

> Date: 2026-06-15
> Scope: 2 existing diagnostic seeds x 5 conditions x 5 probes.
> Status: alpha pilot closure, not the full 5/10-seed Stage 1 pilot.
> Superseded for current planning by `stage1_pilot_10seed_2026-06-15.md`.

## Why This Run Exists

The previous diagnostic table was missing `M3_placebo`, so `M3_actionable=10/10`
could not distinguish current memory content from the structured M3 interface.
This run adds the stale-memory placebo condition and reruns the two existing
diagnostic seeds under persisted LLM-judge summaries.

## Conditions

```text
M0_GA
M0_prompted
M2_memory_only
M3_placebo
M3_actionable
```

`M3_placebo` uses the same structured-M3 interface as `M3_actionable`, but its
memory content is deterministically constructed from the early log before the
first current-update event. Later contradictions, repairs, and permission
revisions are omitted, and the stale facts are presented as current to preserve
an interface-matched placebo.

## Headline Scores

```text
              seed_0001   seed_0002   total/10
M0_GA            4/5         5/5         9
M0_prompted      4/5         3/5         7
M2_memory_only   5/5         3/5         8
M3_placebo       3/5         4/5         7
M3_actionable    5/5         5/5         10
```

## Failure Pattern

```text
seed_0001 / M0_GA: probe_0004
seed_0001 / M0_prompted: probe_0004
seed_0001 / M2_memory_only: none
seed_0001 / M3_placebo: probe_0003, probe_0004
seed_0001 / M3_actionable: none

seed_0002 / M0_GA: none
seed_0002 / M0_prompted: probe_0003, probe_0004
seed_0002 / M2_memory_only: probe_0002, probe_0003
seed_0002 / M3_placebo: probe_0004
seed_0002 / M3_actionable: none
```

## Interpretation

This is a positive mechanism signal, not a conclusion:

- `M3_actionable` beats `M3_placebo` by 3/10 on the current two-seed diagnostic set.
- `M3_actionable` also beats `M0_prompted` by 3/10.
- `M0_GA` remains strong at 9/10, so the plain GA baseline must stay prominent.
- `M3_placebo` still passes several probes because some probes are solvable from
  the probe wording, stable early facts, general social norms, or routine facts.
- The most diagnostic placebo failure is `probe_0004` in both seeds: stale memory
  over-relies on Klaus/Ben reliability, while actionable memory reflects reduced
  trust and verification needs.

## Pilot Boundary

This alpha run closes the local 2-seed control gap. It does not replace the
planned Stage 1 seed expansion.

Recommended next pilot:

```text
10 seeds x 5 probes x 5 conditions
```

Minimum acceptable next pilot if budget is tight:

```text
5 seeds x 5 probes x 5 conditions
```

The next work item is seed expansion, not more repeated runs of the same two
seeds.
