# Supplementary Appendix

Anonymous supplementary material for `When Truth Loses Its Source: Provenance-Aware Memory for Socially Distributed Agents`.

This appendix is intended to support the AAAI submission without carrying the main argument. The main paper should remain self-contained; this file stores protocol details, result ledgers, and the reference-placement map.

## A. Experimental Protocol

### Society

- Population: 25 LLM agents.
- Contact model: random pairwise meetings, with duplicate pairs removed.
- Default connectivity: two meetings per agent per round (`m=2`) unless a condition varies connectivity.
- Meeting length: short alternating-turn exchanges.
- Memory: generative-agent-style event stream plus reflection memory.
- Default model: `gpt-5.4-mini`, temperature 0.

### Mutable Fact

Each scenario contains a stale event value and a current event value. The update changes both day/time and location, so an answer can be scored as current, stale, mixed, or unknown.

Main scenarios:

- `repair_drive`: Saturday/porch changes to Sunday/community center.
- `book_club`: Tuesday/library changes to Thursday/cafe.
- `carpool`: 7am/school lot changes to 8am/church lot.

### Interventions

- `baseline`: update injected once into a single source at round 1.
- `source`: authoritative source receives the update every round and must re-propagate it socially.
- `broadcast`: every agent receives the update every round.
- `early all-agent broadcast`: every agent receives one broadcast at round 1.
- `late all-agent broadcast`: every agent receives one broadcast immediately before the final probe.
- `capability`: default model compared with stronger models.
- `connectivity`: vary meetings per round.
- `memory`: compare generative-agent memory with a currency-resolving memory variant.

## B. Measures

### HEAR

Whether an agent was exposed to the current update through its event stream or conversations.

### SAY

The value an agent utters in meeting transcripts. SAY is computed only over utterances that explicitly mention the stale or current value; unrelated conversation is not counted as false.

### HOLD

The value an agent gives in a private final interview using only its own memory notes. HOLD is the paper's operational measure of held belief.

## C. Data Interpretation

The headline pattern is a three-way separation:

- Availability: source makes the current value visible in the transcript.
- Adoption: source does not make the current value the final private answer for most agents.
- Persistence: even when current truth rises early, long-horizon runs decay toward a low, often unknown-dominated state.

Key numeric anchors from the current paper:

- Final SAY-current: baseline 63%, source 82%, broadcast 100%.
- Final HOLD-current: baseline 12%, source 15%, broadcast 99%.
- Long-horizon baseline: held-current peaks at 28% around round 6 and falls to 6% by the end.
- Long-horizon source: held-current peaks at 36% around round 5 and falls to 4% by the end.
- Timing mechanism: late all-agent broadcast reaches 9%, early all-agent broadcast reaches 100%.
- Capability ladder: stronger models improve held-current to roughly 30-34%, but remain far below broadcast.

Interpretation:

The data do not show that agents never hear or say the correction. They show that hearing and saying are insufficient for durable social state. The source condition is therefore the key evidence block: it changes the transcript but not the later private answer. Broadcast is a positive control, not a realistic repair, because it bypasses social transmission and directly aligns the population state.

## D. Experiment Matrix and Seeds

The current repository contains 41 aggregate experiment rows and 166 run-level seed rows. The full ledgers are generated from `sim/runs` by `paper/scripts/supplement_analysis.py`.

Generated files:

- `paper/supplement/experiment_matrix.csv`: one row per aggregate condition.
- `paper/supplement/seed_table.csv`: one row per run/seed.
- `paper/supplement/source_trace_agents.csv`: one row per source-condition agent observation.
- `paper/supplement/source_trace_summary.csv`: trace-level summary counts.
- `paper/supplement/source_trace_examples.md`: transcript-to-interview examples.

Core matrix excerpts:

| Block | Conditions | Runs / seeds | Held-current result |
|---|---|---:|---:|
| Main speech-belief probe | baseline / source / broadcast | 5 each; seeds 41-45 | 12.0% / 15.2% / 99.2% |
| Timing mechanism | late broadcast / early broadcast | 5 each; seeds 41-45 | 8.8% / 100.0% |
| Capability ladder | mini / gpt-5.4 / gpt-5.5 | 8 / 5 / 5 runs | 18.5% / 34.4% / 30.4% |
| Connectivity | m=1 / m=2 / m=3 | 8 each in powered mini runs | 19.5% / 18.5% / 14.0% |
| Memory verification | GA m=2 / SMGA3G m=2 | 5 each; seeds 41-45 | 16.8% / 24.0% |
| Scenario robustness | repair / book / carpool | 5 each per condition | source remains below broadcast |
| Thick persona robustness | baseline / source / broadcast | 5 each; seeds 41-45 | 14.4% / 12.0% / 98.4% |

Seed convention:

- Most five-run conditions use schedule seeds 41-45.
- Powered capability and connectivity reruns use schedule seeds 41-48.
- Some earlier exploratory cells remain in the matrix with fewer seeds; these are retained for provenance but the main paper uses the powered/verified cells.

## E. Source-Condition Trace Audit

The source trace audit asks whether the source result could be dismissed as a transcript absence artifact. It uses the strictest repair-drive current marker: an exposure or utterance counts only when the text contains both `Sunday` and `community center`.

| Trace class | Agents | Final current | Final stale | Final unknown | Interpretation |
|---|---:|---:|---:|---:|---|
| All source-condition agents | 125 | 19 | 3 | 103 | Aggregate held-current is 15.2%. |
| Heard current pair from speech | 28 | 16 | 0 | 12 | Hearing the full current value often fails to become HOLD. |
| Said current pair | 15 | 11 | 0 | 4 | Some agents say the exact current value, then answer unknown. |
| Heard any current marker | 48 | 19 | 2 | 27 | Looser marker exposure is even less predictive. |
| Said any current marker | 33 | 15 | 1 | 17 | Loose current-valued speech also fails as a belief proxy. |
| Direct world injection | 5 | 5 | 0 | 0 | Direct grounded source updates are remembered; social relay is the weak link. |

Representative examples are stored in `source_trace_examples.md`. For example, in `run_001`, Kira heard Noah confirm "Sunday at the community center," repeated the same current pair, and still answered that the notes did not give the time or location. In `run_003`, Oren accepted "Sunday at the community center works for me" but later answered that the notes did not contain the current time or location.

Conclusion: the source condition is not merely failing to expose agents to the correction. The correction enters local traces and even local speech, but it does not reliably become the later private answer.

## F. Reference Placement Map

### Main-Text Citations

Agent societies and communicative-agent substrates:

- Generative Agents
- CAMEL
- AutoGen
- AgentVerse
- MetaGPT
- ChatDev
- AgentScope
- ReAct
- SOTOPIA
- Theory of Mind for Multi-Agent Collaboration
- Generative Agent Simulations of 1,000 People

Factuality, hallucination, and measurement:

- TruthfulQA
- Language Models (Mostly) Know What They Know
- SelfCheckGPT
- Detecting Hallucinations Using Semantic Entropy
- HaluEval
- RAGTruth
- The Internal State of an LLM Knows When It's Lying
- Just Ask for Calibration
- Large Language Models Cannot Self-Correct Reasoning Yet

Debate and deliberation:

- Improving Factuality and Reasoning through Multiagent Debate
- Debate Helps Supervise Unreliable Experts
- Encouraging Divergent Thinking through Multi-Agent Debate
- Debating with More Persuasive LLMs Leads to More Truthful Answers

Memory and persistent agent state:

- Reflexion
- MemoryBank
- MemGPT
- Voyager
- A-MEM

Human misinformation and transmission:

- The Science of Fake News
- The Spread of True and False News Online
- Rumor Cascades
- Belief Echoes
- How Stereotypes Are Shared Through Language
- The Audience-Tuning Effect of Negative Stereotypes in Communication
- Cumulative Cultural Evolution in the Laboratory

Recursive degradation analogy:

- The Curse of Recursion
- Self-Consuming Generative Models Go MAD
- How Bad is Training on Synthetic Data?

### Appendix-Only / Background Candidates

These are useful for literature coverage but should not be forced into the main paper unless a specific claim needs them:

- AIOS and Agent Hospital: agent infrastructure and domain background, less direct than memory-state work.
- UHGEval, ANAH-v2, Chinese hallucination evaluations: useful if adding a multilingual evaluation paragraph.
- PRD, CONSENSAGENT, CortexDebate, SELENE: debate/consensus variants; cite if a future version expands the debate literature.

## G. Reproducibility Pointers

Regenerate figures:

```powershell
& 'C:\Users\lee\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'D:\0-Research\5-Telephone\paper\scripts\plot_figures.py'
```

Regenerate supplement ledgers:

```powershell
python 'D:\0-Research\5-Telephone\paper\scripts\supplement_analysis.py'
```

Compile the main paper:

```powershell
$env:PATH='C:\Users\lee\AppData\Local\Programs\MiKTeX\miktex\bin\x64;' + $env:PATH
pdflatex --enable-installer -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex --enable-installer -interaction=nonstopmode -halt-on-error main.tex
pdflatex --enable-installer -interaction=nonstopmode -halt-on-error main.tex
```

Important output files:

- `paper/latex/main.pdf`
- `paper/figures/figure_data_summary.csv`
- `paper/scripts/plot_figures.py`
