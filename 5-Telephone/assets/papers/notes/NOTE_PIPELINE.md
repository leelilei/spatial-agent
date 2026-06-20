# Telephone Reading Notes Pipeline

> Updated: 2026-06-20
> Scope: convert the 58 parsed local papers into paper-useful notes for the
> 5-TELE submission.

## Purpose

The notes are a bridge between the literature corpus and our paper. They should
not merely summarize papers. Their job is to decide how each reference supports,
limits, or challenges the Telephone argument:

> LLM-agent societies can be made to say the truth without coming to hold the
> truth, because collective belief is path-dependent and entrenched by early,
> broad social evidence.

Every note must therefore produce a usable citation decision: cite strongly,
cite briefly, keep as background, replace, or exclude.

## Desired Outputs

The notes pipeline produces four artifacts:

1. Per-paper notes in `assets/papers/notes/<category>/<index>_<slug>.md`.
2. A claim-evidence matrix in `assets/papers/notes/INDEX.md`.
3. A curated citation list update in `paper/references.md`.
4. A draft-ready related-work map for the final paper.

## What Each Note Must Give Us

Each note should extract six things:

1. **Paper role**: setting, close neighbor, mechanism, metric, intervention, or caveat.
2. **Core result**: the one result we may cite, in one or two sentences.
3. **Telephone bridge**: how it relates to fidelity decay, speech-belief dissociation,
   or entrenchment.
4. **Use sentence**: a draft-ready sentence that could appear in our paper.
5. **Boundary**: what this paper does not show, and what our paper adds.
6. **Citation decision**: must-cite, cite, maybe, background, replace, or exclude.

## Contribution Map

| Telephone contribution | Literature support needed | Note evidence to collect |
|---|---|---|
| C1. Fidelity is distinct from reach | Agent societies and rumor-spread papers show information can spread | Does the paper measure spread/reach but not held truth? |
| C2. Speech-belief dissociation | Memory, debate, correction, and behavioral-coherence papers | Does the paper separate utterance, retrieval, action, belief, or final answer? |
| C3. Path-dependent entrenchment | Transmission chains, iterated learning, continued influence, collective conventions | Does the paper show early/broad exposure, attractors, or persistence after correction? |
| C4. Natural levers do not cure social truth decay | Scaling, connectivity, memory, source/correction papers | Does the paper motivate a lever we tested, or show why it might fail? |
| C5. Communication-time analog of collapse | Model collapse and self-consuming generation | Does the paper support degradation through recursive reuse, but at training time rather than conversation time? |
| C6. Rigor and measurement | LLM judge, hallucination/factuality, trace-level MAS failure papers | Does the paper justify our metrics, trace analysis, or validation? |

## Workflow

### Step 0. Check Source Quality

Before reading, verify the local asset:

- `citation_sources.json` has the preferred venue, DOI, and publisher URL.
- `fulltext_manifest.json` status is `ok`.
- If `quality_flags` includes `abstract_may_include_layout_noise`, use the full text
  and PDF for claims; do not trust the extracted abstract alone.
- If `short_text` or `abstract_not_detected` appears, mark the note as source-problem
  until the correct PDF is obtained.

Known issue:

- Index 55 appears to have a Qeios review PDF rather than the Scientific Reports
  article PDF. Do not use it as article evidence until replaced or verified.

### Step 1. Deduplicate

Use DOI/title before writing a note. If two records point to the same paper, write
one canonical note and list aliases in its front matter.

Known duplicate:

- Index 1 and index 11 both refer to `Generative Agents: Interactive Simulacra of
  Human Behavior`, DOI `10.1145/3586183.3606763`. Use index 11 as canonical unless
  we later decide otherwise.

### Step 2. Read For Role, Not Exhaustiveness

For each paper, read in this order:

1. Title, abstract, intro.
2. Main result or system contribution.
3. Evaluation setup and metrics.
4. Limitations or discussion.
5. Related work only if it points to a missing must-cite source.

The reading question is always: what does this paper let us say more rigorously?

### Step 3. Write The Note

Use `NOTE_TEMPLATE.md`. Keep notes compact enough to be useful while drafting:
usually 500-900 words for must-cite papers and 200-400 words for background papers.

### Step 4. Decide Citation Fate

Each note ends with one of:

- `must-cite`: central to setting, closest neighbor, mechanism, or framing.
- `cite`: useful support for one section.
- `maybe`: keep until related work is drafted.
- `background`: useful for our thinking but unlikely to cite.
- `replace`: right topic, weaker than another source.
- `exclude`: wrong source, wrong PDF, or not useful for our paper.

### Step 5. Promote To Paper Assets

After a batch is reviewed:

1. Update `INDEX.md` with the citation decision.
2. Promote strong entries into `paper/references.md`.
3. Add draft-ready related-work bullets to the paper outline or related-work draft.

## Batch Plan

### Batch A: Must-Cite Spine

Goal: establish setting, closest neighbors, and our novelty.

- 11 Generative Agents
- 12 CAMEL
- 13 AutoGen
- 20 Multiagent Debate
- 29 TruthfulQA
- 39 Cannot Self-Correct
- 50 Simulating Misinformation Propagation with LLMs
- 53 The science of fake news
- 54 Rumor Cascades
- 61 Belief Echoes
- 68 The Curse of Recursion
- 69 Self-Consuming Generative Models Go MAD

### Batch B: Agent Society And Memory Levers

Goal: support why memory, agent frameworks, and communication protocols are natural
levers, then position our negative result.

- 14 AgentVerse
- 15 MetaGPT
- 16 ChatDev
- 17 AgentScope
- 18 SOTOPIA
- 42 MemoryBank
- 43 MemGPT
- 44 Reflexion
- 45 ReAct
- 47 A-MEM
- 48 AIOS

### Batch C: Metrics And Factuality

Goal: support our measurement shift and judge validation.

- 30 SelfCheckGPT
- 31 Language Models Mostly Know What They Know
- 32 Semantic Entropy
- 33 HaluEval
- 36 RAGTruth
- 37 Internal State Knows When It Is Lying
- 38 Just Ask for Calibration
- 40 ANAH-v2
- 41 Delusions of Large Language Models

### Batch D: Optional And Cleanup

Goal: fill gaps only where the draft needs support.

- Remaining debate/consensus papers.
- Remaining misinformation and culture-transmission papers.
- Records with source-quality flags after replacement or manual verification.

## Quality Gates

A note is done only if it has:

- DOI/venue checked against `citation_sources.json`.
- A clear role and citation decision.
- At least one Telephone-specific bridge sentence.
- A boundary statement saying what the paper does not cover.
- A proposed sentence for our manuscript.

If a note cannot pass these gates, keep the paper in `maybe`, `replace`, or `exclude`.
