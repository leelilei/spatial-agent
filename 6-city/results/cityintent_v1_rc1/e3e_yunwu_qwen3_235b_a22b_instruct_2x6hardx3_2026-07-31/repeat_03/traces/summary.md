# CityIntent v1.0-rc1 Trace Results

This run includes `api_llm_*` agents, which call a configured real model provider.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 1.0 | 0.953 | 0.047 | 0.047 | 0.0 | 0.783 | 0.797 | 0.762 |  | 0.047 |  | 1.0 | 1.0 | 0.757 | 0.695 | 0.0 | 0.333 |
| api_llm_react_tool_policy | 1.0 | 0.965 | 0.035 | 0.035 | 0.167 | 0.825 | 0.842 | 0.762 |  | 0.035 |  | 1.0 | 0.833 | 0.803 | 0.917 | 0.167 | 0.5 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| api_llm_plan_and_execute | 6 | 118.871 | 12864 | 4524 | 17388 | True |
| api_llm_react_tool_policy | 58 | 375.911 | 211570 | 5975 | 217545 | True |
