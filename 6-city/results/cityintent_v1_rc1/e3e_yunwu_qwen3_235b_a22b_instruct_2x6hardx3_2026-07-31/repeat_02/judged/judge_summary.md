# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.86 | 0.963 | 0.0 | 0.53 | 0.33 | 0.85 | 0.783 | 0.813 |
| api_llm_react_tool_policy | 0.917 | 0.983 | 0.002 | 0.637 | 0.28 | 0.85 | 0.91 | 0.762 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
