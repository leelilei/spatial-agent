# WikiChurches frozen-confirmation test

Protocol: hyperparameters selected without constructing or evaluating the test split on seeds 1/2/3, then frozen before this single test evaluation on fresh seeds 4/5/6.

| Shots | Frozen candidate | Tip-F | TOGA | Paired Δ | Wins |
|---:|---|---:|---:|---:|---:|
| 1 | c7_dropout_low | 59.87 ± 2.24 | 57.51 ± 2.26 | -2.36 ± 1.28 | 0/3 |
| 4 | c4_teacher_strong | 59.11 ± 0.99 | 57.02 ± 0.62 | -2.09 ± 0.68 | 0/3 |
| 16 | c3_teacher_weak | 58.57 ± 3.05 | 58.73 ± 1.17 | 0.16 ± 2.56 | 1/3 |

Predeclared decision: **NO-GO**.

- Positive shot-level mean deltas: 1/3.
- Pairwise directions: 1 wins, 0 ties, 8 losses.
- Overall paired delta: -1.43 ± 1.90 percentage points.
- Worst shot-level mean delta: -2.36 points.
