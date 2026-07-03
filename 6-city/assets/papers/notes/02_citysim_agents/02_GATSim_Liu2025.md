---
canonical: true
title: "GATSim: Urban Mobility Simulation with Generative Agents"
category: 02_citysim_agents
role: "generative-agent urban mobility simulation"
decision: must-cite
source: "https://arxiv.org/abs/2506.23306; published version https://doi.org/10.1016/j.simpat.2025.103234"
pdf: "assets/papers/pdf/02_citysim_agents/02_GATSim_Liu2025.pdf"
fulltext: "assets/papers/fulltext/02_citysim_agents/02_GATSim_Liu2025.fulltext.md"
quality_flags: []
note_status: reviewed
---

# GATSim: Urban Mobility Simulation with Generative Agents

## Why This Paper Matters For 6-city

GATSim directly connects generative agents with urban mobility simulation, which
overlaps with our concern about agents moving through a city under goals and
constraints.

## Core Claim / Contribution

The paper applies generative agents to urban mobility simulation.

## Evidence We May Cite

- Generative-agent approach to mobility behavior.
- Potential baseline for trajectory and movement realism.
- The ScienceDirect article `S1569190X25001698` is the published journal version,
  not an additional independent benchmark.

## City Benchmark Bridge

- What it already measures: mobility patterns and simulation outcomes.
- What it does not measure: SOTOPIA-style private intentions, social conflict, or controlled counterfactual city layouts.
- How it informs our SOTOPIA-style city benchmark: Use for the mobility branch of related work and for thinking about trajectory metrics.

## What We Add Beyond This Paper

6-city can add interaction-rich benchmark tasks where movement is only one component of
goal pursuit.

## Draft-Ready Use Sentence

> GATSim brings generative agents into urban mobility; 6-city treats mobility as part of a broader benchmark of situated city agency.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Closest mobility-specific neighbor.

## Extracted Abstract Snapshot

Traditional agent-based urban mobility simulations often rely on rigid rulebased systems that struggle to capture the complexity, adaptability, and behavioral diversity inherent in human travel decision making. Inspired by recent advancements in large language models and AI agent technologies, we introduce GATSim, a novel framework that leverages these advancements to simulate urban mobility using generative agents with dedicated cognitive structures. GATSim agents are characterized by diverse socioeconomic profiles, individual lifestyles, and evolving preferences shaped through psychologically informed memory systems and lifelong learning. The main contributions of this work are: 1) a comprehensive architecture that integrates urban mobility foundation model with agent cognitive systems and transport simulation environment; 2) a hierarchical memory designed for efficient retrieval of contextually relevant information, incorporating spatial and temporal associations; 3) planning and reactive mechanisms for modeling adaptive mobility behaviors which integrate a multi-scale reflection process to transform specific travel experiences into generalized behavioral insights.
