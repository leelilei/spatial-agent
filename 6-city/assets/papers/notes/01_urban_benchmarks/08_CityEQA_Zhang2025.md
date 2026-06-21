---
canonical: true
title: "CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space"
category: 01_urban_benchmarks
role: "embodied city QA benchmark"
decision: must-cite
source: "https://arxiv.org/abs/2502.12532"
pdf: "assets/papers/pdf/01_urban_benchmarks/08_CityEQA_Zhang2025.pdf"
fulltext: "assets/papers/fulltext/01_urban_benchmarks/08_CityEQA_Zhang2025.fulltext.md"
quality_flags: []
note_status: first_pass
---

# CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space

## Why This Paper Matters For 6-city

CityEQA is a direct embodied-city benchmark reference. It makes city-space navigation
and question answering concrete.

## Core Claim / Contribution

The paper presents an embodied question-answering benchmark in city space and a
hierarchical LLM-agent approach.

## Evidence We May Cite

- City-space embodied QA setup.
- Hierarchical agent design for navigation and answering.

## City Benchmark Bridge

- What it already measures: question answering grounded in city-space exploration/navigation.
- What it does not measure: daily-life private goals, social encounters, or multi-objective city behavior.
- How it informs our SOTOPIA-style city benchmark: Use as a close benchmark for embodied city navigation, then distinguish our resident-intention episode benchmark.

## What We Add Beyond This Paper

6-city can evaluate whether agents choose and revise actions for their own goals, not
only find information for a query.

## Draft-Ready Use Sentence

> CityEQA demonstrates city-scale embodied QA; 6-city shifts the task from answering external questions to pursuing internal goals under spatial constraints.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Closest reference for embodied city benchmark design.

## Extracted Abstract Snapshot

Embodied Question Answering (EQA) has primarily focused on indoor environments, leaving the complexities of urban settings—spanning environment, action, and perception—largely unexplored. To bridge this gap, we introduce CityEQA, a new task where an embodied agent answers open-vocabulary questions through active exploration in dynamic city spaces. To support this task, we present CityEQA-EC, the first benchmark dataset featuring 1,412 human-annotated tasks across six categories, grounded in a realistic 3D urban simulator. Moreover, we propose Planner-Manager-Actor (PMA), a novel agent tailored for CityEQA. PMA enables long-horizon planning and hierarchical task execution: the Planner breaks down the question answering into sub-tasks, the Manager maintains an object-centric cognitive map for spatial reasoning during the process control, and the specialized Actors handle navigation, exploration, and collection sub-tasks. Experiments demonstrate that PMA achieves 60.7% of human-level answering accuracy, significantly outperforming competitive baselines. While promising, the performance gap compared to humans highlights the need for enhanced visual reasoning in CityEQA.
