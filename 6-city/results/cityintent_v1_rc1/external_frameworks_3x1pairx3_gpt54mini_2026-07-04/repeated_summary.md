# CityIntent Repeated Reliability Table

Repeated runs: 3

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 6 | 0.846 +/- 0.239 | 0.800 +/- 0.245 | 0.812 +/- 0.220 | 0.694 +/- 0.356 |  | 0.918 +/- 0.056 | 0.812 +/- 0.167 | 0.107 +/- 0.121 | 0.188 +/- 0.220 |
| `gatsim_official_planner` | 6 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |  | 0.722 +/- 0.199 | 0.370 +/- 0.252 | 0.352 +/- 0.160 | 0.000 +/- 0.000 |
| `generative_agents_official_planner` | 6 | 0.769 +/- 0.253 | 0.750 +/- 0.274 | 0.766 +/- 0.268 | 0.633 +/- 0.404 |  | 0.892 +/- 0.103 | 0.733 +/- 0.247 | 0.158 +/- 0.151 | 0.234 +/- 0.268 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.715 +/- 0.313 |  | 0.846 +/- 0.239 | 1.000 +/- 0.000 |  | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `gatsim_official_planner` | 1.000 +/- 0.000 |  | 0.410 +/- 0.318 | 1.000 +/- 0.000 |  | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `generative_agents_official_planner` | 0.715 +/- 0.313 |  | 0.576 +/- 0.467 | 1.000 +/- 0.000 |  | 0.000 +/- 0.000 | 0.000 +/- 0.000 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 5.000 +/- 3.950 | 29.360 +/- 22.435 | 35767.667 +/- 28621.288 |
| `gatsim_official_planner` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 1.500 +/- 0.548 | 12.658 +/- 3.345 | 14045.500 +/- 5212.985 |
| `generative_agents_official_planner` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 3.333 +/- 2.658 | 17.286 +/- 12.238 | 20422.333 +/- 15576.351 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `paired_study_b` | `gatsim_official_planner` | 0.373 +/- 0.081 | 0.187 +/- 0.058 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `paired_study_a` | `gatsim_official_planner` | 0.330 +/- 0.236 | 0.553 +/- 0.234 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `paired_study_b` | `generative_agents_official_planner` | 0.290 +/- 0.070 | 0.520 +/- 0.125 | 0.538 +/- 0.000 | 0.500 +/- 0.000 | 0.532 +/- 0.122 |
| `paired_study_b` | `agentsociety_official_plan_blocks` | 0.173 +/- 0.150 | 0.703 +/- 0.180 | 0.692 +/- 0.267 | 0.600 +/- 0.173 | 0.625 +/- 0.125 |
| `paired_study_a` | `agentsociety_official_plan_blocks` | 0.040 +/- 0.026 | 0.920 +/- 0.046 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `paired_study_a` | `generative_agents_official_planner` | 0.027 +/- 0.021 | 0.947 +/- 0.025 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `agentsociety_official_plan_blocks` | `closed_place_action` | 4 | 0.667 |
| `agentsociety_official_plan_blocks` | `money_budget_failure` | 3 | 0.500 |
| `agentsociety_official_plan_blocks` | `time_budget_failure` | 1 | 0.167 |
| `generative_agents_official_planner` | `impossible_route` | 1 | 0.167 |
| `generative_agents_official_planner` | `money_budget_failure` | 6 | 1.000 |
| `generative_agents_official_planner` | `time_budget_failure` | 2 | 0.333 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
