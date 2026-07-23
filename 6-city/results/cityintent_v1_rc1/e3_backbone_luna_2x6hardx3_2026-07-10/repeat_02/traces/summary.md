# CityIntent v1.0-rc1 Trace Results

This run includes `api_llm_*` agents, which call a configured real model provider.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 1.0 | 0.985 | 0.015 | 0.015 | 0.0 | 0.933 | 0.936 | 0.928 |  | 0.015 |  | 1.0 | 1.0 | 0.924 | 0.833 | 0.0 | 0.0 |
| api_llm_react_tool_policy | 1.0 | 0.983 | 0.017 | 0.017 | 0.167 | 0.808 | 0.779 | 0.833 |  | 0.017 |  | 1.0 | 0.833 | 0.799 | 0.75 | 0.0 | 0.333 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| api_llm_plan_and_execute | 6 | 112.381 | 42836 | 11020 | 53856 | True |
| api_llm_react_tool_policy | 52 | 678.835 | 444798 | 47324 | 492122 | True |
