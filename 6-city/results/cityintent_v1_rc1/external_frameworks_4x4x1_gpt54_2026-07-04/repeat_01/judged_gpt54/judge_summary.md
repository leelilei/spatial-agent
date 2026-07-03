# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.767 | 0.863 | 0.007 | 0.542 | 0.225 | 0.7 | 0.522 | 0.69 |
| gatsim_official_planner | 0.605 | 0.875 | 0.0 | 0.448 | 0.158 | 0.613 | 0.345 | 0.598 |
| generative_agents_official_planner | 0.84 | 0.95 | 0.018 | 0.657 | 0.182 | 0.838 | 0.6 | 0.855 |
| sotopia_official_llm_agent | 0.74 | 0.896 | 0.018 | 0.415 | 0.325 | 0.675 | 0.36 | 0.665 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
