---
telephone_index: 40
canonical: true
aliases: []
title: "ANAH-v2"
category: 03_hallucination_factuality
role: hallucination benchmark extension
decision: background
doi: 10.52202/079017-1916
venue: "Advances in Neural Information Processing Systems 37"
year: 2024
source_quality: conference
fulltext: assets/papers/fulltext/03_hallucination_factuality/40_anah-v2.fulltext.md
pdf: assets/papers/pdf/03_hallucination_factuality/40_anah-v2.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# ANAH-v2

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

ANAH-v2 is background for long-form hallucination annotation. It is useful if we need to justify scalable oversight and annotation difficulty, but it is not central to Telephone's mechanism.

## Core Question

The paper addresses hallucination detection and mitigation for long-form QA, where manual annotation is costly and existing annotators may be unreliable.

## Method / Evidence Base

It introduces an iterative self-training or scalable annotation approach for hallucination data.

## Core Claim / Result

The relevant takeaway is that hallucination oversight in long-form outputs remains difficult and dataset-intensive. Telephone avoids some of that complexity by using a controlled factual target.

## Evidence We May Cite

- Long-form hallucination evaluation is expensive and hard to scale.
- Annotation reliability is itself a problem in hallucination datasets.
- The paper supports our use of simpler, controlled truth conditions.

## Telephone Bridge

- Measurement / rigor: our task trades breadth for strong ground truth.
- Fidelity vs reach: not about social reach; about factual annotation.
- Not our claim: no direct speech-belief evidence.

## What We Add Beyond This Paper

Telephone supplies a compact experimental paradigm where factual correctness is known by design, reducing dependence on broad hallucination annotation.

## Draft-Ready Use Sentence

> Long-form hallucination benchmarks such as ANAH-v2 highlight the cost and reliability challenges of factuality annotation; Telephone instead uses controlled truth changes to make social-fidelity failures directly measurable.

## Caveats

- Background only.
- Use only if discussing why a controlled benchmark is valuable.

## Citation Decision

Decision: `background`

Reason: Evaluation background but not a main citation.
