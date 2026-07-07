# CityIntent Paper-Backed Baselines 2x6x3 Social Matrix

Date: 2026-07-07

## Question

Do paper-backed execution-agent policies solve the same social-outcome family
that exposed legal-but-ineffective traces in the adapted city/social simulation
baselines?

This run tests whether the social-outcome failures are mainly caused by the
CityIntent environment and scoring protocol, or whether they reflect meaningful
architecture differences in how agents turn plausible plans into verified urban
traces.

## Setup

- Model: provider-backed `gpt-5.4-mini`.
- Judge: provider-backed `gpt-5.4-mini`.
- Agents:
  - `api_llm_react_tool_policy`
  - `api_llm_plan_and_execute`
- Scenarios:
  - `social_copresence_open_meet`
  - `social_copresence_message_gated`
  - `social_copresence_event_window`
  - `social_copresence_two_party`
  - `social_copresence_with_errand`
  - `social_copresence_decoy_location`
- Repeats: 3 per agent-scenario cell.
- Archive:
  `results/cityintent_v1_rc1/paper_backed_baselines_2x6socialx3_gpt54mini_2026-07-07/`

Command:

```powershell
python 6-city/benchmarks/cityintent_v0/tools/run_repeated_experiment.py `
  --repeats 3 `
  --agents api_llm_react_tool_policy,api_llm_plan_and_execute `
  --scenario-ids social_copresence_open_meet,social_copresence_message_gated,social_copresence_event_window,social_copresence_two_party,social_copresence_with_errand,social_copresence_decoy_location `
  --llm-config 6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json `
  --judge-config 6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json `
  --output-dir 6-city/results/cityintent_v1_rc1/paper_backed_baselines_2x6socialx3_gpt54mini_2026-07-07 `
  --skip-existing
```

The archive contains 36 raw traces and 36 judged traces.

## Main Agent Table

| Agent | n | Task | Feasibility | Social approp. | Accepted co-presence | Full social traces | Joint success | Face plaus. | Trace believ. | Calls | Tokens |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_react_tool_policy` | 18 | 1.000 | 0.958 | 1.000 | 21/21 | 1.000 | 0.833 | 0.876 | 0.663 | 7.278 | 59526 |
| `api_llm_plan_and_execute` | 18 | 0.917 | 0.957 | 0.917 | 18/21 | 0.833 | 0.667 | 0.910 | 0.664 | 1.000 | 7172 |

## Scenario Diagnostics

| Scenario | Plan-and-Execute outcome rate | ReAct outcome rate | Main reading |
|---|---:|---:|---|
| `social_copresence_open_meet` | 1.000 | 1.000 | Both solve the simplest open meeting. |
| `social_copresence_message_gated` | 1.000 | 1.000 | Both can satisfy explicit messaging before meeting. |
| `social_copresence_event_window` | 1.000 | 1.000 | Both respect the event window in all repeats. |
| `social_copresence_two_party` | 0.500 | 1.000 | Two-party co-presence is the clearest architecture separator. |
| `social_copresence_with_errand` | 1.000 | 1.000 | Both complete social outcome, but feasibility drops. |
| `social_copresence_decoy_location` | 1.000 | 1.000 | Both avoid the decoy and reach the intended target. |

## Failure Signatures

| Agent | Main failures | Count pattern |
|---|---|---|
| `api_llm_plan_and_execute` | `social_derailment`, `money_budget_failure`, `time_budget_failure`, one `goal_drift`, one `invalid_state_transition` | Social derailment appears in 3/18 traces and aligns with the two-party weakness. |
| `api_llm_react_tool_policy` | `done_state_loop`, `invalid_state_transition`, `money_budget_failure` | Social outcomes are complete, but some traces still over-continue or mishandle paid/terminal states. |

## Comparison To Four Adapted Decision Layers

The previous 4-adapter social-outcome family produced 21 required co-presence
outcomes per adapter:

| Adapter family | Accepted co-presence outcomes | Interpretation |
|---|---:|---|
| GATSim adapted decision layer | 15/21 | Strongest prior city-simulation-derived baseline. |
| AgentSociety adapted decision layer | 4/21 | Some plan structure, weak verified social execution. |
| Generative Agents adapted planner | 2/21 | Believable planning does not reliably become co-presence. |
| SOTOPIA-style `LLMAgent` adapter | 0/21 | Legal or plausible dialogue-style traces can still miss verified urban meetings. |
| ReAct-style tool-use policy | 21/21 | Interleaved observation/action discipline closes the social-outcome gap on this family. |
| Plan-and-Execute policy | 18/21 | Stronger than adapted framework baselines, but brittle on simultaneous two-party evidence. |

## Takeaway

This run strengthens the CityAgency thesis. The social-outcome family is not
unwinnable, and the scoring protocol is not merely punishing all LLM agents.
Paper-backed execution policies can satisfy the same typed city evidence that
adapted social/city simulation decision layers often miss.

The result also sharpens the paper story. The benchmark should not only ask
whether an agent writes a plausible urban plan. It should ask whether a decision
architecture can produce continuous, verifiable traces: enter the right place,
at the right time, with the right person, under resource and state constraints.

The remaining failures are useful rather than fatal. ReAct buys social evidence
at substantially higher call/token cost and still shows done-loop and paid-state
issues. Plan-and-Execute is cheaper and face-plausible, but loses simultaneous
co-presence in the two-party case. These are exactly the kinds of mechanism
differences CityAgency can make visible.

## Next Step

For the paper table, combine:

```text
4 adapted official decision layers
+ 2 paper-backed execution baselines
x 6 social-outcome scenarios
x 3 repeats
```

Then rerun the same archive with the stronger judge or a small human audit
sample. The deterministic co-presence outcome should remain the anchor metric;
LLM believability scores should be reported as secondary diagnostics.
