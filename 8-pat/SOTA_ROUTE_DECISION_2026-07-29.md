# SOTA route decision

## Bottom line

There is currently no confirmed accuracy SOTA in the 8-pat project.

The project does have a paper-level GO: DCTPR provides a reproducible
accuracy--efficiency contribution across CUB and Stanford Dogs. It must not be
renamed or advertised as an accuracy-SOTA method.

## Attempts completed

| Attempt | Signal | Frozen decision |
|---|---:|---|
| SAGE solver-agreement ensemble | +0.0617pp on untouched Dogs confirmation | No-Go |
| DCPR unknown-prior recovery | +0.9644pp on CUB development; +0.9657pp internal transfer | No-Go; missed +1.0pp gate |

Both results are useful research evidence. Neither passes its preregistered
claim gate.

## What would count as SOTA

A legitimate SOTA claim needs all of the following:

1. a public dataset and standard split/task sampler;
2. matched backbone, pretraining, image size, shots, ways, and query protocol;
3. comparison with the strongest current methods, not a deliberately weak baseline;
4. untouched confirmation or official test evaluation;
5. a result above the strongest matched method with uncertainty and repeated tasks;
6. public code/protocol sufficient for reproduction.

Creating a new benchmark does not automatically make the first submitted method
a meaningful SOTA. A benchmark paper is also not merely a survey: it can be a
research contribution when it introduces a justified task, dataset/protocol,
analysis, and strong baselines. That is a different paper route from claiming a
new recognition method.

## Recommended execution decision

Finish and submit the DCTPR accuracy--efficiency manuscript now. Do not spend
more of this paper's evidence budget on solver gates or prior-estimator variants.

If an accuracy-SOTA project is started, treat it as a new project on the public
5-way Dirichlet imbalanced transductive protocol. Reproduce the public backbone
and strongest baselines first. Only develop a method if that reproduction leaves
a measured, non-oracle headroom of several percentage points. SOTA cannot be
promised before the confirmation run.

