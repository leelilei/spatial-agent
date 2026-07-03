---
canonical: true
title: "GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies"
category: 07_large_scale_urban_sim
role: "empirically grounded large-scale urban simulation"
decision: cite
source: "https://arxiv.org/abs/2606.27650"
pdf: "assets/papers/pdf/07_large_scale_urban_sim/01_GenWorld_Li2026.pdf"
fulltext: "assets/papers/fulltext/07_large_scale_urban_sim/01_GenWorld_Li2026.fulltext.md"
quality_flags: []
note_status: reviewed
---

# GenWorld

## Why This Paper Matters For 6-city

GenWorld shows how to ground and scale an urban LLM-agent simulation without making online LLM calls for every resident at every step. It is the clearest contrast between CityAgency's diagnostic micro-benchmark and a city-wide simulation infrastructure.

## Core Claim / Contribution

The system constructs 196,608 synthetic residents for Higashihiroshima from census, building, POI, road, and mobility evidence, then compiles repeated teacher-model decisions into reusable offline policies for scalable rollouts.

## Evidence We May Cite

- Multi-scale empirical grounding from city demographics down to building-level assignments.
- Offline compilation separates expensive LLM decision generation from population-scale execution.
- Weekday, weekend, and perturbation rollouts support aggregate mobility and response analysis.

## City Benchmark Bridge

- What it already measures: grounded population construction, city-wide activity patterns, and scalable perturbation response.
- What it does not measure: whether a live individual agent preserves a private intention through a formally validated multi-step trace.
- How it informs CityAgency: use it to define the scale-agency boundary and future micro-to-macro connection.

## What We Add Beyond This Paper

CityAgency sacrifices population scale to isolate causal failures in online decision making, execution validity, goal persistence, and replanning.

## Draft-Ready Use Sentence

> GenWorld demonstrates empirically grounded urban rollouts at population scale; CityAgency complements this by diagnosing the executable agency of individual online agents.

## Caveats / Follow-Up

- Do not compare aggregate realism scores directly with CityAgency's episode-level metrics.
- Track whether the authors later publish cross-city validation or framework adapters.

## Citation Decision

Decision: `cite`

Reason: Strong scale-and-grounding reference, but not a direct benchmark competitor.

## Extracted Abstract Snapshot

GenWorld builds a grounded synthetic population of 196,608 residents and uses offline LLM-policy compilation to make city-scale simulation computationally practical.
