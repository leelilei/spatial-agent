---
telephone_index: 46
canonical: true
aliases: []
title: "Voyager"
category: 04_memory_state_agents
role: lifelong embodied agent with skill memory
decision: cite
doi: 
venue: "Transactions on Machine Learning Research"
year: 2023
source_quality: journal
fulltext: assets/papers/fulltext/04_memory_state_agents/46_voyager.fulltext.md
pdf: assets/papers/pdf/04_memory_state_agents/46_voyager.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# Voyager

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

Voyager is relevant as a strong example of long-term agent learning through an external skill library. It supports the claim that durable state is engineered, accumulated, and retrieved, not magically guaranteed by prior interaction.

## Core Question

The paper asks how an LLM-powered embodied agent can learn continually in an open-ended environment.

## Method / Evidence Base

It combines automatic curriculum generation, a growing skill library of executable code, and iterative prompting for Minecraft exploration.

## Core Claim / Result

The key lesson is that successful long-horizon agents rely on explicit accumulation and reuse of learned skills. Telephone's stale beliefs can be framed as a missing or failed update to such durable state.

## Evidence We May Cite

- Long-horizon agents need externalized memory or skill stores.
- Retrieval and reuse of past experience are central to lifelong agent behavior.
- The paper helps motivate stateful agents as a setting where factual updates matter.

## Telephone Bridge

- Entrenchment / path dependence: durable stores shape future behavior.
- Speech vs belief: a correction must be written into and retrieved from state to matter later.
- Failed natural lever: communication without memory integration is weak.

## What We Add Beyond This Paper

Telephone supplies a compact factual-update test for whether agent state tracks socially transmitted truth.

## Draft-Ready Use Sentence

> Voyager demonstrates how long-horizon agents depend on accumulated, retrievable state; Telephone asks whether socially delivered factual corrections enter the kind of durable state that later answers draw on.

## Caveats

- Use as memory/agent background, not misinformation evidence.
- No need to detail Minecraft unless discussing lifelong agents.

## Citation Decision

Decision: `cite`

Reason: Good durable-state background.
