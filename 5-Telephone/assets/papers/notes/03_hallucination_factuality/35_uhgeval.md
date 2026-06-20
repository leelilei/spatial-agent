---
telephone_index: 35
canonical: true
aliases: []
title: "UHGEval"
category: 03_hallucination_factuality
role: universal hallucination generation/evaluation
decision: background
doi: 10.18653/v1/2024.acl-long.288
venue: "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics"
year: 2024
source_quality: conference
fulltext: assets/papers/fulltext/03_hallucination_factuality/35_uhgeval.fulltext.md
pdf: assets/papers/pdf/03_hallucination_factuality/35_uhgeval.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# UHGEval

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

UHGEval is background for scalable hallucination evaluation. It is less directly useful than TruthfulQA, Semantic Entropy, or RAGTruth, but it supports the claim that hallucination metrics remain an active problem.

## Core Question

The paper addresses limitations of hallucination benchmarks that rely on constrained generation or narrow data construction.

## Method / Evidence Base

It proposes an evaluation dataset or framework for unconstrained hallucination generation/evaluation in professional contexts.

## Core Claim / Result

The useful takeaway is that hallucination evaluation needs to handle open-ended generation. Telephone is also open-ended at the message level but has a controlled factual target.

## Evidence We May Cite

- Existing hallucination benchmarks may be constrained by dataset-generation choices.
- Open-ended hallucination evaluation is an active need.
- The paper helps justify why our judge must handle varied natural-language outputs.

## Telephone Bridge

- Measurement / rigor: supports robust semantic judging over unconstrained text.
- Fidelity vs reach: our task constrains the truth while allowing flexible messages.
- Not our claim: not about multi-agent social transmission.

## What We Add Beyond This Paper

Telephone controls the factual state while allowing social messages to vary, producing a focused form of open-ended factuality evaluation.

## Draft-Ready Use Sentence

> Recent hallucination-evaluation work emphasizes the difficulty of judging unconstrained model outputs; Telephone similarly allows flexible social messages but anchors evaluation to a known current fact.

## Caveats

- Background only.
- Use only if discussing evaluation breadth.

## Citation Decision

Decision: `background`

Reason: Metric background with limited direct connection.
