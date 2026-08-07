# Conservative positive-expansion multi-seed diagnostic

- Sampler seeds: 8
- Labels: 9
- Image-split repeats: 30
- Baseline rows: 10800
- PositiveExpansion rows: 2160
- Combined rows: 12960
- Reproduced Ignore max absolute difference: 0

## Held-out known-label performance

| Method | ROC-AUC | hierarchical 95% CI | AP | hierarchical 95% CI |
|---|---:|---:|---:|---:|
| PN-sampled | 0.871 | 0.804–0.928 | 0.566 | 0.453–0.667 |
| Ignore | 0.874 | 0.816–0.922 | 0.551 | 0.448–0.651 |
| nnPU-sampled | 0.774 | 0.684–0.858 | 0.443 | 0.327–0.555 |
| IPW-nnPU | 0.792 | 0.707–0.866 | 0.450 | 0.340–0.555 |
| FullPool-nnPU | 0.790 | 0.699–0.868 | 0.453 | 0.336–0.560 |
| PositiveExpansion | 0.872 | 0.814–0.921 | 0.544 | 0.438–0.642 |

## Frozen-gate contrasts

| Contrast | ΔROC-AUC | hierarchical 95% CI | ΔAP | hierarchical 95% CI |
|---|---:|---:|---:|---:|
| PositiveExpansion − Ignore | -0.002 | -0.005–-0.000 | -0.007 | -0.014–-0.001 |
| PositiveExpansion − PN-sampled | +0.001 | -0.013–+0.018 | -0.022 | -0.059–+0.013 |
| PositiveExpansion − IPW-nnPU | +0.080 | +0.042–+0.121 | +0.094 | +0.045–+0.141 |
| PositiveExpansion − FullPool-nnPU | +0.083 | +0.043–+0.126 | +0.091 | +0.045–+0.137 |

## Per-label diagnostics

| Label | selected / split | ΔAUC vs Ignore | ΔAP vs Ignore |
|---|---:|---:|---:|
| Buttress | 2.04 | -0.004 | -0.022 |
| Pilaster | 0.19 | -0.000 | +0.002 |
| Pinnacle | 0.00 | +0.000 | +0.000 |
| Pointed Arch Window | 0.23 | -0.001 | -0.006 |
| Round Arch Window | 0.38 | -0.002 | -0.002 |
| Tracery | 0.02 | -0.000 | -0.001 |
| Tracery Rose Window | 0.39 | -0.001 | -0.007 |
| Triangular Pediment | 2.60 | -0.011 | -0.025 |
| Wimperg | 1.22 | -0.000 | -0.000 |

## Per-sampler-seed diagnostics

| Sampler seed | selected / split | ΔAUC vs Ignore | ΔAP vs Ignore |
|---:|---:|---:|---:|
| 20260726 | 0.80 | -0.002 | -0.008 |
| 20260727 | 0.86 | -0.003 | -0.006 |
| 20260728 | 0.52 | -0.002 | -0.006 |
| 20260729 | 0.68 | -0.001 | -0.006 |
| 20260730 | 0.83 | -0.003 | -0.010 |
| 20260731 | 0.92 | -0.001 | -0.004 |
| 20260732 | 0.84 | -0.003 | -0.012 |
| 20260733 | 0.83 | -0.002 | -0.002 |

## Frozen Go gate

- Mean selected pseudo-positives / split: 0.79
- Labels with any mean expansion: 8/9
- Labels with positive AUC delta: 0/9
- Sampler seeds with positive AUC delta: 0/8
- Required: ΔAUC and ΔAP ≥ +0.01, both lower CIs > 0, coverage ≥ 4 labels, AUC positive in every sampler seed.
- Decision: **NO-GO**.

U not selected as pseudo-positive receives zero loss. This experiment evaluates preservation of held-out official labels; it does not establish missing-positive truth.
