# WikiChurches train–validation split-shift diagnostic

Decision: **SPLIT_SHIFT_NOT_FULLY_SUPPORTED**. Test images encoded: **0**.

| Representation | Train BA | Validation BA | Drop | Stratified p |
|---|---:|---:|---:|---:|
| Global CLIP | 63.02 | 66.92 | -3.90 | 0.46555 |
| Local residual | 86.22 | 52.25 | +33.97 | 0.00110 |

## Local shift by style

| Style | Train n | Val n | Normalized shift | Permutation p |
|---|---:|---:|---:|---:|
| Romanesque | 38 | 50 | 0.509 | 0.00190 |
| Gothic | 35 | 52 | 1.119 | 0.00010 |
| Renaissance | 4 | 52 | 1.102 | 0.10269 |
| Baroque | 13 | 52 | 0.737 | 0.00220 |

## Gate

- global_stratified_permutation: FAIL ({"observed": 0.46555344465553444, "pass": false, "required_at_most": 0.01})
- local_stratified_permutation: PASS ({"observed": 0.0010998900109989002, "pass": true, "required_at_most": 0.01})
- local_balanced_accuracy_drop: PASS ({"observed": 33.96746814250946, "pass": true, "required_at_least": 20.0})
- gothic_local_recall_drop: PASS ({"observed": 64.50549364089966, "pass": true, "required_at_least": 20.0})
- gothic_local_shift_effect_rank: PASS ({"observed": 1, "pass": true, "required_at_most": 2})
