# Said, Not Held: The Speech–Belief Dissociation in LLM Agent Societies and the Integration Rule That Repairs It

> **Draft v2 (2026-07-06; post-audit surgery).** Supersedes `draft_v1.md` per
> `../docs/project/harvest_plan_2026-07-06.md`. Changes: (a) §4.3 entrenchment + Fig 3 EXCISED
> (P1-rec retracted, see `../docs/project/p1_rec_audit_2026-06-30.md`); replaced by the P1-mech
> exposure probe; (b) title/abstract/intro reframed from provenance-as-headline to the
> combination arc (see `../docs/project/red_ocean_audit_2026-07-06.md`: encircled, not occupied);
> (c) related work rebuilt on the 11 first-hand-verified neighbors with precise-scope contrasts;
> (d) figures/tables renumbered (old Fig 4–7 → Fig 3–6). Numbers trace to the RESULTS.md ledger.
> Anonymized AAAI-style draft. New citations carry placeholder bib keys — references.bib sync
> pending (LaTeX pass).

## Abstract

LLM agents increasingly coordinate by talking to one another, and a growing body of work shows
that information *spreads* through agent societies. We ask a reliability question that spread does
not answer: when a ground-truthed fact changes, does the society come to **hold** the new truth,
or merely **say** it? With a social-fidelity probe that separately measures what agents hear, say,
and later hold, we find a robust **speech–belief dissociation**: an authoritative source drives
agents to utter the current value (83% of final-round utterances) while their held belief stays at
baseline (15%). No natural lever fixes this — not model capability, connectivity, memory swaps,
richer personas, or a persistent source; only direct broadcast, an overwrite control, succeeds.
Exposure alone does not explain the failure: held truth rises with the fraction of current-value
mentions an agent hears, yet conditions with near-identical exposure produce opposite outcomes.
In a matched-event replay that freezes every agent's received stream, provenance-aware integration
still lifts held truth from 32.0% to 60.5% (paired +28.5 points [21.5, 35.5], n=8), establishing
listener integration as a causal locus. Changing that rule —
integrate by source and version rather than by frequency — is the only memory-architecture change
that lifts held truth in a seven-architecture head-to-head, and it holds across scenarios, fact
types, topologies, and model families (gpt-5.4-mini and DeepSeek-V4-Flash, n=8). Hardened into an
**auditable architecture (APM)** with origin anchoring, corroboration, and abstain, it remains the
only architecture that survives an adversarial liar (zero hijack, against the naive rule's
collapse) and settles to a realistic, non-saturating equilibrium under sparse communication —
never confidently wrong. In one controlled society we thus deliver the full arc: a measurement
(hear/say/hold separated), a diagnosis (speech moves without belief; integration is the locus),
and a repair (an integration rule, hardened into an auditable architecture).

---

## 1. Introduction

A true update can become unreliable without ever becoming intentionally false. In human societies
a message may be accurate when first announced, but after a few retellings people keep the content
while losing track of who said it, when it was updated, and whether it superseded an older version.
This is the telephone-game failure: the social channel does not merely transmit content, it also
drops source, timing, and authority cues.

LLM-agent societies reproduce this failure in an instrumented setting. Unlike a human rumor chain,
an agent society exposes every utterance, every injected update, every memory snapshot, and every
final answer — letting us separate three objects that are usually conflated:

- **Reach** — whether the current update appears in the social transcript;
- **Speech** — whether agents later utter the current value;
- **Held answer** — whether agents answer with the current value when probed after transmission.

Generative-agent work establishes that information can spread through an agent society
(Park et al. 2023; Li et al. 2023; Wu et al. 2023; Zhou et al. 2024). Spread, however, is not
fidelity. A correction, schedule change, or policy update can reach the conversation stream yet
fail to become the society's later answer. Our central finding is that reach and speech improve
**without** durable held truth — so "information spread" is not a sufficient evaluation target for
agent societies.

We make three contributions. **(1) A measurement shift:** a social-fidelity probe that separates
heard, said, and held — elicited separately, per agent, inside one natural-dialogue society.
**(2) A diagnosis:** a robust speech–belief dissociation that no natural lever repairs, localized
by an exposure probe to the listener-side **integration rule**: what agents hear matters, but
near-identical exposure yields opposite outcomes, and matched-event replay confirms that changing
listener integration changes held truth under fixed received evidence. **(3) A cure
and an architecture:** integrating by provenance rather than frequency is the one memory change
that works in a seven-architecture head-to-head, and hardened as APM it is the only architecture
that stays interpretable, survives an adversarial liar, and yields a realistic non-saturating
equilibrium. The contribution is the arc, measured end-to-end in a single controlled society —
not any one link in isolation.

Our working hypothesis is that *truth decays not merely because content changes, but because content
loses its source.* Stripped of source and version, "Saturday at the porch" and "Sunday at the
community center" compete as undifferentiated text, and an agent has no principled way to prefer
the later authoritative version over the more familiar one. Provenance changes the social state
representation: an agent can ask not only "what have I heard?" but "who said it, is it the latest
authoritative version, and does it supersede the old one?"

---

## 2. Related work

**Agent societies and communicative agents.** Generative Agents (Park et al. 2023), CAMEL
(Li et al. 2023), AutoGen (Wu et al. 2023), and SOTOPIA (Zhou et al. 2024) establish the setting:
agents talk, remember, coordinate, and simulate social environments. We pose a missing reliability
question within it — the fidelity of a *changing* held fact. Methodologically, our agents are never
instructed to relay accurately; the update must survive free conversation. This satisfies the
minimal-control principle that a recent audit of LLM-society experiments identifies as a pervasive
validity requirement (PIMMUR, Wang et al. 2025 — `pimmur2025`).

**Speech–belief gaps in LLM agents.** That an agent's public statements can part ways with its
private answers has precedent. Persona Inconstancy (Frisch & Giulianelli 2024 — `frisch2024persona`)
shows agents in group chat voice opinions they privately revert from, attributing the gap to
conformity; role-playing evaluations show stated beliefs diverging from enacted behavior in
single-agent settings (Do Role-Playing Agents Practice What They Preach, 2025 —
`preach2025roleplay`); and sycophancy work documents assertion shifts under social pressure.
Our object differs on three axes at once: we **separately elicit** SAY (in-conversation
utterances) and HELD (later private interviews) for every agent in an open multi-agent society;
we show an *intervention* (a persistent authoritative source) that moves SAY massively while HELD
stays flat — a dissociation, not just a gap; and we connect the gap to a repairable architectural
locus rather than documenting it. None of these neighbors tests whether any lever closes the gap.

**Misinformation, rumor, and cascades in agent societies.** Rumor and continued-influence research
separates spread from truth and shows that corrections often fail to displace stale beliefs
(Lewandowsky et al. 2012; Thorson 2016). Within LLM societies, transmission-chain work shows text
*properties* (toxicity, style) drift toward attractors (When LLMs Play the Telephone Game,
Perez et al. 2024 — `perez2024telephone`) — style drift, not the fate of a ground-truthed changing
fact. The closest concurrent neighbor, From Spark to Fire (Xie et al. 2026 — `xie2026spark`),
injects an *error* and defends with a centralized lineage-graph governance plugin that reads
adoption off agent outputs. We run the opposite direction — a *valid correction* failing to
install — read HELD from separate private probes rather than outputs, and repair with a
decentralized per-agent memory rule, not a message-layer governance service. Delayed-verification
analyses (2026 — `delayedverif2026`) derive closed-form instability thresholds for correction
timing, but in engineered verifier/critic networks; our society has no verifier and communicates
by free dialogue.

**Provenance in agent memory systems.** Provenance-tracking is an established idea in agent memory
engineering, and we do not claim it. MemClaw (2026 — `memclaw2026`) builds a *centralized,
policy-governed shared-memory service* and names stale propagation and provenance collapse among
its failure modes; MemIR (2026 — `memir2026`) types a *single agent's* long-term memory to
separate raw evidence from truth-bearing claims; BeliefMem (2026 — `beliefmem2026`) keeps
probabilistic candidate conclusions in a single agent's store; and a recent LLM-MAS memory survey
records provenance as a standard conflict-resolution principle. All of these place provenance in a
centralized store or one agent's memory hygiene. None asks our question: in a *decentralized*
society of per-agent memories communicating by natural dialogue, does a changing fact install as
held belief — and which memory architecture, compared head-to-head under one social harness, makes
it install? Our finding is a localization: the decisive locus is the listener-side integration
rule inside the social channel, quantified through the SAY/HELD dissociation.

**Factuality, measurement, and memory baselines.** Treating truthfulness as a semantic behavioral
target rather than surface fluency is now standard (TruthfulQA, Lin et al. 2022; SelfCheckGPT,
Manakul et al. 2023; semantic entropy, Farquhar et al. 2024). Our three-way verdict mirrors fact
verification (FEVER, Thorne et al. 2018) and the efficacy-vs-locality structure of knowledge
editing (ROME, Meng et al. 2022; MEMIT, Meng et al. 2023). The memory architectures we compare are
recognized systems (Mem0, Chhikara et al. 2025; A-MEM, Xu et al. 2025; MemoryBank, Zhong et al.
2024); belief revision and truth maintenance (AGM, Alchourrón et al. 1985; Doyle 1979) and
source-credibility opinion dynamics (DeGroot 1974) supply the classical grounding; and
model-collapse work (Shumailov et al. 2023) offers an analogy for recursive degradation — though
ours is communication-time degradation, not training-time collapse.

---

## 3. Method: the social-fidelity probe

**Setup.** A society of 25 LLM agents on a contact graph organizes an event. At round 1 the event's
time and place **change** from a stale value (A) to a current value (B), and the update is injected
into a single source agent. Agents then meet pairwise over rounds (a `meetings` parameter sets how
many encounters each agent has per round, i.e. connectivity), converse, store what they hear, and
retrieve memory to condition later utterances. We log every utterance (SAID) and, at the end,
privately interview every agent about the current fact (HELD): Inject → Propagate → Measure.

**The current / stale / unknown verdict.** Because the fact's truth value changed, we classify each
held answer three ways, mirroring recognized evaluation structures: **current** (holds the new
value — edit *efficacy* / SUPPORTED), **stale** (holds the superseded value — a *locality* failure /
continued-influence), and **unknown** (holds neither — a retention failure / NOT-ENOUGH-INFO).
The three-way split is load-bearing: separating *stale* (active corruption) from *unknown*
(information loss) is essential, because interventions act on them differently — scaling capability,
for instance, converts loss into confident corruption (§4.1). A semantic LLM judge reproduces the
keyword verdict (99–100% agreement), so the categories are not a keyword artifact.

**HEARD / SAID / HELD.** The probe's leverage comes from separating what reaches an agent, what it
utters, and what it later holds. "Held belief" is operational — the answer an agent gives when
probed; we make no claim about literal mental states.

**Matched-event replay.** To separate memory integration from architecture-induced changes in later
conversation, we freeze the realized per-agent event streams from eight independent PROV runs and
replay each same text-plus-metadata stream into fresh GA and PROV memories. Reconstruction must
match every original agent's final PROV version/value before replay. The independent unit is the
society seed; we report seed-level 95% t intervals and an exact paired sign test.

---

## 4. Results

### 4.1 Social fidelity decays, and no natural lever repairs it

In the core task the current value reaches the conversation stream but does not reliably become the
society's held answer. Over a long horizon (M5) the dynamics are sharper still: current truth can
rise early, peak near round 6, then decay toward a low steady state by round 30 — so truth can
appear transiently and still lose, and the round-5 snapshot slightly overstates retention.

Figure 1 and Table 1 rule out every intuitive repair. Capability produces a modest but incomplete
lift (18%→34%→30% across mini→gpt-5.4→gpt-5.5), connectivity (roughly neutral in the powered rerun — the early
"connectivity amplifies corruption" cell was an underpowered outlier, now retracted), a memory swap
(the apparent smga3g rescue did not replicate), thick Park-style personas, and a persistent
authoritative source all leave held truth at the ~14–21% baseline. Only broadcasting the current
value into **every** agent succeeds (99%) — an overwrite-style positive control that bypasses social
transmission, not a social cure. Agents can clearly output the truth; the problem is that ordinary
social communication does not reliably install it as held belief.

![Figure 1. Failed natural levers.](figures/fig_failed_levers.png)

*Table 1 — failed-lever evidence ledger.* capability mini→gpt-5.4→gpt-5.5: 18→34→30% (modest,
non-curative); connectivity:
ratio ~0.8–1.1 (neutral); memory GA vs smga3g: Δ≈0 (ns); persona thin vs thick: 12 vs 14% (ns);
source: Δ+0.8 (ns); broadcast: +21.8 (sig) → 99%.

### 4.2 Speech is not belief

Figure 2 is the centerpiece. Separating SAID (final-round utterances) from HELD (private interviews)
exposes a dissociation: under a persistent authoritative source, agents reach 83% current in what
they **say** while their **held** belief stays near baseline (15%). The gap is not confined to the
source condition — even baseline agents say the current value more than they hold it (SAID 56% /
HELD 12%) — and only broadcast aligns the two (99/99). Reach is not belief: a fact can be visible in
the transcript while failing as held state.

![Figure 2. Speech is not belief (SAY/HOLD dissociation).](figures/fig_say_vs_hold.png)

*Table 2 — HEARD→SAID→HELD (final-round SAID; HELD at interview).* baseline said 56 / held 12;
source said 83 / held 15 (the gap); broadcast said 99 / held 99. The source row's high-SAID,
low-HELD is the dissociation, and even baseline says more than it holds. The pattern replicates
across three scenarios (G1) and survives thick personas (G2).

### 4.3 Exposure matters, but integration decides

What drives the dissociation? A natural first suspect is exposure: perhaps agents that fail to
hold the truth simply have not heard it enough. The exposure probe (P1-mech) says exposure is real
but not decisive. Within conditions there is a clean dose–response — an agent's probability of
holding the current value rises with the fraction of current-value mentions it has heard,
approaching 95% at the highest exposures. Yet **across** conditions the naive frequency story
fails: baseline, source, and broadcast deliver near-identical mean heard-fractions
(0.64 / 0.72 / 0.73) with opposite outcomes (12% / 15% / 99% held). Two societies can hear almost
the same mixture of old and new values and end in opposite belief states. What an agent hears
therefore under-determines what it holds; the integration rule is a candidate causal factor.

The stronger test holds the received evidence itself fixed. We reconstruct the exact per-agent
event streams from eight realized PROV runs, audit the reconstruction against every original final
PROV state, and replay each identical text-plus-metadata stream into fresh GA and PROV memories.
PROV yields 60.5% held-current [52.8, 68.2] versus GA's 32.0% [28.0, 36.0], a paired lift of 28.5
points [21.5, 35.5]; PROV is higher in 8/8 seeds (exact two-sided sign test, p=.0078). Thus the
difference is not merely caused by the architectures generating different downstream
conversations: under matched received evidence, listener-side integration remains causally
consequential. We do not claim it is the only mechanism, and the replay conditions on structured
provenance being available (§5).

### 4.4 The cure: integrate by provenance, not frequency

The localization points to a precise repair. If integration by frequency lets the merely familiar
value win, integrate by **provenance** instead. Each claim carries a version (its origin round) as
conversation metadata; an agent holds the highest version it has *heard* and re-broadcasts that
versioned belief, so the latest authoritative version supersedes the merely frequent older one.
This is **fair**, not broadcast in disguise: PROV never overwrites an agent — the current value
must still arrive through conversation, and an agent that never hears it stays stale or unknown.
PROV changes only how an agent integrates and relays what it locally hears. It is also principled:
it acts exactly at the diagnosed locus (the integration rule), it is normatively correct for a
changing fact (frequency is the wrong cue — an old value repeated often is still old), and it
instantiates classic ideas — truth maintenance and belief revision (Doyle 1979; AGM) and
source-weighted opinion dynamics (DeGroot 1974) — in the social channel.

Figure 3 places PROV beside recognized memory architectures under one harness. Raw (14), Mem0 (18),
A-MEM (19), GA (22), GA-curr (25), and MemBank (25) all fail; only PROV lifts held truth (57%). The
decisive lever is the listener-side **integration rule**, not a larger or fancier memory.

![Figure 3. Architecture comparison — only PROV lifts held truth.](figures/fig_architecture.png)

The cure is not a single-condition artifact (Table 3): PROV wins across three scenarios (C8), a
numeric fact change (C9, dues $40→$60), and contact topologies (C10), with the margin *widening* on
harder structured networks (ring GA6/PROV68; smallworld GA10/PROV83).

*Table 3 — cure generality.* scenarios: repair_drive 57 vs GA22, book_club 69 vs 47, carpool 59
vs 18; fact type: dues PROV 59 [49-69] > GA 28; topology: random GA22/PROV93, ring GA6/PROV68,
smallworld GA10/PROV83 (r10).

### 4.5 The cure survives capability

Figure 4 repeats the comparison on a different model family (DeepSeek-V4-Flash) at full power (n=8).
GA is statistically flat-and-failing across models (mini 21.5%, DeepSeek 15.5%, overlapping CIs),
while PROV wins on both (57% / 64%) with CIs disjoint from GA. The cure survives capability — the
mirror image of "the phenomenon survives capability" (§4.1).

![Figure 4. Capability check (n=8) — the cure survives a model-family change.](figures/fig_capability_c14.png)

### 4.6 From lever to architecture: APM

Naive PROV identifies the right lever but is not yet a deployable architecture: it adopts the
highest version blindly — a liar can claim version 999 and hijack the society — and it carries only
a version, not an auditable chain. We harden it into **APM (Auditable Provenance Memory)** with three
guards, each closing one gap. **Origin anchoring**: an `auth` flag is minted only at the source and
relayed faithfully, so unauthenticated forgeries are rejected. **Chain corroboration**: a value is
committed only after K *independent* sources support it, counting paths rather than value-frequency —
the fix for the failure mode in which systematic garble corroborates the stale value. **Abstain**:
the agent holds *unknown* until that bar is met. Because every committed belief carries a complete
source→version→path trace, APM is auditable by construction — something black-box memories cannot
offer.

Without an adversary, APM ≈ PROV: interpretability is nearly free (~64% on DeepSeek, with 60–76% of
agents holding a fully traceable belief). Its reason to exist appears under attack (Figure 5). A
liar broadcasting a forged high-version stale claim collapses PROV from 57% to 33% and hijacks 43 of
75 agents (stale 57%); APM is unmoved (64%) with **zero hijack (stale 0)**, its origin anchoring
rejecting the forgery society-wide. Equivalent without an adversary, APM is the only architecture
left standing with one.

![Figure 5. Adversarial liar — only APM survives (stale=0).](figures/fig_apm_adversarial.png)

*Table 4 — architecture comparison incl. APM (held-current / auditable / under-liar).* Raw 14,
Mem0 18, A-MEM 19, GA 22, GA-curr 25, MemBank 25 — none auditable; PROV 57, half-auditable (version
only), collapses to 33% (stale 57%) under a liar; **APM ≈ PROV (64%), fully auditable, holds 64%
(stale 0) under a liar.** (held-current is mini/n=8 for recognized memories; APM no-adversary is
measured on DeepSeek; the under-liar column is mini/C16.)

### 4.7 APM does not saturate

One might worry that any sticky provenance memory simply floods to 100%. That ceiling is a
communication-model artifact (every-utterance, lossless broadcast), not a property of provenance
integration. Figure 6 sweeps communication density — how often agents actually mention the fact.
APM traces a smooth, fully monotonic S-curve: held-current climbs from 11% (mention 0, where only
the source knows) to 87% (mention 0.25–0.3), and reaches 100% only at the unrealistic dense limit
(0.5+). The 40% value at the sparse end is an honest floor, not a ceiling. Crucially, **stale stays
0 at every density**: under hard sparse communication no method spreads truth widely (the breadth
advantage over GA narrows), but APM still guarantees that the informed are never misled, which GA
does not. Its safety is independent of how far truth spreads.

![Figure 6. APM communication-sufficiency curve (n=5) — non-saturating, stale≡0.](figures/fig_apm_comms_curve.png)

---

## 5. Discussion and limitations

**What we claim.** In one controlled society we measure the full arc: speech and belief dissociate
under every natural lever; matched-stream intervention identifies listener integration as a causal
locus; changing that rule is the only architecture-level repair in a seven-way comparison; and the
repair can be hardened into an interpretable, adversary-resistant, non-saturating architecture. The claim is the
arc — measurement, diagnosis, localization, repair, hardening — under one harness with one
evidence standard (multi-seed, CIs, judge-validated metrics, pre-registered go/no-go for the APM
questions).

**Is structured PROV cheating?** This is the central reviewer risk, and the answer is no on both
sides. PROV is **not** broadcast: it still propagates through meetings, helps only agents the update
reaches, and is weakened by loss, garble, sparse mention, horizon, and topology (C5-stress, C7,
C10). But it is **not** fully naturalistic either — it assumes source and version survive the relay
as structured metadata, so it is best read as an idealized protocol or upper bound. A companion
result (PROV-text) shows that ordinary LLM dialogue does **not** spontaneously preserve
source/version, whereas an explicit attribution norm can repair held truth — a text-only upper
bound that is visibly protocolized. The engineering lesson is that agent societies may need not
larger memories but **social-memory interfaces that preserve provenance through communication**.

**We did not invent provenance — we localized where it must act.** Provenance is a classic idea
from truth maintenance and belief revision, and contemporary agent-memory systems already track it
in centralized stores (MemClaw) and single-agent memory hygiene (MemIR). Our contribution is
orthogonal to those designs: (i) show that default *decentralized* agent memories systematically
lose a changing fact even as agents keep saying it, (ii) localize the repair to the listener-side
integration rule inside the social channel, (iii) quantify the failure through the separately
elicited SAY/HOLD dissociation, and (iv) harden the rule into an auditable, adversary-tested
architecture and map its honest operating envelope.

**Limitations.** All experiments are simulations, and "held belief" is operational. The
fixed-stream test uses realized PROV-run conversations and conditions on structured provenance
metadata being available to both replay memories. It isolates downstream listener handling from
conversation generation, but does not show that ordinary dialogue spontaneously retains source and
version; C12 shows that it does not. The
micro-mechanism of the dissociation remains partially open: we rule out naive exposure-frequency
(§4.3) and identify the integration rule as a causal locus, but we do not characterize the
within-agent dynamics (e.g., recency versus incumbency of competing versions) — a timing-contrast
experiment we ran for this purpose failed its injection-config audit and is excluded. APM's
headline cells are n=3–5 pilots (versus n=8 for the diagnosis and the capability check); under
sparse communication its breadth advantage over GA is suggestive (overlapping CIs) while its
safety advantage (stale 0 vs 30) is decisive. APM's corroboration knob K trades flooding (K=1,
PROV-like) against over-conservatism (K≥2 deadlocks without relay-before-commit), and value
fidelity remains a dependency — heavy garble still degrades it. We deliberately disable individual
**forgetting** so that the failure is attributable to the integration rule rather than to memory
loss; whether forgetting reopens the update window is left open (our preliminary follow-up
returned a null at n=5).

**Human-society reading.** The telephone effect is not always a defect — for descriptive social
simulation, selective absorption and provenance loss are features to be reproduced, not bugs. Our
normative claim is narrower: once an agent society must maintain a changing fact for reliable
coordination, human-like telephone effects turn from feature into engineering risk.

---

## 6. Conclusion

In a society of LLM agents, a ground-truthed update can be *said* without being *held*: authority
moves speech but not belief. No natural lever repairs this, and exposure alone does not explain
it. When every received event is held fixed, changing how listeners integrate that evidence still
raises held truth by 28.5 points. Integrating heard claims by provenance rather than frequency is
the only memory-architecture repair that
works, and it holds across scenarios, fact types, topologies, and model families. Hardened into
APM, the rule becomes interpretable by construction, the only architecture that survives an
adversarial liar, and a realistic non-saturating equilibrium that is never confidently wrong.
Reach is not belief; for agent societies that must track changing facts, the difference between
saying the truth and holding it is one integration rule — and it can be engineered.

---

## References (key bib keys — see `latex/references.bib`)

Existing: park2023generative · li2023camel (CAMEL) · wu2023autogen (AutoGen) · zhou2024sotopia
(SOTOPIA) · xie2026spark (From Spark to Fire) · thorne2018fever (FEVER) · meng2022rome (ROME) ·
meng2023memit (MEMIT) · lewandowsky2012misinformation · thorson2016belief · lin2022truthfulqa ·
manakul2023selfcheckgpt · farquhar2024detecting · doyle1979truth (TMS) · alchourron1985logic (AGM) ·
degroot1974reaching · shumailov2023curse (model collapse) · chhikara2025mem0 (Mem0) ·
xu2025amem (A-MEM) · zhong2024memorybank (MemoryBank).

**New (bib sync pending — all first-hand verified 2026-07-06, see
`../docs/project/red_ocean_audit_2026-07-06.md`):**
frisch2024persona (Persona Inconstancy, arXiv 2405.03862) · preach2025roleplay (Do Role-Playing
Agents Practice What They Preach, arXiv 2507.02197) · pimmur2025 (PIMMUR Principles, arXiv
2509.18052) · perez2024telephone (When LLMs Play the Telephone Game, arXiv 2407.04503) ·
memclaw2026 (Governed Shared Memory for Multi-Agent LLM Systems, arXiv 2606.24535) ·
memir2026 (Mitigating Provenance-Role Collapse via Typed Memory, arXiv 2605.25869) ·
beliefmem2026 (Belief Memory: Agent Memory Under Partial Observability, arXiv 2605.05583) ·
delayedverif2026 (Delayed Verification Destabilizes Multi-Agent LLM Belief, arXiv 2606.27409).
