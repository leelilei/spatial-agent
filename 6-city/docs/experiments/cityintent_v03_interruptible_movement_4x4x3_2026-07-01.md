# CityIntent v0.3 Interruptible Movement: 4 x 4 x 3 Experiment

Date: 2026-07-01

## Question

Can an urban agent recover from a disruption at a real movement decision
boundary, and can the benchmark distinguish legal execution from actual goal
completion?

## Protocol

CityIntent v0.3 adds interruptible multi-edge movement:

- A block that becomes visible after `move` begins stops the agent at the last
  reachable node and records `route_interruptions`; it is not an agent fault.
- A later move creates verified replanning evidence only if its chosen path
  avoids an active blocked edge that the normal shortest path would use.
- Trying an already visible blocked edge is an environment violation.
- `trace_feasibility` uses only environment/state-transition violations.
  `goal_completion` and `goal_drift` remain separate.

Eight action/movement tests and one API transport-safety test pass. The
deterministic utility baseline reaches goal completion 1.0 and feasibility 1.0
on all 12 scenarios, including both mid-route disruption scenarios.

## Experiment Matrix

- Model: `gpt-5.4-mini`, temperature 0.
- Decision layers: GATSim, SOTOPIA, Generative Agents, and AgentSociety.
- Scenarios: mid-route commute block, closed study replacement, school pickup
  social detour, and meeting wait trap.
- Repeats: 3; 48 provider-backed traces total.
- Scoring: deterministic verifier only; no second-pass LLM judge.
- Integration level: verified adapted official decision layers, not native full
  framework backends.

## Main Results

| Adapter | Goal | Feasibility | Replan on commute | Calls/trace | Tokens/trace |
|---|---:|---:|---:|---:|---:|
| GATSim | 0.788 +/- 0.277 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.667 | 15,171 |
| Generative Agents | 0.742 +/- 0.182 | 0.734 +/- 0.260 | 0.000 +/- 0.000 | 4.667 | 27,392 |
| AgentSociety | 0.692 +/- 0.186 | 0.714 +/- 0.286 | 0.333 +/- 0.577 | 6.500 | 45,108 |
| SOTOPIA | 0.521 +/- 0.137 | 0.875 +/- 0.226 | 0.667 +/- 0.577 | 5.167 | 34,395 |

All 48 traces have complete provider token usage. Every successful replanning
condition has concrete `normal_path`, `chosen_path`, and `avoided_edges`
evidence; no adapter can self-report replanning success.

## Scenario Findings

### Mid-route commute block

GATSim reaches goal 1.0, feasibility 1.0, and verified replanning 1.0 in all
three repeats. SOTOPIA produces a legal trace in all repeats but replans in two
of three. AgentSociety replans once. Generative Agents never produces a
verified detour and has mean goal completion 0.533.

### Closed study replacement

GATSim is the only adapter with goal and feasibility both 1.0. AgentSociety and
Generative Agents repeatedly produce paid-place or state-transition failures;
their mean feasibility is 0.298 and 0.362. This is the clearest action-evidence
stress test in the current set.

### Meeting wait trap

Generative Agents performs best on the goal (0.933) with feasibility 1.0.
GATSim remains perfectly legal but completes only 0.35 of the weighted goal.
This is important: a legal city trace is not necessarily an agentic one.

### School pickup social detour

GATSim and Generative Agents reach goal 0.8; SOTOPIA reaches only 0.35 while
remaining feasible. Again, incompletion and impossibility are different failure
modes.

## Interpretation

The experiment supports the CityAgency story more strongly than a simple
architecture leaderboard. The benchmark exposes at least three distinct
outcomes:

1. feasible and complete;
2. feasible but intention-incomplete;
3. infeasible because the trace violates city state or resource constraints.

It also shows a meaningful cost dimension. AgentSociety uses about three times
GATSim's tokens per trace while achieving lower completion and feasibility in
this matrix. This is relevant to large-scale urban simulation, where per-agent
decision cost limits population size and horizon length.

## Reliability And Caveats

The first attempt completed two repeats and then hit a provider timeout. The
toolchain was upgraded with sanitized transport errors, per-trace checkpoints,
and `--resume`; the third repeat then completed without rerunning the first two.

These results use one model, four scenarios, and three repeats. They do not
establish universal framework rankings. The adapters preserve verified official
decision surfaces but do not run each framework's full native world backend.
Human auditing and native integrations remain necessary.

## Next Step

Calibrate the deterministic evidence labels with a blinded human audit, then
expand the scenario set around feasible-but-incomplete behavior. In parallel,
run independent traces concurrently while preserving serial decisions within
each trace, so larger matrices remain practical.

Archive:
`results/cityintent_v03/external_frameworks_4x4x3_gpt54mini_2026-07-01/`
