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
- Sampled rows: 690
- Labels: 9
- Repeats: 30 / label
- Class prior: 0.25

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | pool score |
|---|---:|---:|---:|---:|---:|---:|
| PN-sampled | 0.875 | 0.811–0.927 | 0.571 | 0.463–0.665 | 0.544 | 0.378 |
| Ignore | 0.874 | 0.816–0.921 | 0.551 | 0.449–0.649 | 0.540 | 0.447 |
| nnPU-sampled | 0.776 | 0.681–0.858 | 0.423 | 0.303–0.545 | 0.900 | 0.482 |
| IPW-nnPU | 0.792 | 0.703–0.868 | 0.438 | 0.308–0.571 | 0.920 | 0.508 |
| FullPool-nnPU | 0.790 | 0.697–0.867 | 0.453 | 0.338–0.560 | 0.913 | 0.462 |

## Sampling diagnostics

- q min/median/max over split samples: 0.016/0.035/0.076
- IPW ESS mean: 16.90

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| IPW-nnPU − nnPU-sampled | +0.016 | +0.001–+0.027 | +0.015 | -0.019–+0.045 |
| IPW-nnPU − FullPool-nnPU | +0.002 | -0.019–+0.022 | -0.015 | -0.075–+0.043 |
| nnPU-sampled − FullPool-nnPU | -0.014 | -0.035–+0.006 | -0.030 | -0.091–+0.033 |
| IPW-nnPU − Ignore | -0.082 | -0.119–-0.043 | -0.113 | -0.180–-0.037 |

## FullPool approximation

Negative values mean IPW is closer to FullPool than unweighted sampled-U nnPU.

| Gap contrast | Δ absolute AUC gap | 95% CI | Δ absolute AP gap | 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | +0.000 | -0.015–+0.017 | -0.008 | -0.032–+0.017 |

This experiment identifies candidate-sampling correction only. It does not identify annotation propensity, missing-positive precision, or Oracle performance.
