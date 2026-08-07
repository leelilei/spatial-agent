# PAT-D-260728-001 result report

## Decision

**GO: CUB has a positive privileged-part Oracle ceiling under the frozen
10-shot train-only protocol.**

The experiment compares the same ImageNet-pretrained ResNet-50 `layer4`
adaptation budget with and without 15-keypoint Privileged-Pooling supervision.
The official CUB test split was not decoded or encoded.

## Five-fold OOF results

| Fold | Global BA | Full-Keypoint Oracle BA | Delta |
|---:|---:|---:|---:|
| 0 | 65.75% | 70.50% | +4.75pp |
| 1 | 67.25% | 70.75% | +3.50pp |
| 2 | 65.50% | 72.25% | +6.75pp |
| 3 | 66.00% | 71.50% | +5.50pp |
| 4 | 62.75% | 69.75% | +7.00pp |
| **OOF total** | **65.45%** | **70.95%** | **+5.50pp** |

The pre-registered gate required at least +2 pp. It passed in all five folds
and overall. A descriptive class-cluster bootstrap gives a 95% interval of
approximately +3.35 to +7.60 pp; this interval was not a pre-registered
endpoint.

## Safety signal

The positive mean ceiling is not itself a safety result:

- 97/200 classes improved;
- 57/200 were unchanged;
- 46/200 (23%) declined;
- worst observed class delta was −40 pp.

With only ten OOF predictions per class, class deltas move in 10-point steps
and are noisy. Nevertheless, the result justifies the project's focus on
negative transfer rather than permitting a claim that the Oracle is uniformly
beneficial.

## Interpretation

The PartImageNet failures were setting/mechanism-specific. On CUB, synchronized
keypoint attention produces a material, cross-fold gain over a strong matched
global reference. This establishes the positive ceiling required before
studying selectively missing keypoint annotations.

The next experiment may freeze this mechanism and compare MCAR, MAR, MNAR, and
support-isolation at a fixed annotation budget. It must keep reporting
class-level harm and must not open the official test split.

## Traceability

- CaltechDATA archive: `1,150,585,339` bytes,
  MD5 `97eceeb196236b17998738112f37df78`
- Protocol SHA256:
  `d881a13d3806a61811586533c3b4a166118906b1ba9f93c6f524fa4b1941671e`
- Manifest SHA256:
  `53cb7db2360556453d0868d7fcf59328cfd8ed5065cacf35c719c1030e14dded`
- Summary SHA256:
  `9de28c91d81d94840ea5bdaf3fbbfab7f52ec78a174ade1bc7856de0e62c2456`
- Predictions SHA256:
  `4faebc7f9390cd442da103036a76da3bc46123333f6aa47bc9d42c791ff26b1f`
- Official-test images decoded or encoded: `0`

