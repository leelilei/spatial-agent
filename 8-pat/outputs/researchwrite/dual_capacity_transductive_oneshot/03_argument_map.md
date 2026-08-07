# Argument map

## Tension

Strong frozen features nearly saturate 10-shot CUB, while one labelled image per
class creates prototype bias and exposes a practically meaningful accuracy gap.

## Central question

Can complementary frozen capacities and unlabeled-query geometry correct
single-support prototypes without neural adaptation?

## Central thesis

DCTPR is a simple, parameter-free task adapter for balanced high-way one-shot
recognition. Across CUB-200 and Stanford Dogs it consistently closes most of the
gap between nearest-support inference and much slower published transductive
optimizers, retaining within 0.61--1.35pp of the best method while running
3.8--49x faster.

## Counterarguments

- Exact class balance may explain part of the gain.
- TIM exceeds DCTPR on CUB and MAP exceeds it on Dogs, so accuracy-SOTA is false.
- The method depends strongly on a uniform query prior.
- A solver-agreement ensemble produced only +0.0617pp on untouched confirmation
  data, so it cannot be used to upgrade the paper to an accuracy-SOTA claim.

## Required final move

Frame the contribution as an accuracy--efficiency tradeoff under an explicit
balanced-prior scope, present imbalance as a measured limitation, and keep the
failed SAGE exploration outside the manuscript's positive contribution list.
