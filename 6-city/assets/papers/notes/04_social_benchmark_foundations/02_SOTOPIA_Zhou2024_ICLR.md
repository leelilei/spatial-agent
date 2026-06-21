---
canonical: true
title: "SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents"
category: 04_social_benchmark_foundations
role: "interactive social-agent benchmark foundation"
decision: must-cite
source: "https://openreview.net/forum?id=mM7VurbA4r"
pdf: "assets/papers/pdf/04_social_benchmark_foundations/02_SOTOPIA_Zhou2024_ICLR.pdf"
fulltext: "assets/papers/fulltext/04_social_benchmark_foundations/02_SOTOPIA_Zhou2024_ICLR.fulltext.md"
quality_flags: []
note_status: first_pass
---

# SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents

## Why This Paper Matters For 6-city

SOTOPIA is the benchmark pattern we want to adapt: scenarios, private goals, characters,
interaction traces, and evaluator dimensions.

## Core Claim / Contribution

The paper proposes an interactive benchmark for social intelligence in language agents,
using goal-driven social scenarios and evaluators.

## Evidence We May Cite

- Scenario plus private-goal episode design.
- Evaluation dimensions for social interaction quality.

## City Benchmark Bridge

- What it already measures: social intelligence through interactive episodes and evaluator judgments.
- What it does not measure: a spatial/city benchmark, because its constraints are social rather than urban-geometric.
- How it informs our SOTOPIA-style city benchmark: Use its episode structure as the direct template for CityIntent.

## What We Add Beyond This Paper

6-city can add maps, POIs, travel costs, opening hours, spatial counterfactuals, and
trajectory validators to the SOTOPIA setup.

## Draft-Ready Use Sentence

> SOTOPIA provides the interactive evaluation pattern; 6-city spatializes that pattern into city-agent scenarios with verifiable movement and environmental constraints.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Core benchmark-method foundation.

## Extracted Abstract Snapshot

Humans are social beings; we pursue social goals in our daily interactions, which is a crucial aspect of social intelligence. Yet, AI systems’ abilities in this realm remain elusive. We present SOTOPIA, an open-ended environment to simulate complex social interactions between artificial agents and evaluate their social intelligence. In our environment, agents role-play and interact under a wide variety of scenarios; they coordinate, collaborate, exchange, and compete with each other to achieve complex social goals. We simulate the role-play interaction between LLM-based agents and humans within this task space and evaluate their performance with a holistic evaluation framework called SOTOPIA-EVAL. With SOTOPIA, we find significant differences between these models in terms of their social intelligence, and we identify a subset of SOTOPIA scenarios, SOTOPIAhard, that is generally challenging for all models. We find that on this subset, GPT4 achieves a significantly lower goal completion rate than humans and struggles to exhibit social commonsense reasoning and strategic communication skills.
