---
telephone_index: 29
canonical: true
aliases: []
title: "TruthfulQA: Measuring How Models Mimic Human Falsehoods"
category: 03_hallucination_factuality
role: truthfulness benchmark / metric anchor
decision: must-cite
doi: 10.18653/v1/2022.acl-long.229
venue: "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics"
year: 2022
source_quality: conference
fulltext: assets/papers/fulltext/03_hallucination_factuality/29_truthfulqa-measuring-how-models-mimic-human-falsehoods.fulltext.md
pdf: assets/papers/pdf/03_hallucination_factuality/29_truthfulqa-measuring-how-models-mimic-human-falsehoods.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# TruthfulQA: Measuring How Models Mimic Human Falsehoods

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

TruthfulQA is a must-cite measurement predecessor. It makes factuality specifically about avoiding learned human falsehoods, which is close to our concern that agents can reproduce stale or false content even when fluent.

## Core Question

The benchmark asks whether language models answer truthfully when questions target common misconceptions or false beliefs present in human text.

## Method / Evidence Base

It provides 817 questions across many categories and evaluates models on truthfulness and informativeness rather than mere plausibility.

## Core Claim / Result

The key lesson is that larger or more capable language models can still mimic falsehoods learned from data. For Telephone, this supports treating truthfulness as a measurable behavioral property distinct from fluency.

## Evidence We May Cite

- Truthfulness can be benchmarked directly with adversarial misconception questions.
- Imitating human text can reproduce human false beliefs.
- Factuality measurement should separate plausible language from correct answers.

## Telephone Bridge

- Measurement / rigor: Telephone follows the same spirit by using ground-truthed factual probes.
- Speech vs belief: fluent statements cannot be treated as truth without an answer probe.
- Fidelity vs reach: our endpoint is social update fidelity rather than one-shot truthfulness.

## What We Add Beyond This Paper

Telephone shifts factuality from isolated QA to a dynamic social process where the truth changes and must be transmitted, spoken, and retained.

## Draft-Ready Use Sentence

> TruthfulQA shows that language models can produce plausible answers that mimic human falsehoods; Telephone extends factuality evaluation from isolated questions to social transmission, testing whether updated truths remain faithful after agents communicate.

## Caveats

- Use the canonical index 29 note/citation, not duplicate index 5.
- Verify benchmark numbers if quoted.

## Citation Decision

Decision: `must-cite`

Reason: Core factuality measurement precedent.
