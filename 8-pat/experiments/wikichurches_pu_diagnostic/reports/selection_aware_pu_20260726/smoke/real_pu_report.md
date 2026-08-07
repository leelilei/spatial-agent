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
- Repeats: 1 / label
- Primary PU prior: 0.25; sensitivity priors: 0.10, 0.25, 0.50
- Selection-aware prior: 0.25; propensity floors: 0.10, 0.20

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | U score | U > RN95 |
|---|---:|---:|---:|---:|---:|---:|---:|
| PN | 0.903 | 0.822–0.967 | 0.568 | 0.399–0.735 | 0.537 | 0.394 | 0.126 |
| Ignore | 0.916 | 0.850–0.969 | 0.629 | 0.463–0.796 | 0.545 | 0.480 | 0.311 |
| nnPU(pi=0.10) | 0.517 | 0.366–0.675 | 0.201 | 0.093–0.354 | 0.236 | 0.044 | 0.000 |
| nnPU(pi=0.25) | 0.633 | 0.476–0.773 | 0.246 | 0.144–0.357 | 0.544 | 0.271 | 0.000 |
| nnPU(pi=0.50) | 0.740 | 0.563–0.900 | 0.447 | 0.251–0.641 | 0.896 | 0.738 | 0.006 |
| SA-nnPU(pi=0.25,e>=0.10) | 0.654 | 0.493–0.796 | 0.276 | 0.168–0.384 | 0.576 | 0.299 | 0.000 |
| SA-nnPU(pi=0.25,e>=0.20) | 0.654 | 0.493–0.796 | 0.276 | 0.168–0.384 | 0.576 | 0.299 | 0.000 |

## Selection-proxy diagnostics

| Method | raw e min | raw e median | raw e max | positive ESS |
|---|---:|---:|---:|---:|
| SA-nnPU(pi=0.25,e>=0.10) | 0.557 | 0.768 | 0.893 | 7.17 |
| SA-nnPU(pi=0.25,e>=0.20) | 0.557 | 0.768 | 0.893 | 7.17 |

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| nnPU(pi=0.25) − PN | -0.270 | -0.427–-0.151 | -0.322 | -0.470–-0.171 |
| nnPU(pi=0.25) − Ignore | -0.283 | -0.439–-0.159 | -0.383 | -0.548–-0.204 |
| SA-nnPU(pi=0.25,e>=0.10) − nnPU(pi=0.25) | +0.021 | +0.002–+0.042 | +0.031 | +0.009–+0.060 |
| SA-nnPU(pi=0.25,e>=0.10) − PN | -0.249 | -0.409–-0.131 | -0.292 | -0.437–-0.146 |
| SA-nnPU(pi=0.25,e>=0.10) − Ignore | -0.262 | -0.419–-0.139 | -0.353 | -0.521–-0.171 |
| SA-nnPU(pi=0.25,e>=0.20) − nnPU(pi=0.25) | +0.021 | +0.002–+0.042 | +0.031 | +0.009–+0.060 |
| SA-nnPU(pi=0.25,e>=0.20) − PN | -0.249 | -0.409–-0.131 | -0.292 | -0.437–-0.146 |
| SA-nnPU(pi=0.25,e>=0.20) − Ignore | -0.262 | -0.419–-0.139 | -0.353 | -0.521–-0.171 |

## Interpretation limit

`U > RN95` is a recovery-candidate rate, not precision: U has no human truth. The held-out metrics only test known official labels. SA-nnPU uses an annotation-selection proxy, not an identified causal propensity. This experiment can reject an unstable P/U formulation, but it cannot estimate the real missing-positive rate or an Oracle gap.
