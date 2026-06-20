---
telephone_index: 20
canonical: true
aliases: [3]
title: "Improving Factuality and Reasoning in Language Models through Multiagent Debate"
category: 02_debate_consensus
role: debate / positive social-reasoning baseline
decision: cite
doi:
venue: arXiv
year: 2023
source_quality: preprint_or_unresolved
fulltext: assets/papers/fulltext/02_debate_consensus/20_improving-factuality-and-reasoning-in-language-models-through-multiagent-debate.fulltext.md
pdf: assets/papers/pdf/02_debate_consensus/20_improving-factuality-and-reasoning-in-language-models-through-multiagent-debate.pdf
read_status: deep-read
deep_read_scope: manual-project-deep-read

---

# Improving Factuality and Reasoning in Language Models through Multiagent Debate

## Why This Paper Matters For Telephone

This paper is a useful positive reference for the intuition that multi-agent
interaction can improve factuality and reasoning. It frames debate as a mechanism
where multiple model instances propose answers, critique one another, and converge
on a common final answer. That is the optimistic prior against which our results
become interesting: social interaction among LLM agents can help on some
question-answering tasks, but a socially embedded agent society can still fail to
convert a correction into held belief.

## Core Claim / Result

The paper proposes multiagent debate as a black-box prompting procedure. Multiple
model instances produce candidate answers, read and critique others' responses,
and update over several rounds before converging. The reported result is improved
reasoning and factual validity over single-model baselines across a set of tasks.

## Evidence We May Cite

- Multi-agent discussion/debate is an established method for improving factuality
  and reasoning.
- The paper explicitly frames convergence on a common answer as desirable.
- The method operates through utterances and critique over rounds, making it a
  useful contrast to our society-scale conversational dynamics.
- Its positive results make it natural to ask whether more social exchange or
  authoritative speech should repair truth in agent societies.

## Telephone Bridge

- Fidelity vs reach: Debate improves final task answers in a structured QA
  setting. Telephone asks whether social propagation preserves a factual update
  in an open memory-bearing society.
- Speech vs belief: Debate's endpoint is a final answer; Telephone separates the
  conversation stream from the final probed belief.
- Entrenchment / path dependence: Debate assumes later critique can correct earlier
  answers. Telephone shows that in a society with memory and repeated interaction,
  late correction can fail if the stale value is already entrenched.
- Failed natural lever: This paper motivates why multi-agent interaction might be
  expected to help; our connectivity/source results show that more or clearer
  speech is not sufficient.
- Measurement / rigor: It helps position our work as not anti-debate, but as
  showing a different failure regime.

## What We Add Beyond This Paper

The debate setup is task-centered and answer-centered. Telephone is
society-centered and belief-centered. We do not ask whether a panel can produce a
better answer to a query; we ask whether an update can survive social transmission
and become what agents hold after conversation. This lets us expose a gap that
debate-style evaluation tends to collapse: the difference between saying the
current answer and holding the current version as belief.

## Draft-Ready Use Sentence

> Multi-agent debate has shown that structured interaction among model instances
> can improve factuality and reasoning on answer-generation tasks; our results
> identify a complementary failure mode in which social interaction changes what
> agents say without reliably changing what they later hold.

## Caveats

- Source-quality issues: currently recorded as arXiv; verify final venue before
  camera-ready.
- Extraction issues: local fulltext is usable and unflagged.
- Not our claim: do not frame this paper as a failure result. Its role is the
  optimistic baseline for multi-agent factual improvement.

## Citation Decision

Decision: `cite`

Reason: Important for positioning, but less central than Generative Agents or the
closest misinformation/fidelity neighbors.
