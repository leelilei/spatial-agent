# CityIntent Repeated Reliability Table

Repeated runs: 1

Each cell is mean +/- sample standard deviation across all deterministically verified scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 4 | 0.827 +/- 0.346 | 0.750 +/- 0.314 | 0.823 +/- 0.146 | 0.649 +/- 0.353 | 0.000 +/- 0.000 |  |  |  | 0.177 +/- 0.146 |
| `gatsim_official_planner` | 4 | 0.750 +/- 0.500 | 0.787 +/- 0.425 | 0.830 +/- 0.264 | 0.736 +/- 0.450 | 1.000 +/- 0.000 |  |  |  | 0.170 +/- 0.264 |
| `generative_agents_official_planner` | 4 | 0.702 +/- 0.353 | 0.675 +/- 0.266 | 0.635 +/- 0.130 | 0.440 +/- 0.250 | 0.000 +/- 0.000 |  |  |  | 0.365 +/- 0.130 |
| `sotopia_official_llm_agent` | 4 | 0.077 +/- 0.154 | 0.488 +/- 0.075 | 1.000 +/- 0.000 | 0.488 +/- 0.075 | 0.000 +/- 0.000 |  |  |  | 0.000 +/- 0.000 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.774 +/- 0.278 | 0.000 +/- 0.000 | 0.849 +/- 0.302 | 1.000 +/- 0.000 | 0.750 +/- 0.354 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `gatsim_official_planner` | 0.857 +/- 0.285 | 1.000 +/- 0.000 | 0.706 +/- 0.278 | 1.000 +/- 0.000 | 0.500 +/- 0.707 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `generative_agents_official_planner` | 0.774 +/- 0.278 | 0.000 +/- 0.000 | 0.971 +/- 0.035 | 1.000 +/- 0.000 | 0.750 +/- 0.354 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `sotopia_official_llm_agent` | 1.000 +/- 0.000 | 0.000 +/- 0.000 | 0.898 +/- 0.205 | 1.000 +/- 0.000 | 0.750 +/- 0.354 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 5.500 +/- 2.517 | 37.718 +/- 20.994 | 38626.000 +/- 18218.646 |
| `gatsim_official_planner` | 0.250 +/- 0.500 | 0.250 +/- 0.500 | 2.750 +/- 2.217 | 37.690 +/- 27.524 | 25870.750 +/- 21188.114 |
| `generative_agents_official_planner` | 0.250 +/- 0.500 | 0.000 +/- 0.000 | 6.500 +/- 3.416 | 41.529 +/- 18.875 | 38829.000 +/- 19620.994 |
| `sotopia_official_llm_agent` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 5.250 +/- 3.403 | 26.514 +/- 16.427 | 36034.250 +/- 23998.902 |

## Scenario-Agent Breakdown

| Scenario | Agent | Task | Legacy goal | Feasibility | Replanning | Calls | Tokens |
|---|---|---:|---:|---:|---:|---:|---:|
| `closed_study_spot_replacement` | `agentsociety_official_plan_blocks` | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.875 +/- 0.000 |  | 6.000 +/- 0.000 | 42194.000 +/- 0.000 |
| `closed_study_spot_replacement` | `gatsim_official_planner` | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.875 +/- 0.000 |  | 2.000 +/- 0.000 | 19029.000 +/- 0.000 |
| `closed_study_spot_replacement` | `generative_agents_official_planner` | 0.500 +/- 0.000 | 0.700 +/- 0.000 | 0.571 +/- 0.000 |  | 7.000 +/- 0.000 | 41768.000 +/- 0.000 |
| `closed_study_spot_replacement` | `sotopia_official_llm_agent` | 0.000 +/- 0.000 | 0.400 +/- 0.000 | 1.000 +/- 0.000 |  | 2.000 +/- 0.000 | 13731.000 +/- 0.000 |
| `detour_commute_midroute_block` | `agentsociety_official_plan_blocks` | 1.000 +/- 0.000 | 0.650 +/- 0.000 | 0.750 +/- 0.000 | 0.000 +/- 0.000 | 6.000 +/- 0.000 | 41641.000 +/- 0.000 |
| `detour_commute_midroute_block` | `gatsim_official_planner` | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 2.000 +/- 0.000 | 18518.000 +/- 0.000 |
| `detour_commute_midroute_block` | `generative_agents_official_planner` | 1.000 +/- 0.000 | 0.650 +/- 0.000 | 0.500 +/- 0.000 | 0.000 +/- 0.000 | 11.000 +/- 0.000 | 64580.000 +/- 0.000 |
| `detour_commute_midroute_block` | `sotopia_official_llm_agent` | 0.000 +/- 0.000 | 0.450 +/- 0.000 | 1.000 +/- 0.000 | 0.000 +/- 0.000 | 5.000 +/- 0.000 | 33864.000 +/- 0.000 |
| `meeting_wait_trap` | `agentsociety_official_plan_blocks` | 0.308 +/- 0.000 | 0.350 +/- 0.000 | 0.667 +/- 0.000 |  | 8.000 +/- 0.000 | 57155.000 +/- 0.000 |
| `meeting_wait_trap` | `gatsim_official_planner` | 0.000 +/- 0.000 | 0.150 +/- 0.000 | 0.444 +/- 0.000 |  | 6.000 +/- 0.000 | 56897.000 +/- 0.000 |
| `meeting_wait_trap` | `generative_agents_official_planner` | 0.308 +/- 0.000 | 0.350 +/- 0.000 | 0.667 +/- 0.000 |  | 5.000 +/- 0.000 | 30469.000 +/- 0.000 |
| `meeting_wait_trap` | `sotopia_official_llm_agent` | 0.308 +/- 0.000 | 0.550 +/- 0.000 | 1.000 +/- 0.000 |  | 10.000 +/- 0.000 | 69791.000 +/- 0.000 |
| `school_pickup_social_detour` | `agentsociety_official_plan_blocks` | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |  | 2.000 +/- 0.000 | 13514.000 +/- 0.000 |
| `school_pickup_social_detour` | `gatsim_official_planner` | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |  | 1.000 +/- 0.000 | 9039.000 +/- 0.000 |
| `school_pickup_social_detour` | `generative_agents_official_planner` | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.800 +/- 0.000 |  | 3.000 +/- 0.000 | 18499.000 +/- 0.000 |
| `school_pickup_social_detour` | `sotopia_official_llm_agent` | 0.000 +/- 0.000 | 0.550 +/- 0.000 | 1.000 +/- 0.000 |  | 4.000 +/- 0.000 | 26751.000 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `agentsociety_official_plan_blocks` | `invalid_state_transition` | 2 | 0.500 |
| `agentsociety_official_plan_blocks` | `money_budget_failure` | 2 | 0.500 |
| `agentsociety_official_plan_blocks` | `time_budget_failure` | 1 | 0.250 |
| `gatsim_official_planner` | `invalid_state_transition` | 4 | 1.000 |
| `gatsim_official_planner` | `time_budget_failure` | 2 | 0.500 |
| `generative_agents_official_planner` | `impossible_route` | 4 | 1.000 |
| `generative_agents_official_planner` | `invalid_state_transition` | 1 | 0.250 |
| `generative_agents_official_planner` | `money_budget_failure` | 6 | 1.500 |
| `sotopia_official_llm_agent` | `goal_drift` | 4 | 1.000 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
