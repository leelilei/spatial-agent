---
canonical: true
title: "Generative Agents: Interactive Simulacra of Human Behavior"
category: 04_social_benchmark_foundations
role: "generative-agent foundation"
decision: must-cite
source: "https://arxiv.org/abs/2304.03442"
pdf: "assets/papers/pdf/04_social_benchmark_foundations/01_Generative_Agents_Park2023.pdf"
fulltext: "assets/papers/fulltext/04_social_benchmark_foundations/01_Generative_Agents_Park2023.fulltext.md"
quality_flags: ["abstract_may_include_layout_noise"]
note_status: first_pass
---

# Generative Agents: Interactive Simulacra of Human Behavior

## Why This Paper Matters For 6-city

Generative Agents is the foundation for believable LLM agents with memory, reflection,
planning, and daily behavior in a simulated town.

## Core Claim / Contribution

The paper shows that LLM agents with memory, reflection, and planning can produce
believable interactive behavior in a sandbox environment.

## Evidence We May Cite

- Memory-reflection-planning architecture.
- Small-town simulation as the ancestor of city-agent demos.

## City Benchmark Bridge

- What it already measures: believability and behavioral coherence in an interactive agent sandbox.
- What it does not measure: a benchmark with controlled city layouts, private goal scoring, counterfactual perturbations, and standardized evaluation across models.
- How it informs our SOTOPIA-style city benchmark: Use as the historical foundation, then argue that the next step is benchmark-grade evaluation of spatial agency.

## What We Add Beyond This Paper

6-city can turn the sandbox intuition into resettable scenarios with measurable
autonomy, feasibility, and adaptation.

## Draft-Ready Use Sentence

> Generative Agents established the memory-planning architecture for believable agents; 6-city asks how such agents should be evaluated when they inhabit a city environment.

## Caveats / Follow-Up

- Extraction issues: abstract_may_include_layout_noise.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Foundational prior for all generative-agent city work.

## Extracted Abstract Snapshot

Believable proxies of human behavior can empower interactive applications ranging from immersive environments to rehearsal spaces for interpersonal communication to prototyping tools. In this paper, we introduce generative agents: computational software agents that simulate believable human behavior. Generative agents wake up, cook breakfast, and head to work; artists paint, while authors write; they form opinions, notice each other, and initiate conversations; they remember and reflect on days past as they plan the next day. To enable generative agents, we describe an architecture that extends a large language model to store a complete record of the agent’s experiences using natural language, synthesize those memories over time into higher-level reflections, and retrieve them dynamically to plan behavior. We instantiate generative agents to populate an interactive sandbox environment inspired by The Sims, where end users can interact with a small town of twenty-five agents using natural language. In an evaluation, these generative agents produce believable individual and emergent social behaviors.
