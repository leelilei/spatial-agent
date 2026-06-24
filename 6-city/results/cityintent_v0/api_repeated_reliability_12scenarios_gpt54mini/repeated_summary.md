# CityIntent v0 Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_direct_actor` | 36 | 0.832 +/- 0.233 | 0.873 +/- 0.185 | 0.790 +/- 0.272 | 0.833 +/- 0.408 | 0.805 +/- 0.154 | 0.500 +/- 0.256 | 0.305 +/- 0.169 | 0.127 +/- 0.185 |
| `api_llm_plan_then_act` | 36 | 0.918 +/- 0.141 | 0.906 +/- 0.221 | 0.843 +/- 0.263 | 1.000 +/- 0.000 | 0.903 +/- 0.104 | 0.784 +/- 0.249 | 0.120 +/- 0.192 | 0.094 +/- 0.221 |
| `api_llm_reactive_replanner` | 36 | 0.913 +/- 0.171 | 0.822 +/- 0.379 | 0.799 +/- 0.380 | 0.500 +/- 0.548 | 0.883 +/- 0.102 | 0.718 +/- 0.276 | 0.167 +/- 0.218 | 0.178 +/- 0.379 |
| `utility_planner` | 36 | 0.850 +/- 0.216 | 0.750 +/- 0.439 | 0.713 +/- 0.425 | 0.000 +/- 0.000 | 0.756 +/- 0.197 | 0.508 +/- 0.324 | 0.248 +/- 0.209 | 0.250 +/- 0.439 |

## Diagnostic Metrics

| Agent | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|
| `api_llm_direct_actor` | 0.804 +/- 0.273 | 0.972 +/- 0.167 | 0.667 +/- 0.383 | 0.222 +/- 0.422 | 0.083 +/- 0.280 |
| `api_llm_plan_then_act` | 0.869 +/- 0.238 | 0.917 +/- 0.280 | 0.778 +/- 0.352 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `api_llm_reactive_replanner` | 0.902 +/- 0.229 | 0.972 +/- 0.167 | 0.861 +/- 0.230 | 0.028 +/- 0.167 | 0.000 +/- 0.000 |
| `utility_planner` | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.667 +/- 0.383 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Goal | Feasibility |
|---|---|---:|---:|---:|---:|
| `meeting_wait_trap` | `api_llm_direct_actor` | 0.547 +/- 0.110 | 0.227 +/- 0.092 | 0.550 +/- 0.000 | 1.000 +/- 0.000 |
| `unexpected_friend_encounter` | `api_llm_direct_actor` | 0.527 +/- 0.130 | 0.153 +/- 0.031 | 0.450 +/- 0.000 | 0.750 +/- 0.000 |
| `meeting_wait_trap` | `utility_planner` | 0.467 +/- 0.219 | 0.187 +/- 0.162 | 0.800 +/- 0.000 | 1.000 +/- 0.000 |
| `meeting_wait_trap` | `api_llm_reactive_replanner` | 0.437 +/- 0.040 | 0.377 +/- 0.038 | 0.700 +/- 0.260 | 1.000 +/- 0.000 |
| `meeting_wait_trap` | `api_llm_plan_then_act` | 0.400 +/- 0.087 | 0.407 +/- 0.121 | 0.700 +/- 0.260 | 1.000 +/- 0.000 |
| `avoid_crowd_event` | `utility_planner` | 0.393 +/- 0.212 | 0.333 +/- 0.300 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `budget_errand_chain` | `api_llm_direct_actor` | 0.390 +/- 0.050 | 0.370 +/- 0.026 | 1.000 +/- 0.000 | 0.813 +/- 0.056 |
| `memory_dependent_place_choice` | `api_llm_plan_then_act` | 0.357 +/- 0.531 | 0.610 +/- 0.528 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `unexpected_friend_encounter` | `api_llm_reactive_replanner` | 0.357 +/- 0.318 | 0.460 +/- 0.333 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `memory_dependent_place_choice` | `api_llm_reactive_replanner` | 0.343 +/- 0.534 | 0.627 +/- 0.543 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `unexpected_friend_encounter` | `utility_planner` | 0.343 +/- 0.078 | 0.140 +/- 0.125 | 0.750 +/- 0.000 | 1.000 +/- 0.000 |
| `closed_study_spot_replacement` | `utility_planner` | 0.330 +/- 0.546 | 0.630 +/- 0.546 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Rate/trace |
|---|---|---:|---:|
| `api_llm_direct_actor` | `closed_place_action` | 4 | 0.111 |
| `api_llm_direct_actor` | `done_state_loop` | 8 | 0.222 |
| `api_llm_direct_actor` | `goal_drift` | 4 | 0.111 |
| `api_llm_direct_actor` | `impossible_route` | 1 | 0.028 |
| `api_llm_direct_actor` | `money_budget_failure` | 1 | 0.028 |
| `api_llm_direct_actor` | `social_derailment` | 3 | 0.083 |
| `api_llm_direct_actor` | `time_budget_failure` | 1 | 0.028 |
| `api_llm_plan_then_act` | `closed_place_action` | 5 | 0.139 |
| `api_llm_plan_then_act` | `money_budget_failure` | 3 | 0.083 |
| `api_llm_reactive_replanner` | `closed_place_action` | 3 | 0.083 |
| `api_llm_reactive_replanner` | `done_state_loop` | 1 | 0.028 |
| `api_llm_reactive_replanner` | `impossible_route` | 3 | 0.083 |
| `api_llm_reactive_replanner` | `money_budget_failure` | 1 | 0.028 |
| `utility_planner` | `closed_place_action` | 3 | 0.083 |
| `utility_planner` | `impossible_route` | 6 | 0.167 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
