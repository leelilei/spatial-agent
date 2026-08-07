# CityIntent Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 18 | 0.556 +/- 0.217 | 0.661 +/- 0.168 | 0.960 +/- 0.061 | 0.641 +/- 0.188 |  | 0.854 +/- 0.064 | 0.478 +/- 0.179 | 0.377 +/- 0.179 | 0.040 +/- 0.061 |
| `api_llm_react_tool_policy` | 18 | 0.932 +/- 0.166 | 0.958 +/- 0.100 | 1.000 +/- 0.000 | 0.958 +/- 0.100 |  | 0.928 +/- 0.038 | 0.722 +/- 0.216 | 0.207 +/- 0.206 | 0.000 +/- 0.000 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 0.833 +/- 0.243 |  | 0.951 +/- 0.112 | 1.000 +/- 0.000 | 0.481 +/- 0.370 | 0.000 +/- 0.000 | 0.722 +/- 0.461 |
| `api_llm_react_tool_policy` | 1.000 +/- 0.000 |  | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.944 +/- 0.162 | 0.000 +/- 0.000 | 0.167 +/- 0.383 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 1.000 +/- 0.000 | 13.967 +/- 2.692 | 3193.278 +/- 357.017 |
| `api_llm_react_tool_policy` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 9.611 +/- 2.547 | 60.954 +/- 20.151 | 39285.778 +/- 12455.793 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `hard_three_meeting_relay` | `api_llm_plan_and_execute` | 0.513 +/- 0.241 | 0.437 +/- 0.242 | 0.556 +/- 0.193 | 0.533 +/- 0.115 | 0.897 +/- 0.044 |
| `hard_deadline_then_meet` | `api_llm_plan_and_execute` | 0.447 +/- 0.031 | 0.367 +/- 0.046 | 0.500 +/- 0.000 | 0.700 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_overlapping_windows` | `api_llm_plan_and_execute` | 0.400 +/- 0.243 | 0.477 +/- 0.263 | 0.500 +/- 0.000 | 0.500 +/- 0.000 | 0.863 +/- 0.010 |
| `hard_budget_entangled_meet` | `api_llm_react_tool_policy` | 0.393 +/- 0.348 | 0.560 +/- 0.356 | 0.923 +/- 0.133 | 0.950 +/- 0.087 | 1.000 +/- 0.000 |
| `hard_stale_plan_override` | `api_llm_plan_and_execute` | 0.363 +/- 0.155 | 0.460 +/- 0.144 | 0.333 +/- 0.000 | 0.600 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_stale_plan_override` | `api_llm_react_tool_policy` | 0.357 +/- 0.133 | 0.533 +/- 0.112 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_full_evening_chain` | `api_llm_plan_and_execute` | 0.283 +/- 0.217 | 0.593 +/- 0.258 | 0.857 +/- 0.124 | 0.900 +/- 0.087 | 1.000 +/- 0.000 |
| `hard_budget_entangled_meet` | `api_llm_plan_and_execute` | 0.253 +/- 0.103 | 0.533 +/- 0.092 | 0.590 +/- 0.355 | 0.733 +/- 0.231 | 1.000 +/- 0.000 |
| `hard_overlapping_windows` | `api_llm_react_tool_policy` | 0.180 +/- 0.209 | 0.717 +/- 0.241 | 0.667 +/- 0.289 | 0.800 +/- 0.173 | 1.000 +/- 0.000 |
| `hard_deadline_then_meet` | `api_llm_react_tool_policy` | 0.173 +/- 0.157 | 0.790 +/- 0.151 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_full_evening_chain` | `api_llm_react_tool_policy` | 0.100 +/- 0.069 | 0.837 +/- 0.098 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_three_meeting_relay` | `api_llm_react_tool_policy` | 0.040 +/- 0.010 | 0.897 +/- 0.029 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `api_llm_plan_and_execute` | `goal_drift` | 8 | 0.444 |
| `api_llm_plan_and_execute` | `invalid_state_transition` | 7 | 0.389 |
| `api_llm_plan_and_execute` | `social_derailment` | 13 | 0.722 |
| `api_llm_react_tool_policy` | `goal_drift` | 2 | 0.111 |
| `api_llm_react_tool_policy` | `social_derailment` | 3 | 0.167 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
