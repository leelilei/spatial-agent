# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 0.855 | 0.844 | 0.11 | 0.47 | 0.385 | 0.75 | 0.917 | 0.518 |
| api_llm_plan_then_act | 0.92 | 0.938 | 0.043 | 0.84 | 0.088 | 0.913 | 0.95 | 0.888 |
| api_llm_reactive_replanner | 0.85 | 0.719 | 0.233 | 0.6 | 0.26 | 0.75 | 0.88 | 0.705 |
| utility_planner | 0.725 | 0.5 | 0.31 | 0.465 | 0.26 | 0.738 | 0.8 | 0.585 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
