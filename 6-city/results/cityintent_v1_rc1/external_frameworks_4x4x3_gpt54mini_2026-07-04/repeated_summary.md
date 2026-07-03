# CityIntent Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 12 | 0.702 +/- 0.384 | 0.713 +/- 0.302 | 0.765 +/- 0.174 | 0.583 +/- 0.340 | 0.333 +/- 0.577 | 0.895 +/- 0.067 | 0.583 +/- 0.214 | 0.312 +/- 0.184 | 0.235 +/- 0.174 |
| `gatsim_official_planner` | 12 | 0.667 +/- 0.492 | 0.729 +/- 0.371 | 0.908 +/- 0.161 | 0.696 +/- 0.377 | 0.333 +/- 0.577 | 0.558 +/- 0.289 | 0.207 +/- 0.144 | 0.352 +/- 0.195 | 0.092 +/- 0.161 |
| `generative_agents_official_planner` | 12 | 0.619 +/- 0.362 | 0.662 +/- 0.246 | 0.678 +/- 0.139 | 0.461 +/- 0.237 | 0.333 +/- 0.577 | 0.687 +/- 0.305 | 0.388 +/- 0.263 | 0.298 +/- 0.181 | 0.322 +/- 0.139 |
| `sotopia_official_llm_agent` | 12 | 0.160 +/- 0.208 | 0.571 +/- 0.092 | 0.897 +/- 0.189 | 0.503 +/- 0.103 | 0.667 +/- 0.577 | 0.767 +/- 0.152 | 0.290 +/- 0.121 | 0.477 +/- 0.115 | 0.103 +/- 0.189 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.774 +/- 0.252 | 0.333 +/- 0.577 | 0.852 +/- 0.249 | 1.000 +/- 0.000 | 0.750 +/- 0.274 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `gatsim_official_planner` | 0.877 +/- 0.230 | 0.333 +/- 0.577 | 0.601 +/- 0.286 | 1.000 +/- 0.000 | 0.500 +/- 0.548 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `generative_agents_official_planner` | 0.774 +/- 0.252 | 0.333 +/- 0.577 | 0.834 +/- 0.226 | 1.000 +/- 0.000 | 0.750 +/- 0.274 | 0.000 +/- 0.000 | 0.083 +/- 0.289 |
| `sotopia_official_llm_agent` | 1.000 +/- 0.000 | 0.667 +/- 0.577 | 0.944 +/- 0.122 | 1.000 +/- 0.000 | 0.750 +/- 0.274 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.000 +/- 0.000 | 0.083 +/- 0.289 | 5.833 +/- 2.758 | 35.756 +/- 17.952 | 41564.750 +/- 20175.377 |
| `gatsim_official_planner` | 0.250 +/- 0.452 | 0.083 +/- 0.289 | 2.083 +/- 1.379 | 23.631 +/- 18.371 | 19611.500 +/- 13195.461 |
| `generative_agents_official_planner` | 0.083 +/- 0.289 | 0.083 +/- 0.289 | 5.667 +/- 2.309 | 34.675 +/- 13.277 | 34412.750 +/- 13411.702 |
| `sotopia_official_llm_agent` | 0.000 +/- 0.000 | 0.167 +/- 0.389 | 5.417 +/- 2.968 | 23.903 +/- 14.532 | 37751.583 +/- 21416.958 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `meeting_wait_trap` | `sotopia_official_llm_agent` | 0.540 +/- 0.000 | 0.320 +/- 0.035 | 0.308 +/- 0.000 | 0.550 +/- 0.000 | 1.000 +/- 0.000 |
| `school_pickup_social_detour` | `sotopia_official_llm_agent` | 0.493 +/- 0.130 | 0.253 +/- 0.153 | 0.000 +/- 0.000 | 0.550 +/- 0.000 | 0.889 +/- 0.192 |
| `meeting_wait_trap` | `agentsociety_official_plan_blocks` | 0.477 +/- 0.051 | 0.370 +/- 0.036 | 0.308 +/- 0.000 | 0.350 +/- 0.000 | 0.613 +/- 0.049 |
| `detour_commute_midroute_block` | `sotopia_official_llm_agent` | 0.447 +/- 0.154 | 0.240 +/- 0.072 | 0.000 +/- 0.000 | 0.583 +/- 0.115 | 1.000 +/- 0.000 |
| `school_pickup_social_detour` | `generative_agents_official_planner` | 0.430 +/- 0.265 | 0.213 +/- 0.142 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.825 +/- 0.043 |
| `closed_study_spot_replacement` | `sotopia_official_llm_agent` | 0.427 +/- 0.142 | 0.347 +/- 0.197 | 0.333 +/- 0.289 | 0.600 +/- 0.173 | 0.700 +/- 0.265 |
| `detour_commute_midroute_block` | `gatsim_official_planner` | 0.407 +/- 0.284 | 0.180 +/- 0.100 | 0.667 +/- 0.577 | 0.700 +/- 0.361 | 0.958 +/- 0.072 |
| `meeting_wait_trap` | `generative_agents_official_planner` | 0.387 +/- 0.086 | 0.457 +/- 0.108 | 0.308 +/- 0.000 | 0.350 +/- 0.000 | 0.630 +/- 0.064 |
| `detour_commute_midroute_block` | `agentsociety_official_plan_blocks` | 0.367 +/- 0.205 | 0.520 +/- 0.140 | 0.667 +/- 0.577 | 0.600 +/- 0.278 | 0.722 +/- 0.048 |
| `closed_study_spot_replacement` | `gatsim_official_planner` | 0.363 +/- 0.049 | 0.403 +/- 0.080 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.917 +/- 0.072 |
| `meeting_wait_trap` | `gatsim_official_planner` | 0.360 +/- 0.231 | 0.140 +/- 0.106 | 0.000 +/- 0.000 | 0.217 +/- 0.115 | 0.759 +/- 0.285 |
| `school_pickup_social_detour` | `gatsim_official_planner` | 0.277 +/- 0.245 | 0.103 +/- 0.068 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `agentsociety_official_plan_blocks` | `invalid_state_transition` | 10 | 0.833 |
| `agentsociety_official_plan_blocks` | `money_budget_failure` | 5 | 0.417 |
| `agentsociety_official_plan_blocks` | `time_budget_failure` | 3 | 0.250 |
| `gatsim_official_planner` | `closed_place_action` | 1 | 0.083 |
| `gatsim_official_planner` | `goal_drift` | 1 | 0.083 |
| `gatsim_official_planner` | `invalid_state_transition` | 4 | 0.333 |
| `gatsim_official_planner` | `time_budget_failure` | 4 | 0.333 |
| `generative_agents_official_planner` | `closed_place_action` | 1 | 0.083 |
| `generative_agents_official_planner` | `impossible_route` | 7 | 0.583 |
| `generative_agents_official_planner` | `invalid_state_transition` | 3 | 0.250 |
| `generative_agents_official_planner` | `money_budget_failure` | 16 | 1.333 |
| `generative_agents_official_planner` | `social_derailment` | 1 | 0.083 |
| `generative_agents_official_planner` | `time_budget_failure` | 1 | 0.083 |
| `sotopia_official_llm_agent` | `goal_drift` | 9 | 0.750 |
| `sotopia_official_llm_agent` | `invalid_state_transition` | 3 | 0.250 |
| `sotopia_official_llm_agent` | `money_budget_failure` | 2 | 0.167 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
