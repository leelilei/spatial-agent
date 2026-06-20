---
telephone_index: 38
canonical: true
aliases: []
title: "Just Ask for Calibration"
category: 03_hallucination_factuality
role: calibration prompting / uncertainty
decision: cite
doi: 10.18653/v1/2023.emnlp-main.330
venue: "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing"
year: 2023
source_quality: conference
fulltext: assets/papers/fulltext/03_hallucination_factuality/38_just-ask-for-calibration.fulltext.md
pdf: assets/papers/pdf/03_hallucination_factuality/38_just-ask-for-calibration.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# Just Ask for Calibration

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

Calibration is relevant because Telephone's final probe is an epistemic measurement problem. This paper reminds us that how we ask for confidence or correctness matters, especially after instruction tuning or conversational pressure.

## Core Question

The paper asks how to elicit calibrated confidence from language models in real-world prediction or QA settings.

## Method / Evidence Base

It studies prompting formats for calibration and examines how model probabilities or verbalized confidence relate to correctness.

## Core Claim / Result

The key takeaway is that calibration can be elicited but is sensitive to prompting and model training. Telephone should therefore treat its held-answer probe as an operational response, not a transparent mind-read.

## Evidence We May Cite

- Language-model calibration depends on elicitation method.
- Confidence and correctness can diverge under common generation settings.
- Calibration work provides caution for interpreting agent self-reports.

## Telephone Bridge

- Measurement / rigor: final belief probes need stable wording and careful interpretation.
- Speech vs belief: confident utterance is not equivalent to true belief.
- Failed natural lever: asking again may not fix stale answers unless the elicitation is designed well.

## What We Add Beyond This Paper

Telephone focuses on correctness of the held answer after social transmission; calibration could be a future extension.

## Draft-Ready Use Sentence

> Calibration work shows that language models' confidence and correctness are sensitive to elicitation; Telephone therefore interprets post-transmission answers as operational held-belief probes rather than transparent access to internal certainty.

## Caveats

- Good methods caveat, but not necessary for core related work.
- Do not overuse if paper does not report confidence.

## Citation Decision

Decision: `cite`

Reason: Useful for measurement caution and possible limitations.
