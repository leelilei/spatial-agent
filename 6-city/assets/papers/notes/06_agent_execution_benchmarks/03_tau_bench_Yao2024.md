---
canonical: true
title: "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
category: 06_agent_execution_benchmarks
role: "state-based interactive-agent benchmark"
decision: must-cite
source: "https://arxiv.org/abs/2406.12045"
pdf: "assets/papers/pdf/06_agent_execution_benchmarks/03_tau_bench_Yao2024.pdf"
fulltext: "assets/papers/fulltext/06_agent_execution_benchmarks/03_tau_bench_Yao2024.fulltext.md"
quality_flags: []
note_status: first_pass
---

# tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

## Why This Paper Matters For 6-city

tau-bench provides two crucial design precedents: evaluate final environment state
rather than verbal claims, and measure reliability over repeated executions.

## Core Claim / Contribution

The benchmark evaluates agents interacting with simulated users and domain APIs by
comparing the resulting database state with an annotated goal state.

## Evidence We May Cite

- Authoritative state-based task evaluation.
- The pass^k metric for repeated-run behavioral reliability.

## City Benchmark Bridge

- What it already measures: goal-state correctness, policy compliance, and consistency over repeated trials.
- What it does not measure: continuous space, travel time, embodied observations, or human-like urban traces.
- How it informs our SOTOPIA-style city benchmark: Use world-state predicates for goal completion and repeated seeds for reliability instead of trusting self-reported success.

## What We Add Beyond This Paper

CityAgency can add trace continuity and intermediate-state validity, because the path to
a city goal matters as well as the final state.

## Draft-Ready Use Sentence

> tau-bench validates agents against authoritative goal states and repeated trials; CityAgency extends this principle to continuous urban trajectories.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Core methodological precedent for proof-carrying traces and repeated reliability.

## Extracted Abstract Snapshot

Existing benchmarks do not test language agents on their interaction with human users or ability to follow domain-specific rules, both of which are vital for deploying them in real world applications. We propose τ -bench, a benchmark emulating dynamic conversations between a user (simulated by language models) and a language agent provided with domain-specific API tools and policy guidelines. We employ an efficient and faithful evaluation process that compares the database state at the end of a conversation with the annotated goal state. We also propose a new metric (pass^k) to evaluate the reliability of agent behavior over multiple trials. Our experiments show that even state-of-the-art function calling agents (like gpt-4o) succeed on < 50% of the tasks, and are quite inconsistent (pass^8 < 25% in retail). Our findings point to the need for methods that can improve the ability of agents to act consistently and follow rules reliably.
