---
telephone_index: 36
canonical: true
aliases: []
title: "RAGTruth"
category: 03_hallucination_factuality
role: RAG hallucination benchmark
decision: cite
doi: 10.18653/v1/2024.acl-long.585
venue: "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics"
year: 2024
source_quality: conference
fulltext: assets/papers/fulltext/03_hallucination_factuality/36_ragtruth.fulltext.md
pdf: assets/papers/pdf/03_hallucination_factuality/36_ragtruth.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# RAGTruth

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

RAGTruth is useful because it evaluates whether generated claims are supported by retrieved evidence. That is not our setting, but the supported/unsupported distinction helps explain Telephone's factual judge.

## Core Question

The paper asks how to benchmark hallucinations in retrieval-augmented generation, where outputs may contradict or go beyond retrieved content.

## Method / Evidence Base

It builds a corpus with hallucination annotations for RAG outputs across domains or tasks, targeting unsupported or contradictory claims.

## Core Claim / Result

The key lesson is that access to evidence does not automatically prevent unsupported claims. Telephone has a social analogue: exposure to a correction does not automatically install the corrected belief.

## Evidence We May Cite

- RAG systems can still produce unsupported or contradictory claims despite retrieval.
- Claim-level annotation is valuable for factuality evaluation.
- The paper supports distinguishing evidence exposure from faithful output.

## Telephone Bridge

- Failed natural lever: retrieval exposure is to RAG what source exposure is to Telephone: helpful in theory, insufficient in practice.
- Measurement / rigor: claim-level support maps to our current-fact correctness judgments.
- Fidelity vs reach: seeing evidence differs from preserving the update.

## What We Add Beyond This Paper

Telephone shifts from document-grounded generation to socially grounded update transmission, where the evidence arrives through other agents.

## Draft-Ready Use Sentence

> RAGTruth shows that even retrieved evidence does not guarantee supported generation; Telephone finds a social analogue, where exposure to corrected information does not reliably produce durable held belief.

## Caveats

- Good metric/analogy citation, not a direct social-system paper.
- Check label taxonomy before quoting.

## Citation Decision

Decision: `cite`

Reason: Strong evidence-exposure versus faithful-output analogy.
