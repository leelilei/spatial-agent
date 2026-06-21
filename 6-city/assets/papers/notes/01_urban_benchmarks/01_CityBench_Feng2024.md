---
canonical: true
title: "CityBench: Evaluating the Capabilities of Large Language Models for Urban Tasks"
category: 01_urban_benchmarks
role: "broad urban-task benchmark"
decision: must-cite
source: "https://arxiv.org/abs/2406.13945"
pdf: "assets/papers/pdf/01_urban_benchmarks/01_CityBench_Feng2024.pdf"
fulltext: "assets/papers/fulltext/01_urban_benchmarks/01_CityBench_Feng2024.fulltext.md"
quality_flags: []
note_status: first_pass
---

# CityBench: Evaluating the Capabilities of Large Language Models for Urban Tasks

## Why This Paper Matters For 6-city

CityBench is the broadest baseline for evaluating LLM capability on urban tasks. It
helps us define what is already covered by current urban benchmarks before claiming a
gap for city-agent behavior.

## Core Claim / Contribution

The paper constructs a benchmark over urban tasks to test whether LLMs can handle city-
relevant knowledge, reasoning, and planning-style questions.

## Evidence We May Cite

- Broad task taxonomy for urban intelligence evaluation.
- Useful contrast between urban knowledge/reasoning benchmarks and interactive city-agent benchmarks.

## City Benchmark Bridge

- What it already measures: urban task competence, usually through static or question-answer style evaluation.
- What it does not measure: long-horizon autonomous movement, private intentions, social interaction, or environment perturbation under resettable scenarios.
- How it informs our SOTOPIA-style city benchmark: Use it as the umbrella related-work anchor, then position 6-city as a behavioral benchmark rather than another urban QA benchmark.

## What We Add Beyond This Paper

6-city can add controlled agent rollouts, private goals, spatial feasibility checks, and
trajectory-level scoring.

## Draft-Ready Use Sentence

> CityBench establishes that LLM urban intelligence can be evaluated systematically, but our focus shifts from static urban task ability to situated, intention-driven city behavior.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Central reference for the benchmark landscape we are entering.

## Extracted Abstract Snapshot

As large language models (LLMs) continue to advance and gain widespread use, establishing systematic and reliable evaluation methodologies for LLMs and vision-language models (VLMs) has become essential to ensure their real-world effectiveness and reliability. There have been some early explorations about the usability of LLMs for limited urban tasks, but a systematic and scalable evaluation benchmark is still lacking. The challenge in constructing a systematic evaluation benchmark for urban research lies in the diversity of urban data, the complexity of application scenarios and the highly dynamic nature of the urban environment. In this paper, we design CityBench, an interactive simulator based evaluation platform, as the first systematic benchmark for evaluating the capabilities of LLMs for diverse tasks in urban research. First, we build CityData to integrate the diverse urban data and CitySimu to simulate fine-grained urban dynamics. Based on CityData and CitySimu, we design 8 representative urban tasks in 2 categories of perception-understanding and decision-making as the CityBench.
