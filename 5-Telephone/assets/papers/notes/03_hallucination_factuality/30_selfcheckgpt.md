---
telephone_index: 30
canonical: true
aliases: []
title: "SelfCheckGPT"
category: 03_hallucination_factuality
role: self-consistency hallucination detection
decision: cite
doi: 10.18653/v1/2023.emnlp-main.557
venue: "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing"
year: 2023
source_quality: conference
fulltext: assets/papers/fulltext/03_hallucination_factuality/30_selfcheckgpt.fulltext.md
pdf: assets/papers/pdf/03_hallucination_factuality/30_selfcheckgpt.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# SelfCheckGPT

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

SelfCheckGPT matters as a black-box hallucination detector based on inconsistency across samples. It helps situate our measurement problem: hallucination can be detected behaviorally, but Telephone measures social belief fidelity rather than self-consistency of one model.

## Core Question

The paper asks how to detect factual hallucinations from a generative model without access to token probabilities or external databases.

## Method / Evidence Base

It samples multiple passages from the same model and checks whether claims are consistent across samples, using inconsistency as a signal of hallucination.

## Core Claim / Result

The central insight is that a model's own sampled outputs can reveal uncertainty or unsupported claims. Telephone similarly uses behavioral probes, but across agents and time rather than repeated samples from one model.

## Evidence We May Cite

- Black-box factuality can be probed through generated text behavior.
- Inconsistency across sampled outputs is informative about hallucination risk.
- The paper supports the value of behavioral measurement when internals are unavailable.

## Telephone Bridge

- Measurement / rigor: Telephone uses behavioral held-answer probes instead of hidden-state access.
- Speech vs belief: output variability cautions against treating one utterance as stable belief.
- Fidelity vs reach: consistency is within-model; our fidelity is across social transmission.

## What We Add Beyond This Paper

Telephone contributes a multi-agent, truth-changing setting rather than a single-model hallucination detector.

## Draft-Ready Use Sentence

> SelfCheckGPT demonstrates that black-box generation behavior can expose hallucination risk through inconsistency; Telephone applies the same behavioral-measurement spirit to social transmission, probing whether agents retain the corrected fact after communication.

## Caveats

- Cite as measurement background, not as a social-interaction paper.
- Avoid implying SelfCheckGPT measures belief.

## Citation Decision

Decision: `cite`

Reason: Useful factuality/hallucination measurement background.
