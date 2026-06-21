---
canonical: true
title: "STBench: Assessing the Ability of Large Language Models in Spatio-Temporal Analysis"
category: 01_urban_benchmarks
role: "spatiotemporal reasoning benchmark"
decision: cite
source: "https://arxiv.org/abs/2406.19065"
pdf: "assets/papers/pdf/01_urban_benchmarks/03_STBench_Wang2024.pdf"
fulltext: "assets/papers/fulltext/01_urban_benchmarks/03_STBench_Wang2024.fulltext.md"
quality_flags: []
note_status: first_pass
---

# STBench: Assessing the Ability of Large Language Models in Spatio-Temporal Analysis

## Why This Paper Matters For 6-city

STBench gives us a reference for evaluating spatiotemporal reasoning, which city agents
need for scheduling, route choice, opening hours, and event timing.

## Core Claim / Contribution

The benchmark dissects LLM spatiotemporal capability into multiple categories, including
knowledge, reasoning, computation, and downstream tasks.

## Evidence We May Cite

- Task decomposition for spatiotemporal analysis.
- Large QA-style benchmark that can inspire our spatial-temporal probe design.

## City Benchmark Bridge

- What it already measures: spatiotemporal analysis and QA performance.
- What it does not measure: agents embedded in a changing city world with action feasibility and state updates.
- How it informs our SOTOPIA-style city benchmark: Reuse its decomposition when designing probes for time windows, route constraints, and schedule conflicts.

## What We Add Beyond This Paper

6-city can turn spatiotemporal questions into embodied decisions with consequences.

## Draft-Ready Use Sentence

> STBench motivates spatiotemporal reasoning as a distinct requirement, while 6-city evaluates how such reasoning affects agent trajectories.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `cite`

Reason: Useful methods reference for temporal/spatial subskills.

## Extracted Abstract Snapshot

The rapid evolution of large language models (LLMs) holds promise for reforming the methodology of spatio-temporal data mining. However, current works for evaluating the spatio-temporal understanding capability of LLMs are somewhat limited and biased. These works either fail to incorporate the latest language models or only focus on assessing the memorized spatio-temporal knowledge. To address this gap, this paper dissects LLMs’ capability of spatio-temporal data into four distinct dimensions: knowledge comprehension, spatio-temporal reasoning, accurate computation, and downstream applications. We curate several natural language question-answer tasks for each category and build the benchmark dataset, namely STBench, containing 13 distinct tasks and over 60,000 QA pairs. Moreover, we have assessed the capabilities of 13 LLMs, such as GPT-4o, Gemma and Mistral. Experimental results reveal that existing LLMs show remarkable performance on knowledge comprehension and spatio-temporal reasoning tasks, with potential for further enhancement on other tasks through in-context learning, chain-of-though prompting, and fine-tuning.
