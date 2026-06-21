---
canonical: true
title: "CitySim: Modeling Urban Behaviors and City Dynamics with Large-Scale LLM-Driven Agent Simulation"
category: 02_citysim_agents
role: "closest CitySim agent simulation neighbor"
decision: must-cite
source: "https://arxiv.org/abs/2506.21805"
pdf: "assets/papers/pdf/02_citysim_agents/01_CitySim_Wang2025.pdf"
fulltext: "assets/papers/fulltext/02_citysim_agents/01_CitySim_Wang2025.fulltext.md"
quality_flags: []
note_status: first_pass
---

# CitySim: Modeling Urban Behaviors and City Dynamics with Large-Scale LLM-Driven Agent Simulation

## Why This Paper Matters For 6-city

CitySim is the closest named reference to the direction we are discussing. It directly
uses LLM-driven agents for urban behavior and city dynamics.

## Core Claim / Contribution

The paper models urban behavior and city dynamics through large-scale LLM-driven agent
simulation.

## Evidence We May Cite

- LLM-driven city agent simulation design.
- Reference point for needs, schedules, mobility, and city dynamics.

## City Benchmark Bridge

- What it already measures: urban behavior and aggregate city dynamics in simulation.
- What it does not measure: benchmark-grade controlled evaluation of agent autonomy, private intentions, and spatial sensitivity as the central product.
- How it informs our SOTOPIA-style city benchmark: Use as closest simulation neighbor; position 6-city as a benchmark harness rather than a city simulator demo.

## What We Add Beyond This Paper

6-city can focus on resettable scenarios, counterfactual layout changes, private goals,
and transparent scoring.

## Draft-Ready Use Sentence

> CitySim demonstrates large-scale LLM-driven urban simulation; 6-city asks how such agents should be benchmarked under controlled spatial and social conditions.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Closest direct neighbor and required related work.

## Extracted Abstract Snapshot

Modeling human behavior in urban environments is fundamental for social science, behavioral studies, and urban planning. Prior work often rely on rigid, hand-crafted rules, limiting their ability to simulate nuanced intentions, plans, and adaptive behaviors. Addressing these challenges, we envision an urban simulator (CitySim), capitalizing on breakthroughs in human-level intelligence exhibited by large language models. In CitySim, agents generate realistic daily schedules using a recursive value-driven approach that balances mandatory activities, personal habits, and situational factors. To enable long-term, lifelike simulations, we endow agents with beliefs, long-term goals, and spatial memory for navigation. CitySim exhibits closer alignment with real humans than prior work, both at micro and macro levels. Additionally, we conduct insightful experiments by modeling tens of thousands of agents and evaluating their collective behaviors under various real-world scenarios, including estimating crowd density, predicting place popularity, and assessing well-being. Our results highlight CitySim as a scalable, flexible testbed for understanding and forecasting urban phenomena.
