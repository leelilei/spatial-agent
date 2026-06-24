# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 0.827 | 0.885 | 0.038 | 0.537 | 0.29 | 0.829 | 0.887 | 0.65 |
| api_llm_plan_then_act | 0.893 | 0.938 | 0.041 | 0.809 | 0.084 | 0.908 | 0.948 | 0.862 |
| api_llm_reactive_replanner | 0.877 | 0.833 | 0.142 | 0.643 | 0.233 | 0.904 | 0.858 | 0.789 |
| utility_planner | 0.757 | 0.75 | 0.128 | 0.594 | 0.163 | 0.85 | 0.763 | 0.671 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
