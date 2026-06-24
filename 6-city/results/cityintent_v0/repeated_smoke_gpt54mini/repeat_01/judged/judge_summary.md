# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 0.95 | 1.0 | 0.0 | 0.62 | 0.33 | 1.0 | 0.96 | 0.81 |
| api_llm_plan_then_act | 0.98 | 0.5 | 0.48 | 0.99 | 0.0 | 0.75 | 0.99 | 0.97 |
| api_llm_reactive_replanner | 0.97 | 1.0 | 0.0 | 0.96 | 0.01 | 1.0 | 0.98 | 0.95 |
| utility_planner | 0.86 | 1.0 | 0.0 | 0.72 | 0.14 | 1.0 | 0.95 | 0.88 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
