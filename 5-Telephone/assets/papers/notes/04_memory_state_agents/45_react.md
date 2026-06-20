---
telephone_index: 45
canonical: true
aliases: []
title: "ReAct"
category: 04_memory_state_agents
role: reasoning-action interleaving
decision: background
doi: 
venue: "International Conference on Learning Representations (ICLR 2023)"
year: 2023
source_quality: conference
fulltext: assets/papers/fulltext/04_memory_state_agents/45_react.fulltext.md
pdf: assets/papers/pdf/04_memory_state_agents/45_react.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# ReAct

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

ReAct is background for agent architectures that interleave reasoning and action. It matters only indirectly: it reminds readers that agents produce traces and actions, but Telephone's key endpoint is later factual state.

## Core Question

The paper asks how to combine chain-of-thought-style reasoning with external actions in language agents.

## Method / Evidence Base

It prompts models to alternate reasoning traces and task-specific actions, enabling tool use and interactive decision making.

## Core Claim / Result

The relevant point is that agent behavior is multi-step and trace-based. However, ReAct is not about social transmission, memory update, or misinformation correction.

## Evidence We May Cite

- Reasoning and acting can be interleaved in LLM agents.
- Action traces make agent processes more observable in interactive tasks.
- The paper is a general agent-method background reference.

## Telephone Bridge

- Measurement / rigor: traces can be useful, but final held answers still need probing.
- Speech vs belief: a reasoning trace is not necessarily a durable belief.
- Not our claim: ReAct does not study multi-agent factual fidelity.

## What We Add Beyond This Paper

Telephone focuses on social communication among agents, not tool-augmented action loops.

## Draft-Ready Use Sentence

> ReAct-style agents interleave reasoning and action in interactive tasks; Telephone instead focuses on how factual information changes as agents communicate with one another and later answer from their own state.

## Caveats

- Background only.
- Likely omit from final related work if space is tight.

## Citation Decision

Decision: `background`

Reason: General agent background, not central.
