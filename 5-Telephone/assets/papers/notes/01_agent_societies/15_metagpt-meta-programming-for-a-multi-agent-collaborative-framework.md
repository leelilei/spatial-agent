---
telephone_index: 15
canonical: true
aliases: []
title: "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework"
category: 01_agent_societies
role: role-structured multi-agent collaboration
decision: background
doi: 
venue: "arXiv"
year: 2023
source_quality: preprint_or_unresolved
fulltext: assets/papers/fulltext/01_agent_societies/15_metagpt-meta-programming-for-a-multi-agent-collaborative-framework.fulltext.md
pdf: assets/papers/pdf/01_agent_societies/15_metagpt-meta-programming-for-a-multi-agent-collaborative-framework.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

MetaGPT is useful because it explicitly names cascading hallucinations as a problem in chained multi-agent workflows. That is close to our worry that communication pipelines can transform or preserve wrong information despite role structure.

## Core Question

The paper addresses how to make multi-agent software-development workflows more reliable by imposing structured roles and standard operating procedures.

## Method / Evidence Base

It casts agents into specialized roles and uses meta-programming/SOP-style coordination to produce software artifacts.

## Core Claim / Result

For Telephone, the key insight is diagnostic: naive agent chaining can produce logic inconsistencies and cascading hallucinations, so multi-agent structure is not automatically reliability-preserving.

## Evidence We May Cite

- Multi-agent workflows can suffer from cascading hallucinations or inconsistencies.
- Structured roles and procedures are proposed as a mitigation.
- The paper supports our framing that communication architecture matters for reliability.

## Telephone Bridge

- Fidelity vs reach: successful workflow completion can hide degradation in transmitted content.
- Failed natural lever: role structure helps tasks, but Telephone tests whether natural social levers repair belief.
- Communication-time collapse analogy: cascades in workflows are an engineering cousin of social fidelity decay.

## What We Add Beyond This Paper

Telephone supplies controlled empirical evidence for one reliability failure: agents can circulate corrected facts without converging to the corrected held belief.

## Draft-Ready Use Sentence

> MetaGPT highlights cascading hallucinations in chained multi-agent workflows and proposes procedural structure as a remedy; Telephone studies a complementary social reliability failure in which factual updates degrade or fail to persist through communication itself.

## Caveats

- Use as background for multi-agent reliability, not as direct evidence of belief persistence.
- Keep citation light unless discussing engineering mitigations.

## Citation Decision

Decision: `background`

Reason: Good reliability framing, but secondary to direct factuality and misinformation papers.
