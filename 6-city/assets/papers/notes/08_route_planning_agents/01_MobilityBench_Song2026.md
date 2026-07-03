---
canonical: true
title: "MobilityBench: A Benchmark for Evaluating Route-Planning Agents in Real-World Mobility Scenarios"
category: 08_route_planning_agents
role: "closest deterministic route-planning benchmark"
decision: must-cite
source: "https://arxiv.org/abs/2602.22638"
pdf: "assets/papers/pdf/08_route_planning_agents/01_MobilityBench_Song2026.pdf"
fulltext: "assets/papers/fulltext/08_route_planning_agents/01_MobilityBench_Song2026.fulltext.md"
quality_flags: []
note_status: reviewed
---

# MobilityBench

## Why This Paper Matters For 6-city

MobilityBench is the closest route-execution reference because it combines real user mobility requests, tool-using agents, outcome validation, and a deterministic API-replay sandbox.

## Core Claim / Contribution

The benchmark contains 100,000 anonymized Amap route queries from more than 350 cities in 22 countries and evaluates outcome validity plus instruction understanding, planning, tool use, and efficiency under reproducible API responses.

## Evidence We May Cite

- Tests Qwen3, DeepSeek R1/V3.2, GPT-4.1/5.2, Claude 4.5, and Gemini 3 model families as route-agent backbones.
- Basic retrieval and ordinary route planning are stronger than preference-constrained route planning.
- API replay is a useful precedent for freezing external urban services while preserving realistic tool traces.

## City Benchmark Bridge

- What it already measures: single-request route correctness, preference satisfaction, tool behavior, and efficiency.
- What it does not measure: a resident's multi-goal episode, persistent world state, social interruption, resource evolution, or recovery after execution-time disruption.
- How it informs CityAgency: borrow deterministic replay and process diagnostics; retain the full-episode, state-transition focus.

## What We Add Beyond This Paper

CityAgency evaluates an evolving urban episode in which movement is only one action type and completion requires evidence accumulated across time, resources, POIs, and other agents.

## Draft-Ready Use Sentence

> MobilityBench makes route-agent evaluation reproducible through deterministic API replay; CityAgency extends executable validation from a route request to a stateful urban episode.

## Caveats / Follow-Up

- The 100,000-query benchmark is much larger than CityAgency's initial scenario set.
- Distinguish real-query coverage from CityAgency's causal paired-scenario design.

## Citation Decision

Decision: `must-cite`

Reason: Direct benchmark neighbor for deterministic mobility-tool evaluation.

## Extracted Abstract Snapshot

MobilityBench evaluates route-planning agents on large-scale real queries in a deterministic API-replay sandbox and identifies preference-constrained planning as the main weakness.
