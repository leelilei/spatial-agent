---
telephone_index: 41
canonical: true
aliases: []
title: "Delusions of Large Language Models"
category: 03_hallucination_factuality
role: LLM delusions / persistent false beliefs
decision: maybe
doi: 
venue: "arXiv"
year: 2025
source_quality: preprint_or_unresolved
fulltext: assets/papers/fulltext/03_hallucination_factuality/41_delusions-of-large-language-models.fulltext.md
pdf: assets/papers/pdf/03_hallucination_factuality/41_delusions-of-large-language-models.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# Delusions of Large Language Models

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

This paper is conceptually useful because 'delusion' names high-confidence hallucination. Telephone's stale beliefs may behave like high-confidence wrong answers, though our evidence is behavioral rather than internal confidence-based.

## Core Question

The paper asks how to identify hallucinations that are not merely wrong but held or generated with abnormally high confidence.

## Method / Evidence Base

It empirically analyzes model confidence or uncertainty patterns around incorrect outputs and proposes the delusion framing.

## Core Claim / Result

The useful takeaway is that false outputs can be difficult to detect when they are stable and high-confidence. That resonates with Telephone's persistent stale-answer failures.

## Evidence We May Cite

- Not all hallucinations are equally uncertain or easy to flag.
- High-belief falsehoods pose a different reliability risk from ordinary errors.
- The framing helps discuss persistence and confidence cautiously.

## Telephone Bridge

- Entrenchment / path dependence: stale answers may persist as if epistemically settled.
- Speech vs belief: confidence would be a future measurement dimension beyond our current probe.
- Measurement / rigor: avoid equating our held-answer metric with internal high confidence unless measured.

## What We Add Beyond This Paper

Telephone contributes social history as a source of persistent wrong answers, without claiming to measure internal confidence directly.

## Draft-Ready Use Sentence

> Work on high-confidence hallucinations or LLM delusions emphasizes that false answers can appear epistemically settled; Telephone studies how social transmission history can produce persistent stale answers even after corrections circulate.

## Caveats

- Maybe citation; verify source quality and venue before final use.
- Do not use the term delusion casually in the main paper without defining it.

## Citation Decision

Decision: `maybe`

Reason: Conceptually related to persistence, but not essential.
