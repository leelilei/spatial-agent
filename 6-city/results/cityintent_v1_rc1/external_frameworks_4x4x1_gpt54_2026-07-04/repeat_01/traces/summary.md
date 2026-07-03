# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.863 | 0.138 | 0.138 | 0.25 | 0.7 | 0.577 | 0.857 | 0.0 | 0.138 | 0.0 | 0.858 | 1.0 | 0.611 | 0.75 | 0.0 | 0.0 |
| gatsim_official_planner | 1.0 | 0.875 | 0.125 | 0.125 | 0.0 | 0.613 | 0.5 | 0.774 | 0.0 | 0.125 | 0.0 | 0.847 | 1.0 | 0.562 | 0.5 | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.95 | 0.05 | 0.05 | 0.0 | 0.838 | 0.827 | 1.0 | 0.0 | 0.05 | 0.0 | 0.85 | 1.0 | 0.788 | 0.75 | 0.0 | 0.0 |
| sotopia_official_llm_agent | 1.0 | 0.896 | 0.104 | 0.104 | 0.25 | 0.675 | 0.452 | 1.0 | 0.0 | 0.104 | 0.0 | 0.837 | 1.0 | 0.59 | 0.75 | 0.25 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 24 | 212.857 | 170331 | 6524 | 176855 | True |
| gatsim_official_planner | 9 | 97.161 | 83156 | 3041 | 86197 | True |
| generative_agents_official_planner | 10 | 76.933 | 61208 | 2086 | 63294 | True |
| sotopia_official_llm_agent | 22 | 97.168 | 151827 | 463 | 152290 | True |
