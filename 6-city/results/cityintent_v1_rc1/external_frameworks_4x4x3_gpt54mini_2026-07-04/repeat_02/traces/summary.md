# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.705 | 0.295 | 0.295 | 0.25 | 0.725 | 0.702 | 0.774 | 1.0 | 0.295 | 1.0 | 0.814 | 1.0 | 0.547 | 0.75 | 0.0 | 0.0 |
| gatsim_official_planner | 0.75 | 1.0 | 0.0 | 0.0 | 0.0 | 0.787 | 0.75 | 1.0 | 0.0 | 0.0 | 0.0 | 0.607 | 1.0 | 0.787 | 0.5 | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.701 | 0.299 | 0.299 | 1.0 | 0.637 | 0.452 | 0.774 | 1.0 | 0.299 | 1.0 | 0.835 | 1.0 | 0.458 | 0.75 | 0.0 | 0.0 |
| sotopia_official_llm_agent | 1.0 | 0.817 | 0.183 | 0.183 | 0.25 | 0.613 | 0.202 | 1.0 | 1.0 | 0.183 | 1.0 | 0.967 | 1.0 | 0.497 | 0.75 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 24 | 136.894 | 168477 | 3409 | 171886 | True |
| gatsim_official_planner | 6 | 64.715 | 54144 | 1955 | 56099 | True |
| generative_agents_official_planner | 22 | 128.338 | 131730 | 3408 | 135138 | True |
| sotopia_official_llm_agent | 23 | 92.612 | 160393 | 840 | 161233 | True |
