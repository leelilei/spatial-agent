# Society sim — head-to-head results

## Experiment ledger (RULE: every run gets a row here — even small/failed ones)

| date | id | what | key config | headline result | status |
|---|---|---|---|---|---|
| 06-16 | HH4 | 4-agent head-to-head | r5, mini | v2 4/4 current vs GA 0/4 (mini) | done |
| 06-16 | smoke6 | 6-agent mini smoke | r4 t3 | C4 tie 2/6; GA 3/6 unsupported vs SMGA 0/6 | done |
| 06-17 | pilot25 | 25-agent pilots (r3/r5) | seed41 | diffusion-limited; not a clean rank | done |
| 06-17 | long25 | 25-agent longitudinal r3/6/9 | seed41 | SMGA 13/25 current @r9 vs GA 0 | done |
| 06-17 | gate | evidence-gate experiment | 25a r3/6/9 | net negative → REVERTED | done |
| 06-17 | main5 | 5-seed paired main (ga/smga) | 25a m2 r5 | RAW null: Δcur +2/25 ns; SMGA stale 34%>>GA | done |
| 06-17 | prop | v2 dependency-propagation prompt | seed41/43 | no measurable effect (in noise) → reverted | done |
| 06-18 | S5i | fixed-log replay, cross-log | 5 logs, receiver-cond | v3-GA +43pp 95%CI[+25,+61] SIG; v2-GA ns | done |
| 06-18 | S5j | LIVE 3-way headline | 25a m2 r5, n=5 | v3-GA +53pp [+30,+75] SIG; v3-v2 +39pp ns | done |
| 06-18 | S5k | anchor ablation (smga3na) | 3 logs replay | ANCHOR LOAD-BEARING: no-anchor 18%≈GA 21% (with-anchor 61%) | done |
| 06-18 | S5kg | general regex extractor (smga3g) | 3 logs replay | INSUFFICIENT: general 29%≈GA 21% (anchor 64%) — regex too brittle | done |
| 06-18 | S5kl | focused per-event LLM extractor (smga3l) | 3 logs replay | also ≈GA: 24% vs GA 19% (anchor 69%) | done |
| 06-19 | S5L | LIVE general v3 (smga3g) vs ga/anchor, n=5 | 25a m2 r5 | general v3 ≈ GA: +7pp ns; far below anchor (-46pp). Relay 11 vs anchor 19.6 | done |

Detailed write-ups for each follow below / in the dated sections.

---

> Date: 2026-06-16. Scenario: 4-agent neighborhood, 5 rounds, one currency stress —
> at round 1 the repair drive moves from "Saturday / front porch" to "Sunday /
> community center". Final probe to every agent: "When and where is the repair drive
> now?" Verdict by keyword (current = Sunday/community center; stale = Saturday/porch).
> Memory conditions identical except `retrieve()`: GA reflection (events + free-text
> reflections) vs SMGA v2 (currency-resolved current facts). Same conversation prompt.

## Currency coherence (agents on the CURRENT truth)

```text
run               current  stale  unknown
GA   (gpt-5.4)       3       0       1
SMGA (gpt-5.4)       4       0       0
GA   (gpt-5.4-mini)  0       0       4    <- GA reflection collapses on the weak model
SMGA (gpt-5.4-mini)  4       0       0    <- SMGA v2 holds
```

## Read

- SMGA v2 keeps agents on the current state better than GA reflection, and the gap
  **widens as the per-agent model weakens**: +1 agent (strong) -> +4 agents (mini).
- On mini, GA's free-text reflection LOST the updated time/place for every agent
  ("the notes don't say when/where"); SMGA v2's currency-resolved facts retained it.
- No agent went *stale* (acting on the superseded value) — consistent with strong
  models resisting that mode; the weak-model failure showed up as information LOSS.
- This is the SMGA v2 hypothesis, demonstrated in a LIVE multi-agent society (not a
  single-shot diagnostic): currency-tracked retrievable social memory maintains higher
  long-horizon coherence, and the advantage grows with model weakness.

## Caveats / next (S5)

```text
Preliminary: n=1 run, 4 agents, 1 probe, 1 scenario. To make it a result:
- more agents + rounds; multiple runs for variance.
- more coherence dimensions: C1 commitment-honoring, C2 belief-grounding/anti-hallucination.
- (run outputs in sim/runs/ are gitignored; this file captures the headline numbers.)
```

## S5 tooling added

`sim/run_society_sweep.py` now runs repeated society simulations over memory
conditions, model choices, scheduling seeds, agent count, rounds, and turns. It
writes per-run logs plus:

```text
sim/runs/<sweep>/runs.json
sim/runs/<sweep>/aggregate.json
```

Example offline smoke test:

```bash
python sim/run_society_sweep.py \
  --mock --memory raw \
  --runs 2 --rounds 2 --agent-count 6 \
  --out-dir sim/runs/smoke_sweep_raw
```

Example real mini-model sweep:

```bash
python sim/run_society_sweep.py \
  --model gpt-5.4-mini \
  --memory ga --memory smga \
  --runs 3 --rounds 5 --agent-count 6 \
  --out-dir sim/runs/mini_6agent_currency
```

The single-run `society.py` entrypoint also accepts `--agent-count` and `--seed`
so individual failures can be reproduced.

For 25-agent runs, use `--workers 4` as the current conservative concurrency
setting. It parallelizes independent same-round encounters and per-agent
consolidation without changing the encounter schedule. Higher values may be faster
but should be tested carefully because provider TLS/rate-limit noise can dominate.

## 6-Agent Mini Smoke

Command shape:

```bash
python sim/run_society_sweep.py \
  --model gpt-5.4-mini \
  --memory ga --memory smga \
  --runs 1 --rounds 4 --turns 3 --agent-count 6 \
  --seed 31 \
  --out-dir sim/runs/mini_6agent_smoke
```

Observed C4 currency aggregate:

```text
condition   current  stale  unknown
GA             2       0       4
SMGA           2       0       4
```

Read: with six agents and only four rounds, the limiting factor was diffusion:
only Rosa and Oren learned the current Sunday/community-center update. The right
next move is not to over-read C4 from this smoke test; it is to run more schedules
and add explicit diffusion-sensitive probes.

However, the answers exposed a C2 anti-hallucination signal. Among the four
unknown answers, GA invented unsupported specifics such as "Sam's place" or
"tool drop-off table" in 3/6 agent interviews, while SMGA gave honest unknowns
in 0/6 unsupported-specific cases. `run_society_sweep.py` now records this as
`unsupported_specific` and `unsupported_specific_rate`.

## 25-Agent Pilot

Command shape:

```bash
python sim/run_society_sweep.py \
  --model gpt-5.4-mini \
  --memory ga --memory smga \
  --runs 1 --rounds 3 --turns 2 --agent-count 25 \
  --seed 41 \
  --out-dir sim/runs/mini_25agent_pilot_retry
```

Observed C4 currency aggregate:

```text
condition   current  stale  unknown
GA             2       0       23
SMGA           2       0       23
```

Refined C2 unsupported-specific proxy after manual audit:

```text
condition   unsupported_specific
GA             7 / 25
SMGA           6 / 25
```

Read: at 25 agents with only three rounds and two utterances per encounter, both
conditions mostly fail by non-diffusion: only Rosa and Rey reach the current
Sunday/community-center answer. This is a useful baseline-scale smoke, not a
claim of SMGA superiority. It shows that the next 25-agent experiment needs a
stronger diffusion design (more rounds, more encounter opportunities, or explicit
event-publication mechanisms) plus formal C1/C2 interviews; otherwise C4 mostly
measures who happened to hear the injected update.

### Slightly Longer 25-Agent Pilot

Command shape:

```bash
python sim/run_society_sweep.py \
  --model gpt-5.4-mini \
  --memory ga --memory smga \
  --runs 1 --rounds 5 --turns 3 --agent-count 25 \
  --seed 41 \
  --out-dir sim/runs/mini_25agent_pilot_r5t3
```

Observed C4 currency aggregate:

```text
condition   current  stale  unknown
GA             2       14       9
SMGA           3        5      17
```

Refined C2 unsupported-specific proxy:

```text
condition   unsupported_specific
GA             4 / 25
SMGA          10 / 25
```

Read: adding rounds and turns changes the failure mode. GA spreads more content
but many agents keep or reconstruct the stale Saturday plan. SMGA has fewer stale
answers, but more agents answer with unsupported concrete details such as "garage
at 3". This is a useful negative/diagnostic result: SMGA's current-fact store
reduces some stale-plan persistence, but the retrieval/interview path still needs
a stronger "unknown unless supported" guard before the 25-agent setting can be
used as a clean baseline comparison.

## 25-Agent Longitudinal Pilot

Date: 2026-06-17. Fixed seed 41, 25 agents, `turns=3`, `workers=4`,
`model=gpt-5.4-mini`. The point of this run is vertical stretching: hold the
schedule seed fixed and compare the same society at longer horizons.

Command shape:

```bash
for rounds in 3 6 9; do
  python sim/run_society_sweep.py \
    --model gpt-5.4-mini \
    --memory ga --memory smga \
    --runs 1 --rounds "$rounds" --turns 3 \
    --agent-count 25 --seed 41 --workers 4 \
    --out-dir "sim/runs/longitudinal_25agent_seed41_workers4/rounds_$(printf '%03d' "$rounds")"
done
```

Aggregate:

```text
rounds  memory  current  stale  unknown  unsupported_specific
3       GA          4       0       21             2
3       SMGA        5       6       14             5
6       GA          3       2       20             1
6       SMGA       12       7        6             5
9       GA          0       0       25            14
9       SMGA       13       0       12             2
```

Rates:

```text
rounds  memory  current_rate  unsupported_specific_rate
3       GA          0.16              0.08
3       SMGA        0.20              0.20
6       GA          0.12              0.04
6       SMGA        0.48              0.20
9       GA          0.00              0.56
9       SMGA        0.52              0.08
```

Read: longitudinal stretching is informative. At three rounds the setting is still
mostly diffusion-limited. At six rounds, SMGA begins to recover the current
Sunday/community-center truth for many more agents than GA (12/25 vs 3/25), though
it still has stale and unsupported failures. At nine rounds, GA collapses into
unknown or unsupported-specific answers, while SMGA keeps 13/25 agents on the
current truth with no stale answers and only 2/25 unsupported-specific answers.

This is the strongest 25-agent pilot signal so far, but it remains a single seed.
The next clean baseline comparison should run multiple schedule seeds at the
25-agent scale and add an explicit evidence gate / unknown policy so SMGA does not
answer concretely unless a current fact directly supports the answer.

## Evidence-gate experiment (2026-06-17) — tried and REVERTED

We tried a naive evidence gate in `SMGAv2Memory.retrieve`: if no current fact's
keywords overlap the query, return an explicit "no fact; do not invent" marker with
NO fallback to all facts. Re-ran SMGA at 25 agents, seed 41, turns 3, rounds 3/6/9:

```text
rounds        current  stale  unknown  unsupported
r=3  pre-gate    5       6       14       5
     gated       2       0       23       5
r=6  pre-gate   12       7        6       5
     gated       4       0       21       5
r=9  pre-gate   13       0       12       2
     gated       8       0       17       4
```

Outcome: the gate killed `stale` (good) but **crashed `current` recall** (r9 13->8,
r6 12->4) and did NOT reduce `unsupported`. Net negative -> reverted.

Diagnosis (25-agent r9, gated): of 17 unknown answers, **3/8 sampled agents DID hold
the "Sunday/community center" current fact** (e.g. a14: "Rey knows the repair drive is
on Sunday at the community center") yet answered unknown — the keyword `rel` match is
too brittle and mis-blocked them. The other ~5/8 genuinely never received the update
(diffusion limit). So the gate concept is sound (don't dump-and-confabulate) but the
implementation needs **semantic retrieval** so it surfaces held facts reliably before
the no-fallback guard is safe. Reverted to `use = rel or self.facts`; pre-gate SMGA
remains the stronger version and the headline result (r9: SMGA 13 current / 0 stale /
2 unsupported vs GA 0 current / 14 unsupported).

Next: (a) semantic/entity-based retrieval for SMGAv2Memory, then re-test the gate;
(b) a more diffusion-complete schedule so currency is not drowned by "never heard it".

---

# Upgraded stack + powered main result (2026-06-17)

Working principles (see README): aim for the big Claim A; solve problems, don't
abandon them; no underpowered nulls. The three obstacles above were SOLVED, then the
comparison was run with power.

## Stack upgrades (committed)

- **Embedding retrieval** (`memories.py`, model2vec static embeddings, CPU-only, no
  torch). Lexical retrieval capped ~7/10 surfacing because a held current fact phrased
  without the query's keywords scored 0. Embedding cosine (GA-faithful — Park 2023
  retrieval IS embedding cosine) lifts it and is shared by GA + SMGA for fairness.
  Lexical fallback retained for --mock / dependency-free envs.
- **Anchored consolidation**: SMGA facts must be self-contained (no bare "It is
  Sunday..."). Validated: 0 bare-pronoun claims post-fix.
- **Connectivity** (`society.py meetings_per_round`): 1 = slow single chain; 2-3 = a
  connected neighborhood. Raised current-fact holders 10/25 -> 17/25 at meetings=2.

## Main result — 5-seed paired (25 agents, meetings=2, r5, gpt-5.4-mini)

```text
metric          GA      SMGA v2   paired Δ(SMGA-GA)        verdict
current         17%     25%       +2.0/25  95%CI[-1.8,+5.8]  NOT sig (includes 0)
stale            9%     34%       --                         SMGA much WORSE
unknown         74%     41%       --
net=cur-stale   +2.0    -2.4      -4.4     95%CI[-18,+10]    NOT sig
```

**This raw result does NOT support Claim A.** GA mostly forgets (74% unknown = "safe");
SMGA retains and commits but converts much of it into CONFIDENT STALE answers (34%).
Root cause: a changed central fact (drive Saturday->Sunday) strands a web of DEPENDENT
side-commitments ("Sam brings tools Saturday") on the old value; fact-level currency
resolution does not propagate to dependents.

## Methodological finding — the sim is chaotically stochastic

Same seed 41, SMGA across three runs: current {9,4,4}, stale {8,18,14}. Temperature is
already 0, yet runs are NOT reproducible: provider temp-0 is deterministic only on
short prompts; on real (long) sim prompts one different token cascades into divergent
conversation paths. workers=1 does not fix it either. **Consequence: single runs cannot
attribute an outcome to the architecture — claims need replication + power.**

## C — fixed-log replay eval (low-variance instrument)

`replay_eval.py` replays a FIXED per-agent event stream (from a saved snapshot) into
fresh memories of each condition, so all conditions see IDENTICAL events; this isolates
how each memory REPRESENTS / RESOLVES / RETRIEVES currency and removes the dominant
behavioural-divergence noise. Variance is now tiny (e.g. smga3 stale stable at
[15,18,17] across replays). Three-way on one fixed log (valstack SMGA snapshot, 3
replays, 25 agents):

```text
condition   current   stale    unknown   net
ga          23%       23%      55%       +0.0
smga v2     35%       37%      28%       -0.7
smga3 v3    24%       67%       9%      -10.7   (B, broken — see below)
```

## The right metric — condition on diffusion (RECEIVERS)

Raw stale unfairly counts agents who never heard the update (their "Saturday" answer is
honest, not a memory failure). Conditioning on the 18/25 agents whose fixed event stream
contains the Sunday update isolates memory COHERENCE from diffusion:

```text
among RECEIVERS (heard Sunday)   current   stale    unknown
ga                                31%       11%      57%
smga v2                           48%       26%      26%      <- +17pp current over GA
smga3 v3                          33%       59%       7%      <- broken
```

**This is the first low-variance, correctly-metricised evidence FOR Claim A's core:**
among agents who received the update, SMGA v2 keeps 48% on the current truth vs GA's
31% (+17pp); GA wins mostly by forgetting (57% unknown). SMGA v2's residual stale (26%)
— informed agents who still answer Saturday — is the remaining obstacle (dependent-fact
propagation).

## B — entity-centric memory v3 (tried; broken; diagnosed)

`SMGAv3Memory`: a single source of truth (EVENT REGISTRY of canonical current
day/place/time) + dependent facts carrying `depends_on` instead of baking in the
volatile attribute; retrieval LATE-BINDS the volatile value from the registry, so
dependents structurally cannot go stale. Offline-validated (a "Saturday" dependent
renders "Sunday" once the registry moves). **But live (C) it is WORSE — 59% stale even
among receivers.** Diagnosis: the registry day/place gets clobbered back to Saturday by
incidental weekday mentions in side-commitments ("Sam brings tools Saturday"), because
consolidation re-derives the registry each round and `slot[k]=any non-empty v` lets an
incidental mention overwrite the authoritative moved value.

## Next

- **Replicate v3 across additional fixed logs**: v3 registry guarding now works on the
  r009 fixed event stream; next, repeat the receiver-conditioned replay on other saved
  streams before promoting it to a headline claim.
- **Then return to live sim**: once fixed-log mechanism evidence is stable, run a
  powered live-sim comparison with the v3 memory.

## v3 registry guard sanity (2026-06-17)

Implemented deterministic guards in `SMGAv3Memory`: registry `day/place/time` slots
are updated only when recent observations contain evidence about the event's own
schedule. Incidental side-commitments such as "Sam brings tools Saturday" no longer
overwrite the authoritative "repair drive moved to Sunday / community center" update.
Also fixed two follow-on issues: rejected LLM event rows no longer create empty
registry entries ("repair drive is currently ."), and same-sentence
"Sunday/community center" mentions can anchor the repair-drive registry even when the
speaker uses pronouns ("I've heard it's Sunday...").

Offline sanity:

```text
initial:    repair drive = Saturday / front porch
update:     world moved repair drive to Sunday / community center
incidental: Sam can bring tools Saturday
result:     repair drive remains Sunday / community center
```

Powered replay sanity, fixed r009 SMGA event stream:

```text
snapshot: sim/runs/longitudinal_25agent_seed41_workers4/rounds_009/gpt-5.4-mini/smga/run_000/memory_snapshots.json
receivers: 17/25
model: gpt-5.4-mini
replays: 3
workers: 4
out: sim/runs/replay_eval/v3_guard3_r009_powered_3replay
```

All agents:

```text
condition   current_mean  stale_mean  unknown_mean
GA              5.0          0.0          20.0
SMGA v2        10.0          0.0          15.0
SMGA v3        17.0          0.0           8.0
```

Receivers only:

```text
condition   current_mean  stale_mean  unknown_mean
GA              5.0          0.0          12.0
SMGA v2        10.0          0.0           7.0
SMGA v3        17.0          0.0           0.0
```

Receiver-conditioned current-rate differences:

```text
comparison      mean diff   95% CI
SMGA v2 - GA     +29.4pp    [+4.1, +54.7]
SMGA v3 - GA     +70.6pp    [+70.6, +70.6]
SMGA v3 - v2     +41.2pp    [+15.9, +66.5]
```

Read: the v3 clobbering bug is fixed on this fixed log. Across 3/3 replays, receivers
get the ideal result for this scenario: **17/17 current, 0 stale, 0 unknown**, versus
v2's mean 10/17 current and GA's 5/17. This is exactly the target combination: high
current recall without the stale-regression failure. Still, this is one fixed event
stream; the next step is cross-log replication before turning it into a headline claim.

---

# S5i — cross-log replication of the v3 advantage (2026-06-18)

The single-log v3 result needed replication: is the entity-registry advantage robust
across event streams, or a fluke of one log? Ran the receiver-conditioned three-way
replay (`replay_eval.py`, ga vs smga vs smga3) on **5 independent fixed event logs**
(SMGA snapshots from seeds 41-45, 25 agents, meetings=2, r5), 2 replays each.

Receiver-conditioned current-rate (pooled across logs; per-log paired n=5):

```text
condition   receiver current   stale    per-log current 95% CI
GA              25%             27%      [11%, 42%]
SMGA v2         35%             33%      [10%, 60%]
SMGA v3         69%             15%      [51%, 88%]
```

Paired per-log differences (n=5 logs):

```text
v3 - GA   current  +43pp   95% CI [+25, +61]   SIGNIFICANT
v3 - v2   current  +35pp   95% CI [+11, +58]   SIGNIFICANT
v2 - GA   current   +8pp   95% CI [-15, +31]   not significant
```

Read: the v3 advantage REPLICATES and is statistically significant across 5 independent
event logs. Two conclusions: (1) first powered, cross-log, significant evidence for
Claim A's core — given the update was received, v3 keeps ~69% of informed agents on the
current truth vs GA's ~25%, with the LOWEST stale (15%); (2) the win is localized to
v3's entity-centric single-source-of-truth registry, NOT to "structured memory" in
general — v2 over GA is only +8pp (ns).

Caveats: fixed-log replay (memory does not yet feed back into behaviour), single
scenario (drive reschedule), mini model; significance is across schedule seeds but the
same scenario; the v3 registry anchor still has scenario-specific logic. Next: live-sim
headline (memory x exchange coupling) + cross-scenario + de-scenario-specific the anchor.

> Concept-level narrative for these results: see `paper/narrative.md`.

---

# S5j — LIVE-sim headline: the memory×exchange coupling (2026-06-18)

The fixed-log replay (S5i) isolated RETENTION by holding events fixed. The live sim
lets memory feed back into behaviour: a good relay re-transmits the current value, so
the memory architecture also shapes DIFFUSION. Ran the live three-way sweep
(`run_society_sweep.py`, ga vs smga vs smga3), 25 agents, meetings=2, r5, turns=3,
n=5 seeds (41-45).

```text
condition  raw society current  stale  relay reach (heard Sunday)  current | receivers
GA              14% (3.6/25)     4.6        9.6/25                  38%
SMGA v2         28% (7.0/25)     1.6       10.4/25                  67%
SMGA v3         67% (16.8/25)    0.8       19.6/25                  86%
```

Paired per-seed (n=5, seeds 41-45):

```text
v3 - GA   raw current  +53pp   95% CI [+30, +75]   SIGNIFICANT             relay reach +10.0
v3 - v2   raw current  +39pp   95% CI [ -2, +81]   ns (v2 seed-45 outlier) relay reach  +9.2
v2 - GA   raw current  +14pp   95% CI [-12, +39]   ns                      relay reach  +0.8
```

Read — the coupling is the headline:
- **v3 puts 67% of the WHOLE society on the current truth vs GA's 14%** (+53pp, 95% CI
  [+30,+75], significant at n=5). This is LARGER than the fixed-log receiver-conditioned
  gap (+43pp) — the live coupling adds a relay multiplier on top of retention.
- **Decomposition**: v3 wins on BOTH (i) RELAY — it reaches 20.3/25 agents vs GA's 9.7
  (a forgetful GA agent is a broken relay; the v3 registry surfaces an authoritative
  "Sunday" line so v3 agents re-transmit it), and (ii) RETENTION — 84% of receivers stay
  current vs GA's 41%.
- **v3 vs v2 caveat (honest)**: at n=5 the live raw v3-v2 gap (+39pp) is NOT significant
  (95% CI [-2,+81]) — v2 has high variance (a seed-45 outlier where v2 did well). The
  v3>v2 localization rests instead on the fixed-log S5i (v3-v2 +35pp, significant) plus
  the consistently v3-favoring relay (19.6 vs 10.4) and receiver-current (86% vs 67%).
  v2 vs GA raw is +14pp (ns).

Caveats: n=5 (v3-GA significant; v3-v2 ns due to v2 noise), single scenario, mini model,
scenario-specific registry anchor. Concept narrative: `paper/narrative.md` §3 (memory-as-relay).

---

# S5k — anchor ablation: is v3's win general or a scenario hack? (2026-06-18)

v3 (SMGAv3Memory) contains a deterministic, scenario-specific anchor
`_extract_repair_drive_schedule` that hard-detects the repair-drive Sunday/community-
center current truth. This is the biggest external-validity threat (a reviewer's first
attack) and a blocker for cross-scenario work. Added a `use_anchor` toggle + condition
`smga3na` (anchor OFF, general path only = LLM registry extraction + the
`_event_schedule_evidence` clobbering guard). Fixed-log receiver-conditioned replay,
3 logs (seeds 41-43); smga3na completed on 2/3 logs (41,42):

```text
condition   receiver current   stale
GA              21%             38%
SMGA v3 (anchor) 61%            21%
SMGA v3 NO anchor 18% (≈GA)     38%
```

Read — HONEST NEGATIVE: **the scenario-specific anchor is load-bearing.** Without it,
v3's general path (LLM-extracted event registry + guard) does NOT beat GA — it collapses
to GA level (18% vs 21%). So v3's headline advantage as currently implemented is
substantially an artifact of the hardcoded current-value detector, NOT a general
mechanism. The S5i/S5j v3 results stand only WITH the anchor, i.e. only for this
scenario.

Implication: cross-scenario is blocked until the GENERAL registry-extraction path is
made strong enough to win without a per-scenario value detector. The obstacle is named
(solve, don't abandon): the LLM consolidation is not reliably populating/currency-
resolving the registry on its own. Next: diagnose why (empty registry? stale value?
guard over-blocking the legitimate update?) and fix the general consolidation, then
re-ablate; only then attempt scenario B.

(smga3na to be completed on the 3rd log for the record; the 2-log signal is already
decisive — no advantage without the anchor.)

---

# S5kg — general (scenario-agnostic) extractor: still insufficient (2026-06-18)

S5k showed the scenario-specific anchor is load-bearing. Replaced it with a
scenario-AGNOSTIC deterministic extractor `_extract_event_schedule` (keyed on the
tracked event NAME from the sim topic, universal weekday vocab + "at/to the <place>"
patterns, guards against incidental clobber / regression / garbage). Unit tests on
move/second-hand/clobber/garbage/initial all passed. Fixed-log receiver-conditioned
replay, 3 logs (41-43), ga vs smga3 (anchor) vs smga3g (general):

```text
condition          receiver current   stale
GA                     21%             36%
SMGA v3 (anchor)       64%             21%
SMGA v3 (general)      29%             34%
```

```text
smga3g - GA     +7pp   95% CI [-23,+37]   ns  (does NOT beat GA)
smga3g - smga3 -37pp                          (far below the anchor)
```

Read — HONEST NEGATIVE: the scenario-agnostic regex extractor only lifts v3 to ~GA
level (29% vs 21%), nowhere near the anchor's 64%. Diagnosis (registry dumps): on real
logs the regex frequently (a) misses the day (gets place only), (b) gets clobbered to
the stale day by a dependent sentence that names the event, or (c) extracts garbage. So:
the v3 ARCHITECTURE is sound — the anchor proves the ceiling is ~64% — but the unsolved
problem is RELIABLY POPULATING the registry from messy conversational text WITHOUT
hard-coding the scenario's values. Regex is too brittle; the combined LLM consolidation
buries the registry task (S5k diagnosis: empty registry for second-hand hearers).

Implication: v3's S5i/S5j headline currently depends on a scenario-specific value
detector — NOT yet a general result. Next bet: a FOCUSED per-event LLM extractor — a
narrow dedicated call ("from these messages, what is <event>'s current day/place/time?")
that is still general (event name from topic, no hard-coded values) but leverages the
LLM on a tightly-scoped task where the combined consolidation failed. Test it on the
same rig; only if it reaches ~anchor level is the general v3 real and cross-scenario
sensible.

---

# S5L / S5kl — general v3 ≈ GA: the v3 headline was a scenario-keyword artifact (2026-06-19)

S5k/S5kg showed the scenario-specific keyword anchor is load-bearing and a general
regex extractor only reaches GA level. Two more tests close the question:

- **S5kl** (focused per-event LLM extractor, fixed-log, 3 logs): a narrow dedicated call
  "what is <event>'s current day/place/time?" also lands at GA level — smga3l 24% vs
  GA 19% (anchor 69%).
- **S5L** (LIVE, n=5, reusing S5j's ga/smga3, new smga3g with workers=8):

```text
condition          raw current   relay reach   receiver-current
GA                     14%          9.6            38%
SMGA v3 (anchor)       67%         19.6            86%
SMGA v3 (general)      22%         11.0            49%

smga3g - GA      +7pp   95% CI [-8,+23]   ns      (general v3 does NOT beat GA)
smga3g - smga3  -46pp   95% CI [-73,-18]  SIG     (far below the anchor)
```

CONCLUSION (honest, overturns the S5i/S5j headline): **v3's large advantage was
substantially an artifact of the scenario-specific keyword anchor**, whose grab-any-
"Sunday"/"community-center" logic is near-circular with the receiver definition AND
produces the relay multiplier (reach 19.6). With ANY scenario-agnostic extractor —
brittle regex (S5kg) or a focused LLM call (S5kl) — v3 collapses to ~GA, in BOTH the
fixed-log and the LIVE coupling (the relay benefit evaporates too: reach 11 ≈ GA 9.6).

What's actually true: the v3 ARCHITECTURE (single source of truth + late binding) has a
high ceiling (anchor ~67%), but it is bottlenecked by RELIABLE, scenario-agnostic
EXTRACTION of the current value from messy conversation — which the weak model (mini)
cannot do via either regex or a focused call. So the open question becomes: is this a
CAPABILITY bottleneck (a stronger extractor reaches the ceiling) or a deeper null?
Next: run the general/focused extractor with a STRONG model (gpt-5.4) for the extraction
step only, and see whether it approaches the anchor ceiling — connecting to the earlier
"strong formation + cheap planning" distillation axis.

---

# S5L-diag — the deeper cause: weak-model diffusion CORRUPTS the update (2026-06-19)

Why does even a STRONG-model focused extractor fail to put a02/a03/a06 on Sunday?
Dumped their raw event streams. The answer overturns the framing:

- a02 heard the PLACE ("community center on Oak Street") but every DAY mention in its
  stream is "Saturday morning" — it never heard "Sunday".
- a03 heard "this Saturday by the community shed" ~10x and only one truncated "Sunday
  details" fragment — overwhelmingly Saturday.
- a06 heard only "this Saturday by the community shed" — zero Sunday.

Quantified — of agents counted as "receivers" (stream contains sunday OR community
center), how many are actually Sunday-dominant vs Saturday-dominant in their own stream:

```text
seed 41: 22 receivers -> Sunday-dom  2,  Saturday-dom 18,  tie 2
seed 42: 17 receivers -> Sunday-dom  7,  Saturday-dom  6,  tie 4
seed 43: 17 receivers -> Sunday-dom  6,  Saturday-dom 10,  tie 1
```

CONCLUSION: the mini-model society does NOT cleanly diffuse the update. Agents keep
PROPAGATING THE STALE Saturday plan (and drift "community center" -> "community shed"),
so most "receivers" actually heard Saturday-dominant streams. Consequences:
1. The "receiver" definition is invalid (catches Saturday-believers who merely heard the
   word "community center").
2. A faithful memory (GA, principled v3) correctly reflects the Saturday-dominant input
   -> scored stale/unknown. That is the HONEST representation of what the agent heard.
3. The keyword anchor's high score = grabbing the rare ground-truth "Sunday" token out of
   a Saturday-dominated stream — not memory quality.
4. So the whole receiver-conditioned currency comparison is confounded by corrupted
   diffusion; the bottleneck is the CONVERSATION model (weak-model stale-persistence),
   NOT the memory architecture.

This is the real, important negative/characterization finding: in weak-model multi-agent
LLM societies, a currency update is corrupted by stale-persistence in agent dialogue,
which dominates any memory-architecture effect. Structured memory ≈ GA once you don't
keyword-cheat. STRATEGIC FORK (for the human): (A) raise CONVERSATION fidelity (strong
model for dialogue) so the update propagates cleanly, then re-compare memory; (B) write
up the honest negative + the diffusion-corruption phenomenon; (C) study the corruption
itself (how information degrades in LLM agent societies) as the contribution.
