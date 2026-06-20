# Telephone — fidelity and decay of information in LLM-agent societies

> Codename: **Telephone** (the children's game where a message degrades as it passes
> person to person). New project, started 2026-06-19. Spun out of the society-simulation
> work in `../3-SMGA` (which reused its sim engine here).

## North star

**Understand and quantify how information propagates and DEGRADES in a society of LLM
agents — whether the society converges on the TRUTH or on a corrupted version.**

The agent society is used as a **scientific instrument** (a microscope on a phenomenon),
NOT as a benchmark for ranking architectures.

> **Proposal: `docs/plans/proposal.md`** (the current result-aware "what we're writing"
> doc — claims, related-work positioning, target venues, rigor). Historical proposal drafts
> live in `docs/plans/archive/`; `telephone-research.md` is the literature review behind v1.
>
> **Project controls:** `docs/guides/todolist.md` tracks active work; `docs/guides/project.yaml`
> tracks milestones, phases, and paper-readiness; `docs/project/reference_sources.md` indexes
> the reference workflow.

## The gap we are attacking

Generative-Agents-lineage work treats information diffusion as a **success demo**:
Isabella plans a party, the invitation spreads through the town, everyone applauds the
emergence. **But nobody asks whether what spread is still the original message.** Our
prior work (`../3-SMGA/sim/RESULTS.md`, S5L-diag) found, with hard evidence, that it
often is NOT: in a weak-model society a fact-update degrades as it propagates —

- **stale-persistence**: the superseded value ("Saturday") keeps being retransmitted and
  out-competes the update;
- **detail drift**: "community center" → "community shed"; times and places mutate;
- **version splitting**: different sub-groups converge on different corrupted versions.

So the society converges not on the truth but on a **corrupted consensus**. This is real,
measurable, and (as far as we can tell) un-characterized.

## The claim (big, on purpose)

> In LLM-agent societies, a ground-truthed update **degrades predictably as it
> propagates** (a "telephone" effect). We characterize the **fidelity-decay** of social
> information, identify what governs it (network connectivity, model capability, message
> framing/redundancy, presence of an authoritative source, and **agent memory
> architecture**), and ask whether better memory acts as **error-correction** that
> preserves collective fidelity.

**Memory is a VARIABLE here, not the headline** — a possible "anti-entropy relay" knob,
not the thing we are selling. (This is the lesson from 3-SMGA: memory-architecture-as-
headline kept failing under rigor; here it earns its place as one governing variable.)

## Method (turn the mess into clean quantitative science)

1. **Instrument**: a controllable society sim (reused from `../3-SMGA/sim`). Inject ONE
   update with a known ground truth into a source agent; let it propagate.
2. **Model it like an epidemic / rumor process**: measure a **fidelity-decay curve** —
   how faithful is the held/spoken value as a function of hops / rounds / who you ask.
3. **Ablate the governing variables**: connectivity, model capability (mini vs strong),
   message redundancy/framing, authoritative re-broadcast, and memory architecture.
4. **Core question**: *under what conditions does a society of LLM agents converge on the
   truth vs on a corrupted version?* And: *does better agent memory reduce the drift?*

## Metrics (to be frozen in docs/ before the first real run)

- **Fidelity**: does an agent's held/spoken version match the ground-truth update?
- **Version-share**: what fraction of the society converges on truth vs each corruption?
- **Decay-vs-hops**: fidelity as a function of distance from the source.
- **Corruption taxonomy**: stale-persistence vs drift vs fabrication vs loss.

(Note: avoid the 3-SMGA trap — define "received the update" and "fidelity" INDEPENDENTLY
of the answer keyword, to prevent the circularity that confounded the SMGA metric.)

## Working principles (准绳 — carried over, they govern how we work)

1. **Aim for a big claim.** Don't shrink it because it's hard; build the evidence up to it.
2. **Solve problems; don't abandon them.** An obstacle is something to remove, not a
   reason to switch tracks. (But note: here, the "noise/sensitivity" that defeated 3-SMGA
   is part of the SUBJECT, not a confound to fight.)
3. **No underpowered nulls, no hype.** Adequate power (variance controlled, effect size +
   CI), honest scope.
4. **Record EVERY experiment** — even small/failed ones — in the experiment ledger at the
   top of `RESULTS.md`. Concept-level/paper narrative goes in `paper/narrative.md`.

## Layout

```text
.
|-- README.md            # this file - the thesis
|-- RESULTS.md           # experiment ledger + per-run results
|-- assets/
|   `-- papers/          # reference reports, PDFs, and reading notes
|-- docs/
|   |-- guides/          # execution guides and collection workflows
|   |-- plans/           # proposals, metric definitions, frozen protocols
|   `-- project/         # notes, decisions, conclusions, reference index
|-- experiments/         # orchestration scripts / analysis notebooks above sim/
|-- paper/
|   |-- narrative.md     # living concept narrative
|   `-- references.md    # curated working reference library
|-- results/             # derived tables / figure-ready artifacts
`-- sim/                 # experimental instrument reused from ../3-SMGA/sim
```
## Relation to 3-SMGA

3-SMGA (structured memory for generative agents) is the parent. Its enduring assets we
reuse: the society-sim engine (`society.py`, `memories.py`, `llm.py`, `replay_eval.py`),
the embedding retrieval (model2vec), and — most importantly — the **reproducibility /
variance / controlled-replay rigor** we developed there, which is exactly the scarce
skill this phenomenon-study needs. The 3-SMGA finding that motivated this project lives
at `../3-SMGA/sim/RESULTS.md` (S5L-diag) and `../3-SMGA/paper/narrative.md`.
