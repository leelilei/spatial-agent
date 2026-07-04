# CityIntent v1-rc1 Study-Closure Repeated Pair Experiment

Date: 2026-07-04

## Research Question

Does the joint-success collapse observed under study-place closure persist across
repeated provider runs, or was it a one-run fluctuation?

## Setup

- Matched pair: anonymous no-event control and library-closure treatment.
- Non-event scenario fields are identical by package validation.
- Adapters: GATSim as the stable reference, plus Generative Agents and
  AgentSociety as the two first-screen joint-success reversals.
- Agent model: provider-backed `gpt-5.4-mini`.
- Repeats: 3 per scenario-adapter cell.
- Coverage: 3 adapters x 2 variants x 3 repeats = 18 traces and 9 matched cells.
- Execution telemetry: 59 successful calls, 421,413 provider-reported tokens,
  and 355.828 seconds aggregate request latency.
- Soft judges: `gpt-5.4-mini` and `gpt-5.4` on all 18 traces.

## Repeated Paired Results

| Adapter | Task control/treatment | Task delta | Feasibility control/treatment | Feasibility delta | Joint success control/treatment | Conditional task recovery | Conditional joint recovery |
|---|---:|---:|---:|---:|---:|---:|---:|
| AgentSociety | 1.000/0.692 | -0.308 | 1.000/0.625 | -0.375 | 1.000/0.000 | 0.333 (3) | 0.000 (3) |
| GATSim | 1.000/1.000 | 0.000 | 1.000/1.000 | 0.000 | 1.000/1.000 | 1.000 (3) | 1.000 (3) |
| Generative Agents | 1.000/0.538 | -0.462 | 1.000/0.532 | -0.468 | 1.000/0.000 | 0.000 (3) | 0.000 (3) |

Every control trace is a full joint success. The treatment therefore measures
closure response rather than baseline inability.

## Repeat-Level Evidence

- GATSim: task and feasibility are both `1.0` in all three controls and all three
  treatments. This is `pass^3` joint recovery.
- Generative Agents: all controls are joint successes. Every treatment has task
  `0.538`; feasibility is `0.500`, `0.429`, and `0.667`. Joint recovery is 0/3.
- AgentSociety: all controls are joint successes. Treatment task is `1.0`,
  `0.538`, and `0.538`; feasibility is `0.750`, `0.625`, and `0.500`. Joint
  recovery is 0/3.

The original architecture ordering is therefore not a one-run artifact for this
pair.

## Failure Mechanisms

- Generative Agents treatment traces contain six money-budget failures, two
  time-budget failures, and one impossible route across three repeats.
- AgentSociety treatment traces contain four closed-place actions, three
  money-budget failures, and one time-budget failure.
- GATSim records no deterministic failure in either condition.

The two failing architectures collapse differently. Generative Agents tends to
construct costly or overlong replacement activity chains. AgentSociety more often
continues to interact with the closed preferred place before accumulating resource
or time failures.

## Plausibility Is Still Insufficient

The mini judge marks every Generative Agents and AgentSociety trace as face-
plausible, including all six infeasible treatments. Across all 18 traces, face
plausibility has Pearson correlation `0.052` with deterministic feasibility.

The two judges agree on the face threshold for 72.2% of traces, but kappa is
`-0.154` because labels are highly imbalanced. Trace-believability agreement is
66.7% with kappa `0.333`. Soft judgment remains supporting evidence only.

## New Conclusion

For a controlled facility-access shock, architecture determines whether a
plausible replacement plan becomes a valid activity trace. A stronger narrative
response is not enough: two adapters repeatedly fail resource, time, or state
proof obligations, while GATSim repeatedly completes the same paired task without
violations.

This is evidence for an architecture-specific urban recovery mechanism under one
pair and one base model. It is not yet a general ranking of native frameworks or
evidence of human behavioral realism.

## Archive

`6-city/results/cityintent_v1_rc1/external_frameworks_3x1pairx3_gpt54mini_2026-07-04/`
