# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.767 | 0.233 | 0.233 | 0.5 | 0.662 | 0.577 | 0.774 | 0.0 | 0.233 | 0.0 | 0.892 | 1.0 | 0.552 | 0.75 | 0.0 | 0.0 |
| gatsim_official_planner | 1.0 | 0.896 | 0.104 | 0.104 | 0.25 | 0.613 | 0.5 | 0.774 | 0.0 | 0.104 | 0.0 | 0.491 | 1.0 | 0.566 | 0.5 | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.698 | 0.302 | 0.302 | 0.75 | 0.675 | 0.702 | 0.774 | 0.0 | 0.302 | 0.0 | 0.695 | 1.0 | 0.486 | 0.75 | 0.0 | 0.25 |
| sotopia_official_llm_agent | 1.0 | 0.875 | 0.125 | 0.125 | 0.25 | 0.613 | 0.202 | 1.0 | 1.0 | 0.125 | 1.0 | 0.967 | 1.0 | 0.525 | 0.75 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 24 | 141.304 | 168767 | 3620 | 172387 | True |
| gatsim_official_planner | 8 | 68.095 | 73177 | 2579 | 75756 | True |
| generative_agents_official_planner | 20 | 121.642 | 119268 | 3231 | 122499 | True |
| sotopia_official_llm_agent | 21 | 88.166 | 146799 | 850 | 147649 | True |
