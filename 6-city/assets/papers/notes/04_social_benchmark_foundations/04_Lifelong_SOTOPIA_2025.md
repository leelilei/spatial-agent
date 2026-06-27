---
canonical: true
title: "Lifelong-SOTOPIA: Evaluating Social Intelligence of Language Agents Over Lifelong Social Interactions"
category: 04_social_benchmark_foundations
role: "longitudinal social-agent benchmark"
decision: cite
source: "https://arxiv.org/abs/2506.12666"
pdf: "assets/papers/pdf/04_social_benchmark_foundations/04_Lifelong_SOTOPIA_2025.pdf"
fulltext: "assets/papers/fulltext/04_social_benchmark_foundations/04_Lifelong_SOTOPIA_2025.fulltext.md"
quality_flags: []
note_status: first_pass
---

# Lifelong-SOTOPIA: Evaluating Social Intelligence of Language Agents Over Lifelong Social Interactions

## Why This Paper Matters For 6-city

Lifelong-SOTOPIA shows that agent quality can degrade across episodes and that memory
must be evaluated through later behavior, not only by inspecting stored summaries.

## Core Claim / Contribution

The benchmark extends social-agent evaluation to linked multi-episode interactions that
require agents to recover and use interaction history.

## Evidence We May Cite

- Multi-episode evaluation with persistent character histories.
- Goal achievement and believability tracked over prolonged interaction.

## City Benchmark Bridge

- What it already measures: longitudinal social goal achievement, believability, and use of interaction history.
- What it does not measure: persistent urban routines, spatial memories, or the feasibility of physical action over time.
- How it informs our SOTOPIA-style city benchmark: Use linked episodes later to test whether agents remember places, people, obligations, and prior disruptions.

## What We Add Beyond This Paper

CityAgency can extend lifelong evaluation from social memory to spatial and commitment
memory in a changing city.

## Draft-Ready Use Sentence

> Lifelong-SOTOPIA tests social intelligence across linked episodes; CityAgency can apply this principle to persistent urban commitments and spatial histories.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `cite`

Reason: Important extension path after the single-episode benchmark is stable.

## Extracted Abstract Snapshot

Humans engage in lifelong social interactions through interacting with different people under different scenarios for different social goals. This requires social intelligence to gather information through a long time span and use it to navigate various social contexts effectively. Whether AI systems are also capable of this is understudied in the existing research. In this paper, we present a novel benchmark, LIFELONG-SOTOPIA, to perform a comprehensive evaluation of language agents by simulating multi-episode interactions. In each episode, the language agents role-play characters to achieve their respective social goals in randomly sampled social tasks. With LIFELONG-SOTOPIA, we find that goal achievement and believability of all of the language models that we test decline through the whole interaction. Although using an advanced memory method improves the agents’ performance, the best agents still achieve a significantly lower goal completion rate than humans on scenarios requiring an explicit understanding of interaction history. These findings show that we can use LIFELONG-SOTOPIA to evaluate the social intelligence of language agents over lifelong social interactions.
