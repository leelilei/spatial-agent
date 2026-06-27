---
canonical: true
title: "AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios"
category: 04_social_benchmark_foundations
role: "diverse interactive social-agent benchmark"
decision: must-cite
source: "https://arxiv.org/abs/2410.19346"
pdf: "assets/papers/pdf/04_social_benchmark_foundations/03_AgentSense_2024.pdf"
fulltext: "assets/papers/fulltext/04_social_benchmark_foundations/03_AgentSense_2024.fulltext.md"
quality_flags: []
note_status: first_pass
---

# AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios

## Why This Paper Matters For 6-city

AgentSense is a close social-benchmark neighbor because it tests goal pursuit and
implicit reasoning across 1,225 interactive scenarios rather than relying on a small set
of hand-written conversations.

## Core Claim / Contribution

The paper constructs diverse multi-turn social scenarios from scripts and evaluates
language agents on explicit goal completion and implicit social reasoning.

## Evidence We May Cite

- Large, theory-grounded interactive scenario construction pipeline.
- Separate attention to goal completion, private information, and implicit reasoning.

## City Benchmark Bridge

- What it already measures: social goal achievement and implicit reasoning in multi-turn interactions.
- What it does not measure: spatially grounded execution, travel feasibility, city-state transitions, or continuous mobility traces.
- How it informs our SOTOPIA-style city benchmark: Reuse its scenario-diversity discipline and separate observable goal completion from latent social reasoning.

## What We Add Beyond This Paper

CityAgency can embed similarly diverse private goals in a city world where actions also
have spatial, temporal, and resource consequences.

## Draft-Ready Use Sentence

> AgentSense broadens social-agent evaluation across diverse interactive scenarios; CityAgency adds executable urban state and trajectory validation to that episode structure.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Close benchmark reference for private goals, scenario diversity, and social reasoning.

## Extracted Abstract Snapshot

Large language models (LLMs) are increasingly leveraged to empower autonomous agents to simulate human beings in various fields of behavioral research. However, evaluating their capacity to navigate complex social interactions remains a challenge. Previous studies face limitations due to insufficient scenario diversity, complexity, and a single-perspective focus. To this end, we introduce AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios. Drawing on Dramaturgical Theory, AgentSense employs a bottom-up approach to create 1,225 diverse social scenarios constructed from extensive scripts. We evaluate LLM-driven agents through multi-turn interactions, emphasizing both goal completion and implicit reasoning. We analyze goals using ERG theory and conduct comprehensive experiments. Our findings highlight that LLMs struggle with goals in complex social scenarios, especially highlevel growth needs, and even GPT-4o requires improvement in private information reasoning. Code and data are available at https: //github.com/ljcleo/agent_sense.
