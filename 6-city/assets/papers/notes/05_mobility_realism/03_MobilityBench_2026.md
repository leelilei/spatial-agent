---
canonical: true
title: "MobilityBench: A Benchmark for Evaluating Route-Planning Agents in Real-World Mobility Scenarios"
category: 05_mobility_realism
role: "real-world route-planning agent benchmark; deterministic API-replay sandbox; outcome-validity metric"
decision: must-cite
source: "https://arxiv.org/abs/2602.22638"
pdf: "assets/papers/pdf/05_mobility_realism/03_MobilityBench_2026.pdf"
fulltext: "assets/papers/fulltext/05_mobility_realism/03_MobilityBench_2026.fulltext.md"
quality_flags: [abstract_may_include_layout_noise]
note_status: first_pass
---

# MobilityBench: A Benchmark for Evaluating Route-Planning Agents in Real-World Mobility Scenarios

## Why This Paper Matters For 6-city

MobilityBench (Amap/Alibaba + CAS) is the closest neighbor to CityAgency's movement-validation layer:
real user route queries, a deterministic API-replay sandbox to kill environment variance, and an
evaluation protocol centered on **outcome validity**. Its headline finding — models fail specifically
on Preference-Constrained Route Planning — is directly relevant to CityAgency's constrained,
private-goal routing. The key boundary: MobilityBench scores single route-planning requests;
CityAgency scores a full multi-step episode with hidden intentions and disruptions.

## Core Claim / Contribution

A scalable, reproducible benchmark of anonymized real Amap route queries across many cities, with a
deterministic API-replay sandbox and a multi-dimensional protocol (outcome validity + instruction
understanding, planning, tool use, efficiency). Finding: agents are competent on basic retrieval and
plain route planning but struggle badly with preference-constrained planning.

## Evidence We May Cite

- Deterministic API-replay sandbox as a design precedent for removing live-service nondeterminism (reproducibility).
- Outcome-validity-centered evaluation rather than trajectory plausibility.
- Preference-constrained routing (e.g. "avoid highways, stop by a convenience store en route") is the systematic weak spot.

## City Benchmark Bridge

- What it already measures: single-request route feasibility and preference satisfaction against replayed real map services.
- What it does not measure: multi-step private-intention episodes, mid-trip disruption recovery, social co-presence, or continuous whole-day trace validity.
- How it informs our SOTOPIA-style city benchmark: reuse the deterministic-replay + outcome-validity discipline; extend from one request to a full episode with hidden goals and injected disruptions.

## What We Add Beyond This Paper

CityAgency turns route planning into one edge of a longer intention-driven episode and verifies the
executed trace (entry/purchase/service/interaction), not just whether a returned route satisfies a
single request.

## Draft-Ready Use Sentence

> Route-planning benchmarks such as MobilityBench show that preference-constrained routing is the weak
> spot of LLM agents even for single requests; CityAgency embeds such routing inside a multi-step,
> disruption-prone episode and verifies the realized trace rather than the returned plan.

## Caveats / Follow-Up

- Extraction issues: multi-author header and abstract are de-spaced; use PDF for author list and exact metric names.
- Need to verify: number of cities/queries (index says 100K × 350+ cities — confirm against the PDF) and the precise outcome-validity definition.

## Citation Decision

Decision: `must-cite`

Reason: Closest real-world movement-validation neighbor; shares the deterministic-sandbox + outcome-validity
philosophy and defines the "single request vs full episode" boundary CityAgency claims.

## Extracted Abstract Snapshot

MobilityBench: scalable benchmark from anonymized real Amap route queries across many cities.
Deterministic API-replay sandbox removes live-service variance. Multi-dimensional protocol centered on
outcome validity (+ instruction understanding, planning, tool use, efficiency). Models competent on basic
retrieval/route planning but struggle with Preference-Constrained Route Planning. Data + toolkit released.
