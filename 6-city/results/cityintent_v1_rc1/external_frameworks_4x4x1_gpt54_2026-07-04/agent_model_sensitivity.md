# CityIntent Agent-Model Sensitivity

Baseline agent model: `gpt-5.4-mini`. Candidate agent model: `gpt-5.4`.

All deltas are candidate minus baseline over matched scenario-adapter cells.

| Adapter | n | Task base | Task cand. | Delta | Feas. base | Feas. cand. | Delta | Full task base/cand. | Full feas. base/cand. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 4 | 0.827 | 0.577 | -0.250 | 0.823 | 0.863 | +0.040 | 0.750/0.500 | 0.250/0.500 |
| `gatsim_official_planner` | 4 | 0.750 | 0.500 | -0.250 | 0.830 | 0.875 | +0.045 | 0.750/0.500 | 0.500/0.250 |
| `generative_agents_official_planner` | 4 | 0.702 | 0.827 | +0.125 | 0.635 | 0.950 | +0.315 | 0.500/0.750 | 0.000/0.750 |
| `sotopia_official_llm_agent` | 4 | 0.077 | 0.452 | +0.375 | 1.000 | 0.896 | -0.104 | 0.000/0.250 | 1.000/0.500 |

## Execution Cost

| Adapter | Calls base/cand. | Latency base/cand. (s) | Tokens base/cand. |
|---|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 5.50/6.00 | 37.7/53.2 | 38626/44214 |
| `gatsim_official_planner` | 2.75/2.25 | 37.7/24.3 | 25871/21549 |
| `generative_agents_official_planner` | 6.50/2.50 | 41.5/19.2 | 38829/15824 |
| `sotopia_official_llm_agent` | 5.25/5.50 | 26.5/24.3 | 36034/38072 |

## Reading

- A positive delta is not expected for every adapter; model-by-architecture interactions are part of the result.
- This one-run paired comparison estimates direction, not repeated model-effect reliability.
- Hard task and feasibility deltas are primary; soft scores remain judge-dependent.
