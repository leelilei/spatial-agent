# PAT-D-260728-007 result report

## Decision

**NO-GO: neither K2 facility selector passed the preregistered benefit or
safety branch. The active-selector direction is stopped.**

The official CUB test was not decoded or encoded. No winner is produced, so
paired confirmation, CCT20+ confirmatory method validation, and final test
unlock remain forbidden.

## Frozen comparison

Both policies selected exactly two official-train images per class and outer
fold. Selection used only the sanitized image manifest, frozen ordinary-image
ResNet-50 features, complete class labels, and fold-training linear-head
probabilities.

| Strategy | OOF BA | vs Global | vs Random-K2 mean | Negative-transfer rate | vs Random-K2 rate | Worst class |
|---|---:|---:|---:|---:|---:|---:|
| Random K2, 3-seed mean | 69.68% | +4.23pp | — | 22.50% | — | −30 to −40pp |
| Feature-Facility | 69.60% | +4.15pp | −0.08pp | 23.50% | +1.00pp | −40pp |
| Gradient-Facility | **69.80%** | **+4.35pp** | **+0.12pp** | **23.00%** | +0.50pp | −40pp |

The benefit branch required BA ≥70.18% and negative-transfer rate ≤22.50%.
The safety branch required BA ≥69.43% and negative-transfer rate ≤17.50%.
Neither policy satisfied either conjunction.

## Selector diagnostics

The five fold-training task heads reached 97.1%–98.3% training accuracy, with
mean maximum probability near 29% under the frozen label-smoothing
configuration. Every selection mask contained 400 rows per fold, exactly two
per class, with zero OOF rows.

Despite using task probabilities, Gradient-Facility selected almost the same
pairs as Feature-Facility: pair-mask overlap was 95.5%–98.8% across folds.
Within a class, the normalized softmax-error directions were too similar for
the implicit gradient kernel to depart materially from the ordinary feature
kernel.

## Interpretation

Moving from K1 point scoring to K2 set coverage produced only a 0.12pp BA
increase over the Random-K2 mean and slightly worsened class-level negative
transfer. Together with `PAT-D-260728-005`, the evidence now rejects the
working claim that the tested ordinary-image geometry can reliably predict
which CUB images have greater downstream keypoint annotation value.

This does not negate the strong sparse-annotation value established by
`PAT-D-260728-004`. It shows that Random is already a difficult baseline and
that the tested active selectors do not add a defensible method contribution.

## Stage-gate consequence

Per the frozen protocol:

1. stop adding selection heuristics on this CUB setup;
2. do not run paired selector confirmation;
3. do not present CCT20+ as confirmatory evidence for an unvalidated method;
4. do not generate the one-time final-evaluation lock;
5. keep CUB test and CCT Cis/Trans unopened.

## Traceability

- Reused feature SHA256:
  `c653df616b210d3f33559d727943db374ed911c35c87a00f0ec6e68dfad3c997`
- Selection-mask SHA256:
  `bc178bc8aeb33fcd9430740bb966146a7119a31d54334e35813264ee1d3366bc`
- Pair table SHA256:
  `343956aa454c9804ada9ab8fe2913322282d028c501970b01e33a081bd967e04`
- Task-head diagnostics SHA256:
  `6c4596b08b99a08649c7585aa3e07910370f206b732d4497643e1987cf110823`
- Official-test images decoded or encoded: `0`

