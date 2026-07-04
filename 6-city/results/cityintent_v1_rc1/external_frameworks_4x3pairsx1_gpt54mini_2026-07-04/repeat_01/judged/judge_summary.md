# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.877 | 0.787 | 0.107 | 0.658 | 0.218 | 0.767 | 0.908 | 0.752 |
| gatsim_official_planner | 0.602 | 0.976 | 0.0 | 0.222 | 0.38 | 0.958 | 0.353 | 0.398 |
| generative_agents_official_planner | 0.868 | 0.853 | 0.065 | 0.462 | 0.407 | 0.858 | 0.327 | 0.652 |
| sotopia_official_llm_agent | 0.897 | 0.805 | 0.166 | 0.462 | 0.438 | 0.425 | 0.555 | 0.628 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
