# CityIntent v0 Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_direct_actor` | 24 | 0.921 +/- 0.168 | 0.930 +/- 0.108 | 0.914 +/- 0.179 | 1.000 +/- 0.000 | 0.835 +/- 0.111 | 0.513 +/- 0.236 | 0.322 +/- 0.165 | 0.070 +/- 0.108 |
| `api_llm_plan_then_act` | 24 | 0.963 +/- 0.105 | 0.958 +/- 0.141 | 0.931 +/- 0.190 | 1.000 +/- 0.000 | 0.930 +/- 0.060 | 0.846 +/- 0.165 | 0.085 +/- 0.111 | 0.042 +/- 0.141 |
| `api_llm_reactive_replanner` | 24 | 0.938 +/- 0.169 | 0.875 +/- 0.338 | 0.875 +/- 0.338 | 0.000 +/- 0.000 | 0.898 +/- 0.120 | 0.813 +/- 0.219 | 0.087 +/- 0.109 | 0.125 +/- 0.338 |
| `utility_planner` | 24 | 0.906 +/- 0.178 | 0.875 +/- 0.338 | 0.844 +/- 0.336 | 0.000 +/- 0.000 | 0.820 +/- 0.153 | 0.619 +/- 0.260 | 0.202 +/- 0.178 | 0.125 +/- 0.338 |

## Diagnostic Metrics

| Agent | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|
| `api_llm_direct_actor` | 0.806 +/- 0.270 | 0.917 +/- 0.282 | 0.750 +/- 0.452 | 0.167 +/- 0.381 | 0.042 +/- 0.204 |
| `api_llm_plan_then_act` | 0.865 +/- 0.255 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `api_llm_reactive_replanner` | 0.911 +/- 0.241 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `utility_planner` | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.750 +/- 0.452 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Goal | Feasibility |
|---|---|---:|---:|---:|---:|
| `avoid_crowd_event` | `api_llm_direct_actor` | 0.453 +/- 0.342 | 0.360 +/- 0.338 | 1.000 +/- 0.000 | 0.933 +/- 0.115 |
| `unexpected_friend_encounter` | `api_llm_direct_actor` | 0.453 +/- 0.081 | 0.180 +/- 0.100 | 0.650 +/- 0.173 | 0.875 +/- 0.125 |
| `budget_errand_chain` | `api_llm_direct_actor` | 0.423 +/- 0.040 | 0.367 +/- 0.046 | 1.000 +/- 0.000 | 0.783 +/- 0.029 |
| `unexpected_friend_encounter` | `utility_planner` | 0.420 +/- 0.183 | 0.227 +/- 0.092 | 0.750 +/- 0.000 | 1.000 +/- 0.000 |
| `commute_disruption` | `utility_planner` | 0.343 +/- 0.257 | 0.343 +/- 0.091 | 0.500 +/- 0.000 | 0.000 +/- 0.000 |
| `avoid_crowd_event` | `utility_planner` | 0.327 +/- 0.058 | 0.433 +/- 0.023 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `conflicting_social_obligation` | `api_llm_direct_actor` | 0.310 +/- 0.082 | 0.593 +/- 0.064 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `avoid_crowd_event` | `api_llm_reactive_replanner` | 0.300 +/- 0.017 | 0.327 +/- 0.129 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `lunch_meeting_time_pressure` | `api_llm_direct_actor` | 0.287 +/- 0.127 | 0.540 +/- 0.208 | 0.883 +/- 0.202 | 0.958 +/- 0.072 |
| `memory_dependent_place_choice` | `api_llm_direct_actor` | 0.277 +/- 0.110 | 0.667 +/- 0.117 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `unexpected_friend_encounter` | `api_llm_plan_then_act` | 0.257 +/- 0.057 | 0.593 +/- 0.046 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `closed_poi_replacement` | `api_llm_direct_actor` | 0.230 +/- 0.066 | 0.683 +/- 0.055 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Rate/trace |
|---|---|---:|---:|
| `api_llm_direct_actor` | `done_state_loop` | 4 | 0.167 |
| `api_llm_direct_actor` | `goal_drift` | 2 | 0.083 |
| `api_llm_direct_actor` | `money_budget_failure` | 2 | 0.083 |
| `api_llm_direct_actor` | `social_derailment` | 1 | 0.042 |
| `api_llm_plan_then_act` | `closed_place_action` | 2 | 0.083 |
| `api_llm_reactive_replanner` | `impossible_route` | 3 | 0.125 |
| `utility_planner` | `impossible_route` | 3 | 0.125 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
