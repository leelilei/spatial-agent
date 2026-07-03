# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.823 | 0.177 | 0.177 | 0.5 | 0.75 | 0.827 | 0.774 | 0.0 | 0.177 | 0.0 | 0.849 | 1.0 | 0.649 | 0.75 | 0.0 | 0.0 |
| gatsim_official_planner | 1.0 | 0.83 | 0.17 | 0.17 | 0.25 | 0.787 | 0.75 | 0.857 | 1.0 | 0.17 | 1.0 | 0.706 | 1.0 | 0.736 | 0.5 | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.635 | 0.365 | 0.365 | 1.0 | 0.675 | 0.702 | 0.774 | 0.0 | 0.365 | 0.0 | 0.971 | 1.0 | 0.44 | 0.75 | 0.0 | 0.0 |
| sotopia_official_llm_agent | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.488 | 0.077 | 1.0 | 0.0 | 0.0 | 0.0 | 0.898 | 1.0 | 0.488 | 0.75 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 22 | 150.872 | 150360 | 4144 | 154504 | True |
| gatsim_official_planner | 11 | 150.759 | 100477 | 3006 | 103483 | True |
| generative_agents_official_planner | 26 | 166.114 | 151288 | 4028 | 155316 | True |
| sotopia_official_llm_agent | 21 | 106.058 | 143230 | 907 | 144137 | True |
