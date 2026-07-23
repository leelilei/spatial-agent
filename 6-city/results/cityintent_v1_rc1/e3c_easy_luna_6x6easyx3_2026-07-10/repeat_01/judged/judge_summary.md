# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.872 | 0.944 | 0.011 | 0.665 | 0.207 | 0.8 | 0.877 | 0.777 |
| api_llm_plan_and_execute | 0.89 | 0.976 | 0.0 | 0.695 | 0.195 | 0.933 | 0.94 | 0.792 |
| api_llm_react_tool_policy | 0.912 | 0.976 | 0.0 | 0.743 | 0.168 | 0.933 | 0.913 | 0.83 |
| gatsim_official_planner | 0.833 | 0.802 | 0.112 | 0.322 | 0.512 | 0.65 | 0.663 | 0.447 |
| generative_agents_official_planner | 0.842 | 0.967 | 0.012 | 0.433 | 0.408 | 0.733 | 0.618 | 0.577 |
| sotopia_official_llm_agent | 0.74 | 0.817 | 0.065 | 0.433 | 0.307 | 0.5 | 0.538 | 0.552 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
