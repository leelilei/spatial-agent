# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.805 | 0.852 | 0.048 | 0.435 | 0.37 | 0.708 | 0.882 | 0.605 |
| gatsim_official_planner | 0.747 | 0.905 | 0.0 | 0.323 | 0.423 | 0.767 | 0.762 | 0.555 |
| generative_agents_official_planner | 0.718 | 0.943 | 0.031 | 0.47 | 0.248 | 0.708 | 0.48 | 0.603 |
| sotopia_official_llm_agent | 0.705 | 0.906 | 0.004 | 0.365 | 0.34 | 0.525 | 0.438 | 0.552 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
