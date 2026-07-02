# CityIntent v1-rc1 External-Adapter Experiment

Date: 2026-07-02

## Question

Does the v1 evidence contract change what counts as success when four verified
external framework decision layers execute the same urban pressure scenarios?

## Setup

- Framework adapters: GATSim, SOTOPIA, Generative Agents, and AgentSociety.
- Integration: pinned official decision prompts/control structures adapted to
  CityIntent's common world and typed executor; not native full backends.
- Model: real configured `gpt-5.4-mini` provider calls.
- Scenarios: mid-route commute block, closed study replacement, school pickup,
  and meeting wait trap.
- Repeats: one. This is a release-candidate diagnostic, not a reliability
  estimate.

All 16 traces report a real provider and verified pinned source metadata.

## Agent-Level Results

| Adapter | Task completion | Legacy goal | Trace feasibility | Calls | Tokens |
|---|---:|---:|---:|---:|---:|
| GATSim | 0.750 | 0.788 | 0.830 | 11 | 103,483 |
| SOTOPIA | 0.077 | 0.488 | 1.000 | 21 | 144,137 |
| Generative Agents | 0.702 | 0.675 | 0.635 | 26 | 155,316 |
| AgentSociety | 0.827 | 0.750 | 0.823 | 22 | 154,504 |

The separation between `task_completion` and the legacy weighted sum is
material. SOTOPIA, for example, preserves constraints and produces legal
actions in this sample but completes few outcome-role conditions.

## Evidence Findings

- Three of four school-pickup traces produced accepted `child_pickup` service
  evidence. SOTOPIA did not; visiting or discussing school no longer earns the
  outcome.
- None of the four meeting traces produced an accepted interaction with Ben.
  SOTOPIA repeatedly messaged without moving. Generative Agents and
  AgentSociety coordinated and moved but did not complete a typed interaction.
  GATSim attempted interaction without the required prior coordination message,
  so the environment rejected the claims.
- GATSim alone produced a verified recovery in the mid-route block item in this
  single run.

The meeting result should not yet be read as a pure ranking of social ability.
The frameworks expose different native action surfaces, and the adapters map
those surfaces into a shared executor. The result currently supports the
narrower conclusion that none of these adapted decision layers produced enough
environment-owned evidence to prove the meeting under the common contract.

## Construct Implication

The v1 contract changes the scientific answer in the intended way: a plausible
meeting plan, repeated messages, venue arrival, or waiting no longer proves
that a meeting happened. This creates a measurable gap between plan plausibility
and realized urban outcome rather than rewarding narrative proxies.

## Human Validation

The deterministic 16-item audit package is archived at:

`6-city/annotation/cityintent_v1_rc1_blind_validation_2026-07-02/`

Its two annotation files are blank. Two independent humans must complete them
before verifier calibration and v1 freeze. Model labels cannot satisfy this
gate.

## Archive

Raw traces, prompts, model metadata, telemetry, manifests, tables, and failure
taxonomy are stored under:

`6-city/results/cityintent_v1_rc1/external_frameworks_4x4x1_gpt54mini_2026-07-02/`
