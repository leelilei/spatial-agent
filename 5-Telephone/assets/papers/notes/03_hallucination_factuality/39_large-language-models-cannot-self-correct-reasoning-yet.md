---
telephone_index: 39
canonical: true
aliases: []
title: "Large Language Models Cannot Self-Correct Reasoning Yet"
category: 03_hallucination_factuality
role: correction limit / failed natural lever
decision: cite
doi:
venue: arXiv
year: 2023
source_quality: preprint_or_unresolved
fulltext: assets/papers/fulltext/03_hallucination_factuality/39_large-language-models-cannot-self-correct-reasoning-yet.fulltext.md
pdf: assets/papers/pdf/03_hallucination_factuality/39_large-language-models-cannot-self-correct-reasoning-yet.pdf
read_status: deep-read
deep_read_scope: manual-project-deep-read

---

# Large Language Models Cannot Self-Correct Reasoning Yet

## Why This Paper Matters For Telephone

This paper supports the broader claim that correction is not automatic for LLMs.
It focuses on intrinsic self-correction: an LLM revises an initial response based
on its own capabilities without high-quality external feedback. The central result
is negative: models often fail to improve and may degrade after self-correction.

For Telephone, this is useful because our source/broadcast experiments also test
correction assumptions. But the analogy must be drawn carefully. Huang et al. study
individual-model reasoning correction; Telephone studies social correction in a
multi-agent memory system.

## Core Claim / Result

The paper argues that LLMs struggle to self-correct reasoning without external
feedback. It also critiques prior self-correction evaluations, noting that some
reported gains rely on oracle labels, better instructions hidden in feedback, or
unfair cost baselines. The paper also reports that multi-agent debate may not
outperform self-consistency under equivalent response budgets.

## Evidence We May Cite

- Intrinsic self-correction is unreliable when models lack external feedback.
- Apparent self-correction gains may disappear when oracle labels or prompt
  confounds are removed.
- Correction should be evaluated against fair baselines and with attention to
  where feedback information comes from.
- Debate-like social critique is not automatically superior under cost-equivalent
  comparisons.

## Telephone Bridge

- Fidelity vs reach: The paper reinforces that producing another response is not
  the same as producing a corrected response.
- Speech vs belief: It does not study belief, but it supports our skepticism that
  additional language alone guarantees correction.
- Entrenchment / path dependence: The paper does not test path dependence, but it
  makes room for our finding that late correction speech can fail.
- Failed natural lever: Direct support for why self-correction and critique are
  not assumed cures.
- Measurement / rigor: Strongly relevant to our claim hygiene: compare interventions
  carefully and do not over-credit prompt artifacts.

## What We Add Beyond This Paper

This paper's correction object is an individual reasoning answer. Telephone's
correction object is collective held belief after social transmission. We also
distinguish an external source from broadcast-to-all and show a sharper
dissociation: a source can change the conversation stream while final belief
remains near baseline.

## Draft-Ready Use Sentence

> Prior work on LLM self-correction shows that additional rounds of revision or
> critique do not reliably repair errors without high-quality external feedback;
> Telephone extends this caution to social correction, where even an authoritative
> source can change utterances without repairing held belief.

## Caveats

- Source-quality issues: currently recorded as arXiv; verify final source before
  bibliography freeze.
- Extraction issues: local fulltext is usable and unflagged.
- Not our claim: do not cite this as evidence for social entrenchment; it is an
  individual-model correction limit.

## Citation Decision

Decision: `cite`

Reason: Useful for the failed-correction and rigor framing, but not a direct
society-scale neighbor.
