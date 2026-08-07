# Seed-level SAID and agent-level SAID--HELD audit (2026-07-23)

## Decision

The pooled public-utterance result is reproduced exactly, but its interpretation
must remain descriptive. The source condition changes the composition of the
public transcript more clearly than it changes population-wide retrieval. The
data do not support a claim that most individual agents publicly state the
current value and then lose it.

## Seed-level SAID

| Condition | Pooled current / value-bearing | Pooled share | Mean of seed shares (95% t CI) |
|---|---:|---:|---:|
| Baseline | 22 / 35 | 62.9% | 76.6% [45.7, 107.6] |
| Persistent source | 27 / 33 | 81.8% | 84.4% [57.6, 111.3] |

The paired source-minus-baseline differences across seeds 41--45 are
`+58.3, -22.2, 0.0, -33.3, +36.4` percentage points. Their mean is **+7.8
points [−40.3, 56.0]**. The interval is extremely wide because each seed has
few and variable value-bearing utterances. The pooled +18.9-point contrast is
therefore retained as descriptive rather than inferential.

Unbounded t intervals are shown above for audit transparency; presentation may
clip proportion-axis graphics at 0--100% but must not silently change the
reported calculation.

## Descriptive agent alignment

| Condition | Agents that said current | Subsequently HELD current | Stale | Unknown |
|---|---:|---:|---:|---:|
| Baseline | 14 | 10 (71.4%) | 2 | 2 |
| Persistent source | 19 | 12 (63.2%) | 0 | 7 |

Across both conditions, 22/33 agent--seed instances that publicly uttered a
current marker later returned a current private answer. This conditional
quantity is descriptive and selection-conditioned; it is not a causal effect
and should not be compared numerically with the utterance-level SAID share.

## Valid interpretation

Use:

> The persistent source descriptively increases the current share of
> value-bearing public utterances, whereas population-wide private retrieval
> shows no statistically supported gain. The mismatch is between public-record
> visibility and society-wide retrievability, not evidence of widespread
> within-agent forgetting.

Do not use:

- “Most agents say the update but later forget it.”
- “The source has no effect on retrieval.”
- “The pooled SAID contrast is statistically established across societies.”

## Artifacts

- Analysis: `sim/said_held_alignment.py`
- Output: `sim/runs/m4_rebroadcast/said_held_alignment.json`
- Source logs: `sim/runs/m4_rebroadcast/{baseline,source}/`
