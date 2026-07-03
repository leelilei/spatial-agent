---
canonical: true
title: "LiveCultureBench: a Multi-Agent, Multi-Cultural Benchmark for Large Language Models in Dynamic Social Simulations"
category: 04_social_benchmark_foundations
role: "closest small-city social-agent benchmark"
decision: must-cite
source: "https://arxiv.org/abs/2603.01952"
pdf: "assets/papers/pdf/04_social_benchmark_foundations/07_LiveCultureBench_Pham2026.pdf"
fulltext: "assets/papers/fulltext/04_social_benchmark_foundations/07_LiveCultureBench_Pham2026.fulltext.md"
quality_flags: []
note_status: reviewed
---

# LiveCultureBench

## Why This Paper Matters For 6-city

This is CityAgency's closest newly identified competitor. It already places an LLM-controlled resident in a small-city location graph, assigns a daily goal, supplies other residents as social context, and evaluates both task completion and socio-cultural norm adherence.

## Core Claim / Contribution

LiveCultureBench evaluates whether LLM agents can pursue dynamic daily goals across cultural profiles without violating human-annotated social norms, while also measuring when an LLM verifier is reliable enough for automated evaluation.

## Evidence We May Cite

- A graph-based town with time, locations, target and supporting residents, daily goals, subtasks, and cultural norms.
- Gemini 2.5 Pro/Flash, Qwen 3, Llama 3, and Ministral 3 Reasoning families are compared across British, German, and Chinese profiles.
- Human-annotated samples are used to calibrate verifier uncertainty; goal completion changes less than norm adherence under harder cultural conditions.

## City Benchmark Bridge

- What it already measures: goal completion, cultural norm violations, task-norm trade-offs, cross-cultural robustness, and verifier reliability.
- What it does not measure: environment-owned physical action validity, typed state transitions, resource accounting, impossible-route evidence, or continuous trace feasibility under disruptions.
- How it informs CityAgency: it invalidates any novelty claim based only on a small city, private/daily goals, supporting agents, or an LLM verifier.

## What We Add Beyond This Paper

CityAgency must center deterministic execution evidence: every move, entry, purchase, meeting, time advance, and completion claim is checked against authoritative world state. Its primary object is the plan-to-trace gap, not cultural appropriateness.

## Draft-Ready Use Sentence

> LiveCultureBench evaluates goal pursuit and cultural norm adherence in a graph-based town, whereas CityAgency asks whether a plausible urban plan survives deterministic spatial, temporal, and resource execution.

## Caveats / Follow-Up

- The paper is a 2026 preprint and should be rechecked for later versions.
- Its verifier and human-oversight design should be compared directly with CityAgency's soft-score protocol.

## Citation Decision

Decision: `must-cite`

Reason: Closest benchmark competitor and a direct constraint on novelty claims.

## Extracted Abstract Snapshot

The benchmark embeds diverse synthetic residents in a small-city graph and evaluates a target resident's daily goal completion, socio-cultural norm adherence, and LLM-verifier uncertainty.
