# Proposal v0 — Diagnostic Social Coherence for Multi-Agent LLM Game Agents
### (and a revised, GA-based SMGA memory architecture to improve it)

> Date: 2026-06-16
> Status: first draft, post-pivot. Consolidates the 2026-06-15/16 investigation.
> North star: **LLM GAME AGENTS** — believable multi-agent social *simulation* in
> the Generative Agents (GA) lineage. Memory is a lever, not the goal.

---

## 0. TL;DR

We build, in one program, two reinforcing things:

1. **A diagnostic benchmark + automatic metric suite for long-horizon SOCIAL
   COHERENCE in persistent multi-agent LLM simulations** — grounding coherence
   checks in the **emergent event log of the simulation itself** (not pre-assigned
   goals, not a static identity profile). This is the contribution and the
   measuring stick. It fills a gap GA, AGA, SOTOPIA, LIFELONG-SOTOPIA, and ID-RAG
   each explicitly leave open.

2. **A revised GA-based social-memory architecture** ("SMGA v2"), developed and
   validated *on* that benchmark, informed by what the modern memory frameworks
   (Mem0, A-Mem, ENGRAM, ID-RAG) do well — and by what our own experiments proved
   does *not* work (pre-committed affordances). SMGA is not abandoned; it is
   re-pointed at the regime where memory architecture actually matters
   (long-horizon coherence + simulation cost), with a standard to measure it.

The eval is the foundation; the architecture is what it enables.

---

## 1. North star and why memory is the lever

The original reason to build on GA was to enter **LLM game agents** —
believable, autonomous multi-agent societies (GA's Smallville). Pure memory-QA
research (LongMemEval/LoCoMo) abandons that goal, so we reject it. We stay in the
multi-agent social-simulation frame and ask: *what makes a society of LLM agents
stay believable and coherent over a long simulation, affordably?*

## 2. What the investigation taught us (the gauntlet)

Condensed, all from our own runs (`docs/project/findings_capability_axis_2026-06-15.md`):

```text
- On a frontier model with everything in context, NO memory STRUCTURE improves
  single-decision accuracy (format/currency/retrieval all null). The model
  re-derives. Memory architecture's value is therefore NOT better one-shot reasoning.
- Pre-committed "affordances" (actions baked into memory at formation) are
  DOUBLE-EDGED: they help when the right action is in-frame, and MISLEAD when it
  is out-of-frame. They did not generalize across scenario families. -> DROP THEM.
- Free-text reflection (GA-style) is robust and sometimes beats structured memory.
- Amortized formation works: a strong model can form memory a cheap planner reuses
  at near-frontier quality (distillation). Structure is most capability-robust.
- Where memory MUST matter: long horizon (info out of context), weak/cheap models,
  cost, and behavioral COHERENCE over time — none of which a single-shot probe shows.
```

The meta-lesson: we kept testing in the one regime where memory architecture cannot
matter (short context, single-shot, strong model). The game-agent regime — long,
persistent, multi-agent, where errors compound — is exactly where it does.

## 3. The gap (what every neighbor leaves open)

| System | Setting | Ground truth | What it scores |
|---|---|---|---|
| GA (Park 2023) | multi-agent society | emergent | **human** believability rank + coarse counts (diffusion, density) |
| AGA (Yu 2024) | multi-agent society | — | **cost** + believability Likert (GPT-4) |
| SOTOPIA (2024) | **2-agent, single episode** | **pre-assigned** goals | 7 end-of-episode dims |
| LIFELONG-SOTOPIA (2025) | 2-agent, multi-episode | pre-assigned goals | Goal + Bel (+8-item checklist) |
| ID-RAG (2025) | multi-agent (evals 2) | **static identity profile** | persona self-consistency |
| LoCoMo / MemBench | single user | conversation QA | retrieval accuracy |
| **This proposal** | **persistent multi-agent society** | **emergent sim event log** | **fine-grained, machine-checkable social coherence** |

Direct, quoted confirmations the gap is open:
- GA future work: evaluation "limited to a relatively short timescale"; "establish
  rigorous benchmarks"; robustness to "memory hacking" and hallucination "largely unknown".
- AGA limitation: "existing methods fall short in comprehensively assessing the
  believable behaviors of LLM agents; constructing a valid evaluation mechanism is
  of significant value."
- LIFELONG-SOTOPIA: hard scenarios "require human intervention, is not scalable."
- ID-RAG: "we have not yet measured the broader impact on social dynamics, emergent
  behaviors, or system fidelity."

Our distinctive asset: **emergent ground truth.** Everyone else scores against
something pre-specified (goals, identity profiles, QA answers). We score against
what the society *actually produced* in its own logs.

---

## 4. PART I — The diagnostic social-coherence benchmark

### 4.1 Core idea

Run (or reuse) a persistent multi-agent GA-style simulation. From its logs derive
**ground-truth social facts** (who said/promised/learned what, when), then
automatically check whether each agent's later behavior and memory stay coherent
with that ground truth. No human believability ranking, no pre-assigned goals.

### 4.2 The coherence dimensions (machine-checkable)

```text
C1 Commitment-honoring : promises/agreements made in dialogue are later remembered
                         and acted on (or explicitly renegotiated), not dropped.
C2 Belief grounding     : when an agent claims to know X, X is traceable to a real
   (anti-hallucination)   event in the log that reached that agent; no fabricated
                         social facts (GA checked this MANUALLY for 2 facts -> we
                         automate it for all, the "memory hacking" robustness GA flagged).
C3 Relational consistency: an agent's stance/treatment of another stays consistent
                         with their interaction history (no "I don't know you" after
                         meeting; relationship valence not contradicting events).
C4 Currency / temporal  : when a social fact updates (plan changes, trust shifts,
                         permission revised), the agent acts on the CURRENT state.
```

These map directly onto our prior probe families and onto GA's own emergent
phenomena (diffusion, relationship formation, coordination) — but as verifiable
properties rather than human-rated impressions.

### 4.3 Ground-truth extraction from GA logs (feasible, verified)

GA's released sim storage gives us exactly what we need (confirmed by inspecting
the cloned repo):
```text
movement/<timestep>.json   : per-step ground truth of every agent's action + full
                             chat -> the emergent event/interaction log.
personas/<agent>/.../nodes.json : each agent's accumulated memory stream (event/
                             thought/chat nodes) -> what the agent believes.
scratch.json               : identity + current plans.
```
Pipeline: parse movement logs -> extract emergent social facts/commitments/
relationship events (via our condition-blind LLM extraction) -> check agent
memory/behavior against them with the judge -> emit per-dimension diagnostics.
Prototype on the **pre-packaged GA run logs first at ZERO API cost.**

### 4.4 Methodology (reuse our toolkit)

- Condition-blind extraction + LLM-judge scoring (`judge_scorer.py` lineage).
- Gold-fact/probe discipline, now with **gold facts derived from the sim log**.
- Ablations: memory architecture (none / GA-reflection / SMGA v2) × model capability
  (strong / mini) × horizon length. (Our concurrency + capability-axis tooling.)
- Report coherence per dimension AND token cost/latency (so coherence-vs-cost is visible).

### 4.5 Why it is not redundant

Scalable + automatic (no hand-crafted scenarios, unlike LIFELONG-SOTOPIA) +
emergent-grounded (unlike SOTOPIA's pre-assigned goals and ID-RAG's static
profiles) + society-scale + decomposed into specific coherence properties (unlike
GA's human rank / AGA's Likert).

---

## 5. PART II — Revised SMGA architecture (kept alive, GA-based)

SMGA continues, re-pointed and informed by the modern frameworks. It is *the
treatment* we develop and measure on Part I.

### 5.1 Drop
- **Pre-committed affordances** (single action baked into memory at formation).
  Our experiments proved they are double-edged and do not generalize.

### 5.2 Keep / borrow (lessons + modern frameworks)
```text
- Amortized formation (ours): consolidate interactions with a capable model; cheap
  agents reuse it. Distillation held at 40 seeds.
- Persona-core vs episodic split (ID-RAG): separate stable identity/relationship
  state from transient episodic memory; retrieve identity context per decision.
- Typed, linked, retrievable social memory (A-Mem / ENGRAM): not pre-chosen actions
  but addressable social facts with currency status + evidence links, surfaced by
  retrieval at decision time (context-aware, not committed up front).
- Currency / contradiction tracking (ours): mark superseded social facts so agents
  act on current state — exactly C4 above.
```

### 5.3 Hypothesis to test on Part I
> A GA agent whose memory carries currency-tracked, retrievable social state (and a
> persona/episodic split), formed by a capable model, maintains higher long-horizon
> social coherence (C1–C4) at lower simulation cost than vanilla GA reflection — and
> the gap grows with horizon and as the per-agent model weakens.

This is the SMGA claim, finally in the regime where memory can matter, with a
benchmark that can show it.

---

## 6. Roadmap

```text
P0  (zero API)   Build the C2 belief-grounding prototype on pre-packaged GA run
                 logs: extract who-heard-what, check agent claims vs memory streams.
                 Proves "emergent ground truth + automatic check" works.
P1  (low API)    Extend to C1/C3/C4 on existing logs; freeze metric definitions;
                 validate against a few human spot-checks for agreement.
P2  (medium API) Re-run short GA sims with model/architecture ablations (vanilla GA
                 vs SMGA v2; strong vs mini) on a chosen horizon; report coherence + cost.
P3               Scale horizon / agents to where vanilla GA coherence breaks and SMGA v2
                 holds; write the benchmark + architecture paper.
```

## 7. Risks & novelty boundaries (honest)

```text
- The niche is narrow and the field moves weekly; the delta (emergent-grounded,
  scalable, society-scale coherence diagnostics) must stay sharply stated.
- Re-running GA sims needs adapting the GPT-3.5-era code to current models ($ + work);
  the eval prototype avoids this by using released logs.
- Defining "coherent" operationally per dimension is the real research work (as with
  our gold-fact/probe design); validate against human agreement.
- A genuinely hard goal: showing an ARCHITECTURE that is SOTA on coherence under broad
  generalization. Part I (the eval) is publishable on its own even if Part II is modest.
```

## 8. Reusable assets

```text
judge_scorer.py / condition-blind extraction · gold-fact-probe methodology ·
capability-axis runners (run_model_sweep, run_weak_agent) · concurrency (--parallel,
FHL ceiling ~60) · progress_monitor · cloned GA + AGA code and released sim logs ·
the entire SMGA diagnostic_v0 harness.
```

---

### Appendix: key references
GA (Park 2023, UIST) · AGA (Yu 2024, TMLR) · SOTOPIA (Zhou 2024, ICLR
2310.11667) · LIFELONG-SOTOPIA (2506.12666) · ID-RAG (2509.25299) · Mem0
(2504.19413) · A-Mem (2502.12110) · ENGRAM (2511.12960) · LoCoMo / LongMemEval /
MemBench.
