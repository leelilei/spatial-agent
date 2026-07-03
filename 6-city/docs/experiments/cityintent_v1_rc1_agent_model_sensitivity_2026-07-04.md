# CityIntent v1-rc1 Agent-Model Sensitivity Experiment

Date: 2026-07-04

## Research Question

Are the architecture differences observed with `gpt-5.4-mini` stable when the
agent model is changed to `gpt-5.4`, while scenarios, adapters, executor, hard
scorers, and soft judges remain fixed?

## Setup

- Matched cells: 4 adapted official decision layers x 4 pressure scenarios.
- Baseline: repeat 1 from the `gpt-5.4-mini` repeated experiment.
- Candidate: one new `gpt-5.4` agent run per matched cell.
- Candidate execution telemetry: 65 successful agent calls, 478,636 provider-
  reported tokens, and 484.119 seconds aggregate request latency.
- Primary comparison: deterministic task completion and trace feasibility.
- Soft evaluators: `gpt-5.4-mini` and `gpt-5.4` on all 16 candidate traces.
- The runner records separate agent and judge configurations, preventing a model
  change from silently changing the primary soft evaluator.

## Paired Results

All deltas are `gpt-5.4` minus `gpt-5.4-mini` over identical scenario-adapter
cells.

| Adapter | Task mini | Task full | Delta | Feas. mini | Feas. full | Delta | Full-task rate mini/full | Fully-feasible rate mini/full |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AgentSociety | 0.827 | 0.577 | -0.250 | 0.823 | 0.863 | +0.040 | 0.750/0.500 | 0.250/0.500 |
| GATSim | 0.750 | 0.500 | -0.250 | 0.830 | 0.875 | +0.045 | 0.750/0.500 | 0.500/0.250 |
| Generative Agents | 0.702 | 0.827 | +0.125 | 0.635 | 0.950 | +0.315 | 0.500/0.750 | 0.000/0.750 |
| SOTOPIA | 0.077 | 0.452 | +0.375 | 1.000 | 0.896 | -0.104 | 0.000/0.250 | 1.000/0.500 |

The architecture ordering changes substantially. Generative Agents benefits most
on feasibility and becomes the strongest candidate-model adapter on mean task and
feasibility in this four-scenario run. SOTOPIA gains task completion but loses
some feasibility. AgentSociety and GATSim lose task completion despite small mean
feasibility gains.

This rejects the simple hypothesis that a stronger base model uniformly improves
every architecture. The observed behavior is consistent with a model-by-
architecture interaction: each control surface elicits and executes model output
differently.

## Cost

| Adapter | Calls mini/full | Latency mini/full (s) | Tokens mini/full |
|---|---:|---:|---:|
| AgentSociety | 5.50/6.00 | 37.7/53.2 | 38,626/44,214 |
| GATSim | 2.75/2.25 | 37.7/24.3 | 25,871/21,549 |
| Generative Agents | 6.50/2.50 | 41.5/19.2 | 38,829/15,824 |
| SOTOPIA | 5.25/5.50 | 26.5/24.3 | 36,034/38,072 |

The candidate model is not uniformly more expensive at the trace level because
architecture-dependent stopping behavior changes the number of calls and prompt
growth. Agent quality, architecture, and execution cost therefore need to be
reported together.

## Soft-Judge Sensitivity

For candidate traces, face-plausibility threshold agreement between the two judges
is 81.2% with kappa 0.455. Trace-believability agreement is 75.0% with kappa
0.256. `gpt-5.4` is not an independent evaluator of its own agent outputs, so the
paper should treat this second score only as a sensitivity check. Hard paired
outcomes carry the main claim.

## Limits And Next Test

This is a one-run paired screen. It identifies a strong interaction signal but
does not establish the reliability of each model effect. The most informative
follow-up is to repeat cells showing ranking reversals, especially Generative
Agents and GATSim, rather than immediately rerunning every cell.

The next distinct automatic experiment should add matched no-disruption and
disruption scenario pairs. That tests causal recovery, which the current scenario
set cannot cleanly separate from ordinary task difficulty.

## Archive

Raw traces, provider telemetry, deterministic evidence, both judge archives,
paired model tables, and manifests are stored at:

`6-city/results/cityintent_v1_rc1/external_frameworks_4x4x1_gpt54_2026-07-04/`
