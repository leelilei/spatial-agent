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
- Sampled rows: 699
- Labels: 9
- Repeats: 30 / label
- Class prior: 0.25

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | pool score |
|---|---:|---:|---:|---:|---:|---:|
| PN-sampled | 0.872 | 0.804–0.925 | 0.569 | 0.456–0.665 | 0.547 | 0.370 |
| Ignore | 0.874 | 0.816–0.921 | 0.551 | 0.449–0.649 | 0.540 | 0.447 |
| nnPU-sampled | 0.776 | 0.689–0.856 | 0.451 | 0.336–0.554 | 0.903 | 0.469 |
| IPW-nnPU | 0.784 | 0.693–0.862 | 0.453 | 0.342–0.553 | 0.914 | 0.492 |
| FullPool-nnPU | 0.790 | 0.697–0.867 | 0.453 | 0.338–0.560 | 0.913 | 0.462 |

## Sampling diagnostics

- q min/median/max over split samples: 0.017/0.037/0.080
- IPW ESS mean: 19.66

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| IPW-nnPU − nnPU-sampled | +0.007 | -0.004–+0.019 | +0.002 | -0.022–+0.022 |
| IPW-nnPU − FullPool-nnPU | -0.006 | -0.020–+0.008 | +0.000 | -0.029–+0.036 |
| nnPU-sampled − FullPool-nnPU | -0.014 | -0.031–+0.005 | -0.002 | -0.038–+0.035 |
| IPW-nnPU − Ignore | -0.091 | -0.136–-0.049 | -0.098 | -0.152–-0.038 |

## FullPool approximation

Negative values mean IPW is closer to FullPool than unweighted sampled-U nnPU.

| Gap contrast | Δ absolute AUC gap | 95% CI | Δ absolute AP gap | 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | -0.007 | -0.018–+0.002 | -0.013 | -0.024–-0.003 |

This experiment identifies candidate-sampling correction only. It does not identify annotation propensity, missing-positive precision, or Oracle performance.
