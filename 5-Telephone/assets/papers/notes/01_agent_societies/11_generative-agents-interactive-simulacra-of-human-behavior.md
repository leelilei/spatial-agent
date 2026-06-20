---
telephone_index: 11
canonical: true
aliases: [1]
title: "Generative Agents: Interactive Simulacra of Human Behavior"
category: 01_agent_societies
role: setting / must-cite neighbor
decision: must-cite
doi: 10.1145/3586183.3606763
venue: "Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST 2023)"
year: 2023
source_quality: abstract_layout_caution
fulltext: assets/papers/fulltext/01_agent_societies/11_generative-agents-interactive-simulacra-of-human-behavior.fulltext.md
pdf: assets/papers/pdf/01_agent_societies/11_generative-agents-interactive-simulacra-of-human-behavior.pdf
read_status: deep-read
deep_read_scope: manual-project-deep-read

---

# Generative Agents: Interactive Simulacra of Human Behavior

## Why This Paper Matters For Telephone

This is the canonical LLM-agent society paper for our setting. It demonstrates
that a population of LLM-driven agents with memory, reflection, planning, and
environmental interaction can produce believable individual behavior and
emergent group behavior. For Telephone, its most important role is not simply
"agent framework citation"; it is the paper that makes social information
diffusion in agent societies vivid and legitimate.

The key bridge is the Valentine party example. A single agent is given an
intention to host a party, and the society propagates invitations, forms social
plans, and coordinates attendance. That example is a success case for reach and
coordination. Our paper asks the complementary question that this success case
leaves open: when information spreads through such a society, does the society
preserve the truth of the information?

## Core Claim / Result

The paper introduces generative agents: LLM-based computational agents that
store experiences as natural-language memories, retrieve relevant memories,
synthesize higher-level reflections, and plan actions. In a sandbox town of 25
agents, the architecture produces believable routines and emergent social
coordination, including an example where a party plan spreads from one agent
through the community.

## Evidence We May Cite

- The architecture has three central components that matter for our experiments:
  memory stream, reflection, and planning.
- The sandbox contains 25 agents, matching the scale of our core Telephone
  society and making it a natural methodological ancestor.
- The paper explicitly treats information diffusion and emergent social behavior
  as evidence that agent societies can coordinate through conversation and
  memory.
- The Valentine party episode is a positive example of social spread, but it is
  not a fidelity evaluation: the endpoint is believable coordination, not
  whether a ground-truthed update remains correct after transmission.

## Telephone Bridge

- Fidelity vs reach: Generative Agents shows that information can move through
  an LLM-agent society. Telephone adds the missing fidelity axis: whether the
  final held belief matches a known current truth.
- Speech vs belief: The UIST paper evaluates believable behavior and coordination.
  Telephone separates what agents say in conversation from what they later hold
  when probed.
- Entrenchment / path dependence: The original architecture gives agents memory
  and reflection loops that make prior experiences consequential. Telephone shows
  that these same social-memory dynamics can entrench stale versions.
- Failed natural lever: Because the architecture already uses memory, retrieval,
  reflection, and planning, our negative memory/source results matter: ordinary
  agent-society machinery does not guarantee truth repair.
- Communication-time collapse analogy: Generative Agents supplies the
  communication substrate. Telephone studies degradation through that substrate,
  rather than through recursive training.
- Measurement / rigor: This paper motivates ecological believability; our
  contribution is a controlled, ground-truthed fidelity metric inside a similar
  multi-agent scale.

## What We Add Beyond This Paper

Generative Agents asks whether LLM agents can simulate believable social life.
Telephone asks whether a society of such agents can preserve a corrected fact.
The UIST paper demonstrates emergent diffusion and coordination; it does not
measure truth preservation, distinguish speech from held belief, or test whether
an authoritative correction changes final belief. Our result is therefore not a
replacement for Generative Agents, but a stress test of the epistemic reliability
of the kind of society it made plausible.

## Draft-Ready Use Sentence

> Generative-agent societies have shown that LLM agents with memory, reflection,
> and planning can produce believable social dynamics and diffuse information
> across a 25-agent community; our work asks the missing fidelity question:
> whether what diffuses remains the current truth when agents later report their
> held belief.

## Caveats

- Source-quality issues: index 1 and index 11 are duplicates of the same UIST
  2023 paper. Use this note as canonical.
- Extraction issues: the extracted abstract contains minor layout noise from the
  ACM first page; use the full text/PDF for exact wording.
- Not our claim: we should not claim Generative Agents studied misinformation,
  correction, or belief fidelity. Its role is setting and contrast.

## Citation Decision

Decision: `must-cite`

Reason: It is the foundational LLM-agent society reference and the cleanest
contrast for our measurement shift from social reach/coordination to
ground-truthed fidelity and held belief.
