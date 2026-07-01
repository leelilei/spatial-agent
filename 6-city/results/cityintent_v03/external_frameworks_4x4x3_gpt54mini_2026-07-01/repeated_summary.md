# CityIntent Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all deterministically verified scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 12 | 0.692 +/- 0.186 | 0.714 +/- 0.286 | 0.500 +/- 0.274 | 0.333 +/- 0.577 |  |  |  | 0.286 +/- 0.286 |
| `gatsim_official_planner` | 12 | 0.788 +/- 0.277 | 1.000 +/- 0.000 | 0.788 +/- 0.277 | 1.000 +/- 0.000 |  |  |  | 0.000 +/- 0.000 |
| `generative_agents_official_planner` | 12 | 0.742 +/- 0.182 | 0.734 +/- 0.260 | 0.558 +/- 0.288 | 0.000 +/- 0.000 |  |  |  | 0.266 +/- 0.260 |
| `sotopia_official_llm_agent` | 12 | 0.521 +/- 0.137 | 0.875 +/- 0.226 | 0.446 +/- 0.142 | 0.667 +/- 0.577 |  |  |  | 0.125 +/- 0.226 |

## Diagnostic Metrics

| Agent | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.809 +/- 0.228 | 1.000 +/- 0.000 | 0.667 +/- 0.258 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `gatsim_official_planner` | 0.852 +/- 0.199 | 1.000 +/- 0.000 | 0.250 +/- 0.274 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `generative_agents_official_planner` | 0.938 +/- 0.145 | 1.000 +/- 0.000 | 0.667 +/- 0.258 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `sotopia_official_llm_agent` | 0.869 +/- 0.212 | 1.000 +/- 0.000 | 0.500 +/- 0.000 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.000 +/- 0.000 | 0.083 +/- 0.289 | 6.500 +/- 3.631 | 67.884 +/- 48.528 | 45108.083 +/- 25513.081 |
| `gatsim_official_planner` | 0.250 +/- 0.452 | 0.250 +/- 0.452 | 1.667 +/- 0.492 | 19.238 +/- 6.514 | 15171.417 +/- 4555.867 |
| `generative_agents_official_planner` | 0.083 +/- 0.289 | 0.000 +/- 0.000 | 4.667 +/- 2.807 | 30.389 +/- 14.991 | 27392.083 +/- 15925.747 |
| `sotopia_official_llm_agent` | 0.000 +/- 0.000 | 0.167 +/- 0.389 | 5.167 +/- 1.992 | 19.513 +/- 9.859 | 34394.583 +/- 13776.336 |

## Scenario-Agent Breakdown

| Scenario | Agent | Goal | Feasibility | Replanning | Calls | Tokens |
|---|---|---:|---:|---:|---:|---:|
| `closed_study_spot_replacement` | `agentsociety_official_plan_blocks` | 0.700 +/- 0.000 | 0.298 +/- 0.134 |  | 11.333 +/- 1.155 | 78990.333 +/- 8083.766 |
| `closed_study_spot_replacement` | `gatsim_official_planner` | 1.000 +/- 0.000 | 1.000 +/- 0.000 |  | 2.000 +/- 0.000 | 18236.667 +/- 30.730 |
| `closed_study_spot_replacement` | `generative_agents_official_planner` | 0.700 +/- 0.000 | 0.362 +/- 0.066 |  | 8.333 +/- 2.309 | 47960.333 +/- 13404.922 |
| `closed_study_spot_replacement` | `sotopia_official_llm_agent` | 0.600 +/- 0.173 | 0.500 +/- 0.000 |  | 4.667 +/- 1.528 | 31014.000 +/- 10235.638 |
| `detour_commute_midroute_block` | `agentsociety_official_plan_blocks` | 0.767 +/- 0.202 | 0.850 +/- 0.132 | 0.333 +/- 0.577 | 5.333 +/- 1.155 | 36612.000 +/- 7890.985 |
| `detour_commute_midroute_block` | `gatsim_official_planner` | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 2.000 +/- 0.000 | 18238.667 +/- 46.145 |
| `detour_commute_midroute_block` | `generative_agents_official_planner` | 0.533 +/- 0.202 | 0.742 +/- 0.138 | 0.000 +/- 0.000 | 5.000 +/- 2.000 | 29605.000 +/- 11411.118 |
| `detour_commute_midroute_block` | `sotopia_official_llm_agent` | 0.583 +/- 0.115 | 1.000 +/- 0.000 | 0.667 +/- 0.577 | 4.333 +/- 1.528 | 28556.000 +/- 10127.165 |
| `meeting_wait_trap` | `agentsociety_official_plan_blocks` | 0.650 +/- 0.260 | 0.708 +/- 0.072 |  | 7.333 +/- 1.155 | 51324.333 +/- 8130.807 |
| `meeting_wait_trap` | `gatsim_official_planner` | 0.350 +/- 0.000 | 1.000 +/- 0.000 |  | 1.667 +/- 0.577 | 15236.667 +/- 5321.682 |
| `meeting_wait_trap` | `generative_agents_official_planner` | 0.933 +/- 0.115 | 1.000 +/- 0.000 |  | 3.000 +/- 0.000 | 18140.000 +/- 87.023 |
| `meeting_wait_trap` | `sotopia_official_llm_agent` | 0.550 +/- 0.000 | 1.000 +/- 0.000 |  | 8.000 +/- 0.000 | 54172.333 +/- 210.735 |
| `school_pickup_social_detour` | `agentsociety_official_plan_blocks` | 0.650 +/- 0.260 | 1.000 +/- 0.000 |  | 2.000 +/- 0.000 | 13505.667 +/- 56.163 |
| `school_pickup_social_detour` | `gatsim_official_planner` | 0.800 +/- 0.000 | 1.000 +/- 0.000 |  | 1.000 +/- 0.000 | 8973.667 +/- 63.256 |
| `school_pickup_social_detour` | `generative_agents_official_planner` | 0.800 +/- 0.000 | 0.833 +/- 0.144 |  | 2.333 +/- 1.155 | 13863.000 +/- 6337.830 |
| `school_pickup_social_detour` | `sotopia_official_llm_agent` | 0.350 +/- 0.000 | 1.000 +/- 0.000 |  | 3.667 +/- 0.577 | 23836.000 +/- 3770.675 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `agentsociety_official_plan_blocks` | `goal_drift` | 1 | 0.083 |
| `agentsociety_official_plan_blocks` | `invalid_state_transition` | 8 | 0.667 |
| `agentsociety_official_plan_blocks` | `money_budget_failure` | 15 | 1.250 |
| `agentsociety_official_plan_blocks` | `time_budget_failure` | 2 | 0.167 |
| `gatsim_official_planner` | `goal_drift` | 3 | 0.250 |
| `generative_agents_official_planner` | `closed_place_action` | 1 | 0.083 |
| `generative_agents_official_planner` | `impossible_route` | 6 | 0.500 |
| `generative_agents_official_planner` | `invalid_state_transition` | 1 | 0.083 |
| `generative_agents_official_planner` | `money_budget_failure` | 8 | 0.667 |
| `generative_agents_official_planner` | `time_budget_failure` | 1 | 0.083 |
| `sotopia_official_llm_agent` | `goal_drift` | 4 | 0.333 |
| `sotopia_official_llm_agent` | `invalid_state_transition` | 3 | 0.250 |
| `sotopia_official_llm_agent` | `money_budget_failure` | 2 | 0.167 |
| `sotopia_official_llm_agent` | `time_budget_failure` | 1 | 0.083 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
