# CityIntent v1-rc1 External-Adapter Scenario-Breadth Experiment

Date: 2026-07-04

## Research Question

Do the architecture-specific gaps observed in four pressure scenarios remain visible
when the same adapted decision layers are evaluated across all 12 current CityIntent
scenario packages?

## Setup

- Decision layers: GATSim, SOTOPIA, Generative Agents, and AgentSociety.
- Integration level: pinned official prompt/control surfaces adapted to the shared
  CityIntent executor, not native end-to-end framework deployments.
- Agent model: real provider-backed `gpt-5.4-mini` calls.
- Coverage: 12 scenarios x 4 adapters x 1 run = 48 traces.
- The four pressure-scenario cells reuse repeat 1 of the archived repeated experiment;
  the other 32 traces are new provider executions.
- Execution telemetry: 219 successful agent calls, 1,531,834 provider-reported
  tokens, and 1,320.862 seconds aggregate request latency.
- Soft evaluators: `gpt-5.4-mini` and `gpt-5.4`, each judging the same 48 traces
  without deterministic validator labels.
- Hard outcomes: deterministic environment state, typed evidence, constraints,
  resource accounting, and transition validity.

## Main Architecture Results

| Adapter | Mean task | Mean feasibility | Full task | Fully feasible | Face plausible | Plausible task failure | Plausible infeasible |
|---|---:|---:|---:|---:|---:|---:|---:|
| AgentSociety | 0.528 | 0.627 | 0.417 | 0.250 | 0.917 | 0.500 | 0.667 |
| GATSim | 0.840 | 0.943 | 0.750 | 0.833 | 0.583 | 0.083 | 0.167 |
| Generative Agents | 0.537 | 0.691 | 0.333 | 0.000 | 0.750 | 0.583 | 0.750 |
| SOTOPIA | 0.098 | 0.838 | 0.000 | 0.583 | 0.750 | 0.750 | 0.333 |

`Full task` and `fully feasible` require a score of at least 0.999. `Face
plausible` uses the pre-registered exploratory threshold of 0.70 from the
`gpt-5.4-mini` judge. Because this matrix has one run per cell, it measures
scenario breadth, not repeated reliability.

## Findings

The broad matrix preserves the main dissociation seen in the repeated pressure
subset. GATSim performs best on deterministic task completion and feasibility, but
does not lead the soft plausibility table. AgentSociety is judged face-plausible
on 91.7% of traces while only 25% are fully feasible. Generative Agents has no
fully feasible trace and is face-plausible but infeasible on 75% of scenarios.
SOTOPIA is frequently legal but non-achieving: no trace fully completes its task,
yet 75% are face-plausible.

Across all 48 traces, mini-judge face plausibility correlates negatively with
deterministic task completion (Pearson `-0.207`, Spearman `-0.132`) and feasibility
(Pearson `-0.166`, Spearman `-0.245`). These are pooled architecture-by-scenario
associations; within-cell correlations are undefined with one run per cell.

Failure signatures also remain architecture-specific:

- AgentSociety: invalid state transitions (15), money-budget failures (9), and
  time-budget failures (3).
- GATSim: invalid state transitions (4), time-budget failures (2), and goal drift (1).
- Generative Agents: money-budget failures (11), invalid transitions (6), and
  impossible routes (5).
- SOTOPIA: goal drift (7), invalid transitions (7), plus one done-state loop and
  one money-budget failure.

## Judge Robustness

| Soft metric | Mean mini | Mean full | MAE | Pearson | Spearman | Threshold agreement | Kappa |
|---|---:|---:|---:|---:|---:|---:|---:|
| Face plausibility | 0.705 | 0.713 | 0.180 | 0.416 | 0.471 | 0.708 | 0.300 |
| Trace believability | 0.373 | 0.494 | 0.201 | 0.549 | 0.528 | 0.771 | 0.362 |
| Rationale alignment | 0.544 | 0.467 | 0.187 | 0.660 | 0.648 | 0.750 | 0.464 |
| Urban common sense | 0.538 | 0.673 | 0.211 | 0.510 | 0.530 | 0.646 | 0.306 |

Soft-judge agreement is only moderate. Judge identity and sensitivity must be
reported, while deterministic task and feasibility evidence remain the benchmark's
primary truth source.

## Interpretation And Limits

This experiment strengthens the benchmark story in two ways. First, the
plan-to-trace gap is not confined to four hand-picked pressure episodes. Second,
the adapters expose different failure mechanisms under an identical model and
executor, which is more informative than a single aggregate leaderboard.

It does not establish native-framework superiority, human behavioral realism, or
macro urban validity. It is a controlled comparison of adapted official decision
layers. The 4 x 4 x 3 pressure experiment supplies repeat reliability; this 4 x
12 x 1 experiment supplies scenario breadth. Human construct validation remains
a separate release gate.

## Archive

All traces, provider metadata, deterministic scores, both judge archives, failure
tables, correlations, and comparison manifests are stored at:

`6-city/results/cityintent_v1_rc1/external_frameworks_4x12x1_gpt54mini_2026-07-04/`
