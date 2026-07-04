# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.875 | 0.125 | 0.125 | 0.0 | 0.9 | 1.0 | 0.715 |  | 0.125 |  | 1.0 | 1.0 | 0.8 |  | 0.0 | 0.0 |
| gatsim_official_planner | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 | 1.0 |  | 0.0 |  | 0.576 | 1.0 | 1.0 |  | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.75 | 0.25 | 0.25 | 0.5 | 0.75 | 0.769 | 0.715 |  | 0.25 |  | 0.552 | 1.0 | 0.625 |  | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 6 | 35.253 | 41560 | 952 | 42512 | True |
| gatsim_official_planner | 3 | 27.841 | 27133 | 897 | 28030 | True |
| generative_agents_official_planner | 6 | 31.447 | 36203 | 761 | 36964 | True |
