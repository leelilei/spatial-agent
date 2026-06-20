---
telephone_index: 31
canonical: true
aliases: []
title: "Language Models (Mostly) Know What They Know"
category: 03_hallucination_factuality
role: model knowledge and calibration
decision: cite
doi: 
venue: "arXiv"
year: 2022
source_quality: preprint_or_unresolved
fulltext: assets/papers/fulltext/03_hallucination_factuality/31_language-models-mostly-know-what-they-know.fulltext.md
pdf: assets/papers/pdf/03_hallucination_factuality/31_language-models-mostly-know-what-they-know.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# Language Models (Mostly) Know What They Know

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

This paper is important for our belief/knowledge language because it studies whether models can evaluate their own claims. It supports the idea that there may be a measurable gap between answer generation and confidence or validity assessment.

## Core Question

The paper asks whether language models can predict when their own answers or claims are true.

## Method / Evidence Base

It uses calibrated formats such as P(True), asking models to propose answers and then assess the probability that those answers are valid.

## Core Claim / Result

The relevant takeaway is conditional: models can show useful self-evaluation/calibration under the right prompting formats, but this is fragile and format-dependent. Telephone therefore should not assume that self-report alone equals belief fidelity.

## Evidence We May Cite

- Models can sometimes evaluate the truth of their own generated claims.
- Calibration depends strongly on elicitation format.
- Self-evaluation is a distinct measurement target from answer generation.

## Telephone Bridge

- Speech vs belief: answer, confidence, and held belief need separate elicitation.
- Measurement / rigor: Telephone's final probe should be framed as behavioral evidence, not direct access to mind.
- Failed natural lever: self-evaluation may help, but is not guaranteed in social update settings.

## What We Add Beyond This Paper

Telephone uses a simpler operational definition: after transmission, what answer does the agent give about the current fact?

## Draft-Ready Use Sentence

> Work on whether language models know what they know shows that self-evaluation can be elicited but is prompt-sensitive; Telephone therefore treats held belief operationally, using post-transmission factual probes rather than assuming utterances or confidence reports are definitive.

## Caveats

- Useful for methods caveat language.
- Do not overclaim about literal belief or consciousness.

## Citation Decision

Decision: `cite`

Reason: Strong measurement and epistemic-status background.
