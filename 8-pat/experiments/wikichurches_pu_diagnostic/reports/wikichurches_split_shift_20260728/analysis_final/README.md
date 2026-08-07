# WikiChurches train–validation split-shift diagnostic

Decision: **SPLIT_SHIFT_SUPPORTED**. Test images encoded: **0**.

| Representation | Train BA | Validation BA | Drop | Stratified p |
|---|---:|---:|---:|---:|
| Global CLIP, box subset | 84.46 | 57.36 | +27.10 | 0.00120 |
| Global CLIP, all-train control | 63.02 | 66.92 | -3.90 | 0.47965 |
| Local residual | 86.22 | 52.18 | +34.03 | 0.00070 |

## Local shift by style

| Style | Train n | Val n | Normalized shift | Permutation p |
|---|---:|---:|---:|---:|
| Romanesque | 38 | 50 | 0.509 | 0.00210 |
| Gothic | 35 | 50 | 1.125 | 0.00010 |
| Renaissance | 4 | 49 | 1.094 | 0.11099 |
| Baroque | 13 | 50 | 0.742 | 0.00290 |

## Gate

- global_stratified_permutation: PASS ({"observed": 0.0011998800119988001, "pass": true, "required_at_most": 0.01})
- local_stratified_permutation: PASS ({"observed": 0.0006999300069993001, "pass": true, "required_at_most": 0.01})
- local_balanced_accuracy_drop: PASS ({"observed": 34.033794701099396, "pass": true, "required_at_least": 20.0})
- gothic_local_recall_drop: PASS ({"observed": 65.4285728931427, "pass": true, "required_at_least": 20.0})
- gothic_local_shift_effect_rank: PASS ({"observed": 1, "pass": true, "required_at_most": 2})
