---
canonical: true
title: "Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents"
category: 06_agent_execution_benchmarks
role: "agent infeasibility-awareness benchmark"
decision: must-cite
source: "https://arxiv.org/abs/2605.28532"
pdf: "assets/papers/pdf/06_agent_execution_benchmarks/02_FeasiGen_Do_Agents_Know_What_They_Cant_Do_2026.pdf"
fulltext: "assets/papers/fulltext/06_agent_execution_benchmarks/02_FeasiGen_Do_Agents_Know_What_They_Cant_Do_2026.fulltext.md"
quality_flags: []
note_status: first_pass
---

# Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents

## Why This Paper Matters For 6-city

FeasiGen isolates whether agents recognize that a task has become impossible and stop, a
central failure mode when city resources, routes, or time windows disappear.

## Core Claim / Contribution

The paper generates infeasible tasks by masking critical tools and evaluates whether
agents detect infeasibility instead of continuing unproductively.

## Evidence We May Cite

- Automatic construction of infeasible variants from successful tool traces.
- False-continue-style metrics for feasibility awareness.

## City Benchmark Bridge

- What it already measures: infeasibility detection, appropriate stopping, and wasted execution under missing capabilities.
- What it does not measure: graded spatial feasibility or recovery through alternative routes, places, and social coordination.
- How it informs our SOTOPIA-style city benchmark: Include paired feasible and infeasible city scenarios and report false continuation separately from task failure.

## What We Add Beyond This Paper

CityAgency can distinguish stop, repair, substitute, and impossible physical
continuation under urban disruptions.

## Draft-Ready Use Sentence

> FeasiGen tests whether tool agents know when execution is impossible; CityAgency brings feasibility awareness into spatially and temporally constrained city worlds.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Direct source for the false-continue metric and infeasible-scenario design.

## Extracted Abstract Snapshot

Tool-using agents often incur substantial computational cost due to long reasoning chains and iterative tool usage. In practical scenarios, many tasks become infeasible under constrained tool environments, where the capabilities required for successful task completion are unavailable. Detecting infeasible tasks and stopping execution early can significantly reduce unnecessary execution cost. In this work, we propose FeasiGen, an automatic pipeline for constructing infeasible agent tasks by identifying the critical tools required for successful task completion. Our approach extracts toolcalling traces from successful executions across multiple agent systems, identifies critical tools consistently shared across diverse execution strategies, and masks these tools to automatically transform solvable tasks into infeasible ones. Human verification confirms that the infeasibility annotations for our constructed tasks achieve over 94% accuracy. We further introduce feasibility-aware evaluation metrics for measuring whether agents can recognize infeasible tasks and stop execution appropriately.
