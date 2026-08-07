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
- Sampled rows: 673
- Labels: 9
- Repeats: 30 / label
- Class prior: 0.25

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | pool score |
|---|---:|---:|---:|---:|---:|---:|
| PN-sampled | 0.872 | 0.803–0.928 | 0.569 | 0.451–0.667 | 0.544 | 0.373 |
| Ignore | 0.874 | 0.816–0.921 | 0.551 | 0.449–0.649 | 0.540 | 0.447 |
| nnPU-sampled | 0.779 | 0.695–0.857 | 0.456 | 0.337–0.566 | 0.904 | 0.475 |
| IPW-nnPU | 0.796 | 0.720–0.867 | 0.458 | 0.351–0.560 | 0.919 | 0.506 |
| FullPool-nnPU | 0.790 | 0.697–0.867 | 0.453 | 0.338–0.560 | 0.913 | 0.462 |

## Sampling diagnostics

- q min/median/max over split samples: 0.016/0.035/0.088
- IPW ESS mean: 17.99

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| IPW-nnPU − nnPU-sampled | +0.017 | +0.004–+0.033 | +0.002 | -0.031–+0.032 |
| IPW-nnPU − FullPool-nnPU | +0.006 | -0.015–+0.034 | +0.005 | -0.015–+0.028 |
| nnPU-sampled − FullPool-nnPU | -0.011 | -0.038–+0.016 | +0.003 | -0.037–+0.049 |
| IPW-nnPU − Ignore | -0.079 | -0.123–-0.040 | -0.093 | -0.146–-0.037 |

## FullPool approximation

Negative values mean IPW is closer to FullPool than unweighted sampled-U nnPU.

| Gap contrast | Δ absolute AUC gap | 95% CI | Δ absolute AP gap | 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | -0.014 | -0.031–+0.001 | -0.027 | -0.062–+0.005 |

This experiment identifies candidate-sampling correction only. It does not identify annotation propensity, missing-positive precision, or Oracle performance.
