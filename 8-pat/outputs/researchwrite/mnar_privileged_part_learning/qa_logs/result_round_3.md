# Result integration QA — round 3

## Decision integrity

- Limited adaptation was pre-registered before model predictions: yes.
- Hyperparameter search after observing OOF results: no.
- Validation images read or encoded: 0.
- Test images read or encoded: 0.
- The +2.5 pp and −2 pp gates were applied without relaxation: yes.
- MCAR/MAR/MNAR arms stopped after Oracle failure: yes.

## Claim control

- Supported: adapting the final CLIP visual block raises the global train-only
  OOF balanced accuracy to 94.5625%.
- Supported: the adapted full-part Oracle reaches 94.0625%, a −0.5000 pp
  difference, with a −2.5000 pp worst-class delta.
- Supported: all three tested PartImageNet mechanism stages failed their
  pre-registered Oracle/safety gates.
- Prohibited: claiming that privileged part information never helps.
- Prohibited: claiming an MNAR correction result; no correction arm was run.
- Prohibited: claiming the broad research question is novel without a complete
  citation-chain audit.

## Direction decision

PartImageNet method development is stopped. A continued method paper requires a
new benchmark on which an established privileged-part mechanism first
reproduces a positive Oracle ceiling. Otherwise the defensible contribution is
a diagnostic/benchmark study of negative transfer and annotation selection.

## Scores

| Dimension | Score / 10 |
|---|---:|
| Traceability | 9.5 |
| Protocol fidelity | 9.6 |
| Claim calibration | 9.5 |
| Negative-result reporting | 9.6 |
| Stopping-rule compliance | 9.7 |

Average: **9.58 / 10**.

