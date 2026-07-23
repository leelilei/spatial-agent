# CityIntent Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 18 | 0.665 +/- 0.295 | 0.694 +/- 0.196 | 0.893 +/- 0.128 | 0.624 +/- 0.218 |  | 0.810 +/- 0.088 | 0.439 +/- 0.191 | 0.371 +/- 0.153 | 0.107 +/- 0.128 |
| `gatsim_official_planner` | 18 | 0.701 +/- 0.386 | 0.786 +/- 0.299 | 0.934 +/- 0.167 | 0.773 +/- 0.327 |  | 0.726 +/- 0.252 | 0.356 +/- 0.204 | 0.371 +/- 0.200 | 0.066 +/- 0.167 |
| `generative_agents_official_planner` | 18 | 0.629 +/- 0.242 | 0.683 +/- 0.156 | 0.922 +/- 0.106 | 0.633 +/- 0.176 |  | 0.696 +/- 0.249 | 0.406 +/- 0.252 | 0.290 +/- 0.156 | 0.078 +/- 0.106 |
| `sotopia_official_llm_agent` | 18 | 0.527 +/- 0.246 | 0.597 +/- 0.179 | 0.913 +/- 0.091 | 0.552 +/- 0.190 |  | 0.769 +/- 0.145 | 0.459 +/- 0.184 | 0.310 +/- 0.168 | 0.087 +/- 0.091 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.758 +/- 0.250 |  | 0.931 +/- 0.108 | 1.000 +/- 0.000 | 0.639 +/- 0.447 | 0.000 +/- 0.000 | 0.389 +/- 0.502 |
| `gatsim_official_planner` | 0.917 +/- 0.192 |  | 0.944 +/- 0.162 | 1.000 +/- 0.000 | 0.639 +/- 0.447 | 0.000 +/- 0.000 | 0.167 +/- 0.383 |
| `generative_agents_official_planner` | 0.786 +/- 0.247 |  | 0.988 +/- 0.020 | 1.000 +/- 0.000 | 0.491 +/- 0.441 | 0.000 +/- 0.000 | 0.333 +/- 0.485 |
| `sotopia_official_llm_agent` | 0.706 +/- 0.242 |  | 0.929 +/- 0.096 | 1.000 +/- 0.000 | 0.398 +/- 0.409 | 0.000 +/- 0.000 | 0.333 +/- 0.485 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 4.556 +/- 2.812 | 58.271 +/- 32.533 | 39200.889 +/- 24237.321 |
| `gatsim_official_planner` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 1.667 +/- 1.645 | 24.683 +/- 22.058 | 18310.167 +/- 18138.351 |
| `generative_agents_official_planner` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 2.667 +/- 2.497 | 34.182 +/- 24.608 | 20146.722 +/- 17697.615 |
| `sotopia_official_llm_agent` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 10.611 +/- 2.893 | 81.040 +/- 30.132 | 85835.222 +/- 23934.534 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `hard_deadline_then_meet` | `agentsociety_official_plan_blocks` | 0.547 +/- 0.130 | 0.253 +/- 0.095 | 0.333 +/- 0.289 | 0.533 +/- 0.153 | 0.967 +/- 0.058 |
| `hard_deadline_then_meet` | `gatsim_official_planner` | 0.510 +/- 0.062 | 0.320 +/- 0.036 | 0.833 +/- 0.289 | 0.900 +/- 0.173 | 1.000 +/- 0.000 |
| `hard_budget_entangled_meet` | `gatsim_official_planner` | 0.507 +/- 0.049 | 0.290 +/- 0.101 | 0.872 +/- 0.222 | 0.917 +/- 0.144 | 1.000 +/- 0.000 |
| `hard_full_evening_chain` | `gatsim_official_planner` | 0.480 +/- 0.087 | 0.393 +/- 0.046 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_three_meeting_relay` | `agentsociety_official_plan_blocks` | 0.430 +/- 0.062 | 0.413 +/- 0.072 | 1.000 +/- 0.000 | 0.800 +/- 0.000 | 0.718 +/- 0.044 |
| `hard_budget_entangled_meet` | `generative_agents_official_planner` | 0.407 +/- 0.104 | 0.167 +/- 0.023 | 0.385 +/- 0.000 | 0.500 +/- 0.087 | 0.945 +/- 0.048 |
| `hard_stale_plan_override` | `sotopia_official_llm_agent` | 0.357 +/- 0.334 | 0.530 +/- 0.328 | 0.555 +/- 0.385 | 0.667 +/- 0.306 | 0.967 +/- 0.058 |
| `hard_overlapping_windows` | `sotopia_official_llm_agent` | 0.340 +/- 0.100 | 0.440 +/- 0.072 | 0.500 +/- 0.000 | 0.567 +/- 0.115 | 0.930 +/- 0.061 |
| `hard_full_evening_chain` | `sotopia_official_llm_agent` | 0.337 +/- 0.071 | 0.487 +/- 0.153 | 0.667 +/- 0.206 | 0.667 +/- 0.058 | 0.939 +/- 0.054 |
| `hard_full_evening_chain` | `generative_agents_official_planner` | 0.333 +/- 0.168 | 0.227 +/- 0.175 | 0.667 +/- 0.206 | 0.767 +/- 0.144 | 1.000 +/- 0.000 |
| `hard_stale_plan_override` | `agentsociety_official_plan_blocks` | 0.327 +/- 0.179 | 0.513 +/- 0.205 | 0.778 +/- 0.385 | 0.800 +/- 0.346 | 0.963 +/- 0.064 |
| `hard_three_meeting_relay` | `sotopia_official_llm_agent` | 0.327 +/- 0.265 | 0.543 +/- 0.294 | 0.556 +/- 0.509 | 0.533 +/- 0.306 | 0.751 +/- 0.032 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `agentsociety_official_plan_blocks` | `goal_drift` | 4 | 0.222 |
| `agentsociety_official_plan_blocks` | `impossible_route` | 1 | 0.056 |
| `agentsociety_official_plan_blocks` | `invalid_state_transition` | 12 | 0.667 |
| `agentsociety_official_plan_blocks` | `money_budget_failure` | 8 | 0.444 |
| `agentsociety_official_plan_blocks` | `social_derailment` | 7 | 0.389 |
| `agentsociety_official_plan_blocks` | `time_budget_failure` | 1 | 0.056 |
| `gatsim_official_planner` | `goal_drift` | 4 | 0.222 |
| `gatsim_official_planner` | `invalid_state_transition` | 9 | 0.500 |
| `gatsim_official_planner` | `social_derailment` | 3 | 0.167 |
| `generative_agents_official_planner` | `goal_drift` | 7 | 0.389 |
| `generative_agents_official_planner` | `invalid_state_transition` | 5 | 0.278 |
| `generative_agents_official_planner` | `money_budget_failure` | 11 | 0.611 |
| `generative_agents_official_planner` | `social_derailment` | 6 | 0.333 |
| `sotopia_official_llm_agent` | `done_state_loop` | 3 | 0.167 |
| `sotopia_official_llm_agent` | `goal_drift` | 6 | 0.333 |
| `sotopia_official_llm_agent` | `invalid_state_transition` | 11 | 0.611 |
| `sotopia_official_llm_agent` | `money_budget_failure` | 5 | 0.278 |
| `sotopia_official_llm_agent` | `social_derailment` | 6 | 0.333 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
