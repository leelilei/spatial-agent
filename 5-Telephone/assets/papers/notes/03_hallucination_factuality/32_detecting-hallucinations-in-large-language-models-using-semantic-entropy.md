---
telephone_index: 32
canonical: true
aliases: []
title: "Detecting Hallucinations in Large Language Models Using Semantic Entropy"
category: 03_hallucination_factuality
role: semantic entropy hallucination detection
decision: cite
doi: 10.1038/s41586-024-07421-0
venue: "Nature"
year: 2024
source_quality: journal
fulltext: assets/papers/fulltext/03_hallucination_factuality/32_detecting-hallucinations-in-large-language-models-using-semantic-entropy.fulltext.md
pdf: assets/papers/pdf/03_hallucination_factuality/32_detecting-hallucinations-in-large-language-models-using-semantic-entropy.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# Detecting Hallucinations in Large Language Models Using Semantic Entropy

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

Semantic entropy is a strong metric reference because it measures uncertainty over meanings rather than surface strings. This is directly relevant to Telephone's need to judge whether agents preserve the same factual state across paraphrases.

## Core Question

The paper asks how to detect hallucinations by estimating uncertainty at the semantic rather than lexical level.

## Method / Evidence Base

It groups generated answers by meaning and computes entropy over semantic clusters, distinguishing alternative phrasings from genuinely different claims.

## Core Claim / Result

The key insight for us is methodological: factuality evaluation should account for semantic equivalence. Telephone's judge or metric should likewise focus on the current fact, not exact wording.

## Evidence We May Cite

- Meaning-level uncertainty can be more appropriate than token- or string-level disagreement.
- Hallucination detection benefits from grouping paraphrases that express the same answer.
- The paper supports semantic judging in Telephone.

## Telephone Bridge

- Measurement / rigor: our correctness metric should be semantic, not exact-match.
- Fidelity vs reach: fidelity means preserving the fact, not preserving literal phrasing.
- Speech vs belief: paraphrased correct speech can still be correct; stale semantic content is the failure.

## What We Add Beyond This Paper

Telephone applies semantic correctness to a social-transmission setting with evolving ground truth.

## Draft-Ready Use Sentence

> Semantic-entropy work argues that hallucination detection should reason over meanings rather than surface forms; Telephone adopts the same principle when judging whether a transmitted update preserves the current factual state.

## Caveats

- The extracted abstract is weak, so verify details from the full PDF before quoting specifics.
- Use for metric rationale.

## Citation Decision

Decision: `cite`

Reason: Important semantic-evaluation support.
