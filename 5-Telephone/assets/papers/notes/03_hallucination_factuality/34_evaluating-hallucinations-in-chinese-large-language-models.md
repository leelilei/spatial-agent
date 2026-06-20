---
telephone_index: 34
canonical: true
aliases: []
title: "Evaluating Hallucinations in Chinese Large Language Models"
category: 03_hallucination_factuality
role: Chinese hallucination evaluation
decision: background
doi: 
venue: "arXiv"
year: 2023
source_quality: preprint_or_unresolved
fulltext: assets/papers/fulltext/03_hallucination_factuality/34_evaluating-hallucinations-in-chinese-large-language-models.fulltext.md
pdf: assets/papers/pdf/03_hallucination_factuality/34_evaluating-hallucinations-in-chinese-large-language-models.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# Evaluating Hallucinations in Chinese Large Language Models

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

This paper is mainly background. It shows hallucination evaluation in Chinese LLMs and distinguishes imitative falsehoods from factual fabrication, which may help if we need a broader benchmark paragraph.

## Core Question

The paper asks how to evaluate hallucinations in Chinese large language models with culturally and historically grounded adversarial questions.

## Method / Evidence Base

It builds HalluQA with questions spanning domains and distinguishes types such as imitative falsehood and factual fabrication.

## Core Claim / Result

The key value is the taxonomy: models may fail by reproducing false beliefs or fabricating facts. Telephone's stale-answer failures are closer to imitative or persistent falsehood than arbitrary fabrication.

## Evidence We May Cite

- Hallucination benchmarks can be language- and culture-specific.
- Imitative falsehood and factual fabrication are separable failure types.
- The taxonomy may help describe stale belief as distinct from random hallucination.

## Telephone Bridge

- Measurement / rigor: supports careful labeling of failure types.
- Speech vs belief: not directly about belief, but about output-level falsehood.
- Fidelity vs reach: not a social transmission task.

## What We Add Beyond This Paper

Telephone contributes a dynamic update setting where stale falsehood is induced by social history rather than only benchmark question design.

## Draft-Ready Use Sentence

> Chinese hallucination benchmarks such as HalluQA distinguish imitative falsehoods from factual fabrications; Telephone studies a dynamic variant in which stale answers persist after social exposure to corrected facts.

## Caveats

- Background only.
- Probably omit unless discussing hallucination taxonomies.

## Citation Decision

Decision: `background`

Reason: Taxonomy useful, but not central to Telephone.
