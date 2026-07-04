# CityIntent v1-rc1 Matched Perturbation Experiment

Date: 2026-07-04

## Research Question

How much do specific urban events change task completion and executable-trace
quality when agent architecture, model, private goal, city, budget, time window,
and success conditions are held fixed?

## Design

- Three matched pairs: mid-route network block, study-place closure, and optional
  social invitation before school pickup.
- Each pair contains an anonymous `a/b` scenario. Agents do not receive control or
  treatment labels, and both variants use the same title.
- Persona, private intention, memory, public context, initial state, episode,
  success conditions, scoring metrics, and architecture probes are byte-equivalent
  after pair metadata is removed. Only the event list differs.
- Four pinned official decision-layer adapters: GATSim, SOTOPIA, Generative Agents,
  and AgentSociety.
- Agent model: provider-backed `gpt-5.4-mini`.
- Coverage: 3 pairs x 2 variants x 4 adapters x 1 run = 24 traces and 12 matched
  control-treatment cells.
- Execution telemetry: 92 successful agent calls, 650,944 provider-reported tokens,
  and 906.246 seconds aggregate request latency.
- Soft judges: `gpt-5.4-mini` and `gpt-5.4` on all 24 traces.

A deterministic UtilityPlanner smoke test reaches task completion 1.0 and trace
feasibility 1.0 in all six scenarios, establishing that both variants are solvable
under the shared executor.

## Adapter-Level Paired Results

Deltas are treatment minus control. Negative values mean the event reduced the
metric. Joint success requires both full task completion and full feasibility.

| Adapter | Task control/treatment | Task delta | Feasibility control/treatment | Feasibility delta | Joint success control/treatment | Conditional task recovery | Conditional joint recovery |
|---|---:|---:|---:|---:|---:|---:|---:|
| AgentSociety | 0.667/0.846 | +0.179 | 1.000/0.575 | -0.425 | 0.667/0.000 | 0.500 (2) | 0.000 (2) |
| GATSim | 1.000/1.000 | 0.000 | 1.000/0.952 | -0.048 | 1.000/0.667 | 1.000 (3) | 0.667 (3) |
| Generative Agents | 1.000/0.846 | -0.154 | 1.000/0.707 | -0.293 | 1.000/0.000 | 0.667 (3) | 0.000 (3) |
| SOTOPIA | 0.000/0.179 | +0.179 | 0.778/0.833 | +0.056 | 0.000/0.000 | n/a (0) | n/a (0) |

Conditional recovery includes only cells where the corresponding control succeeds.
SOTOPIA cannot be credited or penalized for recovery because none of its three
control tasks fully succeeds in this run.

## Perturbation-Level Results

| Perturbation | Task control/treatment | Task delta | Feasibility control/treatment | Feasibility delta |
|---|---:|---:|---:|---:|
| Mid-route network block | 0.500/0.750 | +0.250 | 1.000/0.814 | -0.186 |
| Pickup social opportunity | 0.750/0.750 | 0.000 | 1.000/0.812 | -0.188 |
| Study-place closure | 0.750/0.653 | -0.097 | 0.833/0.674 | -0.159 |

The positive commute task delta is not evidence that disruption helps mobility.
In one AgentSociety cell, the event provides a salient cue that improves task
completion relative to a failed control, while introducing invalid execution.
Across adapters, all three event types reduce feasibility. This demonstrates why
task-only resilience scores can be misleading.

## Failure Mechanisms

- GATSim has no control failures and adds one closed-place action under treatment.
- Generative Agents has no control failures but treatment adds one impossible
  route, two invalid transitions, three budget failures, and one done-state loop.
- AgentSociety moves from one control goal-drift event to treatment failures
  comprising six invalid transitions, two budget failures, one closed-place
  action, and one done-state loop.
- SOTOPIA already has control goal-drift and invalid-transition failures; treatment
  changes the mix but does not produce joint success.

The event effect is therefore architecture-specific, not a uniform reduction in
one aggregate score.

## Soft-Judge Robustness

Face-plausibility threshold agreement is 75.0%, but Cohen's kappa is `-0.143` due
to strongly imbalanced labels and disagreement on the few low-scoring traces.
Trace-believability kappa is `0.474`. The mini judge lowers average face and trace
scores for every treatment family, but judge instability means these deltas remain
diagnostic rather than ground truth.

## Interpretation And Limits

This first screen supports a stronger CityAgency claim than an unpaired
leaderboard: the same urban event creates measurably different execution losses
and failure mechanisms across agent architectures, even with a fixed base model.
It also shows that task preservation alone is insufficient; some agents complete
the task while accumulating invalid state transitions or resource failures.

The experiment has one run per matched cell. It establishes direction and selects
high-information cells, not repeated causal-effect reliability. The next run
should repeat the study-place pair and the architecture cells with joint-success
reversals before generalizing effect sizes.

## Targeted Repeat Follow-Up

The study-place pair was subsequently repeated three times for GATSim, Generative
Agents, and AgentSociety. All nine control traces are joint successes. GATSim
retains 3/3 treatment joint success, while Generative Agents and AgentSociety each
retain 0/3. The targeted follow-up therefore confirms the first-screen ordering
for this facility-closure pair. See
`cityintent_v1_rc1_study_closure_3x2x3_2026-07-04.md`.

## Archive

Real traces and paired analysis:

`6-city/results/cityintent_v1_rc1/external_frameworks_4x3pairsx1_gpt54mini_2026-07-04/`

Deterministic solvability smoke test:

`6-city/results/cityintent_v1_rc1/paired_perturbation_design_smoke_2026-07-04/`
