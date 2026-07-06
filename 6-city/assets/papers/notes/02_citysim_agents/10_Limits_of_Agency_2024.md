---
canonical: true
title: "On the Limits of Agency in Agent-Based Models"
category: 02_citysim_agents
role: "agency-vs-scale trade-off formalization; LLM-archetype (grouped, low-agency) million-scale ABM"
decision: cite
source: "https://arxiv.org/abs/2409.10568"
pdf: "assets/papers/pdf/02_citysim_agents/10_Limits_of_Agency_2024.pdf"
fulltext: "assets/papers/fulltext/02_citysim_agents/10_Limits_of_Agency_2024.fulltext.md"
quality_flags: [abstract_may_include_layout_noise]
note_status: first_pass
---

# On the Limits of Agency in Agent-Based Models

## Why This Paper Matters For 6-city

This paper (MIT/Oxford, AAMAS 2025) names the exact axis CityAgency sits on: the trade-off between
simulation scale and individual agent expressiveness. Its "LLM archetypes" — group the population by
demographics, one LLM call per archetype, replay that behavior for the whole group — is the
low-agency, high-scale end. CityAgency is the opposite pole (few agents, full individual agency,
verified per-agent trace). Cite it to place CityAgency on a recognized continuum rather than as an
isolated design choice.

## Core Claim / Contribution

Integrating LLMs into large ABMs is bottlenecked by cost and by simplistic agent behavior.
LLM archetypes balance behavioral complexity against compute, enabling millions of adaptive agents;
demonstrated on an 8.4M-agent NYC COVID-19 simulation (health × economic outcomes) in an open-source
differentiable-ABM framework.

## Evidence We May Cite

- Explicit scale↔expressiveness trade-off across architectures (heuristic → archetype → fully adaptive LLM agent).
- 8.4M-agent NYC case study; realism/utility gains while keeping compute feasible.
- Open-source differentiable ABM (AgentTorch-style) framing.

## City Benchmark Bridge

- What it already measures: population-level predictive/counterfactual realism at million scale.
- What it does not measure: whether any single agent held a private intention and completed a verifiable trace — archetype sharing deliberately erases per-agent autonomy.
- How it informs our SOTOPIA-style city benchmark: cite as the theoretical statement of why CityAgency chooses micro-scale + full agency; the two occupy different, complementary ends.

## What We Add Beyond This Paper

CityAgency operationalizes the high-agency end this paper flags as expensive: it keeps each agent
individually adaptive and adds an environment-owned evidence contract to verify that agency actually
produced outcomes.

## Draft-Ready Use Sentence

> The scale–agency trade-off in agent-based modeling is explicit (Chopra et al., 2025): archetype
> sharing buys millions of agents at the cost of individual expressiveness; CityAgency deliberately
> holds the opposite end, verifying the trace of a single fully-adaptive resident.

## Caveats / Follow-Up

- Extraction issues: two-column abstract is de-spaced (word boundaries lost); use PDF for quotes.
- Need to verify: exact framework name (AgentTorch) and whether any individual-level validation is reported.

## Citation Decision

Decision: `cite`

Reason: Canonical statement of the agency-vs-scale continuum that motivates CityAgency's position;
support for the "why micro-scale + full agency" subsection.

## Extracted Abstract Snapshot

Integrating LLMs into large ABMs is limited by compute and simplistic agents. Proposes LLM archetypes
(group by demographics, one LLM call per archetype) to simulate millions of adaptive agents. 8.4M-agent
NYC COVID-19 case study; open-source differentiable ABM. Formalizes scale↔expressiveness trade-off.
