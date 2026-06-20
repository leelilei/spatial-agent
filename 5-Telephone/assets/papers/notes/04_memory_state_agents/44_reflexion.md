---
telephone_index: 44
canonical: true
aliases: []
title: "Reflexion"
category: 04_memory_state_agents
role: reflection as verbal reinforcement / memory
decision: cite
doi: 10.52202/075280-0377
venue: "Neural Information Processing Systems"
year: 2023
source_quality: conference
fulltext: assets/papers/fulltext/04_memory_state_agents/44_reflexion.fulltext.md
pdf: assets/papers/pdf/04_memory_state_agents/44_reflexion.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# Reflexion

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

Reflexion is useful because it shows agents can use verbal memory from prior trials to improve future behavior. Telephone contrasts with this optimistic memory-learning picture: social feedback or correction does not necessarily update held factual state.

## Core Question

The paper asks how language agents can learn from trial-and-error without gradient updates or reinforcement-learning training.

## Method / Evidence Base

It stores verbal reflections in episodic memory and retrieves them to guide later decisions across tasks.

## Core Claim / Result

The key point is that explicit memory/reflection can improve agents when the loop is designed for learning. Telephone shows that ordinary social communication is a much weaker update mechanism.

## Evidence We May Cite

- Verbal feedback can be stored and reused as episodic memory.
- Agent improvement can occur through memory-mediated reflection without fine-tuning.
- The paper offers a plausible mitigation direction for stale belief.

## Telephone Bridge

- Failed natural lever: reflection helps when engineered; our natural social levers may fail without such mechanisms.
- Speech vs belief: reflecting on feedback is different from merely hearing it.
- Entrenchment / path dependence: stored reflections can redirect future behavior, suggesting why memory-write policies matter.

## What We Add Beyond This Paper

Telephone contributes evidence that factual corrections need not become effective memory unless the system is designed to integrate them.

## Draft-Ready Use Sentence

> Reflexion shows that verbal feedback can improve agents when stored as episodic memory; Telephone suggests that ordinary social exposure to correction is not enough to guarantee such memory-level update.

## Caveats

- Good future-work or mitigation citation.
- Do not cite as direct evidence for social correction failure.

## Citation Decision

Decision: `cite`

Reason: Useful memory-learning contrast and mitigation reference.
