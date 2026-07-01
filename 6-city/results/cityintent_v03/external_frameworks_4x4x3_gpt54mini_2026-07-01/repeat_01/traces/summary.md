# CityIntent v0.3 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.75 | 0.25 | 0.25 | 0.25 | 0.712 | 0.25 | 1.0 | 0.691 | 1.0 | 0.57 | 0.5 | 0.0 | 0.0 |
| gatsim_official_planner | 0.75 | 1.0 | 0.0 | 0.0 | 0.0 | 0.788 | 0.0 | 1.0 | 0.791 | 1.0 | 0.788 | 0.25 | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.688 | 0.312 | 0.312 | 0.75 | 0.788 | 0.312 | 0.0 | 1.0 | 1.0 | 0.568 | 0.75 | 0.0 | 0.0 |
| sotopia_official_llm_agent | 1.0 | 0.875 | 0.125 | 0.125 | 0.0 | 0.488 | 0.125 | 1.0 | 0.967 | 1.0 | 0.438 | 0.5 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 24 | 152.012 | 161805 | 4798 | 166603 | True |
| gatsim_official_planner | 6 | 73.835 | 52321 | 2333 | 54654 | True |
| generative_agents_official_planner | 20 | 105.009 | 113536 | 3170 | 116706 | True |
| sotopia_official_llm_agent | 17 | 65.517 | 112448 | 664 | 113112 | True |
