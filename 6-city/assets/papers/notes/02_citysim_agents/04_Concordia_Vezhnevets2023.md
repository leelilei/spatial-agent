---
canonical: true
title: "Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia"
category: 02_citysim_agents
role: "grounded generative-agent framework"
decision: must-cite
source: "https://arxiv.org/abs/2312.03664"
pdf: "assets/papers/pdf/02_citysim_agents/04_Concordia_Vezhnevets2023.pdf"
fulltext: "assets/papers/fulltext/02_citysim_agents/04_Concordia_Vezhnevets2023.fulltext.md"
quality_flags: ["abstract_may_include_layout_noise"]
note_status: first_pass
---

# Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia

## Why This Paper Matters For 6-city

Concordia is methodologically important because it treats agent actions as grounded in
physical, social, or digital spaces through a configurable environment/game-master
structure.

## Core Claim / Contribution

The framework supports generative agent-based modeling with actions grounded in explicit
spaces.

## Evidence We May Cite

- Grounding actions in spaces.
- Game-master/environment framing useful for separating agent intent from world truth.

## City Benchmark Bridge

- What it already measures: simulation behavior depending on configured scenarios and components.
- What it does not measure: a city-agent benchmark with fixed task families and scoring rubrics.
- How it informs our SOTOPIA-style city benchmark: Use its architecture idea: LLM chooses intent, environment validates actions, evaluator scores traces.

## What We Add Beyond This Paper

6-city can specialize this pattern into urban benchmark seeds and spatial counterfactual
tests.

## Draft-Ready Use Sentence

> Concordia motivates environment-grounded generative agents; 6-city instantiates that idea as a benchmark for city-space agency.

## Caveats / Follow-Up

- Extraction issues: abstract_may_include_layout_noise.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Core methodological foundation.

## Extracted Abstract Snapshot

level of analysis, and this has limited their usefulness. For instance, insights from behavioral economics and related fields which study how people actually make decisions are rarely combined with ideas from institutional and resource economics in the same model despite the fact that integrating these two bodies of knowledge is thought to be critical for building up the full picture of how social-ecological systems function, and how interventions may help or hinder their governance (Schill et al., 2019) Now, using generative AI1, it is possible to construct a new generation of ABMs where the agents not only have a richer set of cognitive operations available for adaptive decision making but also communicate with one another in natural language. Here we propose Generative Agent-Based Models (GABM)s, which are much more flexible and expressive than ABMs, and as a result can incorporate far more of the complexity of real social situations.
