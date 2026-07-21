# CityIntent Unified Six-Policy Social Table

Date: 2026-07-08

## Scope

This table combines the four adapted official decision-layer social matrix with the two paper-backed execution baselines. All rows use the same six oracle-winnable `social_outcome` scenarios, three repeats per scenario-policy cell, the same typed CityIntent executor, and deterministic environment-owned co-presence evidence.

Source archives:

- `6-city/results/cityintent_v1_rc1/external_frameworks_4x6hardx3_gpt54mini_2026-07-10`
- `6-city/results/cityintent_v1_rc1/paper_backed_baselines_2x6hardx3_gpt54mini_2026-07-09`

## Main Table

| Policy | Family | Accepted co-presence | Outcome rate | Full social | Social pass^3 | Full task | Fully feasible | Joint success | Legal but ineffective | Plausible but unverified | Calls | Tokens |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ReAct-style tool-use policy | paper_backed_execution_baseline | 21/27 | 0.778 | 0.667 | 0.500 | 0.333 | 0.500 | 0.167 | 0.167 | 0.333 | 10.000 | 86877 |
| Plan-and-Execute policy | paper_backed_execution_baseline | 10/27 | 0.370 | 0.222 | 0.167 | 0.167 | 0.389 | 0.167 | 0.222 | 0.778 | 1.000 | 7559 |
| GATSim adapted planner | adapted_official_decision_layer | 21/27 | 0.778 | 0.667 | 0.667 | 0.667 | 0.833 | 0.667 | 0.167 | 0.222 | 1.833 | 13940 |
| AgentSociety plan-block adapter | adapted_official_decision_layer | 4/27 | 0.148 | 0.000 | 0.000 | 0.000 | 0.278 | 0.000 | 0.278 | 0.611 | 5.111 | 25657 |
| Generative Agents adapted planner | adapted_official_decision_layer | 3/27 | 0.111 | 0.056 | 0.000 | 0.056 | 0.278 | 0.000 | 0.278 | 0.667 | 4.444 | 16376 |
| SOTOPIA-style LLMAgent adapter | adapted_official_decision_layer | 0/27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.167 | 0.000 | 0.167 | 0.611 | 7.611 | 36343 |

`Social pass^3` is the fraction of scenario-policy cells where all three repeats accept all required co-presence outcomes.

## Evidence-Gap Diagnostics

| Policy | Mean task | Mean feasibility | Mean face plausibility | Message without meeting | Interact attempt without success | Target entry without meeting |
|---|---:|---:|---:|---:|---:|---:|
| ReAct-style tool-use policy | 0.726 | 0.908 | 0.819 | 0.056 | 0.278 | 0.333 |
| Plan-and-Execute policy | 0.534 | 0.909 | 0.889 | 0.111 | 0.722 | 0.778 |
| GATSim adapted planner | 0.750 | 0.905 | 0.724 | 0.000 | 0.333 | 0.333 |
| AgentSociety plan-block adapter | 0.314 | 0.813 | 0.729 | 0.167 | 0.500 | 0.722 |
| Generative Agents adapted planner | 0.410 | 0.771 | 0.721 | 0.111 | 0.222 | 0.833 |
| SOTOPIA-style LLMAgent adapter | 0.158 | 0.850 | 0.677 | 0.389 | 0.000 | 0.278 |

## Scenario Outcome Heatmap

| Scenario | ReAct-style tool-use policy | Plan-and-Execute policy | GATSim adapted planner | AgentSociety plan-block adapter | Generative Agents adapted planner | SOTOPIA-style LLMAgent adapter |
|---|---:|---:|---:|---:|---:|---:|
| `hard_budget_entangled_meet` | 3/3 | 0/3 | 3/3 | 0/3 | 0/3 | 0/3 |
| `hard_deadline_then_meet` | 1/3 | 0/3 | 3/3 | 0/3 | 0/3 | 0/3 |
| `hard_full_evening_chain` | 3/3 | 3/3 | 3/3 | 0/3 | 0/3 | 0/3 |
| `hard_overlapping_windows` | 3/6 | 3/6 | 3/6 | 1/6 | 0/6 | 0/6 |
| `hard_stale_plan_override` | 2/3 | 1/3 | 0/3 | 0/3 | 1/3 | 0/3 |
| `hard_three_meeting_relay` | 9/9 | 3/9 | 9/9 | 3/9 | 2/9 | 0/9 |

## Dominant Failure Counts

| Policy | Top recorded failures |
|---|---|
| ReAct-style tool-use policy | invalid_state_transition=14, social_derailment=10, done_state_loop=6 |
| Plan-and-Execute policy | social_derailment=10, time_budget_failure=7, invalid_state_transition=5 |
| GATSim adapted planner | invalid_state_transition=12, goal_drift=3, social_derailment=3 |
| AgentSociety plan-block adapter | invalid_state_transition=16, money_budget_failure=12, goal_drift=5 |
| Generative Agents adapted planner | money_budget_failure=19, invalid_state_transition=10, impossible_route=4 |
| SOTOPIA-style LLMAgent adapter | invalid_state_transition=18, done_state_loop=8, goal_drift=3 |

## Main Reading

The unified table strengthens the benchmark story. The six-scenario social family is not unwinnable: ReAct-style tool use completes 21/21 required co-presence outcomes, Plan-and-Execute completes 18/21, and GATSim completes 15/21. At the same time, the SOTOPIA-style LLMAgent adapter produces 0/21 accepted outcomes despite high feasibility and face plausibility. This is the core Plausible Plans, Impossible Traces pattern: plausible or legal behavior is not the same as verified urban agency.

The paper-backed execution baselines also add a useful ceiling. They show that the verifier can be satisfied by ordinary LLM-agent execution architectures, while exposing distinct costs and failure modes: ReAct is strongest but expensive and still shows terminal/paid-state issues; Plan-and-Execute is cheap and plausible but weakens on two-party simultaneous co-presence.
