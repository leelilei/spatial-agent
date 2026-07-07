# CityIntent Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 18 | 0.917 +/- 0.192 | 0.894 +/- 0.173 | 0.957 +/- 0.074 | 0.866 +/- 0.210 |  | 0.910 +/- 0.073 | 0.664 +/- 0.218 | 0.246 +/- 0.182 | 0.043 +/- 0.074 |
| `api_llm_react_tool_policy` | 18 | 1.000 +/- 0.000 | 0.933 +/- 0.153 | 0.958 +/- 0.096 | 0.908 +/- 0.211 |  | 0.876 +/- 0.112 | 0.663 +/- 0.210 | 0.213 +/- 0.128 | 0.042 +/- 0.096 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 0.861 +/- 0.230 |  | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.917 +/- 0.192 | 0.000 +/- 0.000 | 0.167 +/- 0.383 |
| `api_llm_react_tool_policy` | 0.833 +/- 0.383 |  | 1.000 +/- 0.000 | 0.833 +/- 0.383 | 1.000 +/- 0.000 | 0.167 +/- 0.383 | 0.000 +/- 0.000 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 1.000 +/- 0.000 | 8.987 +/- 5.045 | 7172.389 +/- 140.247 |
| `api_llm_react_tool_policy` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 7.278 +/- 1.565 | 33.164 +/- 8.190 | 59526.389 +/- 14003.049 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `social_copresence_two_party` | `api_llm_plan_and_execute` | 0.507 +/- 0.091 | 0.387 +/- 0.055 | 0.500 +/- 0.000 | 0.567 +/- 0.115 | 0.884 +/- 0.111 |
| `social_copresence_with_errand` | `api_llm_react_tool_policy` | 0.423 +/- 0.021 | 0.257 +/- 0.097 | 1.000 +/- 0.000 | 0.600 +/- 0.000 | 0.750 +/- 0.000 |
| `social_copresence_event_window` | `api_llm_plan_and_execute` | 0.327 +/- 0.167 | 0.547 +/- 0.150 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `social_copresence_with_errand` | `api_llm_plan_and_execute` | 0.327 +/- 0.131 | 0.490 +/- 0.114 | 1.000 +/- 0.000 | 0.800 +/- 0.000 | 0.857 +/- 0.000 |
| `social_copresence_open_meet` | `api_llm_react_tool_policy` | 0.233 +/- 0.055 | 0.723 +/- 0.055 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `social_copresence_two_party` | `api_llm_react_tool_policy` | 0.220 +/- 0.121 | 0.687 +/- 0.151 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `social_copresence_message_gated` | `api_llm_plan_and_execute` | 0.167 +/- 0.076 | 0.780 +/- 0.080 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `social_copresence_message_gated` | `api_llm_react_tool_policy` | 0.167 +/- 0.101 | 0.787 +/- 0.070 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `social_copresence_event_window` | `api_llm_react_tool_policy` | 0.133 +/- 0.012 | 0.687 +/- 0.031 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `social_copresence_decoy_location` | `api_llm_react_tool_policy` | 0.100 +/- 0.113 | 0.837 +/- 0.101 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `social_copresence_decoy_location` | `api_llm_plan_and_execute` | 0.097 +/- 0.021 | 0.867 +/- 0.031 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `social_copresence_open_meet` | `api_llm_plan_and_execute` | 0.050 +/- 0.020 | 0.917 +/- 0.031 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `api_llm_plan_and_execute` | `goal_drift` | 1 | 0.056 |
| `api_llm_plan_and_execute` | `invalid_state_transition` | 1 | 0.056 |
| `api_llm_plan_and_execute` | `money_budget_failure` | 3 | 0.167 |
| `api_llm_plan_and_execute` | `social_derailment` | 3 | 0.167 |
| `api_llm_plan_and_execute` | `time_budget_failure` | 2 | 0.111 |
| `api_llm_react_tool_policy` | `done_state_loop` | 3 | 0.167 |
| `api_llm_react_tool_policy` | `invalid_state_transition` | 3 | 0.167 |
| `api_llm_react_tool_policy` | `money_budget_failure` | 3 | 0.167 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
