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
- Sampled rows: 700
- Labels: 9
- Repeats: 30 / label
- Class prior: 0.25

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | pool score |
|---|---:|---:|---:|---:|---:|---:|
| PN-sampled | 0.870 | 0.800–0.927 | 0.567 | 0.451–0.670 | 0.547 | 0.370 |
| Ignore | 0.874 | 0.816–0.921 | 0.551 | 0.449–0.649 | 0.540 | 0.447 |
| nnPU-sampled | 0.775 | 0.689–0.855 | 0.448 | 0.329–0.557 | 0.907 | 0.477 |
| IPW-nnPU | 0.802 | 0.731–0.870 | 0.455 | 0.351–0.558 | 0.922 | 0.513 |
| FullPool-nnPU | 0.790 | 0.697–0.867 | 0.453 | 0.338–0.560 | 0.913 | 0.462 |

## Sampling diagnostics

- q min/median/max over split samples: 0.016/0.034/0.082
- IPW ESS mean: 18.97

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| IPW-nnPU − nnPU-sampled | +0.027 | +0.010–+0.046 | +0.007 | -0.025–+0.035 |
| IPW-nnPU − FullPool-nnPU | +0.012 | -0.009–+0.042 | +0.002 | -0.023–+0.032 |
| nnPU-sampled − FullPool-nnPU | -0.015 | -0.042–+0.012 | -0.005 | -0.042–+0.035 |
| IPW-nnPU − Ignore | -0.072 | -0.105–-0.040 | -0.096 | -0.142–-0.045 |

## FullPool approximation

Negative values mean IPW is closer to FullPool than unweighted sampled-U nnPU.

| Gap contrast | Δ absolute AUC gap | 95% CI | Δ absolute AP gap | 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | -0.012 | -0.033–+0.007 | -0.009 | -0.024–+0.010 |

This experiment identifies candidate-sampling correction only. It does not identify annotation propensity, missing-positive precision, or Oracle performance.
