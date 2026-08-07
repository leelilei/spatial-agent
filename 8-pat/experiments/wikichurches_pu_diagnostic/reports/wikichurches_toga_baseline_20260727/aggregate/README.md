# WikiChurches-4 TOGA mother-method screening

Protocol: church-disjoint official splits; 1/4/16-shot; seeds 1/2/3; validation-selected checkpoints; test evaluated only after selection.

## Test accuracy

| Shots | Tip-Adapter-F | TOGA | Paired Δ (TOGA − Tip-F) |
|---:|---:|---:|---:|
| 1 | 59.20 ± 1.31 | 58.25 ± 1.05 | -0.94 ± 1.28 |
| 4 | 58.84 ± 1.84 | 57.98 ± 0.85 | -0.85 ± 1.05 |
| 16 | 59.29 ± 0.27 | 58.95 ± 2.34 | -0.34 ± 2.58 |

## Screening interpretation

- Mean paired delta across the 9 matched runs: -0.71 ± 1.56 percentage points.
- Direction count: TOGA wins 4/9, ties 0/9, loses 5/9.
- This is a fixed-hyperparameter domain-transfer screen, not a paper-level reproduction or a tuned WikiChurches result.

## Per-seed paired deltas

- 1-shot: seed 1: +0.34, seed 2: -2.23, seed 3: -0.94
- 4-shot: seed 1: -1.28, seed 2: +0.34, seed 3: -1.62
- 16-shot: seed 1: +1.35, seed 2: -3.31, seed 3: +0.94
