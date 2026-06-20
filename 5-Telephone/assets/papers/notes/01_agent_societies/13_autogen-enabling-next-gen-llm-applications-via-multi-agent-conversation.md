---
telephone_index: 13
canonical: true
aliases: []
title: "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
category: 01_agent_societies
role: multi-agent conversation framework / setting
decision: cite
doi: 
venue: "arXiv"
year: 2023
source_quality: preprint_or_unresolved
fulltext: assets/papers/fulltext/01_agent_societies/13_autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation.fulltext.md
pdf: assets/papers/pdf/01_agent_societies/13_autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

AutoGen is a systems reference showing that multi-agent conversation has become an engineering pattern for LLM applications. It supports the practical relevance of studying what happens when agents exchange information through dialogue.

## Core Question

The paper addresses how to build flexible applications from conversable agents that combine LLMs, tools, code, and human input.

## Method / Evidence Base

It provides an open-source framework where agents exchange messages and developers specify interaction patterns for collaborative task solving.

## Core Claim / Result

The key point for Telephone is infrastructural: multi-agent conversations are now easy to construct and deploy, so their information-fidelity risks matter.

## Evidence We May Cite

- Conversable agents are a general programming abstraction for LLM applications.
- Multi-agent message exchange can coordinate tools, humans, and models.
- The framework makes social information flow a normal software primitive.

## Telephone Bridge

- Fidelity vs reach: AutoGen makes message passing easy; Telephone asks whether message passing preserves truth.
- Failed natural lever: framework-level coordination does not by itself guarantee belief repair.
- Measurement / rigor: deployed systems need outcome probes beyond successful conversation completion.

## What We Add Beyond This Paper

Telephone contributes behavioral evidence about a risk inside the communication primitive: agents can participate in plausible conversations while failing to retain the corrected factual state.

## Draft-Ready Use Sentence

> Frameworks such as AutoGen make multi-agent conversation a practical software primitive; Telephone examines a risk of that primitive, namely whether socially exchanged factual updates remain faithful as held beliefs.

## Caveats

- Use for systems motivation rather than empirical claims.
- Avoid making AutoGen sound like a social-science simulation paper.

## Citation Decision

Decision: `cite`

Reason: Strong background for why multi-agent conversational systems are practically important.
