# CityIntent Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 18 | 0.905 +/- 0.187 | 0.900 +/- 0.194 | 0.976 +/- 0.048 | 0.887 +/- 0.219 |  | 0.907 +/- 0.056 | 0.681 +/- 0.220 | 0.227 +/- 0.207 | 0.024 +/- 0.048 |
| `api_llm_react_tool_policy` | 18 | 0.797 +/- 0.231 | 0.853 +/- 0.166 | 0.994 +/- 0.024 | 0.850 +/- 0.172 |  | 0.892 +/- 0.078 | 0.655 +/- 0.204 | 0.237 +/- 0.155 | 0.006 +/- 0.024 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 0.893 +/- 0.207 |  | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.843 +/- 0.336 | 0.000 +/- 0.000 | 0.111 +/- 0.323 |
| `api_llm_react_tool_policy` | 0.944 +/- 0.236 |  | 1.000 +/- 0.000 | 0.944 +/- 0.236 | 0.861 +/- 0.287 | 0.000 +/- 0.000 | 0.444 +/- 0.511 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 1.000 +/- 0.000 | 19.400 +/- 4.099 | 9015.444 +/- 646.443 |
| `api_llm_react_tool_policy` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 9.111 +/- 2.826 | 90.457 +/- 44.236 | 86193.444 +/- 28274.440 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `hard_full_evening_chain` | `api_llm_react_tool_policy` | 0.377 +/- 0.055 | 0.417 +/- 0.032 | 0.643 +/- 0.124 | 0.650 +/- 0.087 | 0.967 +/- 0.058 |
| `hard_three_meeting_relay` | `api_llm_plan_and_execute` | 0.350 +/- 0.357 | 0.573 +/- 0.332 | 0.889 +/- 0.192 | 0.867 +/- 0.231 | 0.974 +/- 0.044 |
| `hard_stale_plan_override` | `api_llm_react_tool_policy` | 0.347 +/- 0.200 | 0.540 +/- 0.208 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_budget_entangled_meet` | `api_llm_react_tool_policy` | 0.287 +/- 0.110 | 0.600 +/- 0.171 | 0.641 +/- 0.222 | 0.767 +/- 0.144 | 1.000 +/- 0.000 |
| `hard_budget_entangled_meet` | `api_llm_plan_and_execute` | 0.267 +/- 0.100 | 0.607 +/- 0.190 | 0.872 +/- 0.222 | 0.867 +/- 0.231 | 0.970 +/- 0.053 |
| `hard_overlapping_windows` | `api_llm_plan_and_execute` | 0.253 +/- 0.336 | 0.690 +/- 0.357 | 0.833 +/- 0.289 | 0.833 +/- 0.289 | 0.952 +/- 0.083 |
| `hard_deadline_then_meet` | `api_llm_plan_and_execute` | 0.223 +/- 0.190 | 0.673 +/- 0.234 | 0.833 +/- 0.289 | 0.833 +/- 0.289 | 0.958 +/- 0.072 |
| `hard_three_meeting_relay` | `api_llm_react_tool_policy` | 0.207 +/- 0.136 | 0.747 +/- 0.151 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_overlapping_windows` | `api_llm_react_tool_policy` | 0.187 +/- 0.031 | 0.680 +/- 0.087 | 0.500 +/- 0.000 | 0.700 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_stale_plan_override` | `api_llm_plan_and_execute` | 0.180 +/- 0.113 | 0.760 +/- 0.106 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_full_evening_chain` | `api_llm_plan_and_execute` | 0.087 +/- 0.074 | 0.780 +/- 0.147 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_deadline_then_meet` | `api_llm_react_tool_policy` | 0.017 +/- 0.006 | 0.947 +/- 0.015 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `api_llm_plan_and_execute` | `invalid_state_transition` | 4 | 0.222 |
| `api_llm_plan_and_execute` | `social_derailment` | 2 | 0.111 |
| `api_llm_react_tool_policy` | `goal_drift` | 4 | 0.222 |
| `api_llm_react_tool_policy` | `money_budget_failure` | 1 | 0.056 |
| `api_llm_react_tool_policy` | `social_derailment` | 8 | 0.444 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
