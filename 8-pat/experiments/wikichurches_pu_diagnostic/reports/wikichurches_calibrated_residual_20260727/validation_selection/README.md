# WikiChurches calibrated-residual validation-only selection

Decision: **NO_GO**. Test images encoded: **0**.

| Shots | Gate τ | Gamma | Official Δ | SD | Robust | Random Δ | O−R | Wins | Mean gate |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.50 | 0.50 | +1.13 | 0.74 | +0.76 | -1.60 | +2.73 | 3/3 | 0.24 |
| 4 | 1.50 | 4.00 | +0.97 | 1.28 | +0.33 | -12.60 | +13.57 | 2/3 | 0.73 |
| 16 | 0.50 | 0.00 | +0.00 | 0.00 | +0.00 | +0.00 | +0.00 | 0/3 | 0.27 |

## Style deltas

- Romanesque: +2.22pp
- Gothic: -10.26pp
- Renaissance: +2.78pp
- Baroque: +8.12pp

## Gate

- positive_robust_score_shots: PASS ({"observed": 2, "pass": true, "required": 2})
- official_better_than_random_shots: PASS ({"observed": 2, "pass": true, "required": 2})
- official_paired_wins: PASS ({"observed": 5, "pass": true, "required": 5})
- worst_style_mean_delta: FAIL ({"observed": -10.256410307354397, "pass": false, "required": -2.0, "style": "Gothic"})
