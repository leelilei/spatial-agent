# CityIntent Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 18 | 0.534 +/- 0.267 | 0.603 +/- 0.208 | 0.909 +/- 0.080 | 0.559 +/- 0.234 |  | 0.889 +/- 0.068 | 0.544 +/- 0.171 | 0.345 +/- 0.157 | 0.091 +/- 0.080 |
| `api_llm_react_tool_policy` | 18 | 0.726 +/- 0.232 | 0.728 +/- 0.179 | 0.908 +/- 0.138 | 0.677 +/- 0.228 |  | 0.819 +/- 0.139 | 0.487 +/- 0.184 | 0.332 +/- 0.149 | 0.092 +/- 0.138 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 0.706 +/- 0.242 |  | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.417 +/- 0.397 | 0.000 +/- 0.000 | 0.556 +/- 0.511 |
| `api_llm_react_tool_policy` | 0.726 +/- 0.305 |  | 1.000 +/- 0.000 | 0.944 +/- 0.236 | 0.778 +/- 0.352 | 0.333 +/- 0.485 | 0.556 +/- 0.511 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 1.000 +/- 0.000 | 12.222 +/- 8.138 | 7559.000 +/- 264.520 |
| `api_llm_react_tool_policy` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 10.000 +/- 2.301 | 75.646 +/- 31.481 | 86877.389 +/- 21986.154 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `hard_full_evening_chain` | `api_llm_react_tool_policy` | 0.493 +/- 0.200 | 0.383 +/- 0.228 | 0.643 +/- 0.124 | 0.600 +/- 0.087 | 0.809 +/- 0.166 |
| `hard_stale_plan_override` | `api_llm_plan_and_execute` | 0.467 +/- 0.087 | 0.427 +/- 0.110 | 0.555 +/- 0.385 | 0.667 +/- 0.306 | 0.944 +/- 0.096 |
| `hard_budget_entangled_meet` | `api_llm_plan_and_execute` | 0.413 +/- 0.247 | 0.423 +/- 0.140 | 0.385 +/- 0.000 | 0.450 +/- 0.000 | 0.815 +/- 0.064 |
| `hard_overlapping_windows` | `api_llm_plan_and_execute` | 0.383 +/- 0.021 | 0.473 +/- 0.061 | 0.500 +/- 0.000 | 0.500 +/- 0.000 | 0.875 +/- 0.000 |
| `hard_stale_plan_override` | `api_llm_react_tool_policy` | 0.347 +/- 0.081 | 0.487 +/- 0.115 | 0.778 +/- 0.385 | 0.800 +/- 0.346 | 0.833 +/- 0.289 |
| `hard_deadline_then_meet` | `api_llm_react_tool_policy` | 0.317 +/- 0.120 | 0.420 +/- 0.140 | 0.667 +/- 0.289 | 0.600 +/- 0.173 | 0.888 +/- 0.013 |
| `hard_deadline_then_meet` | `api_llm_plan_and_execute` | 0.293 +/- 0.191 | 0.613 +/- 0.210 | 0.500 +/- 0.000 | 0.500 +/- 0.000 | 0.863 +/- 0.010 |
| `hard_overlapping_windows` | `api_llm_react_tool_policy` | 0.293 +/- 0.172 | 0.540 +/- 0.147 | 0.500 +/- 0.000 | 0.700 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_budget_entangled_meet` | `api_llm_react_tool_policy` | 0.283 +/- 0.059 | 0.453 +/- 0.239 | 0.769 +/- 0.000 | 0.800 +/- 0.087 | 0.963 +/- 0.064 |
| `hard_three_meeting_relay` | `api_llm_plan_and_execute` | 0.273 +/- 0.169 | 0.637 +/- 0.221 | 0.333 +/- 0.334 | 0.600 +/- 0.200 | 1.000 +/- 0.000 |
| `hard_three_meeting_relay` | `api_llm_react_tool_policy` | 0.260 +/- 0.205 | 0.637 +/- 0.250 | 1.000 +/- 0.000 | 0.867 +/- 0.115 | 0.953 +/- 0.041 |
| `hard_full_evening_chain` | `api_llm_plan_and_execute` | 0.240 +/- 0.125 | 0.693 +/- 0.132 | 0.929 +/- 0.124 | 0.900 +/- 0.173 | 0.958 +/- 0.072 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `api_llm_plan_and_execute` | `goal_drift` | 3 | 0.167 |
| `api_llm_plan_and_execute` | `invalid_state_transition` | 5 | 0.278 |
| `api_llm_plan_and_execute` | `money_budget_failure` | 1 | 0.056 |
| `api_llm_plan_and_execute` | `social_derailment` | 10 | 0.556 |
| `api_llm_plan_and_execute` | `time_budget_failure` | 7 | 0.389 |
| `api_llm_react_tool_policy` | `done_state_loop` | 6 | 0.333 |
| `api_llm_react_tool_policy` | `goal_drift` | 3 | 0.167 |
| `api_llm_react_tool_policy` | `invalid_state_transition` | 14 | 0.778 |
| `api_llm_react_tool_policy` | `money_budget_failure` | 1 | 0.056 |
| `api_llm_react_tool_policy` | `plausible_but_invalid_rationale` | 1 | 0.056 |
| `api_llm_react_tool_policy` | `social_derailment` | 10 | 0.556 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
