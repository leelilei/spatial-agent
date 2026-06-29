# CityIntent v0 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.834 | 0.167 | 0.167 | 0.5 | 0.775 | 0.111 |  | 0.984 | 0.5 | 0.714 |  | 0.5 | 0.0 |
| gatsim_official_planner | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 |  | 1.0 | 1.0 | 1.0 |  | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.875 | 0.125 | 0.125 | 0.5 | 1.0 | 0.125 |  | 0.776 | 0.5 | 0.875 |  | 0.0 | 0.0 |
| sotopia_official_llm_agent | 1.0 | 0.812 | 0.188 | 0.188 | 0.5 | 0.875 | 0.125 |  | 0.881 | 0.5 | 0.781 |  | 0.5 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.
