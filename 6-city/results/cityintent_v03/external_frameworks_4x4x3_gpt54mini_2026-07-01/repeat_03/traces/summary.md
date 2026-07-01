# CityIntent v0.3 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.731 | 0.269 | 0.269 | 0.5 | 0.738 | 0.269 | 0.0 | 0.892 | 1.0 | 0.546 | 0.75 | 0.0 | 0.0 |
| gatsim_official_planner | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.788 | 0.0 | 1.0 | 0.858 | 1.0 | 0.788 | 0.25 | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.697 | 0.303 | 0.303 | 0.5 | 0.738 | 0.303 | 0.0 | 0.908 | 1.0 | 0.522 | 0.5 | 0.0 | 0.0 |
| sotopia_official_llm_agent | 1.0 | 0.875 | 0.125 | 0.125 | 0.25 | 0.512 | 0.125 | 0.0 | 0.72 | 1.0 | 0.425 | 0.5 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 28 | 225.497 | 188992 | 5711 | 194703 | True |
| gatsim_official_planner | 7 | 90.527 | 61342 | 2318 | 63660 | True |
| generative_agents_official_planner | 20 | 105.198 | 113937 | 3172 | 117109 | True |
| sotopia_official_llm_agent | 24 | 87.242 | 158694 | 806 | 159500 | True |
