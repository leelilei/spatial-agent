# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.852 | 0.817 | 0.12 | 0.638 | 0.217 | 0.442 | 0.867 | 0.743 |
| gatsim_official_planner | 0.693 | 0.905 | 0.035 | 0.503 | 0.19 | 0.817 | 0.565 | 0.593 |
| generative_agents_official_planner | 0.795 | 0.754 | 0.113 | 0.463 | 0.332 | 0.45 | 0.525 | 0.658 |
| sotopia_official_llm_agent | 0.753 | 0.848 | 0.004 | 0.412 | 0.342 | 0.317 | 0.608 | 0.615 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
