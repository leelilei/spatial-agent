# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.843 | 0.963 | 0.008 | 0.443 | 0.4 | 0.642 | 0.733 | 0.562 |
| api_llm_react_tool_policy | 0.912 | 1.0 | 0.0 | 0.82 | 0.097 | 0.95 | 0.95 | 0.845 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
