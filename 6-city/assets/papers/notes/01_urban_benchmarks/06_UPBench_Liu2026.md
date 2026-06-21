---
canonical: true
title: "Can AI Reason Like an Urban Planner? Benchmarking Large Language Models Against Professional Judgment"
category: 01_urban_benchmarks
role: "urban planner judgment benchmark"
decision: cite
source: "https://arxiv.org/abs/2606.11678"
pdf: "assets/papers/pdf/01_urban_benchmarks/06_UPBench_Liu2026.pdf"
fulltext: "assets/papers/fulltext/01_urban_benchmarks/06_UPBench_Liu2026.fulltext.md"
quality_flags: ["abstract_may_include_layout_noise"]
note_status: first_pass
---

# Can AI Reason Like an Urban Planner? Benchmarking Large Language Models Against Professional Judgment

## Why This Paper Matters For 6-city

UPBench is another planning-judgment benchmark, useful for contrasting expert urban
reasoning with our intended behavioral benchmark.

## Core Claim / Contribution

The paper benchmarks LLMs against professional urban planning judgment.

## Evidence We May Cite

- Professional-judgment evaluation frame.
- Potential rubric ideas for comparing model outputs against human expert judgments.

## City Benchmark Bridge

- What it already measures: planner-like reasoning and judgment quality.
- What it does not measure: daily-life agency, movement traces, or environment-grounded social interaction.
- How it informs our SOTOPIA-style city benchmark: May inspire rubric language, but should not define our core task family.

## What We Add Beyond This Paper

6-city can evaluate situated behavior rather than professional advice.

## Draft-Ready Use Sentence

> Planner benchmarks such as UPBench evaluate expert judgment; our benchmark asks whether agents can live and adapt inside a city world.

## Caveats / Follow-Up

- Extraction issues: abstract_may_include_layout_noise.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `cite`

Reason: Useful planning contrast; check PDF/source before citing because the extracted abstract has a layout-noise flag.

## Extracted Abstract Snapshot

Problem, Research Strategy, and Findings The emergence of large language models (LLMs) confronts urban planning with an urgent epistemological question: what dimensions of professional planning knowledge can artificial intelligence replicate, and what remains irreducibly human? Despite growing deployment of AI tools in planning practice, we lack systematic frameworks for evaluating whether these systems can reason with the contextual sensitivity, value awareness, and institutional literacy that characterize professional planning judgment. This paper introduces Urban Planning Bench (UPBench), a domainspecific evaluative framework that assesses LLM reasoning across a 4×5 matrix encompassing four knowledge pillars (Principles of Urban Planning, Cross-Disciplinary Integration, Planning Governance, and Planning Practice) and five cognitive levels adapted from Bloom’s revised taxonomy. Evaluating 25 LLMs through a dual-track protocol combining automated scoring with expert panel assessment, we identify an non-monotonic cognitive curve: models perform more robustly on higher-order analytical tasks than on ostensibly lower-order factual recall and integrative judgment.
