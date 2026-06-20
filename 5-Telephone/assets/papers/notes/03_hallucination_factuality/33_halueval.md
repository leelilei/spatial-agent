---
telephone_index: 33
canonical: true
aliases: []
title: "HaluEval"
category: 03_hallucination_factuality
role: hallucination evaluation benchmark
decision: cite
doi: 10.18653/v1/2023.emnlp-main.397
venue: "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing"
year: 2023
source_quality: conference
fulltext: assets/papers/fulltext/03_hallucination_factuality/33_halueval.fulltext.md
pdf: assets/papers/pdf/03_hallucination_factuality/33_halueval.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# HaluEval

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

HaluEval is a benchmark reference for hallucination evaluation. It is not a close social-transmission paper, but it helps position Telephone within the broader factuality-evaluation ecosystem.

## Core Question

The paper asks how to construct a large benchmark of hallucinated and non-hallucinated LLM outputs across tasks.

## Method / Evidence Base

It combines generated samples and human annotation to create evaluation data for hallucination detection.

## Core Claim / Result

The relevant point is that hallucination is common enough and varied enough to require task-specific benchmarks. Telephone contributes a different benchmark style: dynamic social update fidelity.

## Evidence We May Cite

- Hallucination can be benchmarked with human-annotated examples.
- Evaluation needs to distinguish unsupported or conflicting content from valid responses.
- The paper helps locate Telephone as a factuality benchmark rather than only an agent-society demo.

## Telephone Bridge

- Measurement / rigor: benchmark construction and annotation precedent.
- Fidelity vs reach: HaluEval is output factuality; Telephone is transmission fidelity.
- Speech vs belief: hallucination labels concern outputs, not durable social belief.

## What We Add Beyond This Paper

Telephone adds temporal and social structure: the correct answer changes, agents communicate, and later belief is probed.

## Draft-Ready Use Sentence

> Hallucination benchmarks such as HaluEval evaluate unsupported or conflicting model outputs; Telephone extends factuality evaluation into a social setting where the core question is whether updated facts remain faithful after transmission.

## Caveats

- Background citation; not part of the main mechanism argument.
- Use sparingly if the paper needs a factuality-benchmark paragraph.

## Citation Decision

Decision: `cite`

Reason: Useful factuality benchmark background.
