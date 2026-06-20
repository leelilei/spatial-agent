---
telephone_index: 4
canonical: true
aliases: []
title: "Debate Helps Supervise Unreliable Experts"
category: 02_debate_consensus
role: debate supervision / unreliable expert aggregation
decision: cite
doi: 
venue: "arXiv"
year: 2023
source_quality: preprint_or_unresolved
fulltext: assets/papers/fulltext/02_debate_consensus/04_debate-helps-supervise-unreliable-experts.fulltext.md
pdf: assets/papers/pdf/02_debate_consensus/04_debate-helps-supervise-unreliable-experts.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# Debate Helps Supervise Unreliable Experts

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

This paper is foundational for the optimistic case behind debate: when a judge cannot directly verify an answer, structured debate between agents may expose the truth. Telephone needs this backdrop because our results show a different social failure mode: communication can make truth appear in speech without making it durable in belief.

## Core Question

It asks how to supervise unreliable expert systems when the evaluator is weaker than the experts and cannot independently identify the correct answer.

## Method / Evidence Base

The paper formalizes debate as an oversight game and studies whether adversarial argument can make hidden truth easier for a weaker judge to recognize.

## Core Claim / Result

Debate is positioned as a mechanism for truth-revealing supervision under asymmetry. The important contrast for us is that debate assumes argument can surface latent correctness, whereas Telephone tests whether socially transmitted truth survives in agent memory or belief after exposure.

## Evidence We May Cite

- Debate is a major proposed mechanism for supervising stronger or unreliable models.
- The paper frames communication as a truth-extraction procedure under limited judge access.
- It helps justify why one might expect multi-agent interaction to improve factuality.

## Telephone Bridge

- Fidelity vs reach: debate optimizes final judged answer; Telephone measures persistence of the factual update.
- Speech vs belief: a judge may hear the right argument; Telephone asks whether agents later hold it.
- Failed natural lever: our findings qualify the broad hope that more structured interaction naturally repairs factual errors.

## What We Add Beyond This Paper

Telephone is not an oversight game. It contributes a social-transmission measurement where the truth is known to the experimenter and the failure appears as a gap between spoken correction and later held answer.

## Draft-Ready Use Sentence

> Debate has been proposed as a way to supervise unreliable experts by making truth legible to weaker judges; Telephone studies a complementary failure mode in which social communication surfaces correct statements without reliably installing the updated fact as later belief.

## Caveats

- Do not cite as empirical evidence about LLM social diffusion.
- Use mainly for motivation and contrast with debate-as-oversight.

## Citation Decision

Decision: `cite`

Reason: Important debate/oversight background and a useful contrast for our negative social-transmission result.
