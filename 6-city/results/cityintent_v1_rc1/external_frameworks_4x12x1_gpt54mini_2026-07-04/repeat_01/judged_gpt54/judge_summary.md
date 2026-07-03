# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.753 | 0.627 | 0.198 | 0.557 | 0.196 | 0.613 | 0.69 | 0.746 |
| gatsim_official_planner | 0.726 | 0.943 | 0.0 | 0.52 | 0.206 | 0.862 | 0.419 | 0.678 |
| generative_agents_official_planner | 0.709 | 0.691 | 0.083 | 0.495 | 0.214 | 0.613 | 0.364 | 0.689 |
| sotopia_official_llm_agent | 0.665 | 0.838 | 0.082 | 0.405 | 0.26 | 0.438 | 0.397 | 0.579 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
