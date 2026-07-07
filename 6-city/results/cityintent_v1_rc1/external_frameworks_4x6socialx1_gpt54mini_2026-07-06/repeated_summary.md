# CityIntent Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 18 | 0.325 +/- 0.396 | 0.439 +/- 0.294 | 0.615 +/- 0.298 | 0.336 +/- 0.348 |  | 0.903 +/- 0.065 | 0.530 +/- 0.202 | 0.373 +/- 0.181 | 0.385 +/- 0.298 |
| `gatsim_official_planner` | 18 | 0.667 +/- 0.485 | 0.650 +/- 0.392 | 0.819 +/- 0.248 | 0.616 +/- 0.427 |  | 0.776 +/- 0.084 | 0.336 +/- 0.172 | 0.440 +/- 0.124 | 0.181 +/- 0.248 |
| `generative_agents_official_planner` | 18 | 0.220 +/- 0.276 | 0.322 +/- 0.177 | 0.666 +/- 0.221 | 0.226 +/- 0.166 |  | 0.772 +/- 0.226 | 0.368 +/- 0.244 | 0.404 +/- 0.204 | 0.333 +/- 0.221 |
| `sotopia_official_llm_agent` | 18 | 0.103 +/- 0.149 | 0.383 +/- 0.159 | 0.913 +/- 0.124 | 0.366 +/- 0.181 |  | 0.813 +/- 0.185 | 0.420 +/- 0.215 | 0.393 +/- 0.182 | 0.087 +/- 0.124 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.591 +/- 0.263 |  | 0.906 +/- 0.146 | 1.000 +/- 0.000 | 0.389 +/- 0.404 | 0.000 +/- 0.000 | 0.056 +/- 0.236 |
| `gatsim_official_planner` | 0.643 +/- 0.396 |  | 0.768 +/- 0.270 | 0.833 +/- 0.383 | 0.667 +/- 0.485 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `generative_agents_official_planner` | 0.443 +/- 0.177 |  | 0.949 +/- 0.128 | 0.944 +/- 0.236 | 0.250 +/- 0.354 | 0.000 +/- 0.000 | 0.111 +/- 0.323 |
| `sotopia_official_llm_agent` | 0.783 +/- 0.281 |  | 0.816 +/- 0.195 | 1.000 +/- 0.000 | 0.167 +/- 0.243 | 0.056 +/- 0.236 | 0.000 +/- 0.000 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 6.889 +/- 3.954 | 44.018 +/- 25.514 | 49050.000 +/- 28385.730 |
| `gatsim_official_planner` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 2.444 +/- 2.036 | 20.862 +/- 15.266 | 23155.056 +/- 19770.759 |
| `generative_agents_official_planner` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 5.111 +/- 3.394 | 33.309 +/- 21.596 | 30974.222 +/- 20297.747 |
| `sotopia_official_llm_agent` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 5.778 +/- 2.340 | 26.279 +/- 14.746 | 39752.556 +/- 16667.296 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `social_copresence_event_window` | `sotopia_official_llm_agent` | 0.607 +/- 0.023 | 0.330 +/- 0.017 | 0.000 +/- 0.000 | 0.300 +/- 0.173 | 0.833 +/- 0.144 |
| `social_copresence_message_gated` | `gatsim_official_planner` | 0.560 +/- 0.120 | 0.227 +/- 0.050 | 0.000 +/- 0.000 | 0.150 +/- 0.000 | 0.606 +/- 0.183 |
| `social_copresence_event_window` | `agentsociety_official_plan_blocks` | 0.547 +/- 0.125 | 0.373 +/- 0.081 | 0.000 +/- 0.000 | 0.300 +/- 0.173 | 0.533 +/- 0.404 |
| `social_copresence_event_window` | `generative_agents_official_planner` | 0.503 +/- 0.202 | 0.330 +/- 0.121 | 0.000 +/- 0.000 | 0.200 +/- 0.000 | 0.369 +/- 0.034 |
| `social_copresence_with_errand` | `gatsim_official_planner` | 0.500 +/- 0.060 | 0.180 +/- 0.000 | 1.000 +/- 0.000 | 0.600 +/- 0.000 | 0.909 +/- 0.000 |
| `social_copresence_message_gated` | `generative_agents_official_planner` | 0.490 +/- 0.131 | 0.347 +/- 0.115 | 0.308 +/- 0.000 | 0.350 +/- 0.000 | 0.833 +/- 0.058 |
| `social_copresence_open_meet` | `generative_agents_official_planner` | 0.463 +/- 0.059 | 0.240 +/- 0.122 | 0.000 +/- 0.000 | 0.200 +/- 0.000 | 0.737 +/- 0.122 |
| `social_copresence_decoy_location` | `gatsim_official_planner` | 0.450 +/- 0.026 | 0.267 +/- 0.023 | 0.000 +/- 0.000 | 0.150 +/- 0.000 | 0.400 +/- 0.000 |
| `social_copresence_with_errand` | `sotopia_official_llm_agent` | 0.447 +/- 0.110 | 0.380 +/- 0.061 | 0.000 +/- 0.000 | 0.200 +/- 0.000 | 0.767 +/- 0.128 |
| `social_copresence_event_window` | `gatsim_official_planner` | 0.440 +/- 0.139 | 0.370 +/- 0.226 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `social_copresence_with_errand` | `generative_agents_official_planner` | 0.437 +/- 0.196 | 0.420 +/- 0.282 | 0.472 +/- 0.096 | 0.483 +/- 0.208 | 0.732 +/- 0.294 |
| `social_copresence_open_meet` | `agentsociety_official_plan_blocks` | 0.420 +/- 0.104 | 0.437 +/- 0.067 | 0.333 +/- 0.577 | 0.367 +/- 0.289 | 0.642 +/- 0.232 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `agentsociety_official_plan_blocks` | `goal_drift` | 2 | 0.111 |
| `agentsociety_official_plan_blocks` | `invalid_state_transition` | 21 | 1.167 |
| `agentsociety_official_plan_blocks` | `money_budget_failure` | 30 | 1.667 |
| `agentsociety_official_plan_blocks` | `social_derailment` | 1 | 0.056 |
| `agentsociety_official_plan_blocks` | `time_budget_failure` | 8 | 0.444 |
| `gatsim_official_planner` | `impossible_route` | 1 | 0.056 |
| `gatsim_official_planner` | `invalid_state_transition` | 26 | 1.444 |
| `gatsim_official_planner` | `money_budget_failure` | 3 | 0.167 |
| `gatsim_official_planner` | `time_budget_failure` | 2 | 0.111 |
| `generative_agents_official_planner` | `goal_drift` | 1 | 0.056 |
| `generative_agents_official_planner` | `impossible_route` | 14 | 0.778 |
| `generative_agents_official_planner` | `invalid_state_transition` | 4 | 0.222 |
| `generative_agents_official_planner` | `money_budget_failure` | 26 | 1.444 |
| `generative_agents_official_planner` | `social_derailment` | 2 | 0.111 |
| `generative_agents_official_planner` | `time_budget_failure` | 2 | 0.111 |
| `sotopia_official_llm_agent` | `done_state_loop` | 1 | 0.056 |
| `sotopia_official_llm_agent` | `goal_drift` | 11 | 0.611 |
| `sotopia_official_llm_agent` | `invalid_state_transition` | 9 | 0.500 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
