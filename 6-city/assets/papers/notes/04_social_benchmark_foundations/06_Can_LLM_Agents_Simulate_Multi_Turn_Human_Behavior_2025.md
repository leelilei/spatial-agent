---
canonical: true
title: "Can LLM Agents Simulate Multi-Turn Human Behavior? Evidence from Real Online Customer Behavior Data"
category: 04_social_benchmark_foundations
role: "empirical step-by-step behavior benchmark"
decision: must-cite
source: "https://arxiv.org/abs/2503.20749"
pdf: "assets/papers/pdf/04_social_benchmark_foundations/06_Can_LLM_Agents_Simulate_Multi_Turn_Human_Behavior_2025.pdf"
fulltext: "assets/papers/fulltext/04_social_benchmark_foundations/06_Can_LLM_Agents_Simulate_Multi_Turn_Human_Behavior_2025.fulltext.md"
quality_flags: []
note_status: first_pass
---

# Can LLM Agents Simulate Multi-Turn Human Behavior? Evidence from Real Online Customer Behavior Data

## Why This Paper Matters For 6-city

The paper directly challenges qualitative believability as evidence of human-like
behavior and evaluates step-by-step actions against large-scale observed human traces.

## Core Claim / Contribution

Using real online shopping sessions, the paper finds a substantial gap between plausible
generated behavior and accurate next-action simulation.

## Evidence We May Cite

- Action-level comparison against 31,865 real multi-turn sessions.
- Separation of qualitative believability from quantitative behavioral accuracy.

## City Benchmark Bridge

- What it already measures: next-action accuracy and final-outcome prediction against observed human traces.
- What it does not measure: physical mobility, city constraints, or open-ended goal adaptation in an urban environment.
- How it informs our SOTOPIA-style city benchmark: Keep trace-level behavioral validity distinct from judge-rated plausibility and add human data when available.

## What We Add Beyond This Paper

CityAgency can diagnose impossible or incoherent urban traces even before a large human-
trajectory comparison dataset is available.

## Draft-Ready Use Sentence

> Empirical multi-turn studies show that believable narratives need not reproduce human action sequences; CityAgency tests the same gap in urban execution.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Strong empirical support for the plausible-plan versus credible-trace story.

## Extracted Abstract Snapshot

Recent research shows that LLM Agents can generate “believable” human behaviors via prompt-only methods, and such agents have been increasingly adopted in downstream applications. However, existing evaluation of these agents only focuses on qualitative believability (whether human raters think they are accurate), leaving open questions of whether LLM agents can accurately generate step-by-step actions mimicking a particular human’s behavior in a multi-turn interaction task. In this work, we take shopping as a case study and present the first large-scale quantitative evaluation of state-of-the-art LLMs’ ability to accurately simulate human behavior. Using real-world data from 31,865 online shopping sessions containing 230,965 user actions, our evaluation reveals that prompt-based LLMs (DeepSeek-R1, Llama, Claude) achieve only 11.86% accuracy in generating human actions, highlighting a substantial gap in actual behavioral accuracy. Through experiments, we also showcase that strategies as simple as fine-tuning LLMs on real human click-through data augmented with synthesized reasoning traces can greatly enhance models’ performance.
