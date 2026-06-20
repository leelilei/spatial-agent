# Social Fidelity Probe - Results Tables

> Draft tables for Results writing. Keep this file close to `RESULTS.md`; use it
> to avoid re-litigating the evidence chain while drafting.

## Table 1. Headline Results Ledger

| Evidence block | Question | Key result | Paper-level claim |
|---|---|---|---|
| M4 source vs broadcast | Can a realistic authority repair held truth? | Baseline 3.0/25 current; source 3.8/25 ns; broadcast 24.8/25 significant | Source changes speech but not held belief; broadcast is an overwrite control |
| G1 generality | Is the dissociation a single-scenario artifact? | Pattern repeats across repair_drive, book_club, and carpool: source does not approach broadcast | Dissociation generalizes across scenarios |
| G2 persona depth | Is this caused by thin personas? | Thick persona baseline 3.6/25, source 3.0/25, broadcast 24.6/25 | Persona richness is not the missing repair |
| P1-rec timing | Is the mechanism recency? | r1 all-agent broadcast 24.8/25; r5 all-agent broadcast 3.3/25 | Mechanism is early/broad entrenchment, not recency |
| P2 semantic judge | Is the metric a keyword artifact? | Judge matches keyword current counts: 3.0, 3.8, 24.8 | Headline verdict survives semantic judging |
| P3 capability | Does scale solve it? | mini 4.6/25; gpt-5.4 8.6/25; gpt-5.5 7.6/25 | Capability helps modestly but does not cure social fidelity decay |
| P3/P3b connectivity | Does more communication repair or amplify? | Mini connectivity roughly flat; gpt-5.4 amplification did not replicate | Connectivity is neutral/non-curative, not a stable amplifier |
| M5 long horizon | Is r5 the whole phenomenon? | Baseline peaks near 28% at r6 then decays to 6% by r29; source decays to 4%; broadcast stays near 92% | Truth can appear transiently and still lose over time |

## Table 2. HEARD -> SAID -> HELD Mechanism

| Condition | HEARD / exposure | SAID / utterance | HELD / interview | Mechanistic reading |
|---|---|---|---|---|
| Baseline | One source receives the current update early; most agents encounter a mixed stream later | Current value appears but competes with stale history | Low current belief, high stale/unknown | Ordinary social transmission does not preserve the update |
| Persistent source | The authoritative source repeats the current truth across rounds | Final-round utterances become current-dominant in M4 | Held current remains near baseline | Exposure and utterance are insufficient once stale belief is entrenched |
| Broadcast every round | Every agent receives current truth directly and repeatedly | Current utterances dominate | Held current reaches near ceiling | Direct overwrite bypasses social transmission |
| Early all-agent broadcast | Every agent receives current truth at round 1 | Later social stream reinforces the current version | Held current near ceiling | Early and broad establishment creates a truth attractor |
| Late all-agent broadcast | Every agent receives current truth immediately before probing | The update is maximally recent | Held current near baseline | Recency alone cannot overwrite entrenched belief |

## Table 3. Related Work To Result Mapping

| Paper claim | Primary citation spine | Why it belongs |
|---|---|---|
| Agent societies make communication a real substrate | Generative Agents; CAMEL; AutoGen; SOTOPIA | Establishes the setting and why social information flow matters |
| Spread is not fidelity | Generative Agents; rumor / misinformation work; LLM-agent rumor simulations | Prior work measures reach or plausibility; this work measures held-current truth |
| Output truth is not held belief | Multi-agent debate; stance-based faithfulness debate; internal-state truthfulness; calibration | Supports separating utterance, role, confidence, and later answer |
| Correction can leave stale belief | Belief Echoes; fake-news science; LLM self-correction limits | Supports persistence after correction and failed natural repairs |
| Memory is a possible mechanism but not a guaranteed cure | MemoryBank; MemGPT; Reflexion; A-MEM; Voyager | Explains exposure vs durable state and future mitigation directions |
| Recursive degradation is an analogy | Curse of Recursion; Self-Consuming Generative Models; How Bad Is Training on Synthetic Data | Provides collapse vocabulary while keeping mechanism distinct |

## Table 4. Safe Wording For Claims

| Unsafe wording | Use instead |
|---|---|
| Connectivity amplifies corruption | Connectivity does not restore truth and appears roughly neutral in powered reruns |
| Source correction fails because agents do not hear it | Source correction changes what agents say but not what they later hold |
| Broadcast is the cure | Broadcast is a positive control that bypasses social transmission |
| Memory does not matter | The tested memory swap does not robustly repair held belief; memory can still affect speech and remains a mitigation direction |
| This is model collapse | This is a communication-time analogue of model collapse, not the same training-time mechanism |
