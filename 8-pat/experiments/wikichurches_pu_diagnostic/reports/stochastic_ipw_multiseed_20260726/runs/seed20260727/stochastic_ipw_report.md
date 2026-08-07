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
- Sampled rows: 692
- Labels: 9
- Repeats: 30 / label
- Class prior: 0.25

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | pool score |
|---|---:|---:|---:|---:|---:|---:|
| PN-sampled | 0.874 | 0.808–0.927 | 0.564 | 0.452–0.660 | 0.546 | 0.371 |
| Ignore | 0.874 | 0.816–0.921 | 0.551 | 0.449–0.649 | 0.540 | 0.447 |
| nnPU-sampled | 0.780 | 0.682–0.865 | 0.449 | 0.327–0.563 | 0.908 | 0.488 |
| IPW-nnPU | 0.799 | 0.705–0.878 | 0.472 | 0.354–0.581 | 0.920 | 0.520 |
| FullPool-nnPU | 0.790 | 0.697–0.867 | 0.453 | 0.338–0.560 | 0.913 | 0.462 |

## Sampling diagnostics

- q min/median/max over split samples: 0.017/0.037/0.078
- IPW ESS mean: 18.81

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| IPW-nnPU − nnPU-sampled | +0.020 | -0.004–+0.047 | +0.023 | -0.017–+0.063 |
| IPW-nnPU − FullPool-nnPU | +0.010 | -0.015–+0.036 | +0.019 | -0.012–+0.055 |
| nnPU-sampled − FullPool-nnPU | -0.010 | -0.027–+0.007 | -0.004 | -0.043–+0.034 |
| IPW-nnPU − Ignore | -0.075 | -0.128–-0.025 | -0.079 | -0.144–-0.015 |

## FullPool approximation

Negative values mean IPW is closer to FullPool than unweighted sampled-U nnPU.

| Gap contrast | Δ absolute AUC gap | 95% CI | Δ absolute AP gap | 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | -0.006 | -0.019–+0.005 | -0.004 | -0.027–+0.022 |

This experiment identifies candidate-sampling correction only. It does not identify annotation propensity, missing-positive precision, or Oracle performance.
