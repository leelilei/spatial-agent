# TOGA EuroSAT official-direction reproduction

Protocol: CoOp/Tip-Adapter fixed split; CLIP ViT-B/16; official dataset/shot presets; seeds 1/2/3; validation-selected checkpoints and cache hyperparameters; test evaluated only after selection.

## Test accuracy

| Shots | Internal Tip-F | TOGA | Paired Δ | Paper Tip-F | Paper TOGA | TOGA gap |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 68.72 ± 2.82 | 65.16 ± 4.76 | -3.56 ± 5.77 | 59.5 | 67.4 | -2.24 |
| 2 | 75.65 ± 3.84 | 74.02 ± 2.97 | -1.63 ± 1.93 | 66.1 | 74.9 | -0.88 |
| 4 | 78.81 ± 0.28 | 79.29 ± 1.21 | 0.47 ± 1.22 | 74.1 | 80.3 | -1.01 |
| 8 | 82.99 ± 2.81 | 83.58 ± 1.89 | 0.58 ± 1.10 | 77.9 | 84.1 | -0.52 |
| 16 | 88.21 ± 0.92 | 88.93 ± 0.63 | 0.72 ± 0.41 | 84.5 | 89.4 | -0.47 |

## Diagnostics

- Mean paired TOGA − internal Tip-F delta: -0.68 ± 2.95 percentage points.
- Direction count: TOGA wins 7/15, ties 0/15, loses 8/15.
- Mean absolute gap between reproduced and paper TOGA curves: 1.03 percentage points.
- The internal Tip-F control uses the repository's TOGA-tuned shot preset; it is not assumed identical to the historical Tip-Adapter-F row quoted by the paper.

## Per-seed paired deltas

- 1-shot: seed 1: +1.25, seed 2: -9.96, seed 3: -1.96
- 2-shot: seed 1: -0.10, seed 2: -3.80, seed 3: -0.99
- 4-shot: seed 1: -0.14, seed 2: +1.88, seed 3: -0.32
- 8-shot: seed 1: +0.06, seed 2: +1.85, seed 3: -0.16
- 16-shot: seed 1: +1.20, seed 2: +0.48, seed 3: +0.48
