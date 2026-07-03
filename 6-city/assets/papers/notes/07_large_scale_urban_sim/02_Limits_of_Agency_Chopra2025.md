---
canonical: true
title: "On the Limits of Agency in Agent-Based Models"
category: 07_large_scale_urban_sim
role: "agency-versus-scale framing and LLM archetypes"
decision: cite
source: "https://arxiv.org/abs/2409.10568"
pdf: "assets/papers/pdf/07_large_scale_urban_sim/02_Limits_of_Agency_Chopra2025.pdf"
fulltext: "assets/papers/fulltext/07_large_scale_urban_sim/02_Limits_of_Agency_Chopra2025.fulltext.md"
quality_flags: []
note_status: reviewed
---

# On the Limits of Agency in Agent-Based Models

## Why This Paper Matters For 6-city

The paper explicitly frames the trade-off between population scale and individual behavioral expressiveness. That gives CityAgency a principled reason to work at micro scale rather than presenting small scale as an implementation limitation.

## Core Claim / Contribution

LLM archetypes group demographically similar agents, query an LLM at the archetype level, and distribute sampled behavior to individuals, enabling an 8.4-million-agent New York City pandemic and labor-market simulation.

## Evidence We May Cite

- Comparison of heuristic, archetype-based, and fully adaptive LLM-agent designs.
- AgentTorch implementation at New York City population scale.
- Counterfactual health and economic analysis illustrates the utility and loss of individuality introduced by aggregation.

## City Benchmark Bridge

- What it already measures: scalable adaptive behavior and macro counterfactual outcomes.
- What it does not measure: high-resolution intention persistence and environment-valid individual traces.
- How it informs CityAgency: CityAgency occupies the high-agency, low-scale end and should state this design choice explicitly.

## What We Add Beyond This Paper

CityAgency operationalizes individual agency as observable, falsifiable execution behavior instead of treating agency mainly as model expressiveness.

## Draft-Ready Use Sentence

> LLM archetypes expose a scale-expressiveness trade-off in urban ABMs; CityAgency deliberately fixes scale to make individual agency measurable.

## Caveats / Follow-Up

- The term agency has a different operational meaning here; avoid implying the paper measures CityAgency's construct.
- Macro policy utility still depends on empirical mechanism validation.

## Citation Decision

Decision: `cite`

Reason: Important conceptual boundary for the benchmark scope.

## Extracted Abstract Snapshot

The paper proposes LLM archetypes to bridge adaptive behavior and population-scale ABMs, demonstrated with 8.4 million simulated New York City residents.
