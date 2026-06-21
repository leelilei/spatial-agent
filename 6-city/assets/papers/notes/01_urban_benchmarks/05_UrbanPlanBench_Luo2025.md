---
canonical: true
title: "UrbanPlanBench: A Comprehensive Urban Planning Benchmark for Evaluating Large Language Models"
category: 01_urban_benchmarks
role: "urban planning benchmark"
decision: cite
source: "https://arxiv.org/abs/2504.21027"
pdf: "assets/papers/pdf/01_urban_benchmarks/05_UrbanPlanBench_Luo2025.pdf"
fulltext: "assets/papers/fulltext/01_urban_benchmarks/05_UrbanPlanBench_Luo2025.fulltext.md"
quality_flags: []
note_status: first_pass
---

# UrbanPlanBench: A Comprehensive Urban Planning Benchmark for Evaluating Large Language Models

## Why This Paper Matters For 6-city

UrbanPlanBench gives us a contrast class: professional or planning-style urban judgment
is not the same as daily-life agent behavior in a city.

## Core Claim / Contribution

The paper evaluates LLMs on urban planning tasks through a dedicated benchmark.

## Evidence We May Cite

- Planning-oriented benchmark dimensions.
- Useful example of expert-domain urban evaluation.

## City Benchmark Bridge

- What it already measures: urban planning knowledge and reasoning.
- What it does not measure: micro-level residents, daily intentions, or socially situated movement.
- How it informs our SOTOPIA-style city benchmark: Helps keep 6-city scoped away from urban-planner benchmarks and toward resident/agent behavior benchmarks.

## What We Add Beyond This Paper

6-city can evaluate agent-level action under city affordances rather than professional
plan quality.

## Draft-Ready Use Sentence

> UrbanPlanBench evaluates planning judgment, whereas 6-city targets resident-like agents acting within a city environment.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `cite`

Reason: Useful contrast, not the central closest neighbor.

## Extracted Abstract Snapshot

The advent of Large Language Models (LLMs) holds promise for revolutionizing various fields traditionally dominated by human expertise. Urban planning, a professional discipline that fundamentally shapes our daily surroundings, is one such field heavily relying on multifaceted domain knowledge and experience of human experts. The extent to which LLMs can assist human practitioners in urban planning remains largely unexplored. In this paper, we introduce a comprehensive benchmark, UrbanPlanBench, tailored to evaluate the efficacy of LLMs in urban planning, which encompasses fundamental principles, professional knowledge, and management and regulations, aligning closely with the qualifications expected of human planners. Through extensive evaluation, we reveal a significant imbalance in the acquisition of planning knowledge among LLMs, with even the most proficient models falling short of meeting professional standards. For instance, we observe that 70% of LLMs achieve subpar performance in understanding planning regulations compared to other aspects.
