# CityIntent Matched Perturbation Analysis

Deltas are treatment minus control. Negative task or feasibility deltas indicate perturbation loss.

## By Adapter

| Adapter | n | Task C/T | Task delta | Feas. C/T | Feas. delta | Joint C/T | Conditional task recovery | Conditional joint recovery |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety_official_plan_blocks` | 3 | 1.000/0.692 | -0.308 | 1.000/0.625 | -0.375 | 1.000/0.000 | 0.333 (3) | 0.000 (3) |
| `gatsim_official_planner` | 3 | 1.000/1.000 | +0.000 | 1.000/1.000 | +0.000 | 1.000/1.000 | 1.000 (3) | 1.000 (3) |
| `generative_agents_official_planner` | 3 | 1.000/0.538 | -0.462 | 1.000/0.532 | -0.468 | 1.000/0.000 | 0.000 (3) | 0.000 (3) |

## By Perturbation

| Pair | n | Task C/T | Task delta | Feas. C/T | Feas. delta | Interruptions C/T | Replans C/T |
|---|---:|---:|---:|---:|---:|---:|---:|
| `study_place_closure` | 9 | 1.000/0.743 | -0.257 | 1.000/0.719 | -0.281 | 0.00/0.00 | 0.00/0.00 |

## Interpretation Rules

- Compare only matched cells with identical agent, repeat, goals, and non-event scenario fields.
- Conditional recovery is evaluated only where the corresponding control succeeds.
- This archive contains 3 repeats per matched cell; broader pair families are still required for generalization claims.
- Soft plausibility deltas are diagnostic and do not replace hard environment evidence.
