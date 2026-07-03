# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.856 | 0.627 | 0.253 | 0.547 | 0.309 | 0.613 | 0.844 | 0.725 |
| gatsim_official_planner | 0.521 | 0.943 | 0.026 | 0.209 | 0.312 | 0.862 | 0.379 | 0.341 |
| generative_agents_official_planner | 0.693 | 0.691 | 0.115 | 0.404 | 0.289 | 0.613 | 0.453 | 0.578 |
| sotopia_official_llm_agent | 0.752 | 0.838 | 0.079 | 0.332 | 0.42 | 0.438 | 0.497 | 0.506 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
