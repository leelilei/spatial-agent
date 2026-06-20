---
telephone_index: 70
canonical: true
aliases: []
title: "How Bad is Training on Synthetic Data?"
category: 07_model_collapse_homogeneity
role: synthetic data collapse analysis
decision: cite
doi: 
venue: "arXiv"
year: 2024
source_quality: preprint_or_unresolved
fulltext: assets/papers/fulltext/07_model_collapse_homogeneity/70_how-bad-is-training-on-synthetic-data.fulltext.md
pdf: assets/papers/pdf/07_model_collapse_homogeneity/70_how-bad-is-training-on-synthetic-data.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# How Bad is Training on Synthetic Data?

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

This is a useful model-collapse/theory citation. It provides a more statistical framing of recursive synthetic-data training and clarifies when collapse can or cannot be avoided.

## Core Question

The paper asks how synthetic data affects language-model training under recursive training scenarios.

## Method / Evidence Base

It develops a statistical model of recursive training and supports conclusions with empirical validation.

## Core Claim / Result

The important finding is that training solely on synthetic data leads to collapse, while mixtures of real and synthetic data may avoid collapse below certain synthetic-data levels. For Telephone, this is an analogy, not the same mechanism.

## Evidence We May Cite

- Recursive use of synthetic data can make models forget tails of the original distribution.
- Fresh real data can mitigate collapse under some mixture conditions.
- The paper gives a precise way to discuss collapse as distributional degradation.

## Telephone Bridge

- Communication-time collapse analogy: Telephone is not training-time collapse, but both involve recursive reuse degrading fidelity/diversity.
- Fidelity vs reach: preserving the original or current signal requires fresh grounding.
- Failed natural lever: repeated internal/social reuse without grounding can degrade reliability.

## What We Add Beyond This Paper

Telephone contributes a communication-time analogue: factual updates can degrade through agent-to-agent transmission even without model retraining.

## Draft-Ready Use Sentence

> Synthetic-data theory shows that recursive training can collapse distributional fidelity unless refreshed with real data; Telephone studies a communication-time analogue in which factual updates require grounding to survive social reuse.

## Caveats

- Be explicit that this is an analogy, not our mechanism.
- Use alongside Curse of Recursion and Self-Consuming Generative Models.

## Citation Decision

Decision: `cite`

Reason: Good theoretical support for the collapse analogy.
