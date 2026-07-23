# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.922 | 0.976 | 0.011 | 0.693 | 0.228 | 0.917 | 0.943 | 0.76 |
| api_llm_react_tool_policy | 0.877 | 1.0 | 0.0 | 0.65 | 0.227 | 0.875 | 0.892 | 0.768 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
