# When Truth Loses Its Source: Provenance-Aware Memory for Socially Distributed Agents

> Draft v1 (2026-06-26). Assembled from `narrative.md`, `introduction.md`,
> `measurement_grounding.md`, `sections/discussion.md`, and the `figure_guide.md` /
> `RESULTS.md` data. Figures are in `figures/`; numbers trace to the RESULTS.md ledger.
> Anonymized AAAI-style draft. Citations are placeholder `(Author Year)` / bib keys.

## Abstract

LLM agents increasingly coordinate by talking to one another, and prior work shows that
information *spreads* through agent societies. We ask a reliability question that spread does
not answer: when a ground-truthed fact changes, does the society come to **hold** the new
truth, or merely **say** it? Using a social-fidelity probe that separately measures what agents
hear, say, and later hold, we find a robust **speech–belief dissociation**: an authoritative
source makes agents utter the current value while their held belief stays at baseline. The
failure is not fixed by model capability, connectivity, memory swaps, richer personas, or a
persistent source; only direct broadcast — an overwrite control — works. The mechanism is
**path-dependent entrenchment**: the version established early and broadly wins. We then show
the repair is a specific architectural locus — integrating heard claims by **provenance**
(source + version) rather than frequency. Provenance-aware memory (PROV) is the only memory
architecture that lifts held truth, and it survives across scenarios, fact types, topologies,
and model families (gpt-5.4-mini and DeepSeek-V4-Flash, n=8). Hardened into an **auditable
architecture (APM)** with origin anchoring, corroboration, and abstain, it remains the only
architecture that survives an adversarial liar (zero hijack vs PROV's collapse) and settles to
a realistic, non-saturating equilibrium under sparse communication, never confidently wrong.

---

## 1. Introduction

A true update can become unreliable without ever becoming intentionally false. In human
societies a message may be accurate when first announced, but after several retellings people
remember the content while losing track of who said it, when it was updated, or whether it
superseded an older version. This is the telephone-game failure: the social channel does not
merely transmit content, it also drops source, timing, and authority cues.

LLM-agent societies reproduce this familiar social failure in an instrumented setting. Unlike
human rumor chains, an agent society lets us observe every utterance, every injected update,
every memory snapshot, and every final answer. This lets us separate three objects that are
usually conflated:

- **Reach** — whether the current update appears in the social transcript;
- **Speech** — whether agents later utter the current value;
- **Held answer** — whether agents answer with the current value when probed after transmission.

Generative-agent work establishes that information can spread through an agent society
(Park et al. 2023; CAMEL; AutoGen; SOTOPIA). That is not the same as showing the spread is
faithful. A correction, schedule change, or policy update can reach the conversation stream
while failing to become the society's later answer. Our central empirical pattern is that reach
and speech can improve **without** durable held truth — so "information spread" is not enough as
an evaluation target for agent societies.

We make three contributions. **(1) A measurement shift:** a social-fidelity probe that separates
heard, said, and held. **(2) A diagnosis:** a speech–belief dissociation driven by path-dependent
entrenchment; no natural lever repairs it. **(3) A cure and an architecture:** integrating by
provenance rather than frequency is the lever that works, and hardened as APM it is the only
memory architecture that stays interpretable, survives an adversarial liar, and gives a realistic
non-saturating equilibrium.

The working hypothesis: *truth decays not merely because content changes, but because content
loses its source.* Without source/version, "Saturday at the porch" and "Sunday at the community
center" compete as undifferentiated text, and the old value can win because it was established
early, repeated often, or retrieved more easily. Provenance changes the social state
representation: agents can ask not only "what have I heard?" but "who said it, is it the latest
authoritative version, does it supersede the old one?"

---

## 2. Related work

**Agent societies and communicative agents.** Generative Agents, CAMEL, AutoGen, and SOTOPIA
establish the setting: agents talk, remember, coordinate, and simulate social environments. We
ask a missing reliability question inside that setting — fidelity of a *changing* held fact.

**Misinformation, rumor, reach vs fidelity.** Rumor and continued-influence work distinguishes
spread from truth and shows corrections often fail to displace stale beliefs
(Lewandowsky et al. 2012; Thorson 2016). LLM-agent rumor simulations are close neighbors but
typically measure propagation or vulnerability; we measure held-fact fidelity after a truth
change. The closest concurrent neighbor (*From Spark to Fire*, Xie et al. 2026) also studies
provenance-style cures and adoption-vs-repetition; we lead on the explicit SAY/HOLD dissociation
(separately elicited), a decentralized-memory comparison, and adversarial robustness.

**Factuality and measurement.** Treating truthfulness as a semantic behavioral target rather than
surface fluency is standard (TruthfulQA; SelfCheckGPT, Manakul et al. 2023; semantic entropy,
Farquhar et al. 2024). Our three-way verdict mirrors fact-verification (FEVER, Thorne et al. 2018)
and knowledge-editing efficacy-vs-locality (ROME, Meng et al. 2022; MEMIT, Meng et al. 2023).

**Memory, correction, recursive degradation.** Memory systems (Mem0, A-MEM, MemoryBank) explain
why exposure is not retention; belief-revision and truth-maintenance (AGM, Alchourrón et al. 1985;
Doyle 1979) and source-credibility opinion dynamics (DeGroot 1974) motivate provenance; and
model-collapse work (Shumailov et al. 2023) provides an analogy for recursive degradation — but
ours is communication-time degradation, not training-time collapse.

---

## 3. Method: the social-fidelity probe

**Setup.** A society of 25 LLM agents on a contact graph organizes an event. At round 1 the
event's time and place **change** from a stale value (A) to a current value (B); the update is
injected into a single source agent. Agents then meet pairwise over rounds (`meetings` per
agent per round controls connectivity), converse, store what they hear, and retrieve memory to
condition later utterances. We log every utterance (SAID) and, at the end, privately interview
every agent about the current fact (HELD). Inject → Propagate → Measure.

**The current / stale / unknown verdict.** Because the fact's truth value changed, we classify
each held answer three ways, mirroring recognized structures (Table caption): **current** (holds
the new value; edit *efficacy*, SUPPORTED), **stale** (holds the superseded value; *locality*
failure / continued-influence), **unknown** (holds neither; retention failure / NOT-ENOUGH-INFO).
The three-way split is load-bearing: distinguishing *stale* (active corruption) from *unknown*
(information loss) is essential, because interventions act on them differently — capability turns
loss into confident corruption (§4.3). A semantic LLM judge reproduces the keyword verdict
(99–100% agreement), so the categories are not a keyword artifact.

**HEARD / SAID / HELD.** The probe's power is separating what reaches an agent, what it utters,
and what it later holds. Held belief is operational: the answer an agent gives when probed; we do
not claim access to literal mental states.

---

## 4. Results

### 4.1 Social fidelity decays; no natural lever repairs it

In the core task the current value reaches the conversation stream but does not reliably become
the society's held answer. Over a long horizon (M5), current truth can rise early, peak near
round 6, then decay toward a low steady state by round 30 — truth can appear transiently and
still lose; the r5 snapshot slightly overstates retention.

Figure 1 and Table 1 rule out every intuitive repair. Capability (16→21% across
mini→gpt-5.4→gpt-5.5), connectivity (roughly neutral after the powered rerun; the early
"connectivity amplifies corruption" cell was an underpowered outlier and is retracted), a memory
swap (the apparent smga3g rescue did not replicate), thick Park-style personas, and a persistent
authoritative source all leave held truth at the ~14–21% baseline. Only broadcasting the current
value into **every** agent succeeds (99%) — an overwrite-style positive control that bypasses
social transmission, not a social cure. The claim is not that agents cannot output the truth;
they can. It is that ordinary social communication does not reliably install it as held belief.

![Figure 1. Failed natural levers.](figures/fig_failed_levers.png)

*Table 1 — failed-lever evidence ledger.* capability mini→gpt-5.5: 16→21% (ns); connectivity:
ratio ~0.8–1.1 (neutral); memory GA vs smga3g: Δ≈0 (ns); persona thin vs thick: 12 vs 14% (ns);
source: Δ+0.8 (ns); broadcast: +21.8 (sig) → 99%.

### 4.2 Speech is not belief

Figure 2 is the centerpiece. Separating SAID (final-round utterances) from HELD (private
interviews) reveals a dissociation: under a persistent authoritative source, agents increasingly
**say** the current value (SAID 25→83%) while their **held** belief stays at baseline (≈15%).
Only broadcast moves both (99/99). Reach is not belief — a fact can be visible in the log while
failing as held state.

![Figure 2. Speech is not belief (SAY/HOLD dissociation).](figures/fig_say_vs_hold.png)

*Table 2 — HEARD→SAID→HELD.* baseline said 25 / held 14; source said 83 / held 15 (the gap);
broadcast said 99 / held 99. The source row's high-SAID, low-HELD is the dissociation. The
pattern replicates across three scenarios (G1) and survives thick personas (G2).

### 4.3 The mechanism is entrenchment, not recency

If recency drove belief, a late all-agent broadcast just before the probe should work; if it
were mere repetition, a single early all-agent broadcast should fail. The opposite happens
(Figure 3): an early (round-1) all-agent correction succeeds (100%) while an identical late
(round-5) one fails (0%). The governing factor is whether the truth becomes the early, broad
version that later conversation reinforces. The stale value begins with incumbent advantage;
narrow or late correction can be uttered without taking over the society's held state. We call
this **path-dependent entrenchment**.

![Figure 3. Entrenchment, not recency.](figures/fig_entrenchment.png)

### 4.4 The cure: integrate by provenance, not frequency

The diagnosis points to a specific repair. Decay arises because integration is by
frequency/majority, so the stale incumbent wins. We integrate instead by **provenance**: each
claim carries a version (origin round) as conversation metadata; an agent holds the highest
version it has *heard* and re-broadcasts that versioned belief. The latest authoritative version
thus supersedes the frequent older one. This is **fair**, not broadcast in disguise: PROV does
not overwrite agents — the current value must still be heard via conversation, and an agent that
never hears it stays stale/unknown. PROV only changes how an agent integrates and relays what it
locally hears. It is principled: it negates the diagnosed mechanism, is normatively correct for a
changing fact (frequency is the wrong cue), and instantiates truth-maintenance / belief-revision
(Doyle 1979; AGM) and source-weighted opinion dynamics (DeGroot 1974) in the social channel.

Figure 4 compares PROV against recognized memory architectures under one harness. Raw (14),
Mem0 (18), A-MEM (19), GA (22), GA-curr (25), and MemBank (25) all fail; only PROV lifts held
truth (57%). The decisive lever is the listener-side **integration rule**, not a bigger memory.

![Figure 4. Architecture comparison — only PROV lifts held truth.](figures/fig_architecture.png)

The cure is not a single-condition artifact (Table 4): PROV wins across three scenarios (C8),
a numeric fact change (C9, dues $40→$60), and contact topologies (C10), with the margin growing
on harder structured networks (ring GA6/PROV68; smallworld GA10/PROV83).

### 4.5 The cure survives capability

Figure 5 repeats the comparison on a different model family (DeepSeek-V4-Flash) at full power
(n=8). GA is statistically flat-and-failing across models (mini 21.5%, DeepSeek 15.5%, CIs
overlapping), while PROV wins on both (57% / 64%) with CIs disjoint from GA. The cure survives
capability — the symmetric counterpart of "the phenomenon survives capability" (§4.1).

![Figure 5. Capability check (n=8) — the cure survives a model-family change.](figures/fig_capability_c14.png)

### 4.6 From lever to architecture: APM

Naive PROV identifies the right lever but is not yet a deployable architecture: it adopts the
highest version blindly (a liar can claim version 999 and hijack the society) and carries only a
version, not an auditable chain. We harden it into **APM (Auditable Provenance Memory)** by adding
three guards, each fixing one weakness: **origin anchoring** (an `auth` flag minted only at the
source and relayed faithfully — unauthenticated forgeries are rejected); **chain corroboration**
(commit a value only after K *independent* sources, counting paths not value-frequency — the fix
for the failure mode where systematic garble corroborates the stale value); and **abstain** (hold
*unknown* until the bar is met). Every committed belief carries a complete source→version→path
trace, making it auditable — something black-box memories cannot provide.

Without an adversary APM ≈ PROV (interpretability is nearly free; ~64% on DeepSeek, with 60–76%
of agents holding a fully traceable belief). Its reason to exist appears under attack (Figure 6).
A liar that broadcasts a forged high-version stale claim collapses PROV from 57% to 33% and
hijacks 43/75 agents (stale 57%), while APM is unmoved (64%) with **zero hijack (stale 0)** — its
origin anchoring rejects the forgery society-wide. Without an adversary the two are equivalent;
with one, only APM stands.

![Figure 6. Adversarial liar — only APM survives (stale=0).](figures/fig_apm_adversarial.png)

*Table 3 — architecture comparison incl. APM (held-current / auditable / under-liar).* Raw 14,
Mem0 18, A-MEM 19, GA 22, GA-curr 25, MemBank 25 — none auditable; PROV 57, half-auditable
(version only), collapses to 33% (stale 57%) under a liar; **APM ≈PROV (64%), fully auditable,
holds 64% (stale 0) under a liar.** (held-current mini/n=8 for recognized memories; APM
no-adversary measured on DeepSeek; under-liar column mini/C16.)

### 4.7 APM does not saturate

A natural worry is that any sticky provenance memory floods to 100%. That ceiling is a
communication-model artifact (every-utterance lossless broadcast), not a property of provenance
integration. Figure 7 sweeps communication density (how often agents actually mention the fact).
APM traces a smooth, fully monotonic S-curve: held-current rises from 11% (mention 0, only the
source knows) to 87% (0.25–0.3) and reaches 100% only at the unrealistic dense limit (0.5+). The
40% sparse-end value is an honest floor, not a ceiling. Crucially **stale stays 0 at every
density**: under hard sparse comms no method spreads truth widely (the breadth advantage over GA
narrows), but APM guarantees the informed are never misled, which GA does not. Safety is
independent of how well truth spreads.

![Figure 7. APM communication-sufficiency curve (n=5) — non-saturating, stale≡0.](figures/fig_apm_comms_curve.png)

---

## 5. Discussion and limitations

**What we claim.** Social truth maintenance requires preserving provenance. PROV shows the value
of provenance-aware memory; the failure of every other lever shows the repair is a specific
locus (listener-side integration), not capacity. APM shows that provenance can be hardened into
an interpretable, adversary-resistant, non-saturating architecture.

**Is structured PROV cheating?** This is the central reviewer risk. PROV is **not** broadcast: it
still requires propagation through meetings, only benefits agents the update reaches, and is
weakened by loss, garble, sparse mention, horizon, and topology (C5-stress, C7, C10). But it is
also **not** fully naturalistic — it assumes source/version survives the relay as structured
metadata, so it is best framed as an idealized protocol / upper bound. A companion result
(PROV-text) shows ordinary LLM dialogue does **not** spontaneously preserve source/version, while
an explicit attribution norm can repair held truth (a text-only upper bound, visibly
protocolized). The honest engineering lesson: agent societies may need not larger memories but
**social-memory interfaces that preserve provenance through communication**.

**We did not invent provenance.** The contribution is not the idea of provenance (a classic
TMS/belief-revision idea) but: (i) demonstrating that default decentralized agent memories
systematically lose it, (ii) localizing the repair to the integration rule, (iii) quantifying it
via the SAY/HOLD dissociation, and (iv) hardening it into an auditable, adversary-tested
architecture.

**Limitations.** All experiments are simulations; "held belief" is operational. APM's headline
cells are n=3–5 pilots (vs the diagnosis and capability check at n=8); its breadth advantage over
GA under sparse comms is suggestive (overlapping CIs) while its safety advantage (stale 0 vs 30)
is decisive. APM's corroboration knob K trades flood (K=1, PROV-like) against over-conservatism
(K≥2 deadlocks without relay-before-commit), and value fidelity remains a dependency (heavy garble
still degrades it). Individual **forgetting** is deliberately disabled here so that the failure is
attributable to the integration rule, not memory loss; whether forgetting could itself *thaw*
entrenchment is a sequel question.

**Human-society reading.** The telephone effect is not always a defect — for descriptive social
simulation, selective absorption and provenance loss are features. The normative claim is
narrower: when agent societies must maintain a changing fact for reliable coordination, human-like
telephone effects become an engineering risk.

---

## 6. Conclusion

In a society of LLM agents, a ground-truthed update can be *said* without being *held*: authority
moves speech but not belief, and the version established early and broadly entrenches. No natural
lever repairs this. The repair is a specific architectural locus — integrate heard claims by
provenance, not frequency — and it holds across scenarios, fact types, topologies, and model
families. Hardened into APM, provenance integration becomes interpretable by construction, the
only architecture that survives an adversarial liar, and a realistic non-saturating equilibrium
that is never confidently wrong. Reach is not belief; for agent societies that must track changing
facts, faithfully carrying source and version is the difference between saying the truth and
holding it.

---

## References (key bib keys — see `latex/references.bib`)

park2023generative · CAMEL · AutoGen · SOTOPIA · xie2026spark (From Spark to Fire) ·
thorne2018fever (FEVER) · meng2022rome (ROME) · meng2023memit (MEMIT) ·
lewandowsky2012misinformation · thorson2016belief · manakul2023selfcheckgpt ·
farquhar2024detecting · doyle1979truth (TMS) · alchourron1985logic (AGM) ·
degroot1974reaching · shumailov2023curse (model collapse) · chhikara2025mem0 (Mem0) · A-MEM · MemoryBank.
