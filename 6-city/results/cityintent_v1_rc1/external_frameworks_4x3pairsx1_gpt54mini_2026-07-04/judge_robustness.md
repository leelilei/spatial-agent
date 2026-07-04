# CityIntent Plausibility-Judge Robustness

Judges: `gpt54mini` and `gpt54`. Binary agreement uses threshold >= 0.70.

| Metric | n | Baseline mean | Candidate mean | MAE | Pearson | Spearman | Threshold agreement | Kappa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `face_plausibility` | 24 | 0.811 | 0.820 | 0.147 | 0.14 | 0.515 | 0.750 | -0.143 |
| `trace_believability` | 24 | 0.451 | 0.668 | 0.278 | 0.413 | 0.417 | 0.750 | 0.474 |
| `rationale_alignment` | 24 | 0.536 | 0.597 | 0.228 | 0.661 | 0.682 | 0.833 | 0.66 |
| `urban_common_sense` | 24 | 0.607 | 0.773 | 0.272 | 0.214 | 0.384 | 0.458 | -0.164 |

## Interpretation

- Cross-judge agreement is only moderate, so soft plausibility scores must be reported with evaluator identity and sensitivity analysis.
- Deterministic task, feasibility, resource, and state-transition scores remain unchanged across judges.
- This robustness check strengthens the case for the two-person human audit; it does not replace that release gate.
