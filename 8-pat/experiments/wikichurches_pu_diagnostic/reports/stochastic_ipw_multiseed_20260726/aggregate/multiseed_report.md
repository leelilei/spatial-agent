# Multi-sampler-seed stochastic IPW diagnostic

The fixed Bernoulli inclusion probabilities are held constant while the sampled candidate set is redrawn under eight predeclared seeds.

- Sampler seeds: 20260726, 20260727, 20260728, 20260729, 20260730, 20260731, 20260732, 20260733
- Seeds: 8
- Labels: 9
- Image-split repeats: 30 per seed/label
- Result rows: 10800
- Hierarchical bootstrap replicates: 10000

## Held-out known-label performance

| Method | ROC-AUC | hierarchical 95% CI | AP | hierarchical 95% CI |
|---|---:|---:|---:|---:|
| PN-sampled | 0.871 | 0.804–0.928 | 0.566 | 0.453–0.667 |
| Ignore | 0.874 | 0.816–0.922 | 0.551 | 0.448–0.651 |
| nnPU-sampled | 0.774 | 0.684–0.858 | 0.443 | 0.327–0.555 |
| IPW-nnPU | 0.792 | 0.707–0.866 | 0.450 | 0.340–0.555 |
| FullPool-nnPU | 0.790 | 0.699–0.868 | 0.453 | 0.336–0.560 |

## Paired differences

| Contrast | ΔROC-AUC | hierarchical 95% CI | ΔAP | hierarchical 95% CI |
|---|---:|---:|---:|---:|
| IPW-nnPU − nnPU-sampled | +0.018 | +0.005–+0.034 | +0.007 | -0.018–+0.031 |
| IPW-nnPU − FullPool-nnPU | +0.002 | -0.010–+0.018 | -0.003 | -0.023–+0.017 |
| IPW-nnPU − Ignore | -0.082 | -0.125–-0.043 | -0.101 | -0.149–-0.051 |

## FullPool approximation

Negative values mean IPW is closer to the FullPool sampling-risk reference than unweighted sampled-U nnPU.

| Gap contrast | Δ absolute AUC gap | hierarchical 95% CI | Δ absolute AP gap | hierarchical 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | -0.008 | -0.018–+0.001 | -0.010 | -0.026–+0.003 |

## Per-sampler-seed IPW effects

| Sampler seed | sampled rows (9 labels) | ΔAUC vs unweighted | ΔAP vs unweighted | ΔAUC vs Ignore |
|---:|---:|---:|---:|---:|
| 20260726 | 260 | +0.027 | +0.007 | -0.072 |
| 20260727 | 258 | +0.020 | +0.023 | -0.075 |
| 20260728 | 217 | +0.013 | +0.016 | -0.080 |
| 20260729 | 253 | +0.024 | +0.014 | -0.082 |
| 20260730 | 268 | +0.007 | +0.002 | -0.091 |
| 20260731 | 276 | +0.022 | -0.012 | -0.083 |
| 20260732 | 250 | +0.017 | +0.002 | -0.079 |
| 20260733 | 270 | +0.014 | +0.007 | -0.098 |

## Interpretation boundary

This analysis tests robustness to candidate sampling only. FullPool is not an annotation Oracle, and no missing region has acquired human truth through this experiment.
