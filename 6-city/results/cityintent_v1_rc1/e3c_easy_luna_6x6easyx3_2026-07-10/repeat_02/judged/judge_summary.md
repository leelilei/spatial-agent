# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.785 | 0.951 | 0.011 | 0.578 | 0.207 | 0.758 | 0.808 | 0.675 |
| api_llm_plan_and_execute | 0.862 | 0.979 | 0.0 | 0.687 | 0.175 | 0.933 | 0.893 | 0.782 |
| api_llm_react_tool_policy | 0.823 | 0.976 | 0.0 | 0.662 | 0.162 | 0.933 | 0.875 | 0.702 |
| gatsim_official_planner | 0.688 | 0.783 | 0.053 | 0.32 | 0.368 | 0.592 | 0.51 | 0.378 |
| generative_agents_official_planner | 0.818 | 0.958 | 0.018 | 0.538 | 0.28 | 0.792 | 0.703 | 0.703 |
| sotopia_official_llm_agent | 0.828 | 0.839 | 0.07 | 0.578 | 0.25 | 0.633 | 0.747 | 0.647 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
