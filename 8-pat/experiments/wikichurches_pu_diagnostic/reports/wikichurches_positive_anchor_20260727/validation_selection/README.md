# WikiChurches positive-anchor validation-only selection

Decision: **NO_GO**. Test images encoded: **0**.

| Shots | Ratio | Gamma | Official Δ | SD | Robust | Random Δ | O−R | Wins |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.01 | 20 | +1.62 | 1.48 | +0.88 | -20.39 | +22.01 | 2/3 |
| 4 | 0.01 | 0 | +0.00 | 0.00 | +0.00 | +0.00 | +0.00 | 0/3 |
| 16 | 0.01 | 0 | +0.00 | 0.00 | +0.00 | +0.00 | +0.00 | 0/3 |

## Gate

- positive_robust_score_shots: 1 / 2 (FAIL)
- official_better_than_random_shots: 1 / 2 (FAIL)
- official_paired_wins: 2 / 5 (FAIL)
