# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.817 | 0.183 | 0.183 | 0.333 | 0.442 | 0.302 | 0.678 |  | 0.183 |  | 0.896 | 1.0 | 0.377 | 0.195 | 0.0 | 0.333 |
| gatsim_official_planner | 1.0 | 0.905 | 0.095 | 0.095 | 0.0 | 0.817 | 0.75 | 0.917 |  | 0.095 |  | 1.0 | 1.0 | 0.798 | 0.75 | 0.0 | 0.167 |
| generative_agents_official_planner | 1.0 | 0.754 | 0.246 | 0.246 | 0.667 | 0.45 | 0.366 | 0.595 |  | 0.246 |  | 0.908 | 1.0 | 0.352 | 0.139 | 0.0 | 0.167 |
| sotopia_official_llm_agent | 1.0 | 0.848 | 0.152 | 0.152 | 0.0 | 0.317 | 0.191 | 0.512 |  | 0.152 |  | 0.823 | 1.0 | 0.27 | 0.083 | 0.5 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 32 | 249.857 | 146697 | 6819 | 153516 | True |
| gatsim_official_planner | 11 | 212.246 | 78685 | 3790 | 82475 | True |
| generative_agents_official_planner | 28 | 242.643 | 90727 | 5256 | 95983 | True |
| sotopia_official_llm_agent | 46 | 340.201 | 189791 | 1157 | 190948 | True |
