---
canonical: true
title: "CityGPT: Empowering Urban Spatial Cognition of Large Language Models"
category: 01_urban_benchmarks
role: "urban spatial cognition benchmark/model"
decision: cite
source: "https://arxiv.org/abs/2406.13948"
pdf: "assets/papers/pdf/01_urban_benchmarks/02_CityGPT_CityEval_Feng2024.pdf"
fulltext: "assets/papers/fulltext/01_urban_benchmarks/02_CityGPT_CityEval_Feng2024.fulltext.md"
quality_flags: []
note_status: first_pass
---

# CityGPT: Empowering Urban Spatial Cognition of Large Language Models

## Why This Paper Matters For 6-city

CityGPT/CityEval is useful because it frames urban spatial cognition as a capability
that can be benchmarked and improved, which is adjacent to our concern with spatially
situated agents.

## Core Claim / Contribution

The paper targets urban spatial cognition in LLMs and proposes evaluation/training
resources around city-space understanding.

## Evidence We May Cite

- Spatial cognition framing for urban LLMs.
- Evidence that city-space knowledge can be treated as a separable evaluation target.

## City Benchmark Bridge

- What it already measures: urban spatial cognition and city knowledge tasks.
- What it does not measure: autonomous daily-life rollouts with dynamic goals and social encounters.
- How it informs our SOTOPIA-style city benchmark: Helps separate our benchmark dimensions: spatial cognition is necessary, but not sufficient for believable city agency.

## What We Add Beyond This Paper

6-city can evaluate whether spatial cognition changes behavior under constraints, not
just whether a model answers spatial questions correctly.

## Draft-Ready Use Sentence

> CityGPT/CityEval treats urban spatial cognition as a measurable LLM capability; 6-city asks whether that capability supports coherent action in a simulated city.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `cite`

Reason: Relevant spatial benchmark, but less direct than CityBench or USTBench for our claim.

## Extracted Abstract Snapshot

Large language models(LLMs), with their powerful language generation and reasoning capabilities, have already achieved notable success in many domains, e.g., math and code generation. However, they often fall short when tackling real-life geospatial tasks within urban environments. This limitation stems from a lack of physical world knowledge and relevant data during training. To address this gap, we propose CityGPT, a systematic framework designed to enhance LLMs’ understanding of urban space and improve their ability to solve the related urban tasks by integrating a city-scale ‘world model’ into the model. Firstly, we construct a diverse instruction tuning dataset, CityInstruction, for injecting urban knowledge into LLMs and effectively boosting their spatial reasoning capabilities. Using a combination of CityInstruction and open source general instruction data, we introduce a novel and easy-to-use self-weighted fine-tuning method (SWFT) to train various LLMs (including ChatGLM3-6B, Llama3-8B, and Qwen2.5-7B) to enhance their urban spatial capabilities without compromising, or even improving, their general abilities.
