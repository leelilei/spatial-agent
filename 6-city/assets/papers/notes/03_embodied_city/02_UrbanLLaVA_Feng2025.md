---
canonical: true
title: "UrbanLLaVA: A Multi-modal Large Language Model for Urban Intelligence with Spatial Reasoning and Understanding"
category: 03_embodied_city
role: "urban multimodal model / spatial reasoning"
decision: cite
source: "https://arxiv.org/abs/2506.23219"
pdf: "assets/papers/pdf/03_embodied_city/02_UrbanLLaVA_Feng2025.pdf"
fulltext: "assets/papers/fulltext/03_embodied_city/02_UrbanLLaVA_Feng2025.fulltext.md"
quality_flags: []
note_status: first_pass
---

# UrbanLLaVA: A Multi-modal Large Language Model for Urban Intelligence with Spatial Reasoning and Understanding

## Why This Paper Matters For 6-city

UrbanLLaVA matters if our agents later receive image or street-view observations. It is
model-side rather than benchmark-episode-side related work.

## Core Claim / Contribution

The paper proposes a multimodal model for urban intelligence with spatial reasoning and
understanding.

## Evidence We May Cite

- Urban multimodal/spatial reasoning model.
- Useful reference for visual observation extensions.

## City Benchmark Bridge

- What it already measures: urban visual/spatial understanding tasks.
- What it does not measure: autonomous goal pursuit in a simulated city world.
- How it informs our SOTOPIA-style city benchmark: Use as model-side context for a visual version of 6-city.

## What We Add Beyond This Paper

6-city can evaluate how urban multimodal understanding affects decisions and
trajectories.

## Draft-Ready Use Sentence

> UrbanLLaVA advances urban multimodal understanding; 6-city would evaluate whether such understanding supports coherent city-agent behavior.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `cite`

Reason: Relevant for future multimodal extension.

## Extracted Abstract Snapshot

Urban research involves a wide range of scenarios and Satellite Image Street View Image tasks that require the understanding of multi-modal data. Current methods often focus on specific data types and lack a unified framework in urban field for processing them comprehensively. The recent success of multi-modal large language models (MLLMs) presents a promising opportunity to overcome this limitation. In this paper, we introduce UrbanGeLoLSpaaVtiAal, Daatamulti-modal largeTrlaajencgtourya gDeatamodel designed to process these four types of data simultaneously and achieve strong performance across diverse urban tasks compared with general MLLMs. In UrbanLLaVA, we first curate a diverse urban instruction dataset encompassing both singlemodal and cross-modal urban data, spanning from location view to global view of urban environment. Additionally, we propose a multi-stage training framework that decouples spatial reasoning enhancement from domain knowledge learning, thereby improving the compatibility and downstream performance of UrbanLLaVA across diverse urban tasks.
