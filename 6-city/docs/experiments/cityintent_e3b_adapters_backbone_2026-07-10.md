# E3b — The four official adapters on a stronger backbone (hard tier)

Date: 2026-07-10

## Question

E3 swept the backbone for the two paper-backed baselines. The missing cell was
the weak scaffolds: does SOTOPIA-style, which never reached the venue on
`gpt-5.4-mini` (no_venue_entry 22/27), stay broken on a much stronger model?
A "yes" would mean architectural deficits are immune to model capability.

## Setup

4 adapted official decision layers × 6 `social_outcome_hard` scenarios × 3
repeats (72 real traces) on `gpt-5.6-luna`; identical executor, evidence
contract, and judge (judge kept on mini for comparability). Compared against the
same matrix on `gpt-5.4-mini` (2026-07-10).

Archived: `results/cityintent_v1_rc1/e3b_adapters_luna_4x6hardx3_2026-07-10/`.

## Result — the prediction was wrong

| Adapter | mini task | luna task | Δ |
|---|---:|---:|---:|
| GATSim | 0.750 | 0.701 | **−0.049** |
| SOTOPIA-style | 0.158 | **0.527** | **+0.369** |
| Generative Agents | 0.410 | 0.629 | +0.219 |
| AgentSociety | 0.314 | 0.665 | +0.351 |

Co-presence failure mechanisms (failed/total, and the `no_venue_entry` count):

| Adapter | mini | luna |
|---|---|---|
| SOTOPIA-style | 27/27 failed, **22 never arrived** | 16/27 failed, **6 never arrived** |
| AgentSociety | 23/27, 10 never arrived | 8/27, 1 never arrived |
| Generative Agents | 24/27, 4 never arrived | 12/27, 3 never arrived |
| GATSim | 6/27, 0 never arrived | 8/27, 1 never arrived |

## Finding 1 — "never arrives" is mostly a weak-model failure, not an architectural one

SOTOPIA-style's signature failure collapses from 22 to 6 once the backbone is
strong. **This corrects the over-attribution in the 2026-07-10 failure-ladder
note**, which read the three-tier ladder (never arrives → arrives but doesn't act
→ acts but mistimes) as three *architectural* deficits. At least the first tier is
substantially a capability deficit: the scaffold could always express the move,
the weaker model simply did not choose it.

## Finding 2 — capability compresses scaffold differences (independent replication)

The four weaker policies gain significantly (SOTOPIA +0.369, AgentSociety +0.351,
GenAgents +0.219; all p < 0.02) while the strongest gains nothing (GATSim −0.049,
p = 0.83, not significant). The weakest scaffolds gain most; the strongest does
not move.

This independently replicates the E3 baseline-side result (Plan-and-Execute +0.371
overtaking ReAct's +0.071) in a completely different policy family. Across six
policies and two experiments the same regularity holds:

> **Scaffolding substitutes for model capability, and its value falls as
> capability rises.**

## Finding 3 — a ceiling, not a regression (corrected)

An earlier version of this note read GATSim's −0.049 as an engineered-scaffold
regression with design implications. **That was noise**: permutation p = 0.83,
95% CI [−0.293, +0.194].

The statistically supported statement is a *ceiling*: the four weaker policies
improve significantly (p < 0.02), while the two strongest — GATSim (0.750) and
ReAct (0.726) — do not move at all. A stronger backbone lifts weak scaffolds and
leaves good ones untouched. See
`results/cityintent_v1_rc1/backbone_significance_2026-07-10/`.

## Caveat

GATSim's meeting-scenario numbers remain confounded by the E4 finding that its
evidence synthesiser emits no `message` action at all, so message-gated
co-presence is unreachable for it regardless of backbone.
