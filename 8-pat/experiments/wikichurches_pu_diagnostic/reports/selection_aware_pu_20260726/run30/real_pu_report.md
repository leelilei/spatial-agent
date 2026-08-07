# Real P/U diagnostic without adjudication

## Protocol boundary

- P: official WikiChurches element boxes;
- U: real candidate regions outside official boxes;
- reliable N: hierarchy-incompatible official boxes;
- evaluation: held-out official P versus held-out reliable N;
- Oracle: unavailable because both annotation CSV files are empty;
- nnPU is a prior-sensitivity diagnostic; candidate selection violates the usual SCAR assumption.
- SA-nnPU uses a propensity proxy fitted from target similarity, box area/aspect, and position; deterministic top-k selection means the true propensity is not identified.

- Frozen encoder: OpenAI CLIP `ViT-B/16`
- Images: 50
- Official boxes: 237
- Unlabeled candidate boxes: 708
- Labels: 9
- Repeats: 30 / label
- Primary PU prior: 0.25; sensitivity priors: 0.10, 0.25, 0.50
- Selection-aware prior: 0.25; propensity floors: 0.10, 0.20

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | U score | U > RN95 |
|---|---:|---:|---:|---:|---:|---:|---:|
| PN | 0.862 | 0.784–0.926 | 0.557 | 0.428–0.662 | 0.537 | 0.398 | 0.142 |
| Ignore | 0.874 | 0.816–0.921 | 0.551 | 0.449–0.649 | 0.540 | 0.486 | 0.361 |
| nnPU(pi=0.10) | 0.728 | 0.627–0.826 | 0.405 | 0.275–0.538 | 0.772 | 0.197 | 0.003 |
| nnPU(pi=0.25) | 0.746 | 0.635–0.848 | 0.422 | 0.272–0.570 | 0.869 | 0.455 | 0.012 |
| nnPU(pi=0.50) | 0.785 | 0.664–0.887 | 0.472 | 0.316–0.606 | 0.956 | 0.824 | 0.014 |
| SA-nnPU(pi=0.25,e>=0.10) | 0.749 | 0.635–0.851 | 0.427 | 0.278–0.573 | 0.874 | 0.459 | 0.014 |
| SA-nnPU(pi=0.25,e>=0.20) | 0.749 | 0.635–0.851 | 0.427 | 0.278–0.573 | 0.874 | 0.459 | 0.014 |

## Selection-proxy diagnostics

| Method | raw e min | raw e median | raw e max | positive ESS |
|---|---:|---:|---:|---:|
| SA-nnPU(pi=0.25,e>=0.10) | 0.543 | 0.778 | 0.889 | 7.16 |
| SA-nnPU(pi=0.25,e>=0.20) | 0.543 | 0.778 | 0.889 | 7.16 |

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| nnPU(pi=0.25) − PN | -0.116 | -0.164–-0.067 | -0.135 | -0.200–-0.064 |
| nnPU(pi=0.25) − Ignore | -0.128 | -0.192–-0.066 | -0.129 | -0.210–-0.031 |
| SA-nnPU(pi=0.25,e>=0.10) − nnPU(pi=0.25) | +0.002 | -0.003–+0.008 | +0.005 | -0.003–+0.014 |
| SA-nnPU(pi=0.25,e>=0.10) − PN | -0.114 | -0.163–-0.064 | -0.130 | -0.191–-0.060 |
| SA-nnPU(pi=0.25,e>=0.10) − Ignore | -0.126 | -0.193–-0.062 | -0.124 | -0.204–-0.026 |
| SA-nnPU(pi=0.25,e>=0.20) − nnPU(pi=0.25) | +0.002 | -0.003–+0.008 | +0.005 | -0.003–+0.014 |
| SA-nnPU(pi=0.25,e>=0.20) − PN | -0.114 | -0.163–-0.064 | -0.130 | -0.191–-0.060 |
| SA-nnPU(pi=0.25,e>=0.20) − Ignore | -0.126 | -0.193–-0.062 | -0.124 | -0.204–-0.026 |

## Interpretation limit

`U > RN95` is a recovery-candidate rate, not precision: U has no human truth. The held-out metrics only test known official labels. SA-nnPU uses an annotation-selection proxy, not an identified causal propensity. This experiment can reject an unstable P/U formulation, but it cannot estimate the real missing-positive rate or an Oracle gap.
