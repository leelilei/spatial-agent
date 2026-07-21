# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.83 | 0.17 | 0.17 | 0.167 | 0.475 | 0.394 | 0.595 |  | 0.17 |  | 1.0 | 1.0 | 0.406 | 0.167 | 0.0 | 0.167 |
| gatsim_official_planner | 1.0 | 0.905 | 0.095 | 0.095 | 0.0 | 0.817 | 0.75 | 0.917 |  | 0.095 |  | 0.943 | 1.0 | 0.798 | 0.75 | 0.0 | 0.167 |
| generative_agents_official_planner | 1.0 | 0.816 | 0.184 | 0.184 | 0.667 | 0.575 | 0.515 | 0.678 |  | 0.184 |  | 0.966 | 1.0 | 0.472 | 0.222 | 0.0 | 0.167 |
| sotopia_official_llm_agent | 1.0 | 0.834 | 0.166 | 0.166 | 0.0 | 0.35 | 0.191 | 0.595 |  | 0.166 |  | 0.856 | 1.0 | 0.292 | 0.083 | 0.5 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 28 | 443.39 | 88179 | 6370 | 94549 | True |
| gatsim_official_planner | 11 | 111.408 | 65115 | 3859 | 68974 | True |
| generative_agents_official_planner | 28 | 317.53 | 55680 | 5641 | 61321 | True |
| sotopia_official_llm_agent | 42 | 172.391 | 125751 | 979 | 126730 | True |
