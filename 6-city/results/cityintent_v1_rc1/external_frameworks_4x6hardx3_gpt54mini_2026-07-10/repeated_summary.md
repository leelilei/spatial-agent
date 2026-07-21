# CityIntent Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 18 | 0.314 +/- 0.222 | 0.442 +/- 0.174 | 0.813 +/- 0.178 | 0.378 +/- 0.197 |  | 0.729 +/- 0.203 | 0.492 +/- 0.264 | 0.239 +/- 0.136 | 0.187 +/- 0.178 |
| `gatsim_official_planner` | 18 | 0.750 +/- 0.393 | 0.817 +/- 0.305 | 0.905 +/- 0.219 | 0.798 +/- 0.346 |  | 0.724 +/- 0.093 | 0.486 +/- 0.144 | 0.238 +/- 0.112 | 0.095 +/- 0.219 |
| `generative_agents_official_planner` | 18 | 0.410 +/- 0.278 | 0.497 +/- 0.216 | 0.771 +/- 0.205 | 0.398 +/- 0.242 |  | 0.721 +/- 0.168 | 0.451 +/- 0.125 | 0.269 +/- 0.113 | 0.229 +/- 0.205 |
| `sotopia_official_llm_agent` | 18 | 0.158 +/- 0.187 | 0.328 +/- 0.130 | 0.850 +/- 0.082 | 0.283 +/- 0.128 |  | 0.677 +/- 0.201 | 0.372 +/- 0.173 | 0.304 +/- 0.102 | 0.150 +/- 0.082 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.647 +/- 0.227 |  | 0.957 +/- 0.139 | 1.000 +/- 0.000 | 0.167 +/- 0.249 | 0.000 +/- 0.000 | 0.222 +/- 0.428 |
| `gatsim_official_planner` | 0.917 +/- 0.192 |  | 0.962 +/- 0.111 | 1.000 +/- 0.000 | 0.750 +/- 0.393 | 0.000 +/- 0.000 | 0.167 +/- 0.383 |
| `generative_agents_official_planner` | 0.647 +/- 0.227 |  | 0.918 +/- 0.115 | 1.000 +/- 0.000 | 0.148 +/- 0.279 | 0.000 +/- 0.000 | 0.222 +/- 0.428 |
| `sotopia_official_llm_agent` | 0.595 +/- 0.188 |  | 0.829 +/- 0.189 | 1.000 +/- 0.000 | 0.083 +/- 0.192 | 0.444 +/- 0.511 | 0.000 +/- 0.000 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 5.111 +/- 2.928 | 60.812 +/- 64.640 | 25657.389 +/- 18298.190 |
| `gatsim_official_planner` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 1.833 +/- 1.917 | 32.644 +/- 48.024 | 13940.278 +/- 14900.375 |
| `generative_agents_official_planner` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 4.444 +/- 3.485 | 63.480 +/- 102.651 | 16375.944 +/- 14870.950 |
| `sotopia_official_llm_agent` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 7.611 +/- 1.650 | 65.537 +/- 78.306 | 36342.944 +/- 21383.519 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `hard_three_meeting_relay` | `sotopia_official_llm_agent` | 0.400 +/- 0.106 | 0.360 +/- 0.151 | 0.000 +/- 0.000 | 0.267 +/- 0.115 | 0.897 +/- 0.090 |
| `hard_stale_plan_override` | `gatsim_official_planner` | 0.380 +/- 0.035 | 0.340 +/- 0.072 | 0.000 +/- 0.000 | 0.200 +/- 0.000 | 0.429 +/- 0.000 |
| `hard_stale_plan_override` | `agentsociety_official_plan_blocks` | 0.337 +/- 0.025 | 0.353 +/- 0.102 | 0.333 +/- 0.000 | 0.467 +/- 0.115 | 0.767 +/- 0.208 |
| `hard_budget_entangled_meet` | `sotopia_official_llm_agent` | 0.333 +/- 0.023 | 0.300 +/- 0.144 | 0.257 +/- 0.222 | 0.367 +/- 0.144 | 0.766 +/- 0.061 |
| `hard_full_evening_chain` | `sotopia_official_llm_agent` | 0.327 +/- 0.029 | 0.433 +/- 0.040 | 0.357 +/- 0.124 | 0.400 +/- 0.087 | 0.827 +/- 0.068 |
| `hard_deadline_then_meet` | `sotopia_official_llm_agent` | 0.310 +/- 0.167 | 0.237 +/- 0.169 | 0.000 +/- 0.000 | 0.200 +/- 0.000 | 0.830 +/- 0.029 |
| `hard_deadline_then_meet` | `generative_agents_official_planner` | 0.300 +/- 0.193 | 0.403 +/- 0.067 | 0.500 +/- 0.000 | 0.567 +/- 0.115 | 0.785 +/- 0.222 |
| `hard_three_meeting_relay` | `agentsociety_official_plan_blocks` | 0.300 +/- 0.050 | 0.323 +/- 0.248 | 0.333 +/- 0.334 | 0.467 +/- 0.231 | 0.822 +/- 0.168 |
| `hard_three_meeting_relay` | `generative_agents_official_planner` | 0.290 +/- 0.142 | 0.503 +/- 0.188 | 0.222 +/- 0.192 | 0.333 +/- 0.115 | 0.767 +/- 0.052 |
| `hard_stale_plan_override` | `generative_agents_official_planner` | 0.287 +/- 0.040 | 0.503 +/- 0.086 | 0.555 +/- 0.385 | 0.533 +/- 0.231 | 0.421 +/- 0.084 |
| `hard_full_evening_chain` | `gatsim_official_planner` | 0.270 +/- 0.026 | 0.540 +/- 0.069 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `hard_full_evening_chain` | `generative_agents_official_planner` | 0.270 +/- 0.095 | 0.497 +/- 0.110 | 0.643 +/- 0.000 | 0.750 +/- 0.000 | 1.000 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `agentsociety_official_plan_blocks` | `goal_drift` | 5 | 0.278 |
| `agentsociety_official_plan_blocks` | `invalid_state_transition` | 16 | 0.889 |
| `agentsociety_official_plan_blocks` | `money_budget_failure` | 12 | 0.667 |
| `agentsociety_official_plan_blocks` | `social_derailment` | 4 | 0.222 |
| `agentsociety_official_plan_blocks` | `time_budget_failure` | 1 | 0.056 |
| `gatsim_official_planner` | `goal_drift` | 3 | 0.167 |
| `gatsim_official_planner` | `invalid_state_transition` | 12 | 0.667 |
| `gatsim_official_planner` | `social_derailment` | 3 | 0.167 |
| `generative_agents_official_planner` | `goal_drift` | 1 | 0.056 |
| `generative_agents_official_planner` | `impossible_route` | 4 | 0.222 |
| `generative_agents_official_planner` | `invalid_state_transition` | 10 | 0.556 |
| `generative_agents_official_planner` | `money_budget_failure` | 19 | 1.056 |
| `generative_agents_official_planner` | `social_derailment` | 4 | 0.222 |
| `generative_agents_official_planner` | `time_budget_failure` | 2 | 0.111 |
| `sotopia_official_llm_agent` | `done_state_loop` | 8 | 0.444 |
| `sotopia_official_llm_agent` | `goal_drift` | 3 | 0.167 |
| `sotopia_official_llm_agent` | `invalid_state_transition` | 18 | 1.000 |
| `sotopia_official_llm_agent` | `time_budget_failure` | 1 | 0.056 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
