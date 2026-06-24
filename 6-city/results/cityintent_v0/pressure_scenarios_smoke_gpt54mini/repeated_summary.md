# CityIntent v0 Repeated Reliability Table

Repeated runs: 1

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_direct_actor` | 4 | 0.750 +/- 0.196 | 0.844 +/- 0.237 | 0.700 +/- 0.204 | 1.000 +/- 0.000 | 0.855 +/- 0.093 | 0.470 +/- 0.306 | 0.385 +/- 0.216 | 0.156 +/- 0.237 |
| `api_llm_plan_then_act` | 4 | 0.913 +/- 0.103 | 0.938 +/- 0.125 | 0.859 +/- 0.176 | 1.000 +/- 0.000 | 0.920 +/- 0.057 | 0.840 +/- 0.188 | 0.088 +/- 0.130 | 0.062 +/- 0.125 |
| `api_llm_reactive_replanner` | 4 | 0.750 +/- 0.196 | 0.719 +/- 0.483 | 0.550 +/- 0.414 | 1.000 +/- 0.000 | 0.850 +/- 0.123 | 0.600 +/- 0.406 | 0.260 +/- 0.277 | 0.281 +/- 0.483 |
| `utility_planner` | 4 | 0.738 +/- 0.275 | 0.500 +/- 0.577 | 0.450 +/- 0.526 | 0.000 +/- 0.000 | 0.725 +/- 0.181 | 0.465 +/- 0.325 | 0.260 +/- 0.186 | 0.500 +/- 0.577 |

## Diagnostic Metrics

| Agent | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|
| `api_llm_direct_actor` | 0.787 +/- 0.262 | 1.000 +/- 0.000 | 0.500 +/- 0.000 | 0.500 +/- 0.577 | 0.000 +/- 0.000 |
| `api_llm_plan_then_act` | 0.887 +/- 0.182 | 1.000 +/- 0.000 | 0.750 +/- 0.354 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `api_llm_reactive_replanner` | 0.866 +/- 0.268 | 1.000 +/- 0.000 | 0.500 +/- 0.000 | 0.250 +/- 0.500 | 0.000 +/- 0.000 |
| `utility_planner` | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.500 +/- 0.000 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Goal | Feasibility |
|---|---|---:|---:|---:|---:|
| `detour_commute_midroute_block` | `api_llm_direct_actor` | 0.580 +/- 0.000 | 0.160 +/- 0.000 | 0.650 +/- 0.000 | 0.875 +/- 0.000 |
| `detour_commute_midroute_block` | `api_llm_reactive_replanner` | 0.560 +/- 0.000 | 0.120 +/- 0.000 | 0.650 +/- 0.000 | 0.875 +/- 0.000 |
| `meeting_wait_trap` | `api_llm_direct_actor` | 0.560 +/- 0.000 | 0.260 +/- 0.000 | 0.550 +/- 0.000 | 1.000 +/- 0.000 |
| `school_pickup_social_detour` | `utility_planner` | 0.440 +/- 0.000 | 0.280 +/- 0.000 | 0.800 +/- 0.000 | 0.000 +/- 0.000 |
| `meeting_wait_trap` | `api_llm_reactive_replanner` | 0.430 +/- 0.000 | 0.410 +/- 0.000 | 0.550 +/- 0.000 | 1.000 +/- 0.000 |
| `meeting_wait_trap` | `utility_planner` | 0.350 +/- 0.000 | 0.350 +/- 0.000 | 0.800 +/- 0.000 | 1.000 +/- 0.000 |
| `meeting_wait_trap` | `api_llm_plan_then_act` | 0.280 +/- 0.000 | 0.560 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `closed_study_spot_replacement` | `api_llm_direct_actor` | 0.240 +/- 0.000 | 0.680 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `detour_commute_midroute_block` | `utility_planner` | 0.240 +/- 0.000 | 0.280 +/- 0.000 | 0.350 +/- 0.000 | 0.000 +/- 0.000 |
| `school_pickup_social_detour` | `api_llm_direct_actor` | 0.160 +/- 0.000 | 0.780 +/- 0.000 | 0.800 +/- 0.000 | 0.500 +/- 0.000 |
| `closed_study_spot_replacement` | `api_llm_reactive_replanner` | 0.050 +/- 0.000 | 0.900 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `school_pickup_social_detour` | `api_llm_plan_then_act` | 0.050 +/- 0.000 | 0.900 +/- 0.000 | 0.800 +/- 0.000 | 1.000 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Rate/trace |
|---|---|---:|---:|
| `api_llm_direct_actor` | `closed_place_action` | 1 | 0.250 |
| `api_llm_direct_actor` | `done_state_loop` | 2 | 0.500 |
| `api_llm_plan_then_act` | `closed_place_action` | 1 | 0.250 |
| `api_llm_reactive_replanner` | `closed_place_action` | 1 | 0.250 |
| `api_llm_reactive_replanner` | `done_state_loop` | 1 | 0.250 |
| `utility_planner` | `closed_place_action` | 1 | 0.250 |
| `utility_planner` | `impossible_route` | 1 | 0.250 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
