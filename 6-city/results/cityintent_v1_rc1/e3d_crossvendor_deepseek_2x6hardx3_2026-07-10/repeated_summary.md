# CityIntent Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 18 | 0.626 +/- 0.347 | 0.678 +/- 0.281 | 0.922 +/- 0.103 | 0.647 +/- 0.309 |  | 0.843 +/- 0.123 | 0.493 +/- 0.238 | 0.349 +/- 0.189 | 0.078 +/- 0.103 |
| `api_llm_react_tool_policy` | 18 | 0.856 +/- 0.204 | 0.889 +/- 0.136 | 0.986 +/- 0.044 | 0.878 +/- 0.150 |  | 0.861 +/- 0.085 | 0.564 +/- 0.188 | 0.297 +/- 0.137 | 0.014 +/- 0.044 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 0.758 +/- 0.250 |  | 0.996 +/- 0.017 | 1.000 +/- 0.000 | 0.509 +/- 0.455 | 0.000 +/- 0.000 | 0.333 +/- 0.485 |
| `api_llm_react_tool_policy` | 0.944 +/- 0.162 |  | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.917 +/- 0.192 | 0.000 +/- 0.000 | 0.389 +/- 0.502 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 1.000 +/- 0.000 | 39.998 +/- 40.203 | 3688.556 +/- 1890.788 |
| `api_llm_react_tool_policy` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 10.111 +/- 2.374 | 308.034 +/- 207.744 | 41799.833 +/- 12430.723 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `hard_deadline_then_meet` | `api_llm_plan_and_execute` | 0.537 +/- 0.119 | 0.347 +/- 0.110 | 0.500 +/- 0.000 | 0.567 +/- 0.115 | 0.905 +/- 0.083 |
| `hard_three_meeting_relay` | `api_llm_plan_and_execute` | 0.500 +/- 0.246 | 0.317 +/- 0.254 | 0.556 +/- 0.509 | 0.667 +/- 0.306 | 0.976 +/- 0.041 |
| `hard_stale_plan_override` | `api_llm_react_tool_policy` | 0.433 +/- 0.129 | 0.337 +/- 0.098 | 1.000 +/- 0.000 | 0.933 +/- 0.115 | 0.944 +/- 0.096 |
| `hard_overlapping_windows` | `api_llm_plan_and_execute` | 0.377 +/- 0.091 | 0.310 +/- 0.089 | 0.333 +/- 0.289 | 0.400 +/- 0.173 | 0.783 +/- 0.159 |
| `hard_full_evening_chain` | `api_llm_react_tool_policy` | 0.363 +/- 0.068 | 0.503 +/- 0.076 | 0.714 +/- 0.124 | 0.750 +/- 0.087 | 0.970 +/- 0.053 |
| `hard_budget_entangled_meet` | `api_llm_plan_and_execute` | 0.337 +/- 0.136 | 0.487 +/- 0.220 | 0.590 +/- 0.355 | 0.633 +/- 0.318 | 0.926 +/- 0.064 |
| `hard_overlapping_windows` | `api_llm_react_tool_policy` | 0.337 +/- 0.055 | 0.477 +/- 0.119 | 0.500 +/- 0.000 | 0.700 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_three_meeting_relay` | `api_llm_react_tool_policy` | 0.260 +/- 0.121 | 0.680 +/- 0.125 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_budget_entangled_meet` | `api_llm_react_tool_policy` | 0.250 +/- 0.182 | 0.600 +/- 0.231 | 0.923 +/- 0.133 | 0.950 +/- 0.087 | 1.000 +/- 0.000 |
| `hard_full_evening_chain` | `api_llm_plan_and_execute` | 0.200 +/- 0.111 | 0.760 +/- 0.092 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_stale_plan_override` | `api_llm_plan_and_execute` | 0.147 +/- 0.086 | 0.740 +/- 0.111 | 0.778 +/- 0.385 | 0.800 +/- 0.346 | 0.944 +/- 0.096 |
| `hard_deadline_then_meet` | `api_llm_react_tool_policy` | 0.137 +/- 0.076 | 0.787 +/- 0.103 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `api_llm_plan_and_execute` | `goal_drift` | 2 | 0.111 |
| `api_llm_plan_and_execute` | `invalid_state_transition` | 6 | 0.333 |
| `api_llm_plan_and_execute` | `social_derailment` | 6 | 0.333 |
| `api_llm_plan_and_execute` | `time_budget_failure` | 4 | 0.222 |
| `api_llm_react_tool_policy` | `goal_drift` | 3 | 0.167 |
| `api_llm_react_tool_policy` | `invalid_state_transition` | 2 | 0.111 |
| `api_llm_react_tool_policy` | `social_derailment` | 7 | 0.389 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
