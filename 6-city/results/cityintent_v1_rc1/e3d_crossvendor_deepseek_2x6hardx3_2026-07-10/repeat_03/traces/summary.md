# CityIntent v1.0-rc1 Trace Results

This run includes `api_llm_*` agents, which call a configured real model provider.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 1.0 | 0.937 | 0.063 | 0.063 | 0.0 | 0.642 | 0.564 | 0.762 |  | 0.063 |  | 1.0 | 1.0 | 0.611 | 0.417 | 0.0 | 0.5 |
| api_llm_react_tool_policy | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.925 | 0.881 | 1.0 |  | 0.0 |  | 1.0 | 1.0 | 0.925 | 0.917 | 0.0 | 0.333 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| api_llm_plan_and_execute | 6 | 346.413 | 12993 | 7781 | 20774 | True |
| api_llm_react_tool_policy | 64 | 1602.758 | 237298 | 23312 | 260610 | True |
