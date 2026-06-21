---
canonical: true
title: "EmbodiedCity: A Benchmark Platform for Embodied Agent in Real-world City Environment"
category: 03_embodied_city
role: "embodied city benchmark platform"
decision: must-cite
source: "https://arxiv.org/abs/2410.09604"
pdf: "assets/papers/pdf/03_embodied_city/01_EmbodiedCity_Zhou2024.pdf"
fulltext: "assets/papers/fulltext/03_embodied_city/01_EmbodiedCity_Zhou2024.fulltext.md"
quality_flags: []
note_status: first_pass
---

# EmbodiedCity: A Benchmark Platform for Embodied Agent in Real-world City Environment

## Why This Paper Matters For 6-city

EmbodiedCity is a central reference for city-scale embodied agents and real-world city
environment benchmarks.

## Core Claim / Contribution

The paper presents a benchmark platform for embodied agents in real-world city
environments.

## Evidence We May Cite

- Embodied city benchmark platform.
- Real-world city environment grounding.

## City Benchmark Bridge

- What it already measures: embodied agent performance in city environments, likely navigation and perception-heavy tasks.
- What it does not measure: social/private-goal daily-life episodes in a controllable micro-city.
- How it informs our SOTOPIA-style city benchmark: Use as a must-cite for embodied city benchmark work and as a boundary for our cheaper graph/grid benchmark version.

## What We Add Beyond This Paper

6-city can begin with weak embodiment and verifiable social-spatial scenarios before
moving to visual embodiment.

## Draft-Ready Use Sentence

> EmbodiedCity grounds agents in real city environments; 6-city explores a lighter but more controllable benchmark for city agency.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Core embodied-city benchmark reference.

## Extracted Abstract Snapshot

Embodied artificial intelligence (EmbodiedAI) emphasizes the role of an agent’s body in generating human-like behaviors. The recent efforts on EmbodiedAI pay a lot of attention to building up machine learning models to possess perceiving, planning, and acting abilities, thereby enabling real-time interaction with the world. However, most works focus on bounded indoor environments, such as navigation in a room or manipulating a device, with limited exploration of embodying the agents in open-world scenarios. That is, embodied intelligence in the open and outdoor environment is less explored, for which one potential reason is the lack of high-quality simulators, benchmarks, and datasets. To address it, in this paper, we construct a benchmark platform for embodied intelligence evaluation in realworld city environments. Specifically, we first construct a highly realistic 3D simulation environment based on the real buildings, roads, and other elements in a real city. In this environment, we combine historically collected data and simulation algorithms to conduct simulations of pedestrian and vehicle flows with high fidelity.
