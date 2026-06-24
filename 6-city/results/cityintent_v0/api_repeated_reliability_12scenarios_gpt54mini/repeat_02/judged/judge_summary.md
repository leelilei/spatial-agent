# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 0.8 | 0.892 | 0.034 | 0.478 | 0.323 | 0.871 | 0.827 | 0.595 |
| api_llm_plan_then_act | 0.902 | 0.883 | 0.077 | 0.797 | 0.107 | 0.913 | 0.939 | 0.866 |
| api_llm_reactive_replanner | 0.868 | 0.8 | 0.16 | 0.692 | 0.177 | 0.929 | 0.879 | 0.766 |
| utility_planner | 0.772 | 0.75 | 0.16 | 0.438 | 0.334 | 0.85 | 0.797 | 0.667 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
