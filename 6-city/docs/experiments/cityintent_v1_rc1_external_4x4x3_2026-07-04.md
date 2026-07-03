# CityIntent v1-rc1 External-Adapter Repeated Experiment

Date: 2026-07-04

## Research Question

When four adapted urban-agent decision architectures use the same model, world,
typed executor, and pressure scenarios, do plausible-looking plans reliably become
environment-supported urban outcomes?

## Setup

- Agent decision layers: GATSim, SOTOPIA, Generative Agents, and AgentSociety.
- Integration level: pinned official prompt/control surfaces adapted to the shared
  CityIntent executor, not native end-to-end framework backends.
- Agent model: real provider-backed `gpt-5.4-mini` calls.
- Scenarios: closed study-place substitution, mid-route commute disruption,
  school pickup under social pressure, and meeting/waiting trap.
- Repeats: 3 per scenario-adapter cell.
- Traces: 48 total. Repeat 1 reuses the archived 2026-07-02 rc1 run; repeats 2 and
  3 are new independent provider runs.
- Agent execution telemetry: 228 successful model calls, 1,600,087 provider-
  reported tokens, and 1,415.569 seconds aggregate request latency; no failed
  provider call appears in the archived trace summaries.
- Soft evaluators: `gpt-5.4-mini` and `gpt-5.4`, each judging all 48 identical traces.
- Hard outcomes: deterministic environment state, typed evidence, constraints,
  and transition validity.

## Main Architecture Results

| Adapter | Mean task | Mean feasibility | Full task success | Fully feasible | Face plausible | Plausible task failure | Plausible infeasible | `pass^3` task | `pass^3` feasible |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| AgentSociety | 0.702 | 0.765 | 0.583 | 0.250 | 1.000 | 0.417 | 0.750 | 0.250 | 0.250 |
| GATSim | 0.667 | 0.908 | 0.667 | 0.583 | 0.583 | 0.167 | 0.333 | 0.500 | 0.250 |
| Generative Agents | 0.619 | 0.678 | 0.417 | 0.000 | 0.667 | 0.500 | 0.667 | 0.250 | 0.000 |
| SOTOPIA | 0.160 | 0.897 | 0.000 | 0.750 | 0.833 | 0.833 | 0.250 | 0.000 | 0.500 |

`Full task success` and `fully feasible` require a score of at least 0.999.
`Face plausible` uses the pre-registered exploratory threshold of 0.70 from the
`gpt-5.4-mini` judge. `pass^3` is the fraction of an adapter's four scenario cells
that succeed on all three runs.

## Core Finding: Proof Obligations Dissociate

No architecture dominates all evaluation objects:

- AgentSociety receives the highest mean face-plausibility score (0.895) and the
  highest mean task score, but only 25% of traces are fully feasible. Every trace
  is face-plausible, while 75% are plausible but not fully feasible.
- GATSim has the highest mean feasibility (0.908), highest full-task rate (66.7%),
  and best `pass^3` task reliability (50%), while its mean trace-believability score
  is the lowest under the mini judge.
- Generative Agents completes some intended outcomes, but no trace is fully
  feasible across the 12 runs; money-budget failures dominate its taxonomy.
- SOTOPIA is the cleanest example of legal non-achievement: 75% of traces are fully
  feasible, but none fully completes the intended task. Ten of 12 traces are
  face-plausible and also fail full task completion.

Across all 48 traces, the mini judge's face plausibility has Pearson correlation
`-0.041` with deterministic task completion and `-0.262` with feasibility. After
removing scenario-adapter cell means, the correlations remain `-0.048` and
`-0.341`. In this pilot, looking plausible is not evidence of completing the task
or executing a fully valid trace.

## Failure Signatures

The architecture adapters fail differently:

- AgentSociety: invalid state transitions (10), money-budget failures (5), and
  time-budget failures (3).
- GATSim: invalid state transitions (4) and time-budget failures (4), with one
  closed-place action and one goal-drift event.
- Generative Agents: money-budget failures (16), impossible routes (7), and invalid
  transitions (3).
- SOTOPIA: goal drift (9), invalid transitions (3), and money-budget failures (2).

These are diagnostic signatures under a shared executor, not claims about each
framework's complete native system.

## Judge Robustness

| Soft metric | Mean mini | Mean full | MAE | Pearson | Spearman | Threshold agreement | Kappa |
|---|---:|---:|---:|---:|---:|---:|---:|
| Face plausibility | 0.727 | 0.694 | 0.176 | 0.470 | 0.432 | 0.729 | 0.373 |
| Trace believability | 0.367 | 0.486 | 0.207 | 0.497 | 0.457 | 0.729 | 0.246 |
| Rationale alignment | 0.547 | 0.457 | 0.243 | 0.528 | 0.548 | 0.646 | 0.308 |
| Urban common sense | 0.578 | 0.630 | 0.200 | 0.451 | 0.396 | 0.625 | 0.254 |

Cross-judge agreement is only moderate. Soft scores must therefore report judge
identity and sensitivity, and cannot serve as completion truth. The deterministic
task, feasibility, resource, and state-transition scores are unchanged by judge
choice.

## What This Supports

The pilot supports a narrow but meaningful benchmark claim:

> Urban-agent architectures can look plausible, remain physically legal, and
> complete intended outcomes to very different degrees. These proof obligations
> are not interchangeable, and their separation exposes architecture-specific
> failures hidden by narrative evaluation or one-shot success.

It does not yet support a human-realism or macro urban-validity claim. The blinded
two-person construct audit remains required before v1 freeze.

## Archive

All traces, prompts, provider metadata, deterministic scores, both judge archives,
reliability tables, correlation tables, and comparison manifests are stored at:

`6-city/results/cityintent_v1_rc1/external_frameworks_4x4x3_gpt54mini_2026-07-04/`
