# CityIntent v0 Baseline Smoke Results

This run uses deterministic offline policies. `llm_direct_actor` is an offline proxy, not an API-backed LLM run.

## Aggregate Metrics

| agent_type | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness |
|---|---:|---:|---:|---:|---:|---:|---:|
| llm_direct_actor | 0.481 | 0.188 | 0.0 | 0.807 | 0.875 | 0.4 | 0.125 |
| memory_reflection | 0.969 | 0.0 | 1.0 | 0.891 | 1.0 | 0.969 | 1.0 |
| reactive_replanner | 0.969 | 0.0 | 1.0 | 0.983 | 1.0 | 0.969 | 0.75 |
| utility_planner | 0.938 | 0.0 | 1.0 | 1.0 | 1.0 | 0.938 | 0.75 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.
