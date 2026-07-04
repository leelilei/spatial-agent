# CityIntent Evidence Reliability And Dissociation

A trace is face-plausible when judge score >= 0.70; full task success and full feasibility require score >= 0.999.

## Architecture Table

| Agent | n | Full task | Fully feasible | Plausible | Plausible task failure | Plausible infeasible | pass^k task | pass^k feasible |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AgentSociety | 6 | 0.667 | 0.500 | 1.000 | 0.333 | 0.500 | 0.667 | 0.500 |
| GATSim | 6 | 1.000 | 0.833 | 0.500 | 0.000 | 0.000 | 1.000 | 0.833 |
| Generative Agents | 6 | 0.833 | 0.500 | 1.000 | 0.167 | 0.500 | 0.833 | 0.500 |
| SOTOPIA | 6 | 0.000 | 0.667 | 1.000 | 1.000 | 0.333 | 0.000 | 0.667 |

`pass^k` uses all available repeats for each scenario-agent cell.

## Metric Dissociation

| Comparison | n | Pooled Pearson | Pooled Spearman | Within-cell Pearson | Within-cell Spearman |
|---|---:|---:|---:|---:|---:|
| `face_vs_task` | 24 | -0.343 | -0.354 | None | None |
| `face_vs_feasibility` | 24 | -0.098 | 0.165 | None | None |
| `trace_believability_vs_task` | 24 | -0.206 | -0.255 | None | None |
| `trace_believability_vs_feasibility` | 24 | 0.122 | 0.06 | None | None |

## Reading

- No architecture dominates all proof obligations: task completion, feasibility, face plausibility, and repeated reliability rank systems differently.
- Face plausibility is not a valid substitute for environment-owned task or feasibility evidence in this sample.
- These are architecture-by-scenario pilot estimates, not human behavioral realism claims; human construct validation remains a separate release gate.
