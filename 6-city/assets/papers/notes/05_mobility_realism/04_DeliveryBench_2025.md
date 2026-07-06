---
canonical: true
title: "DeliveryBench: Can Agents Earn Profit in Real World?"
category: 05_mobility_realism
role: "city-scale embodied benchmark; long-horizon constraint-aware planning with profit as outcome"
decision: cite
source: "https://arxiv.org/abs/2512.19234"
pdf: "assets/papers/pdf/05_mobility_realism/04_DeliveryBench_2025.pdf"
fulltext: "assets/papers/fulltext/05_mobility_realism/04_DeliveryBench_2025.fulltext.md"
quality_flags: []
note_status: first_pass
---

# DeliveryBench: Can Agents Earn Profit in Real World?

## Why This Paper Matters For 6-city

DeliveryBench (UCSD/UMich) grounds a long-horizon embodied agent in a real profession — food delivery
— inside procedurally generated 3D cities with road networks, functional locations, transport modes,
and realistic resource dynamics (deadlines, expenses, battery). It adds an economic/profit outcome
dimension and social interaction with couriers/customers, both relevant to CityAgency's budget and
co-presence constraints. It is an embodied, profit-driven cousin of CityAgency's constrained episode.

## Core Claim / Contribution

A city-scale embodied benchmark where VLM agents maximize net profit over hours under interacting
deadline, cost, battery, and social constraints, across nine procedurally generated cities, compared
with human players. Agents show a substantial gap to humans, are short-sighted, and frequently break
basic commonsense constraints; distinct model "personalities" emerge (adventurous GPT-5 vs
conservative Claude).

## Evidence We May Cite

- Long-horizon net-profit objective as a single scalar that couples cost, benefit, and risk.
- Interacting constraint set (deadline, transport expense, vehicle battery) — a template for CityAgency's budget/deadline layer.
- Agents are short-sighted and break commonsense constraints; large human gap.

## City Benchmark Bridge

- What it already measures: constraint-aware long-horizon planning with an economic outcome in an embodied 3D city; human comparison.
- What it does not measure: private, hidden non-economic intentions; typed environment-owned completion evidence for social/service outcomes; graded replanning taxonomy.
- How it informs our SOTOPIA-style city benchmark: borrow the interacting-constraint + long-horizon design and the profit-as-outcome idea for CityAgency's economic constraint dimension.

## What We Add Beyond This Paper

CityAgency keeps outcomes multi-typed (place entry, purchase, service, meeting) and private rather than
collapsing success into profit, and verifies each with an environment-owned evidence contract instead
of an aggregate score.

## Draft-Ready Use Sentence

> Embodied city benchmarks such as DeliveryBench show agents are short-sighted and break basic
> constraints under long-horizon economic pressure; CityAgency generalizes beyond profit to private,
> multi-typed intentions verified by environment-owned evidence.

## Caveats / Follow-Up

- Extraction issues: two-column body de-spaced; use PDF for the constraint table and per-city results.
- Need to verify: exact metrics (net profit definition, human baseline setup) and how social interactions are scored.

## Citation Decision

Decision: `cite`

Reason: Strong embodied, constraint-dense, long-horizon neighbor; useful for the budget/economic
constraint dimension and the "agents break commonsense constraints" motivation.

## Extracted Abstract Snapshot

DeliveryBench: city-scale embodied benchmark grounded in food delivery. Couriers maximize net profit over
hours under deadline, transport expense, battery, and social constraints, in procedurally generated 3D
cities (nine cities). VLM agents vs humans: substantial gap; agents short-sighted, break commonsense
constraints; distinct model personalities (adventurous GPT-5 vs conservative Claude).
