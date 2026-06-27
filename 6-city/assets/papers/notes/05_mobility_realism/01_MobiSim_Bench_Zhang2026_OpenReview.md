---
canonical: true
title: "MobiSim-Bench: A Multi-Perspective Benchmark for Evaluating LLM-Agent-Based Human Mobility Simulation"
category: 05_mobility_realism
role: "closest mobility-simulation benchmark"
decision: must-cite
source: "https://openreview.net/forum?id=3QFvAXuNl7"
pdf: "assets/papers/pdf/05_mobility_realism/01_MobiSim_Bench_Zhang2026_OpenReview.pdf"
fulltext: "assets/papers/fulltext/05_mobility_realism/01_MobiSim_Bench_Zhang2026_OpenReview.fulltext.md"
quality_flags: ["abstract_may_include_layout_noise"]
note_status: first_pass
---

# MobiSim-Bench: A Multi-Perspective Benchmark for Evaluating LLM-Agent-Based Human Mobility Simulation

## Why This Paper Matters For 6-city

MobiSim-Bench is the strongest direct benchmark neighbor because it evaluates LLM-agent
mobility from robustness, realism, and responsiveness perspectives in both daily and
extraordinary conditions.

## Core Claim / Contribution

The benchmark evaluates human mobility simulation through complementary daily-mobility
and hurricane-response settings using micro- and macro-level measurements.

## Evidence We May Cite

- Three-part robustness, realism, and responsiveness framework.
- Daily and disruptive mobility scenarios implemented on an agent-society simulator.

## City Benchmark Bridge

- What it already measures: aggregate mobility realism, run robustness, and behavioral response to environmental disruption.
- What it does not measure: fine-grained proof that an individual agent completed private goals through a valid continuous trace.
- How it informs our SOTOPIA-style city benchmark: Use it as the macro-level benchmark anchor and make CityAgency's individual execution diagnostics explicit.

## What We Add Beyond This Paper

CityAgency can explain why a trajectory fails by checking goal evidence, world-state
transitions, impossible movement, false continuation, and replanning decisions.

## Draft-Ready Use Sentence

> MobiSim-Bench evaluates whether populations reproduce robust and responsive mobility; CityAgency diagnoses whether individual agents execute intentions as valid city traces.

## Caveats / Follow-Up

- Extraction issues: abstract_may_include_layout_noise.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Closest benchmark competitor and essential positioning reference.

## Extracted Abstract Snapshot

011 012 With advances in large language models (LLMs) and agent technology, LLM 013 agents are transforming social science research on human behavior simulation with 014 their powerful role-playing capabilities. Among the simulation studies on complex 015 human behaviors, mobility behavior simulation has been receiving widespread 016 attention and has important implications for real-world applications. Unlike data017 driven statistical learning approaches, LLM agent-based simulation methods have 018 the potential to support all-day simulation and generation of human mobility be019 haviors or even simulation of adaptive changes in the environment in extraordinary 020 scenarios. To evaluate the performance of LLM agents for human mobility be021 havior simulation from multiple perspectives and in a holistic manner, we first 022 propose an evaluation framework, which contains three perspectives: Robustness, Realism, and Responsiveness. To implement the evaluation framework, 023 we construct and publish a multi-perspective benchmark named MobiSim-Bench 024 based on the AgentSociety simulation framework.
