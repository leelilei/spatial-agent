# CityIntent v0 Repeated Reliability Table

Repeated runs: 1

Each cell is mean +/- sample standard deviation across all judged scenario traces.

## Main Agent Table

| Agent | n | Goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_direct_actor` | 1 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |  | 0.950 +/- 0.000 | 0.620 +/- 0.000 | 0.330 +/- 0.000 | 0.000 +/- 0.000 |
| `api_llm_plan_then_act` | 1 | 0.750 +/- 0.000 | 0.500 +/- 0.000 | 0.375 +/- 0.000 |  | 0.980 +/- 0.000 | 0.990 +/- 0.000 | 0.000 +/- 0.000 | 0.500 +/- 0.000 |
| `api_llm_reactive_replanner` | 1 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |  | 0.970 +/- 0.000 | 0.960 +/- 0.000 | 0.010 +/- 0.000 | 0.000 +/- 0.000 |
| `utility_planner` | 1 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |  | 0.860 +/- 0.000 | 0.720 +/- 0.000 | 0.140 +/- 0.000 | 0.000 +/- 0.000 |

## Diagnostic Metrics

| Agent | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|
| `api_llm_direct_actor` | 1.000 +/- 0.000 | 1.000 +/- 0.000 |  | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `api_llm_plan_then_act` | 1.000 +/- 0.000 | 1.000 +/- 0.000 |  | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `api_llm_reactive_replanner` | 1.000 +/- 0.000 | 1.000 +/- 0.000 |  | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `utility_planner` | 1.000 +/- 0.000 | 1.000 +/- 0.000 |  | 0.000 +/- 0.000 | 0.000 +/- 0.000 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Goal | Feasibility |
|---|---|---:|---:|---:|---:|
| `closed_poi_replacement` | `api_llm_direct_actor` | 0.330 +/- 0.000 | 0.620 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `closed_poi_replacement` | `utility_planner` | 0.140 +/- 0.000 | 0.720 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `closed_poi_replacement` | `api_llm_reactive_replanner` | 0.010 +/- 0.000 | 0.960 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `closed_poi_replacement` | `api_llm_plan_then_act` | 0.000 +/- 0.000 | 0.990 +/- 0.000 | 0.750 +/- 0.000 | 0.500 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Rate/trace |
|---|---|---:|---:|
| `api_llm_plan_then_act` | `closed_place_action` | 1 | 1.000 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
