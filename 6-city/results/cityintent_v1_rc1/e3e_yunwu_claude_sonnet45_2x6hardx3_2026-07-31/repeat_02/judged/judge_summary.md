# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.877 | 0.954 | 0.028 | 0.51 | 0.367 | 0.633 | 0.88 | 0.74 |
| api_llm_react_tool_policy | 0.937 | 1.0 | 0.0 | 0.685 | 0.252 | 1.0 | 0.927 | 0.86 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
