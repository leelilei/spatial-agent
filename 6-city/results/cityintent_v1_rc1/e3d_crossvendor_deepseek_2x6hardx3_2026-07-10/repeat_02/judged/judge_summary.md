# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.892 | 0.909 | 0.021 | 0.592 | 0.3 | 0.783 | 0.92 | 0.723 |
| api_llm_react_tool_policy | 0.885 | 1.0 | 0.0 | 0.55 | 0.335 | 0.9 | 0.915 | 0.78 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
