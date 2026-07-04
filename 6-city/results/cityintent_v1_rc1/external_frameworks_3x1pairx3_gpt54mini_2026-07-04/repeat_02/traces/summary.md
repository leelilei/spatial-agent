# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.812 | 0.188 | 0.188 | 0.5 | 0.75 | 0.769 | 0.715 |  | 0.188 |  | 0.769 | 1.0 | 0.656 |  | 0.0 | 0.0 |
| gatsim_official_planner | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 | 1.0 |  | 0.0 |  | 0.251 | 1.0 | 1.0 |  | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.715 | 0.285 | 0.285 | 0.5 | 0.75 | 0.769 | 0.715 |  | 0.285 |  | 0.552 | 1.0 | 0.607 |  | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 12 | 71.946 | 84246 | 1870 | 86116 | True |
| gatsim_official_planner | 3 | 23.735 | 27094 | 1022 | 28116 | True |
| generative_agents_official_planner | 8 | 43.677 | 47781 | 949 | 48730 | True |
