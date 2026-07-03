# CityIntent Repeated Reliability Table

Repeated runs: 1

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 12 | 0.528 +/- 0.455 | 0.613 +/- 0.290 | 0.627 +/- 0.367 | 0.451 +/- 0.375 | 0.000 +/- 0.000 | 0.856 +/- 0.101 | 0.547 +/- 0.223 | 0.309 +/- 0.173 | 0.373 +/- 0.367 |
| `gatsim_official_planner` | 12 | 0.840 +/- 0.319 | 0.862 +/- 0.254 | 0.943 +/- 0.161 | 0.845 +/- 0.272 | 1.000 +/- 0.000 | 0.521 +/- 0.301 | 0.209 +/- 0.131 | 0.312 +/- 0.204 | 0.057 +/- 0.161 |
| `generative_agents_official_planner` | 12 | 0.537 +/- 0.402 | 0.613 +/- 0.260 | 0.691 +/- 0.139 | 0.444 +/- 0.237 | 0.000 +/- 0.000 | 0.693 +/- 0.302 | 0.404 +/- 0.288 | 0.289 +/- 0.194 | 0.309 +/- 0.139 |
| `sotopia_official_llm_agent` | 12 | 0.098 +/- 0.181 | 0.438 +/- 0.133 | 0.838 +/- 0.221 | 0.372 +/- 0.156 | 0.500 +/- 0.707 | 0.752 +/- 0.137 | 0.332 +/- 0.219 | 0.420 +/- 0.142 | 0.163 +/- 0.221 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.894 +/- 0.199 | 0.000 +/- 0.000 | 0.807 +/- 0.360 | 1.000 +/- 0.000 | 0.333 +/- 0.408 | 0.083 +/- 0.289 | 0.000 +/- 0.000 |
| `gatsim_official_planner` | 0.952 +/- 0.165 | 0.667 +/- 0.577 | 0.727 +/- 0.293 | 1.000 +/- 0.000 | 0.583 +/- 0.492 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `generative_agents_official_planner` | 0.894 +/- 0.199 | 0.000 +/- 0.000 | 0.899 +/- 0.223 | 1.000 +/- 0.000 | 0.417 +/- 0.492 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `sotopia_official_llm_agent` | 1.000 +/- 0.000 | 0.333 +/- 0.577 | 0.955 +/- 0.121 | 1.000 +/- 0.000 | 0.417 +/- 0.492 | 0.083 +/- 0.289 | 0.000 +/- 0.000 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.083 +/- 0.289 | 0.000 +/- 0.000 | 6.833 +/- 3.762 | 42.570 +/- 22.766 | 48511.417 +/- 27163.664 |
| `gatsim_official_planner` | 0.167 +/- 0.389 | 0.167 +/- 0.389 | 1.917 +/- 1.379 | 20.563 +/- 19.305 | 17898.500 +/- 13161.952 |
| `generative_agents_official_planner` | 0.083 +/- 0.289 | 0.000 +/- 0.000 | 4.833 +/- 2.623 | 27.524 +/- 16.204 | 29146.917 +/- 15266.860 |
| `sotopia_official_llm_agent` | 0.083 +/- 0.289 | 0.083 +/- 0.289 | 4.667 +/- 2.270 | 19.415 +/- 11.071 | 32096.000 +/- 16013.132 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `closed_poi_replacement` | `generative_agents_official_planner` | 0.640 +/- 0.000 | 0.180 +/- 0.000 | 0.000 +/- 0.000 | 0.250 +/- 0.000 | 0.500 +/- 0.000 |
| `closed_study_spot_replacement` | `sotopia_official_llm_agent` | 0.590 +/- 0.000 | 0.120 +/- 0.000 | 0.000 +/- 0.000 | 0.400 +/- 0.000 | 1.000 +/- 0.000 |
| `lunch_meeting_time_pressure` | `gatsim_official_planner` | 0.560 +/- 0.000 | 0.220 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `school_pickup_social_detour` | `gatsim_official_planner` | 0.560 +/- 0.000 | 0.180 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `commute_disruption` | `agentsociety_official_plan_blocks` | 0.540 +/- 0.000 | 0.420 +/- 0.000 | 0.000 +/- 0.000 | 0.250 +/- 0.000 | 0.800 +/- 0.000 |
| `conflicting_social_obligation` | `agentsociety_official_plan_blocks` | 0.540 +/- 0.000 | 0.240 +/- 0.000 | 0.000 +/- 0.000 | 0.400 +/- 0.000 | 0.200 +/- 0.000 |
| `meeting_wait_trap` | `gatsim_official_planner` | 0.540 +/- 0.000 | 0.220 +/- 0.000 | 0.000 +/- 0.000 | 0.150 +/- 0.000 | 0.444 +/- 0.000 |
| `meeting_wait_trap` | `sotopia_official_llm_agent` | 0.540 +/- 0.000 | 0.340 +/- 0.000 | 0.308 +/- 0.000 | 0.550 +/- 0.000 | 1.000 +/- 0.000 |
| `budget_errand_chain` | `generative_agents_official_planner` | 0.520 +/- 0.000 | 0.220 +/- 0.000 | 0.600 +/- 0.000 | 0.700 +/- 0.000 | 0.833 +/- 0.000 |
| `detour_commute_midroute_block` | `sotopia_official_llm_agent` | 0.520 +/- 0.000 | 0.320 +/- 0.000 | 0.000 +/- 0.000 | 0.450 +/- 0.000 | 1.000 +/- 0.000 |
| `commute_disruption` | `sotopia_official_llm_agent` | 0.510 +/- 0.000 | 0.220 +/- 0.000 | 0.000 +/- 0.000 | 0.500 +/- 0.000 | 1.000 +/- 0.000 |
| `meeting_wait_trap` | `generative_agents_official_planner` | 0.480 +/- 0.000 | 0.380 +/- 0.000 | 0.308 +/- 0.000 | 0.350 +/- 0.000 | 0.667 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `agentsociety_official_plan_blocks` | `closed_place_action` | 1 | 0.083 |
| `agentsociety_official_plan_blocks` | `done_state_loop` | 1 | 0.083 |
| `agentsociety_official_plan_blocks` | `goal_drift` | 1 | 0.083 |
| `agentsociety_official_plan_blocks` | `invalid_state_transition` | 15 | 1.250 |
| `agentsociety_official_plan_blocks` | `money_budget_failure` | 9 | 0.750 |
| `agentsociety_official_plan_blocks` | `time_budget_failure` | 3 | 0.250 |
| `gatsim_official_planner` | `goal_drift` | 1 | 0.083 |
| `gatsim_official_planner` | `invalid_state_transition` | 4 | 0.333 |
| `gatsim_official_planner` | `time_budget_failure` | 2 | 0.167 |
| `generative_agents_official_planner` | `impossible_route` | 5 | 0.417 |
| `generative_agents_official_planner` | `invalid_state_transition` | 6 | 0.500 |
| `generative_agents_official_planner` | `money_budget_failure` | 11 | 0.917 |
| `sotopia_official_llm_agent` | `done_state_loop` | 1 | 0.083 |
| `sotopia_official_llm_agent` | `goal_drift` | 7 | 0.583 |
| `sotopia_official_llm_agent` | `invalid_state_transition` | 7 | 0.583 |
| `sotopia_official_llm_agent` | `money_budget_failure` | 1 | 0.083 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
