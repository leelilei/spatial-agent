# CityIntent Matched Perturbation Analysis

Deltas are treatment minus control. Negative task or feasibility deltas indicate perturbation loss.

## By Adapter

| Adapter | n | Task C/T | Task delta | Feas. C/T | Feas. delta | Joint C/T | Conditional task recovery | Conditional joint recovery |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 3 | 0.667/0.846 | +0.179 | 1.000/0.575 | -0.425 | 0.667/0.000 | 0.500 (2) | 0.000 (2) |
| `gatsim_official_planner` | 3 | 1.000/1.000 | +0.000 | 1.000/0.952 | -0.048 | 1.000/0.667 | 1.000 (3) | 0.667 (3) |
| `generative_agents_official_planner` | 3 | 1.000/0.846 | -0.154 | 1.000/0.707 | -0.293 | 1.000/0.000 | 0.667 (3) | 0.000 (3) |
| `sotopia_official_llm_agent` | 3 | 0.000/0.179 | +0.179 | 0.778/0.833 | +0.056 | 0.000/0.000 | n/a (0) | n/a (0) |

## By Perturbation

| Pair | n | Task C/T | Task delta | Feas. C/T | Feas. delta | Interruptions C/T | Replans C/T |
|---|---:|---:|---:|---:|---:|---:|---:|
| `commute_midroute_block` | 4 | 0.500/0.750 | +0.250 | 1.000/0.814 | -0.186 | 0.00/0.00 | 0.00/0.25 |
| `pickup_social_opportunity` | 4 | 0.750/0.750 | +0.000 | 1.000/0.812 | -0.188 | 0.00/0.00 | 0.00/0.00 |
| `study_place_closure` | 4 | 0.750/0.653 | -0.097 | 0.833/0.674 | -0.159 | 0.00/0.00 | 0.00/0.00 |

## Interpretation Rules

- Compare only matched cells with identical agent, repeat, goals, and non-event scenario fields.
- Conditional recovery is evaluated only where the corresponding control succeeds.
- One repeat estimates direction; repeated pairs are required for reliability claims.
- Soft plausibility deltas are diagnostic and do not replace hard environment evidence.
