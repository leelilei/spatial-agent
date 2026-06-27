---
canonical: true
title: "ChinaTravel: An Open-Ended Travel Planning Benchmark with Compositional Constraint Validation for Language Agents"
category: 06_agent_execution_benchmarks
role: "compositional travel-plan feasibility benchmark"
decision: must-cite
source: "https://arxiv.org/abs/2412.13682"
pdf: "assets/papers/pdf/06_agent_execution_benchmarks/01_ChinaTravel_Shao2024.pdf"
fulltext: "assets/papers/fulltext/06_agent_execution_benchmarks/01_ChinaTravel_Shao2024.fulltext.md"
quality_flags: []
note_status: first_pass
---

# ChinaTravel: An Open-Ended Travel Planning Benchmark with Compositional Constraint Validation for Language Agents

## Why This Paper Matters For 6-city

ChinaTravel is a close feasibility neighbor because it translates open-ended travel
requirements into compositional constraints that can be checked automatically.

## Core Claim / Contribution

The benchmark combines a multi-day travel sandbox, a constraint DSL, human-authored
requirements, and programmatic feasibility and preference validation.

## Evidence We May Cite

- Domain-specific language for compositional constraint validation.
- Open-ended multi-POI plans with explicit and implicit human requirements.

## City Benchmark Bridge

- What it already measures: plan feasibility, constraint satisfaction, and preference quality.
- What it does not measure: stepwise execution in a changing city, social encounters, or stateful replanning after disturbances.
- How it informs our SOTOPIA-style city benchmark: Represent CityAgency goals and hard constraints as executable predicates instead of relying on free-form judge scores.

## What We Add Beyond This Paper

CityAgency can move from validating a proposed itinerary to validating every action and
resulting world state during execution.

## Draft-Ready Use Sentence

> ChinaTravel demonstrates compositional validation of open-ended travel plans; CityAgency extends validation from plans to stateful urban execution traces.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Closest planning-feasibility precedent for deterministic urban validators.

## Extracted Abstract Snapshot

Travel planning stands out among real-world applications of Language Agents because it couples significant practical demand with a rigorous constraint-satisfaction challenge. However, existing benchmarks primarily operate on a slot-filling paradigm, restricting agents to synthetic queries with pre-defined constraint menus, which fails to capture the open-ended nature of natural language interaction, where user requirements are compositional, diverse, and often implicitly expressed. To address this gap, we introduce ChinaTravel, with four key contributions: 1) a practical sandbox aligned with the multi-day, multi-POI travel planning, 2) a compositionally generalizable domain-specific language (DSL) for scalable evaluation, covering feasibility, constraint satisfaction, and preference comparison 3) an openended dataset that integrates diverse travel requirements and implicit intent from 1154 human participants, and 4) fine-grained analysis reveal the potential of neurosymbolic agents in travel planning, achieving a 37.0% constraint satisfaction rate on human queries, a 10× improvement over purely neural models, yet highlighting significant challenges in compositional generalization.
