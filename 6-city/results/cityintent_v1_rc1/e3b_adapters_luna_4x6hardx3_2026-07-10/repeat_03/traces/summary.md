# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.852 | 0.148 | 0.148 | 0.5 | 0.708 | 0.676 | 0.762 |  | 0.148 |  | 0.897 | 1.0 | 0.61 | 0.75 | 0.0 | 0.5 |
| gatsim_official_planner | 1.0 | 0.905 | 0.095 | 0.095 | 0.0 | 0.767 | 0.667 | 0.917 |  | 0.095 |  | 1.0 | 1.0 | 0.748 | 0.583 | 0.0 | 0.167 |
| generative_agents_official_planner | 1.0 | 0.943 | 0.056 | 0.056 | 0.333 | 0.708 | 0.64 | 0.833 |  | 0.056 |  | 0.979 | 1.0 | 0.67 | 0.528 | 0.0 | 0.5 |
| sotopia_official_llm_agent | 1.0 | 0.906 | 0.094 | 0.094 | 0.167 | 0.525 | 0.417 | 0.678 |  | 0.094 |  | 0.881 | 1.0 | 0.49 | 0.333 | 0.0 | 0.333 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 30 | 351.275 | 212938 | 43349 | 256287 | True |
| gatsim_official_planner | 11 | 136.618 | 102066 | 18222 | 120288 | True |
| generative_agents_official_planner | 16 | 202.663 | 99437 | 21145 | 120582 | True |
| sotopia_official_llm_agent | 60 | 444.293 | 421202 | 66649 | 487851 | True |
