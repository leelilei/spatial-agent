# WikiChurches multinomial-residual validation-only selection

Decision: **NO_GO**. Test images encoded: **0**.

Selected ridge λ: **0.01**; train-CV robust balanced accuracy: **86.28%**.

| Shots | Gate τ | Gamma | Official Δ | SD | Robust | Random Δ | O−R | Wins | Worst style Δ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.50 | 0.00 | +0.00 | 0.00 | +0.00 | +0.00 | +0.00 | 0/3 | Romanesque +0.00 |
| 4 | 0.50 | 0.00 | +0.00 | 0.00 | +0.00 | +0.00 | +0.00 | 0/3 | Romanesque +0.00 |
| 16 | 0.50 | 0.00 | +0.00 | 0.00 | +0.00 | +0.00 | +0.00 | 0/3 | Romanesque +0.00 |

## Style deltas

- Romanesque: +0.00pp
- Gothic: +0.00pp
- Renaissance: +0.00pp
- Baroque: +0.00pp

## Gate

- train_head_robust_cv_balanced_accuracy: PASS ({"observed": 86.27631103563368, "pass": true, "required": 40.0})
- positive_robust_score_shots: FAIL ({"observed": 0, "pass": false, "required": 2})
- official_better_than_random_shots: FAIL ({"observed": 0, "pass": false, "required": 2})
- official_paired_wins: FAIL ({"observed": 0, "pass": false, "required": 5})
- worst_style_mean_delta: PASS ({"observed": 0.0, "pass": true, "required": -2.0, "style": "Romanesque"})
