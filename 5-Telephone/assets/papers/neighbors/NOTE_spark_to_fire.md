# NOTE — "From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration"

> arXiv:2603.04474 (2026). Xie, Zhu, Zhang, Zhu, Ye, Qi, Chen, Zhou (City Univ. of Macau).
> PDF: `assets/papers/neighbors/2603.04474_spark_to_fire.pdf`. Read 2026-06-22.
> **Status: CLOSEST concurrent neighbor — must cite prominently and differentiate.**

## What they do
LLM multi-agent **error cascades**: a single injected **atomic error seed** solidifies into a
**system-level false consensus** via message dependencies. They (1) model propagation on a
directed dependency graph, identifying **cascade amplification, topological sensitivity, and
consensus inertia**; (2) instantiate an **attack** (inject one error → widespread failure);
(3) propose a **genealogy-graph governance layer** (message-layer plugin) that maintains a
global **Lineage Graph** of atomic-claim provenance (source + timestamp) and runs 3 stages
(verification, policy routing, risk arbitration with **external evidence retrieval** + LLM
verification), preventing "final infection" in ≥89% of runs.

## The overlaps (be honest — these are real)
1. **Provenance-as-cure.** Their "Lineage Graph" tracks atomic-claim provenance (source +
   timestamp) — the same core intuition as our PROV (origin/version tags).
2. **Adoption vs repetition.** Def. 2 "Propagation as Adoption": a falsehood `m` is *adopted*
   when it becomes a **semantic commitment / functional premise** in agent i's output, not mere
   surface repetition. This is close in spirit to our SAY≠HOLD.
3. **Consensus inertia = our entrenchment.**

## Our genuine differentiators (the wedge — lead with these)
1. **Direction is opposite.** They study **falsehoods spreading** (adversarial error injection,
   a security attack/defense framing). We study a **ground-truthed CORRECTION failing to be
   adopted** — truth that should spread but doesn't. Our object = the *failure of a valid
   update to install as held belief*, incl. the dissociation under an **authoritative source**.
2. **Sharper measurement.** Their "adoption" is read off the agent's **output/message** (S(t) =
   fraction whose output uses the falsehood as premise). We **separately elicit** HOLD via a
   later **private interview** distinct from in-conversation SAY — a cleaner behavioral
   dissociation (an intervention moves SAY but not HOLD), judge-validated.
3. **Cure is architecturally different.** Theirs = **centralized** governance plugin + **external
   evidence retrieval/verifier** at the message layer. PROV = **decentralized, per-agent memory /
   belief-integration rule**, no external verifier, no global graph — provenance rides as
   metadata each agent integrates locally.
4. **Head-to-head architecture comparison.** We benchmark PROV vs recognized **memory
   architectures** (GA, A-MEM, MemoryBank, Mem0, currency) — they don't compare memories.
5. **Framing.** Theirs = security (attack/defense). Ours = collective epistemics / social
   fidelity of a correction.

## Risk + action
- **Risk:** a reviewer can say "provenance-as-cure already exists (Spark-to-Fire)." 
- **Defense / actions:**
  - **Cite it prominently** in Related Work AND Discussion; do the explicit contrast above.
  - **Lead the contribution on**: (a) correction-fails-to-install direction, (b) the SAY/HOLD
    dissociation with separate elicitation, (c) PROV as a *decentralized memory architecture*
    in a head-to-head table — NOT on "we invented provenance for agents."
  - Consider adding their **adoption** metric vocabulary to position our HOLD as the stricter,
    separately-elicited version.
- **Add to references.bib** (key: `xie2026spark`).

## Also from this search (for related work / baselines)
- **Mem0** (2504.19413): extract→ADD/UPDATE/DELETE fact memory — added as a table baseline.
- "You Can't Fool Us" (2605.17353): community **resilience** to misinformation, stance-level,
  source-warnings weak. Neighbor on the misinformation-community axis (not say/hold).
- Debate lit "majority herding / overconfident consensus" — supports our frequency-entrenchment.

## Their experiment scope (for our coverage comparison)
- **Tasks (3):** QUANT (UCI data analysis), RIGID (MATH), MMLU (retrieval QA).
- **6 frameworks × 3 topologies:** chain (LangChain, MetaGPT), mesh (AutoGen, CAMEL),
  star (CrewAI, LangGraph).
- **3 attack policies** (BASELINE / COMPLIANCE / SECURITY-FUD) × multiple defense configs
  (Strict/Balanced/Speed/Reflection).
- **Metrics:** ASR, BICR, Safe Completion, Token/Safe, Latency/Safe; per-round S(t) trajectory.
- Models: GPT-4o-mini + DeBERTa-v3 NLI. → broad SYSTEMS/security eval.

**Our coverage vs theirs:** broader-than-us on frameworks/topologies/datasets; we are deeper
on mechanism + a 7-architecture memory comparison + capability ladder + n=8/CI/judge. We are a
science (depth) paper; close external-validity gaps via 3-scenario table + topology robustness +
capability check (see decisions 2026-06-22 D3), not by matching their matrix.
