---
telephone_index: 43
canonical: true
aliases: []
title: "MemGPT"
category: 04_memory_state_agents
role: virtual-context memory management
decision: cite
doi: 
venue: "International Conference on Learning Representations (ICLR 2024)"
year: 2024
source_quality: conference
fulltext: assets/papers/fulltext/04_memory_state_agents/43_memgpt.fulltext.md
pdf: assets/papers/pdf/04_memory_state_agents/43_memgpt.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# MemGPT

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

MemGPT is important architecture background because it frames context management as virtual memory. Telephone can use it to say that agent state is not the same as the visible conversation window.

## Core Question

The paper addresses the limited context windows of LLMs and the need to manage information across long interactions and documents.

## Method / Evidence Base

It introduces virtual context management inspired by operating-system memory, paging information between working context and longer-term stores.

## Core Claim / Result

The central relevance is that memory and context are managed systems. If updates are not selected, retrieved, or written correctly, later answers can be stale despite prior exposure.

## Evidence We May Cite

- Context limitations motivate explicit memory management for LLM agents.
- Information can move between working context and external or long-term memory.
- The paper supports the idea that exposure does not equal retention.

## Telephone Bridge

- Speech vs belief: visible dialogue is only one layer of agent state.
- Entrenchment / path dependence: what gets written or retrieved determines later behavior.
- Measurement / rigor: Telephone measures the outcome of this state-management problem behaviorally.

## What We Add Beyond This Paper

Telephone is not proposing a memory architecture; it reveals a social factual-update failure that memory architectures might need to address.

## Draft-Ready Use Sentence

> MemGPT frames long interaction as a memory-management problem; Telephone provides a social factuality stress test showing that information present in conversation may not be the information an agent later retrieves as true.

## Caveats

- Use in memory/state paragraph.
- Do not imply Telephone used MemGPT unless it did.

## Citation Decision

Decision: `cite`

Reason: Core context/memory architecture background.
