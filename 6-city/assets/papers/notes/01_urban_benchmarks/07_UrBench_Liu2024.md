---
canonical: true
title: "UrBench: A Comprehensive Benchmark for Evaluating Large Multimodal Models in Multi-View Urban Scenarios"
category: 01_urban_benchmarks
role: "multimodal urban perception benchmark"
decision: cite
source: "https://arxiv.org/abs/2408.17267"
pdf: "assets/papers/pdf/01_urban_benchmarks/07_UrBench_Liu2024.pdf"
fulltext: "assets/papers/fulltext/01_urban_benchmarks/07_UrBench_Liu2024.fulltext.md"
quality_flags: ["abstract_may_include_layout_noise"]
note_status: first_pass
---

# UrBench: A Comprehensive Benchmark for Evaluating Large Multimodal Models in Multi-View Urban Scenarios

## Why This Paper Matters For 6-city

UrBench matters if 6-city later adds visual or multi-view observations. It currently
helps identify the perception side of urban intelligence.

## Core Claim / Contribution

The paper builds a multimodal benchmark for evaluating urban scene understanding across
multi-view scenarios.

## Evidence We May Cite

- Multi-view urban scenario framing.
- Useful reference for perception-oriented urban benchmarks.

## City Benchmark Bridge

- What it already measures: urban multimodal perception and reasoning.
- What it does not measure: long-horizon autonomous agents with private goals and action traces.
- How it informs our SOTOPIA-style city benchmark: If we add visual observation, UrBench can inform perception tasks while SOTOPIA-style episodes handle agency.

## What We Add Beyond This Paper

6-city can connect perception to decisions and outcomes instead of evaluating perception
alone.

## Draft-Ready Use Sentence

> UrBench covers multimodal urban perception; 6-city would evaluate how such observations shape city-agent behavior.

## Caveats / Follow-Up

- Extraction issues: abstract_may_include_layout_noise.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `cite`

Reason: Relevant for the embodied/multimodal branch, with extraction caveat.

## Extracted Abstract Snapshot

Recent evaluations of Large Multimodal Models (LMMs) have explored their capabilities in various domains, with only few benchmarks specifically focusing on urban environments. Moreover, existing urban benchmarks have been limited to evaluating LMMs with basic region-level urban tasks under singular views, leading to incomplete evaluations of LMMs’ abilities in urban environments. To address these issues, we present UrBench, a comprehensive benchmark designed for evaluating LMMs in complex multi-view urban scenarios. UrBench contains 11.6K meticulously curated questions at both region-level and role-level that cover 4 task dimensions: Geo-Localization, Scene Reasoning, Scene Understanding, and Object Understanding, totaling 14 task types. In constructing UrBench, we utilize data from existing datasets and additionally collect data from 11 cities, creating new annotations using a cross-view detection-matching method. With these images and annotations, we then integrate LMM-based, rule-based, and human-based methods to construct largescale high-quality questions. Our evaluations on 21 LMMs show that current LMMs struggle in the urban environments in several aspects.
