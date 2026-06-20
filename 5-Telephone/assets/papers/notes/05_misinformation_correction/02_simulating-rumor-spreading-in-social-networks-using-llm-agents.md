---
telephone_index: 2
canonical: true
aliases: []
title: "Simulating Rumor Spreading in Social Networks using LLM Agents"
category: 05_misinformation_correction
role: LLM-agent rumor simulation / reach baseline
decision: cite
doi: 
venue: "arXiv"
year: 2025
source_quality: preprint_or_unresolved_layout_caution
fulltext: assets/papers/fulltext/05_misinformation_correction/02_simulating-rumor-spreading-in-social-networks-using-llm-agents.fulltext.md
pdf: assets/papers/pdf/05_misinformation_correction/02_simulating-rumor-spreading-in-social-networks-using-llm-agents.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# Simulating Rumor Spreading in Social Networks using LLM Agents

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

This is a close synthetic-society neighbor because it uses LLM personas and explicit network structures to simulate rumor diffusion. For Telephone, it is useful precisely because it studies spread, while our paper asks a stricter question: after a corrected factual update circulates, what do agents later say and hold?

## Core Question

The paper asks whether LLM agents can simulate rumor propagation across social networks, including how agent traits and network topology shape adoption and retransmission.

## Method / Evidence Base

It builds a simulation framework with multiple LLM-based agent types and several network structures, then observes rumor diffusion dynamics under those synthetic social conditions.

## Core Claim / Result

The paper treats LLM personas as user-level approximations for rumor behavior and emphasizes that propagation depends on both agent characteristics and network structure. Its main endpoint is diffusion behavior, not durable belief-state fidelity after truth changes.

## Evidence We May Cite

- LLM agents can be placed into social-network simulations to study rumor spread at the node and network level.
- Network topology and persona design are central variables in synthetic misinformation simulations.
- The paper motivates why reach and retransmission should not be confused with whether agents retain the corrected state.

## Telephone Bridge

- Fidelity vs reach: it operationalizes reach; Telephone adds ground-truthed update fidelity.
- Speech vs belief: rumor transmission is visible behavior; Telephone separates visible utterance from later held answer.
- Failed natural lever: if structure changes propagation, our null results on breadth/connectivity become sharper.

## What We Add Beyond This Paper

Telephone adds controlled truth changes, repeated transmission rounds, and a final held-belief probe. That lets us distinguish rumor spread from whether the current fact is installed in agent state.

## Draft-Ready Use Sentence

> LLM-agent rumor simulations show that synthetic personas and network topology can reproduce plausible diffusion dynamics; Telephone extends this line by measuring whether the currently true version survives social transmission as held belief, not merely whether messages spread.

## Caveats

- Use as a close-neighbor simulation paper, not as evidence for speech-belief dissociation.
- Verify any numeric result directly from the PDF before using it in the draft.

## Citation Decision

Decision: `cite`

Reason: Close neighbor for LLM-agent misinformation diffusion, but its endpoint is propagation rather than belief fidelity.
