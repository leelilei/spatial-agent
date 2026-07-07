# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.517 | 0.483 | 0.483 | 0.667 | 0.467 | 0.436 | 0.526 |  | 0.483 |  | 0.975 | 1.0 | 0.325 | 0.5 | 0.0 | 0.0 |
| gatsim_official_planner | 1.0 | 0.829 | 0.171 | 0.171 | 0.333 | 0.65 | 0.667 | 0.643 |  | 0.171 |  | 0.751 | 0.833 | 0.618 | 0.667 | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.674 | 0.326 | 0.326 | 0.833 | 0.325 | 0.172 | 0.526 |  | 0.326 |  | 0.98 | 1.0 | 0.25 | 0.167 | 0.0 | 0.167 |
| sotopia_official_llm_agent | 1.0 | 0.925 | 0.075 | 0.075 | 0.0 | 0.4 | 0.103 | 0.817 |  | 0.075 |  | 0.811 | 1.0 | 0.385 | 0.167 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 48 | 305.835 | 335197 | 6984 | 342181 | True |
| gatsim_official_planner | 14 | 114.635 | 129024 | 3511 | 132535 | True |
| generative_agents_official_planner | 34 | 224.083 | 201239 | 4461 | 205700 | True |
| sotopia_official_llm_agent | 30 | 126.63 | 204142 | 712 | 204854 | True |
