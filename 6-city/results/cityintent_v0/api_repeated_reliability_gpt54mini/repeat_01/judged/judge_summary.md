# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 0.829 | 0.896 | 0.029 | 0.535 | 0.294 | 0.863 | 0.848 | 0.7 |
| api_llm_plan_then_act | 0.925 | 0.938 | 0.058 | 0.858 | 0.07 | 0.969 | 0.954 | 0.899 |
| api_llm_reactive_replanner | 0.877 | 0.875 | 0.116 | 0.801 | 0.081 | 0.938 | 0.885 | 0.84 |
| utility_planner | 0.794 | 0.875 | 0.11 | 0.583 | 0.211 | 0.906 | 0.821 | 0.674 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
