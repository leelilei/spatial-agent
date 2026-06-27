---
canonical: true
title: "WebArena: A Realistic Web Environment for Building Autonomous Agents"
category: 06_agent_execution_benchmarks
role: "reproducible long-horizon environment benchmark"
decision: cite
source: "https://arxiv.org/abs/2307.13854"
pdf: "assets/papers/pdf/06_agent_execution_benchmarks/05_WebArena_Zhou2023.pdf"
fulltext: "assets/papers/fulltext/06_agent_execution_benchmarks/05_WebArena_Zhou2023.fulltext.md"
quality_flags: []
note_status: first_pass
---

# WebArena: A Realistic Web Environment for Building Autonomous Agents

## Why This Paper Matters For 6-city

WebArena is a mature example of evaluating agents in a realistic, resettable environment
with long-horizon tasks and functional correctness checks.

## Core Claim / Contribution

The benchmark provides reproducible functional websites and human-like tasks for
evaluating language-guided autonomous web agents end to end.

## Evidence We May Cite

- Self-hosted, resettable environment with realistic task domains.
- Functional task correctness rather than textual answer similarity.

## City Benchmark Bridge

- What it already measures: end-to-end functional success in long-horizon web tasks.
- What it does not measure: private autonomous goals, physical travel, or trajectory believability.
- How it informs our SOTOPIA-style city benchmark: Package city scenarios as resettable world snapshots with reproducible initial and goal states.

## What We Add Beyond This Paper

CityAgency can evaluate both functional completion and whether the intervening physical
trace is possible and credible.

## Draft-Ready Use Sentence

> WebArena established resettable functional environments for agent evaluation; CityAgency transfers that rigor to urban action and movement.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `cite`

Reason: Useful benchmark-infrastructure and end-to-end evaluation precedent.

## Extracted Abstract Snapshot

With advances in generative AI, there is now potential for autonomous agents to manage daily tasks via natural language commands. However, current agents are primarily created and tested in simplified synthetic environments, leading to a disconnect with real-world scenarios. In this paper, we build an environment for language-guided agents that is highly realistic and reproducible. Specifically, we focus on agents that perform tasks on the web, and create an environment with fully functional websites from four common domains: e-commerce, social forum discussions, collaborative software development, and content management. Our environment is enriched with tools (e.g., a map) and external knowledge bases (e.g., user manuals) to encourage human-like task-solving. Building upon our environment, we release a set of benchmark tasks focusing on evaluating the functional correctness of task completions. The tasks in our benchmark are diverse, long-horizon, and designed to emulate tasks that humans routinely perform on the internet. We experiment with several baseline agents, integrating recent techniques such as reasoning before acting.
