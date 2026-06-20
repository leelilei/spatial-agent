---
telephone_index: 24
canonical: true
aliases: []
title: "Faithful, Unfaithful or Ambiguous? Multi-Agent Debate with Initial Stance for Summary Evaluation"
category: 02_debate_consensus
role: multi-agent debate for summary faithfulness
decision: cite
doi: 10.18653/v1/2025.naacl-long.609
venue: "Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)"
year: 2025
source_quality: conference
fulltext: assets/papers/fulltext/02_debate_consensus/24_faithful-unfaithful-or-ambiguous-multi-agent-debate-with-initial-stance-for-summary-eval.fulltext.md
pdf: assets/papers/pdf/02_debate_consensus/24_faithful-unfaithful-or-ambiguous-multi-agent-debate-with-initial-stance-for-summary-eval.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# Faithful, Unfaithful or Ambiguous? Multi-Agent Debate with Initial Stance for Summary Evaluation

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

This is particularly interesting for Telephone because it assigns agents initial stances independent of their likely belief, forcing a separation between role/utterance and truth. That resonates with our speech-versus-belief split.

## Core Question

The paper asks how to evaluate summary faithfulness when LLM evaluators are fooled by fluent but erroneous summaries.

## Method / Evidence Base

It assigns multiple LLM agents initial stances and makes them justify those stances through debate before reaching an evaluation judgment.

## Core Claim / Result

The key contribution is a stance-driven debate method for faithfulness evaluation. Its design makes explicit that an agent's spoken position may be imposed for the debate rather than reflecting an internal belief.

## Evidence We May Cite

- Initial stance assignment can structure multi-agent debate for faithfulness evaluation.
- Faithfulness errors can be targeted through adversarial or role-diverse evaluator discussion.
- The paper gives a useful precedent for separating stated position from actual belief.

## Telephone Bridge

- Speech vs belief: imposed stances show why utterances cannot automatically be treated as beliefs.
- Measurement / rigor: Telephone similarly needs a separate held-answer probe.
- Fidelity vs reach: summary faithfulness and factual update fidelity are adjacent but distinct.

## What We Add Beyond This Paper

Telephone uses the separation empirically: after agents speak, we directly query what they hold about the current fact.

## Draft-Ready Use Sentence

> Stance-based multi-agent debate for summary faithfulness makes clear that an agent's uttered position can be a role in an interaction rather than a held belief; Telephone operationalizes this distinction by measuring both transmitted speech and later held answers.

## Caveats

- Cite for speech/belief distinction and evaluator faithfulness, not for social diffusion.
- Check exact dataset/task names before drafting specifics.

## Citation Decision

Decision: `cite`

Reason: Strong conceptual support for distinguishing stance, utterance, and belief.
