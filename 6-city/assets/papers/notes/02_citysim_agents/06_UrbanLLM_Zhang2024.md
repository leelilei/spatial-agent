---
canonical: true
title: "UrbanLLM: Autonomous Urban Activity Planning and Management with Large Language Models"
category: 02_citysim_agents
role: "urban activity planning with LLMs"
decision: cite
source: "https://arxiv.org/abs/2406.12360"
pdf: "assets/papers/pdf/02_citysim_agents/06_UrbanLLM_Zhang2024.pdf"
fulltext: "assets/papers/fulltext/02_citysim_agents/06_UrbanLLM_Zhang2024.fulltext.md"
quality_flags: []
note_status: first_pass
---

# UrbanLLM: Autonomous Urban Activity Planning and Management with Large Language Models

## Why This Paper Matters For 6-city

UrbanLLM is relevant because city agents need activity planning, daily scheduling, and
management of urban tasks.

## Core Claim / Contribution

The paper applies LLMs to autonomous urban activity planning and management.

## Evidence We May Cite

- Urban activity planning framing.
- Potential baseline for schedule and activity-generation components.

## City Benchmark Bridge

- What it already measures: planning and management quality for urban activities.
- What it does not measure: controlled interactive benchmark episodes with social relationships and spatial perturbations.
- How it informs our SOTOPIA-style city benchmark: Use for the planning component in the benchmark taxonomy.

## What We Add Beyond This Paper

6-city can test whether planning translates into feasible and adaptive trajectories.

## Draft-Ready Use Sentence

> UrbanLLM studies LLM-based urban activity planning; 6-city evaluates planned activity as behavior in a constrained world.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `cite`

Reason: Relevant component-level reference.

## Extracted Abstract Snapshot

Location-based services play an critical role in improving the quality of our daily lives. Despite the proliferation of numerous specialized AI models within spatio-temporal context of location-based services, these models struggle to autonomously tackle problems regarding complex urban planing and management. To bridge this gap, we introduce UrbanLLM, a fine-tuned large language model (LLM) designed to tackle diverse problems in urban scenarios. UrbanLLM functions as a problemsolver by decomposing urban-related queries into manageable sub-tasks, identifying suitable spatio-temporal AI models for each sub-task, and generating comprehensive responses to the given queries. Our experimental results indicate that UrbanLLM significantly outperforms other established LLMs, such as Llama and the GPT series, in handling problems concerning complex urban activity planning and management. UrbanLLM exhibits considerable potential in enhancing the effectiveness of solving problems in urban scenarios, reducing the workload and reliance for human experts. Our code is available at: https://anonymous.4open.science/r/UrbanLLM1227/
