---
canonical: true
title: "ChatSUMO: Large Language Model for Automating Traffic Scenario Generation in Simulation of Urban Mobility"
category: 02_citysim_agents
role: "traffic scenario generation / SUMO reference"
decision: background
source: "https://arxiv.org/abs/2409.09040"
pdf: "assets/papers/pdf/02_citysim_agents/05_ChatSUMO_Mao2024.pdf"
fulltext: "assets/papers/fulltext/02_citysim_agents/05_ChatSUMO_Mao2024.fulltext.md"
quality_flags: []
note_status: first_pass
---

# ChatSUMO: Large Language Model for Automating Traffic Scenario Generation in Simulation of Urban Mobility

## Why This Paper Matters For 6-city

ChatSUMO is useful if we include road networks or traffic scenarios, but it is less
central to the SOTOPIA-style city-agent benchmark direction.

## Core Claim / Contribution

The paper uses LLMs to automate traffic scenario generation for urban mobility
simulation.

## Evidence We May Cite

- LLM-assisted generation of traffic simulation scenarios.
- SUMO-related workflow reference.

## City Benchmark Bridge

- What it already measures: traffic scenario generation or mobility simulation setup quality.
- What it does not measure: autonomous social city agents with private daily goals.
- How it informs our SOTOPIA-style city benchmark: Keep as a background reference for a possible traffic/mobility task family.

## What We Add Beyond This Paper

6-city would evaluate agents acting inside scenarios, not only generate traffic
scenarios.

## Draft-Ready Use Sentence

> ChatSUMO is relevant to traffic-simulation tooling, but 6-city targets broader city-agent behavior.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `background`

Reason: Useful but peripheral for the current benchmark thesis.

## Extracted Abstract Snapshot

—Large Language Models (LLMs), capable of han- Despite its effectiveness, creating traffic simulation scedling multi-modal input and outputs such as text, voice, images, narios is a time-consuming process that requires specialized and video, are transforming the way we process information. traffic-related knowledge [7]. Most mainstream simulation Beyond just generating textual responses to prompts, they can software demands that users define networks, vehicles, routes, integrate with different software platforms to offer comprehensive solutions across diverse applications. In this paper, we and other parameters, which poses a significant barrier to present ChatSUMO, a LLM-based agent that integrates language entry for beginners who lack professional expertise or even for 4202 gu pprreosceensstiCnghastkSiUllsMtOo ,gaenLeLraMte-baabssetdraacgtenatndtharetainl-twegorraldtessimlanuglautaiogne scenarios in the widely-used traffic simulator - Simulation o Urban MObility (SUMO). Our methodology begins by leveraging the LLM for user input which converts to relevant keywords needed to run python scripts.
