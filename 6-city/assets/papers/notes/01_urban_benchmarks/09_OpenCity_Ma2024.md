---
canonical: true
title: "OpenCity: A Scalable Platform to Simulate Urban Activities with Massive LLM Agents"
category: 01_urban_benchmarks
role: "large-scale urban activity simulation platform"
decision: cite
source: "https://arxiv.org/abs/2410.21286"
pdf: "assets/papers/pdf/01_urban_benchmarks/09_OpenCity_Ma2024.pdf"
fulltext: "assets/papers/fulltext/01_urban_benchmarks/09_OpenCity_Ma2024.fulltext.md"
quality_flags: []
note_status: first_pass
---

# OpenCity: A Scalable Platform to Simulate Urban Activities with Massive LLM Agents

## Why This Paper Matters For 6-city

OpenCity is important because it treats LLM agents at urban scale. It is a
systems/platform neighbor to our smaller benchmark idea.

## Core Claim / Contribution

The paper proposes a scalable platform for simulating urban activities with many LLM
agents.

## Evidence We May Cite

- Large-scale urban agent simulation platform.
- System reference for scaling beyond controlled micro-city evaluation.

## City Benchmark Bridge

- What it already measures: urban activities at platform scale, depending on the simulation setup.
- What it does not measure: controlled benchmark episodes and falsifiable scoring as the primary target.
- How it informs our SOTOPIA-style city benchmark: Use as a systems neighbor and explain why 6-city starts smaller for controllability and verification.

## What We Add Beyond This Paper

6-city can trade scale for high-control scenario packages and benchmark-grade
evaluation.

## Draft-Ready Use Sentence

> OpenCity shows the feasibility of large-scale LLM urban activity simulation; 6-city aims for smaller but more controlled evaluation episodes.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `cite`

Reason: Important related platform, not necessarily the benchmark template.

## Extracted Abstract Snapshot

Agent-based models (ABMs) have long been employed to explore how individual behaviors aggregate into complex societal phenomena in urban space. Unlike black-box predictive models, ABMs excel at explaining the micro-macro linkages that drive such emergent behaviors. The recent rise of Large Language Models (LLMs) has led to the development of LLM agents capable of simulating urban activities with unprecedented realism. However, the extreme high computational cost of LLMs presents significant challenges for scaling up the simulations of LLM agents. To address this problem, we propose OpenCity, a scalable simulation platform optimized for both system and prompt efficiencies. Specifically, we propose a LLM request scheduler to reduce communication overhead by parallelizing requests through IO multiplexing. Besides, we deisgn a “group-and-distill” prompt optimization strategy minimizes redundancy by clustering agents with similar static attributes. Through experiments on six global cities, OpenCity achieves a 600-fold acceleration in simulation time per agent, a 70% reduction in LLM requests, and a 50% reduction in token usage.
