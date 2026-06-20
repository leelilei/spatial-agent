---
telephone_index: 42
canonical: true
aliases: []
title: "MemoryBank"
category: 04_memory_state_agents
role: long-term memory for LLM companions
decision: cite
doi: 10.1609/aaai.v38i17.29946
venue: "Proceedings of the AAAI Conference on Artificial Intelligence"
year: 2024
source_quality: article
fulltext: assets/papers/fulltext/04_memory_state_agents/42_memorybank.fulltext.md
pdf: assets/papers/pdf/04_memory_state_agents/42_memorybank.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# MemoryBank

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

MemoryBank is directly relevant to the agent-state side of Telephone. It shows that long-term memory is an explicit design problem for LLM companions, so our observed failures can be framed as failures of social update integration, not just one-off generation errors.

## Core Question

The paper asks how LLM agents can maintain long-term memory over sustained interactions.

## Method / Evidence Base

It proposes a memory mechanism inspired by human memory patterns, including storage, retrieval, updating, and forgetting for companion-like agents.

## Core Claim / Result

The key lesson is that agent memory must be engineered; it is not automatically reliable just because a conversation contains the needed fact.

## Evidence We May Cite

- Long-term memory is a recognized missing component for LLM agents.
- Memory systems involve retrieval and updating, not just larger context windows.
- The paper supports treating held belief or state as a separate layer from conversational text.

## Telephone Bridge

- Speech vs belief: a fact in conversation may fail to become durable memory.
- Entrenchment / path dependence: memory update rules shape what persists.
- Failed natural lever: correction exposure alone may not rewrite prior state.

## What We Add Beyond This Paper

Telephone evaluates the behavioral consequence of memory/update limitations in a social factual-transmission task.

## Draft-Ready Use Sentence

> Agent-memory work such as MemoryBank treats long-term state as an explicit component of LLM agents; Telephone shows why that component matters by separating corrected speech from the factual answer agents later retain.

## Caveats

- Cite as memory/state background, not as evidence about misinformation.
- Avoid implementation detail unless discussing future mitigations.

## Citation Decision

Decision: `cite`

Reason: Strong state/memory support.
