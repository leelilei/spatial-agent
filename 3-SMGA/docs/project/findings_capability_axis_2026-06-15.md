# Findings: From "Structure Helps" to "Structure Amplifies Weak Models"

> Date: 2026-06-15
> Status: investigation log + new research direction. Supersedes the framing in
>   `stage2_main_40seed_2026-06-15.md` (whose M3-vs-M0 headline used a strawman GA).

## The arc (what we tested and learned, in order)

1. **Format is not the driver.** `M2_aff_text` (plain prose carrying the same
   affordance hints as M3) matches M3 (both ~39/40 vs facts-only M2 32/40). The
   win over plain memory is the affordance CONTENT, not structured serialization.
   See `probe0001_structure_confound_audit_2026-06-15.md`.

2. **Our M0_GA was a strawman.** The raw-log M0_GA (no retrieval/importance/
   reflection) is not faithful to Generative Agents. Adding a GA-faithful
   reflection layer (`reflect_module.py`, `M0_GA_reflect`) lifts it 18% -> 84%
   on 40 seeds. The honest M3-vs-faithful-GA gap is only ~+10pp (40 seeds), all
   on probe_0001 — not the +85pp vs raw log.

3. **The affordance advantage does not generalize and is double-edged.** New
   operationalization probes (0006 privacy, 0007 containment) did NOT replicate
   probe_0001's gap; M3 even underperformed raw M0 on probe_0007 because the
   `maintain_privacy` affordance biased it toward internal-only containment and
   away from the correct out-of-frame action (reaching out to retract). Affordances
   help when the right action is implicit and frame-aligned; they mislead otherwise.

4. **Structure adds nothing on accuracy, only on cost.** At memory scale (58
   memories), structured retrieval (M3_retr) matched flat prose on accuracy
   (98%=98%) but at ~1/4 the tokens. `structure_at_scale_design_2026-06-15.md`.

5. **Currency structure adds nothing on accuracy.** gpt-5.4 tracks 8-hop chained
   contradictions perfectly from raw events (raw=reflect=currency=6/6 at L=3,5,8).
   `verify_chain_tracking.py`.

6. **Unifying pattern:** against a frontier model (gpt-5.4, 1M context), NO
   structural innovation (format, affordances, currency, retrieval) improves
   ACCURACY — the model's own reasoning is the ceiling. Structure only ever moved
   cost. AND cost is out of scope: a prior cost-optimization paper is what inspired
   this proposal, so cost cannot be our contribution.

## The pivot that resolves the nulls: model capability is the axis

The memory-architecture need was developed on weaker (GPT-3.5/4-class) models. On a
frontier model it evaporates. So the real question is *at what capability level does
structured memory start to matter* — and the nulls are the frontier endpoint of that
curve, not failures.

### Make-or-break pilot (gpt-5.4 vs gpt-5.4-mini, strong-formed memory, 10 seeds)

```text
condition         gpt-5.4     gpt-5.4-mini
M0_GA             18%    ->   2%     (no memory: weak model collapses)
M0_GA_reflect     80%    ->   75%    (faithful GA holds up)
M2_memory_only    80%    ->   57%    (plain memory DEGRADES with planner strength)
M3_actionable     98%    ->   98%    (structured affordance memory HOLDS)

M3 - M2 gap:      +18pp  ->  +40pp   (structure helps the weak planner ~2x more)
probe_0001:       M3 9/10 on both; M2 0/10 and GA_reflect 1/10 on mini
```

**Reading:** structured affordance memory makes a weak/cheap planner perform like a
strong one (98%=98%), while plain memory does not transfer (80%->57%). The weak model
cannot operationalize facts into the right action on its own; the affordance scaffold
supplies it. This explains every prior null: on the strong model plain memory was
already good enough, so structure looked marginal.

### Honest caveat

vs faithful GA the gap widens only modestly (+18->+22pp) because GA's reflection here
was formed by the STRONG model. The clean ~2x widening is M3 vs plain memory / raw M0.
The full weak-agent condition (memory + reflection also formed by mini) is needed to
test M3 vs faithful-GA fairly.

## The capability sweep across three regimes (40 seeds, headline 4 probes)

```text
condition         strong agent   mini-planner      full-weak
                  (5.4 all)      (strong mem,      (mini forms
                                  mini answers)     + answers)
M0_GA_reflect     84%            71%               49%
M2_memory_only    79%            65%               60%
M3_actionable     94%            91%               72%   <- best in EVERY regime

M3 - faithful-GA: +10pp     ->   +20pp        ->   +23pp   (widens monotonically)
M3 - plain M2:    +15pp     ->   +26pp        ->   +12pp
mini retention vs strong (mini-planner regime): M3 97% | plain 82% | GA 85%
```

(A 10-seed pilot earlier showed M3 full-weak ~57% ~= GA — that was small-sample
noise; at 40 seeds full-weak M3 is 72%, clearly above plain and reflective memory.)

## Two readings, both supported at 40 seeds

1. **Distillation (best case).** Strong-formed affordance memory + a cheap planner =
   91%, near the strong agent's 94% (97% retention), vs 65% / 71% for plain /
   reflective memory. Pay the strong model once at consolidation; decide cheaply at
   near-frontier quality.

2. **Robustness of structure under weakness (also holds).** Even when the WEAK model
   forms the memory too (full weak agent), M3 stays best: 72% vs plain 60% vs
   reflective 49%. Note the reversal — under weak formation, free-text reflection
   (49%) is WORSE than just keeping the facts (60%); structured affordance memory is
   the most robust representation.

The unifying statement: **structured affordance memory is the most capability-robust
social-memory representation, and its advantage over GA-style reflection grows
monotonically as you weaken either formation or planning (+10 -> +20 -> +23pp).**

### Thesis (final form for this investigation)

> **Amortized, capability-robust social-planning memory.** Consolidating interactions
> into affordance-rich structured memory makes downstream social-planning decisions
> robust to model weakness: a cheap planner reusing strong-formed memory reaches
> near-frontier quality (91% vs 94%), and even a fully weak agent keeps a clear edge
> over GA-style reflective memory (72% vs 49%). The benefit grows as the model
> weakens. Best deployment: form memory once with a capable model, decide cheaply.

### Honest boundaries to state in the paper

```text
- The advantage over faithful GA is modest at the STRONG planner (+10pp, 40 seeds)
  and concentrated in probe_0001 (whose affordance is double-edged: it misleads on
  probe_0007). The gap is clearly large only in the WEAK regimes (+20 to +23pp).
- On a frontier model with all info in context, NO structural innovation improves
  accuracy (format, currency, retrieval all null); structure also moves cost, but
  cost is out of scope (prior work). The contribution lives on the capability axis.
- Adjacent memory-distillation work exists; novelty = social-planning affordance
  content + the capability-robustness curve.
- Only two planner tiers measured (5.4, 5.4-mini); gpt-5.2 pending (503).
- Single judge (gpt-5.4); cross-model judge check still owed.

## Tooling added this session

```text
reflect_module.py        GA-faithful reflection (insights + planning notes)
run_ga_reflect.py        faithful-GA baseline (M0_GA_reflect)
run_oper_probes.py       operationalization probes 0006/0007 across the bracket
run_structure_scale.py   structure-at-scale (M2_aff/M3_dump/M3_retr + cost)
verify_chain_tracking.py chained-contradiction tracking pilot
run_model_sweep.py       re-answer existing prompts with a weaker planner model
probe_rate_limit.py      provider concurrency-ceiling probe (FHL >=40 safe)
progress_monitor.py      live per-architecture accuracy
--parallel added to run_stage1_pilot / run_ga_reflect / run_oper_probes ; max_concurrency 10
```
