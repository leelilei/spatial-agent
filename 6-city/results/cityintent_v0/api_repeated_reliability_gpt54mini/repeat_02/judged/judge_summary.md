# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 0.826 | 0.975 | 0.01 | 0.483 | 0.344 | 0.969 | 0.864 | 0.666 |
| api_llm_plan_then_act | 0.922 | 1.0 | 0.0 | 0.811 | 0.111 | 0.95 | 0.922 | 0.888 |
| api_llm_reactive_replanner | 0.904 | 0.875 | 0.115 | 0.816 | 0.087 | 0.938 | 0.926 | 0.874 |
| utility_planner | 0.84 | 0.875 | 0.07 | 0.653 | 0.188 | 0.906 | 0.866 | 0.749 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
