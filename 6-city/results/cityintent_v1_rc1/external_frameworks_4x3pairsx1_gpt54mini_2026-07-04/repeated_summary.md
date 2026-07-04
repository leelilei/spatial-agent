# CityIntent Repeated Reliability Table

Repeated runs: 1

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 6 | 0.756 +/- 0.414 | 0.767 +/- 0.244 | 0.787 +/- 0.237 | 0.610 +/- 0.307 |  | 0.877 +/- 0.103 | 0.658 +/- 0.321 | 0.218 +/- 0.222 | 0.212 +/- 0.237 |
| `gatsim_official_planner` | 6 | 1.000 +/- 0.000 | 0.958 +/- 0.102 | 0.976 +/- 0.058 | 0.941 +/- 0.146 |  | 0.602 +/- 0.316 | 0.222 +/- 0.177 | 0.380 +/- 0.217 | 0.024 +/- 0.058 |
| `generative_agents_official_planner` | 6 | 0.923 +/- 0.189 | 0.858 +/- 0.201 | 0.853 +/- 0.178 | 0.760 +/- 0.293 |  | 0.868 +/- 0.076 | 0.462 +/- 0.280 | 0.407 +/- 0.224 | 0.146 +/- 0.178 |
| `sotopia_official_llm_agent` | 6 | 0.090 +/- 0.220 | 0.425 +/- 0.137 | 0.805 +/- 0.306 | 0.367 +/- 0.181 |  | 0.897 +/- 0.051 | 0.462 +/- 0.269 | 0.438 +/- 0.240 | 0.195 +/- 0.306 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.779 +/- 0.276 |  | 0.834 +/- 0.259 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.167 +/- 0.408 | 0.000 +/- 0.000 |
| `gatsim_official_planner` | 0.907 +/- 0.227 |  | 0.571 +/- 0.307 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `generative_agents_official_planner` | 0.779 +/- 0.276 |  | 0.844 +/- 0.300 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.167 +/- 0.408 | 0.000 +/- 0.000 |
| `sotopia_official_llm_agent` | 0.810 +/- 0.295 |  | 0.897 +/- 0.126 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 6.000 +/- 4.561 | 41.348 +/- 31.675 | 42765.833 +/- 32989.695 |
| `gatsim_official_planner` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 1.667 +/- 0.816 | 52.895 +/- 91.989 | 15595.667 +/- 7802.355 |
| `generative_agents_official_planner` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 3.667 +/- 3.011 | 31.383 +/- 30.991 | 22529.667 +/- 17842.861 |
| `sotopia_official_llm_agent` | 0.000 +/- 0.000 | 0.167 +/- 0.408 | 4.000 +/- 1.549 | 25.414 +/- 17.189 | 27599.500 +/- 11166.713 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `paired_commute_a` | `gatsim_official_planner` | 0.750 +/- 0.000 | 0.150 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `paired_pickup_a` | `sotopia_official_llm_agent` | 0.660 +/- 0.000 | 0.180 +/- 0.000 | 0.000 +/- 0.000 | 0.500 +/- 0.000 | 1.000 +/- 0.000 |
| `paired_pickup_a` | `generative_agents_official_planner` | 0.620 +/- 0.000 | 0.280 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `paired_pickup_b` | `sotopia_official_llm_agent` | 0.590 +/- 0.000 | 0.270 +/- 0.000 | 0.000 +/- 0.000 | 0.500 +/- 0.000 | 1.000 +/- 0.000 |
| `paired_pickup_b` | `generative_agents_official_planner` | 0.560 +/- 0.000 | 0.220 +/- 0.000 | 1.000 +/- 0.000 | 0.900 +/- 0.000 | 0.750 +/- 0.000 |
| `paired_commute_b` | `generative_agents_official_planner` | 0.540 +/- 0.000 | 0.240 +/- 0.000 | 1.000 +/- 0.000 | 0.750 +/- 0.000 | 0.800 +/- 0.000 |
| `paired_pickup_b` | `agentsociety_official_plan_blocks` | 0.540 +/- 0.000 | 0.180 +/- 0.000 | 1.000 +/- 0.000 | 0.900 +/- 0.000 | 0.500 +/- 0.000 |
| `paired_study_a` | `sotopia_official_llm_agent` | 0.530 +/- 0.000 | 0.440 +/- 0.000 | 0.000 +/- 0.000 | 0.150 +/- 0.000 | 0.333 +/- 0.000 |
| `paired_commute_b` | `sotopia_official_llm_agent` | 0.510 +/- 0.000 | 0.410 +/- 0.000 | 0.000 +/- 0.000 | 0.450 +/- 0.000 | 1.000 +/- 0.000 |
| `paired_commute_b` | `agentsociety_official_plan_blocks` | 0.420 +/- 0.000 | 0.410 +/- 0.000 | 1.000 +/- 0.000 | 0.750 +/- 0.000 | 0.600 +/- 0.000 |
| `paired_study_b` | `gatsim_official_planner` | 0.420 +/- 0.000 | 0.340 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `paired_study_a` | `gatsim_official_planner` | 0.410 +/- 0.000 | 0.520 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `agentsociety_official_plan_blocks` | `closed_place_action` | 1 | 0.167 |
| `agentsociety_official_plan_blocks` | `done_state_loop` | 1 | 0.167 |
| `agentsociety_official_plan_blocks` | `goal_drift` | 1 | 0.167 |
| `agentsociety_official_plan_blocks` | `invalid_state_transition` | 6 | 1.000 |
| `agentsociety_official_plan_blocks` | `money_budget_failure` | 2 | 0.333 |
| `gatsim_official_planner` | `closed_place_action` | 1 | 0.167 |
| `generative_agents_official_planner` | `done_state_loop` | 1 | 0.167 |
| `generative_agents_official_planner` | `impossible_route` | 1 | 0.167 |
| `generative_agents_official_planner` | `invalid_state_transition` | 2 | 0.333 |
| `generative_agents_official_planner` | `money_budget_failure` | 3 | 0.500 |
| `sotopia_official_llm_agent` | `closed_place_action` | 1 | 0.167 |
| `sotopia_official_llm_agent` | `goal_drift` | 4 | 0.667 |
| `sotopia_official_llm_agent` | `invalid_state_transition` | 3 | 0.500 |
| `sotopia_official_llm_agent` | `money_budget_failure` | 1 | 0.167 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
