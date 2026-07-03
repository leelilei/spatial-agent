---
canonical: true
title: "DeliveryBench: Can Agents Earn Profit in Real World?"
category: 08_route_planning_agents
role: "constraint-dense long-horizon embodied city benchmark"
decision: must-cite
source: "https://arxiv.org/abs/2512.19234"
pdf: "assets/papers/pdf/08_route_planning_agents/02_DeliveryBench_Mao2025.pdf"
fulltext: "assets/papers/fulltext/08_route_planning_agents/02_DeliveryBench_Mao2025.fulltext.md"
quality_flags: []
note_status: reviewed
---

# DeliveryBench

## Why This Paper Matters For 6-city

DeliveryBench is a strong direct neighbor for long-horizon urban execution. Its delivery agents must earn profit while obeying deadlines, transport costs, battery constraints, and social interactions in procedurally generated 3D cities.

## Core Claim / Contribution

The benchmark evaluates constraint-aware embodied planning over two-hour episodes and nine city configurations, with complete action trajectories and a human baseline.

## Evidence We May Cite

- Seven VLMs are tested: GPT-5, GPT-4o, Claude-3.7-Sonnet, Gemini-2.5-Flash, Qwen2.5-VL-72B/32B, and Llama-3.2-90B-Vision.
- Net profit is supported by diagnostics for planning, constraint compliance, and interaction behavior.
- Agents remain far below humans, are short-sighted, and frequently violate commonsense constraints.

## City Benchmark Bridge

- What it already measures: long-horizon city-scale task execution under economic, temporal, physical, and social constraints.
- What it does not measure: general resident intentions, paired feasible/infeasible variants, false completion claims, or the plan-to-trace plausibility gap across urban-agent frameworks.
- How it informs CityAgency: it narrows the novelty claim; long-horizon constrained city execution is no longer unique.

## What We Add Beyond This Paper

CityAgency is domain-general across daily urban intentions, weakly embodied and resettable, explicitly separates language plausibility from state-valid completion, and supports adapters for multiple agent architectures.

## Draft-Ready Use Sentence

> DeliveryBench reveals severe long-horizon constraint failures in an embodied courier domain; CityAgency generalizes the diagnostic question to everyday urban intentions and explicit plan-to-trace gaps.

## Caveats / Follow-Up

- Treat this as a direct competitor, not merely an embodied-agent reference.
- Compare its action logging and human protocol before freezing CityAgency's full table.

## Citation Decision

Decision: `must-cite`

Reason: Direct city execution benchmark with overlapping time, budget, and interaction constraints.

## Extracted Abstract Snapshot

DeliveryBench tests delivery agents in nine 3D cities and finds large human-agent gaps, short-horizon planning, and frequent violation of basic constraints.
