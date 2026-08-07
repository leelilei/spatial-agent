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
- Sampled rows: 669
- Labels: 9
- Repeats: 30 / label
- Class prior: 0.25

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | pool score |
|---|---:|---:|---:|---:|---:|---:|
| PN-sampled | 0.873 | 0.805–0.928 | 0.571 | 0.455–0.667 | 0.546 | 0.380 |
| Ignore | 0.874 | 0.816–0.921 | 0.551 | 0.449–0.649 | 0.540 | 0.447 |
| nnPU-sampled | 0.782 | 0.699–0.858 | 0.428 | 0.312–0.538 | 0.911 | 0.512 |
| IPW-nnPU | 0.795 | 0.712–0.866 | 0.444 | 0.326–0.554 | 0.924 | 0.543 |
| FullPool-nnPU | 0.790 | 0.697–0.867 | 0.453 | 0.338–0.560 | 0.913 | 0.462 |

## Sampling diagnostics

- q min/median/max over split samples: 0.017/0.033/0.082
- IPW ESS mean: 15.97

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| IPW-nnPU − nnPU-sampled | +0.013 | +0.003–+0.023 | +0.016 | -0.004–+0.038 |
| IPW-nnPU − FullPool-nnPU | +0.005 | -0.006–+0.018 | -0.009 | -0.037–+0.019 |
| nnPU-sampled − FullPool-nnPU | -0.008 | -0.021–+0.009 | -0.025 | -0.062–+0.017 |
| IPW-nnPU − Ignore | -0.080 | -0.113–-0.046 | -0.107 | -0.166–-0.046 |

## FullPool approximation

Negative values mean IPW is closer to FullPool than unweighted sampled-U nnPU.

| Gap contrast | Δ absolute AUC gap | 95% CI | Δ absolute AP gap | 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | -0.002 | -0.015–+0.013 | -0.014 | -0.033–+0.003 |

This experiment identifies candidate-sampling correction only. It does not identify annotation propensity, missing-positive precision, or Oracle performance.
