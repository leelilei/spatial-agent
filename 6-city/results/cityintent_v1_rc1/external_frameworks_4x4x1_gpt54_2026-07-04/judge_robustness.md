# CityIntent Plausibility-Judge Robustness

Judges: `gpt54mini` and `gpt54`. Binary agreement uses threshold >= 0.70.

| Metric | n | Baseline mean | Candidate mean | MAE | Pearson | Spearman | Threshold agreement | Kappa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `face_plausibility` | 16 | 0.694 | 0.738 | 0.171 | 0.457 | 0.102 | 0.812 | 0.455 |
| `trace_believability` | 16 | 0.353 | 0.516 | 0.206 | 0.275 | 0.086 | 0.750 | 0.256 |
| `rationale_alignment` | 16 | 0.573 | 0.457 | 0.292 | 0.338 | 0.262 | 0.500 | 0.099 |
| `urban_common_sense` | 16 | 0.541 | 0.702 | 0.212 | 0.275 | 0.163 | 0.688 | 0.375 |

## Interpretation

- Cross-judge agreement is only moderate, so soft plausibility scores must be reported with evaluator identity and sensitivity analysis.
- Deterministic task, feasibility, resource, and state-transition scores remain unchanged across judges.
- This robustness check strengthens the case for the two-person human audit; it does not replace that release gate.
