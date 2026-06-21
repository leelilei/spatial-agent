---
canonical: true
title: "USTBench: Benchmarking and Dissecting Spatiotemporal Reasoning of LLMs as Urban Agents"
category: 01_urban_benchmarks
role: "urban-agent spatiotemporal benchmark"
decision: must-cite
source: "https://arxiv.org/abs/2505.17572"
pdf: "assets/papers/pdf/01_urban_benchmarks/04_USTBench_Liu2025.pdf"
fulltext: "assets/papers/fulltext/01_urban_benchmarks/04_USTBench_Liu2025.fulltext.md"
quality_flags: []
note_status: first_pass
---

# USTBench: Benchmarking and Dissecting Spatiotemporal Reasoning of LLMs as Urban Agents

## Why This Paper Matters For 6-city

USTBench is one of the closest benchmark references because it explicitly talks about
LLMs as urban agents and spatiotemporal reasoning in urban contexts.

## Core Claim / Contribution

The paper benchmarks and analyzes spatiotemporal reasoning abilities of LLMs in urban-
agent tasks.

## Evidence We May Cite

- Direct use of the urban-agent framing.
- Evaluation categories for spatiotemporal reasoning that overlap with city-agent decisions.

## City Benchmark Bridge

- What it already measures: urban-agent reasoning tasks, especially spatiotemporal reasoning.
- What it does not measure: SOTOPIA-style private-goal episodes with social and spatial constraints.
- How it informs our SOTOPIA-style city benchmark: Use as a direct closest-neighbor benchmark and clarify whether 6-city is measuring behavior over episodes rather than single reasoning answers.

## What We Add Beyond This Paper

6-city can add private intentions, environmental perturbations, social relationships,
and trace-level scoring.

## Draft-Ready Use Sentence

> USTBench brings LLM evaluation into the urban-agent setting; 6-city extends this line toward interactive episodes with verifiable city-state transitions.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Closest benchmark neighbor for our direction.

## Extracted Abstract Snapshot

Large language models (LLMs) have shown emerging potential in spatiotemporal reasoning, making them promising candidates for building urban agents that support diverse urban downstream applications. Despite these benefits, existing studies primarily focus on evaluating urban LLM agent on outcome-level metrics (e.g., prediction accuracy, traffic efficiency), offering limited insight into their underlying reasoning processes. As a result, the strengths and limitations of urban LLM agents in spatiotemporal reasoning remain poorly understood. To this end, we introduce USTBench, the first benchmark to evaluate LLMs’ spatiotemporal reasoning abilities as urban agents across four decomposed dimensions: spatiotemporal understanding, forecasting, planning, and reflection with feedback. Specifically, USTBench supports five diverse urban decision-making and four spatiotemporal prediction tasks, all running within our constructed interactive city environment UAgentEnv. The benchmark includes 62,466 structured QA pairs for process-level evaluation and standardized end-to-end task assessments, enabling fine-grained diagnostics and broad task-level comparison across diverse urban scenarios.
