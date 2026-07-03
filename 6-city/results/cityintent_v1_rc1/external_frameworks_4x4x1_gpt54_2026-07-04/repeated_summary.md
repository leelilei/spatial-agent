# CityIntent Repeated Reliability Table

Repeated runs: 1

Each cell is mean +/- sample standard deviation across all judged scenario traces.

Blank metric values are skipped, so conditional metrics such as replanning success are averaged only over applicable rows.

## Main Agent Table

| Agent | n | Task | Legacy goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 4 | 0.577 +/- 0.504 | 0.700 +/- 0.349 | 0.863 +/- 0.160 | 0.611 +/- 0.332 | 0.000 +/- 0.000 | 0.725 +/- 0.263 | 0.445 +/- 0.248 | 0.280 +/- 0.146 | 0.138 +/- 0.160 |
| `gatsim_official_planner` | 4 | 0.500 +/- 0.577 | 0.613 +/- 0.452 | 0.875 +/- 0.102 | 0.562 +/- 0.440 | 0.000 +/- 0.000 | 0.468 +/- 0.452 | 0.263 +/- 0.282 | 0.205 +/- 0.173 | 0.125 +/- 0.102 |
| `generative_agents_official_planner` | 4 | 0.827 +/- 0.346 | 0.838 +/- 0.214 | 0.950 +/- 0.100 | 0.788 +/- 0.184 | 0.000 +/- 0.000 | 0.790 +/- 0.074 | 0.375 +/- 0.041 | 0.415 +/- 0.053 | 0.050 +/- 0.100 |
| `sotopia_official_llm_agent` | 4 | 0.452 +/- 0.419 | 0.675 +/- 0.240 | 0.896 +/- 0.125 | 0.590 +/- 0.168 | 0.000 +/- 0.000 | 0.792 +/- 0.168 | 0.330 +/- 0.169 | 0.463 +/- 0.165 | 0.104 +/- 0.125 |

## Diagnostic Metrics

| Agent | Constraints | Process | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.857 +/- 0.285 | 0.000 +/- 0.000 | 0.858 +/- 0.182 | 1.000 +/- 0.000 | 0.750 +/- 0.354 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `gatsim_official_planner` | 0.774 +/- 0.278 | 0.000 +/- 0.000 | 0.847 +/- 0.306 | 1.000 +/- 0.000 | 0.500 +/- 0.707 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `generative_agents_official_planner` | 1.000 +/- 0.000 | 0.000 +/- 0.000 | 0.850 +/- 0.300 | 1.000 +/- 0.000 | 0.750 +/- 0.354 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `sotopia_official_llm_agent` | 1.000 +/- 0.000 | 0.000 +/- 0.000 | 0.837 +/- 0.327 | 1.000 +/- 0.000 | 0.750 +/- 0.354 | 0.250 +/- 0.500 | 0.000 +/- 0.000 |

## Execution Cost And Evidence

| Agent | Interruptions | Verified replans | Calls | Latency (s) | Tokens |
|---|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 6.000 +/- 2.828 | 53.214 +/- 28.906 | 44213.750 +/- 21673.981 |
| `gatsim_official_planner` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 2.250 +/- 1.258 | 24.290 +/- 9.849 | 21549.250 +/- 12346.657 |
| `generative_agents_official_planner` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 2.500 +/- 1.000 | 19.233 +/- 7.783 | 15823.500 +/- 5942.645 |
| `sotopia_official_llm_agent` | 0.000 +/- 0.000 | 0.000 +/- 0.000 | 5.500 +/- 2.646 | 24.292 +/- 12.629 | 38072.500 +/- 18383.090 |

## Highest Scenario-Agent Gaps

| Scenario | Agent | Face-believ. gap | Trace believ. | Task | Legacy goal | Feasibility |
|---|---|---:|---:|---:|---:|---:|
| `meeting_wait_trap` | `sotopia_official_llm_agent` | 0.680 +/- 0.000 | 0.240 +/- 0.000 | 0.308 +/- 0.000 | 0.550 +/- 0.000 | 1.000 +/- 0.000 |
| `school_pickup_social_detour` | `sotopia_official_llm_agent` | 0.500 +/- 0.000 | 0.280 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.833 +/- 0.000 |
| `meeting_wait_trap` | `generative_agents_official_planner` | 0.460 +/- 0.000 | 0.420 +/- 0.000 | 0.308 +/- 0.000 | 0.550 +/- 0.000 | 1.000 +/- 0.000 |
| `school_pickup_social_detour` | `generative_agents_official_planner` | 0.440 +/- 0.000 | 0.380 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 |
| `meeting_wait_trap` | `agentsociety_official_plan_blocks` | 0.430 +/- 0.000 | 0.410 +/- 0.000 | 0.308 +/- 0.000 | 0.350 +/- 0.000 | 0.700 +/- 0.000 |
| `detour_commute_midroute_block` | `generative_agents_official_planner` | 0.420 +/- 0.000 | 0.320 +/- 0.000 | 1.000 +/- 0.000 | 0.800 +/- 0.000 | 1.000 +/- 0.000 |
| `school_pickup_social_detour` | `agentsociety_official_plan_blocks` | 0.380 +/- 0.000 | 0.410 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.750 +/- 0.000 |
| `meeting_wait_trap` | `gatsim_official_planner` | 0.360 +/- 0.000 | 0.420 +/- 0.000 | 0.000 +/- 0.000 | 0.150 +/- 0.000 | 0.750 +/- 0.000 |
| `closed_study_spot_replacement` | `gatsim_official_planner` | 0.350 +/- 0.000 | 0.580 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.875 +/- 0.000 |
| `closed_study_spot_replacement` | `generative_agents_official_planner` | 0.340 +/- 0.000 | 0.380 +/- 0.000 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.800 +/- 0.000 |
| `detour_commute_midroute_block` | `sotopia_official_llm_agent` | 0.340 +/- 0.000 | 0.220 +/- 0.000 | 0.000 +/- 0.000 | 0.450 +/- 0.000 | 1.000 +/- 0.000 |
| `closed_study_spot_replacement` | `sotopia_official_llm_agent` | 0.330 +/- 0.000 | 0.580 +/- 0.000 | 0.500 +/- 0.000 | 0.700 +/- 0.000 | 0.750 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Events/trace |
|---|---|---:|---:|
| `agentsociety_official_plan_blocks` | `goal_drift` | 1 | 0.250 |
| `agentsociety_official_plan_blocks` | `invalid_state_transition` | 3 | 0.750 |
| `agentsociety_official_plan_blocks` | `money_budget_failure` | 2 | 0.500 |
| `gatsim_official_planner` | `closed_place_action` | 1 | 0.250 |
| `gatsim_official_planner` | `invalid_state_transition` | 2 | 0.500 |
| `gatsim_official_planner` | `time_budget_failure` | 1 | 0.250 |
| `generative_agents_official_planner` | `goal_drift` | 1 | 0.250 |
| `generative_agents_official_planner` | `time_budget_failure` | 1 | 0.250 |
| `sotopia_official_llm_agent` | `done_state_loop` | 1 | 0.250 |
| `sotopia_official_llm_agent` | `goal_drift` | 2 | 0.500 |
| `sotopia_official_llm_agent` | `invalid_state_transition` | 1 | 0.250 |
| `sotopia_official_llm_agent` | `money_budget_failure` | 1 | 0.250 |

## Files

- `all_runs.csv`: one row per repeat/scenario/agent.
- `agent_repeated_summary.csv`: agent-level means and standard deviations.
- `scenario_agent_repeated_summary.csv`: scenario-agent means and standard deviations.
- `failure_taxonomy_summary.csv`: aggregated failure counts.
