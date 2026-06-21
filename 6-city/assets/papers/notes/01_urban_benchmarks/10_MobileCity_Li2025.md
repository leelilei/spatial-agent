---
canonical: true
title: "MobileCity: An Efficient Framework for Large-Scale Urban Behavior Simulation"
category: 01_urban_benchmarks
role: "efficient urban behavior simulation framework"
decision: cite
source: "https://arxiv.org/abs/2504.16946"
pdf: "assets/papers/pdf/01_urban_benchmarks/10_MobileCity_Li2025.pdf"
fulltext: "assets/papers/fulltext/01_urban_benchmarks/10_MobileCity_Li2025.fulltext.md"
quality_flags: []
note_status: first_pass
---

# MobileCity: An Efficient Framework for Large-Scale Urban Behavior Simulation

## Why This Paper Matters For 6-city

MobileCity is useful for thinking about computational efficiency and large-scale urban
behavior simulation, especially if our benchmark later scales beyond small scenarios.

## Core Claim / Contribution

The paper proposes an efficient framework for large-scale urban behavior simulation.

## Evidence We May Cite

- Efficiency/scaling design choices for urban behavior simulation.
- Potential contrast with high-control benchmark episodes.

## City Benchmark Bridge

- What it already measures: large-scale urban behavior simulation performance and outcomes.
- What it does not measure: a SOTOPIA-style benchmark for private goals and controlled social-spatial constraints.
- How it informs our SOTOPIA-style city benchmark: Useful later if we turn the benchmark into a scalable harness.

## What We Add Beyond This Paper

6-city can begin with rigorous small-scale evaluation before optimizing for massive
scale.

## Draft-Ready Use Sentence

> MobileCity represents the scalable-simulation branch, while 6-city emphasizes verifiable micro-city benchmark episodes.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `cite`

Reason: Relevant scaling reference.

## Extracted Abstract Snapshot

Generative agents offer promising capabilities for simulating realistic urban behaviors. However, existing methods often rely on static profiles, oversimplified behavioral logic, and synchronous inference pipelines that hinder scalability. We present MobileCity, a lightweight generative-agent framework for city-scale simulation powered by cognitively-grounded generative agents. Each agent acts based on its needs, habits, and obligations, evolving over time. Agents are initialized from survey-based demographic data and navigate a realistic multimodal transportation network spanning multiple types of vehicles. To achieve scalability, we introduce asynchronous batched LLM inference during action selection and a low-token communication mechanism. Experiments with 4,000 agents demonstrate that MobileCity generates more human-like urban dynamics than baselines while maintaining high computational efficiency. Our code is publicly available at https://github.com/Tony-Yip/MobileCity.
