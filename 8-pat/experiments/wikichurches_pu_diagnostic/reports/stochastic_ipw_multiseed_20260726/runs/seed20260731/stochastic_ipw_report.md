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
- Sampled rows: 716
- Labels: 9
- Repeats: 30 / label
- Class prior: 0.25

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | pool score |
|---|---:|---:|---:|---:|---:|---:|
| PN-sampled | 0.872 | 0.806–0.926 | 0.566 | 0.455–0.661 | 0.547 | 0.370 |
| Ignore | 0.874 | 0.816–0.921 | 0.551 | 0.449–0.649 | 0.540 | 0.447 |
| nnPU-sampled | 0.770 | 0.683–0.854 | 0.457 | 0.334–0.570 | 0.902 | 0.480 |
| IPW-nnPU | 0.792 | 0.705–0.868 | 0.444 | 0.327–0.556 | 0.916 | 0.523 |
| FullPool-nnPU | 0.790 | 0.697–0.867 | 0.453 | 0.338–0.560 | 0.913 | 0.462 |

## Sampling diagnostics

- q min/median/max over split samples: 0.016/0.033/0.089
- IPW ESS mean: 20.12

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| IPW-nnPU − nnPU-sampled | +0.022 | +0.004–+0.043 | -0.012 | -0.037–+0.013 |
| IPW-nnPU − FullPool-nnPU | +0.002 | -0.018–+0.018 | -0.008 | -0.031–+0.014 |
| nnPU-sampled − FullPool-nnPU | -0.020 | -0.045–+0.006 | +0.004 | -0.033–+0.041 |
| IPW-nnPU − Ignore | -0.083 | -0.134–-0.041 | -0.106 | -0.159–-0.052 |

## FullPool approximation

Negative values mean IPW is closer to FullPool than unweighted sampled-U nnPU.

| Gap contrast | Δ absolute AUC gap | 95% CI | Δ absolute AP gap | 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | -0.009 | -0.023–+0.008 | -0.003 | -0.025–+0.021 |

This experiment identifies candidate-sampling correction only. It does not identify annotation propensity, missing-positive precision, or Oracle performance.
