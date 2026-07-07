# CityIntent Unified Six-Policy Social Table

Date: 2026-07-08

## Scope

This table combines the four adapted official decision-layer social matrix with the two paper-backed execution baselines. All rows use the same six oracle-winnable `social_outcome` scenarios, three repeats per scenario-policy cell, the same typed CityIntent executor, and deterministic environment-owned co-presence evidence.

Source archives:

- `6-city/results/cityintent_v1_rc1/external_frameworks_4x6socialx1_gpt54mini_2026-07-06`
- `6-city/results/cityintent_v1_rc1/paper_backed_baselines_2x6socialx3_gpt54mini_2026-07-07`

## Main Table

| Policy | Family | Accepted co-presence | Outcome rate | Full social | Social pass^3 | Full task | Fully feasible | Joint success | Legal but ineffective | Plausible but unverified | Calls | Tokens |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ReAct-style tool-use policy | paper_backed_execution_baseline | 21/21 | 1.000 | 1.000 | 1.000 | 1.000 | 0.833 | 0.833 | 0.000 | 0.000 | 7.278 | 59526 |
| Plan-and-Execute policy | paper_backed_execution_baseline | 18/21 | 0.857 | 0.833 | 0.833 | 0.833 | 0.722 | 0.667 | 0.056 | 0.167 | 1.000 | 7172 |
| GATSim adapted planner | adapted_official_decision_layer | 15/21 | 0.714 | 0.667 | 0.667 | 0.667 | 0.500 | 0.500 | 0.000 | 0.278 | 2.444 | 23155 |
| AgentSociety plan-block adapter | adapted_official_decision_layer | 4/21 | 0.190 | 0.222 | 0.167 | 0.222 | 0.278 | 0.167 | 0.111 | 0.778 | 6.889 | 49050 |
| Generative Agents adapted planner | adapted_official_decision_layer | 2/21 | 0.095 | 0.111 | 0.000 | 0.056 | 0.056 | 0.000 | 0.056 | 0.667 | 5.111 | 30974 |
| SOTOPIA-style LLMAgent adapter | adapted_official_decision_layer | 0/21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.611 | 0.000 | 0.611 | 0.889 | 5.778 | 39753 |

`Social pass^3` is the fraction of scenario-policy cells where all three repeats accept all required co-presence outcomes.

## Evidence-Gap Diagnostics

| Policy | Mean task | Mean feasibility | Mean face plausibility | Message without meeting | Interact attempt without success | Target entry without meeting |
|---|---:|---:|---:|---:|---:|---:|
| ReAct-style tool-use policy | 1.000 | 0.958 | 0.876 | 0.000 | 0.000 | 0.000 |
| Plan-and-Execute policy | 0.917 | 0.957 | 0.910 | 0.000 | 0.167 | 0.167 |
| GATSim adapted planner | 0.667 | 0.819 | 0.776 | 0.000 | 0.333 | 0.333 |
| AgentSociety plan-block adapter | 0.325 | 0.615 | 0.903 | 0.333 | 0.333 | 0.611 |
| Generative Agents adapted planner | 0.220 | 0.666 | 0.772 | 0.333 | 0.056 | 0.722 |
| SOTOPIA-style LLMAgent adapter | 0.103 | 0.913 | 0.813 | 0.611 | 0.056 | 0.111 |

## Scenario Outcome Heatmap

| Scenario | ReAct-style tool-use policy | Plan-and-Execute policy | GATSim adapted planner | AgentSociety plan-block adapter | Generative Agents adapted planner | SOTOPIA-style LLMAgent adapter |
|---|---:|---:|---:|---:|---:|---:|
| `social_copresence_decoy_location` | 3/3 | 3/3 | 0/3 | 0/3 | 1/3 | 0/3 |
| `social_copresence_event_window` | 3/3 | 3/3 | 3/3 | 0/3 | 0/3 | 0/3 |
| `social_copresence_message_gated` | 3/3 | 3/3 | 0/3 | 0/3 | 0/3 | 0/3 |
| `social_copresence_open_meet` | 3/3 | 3/3 | 3/3 | 1/3 | 0/3 | 0/3 |
| `social_copresence_two_party` | 6/6 | 3/6 | 6/6 | 0/6 | 0/6 | 0/6 |
| `social_copresence_with_errand` | 3/3 | 3/3 | 3/3 | 3/3 | 1/3 | 0/3 |

## Dominant Failure Counts

| Policy | Top recorded failures |
|---|---|
| ReAct-style tool-use policy | done_state_loop=3, invalid_state_transition=3, money_budget_failure=3 |
| Plan-and-Execute policy | money_budget_failure=3, social_derailment=3, time_budget_failure=2 |
| GATSim adapted planner | invalid_state_transition=26, money_budget_failure=3, time_budget_failure=2 |
| AgentSociety plan-block adapter | money_budget_failure=30, invalid_state_transition=21, time_budget_failure=8 |
| Generative Agents adapted planner | money_budget_failure=26, impossible_route=14, invalid_state_transition=4 |
| SOTOPIA-style LLMAgent adapter | goal_drift=11, invalid_state_transition=9, done_state_loop=1 |

## Main Reading

The unified table strengthens the benchmark story. The six-scenario social family is not unwinnable: ReAct-style tool use completes 21/21 required co-presence outcomes, Plan-and-Execute completes 18/21, and GATSim completes 15/21. At the same time, the SOTOPIA-style LLMAgent adapter produces 0/21 accepted outcomes despite high feasibility and face plausibility. This is the core Plausible Plans, Impossible Traces pattern: plausible or legal behavior is not the same as verified urban agency.

The paper-backed execution baselines also add a useful ceiling. They show that the verifier can be satisfied by ordinary LLM-agent execution architectures, while exposing distinct costs and failure modes: ReAct is strongest but expensive and still shows terminal/paid-state issues; Plan-and-Execute is cheap and plausible but weakens on two-party simultaneous co-presence.
