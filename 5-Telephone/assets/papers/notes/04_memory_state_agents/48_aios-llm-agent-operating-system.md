---
telephone_index: 48
canonical: true
aliases: []
title: "AIOS: LLM Agent Operating System"
category: 04_memory_state_agents
role: LLM agent operating system
decision: background
doi: 
venue: "arXiv"
year: 2024
source_quality: preprint_or_unresolved
fulltext: assets/papers/fulltext/04_memory_state_agents/48_aios-llm-agent-operating-system.fulltext.md
pdf: assets/papers/pdf/04_memory_state_agents/48_aios-llm-agent-operating-system.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# AIOS: LLM Agent Operating System

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

AIOS is infrastructure background. It is about resource scheduling and operating-system support for LLM agents, so it is only indirectly relevant to our social-fidelity claim.

## Core Question

The paper addresses deployment challenges for LLM agents, including resource management, scheduling, and safe coordination of tools/models.

## Method / Evidence Base

It proposes an agent operating system abstraction to manage concurrent agent operations and resource use.

## Core Claim / Result

The relevant point is that agent systems are complex enough to need operating-system-like support. Telephone's contribution is not infrastructure but a reliability phenomenon that such systems may need to monitor.

## Evidence We May Cite

- LLM-agent deployment raises coordination and resource-management challenges.
- Agent infrastructure is becoming a research area in its own right.
- Reliability tests can complement infrastructure-level robustness.

## Telephone Bridge

- Measurement / rigor: operating systems can schedule agents, but they do not guarantee factual belief fidelity.
- Fidelity vs reach: system throughput is separate from truth preservation.
- Not our claim: no direct social-transmission mechanism.

## What We Add Beyond This Paper

Telephone could become one behavioral test for agent platforms, but it is not an OS proposal.

## Draft-Ready Use Sentence

> Agent operating-system work focuses on managing resources and coordination in LLM-agent deployments; Telephone highlights a behavioral reliability issue such infrastructure alone may not solve: preserving updated factual state through communication.

## Caveats

- Background only.
- Probably omit from concise related work.

## Citation Decision

Decision: `background`

Reason: Infrastructure context with weak direct connection.
