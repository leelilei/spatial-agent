# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 0.851 | 0.919 | 0.005 | 0.522 | 0.329 | 0.931 | 0.854 | 0.738 |
| api_llm_plan_then_act | 0.944 | 0.938 | 0.06 | 0.869 | 0.075 | 0.969 | 0.965 | 0.925 |
| api_llm_reactive_replanner | 0.912 | 0.875 | 0.115 | 0.821 | 0.091 | 0.938 | 0.894 | 0.868 |
| utility_planner | 0.828 | 0.875 | 0.077 | 0.621 | 0.207 | 0.906 | 0.854 | 0.681 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
