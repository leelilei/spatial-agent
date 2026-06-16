# 3-SMGA-EVAL

Diagnostic **social-coherence evaluation** for multi-agent LLM game agents
(Generative Agents lineage). A sibling project to `../3-SMGA`.

- **3-SMGA-EVAL (this repo)** = the **benchmark + measuring stick**: an automatic,
  scalable diagnostic of long-horizon SOCIAL COHERENCE in persistent multi-agent
  LLM simulations, grounded in the simulation's own **emergent event log** (not
  pre-assigned goals, not static identity profiles).
- **3-SMGA (sibling)** = the **architecture under test**: a revised, GA-based social
  memory mechanism (SMGA v2) developed and validated *on* this benchmark.

The two reinforce each other: the eval is the standard; the architecture is the
treatment.

## Why this exists (the gap)

GA, AGA, SOTOPIA, LIFELONG-SOTOPIA, and ID-RAG each leave the same hole open:
- GA / AGA score believability by **human rank / coarse counts**.
- SOTOPIA / LIFELONG-SOTOPIA score against **pre-assigned goals** in 2-agent episodes.
- ID-RAG checks persona self-consistency against a **static identity profile**.
- LoCoMo / MemBench are **single-user memory QA**.

None do **automatic, society-scale coherence diagnostics grounded in emergent sim
logs**. That is the niche.

## Coherence dimensions (machine-checkable)

```text
C1 Commitment-honoring · C2 Belief grounding / anti-hallucination ·
C3 Relational consistency · C4 Currency / temporal consistency
```

## Layout

```text
docs/        proposal and design notes (proposal_v0.md = full first draft)
benchmarks/  the diagnostic harness + extracted ground-truth (to be built)
```

## Status / next

`docs/proposal_v0.md` is the first draft. Immediate next step is the **E0 zero-API
prototype**: belief-grounding (C2) on pre-packaged GA run logs — extract
who-heard-what from movement logs, check each agent's claims against its memory
stream. Proves "emergent ground truth + automatic check" before any spend.

Reuses the 3-SMGA toolkit (condition-blind extraction, LLM judge, gold-fact/probe
methodology, capability-axis runners, concurrency).
