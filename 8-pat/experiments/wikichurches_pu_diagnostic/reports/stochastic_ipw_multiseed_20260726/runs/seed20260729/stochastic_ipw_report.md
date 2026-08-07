# Stochastic known-inclusion-probability P/U diagnostic

## Boundary

- U is sampled with recorded independent Bernoulli probability q;
- IPW uses self-normalized 1/q on the sampled-U negative risk;
- FullPool-nnPU uses the candidate census as sampling-risk reference;
- FullPool is not label Oracle and U still has no human truth.

- Encoder: `ViT-B/16`
- Images: 50
- Official boxes: 237
- Candidate pool rows: 23371
- Unique encoded regions: 5599
- Sampled rows: 741
- Labels: 9
- Repeats: 30 / label
- Class prior: 0.25

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | pool score |
|---|---:|---:|---:|---:|---:|---:|
| PN-sampled | 0.868 | 0.797–0.926 | 0.564 | 0.443–0.667 | 0.547 | 0.373 |
| Ignore | 0.874 | 0.816–0.921 | 0.551 | 0.449–0.649 | 0.540 | 0.447 |
| nnPU-sampled | 0.769 | 0.661–0.860 | 0.423 | 0.301–0.533 | 0.905 | 0.482 |
| IPW-nnPU | 0.793 | 0.701–0.869 | 0.437 | 0.331–0.531 | 0.918 | 0.514 |
| FullPool-nnPU | 0.790 | 0.697–0.867 | 0.453 | 0.338–0.560 | 0.913 | 0.462 |

## Sampling diagnostics

- q min/median/max over split samples: 0.016/0.033/0.076
- IPW ESS mean: 18.92

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| IPW-nnPU − nnPU-sampled | +0.024 | +0.008–+0.043 | +0.014 | -0.036–+0.050 |
| IPW-nnPU − FullPool-nnPU | +0.003 | -0.023–+0.024 | -0.016 | -0.056–+0.026 |
| nnPU-sampled − FullPool-nnPU | -0.021 | -0.061–+0.003 | -0.029 | -0.077–+0.020 |
| IPW-nnPU − Ignore | -0.082 | -0.128–-0.042 | -0.114 | -0.146–-0.077 |

## FullPool approximation

Negative values mean IPW is closer to FullPool than unweighted sampled-U nnPU.

| Gap contrast | Δ absolute AUC gap | 95% CI | Δ absolute AP gap | 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | -0.010 | -0.032–+0.008 | -0.004 | -0.039–+0.034 |

This experiment identifies candidate-sampling correction only. It does not identify annotation propensity, missing-positive precision, or Oracle performance.
