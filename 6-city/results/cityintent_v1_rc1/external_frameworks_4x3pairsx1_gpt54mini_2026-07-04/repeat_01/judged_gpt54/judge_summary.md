# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.85 | 0.787 | 0.072 | 0.682 | 0.168 | 0.767 | 0.843 | 0.807 |
| gatsim_official_planner | 0.845 | 0.976 | 0.0 | 0.735 | 0.11 | 0.958 | 0.602 | 0.79 |
| generative_agents_official_planner | 0.803 | 0.853 | 0.032 | 0.705 | 0.098 | 0.858 | 0.452 | 0.787 |
| sotopia_official_llm_agent | 0.783 | 0.805 | 0.119 | 0.552 | 0.232 | 0.425 | 0.492 | 0.708 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
