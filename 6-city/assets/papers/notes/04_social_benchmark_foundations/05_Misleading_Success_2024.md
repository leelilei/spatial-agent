---
canonical: true
title: "Is This the Real Life? Is This Just Fantasy? The Misleading Success of Simulating Social Interactions With LLMs"
category: 04_social_benchmark_foundations
role: "information-asymmetry realism critique"
decision: must-cite
source: "https://arxiv.org/abs/2403.05020"
pdf: "assets/papers/pdf/04_social_benchmark_foundations/05_Misleading_Success_2024.pdf"
fulltext: "assets/papers/fulltext/04_social_benchmark_foundations/05_Misleading_Success_2024.fulltext.md"
quality_flags: []
note_status: first_pass
---

# Is This the Real Life? Is This Just Fantasy? The Misleading Success of Simulating Social Interactions With LLMs

## Why This Paper Matters For 6-city

This paper is a methodological warning for CityAgency: agents can look successful when
the simulator grants them omniscient information that real people would not possess.

## Core Claim / Contribution

The paper compares omniscient and non-omniscient social simulations and finds that
apparent agent success falls under realistic information asymmetry.

## Evidence We May Cite

- Controlled comparison of omniscient and information-asymmetric settings.
- Demonstration that simulator information design can inflate social-agent performance.

## City Benchmark Bridge

- What it already measures: social interaction performance under different information-access assumptions.
- What it does not measure: physical observability, map knowledge, local sensing, or trace feasibility in a city.
- How it informs our SOTOPIA-style city benchmark: Give each city agent an explicit observation boundary and keep hidden world state outside the prompt.

## What We Add Beyond This Paper

CityAgency can test whether plans remain valid when agents must discover closures,
delays, and other agents' intentions through permitted observations.

## Draft-Ready Use Sentence

> Information-asymmetry studies warn that omniscient simulation can produce misleading success; CityAgency therefore separates agent observations from authoritative world state.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Central validity reference for avoiding an unrealistically omniscient city benchmark.

## Extracted Abstract Snapshot

Recent advances in large language models (LLM) have enabled richer social simulations, allowing for the study of various social phenomena. However, most recent work has used a more omniscient perspective on these simulations (e.g., single LLM to generate all interlocutors), which is fundamentally at odds with the non-omniscient, information asymmetric interactions that involve humans and AI agents in the real world. To examine these differences, we develop an evaluation framework to simulate social interactions with LLMs in various settings (omniscient, non-omniscient). Our experiments show that LLMs perform better in unrealistic, omniscient simulation settings but struggle in ones that more accurately reflect real-world conditions with information asymmetry. Our findings indicate that addressing information asymmetry remains a fundamental challenge for LLM-based agents.
