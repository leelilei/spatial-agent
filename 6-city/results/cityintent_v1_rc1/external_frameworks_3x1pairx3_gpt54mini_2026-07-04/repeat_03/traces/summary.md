# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.75 | 0.25 | 0.25 | 0.5 | 0.75 | 0.769 | 0.715 |  | 0.25 |  | 0.769 | 1.0 | 0.625 |  | 0.0 | 0.0 |
| gatsim_official_planner | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 | 1.0 |  | 0.0 |  | 0.402 | 1.0 | 1.0 |  | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.834 | 0.167 | 0.167 | 0.5 | 0.75 | 0.769 | 0.715 |  | 0.167 |  | 0.625 | 1.0 | 0.666 |  | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 12 | 68.963 | 84178 | 1800 | 85978 | True |
| gatsim_official_planner | 3 | 24.375 | 27067 | 1060 | 28127 | True |
| generative_agents_official_planner | 6 | 28.591 | 36174 | 666 | 36840 | True |
