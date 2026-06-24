# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 0.859 | 0.92 | 0.0 | 0.547 | 0.311 | 0.912 | 0.898 | 0.664 |
| api_llm_plan_then_act | 0.926 | 1.0 | 0.0 | 0.815 | 0.111 | 0.944 | 0.957 | 0.903 |
| api_llm_reactive_replanner | 0.923 | 1.0 | 0.0 | 0.789 | 0.134 | 1.0 | 0.961 | 0.878 |
| utility_planner | 0.772 | 0.875 | 0.083 | 0.53 | 0.244 | 0.906 | 0.864 | 0.699 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
