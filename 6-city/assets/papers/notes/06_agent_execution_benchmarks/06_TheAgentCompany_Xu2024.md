---
canonical: true
title: "TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks"
category: 06_agent_execution_benchmarks
role: "consequential long-horizon agent benchmark"
decision: cite
source: "https://arxiv.org/abs/2412.14161"
pdf: "assets/papers/pdf/06_agent_execution_benchmarks/06_TheAgentCompany_Xu2024.pdf"
fulltext: "assets/papers/fulltext/06_agent_execution_benchmarks/06_TheAgentCompany_Xu2024.fulltext.md"
quality_flags: []
note_status: first_pass
---

# TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks

## Why This Paper Matters For 6-city

TheAgentCompany broadens executable evaluation to consequential workplace tasks
involving tools, communication, and persistent organizational state.

## Core Claim / Contribution

The benchmark creates a self-contained software-company environment in which agents
complete realistic professional tasks across web, code, programs, and coworker
communication.

## Evidence We May Cite

- Consequential tasks spanning multiple tools and coworkers.
- Persistent environment where agent actions modify shared state.

## City Benchmark Bridge

- What it already measures: completion of long-horizon professional tasks in a stateful environment.
- What it does not measure: physical city movement, resident routines, or empirical mobility realism.
- How it informs our SOTOPIA-style city benchmark: Design city tasks whose actions affect later obligations and other agents rather than isolated one-shot navigation goals.

## What We Add Beyond This Paper

CityAgency can make consequences spatial and temporal, including missed meetings,
unavailable resources, and downstream schedule failures.

## Draft-Ready Use Sentence

> TheAgentCompany evaluates consequential action in a persistent digital workplace; CityAgency studies analogous consequences in an urban world.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `cite`

Reason: Relevant long-horizon comparison for stateful, socially consequential execution.

## Extracted Abstract Snapshot

We interact with computers on an everyday basis, be it in everyday life or work, and many aspects of work can be done entirely with access to a computer and the Internet. At the same time, thanks to improvements in large language models (LLMs), there has also been a rapid development in AI agents that interact with and affect change in their surrounding environments. But how performant are AI agents at accelerating or even autonomously performing work-related tasks? The answer to this question has important implications both for industry looking to adopt AI into their workflows and for economic policy to understand the effects that adoption of AI may have on the labor market. To measure the progress of these LLM agents’ performance on performing real-world professional tasks, in this paper we introduce TheAgentCompany, an extensible benchmark for evaluating AI agents that interact with the world in similar ways to those of a digital worker: by browsing the Web, writing code, running programs, and communicating with other coworkers.
