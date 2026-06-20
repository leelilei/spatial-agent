# Telephone - Reference Spine

> Built from `assets/papers/notes/INDEX.md` and the 54 canonical deep-read
> notes. This file is for paper drafting. Final `.bib` entries still need venue,
> DOI, pages, and publisher URLs verified before submission.

## Citation Decisions

| Tier | Count | Use |
|---|---:|---|
| must-cite | 6 | Core spine for the paper's setting, metric, close neighbor, mechanism, and analogy |
| cite | 30 | Supporting related-work and methods references |
| background | 10 | Keep available but do not crowd the main text |
| maybe | 7 | Use only if a paragraph needs them |
| replace | 5 | Duplicate records or source problems; do not cite as independent papers |

## Must-Cite Spine

### Agent-Society Setting

**Generative Agents: Interactive Simulacra of Human Behavior**  
Role: canonical agent-society setting.  
Use: Generative Agents shows believable social diffusion; Telephone asks whether
what diffuses remains faithful.  
Draft sentence: Prior work on generative agents demonstrates that information can
spread through simulated societies; Telephone studies the missing axis, whether a
ground-truthed update remains faithful after that spread.

### Closest Misinformation Neighbor

**Simulating Misinformation Propagation in Social Networks using Large Language Models**  
Role: close neighbor for LLM-agent misinformation diffusion.  
Use: Cite to show that LLM-agent societies are already used to simulate
misinformation propagation.  
Draft sentence: LLM-agent misinformation simulations model how misleading
content propagates through social networks; Telephone shifts the endpoint from
propagation to held-belief fidelity after a truth change.

### Factuality Metric Anchor

**TruthfulQA: Measuring How Models Mimic Human Falsehoods**  
Role: truthfulness benchmark / metric anchor.  
Use: Cite for the distinction between fluent plausible answers and truthful
answers.  
Draft sentence: TruthfulQA shows that models can reproduce human falsehoods in
plausible language; Telephone extends factuality evaluation from isolated QA to
social transmission.

### Misinformation Framing

**The science of fake news**  
Role: canonical misinformation framing.  
Use: Cite for separating reach, correction, belief, and social consequences.  
Draft sentence: Misinformation research distinguishes the spread of content from
its belief-level consequences; Telephone operationalizes that distinction in an
LLM-agent society.

### Correction Persistence

**Belief Echoes: The Persistent Effects of Corrected Misinformation**  
Role: human-side mechanism analogy for corrected misinformation still shaping
attitudes.  
Use: Cite for the idea that correction can be accepted yet fail to eliminate the
effect of prior misinformation.  
Draft sentence: Human belief-echo work shows that corrected misinformation can
continue to shape attitudes; Telephone finds an LLM-agent analogue in which
corrected speech does not reliably become held truth.

### Model-Collapse Analogy

**The Curse of Recursion**  
Role: training-time recursive degradation analogy.  
Use: Cite carefully as an analogy, not as the same mechanism.  
Draft sentence: Recursive training can collapse model distributions when
generated data feeds back into training; Telephone studies a communication-time
analogue in which repeated social reuse degrades factual fidelity without model
retraining.

## High-Value Cite Set

### Agent Societies And Multi-Agent Conversation

- **CAMEL: Communicative Agents for Mind Exploration of LLM Society**  
  Use: establishes role-playing communicative agents as a standard setting.
- **AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation**  
  Use: establishes multi-agent conversation as an engineering primitive.
- **SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents**  
  Use: establishes social interaction as an evaluation target.
- **Theory of Mind for Multi-Agent Collaboration via Large Language Models**  
  Use: supports separating utterance from latent state/partner modeling.

Draft paragraph: Communicative-agent systems such as CAMEL and AutoGen make
agent-to-agent dialogue a standard substrate for LLM applications, while social
evaluation environments such as SOTOPIA broaden evaluation beyond isolated QA.
Telephone uses this substrate to ask a narrower reliability question: whether a
changing fact remains current after social transmission.

### Debate, Deliberation, And Speech-Belief Separation

- **Improving Factuality and Reasoning in Language Models through Multiagent Debate**  
  Use: optimistic baseline that multi-agent discussion can improve answers.
- **Debate Helps Supervise Unreliable Experts**  
  Use: debate as truth-revealing oversight contrast.
- **Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate**  
  Use: Degeneration-of-Thought / path-dependence contrast.
- **Debating with More Persuasive LLMs Leads to More Truthful Answers**  
  Use: debate can improve truthfulness in judged settings.
- **Faithful, Unfaithful or Ambiguous? Multi-Agent Debate with Initial Stance for Summary Evaluation**  
  Use: stance/utterance can be role-imposed rather than held belief.

Draft paragraph: Debate work provides the optimistic counterpoint: structured
multi-agent conversation can improve judged answers. Telephone identifies a
different failure mode. The correct statement can win space in conversation
without becoming the answer agents later hold.

### Factuality, Hallucination, And Measurement

- **SelfCheckGPT**  
  Use: black-box behavioral factuality measurement.
- **Language Models (Mostly) Know What They Know**  
  Use: self-evaluation and calibration depend on elicitation.
- **Detecting Hallucinations in Large Language Models Using Semantic Entropy**  
  Use: semantic equivalence matters more than surface match.
- **HaluEval**  
  Use: hallucination benchmark background.
- **RAGTruth**  
  Use: evidence exposure does not guarantee supported output.
- **The Internal State of an LLM Knows When It's Lying**  
  Use: surface text is not the whole epistemic story.
- **Just Ask for Calibration**  
  Use: confidence/correctness elicitation caveat.
- **Large Language Models Cannot Self-Correct Reasoning Yet**  
  Use: correction without reliable grounding may fail.

Draft paragraph: Telephone follows factuality evaluation work in treating truth
as a semantic behavioral target, not a fluency property. It differs by placing
the target in a social process: the ground truth changes, agents communicate,
and the final metric asks what they later answer.

### Memory And Durable Agent State

- **MemoryBank**  
  Use: long-term state is an explicit agent design problem.
- **MemGPT**  
  Use: exposure in context is not the same as retrievable state.
- **Reflexion**  
  Use: verbal feedback can help when engineered into memory.
- **Voyager**  
  Use: durable behavior depends on accumulated retrievable state.
- **A-MEM**  
  Use: future mitigation via adaptive memory organization.

Draft paragraph: Agent-memory work makes clear that durable state must be
engineered. Telephone supplies a stress test for such systems: hearing or
uttering a correction is not sufficient unless the update becomes the state
later answers draw on.

### Human Communication And Persistence

- **Rumor Cascades**  
  Use: cascade dynamics and correction background.
- **How Stereotypes Are Shared Through Language**  
  Use: language can stabilize social beliefs through framing.
- **The Audience-Tuning Effect of Negative Stereotypes in Communication**  
  Use: utterance can feed back into later memory/impression.

Draft paragraph: Human communication work provides the conceptual precedent
that transmission is not neutral transport. Messages can be shaped by audience,
framing, and prior belief, then feed back into memory and judgment.

### Recursive Degradation And LLM-Mediated Communication

- **Self-Consuming Generative Models Go MAD**  
  Use: recursive generated-data loops can degrade quality/diversity.
- **How Bad is Training on Synthetic Data?**  
  Use: statistical model of synthetic-data collapse and the need for fresh data.
- **Trustworthy LLM-Mediated Communication: LAAC**  
  Use: communication fidelity as a trustworthiness requirement.

Draft paragraph: Model-collapse work motivates the analogy to recursive
degradation, but Telephone's mechanism is social rather than training-time.
The relevant shared concern is that repeated reuse without fresh grounding can
degrade fidelity.

## Background-Only References

Use these sparingly, mainly in a survey sentence or appendix:

- AgentVerse
- MetaGPT
- ChatDev
- AgentScope
- ReAct
- AIOS
- Agent Hospital
- Evaluating Hallucinations in Chinese Large Language Models
- UHGEval
- ANAH-v2

## Maybe References

Use only if a draft paragraph needs them:

- Artificial Hivemind
- PRD: Peer Rank and Discussion Improve LLM based Evaluations
- Multi-Agent LLM Debate Unveils the Premise Left Unsaid
- CONSENSAGENT
- CortexDebate
- SELENE
- Delusions of Large Language Models

## Replace / Do Not Cite As Independent Entries

- Index 1: duplicate of the Generative Agents UIST paper.
- Index 3: duplicate of the Multiagent Debate paper.
- Index 5: duplicate of TruthfulQA.
- Index 9: duplicate / alternate record for The Curse of Recursion.
- Index 55: local PDF does not appear to be the intended Scientific Reports
  article on emotion and rumor diffusion. Replace from official source before
  using any claim from it.

## Related Work Paragraph Order

1. Agent societies make communication a real substrate.
2. Prior work often measures spread, task success, or judged answer quality.
3. Misinformation and factuality work show why truth requires semantic
   measurement, not fluency or reach.
4. Memory and correction work show why exposure is not durable state.
5. Telephone's contribution: controlled social transmission with separate
   HEARD, SAID, and HELD measurements.
