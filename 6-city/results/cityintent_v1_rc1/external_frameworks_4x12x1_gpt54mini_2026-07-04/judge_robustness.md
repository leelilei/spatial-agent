# CityIntent Plausibility-Judge Robustness

Judges: `gpt54mini` and `gpt54`. Binary agreement uses threshold >= 0.70.

| Metric | n | Baseline mean | Candidate mean | MAE | Pearson | Spearman | Threshold agreement | Kappa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `face_plausibility` | 48 | 0.705 | 0.713 | 0.180 | 0.416 | 0.471 | 0.708 | 0.3 |
| `trace_believability` | 48 | 0.373 | 0.494 | 0.201 | 0.549 | 0.528 | 0.771 | 0.362 |
| `rationale_alignment` | 48 | 0.544 | 0.467 | 0.187 | 0.66 | 0.648 | 0.750 | 0.464 |
| `urban_common_sense` | 48 | 0.538 | 0.673 | 0.211 | 0.51 | 0.53 | 0.646 | 0.306 |

## Interpretation

- Cross-judge agreement is only moderate, so soft plausibility scores must be reported with evaluator identity and sensitivity analysis.
- Deterministic task, feasibility, resource, and state-transition scores remain unchanged across judges.
- This robustness check strengthens the case for the two-person human audit; it does not replace that release gate.
