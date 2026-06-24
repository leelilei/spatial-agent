# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 0.787 | 0.842 | 0.048 | 0.485 | 0.302 | 0.796 | 0.818 | 0.596 |
| api_llm_plan_then_act | 0.913 | 0.896 | 0.083 | 0.747 | 0.168 | 0.933 | 0.938 | 0.865 |
| api_llm_reactive_replanner | 0.904 | 0.833 | 0.149 | 0.818 | 0.092 | 0.904 | 0.901 | 0.868 |
| utility_planner | 0.738 | 0.75 | 0.147 | 0.492 | 0.247 | 0.85 | 0.758 | 0.621 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
