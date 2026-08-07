# PAT-C-260728-003 result report

## Decision

**NO-GO for the PartImageNet mechanism-development line.**

The final admissible escalation unfroze the last OpenAI CLIP ViT-B/16 visual
residual block and `ln_post`. It compared an adapted global classifier with a
full-mask Privileged-Pooling-inspired Oracle under the same train-only
five-fold protocol.

## Train-only OOF results

| Arm | Balanced accuracy | Gain vs adapted global | Worst-class delta |
|---|---:|---:|---:|
| Adapted Global | 94.5625% | — | — |
| Adapted PrPool Full-Part Oracle | 94.0625% | −0.5000 pp | −2.5000 pp |

The pre-registered gate required at least +2.5 pp with worst-class delta no
lower than −2 pp. Both conditions failed. Validation and test images read or
encoded: **0**.

## Interpretation

Limited backbone adaptation materially strengthened the global reference, but
full part supervision did not add a positive downstream ceiling. The result
rules out the tested PartImageNet mechanism family; it does not establish that
non-randomly missing privileged part annotations are unimportant in general.

Per the frozen stopping rule, MCAR/MAR/MNAR correction arms are not run on this
PartImageNet setup. The next admissible study must first reproduce a positive
privileged-part Oracle on a different benchmark or reposition the contribution
as a diagnostic/benchmark study.

## Traceability

- Protocol SHA256:
  `e826034b58439087915f42cb1f784b2e5c3d0d1d63a409a71a822dcded960d08`
- Summary SHA256:
  `7dad6a5215d12dad8ad8a4516789d7fc1d4f9a98eb4ad99d2e8196a281b24779`
- Predictions SHA256:
  `7053f5a2fbba53c57af53778eeef7aa6e33e171917c0eb7aa420ead6225b1f31`
- Test images read or encoded: `0`
- Validation images read or encoded: `0`

