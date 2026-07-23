# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.732 | 0.943 | 0.012 | 0.503 | 0.228 | 0.883 | 0.708 | 0.66 |
| api_llm_plan_and_execute | 0.907 | 0.982 | 0.0 | 0.687 | 0.22 | 0.933 | 0.922 | 0.777 |
| api_llm_react_tool_policy | 0.888 | 0.976 | 0.0 | 0.743 | 0.145 | 0.933 | 0.907 | 0.823 |
| gatsim_official_planner | 0.642 | 0.801 | 0.05 | 0.358 | 0.283 | 0.65 | 0.532 | 0.465 |
| generative_agents_official_planner | 0.882 | 0.958 | 0.0 | 0.552 | 0.33 | 0.817 | 0.727 | 0.773 |
| sotopia_official_llm_agent | 0.812 | 0.811 | 0.047 | 0.507 | 0.305 | 0.558 | 0.663 | 0.673 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
