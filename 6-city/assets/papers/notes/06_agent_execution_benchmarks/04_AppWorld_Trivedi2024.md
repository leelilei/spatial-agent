---
canonical: true
title: "AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents"
category: 06_agent_execution_benchmarks
role: "executable world with programmatic state tests"
decision: cite
source: "https://arxiv.org/abs/2407.18901"
pdf: "assets/papers/pdf/06_agent_execution_benchmarks/04_AppWorld_Trivedi2024.pdf"
fulltext: "assets/papers/fulltext/06_agent_execution_benchmarks/04_AppWorld_Trivedi2024.fulltext.md"
quality_flags: []
note_status: first_pass
---

# AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents

## Why This Paper Matters For 6-city

AppWorld demonstrates how a rich simulated world can support multiple valid solution
paths while still testing intended outcomes and unintended side effects
programmatically.

## Core Claim / Contribution

The work builds an executable multi-app environment and evaluates complex agent tasks
with state-based unit tests, including checks for collateral damage.

## Evidence We May Cite

- Programmatic evaluation over a large executable state space.
- Outcome tests that allow alternative solutions and detect unintended changes.

## City Benchmark Bridge

- What it already measures: functional task completion and collateral state changes.
- What it does not measure: spatial continuity, mobility realism, or socially believable city behavior.
- How it informs our SOTOPIA-style city benchmark: Write verifier tests over world-state deltas and permit any route that satisfies goals without invalid side effects.

## What We Add Beyond This Paper

CityAgency can adapt collateral-damage checks to missed commitments, overspending,
invalid occupancy, and disruption of other agents.

## Draft-Ready Use Sentence

> AppWorld shows how open-ended agent behavior can be judged by executable state tests; CityAgency applies that pattern to urban worlds and traces.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `cite`

Reason: Strong engineering precedent for deterministic outcome and side-effect validation.

## Extracted Abstract Snapshot

Autonomous agents that address day-to-day digital tasks (e.g., ordering groceries for a household), must not only operate multiple apps (e.g., notes, messaging, shopping app) via APIs, but also generate rich code with complex control flow in an iterative manner based on their interaction with the environment. However, existing benchmarks for tool use are inadequate, as they only cover tasks that require a simple sequence of API calls. To remedy this gap, we built AppWorld Engine,1 a high-quality execution environment (60K lines of code) of 9 day-to-day apps operable via 457 APIs and populated with realistic digital activities simulating the lives of ~100 fictitious users. We then created AppWorld Benchmark (40K lines of code), a suite of 750 natural, diverse, and challenging autonomous agent tasks requiring rich and interactive code generation. It supports robust programmatic evaluation with state-based unit tests, allowing for different ways of completing a task while also checking for unexpected changes, i.e., collateral damage. The state-of-the-art LLM, GPT4O, solves only ~49% of our ‘normal’ tasks and ~30% of ‘challenge’ tasks, while other models solve at least 16% fewer.
