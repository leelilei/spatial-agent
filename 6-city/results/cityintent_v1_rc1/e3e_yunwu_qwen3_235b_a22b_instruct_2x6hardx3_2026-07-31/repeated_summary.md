# CityIntent Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 18 | 0.821 +/- 0.238 | 0.828 +/- 0.224 | 0.960 +/- 0.064 | 0.806 +/- 0.254 |  | 0.862 +/- 0.094 | 0.538 +/- 0.172 | 0.323 +/- 0.136 | 0.040 +/- 0.064 |
| `api_llm_react_tool_policy` | 18 | 0.787 +/- 0.269 | 0.797 +/- 0.232 | 0.945 +/- 0.136 | 0.777 +/- 0.262 |  | 0.898 +/- 0.059 | 0.618 +/- 0.171 | 0.280 +/- 0.137 | 0.055 +/- 0.136 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 0.841 +/- 0.232 |  | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.732 +/- 0.388 | 0.000 +/- 0.000 | 0.278 +/- 0.461 |
| `api_llm_react_tool_policy` | 0.782 +/- 0.389 |  | 1.000 +/- 0.000 | 0.833 +/- 0.383 | 0.861 +/- 0.287 | 0.056 +/- 0.236 | 0.500 +/- 0.514 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 1.000 +/- 0.000 | 20.021 +/- 4.100 | 2923.722 +/- 347.970 |
| `api_llm_react_tool_policy` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 9.833 +/- 2.358 | 64.253 +/- 16.154 | 36750.944 +/- 10715.943 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `hard_overlapping_windows` | `api_llm_plan_and_execute` | 0.483 +/- 0.142 | 0.327 +/- 0.101 | 0.500 +/- 0.000 | 0.500 +/- 0.000 | 0.852 +/- 0.064 |
| `hard_stale_plan_override` | `api_llm_react_tool_policy` | 0.427 +/- 0.120 | 0.427 +/- 0.086 | 0.667 +/- 0.577 | 0.733 +/- 0.462 | 0.810 +/- 0.330 |
| `hard_budget_entangled_meet` | `api_llm_plan_and_execute` | 0.397 +/- 0.078 | 0.400 +/- 0.017 | 0.538 +/- 0.133 | 0.600 +/- 0.000 | 0.933 +/- 0.058 |
| `hard_overlapping_windows` | `api_llm_react_tool_policy` | 0.353 +/- 0.035 | 0.513 +/- 0.081 | 0.500 +/- 0.000 | 0.700 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_three_meeting_relay` | `api_llm_plan_and_execute` | 0.353 +/- 0.180 | 0.443 +/- 0.105 | 0.889 +/- 0.192 | 0.867 +/- 0.231 | 0.976 +/- 0.041 |
| `hard_full_evening_chain` | `api_llm_react_tool_policy` | 0.320 +/- 0.026 | 0.567 +/- 0.012 | 0.786 +/- 0.000 | 0.550 +/- 0.000 | 0.900 +/- 0.000 |
| `hard_budget_entangled_meet` | `api_llm_react_tool_policy` | 0.310 +/- 0.131 | 0.590 +/- 0.154 | 0.769 +/- 0.000 | 0.800 +/- 0.087 | 0.963 +/- 0.064 |
| `hard_deadline_then_meet` | `api_llm_plan_and_execute` | 0.287 +/- 0.055 | 0.647 +/- 0.070 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_full_evening_chain` | `api_llm_plan_and_execute` | 0.220 +/- 0.075 | 0.707 +/- 0.081 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_three_meeting_relay` | `api_llm_react_tool_policy` | 0.210 +/- 0.040 | 0.713 +/- 0.031 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_stale_plan_override` | `api_llm_plan_and_execute` | 0.200 +/- 0.026 | 0.707 +/- 0.085 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_deadline_then_meet` | `api_llm_react_tool_policy` | 0.060 +/- 0.030 | 0.900 +/- 0.030 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `api_llm_plan_and_execute` | `goal_drift` | 1 | 0.056 |
| `api_llm_plan_and_execute` | `invalid_state_transition` | 6 | 0.333 |
| `api_llm_plan_and_execute` | `social_derailment` | 5 | 0.278 |
| `api_llm_plan_and_execute` | `time_budget_failure` | 1 | 0.056 |
| `api_llm_react_tool_policy` | `done_state_loop` | 1 | 0.056 |
| `api_llm_react_tool_policy` | `goal_drift` | 3 | 0.167 |
| `api_llm_react_tool_policy` | `invalid_state_transition` | 5 | 0.278 |
| `api_llm_react_tool_policy` | `money_budget_failure` | 3 | 0.167 |
| `api_llm_react_tool_policy` | `social_derailment` | 9 | 0.500 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
