# CityIntent Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 18 | 0.857 +/- 0.340 | 0.814 +/- 0.245 | 0.946 +/- 0.064 | 0.778 +/- 0.263 |  | 0.796 +/- 0.248 | 0.582 +/- 0.295 | 0.214 +/- 0.180 | 0.054 +/- 0.064 |
| `api_llm_plan_and_execute` | 18 | 1.000 +/- 0.000 | 0.933 +/- 0.153 | 0.979 +/- 0.049 | 0.921 +/- 0.183 |  | 0.886 +/- 0.105 | 0.689 +/- 0.254 | 0.197 +/- 0.163 | 0.021 +/- 0.049 |
| `api_llm_react_tool_policy` | 18 | 1.000 +/- 0.000 | 0.933 +/- 0.153 | 0.976 +/- 0.055 | 0.919 +/- 0.186 |  | 0.874 +/- 0.159 | 0.716 +/- 0.244 | 0.158 +/- 0.138 | 0.024 +/- 0.055 |
| `gatsim_official_planner` | 18 | 0.634 +/- 0.481 | 0.631 +/- 0.403 | 0.796 +/- 0.263 | 0.593 +/- 0.441 |  | 0.721 +/- 0.213 | 0.333 +/- 0.157 | 0.388 +/- 0.168 | 0.204 +/- 0.263 |
| `generative_agents_official_planner` | 18 | 0.712 +/- 0.436 | 0.781 +/- 0.315 | 0.961 +/- 0.080 | 0.769 +/- 0.329 |  | 0.847 +/- 0.065 | 0.508 +/- 0.162 | 0.339 +/- 0.144 | 0.039 +/- 0.080 |
| `sotopia_official_llm_agent` | 18 | 0.579 +/- 0.421 | 0.564 +/- 0.263 | 0.822 +/- 0.152 | 0.486 +/- 0.268 |  | 0.793 +/- 0.131 | 0.506 +/- 0.200 | 0.287 +/- 0.168 | 0.178 +/- 0.152 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.753 +/- 0.286 |  | 0.844 +/- 0.163 | 1.000 +/- 0.000 | 0.833 +/- 0.383 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `api_llm_plan_and_execute` | 0.833 +/- 0.383 |  | 1.000 +/- 0.000 | 0.833 +/- 0.383 | 1.000 +/- 0.000 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `api_llm_react_tool_policy` | 0.833 +/- 0.383 |  | 1.000 +/- 0.000 | 0.833 +/- 0.383 | 1.000 +/- 0.000 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `gatsim_official_planner` | 0.643 +/- 0.396 |  | 0.893 +/- 0.206 | 0.833 +/- 0.383 | 0.611 +/- 0.502 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `generative_agents_official_planner` | 0.867 +/- 0.257 |  | 0.907 +/- 0.112 | 1.000 +/- 0.000 | 0.722 +/- 0.428 | 0.000 +/- 0.000 | 0.111 +/- 0.323 |
| `sotopia_official_llm_agent` | 0.534 +/- 0.218 |  | 0.871 +/- 0.156 | 1.000 +/- 0.000 | 0.611 +/- 0.439 | 0.056 +/- 0.236 | 0.111 +/- 0.323 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 2.889 +/- 1.023 | 38.352 +/- 17.278 | 23373.389 +/- 8480.484 |
| `api_llm_plan_and_execute` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 1.000 +/- 0.000 | 14.844 +/- 4.786 | 8462.944 +/- 910.291 |
| `api_llm_react_tool_policy` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 6.833 +/- 1.098 | 54.990 +/- 15.669 | 60575.111 +/- 11296.862 |
| `gatsim_official_planner` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 2.778 +/- 2.264 | 46.253 +/- 42.308 | 29866.167 +/- 24789.311 |
| `generative_agents_official_planner` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 1.444 +/- 0.856 | 20.928 +/- 9.753 | 10898.667 +/- 5663.542 |
| `sotopia_official_llm_agent` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 9.556 +/- 2.572 | 78.939 +/- 33.659 | 75438.278 +/- 22472.491 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `social_copresence_event_window` | `sotopia_official_llm_agent` | 0.493 +/- 0.081 | 0.353 +/- 0.035 | 0.000 +/- 0.000 | 0.200 +/- 0.000 | 0.711 +/- 0.183 |
| `social_copresence_with_errand` | `generative_agents_official_planner` | 0.480 +/- 0.174 | 0.347 +/- 0.145 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `social_copresence_with_errand` | `api_llm_plan_and_execute` | 0.470 +/- 0.061 | 0.213 +/- 0.058 | 1.000 +/- 0.000 | 0.600 +/- 0.000 | 0.874 +/- 0.016 |
| `social_copresence_decoy_location` | `gatsim_official_planner` | 0.460 +/- 0.035 | 0.280 +/- 0.000 | 0.000 +/- 0.000 | 0.150 +/- 0.000 | 0.485 +/- 0.079 |
| `social_copresence_event_window` | `agentsociety_official_plan_blocks` | 0.460 +/- 0.101 | 0.443 +/- 0.107 | 1.000 +/- 0.000 | 0.900 +/- 0.173 | 0.944 +/- 0.096 |
| `social_copresence_event_window` | `gatsim_official_planner` | 0.453 +/- 0.070 | 0.397 +/- 0.078 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `social_copresence_with_errand` | `gatsim_official_planner` | 0.430 +/- 0.200 | 0.173 +/- 0.050 | 0.806 +/- 0.337 | 0.483 +/- 0.202 | 0.889 +/- 0.028 |
| `social_copresence_open_meet` | `generative_agents_official_planner` | 0.390 +/- 0.121 | 0.437 +/- 0.153 | 0.000 +/- 0.000 | 0.300 +/- 0.173 | 0.880 +/- 0.125 |
| `social_copresence_two_party` | `gatsim_official_planner` | 0.370 +/- 0.193 | 0.430 +/- 0.020 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `social_copresence_with_errand` | `api_llm_react_tool_policy` | 0.347 +/- 0.172 | 0.233 +/- 0.050 | 1.000 +/- 0.000 | 0.600 +/- 0.000 | 0.857 +/- 0.000 |
| `social_copresence_event_window` | `generative_agents_official_planner` | 0.343 +/- 0.216 | 0.500 +/- 0.193 | 0.667 +/- 0.577 | 0.633 +/- 0.404 | 0.886 +/- 0.103 |
| `social_copresence_message_gated` | `gatsim_official_planner` | 0.330 +/- 0.313 | 0.180 +/- 0.087 | 0.000 +/- 0.000 | 0.150 +/- 0.000 | 0.400 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `agentsociety_official_plan_blocks` | `goal_drift` | 1 | 0.056 |
| `agentsociety_official_plan_blocks` | `invalid_state_transition` | 8 | 0.444 |
| `api_llm_plan_and_execute` | `money_budget_failure` | 3 | 0.167 |
| `api_llm_react_tool_policy` | `money_budget_failure` | 3 | 0.167 |
| `gatsim_official_planner` | `invalid_state_transition` | 32 | 1.778 |
| `gatsim_official_planner` | `money_budget_failure` | 3 | 0.167 |
| `gatsim_official_planner` | `time_budget_failure` | 1 | 0.056 |
| `generative_agents_official_planner` | `goal_drift` | 3 | 0.167 |
| `generative_agents_official_planner` | `invalid_state_transition` | 3 | 0.167 |
| `generative_agents_official_planner` | `money_budget_failure` | 1 | 0.056 |
| `generative_agents_official_planner` | `social_derailment` | 2 | 0.111 |
| `sotopia_official_llm_agent` | `done_state_loop` | 4 | 0.222 |
| `sotopia_official_llm_agent` | `goal_drift` | 1 | 0.056 |
| `sotopia_official_llm_agent` | `invalid_state_transition` | 20 | 1.111 |
| `sotopia_official_llm_agent` | `money_budget_failure` | 8 | 0.444 |
| `sotopia_official_llm_agent` | `social_derailment` | 2 | 0.111 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
