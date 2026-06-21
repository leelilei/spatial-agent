---
canonical: true
title: "TrajAgent: An LLM-Agent Framework for Trajectory Modeling via Large-and-Small Model Collaboration"
category: 02_citysim_agents
role: "trajectory modeling agent framework"
decision: cite
source: "https://arxiv.org/abs/2410.20445"
pdf: "assets/papers/pdf/02_citysim_agents/07_TrajAgent_Zhang2024.pdf"
fulltext: "assets/papers/fulltext/02_citysim_agents/07_TrajAgent_Zhang2024.fulltext.md"
quality_flags: []
note_status: first_pass
---

# TrajAgent: An LLM-Agent Framework for Trajectory Modeling via Large-and-Small Model Collaboration

## Why This Paper Matters For 6-city

TrajAgent is useful for trajectory modeling and may inform how we score or generate
movement traces in city episodes.

## Core Claim / Contribution

The paper proposes an LLM-agent framework for trajectory modeling using large-and-small
model collaboration.

## Evidence We May Cite

- Trajectory modeling approach.
- Potential design pattern for separating high-level reasoning from efficient low-level modeling.

## City Benchmark Bridge

- What it already measures: trajectory modeling quality.
- What it does not measure: social city-agent autonomy or private-goal benchmark scenarios.
- How it informs our SOTOPIA-style city benchmark: Use for trajectory metrics and possible model architecture baselines.

## What We Add Beyond This Paper

6-city can score trajectories in relation to goals, constraints, and replanning, not
only trajectory plausibility.

## Draft-Ready Use Sentence

> TrajAgent addresses trajectory modeling; 6-city evaluates trajectories as evidence of situated agency.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `cite`

Reason: Useful for movement/trace evaluation.

## Extracted Abstract Snapshot

Trajectory modeling, which includes research on trajectory data pattern mining and future prediction, has widespread applications in areas such as life services, urban transportation, and public administration. Numerous methods have been proposed to address specific problems within trajectory modeling. However, the heterogeneity of data and the diversity of trajectory tasks make effective and reliable trajectory modeling an important yet highly challenging endeavor, even for domain experts. In this paper, we propose TrajAgent, a agent framework powered by large language models (LLMs), designed to facilitate robust and efficient trajectory modeling through automation modeling. This framework leverages and optimizes diverse specialized models to address various trajectory modeling tasks across different datasets effectively. In TrajAgent, we first develop UniEnv, an execution environment with a unified data and model interface, to support the execution and training of various models. Building on UniEnv, we introduce an agentic workflow designed for automatic trajectory modeling across various trajectory tasks and data.
