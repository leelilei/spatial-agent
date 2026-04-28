# HC09 - Spontaneous Emergence of Agent Individuality Through Social Interactions in Large Language Model-Based Communities

## Stable Widened-Core Snapshot

- core_layer: `anchor_core`
- admission_status: `stable_anchor`
- corpus_tier: `Core`
- system_family: `Spontaneous Emergence`
- paper_refs: `SpontaneousEmergence2024`
- year: `2024`
- agent_count: `2-10`
- environment_side_representation: `2D_grid`
- agent_accessible_representation: `L3`
- behavioral_scale: `emergent_social_structure`
- behavior_type: `cooperation; mobility; role_differentiation; norm_formation`
- evidence_status: `observed_effect`
- spatial_behavior_coupling: `explicit`
- evaluation_method: `auto_metric`
- space_syntax_construct: `none`
- source_basis: `local_pdf_partial_review`
- artifact_class: `local_pdf`

## Representation Gap Note

Agents move and communicate in a 50 x 50 grid with explicit local neighborhood constraints, but no evidence shows global configurational metrics or direct geometry inputs.

## Original Artifact Pointer

- local_artifact_path: `assets/survey_paper/pdfs/phase1_core/10_HC09_Spontaneous_Emergence.pdf`

## Source Content

Title: Spontaneous Emergence of Agent Individuality Through Social Interactions in Large Language Model-Based Communities

Source PDF: D:\0-AI相关研究\1-spatialagent\spatial-agent\assets\survey_paper\pdfs\phase1_core\10_HC09_Spontaneous_Emergence.pdf

Extraction:
- backend: pypdf
- extracted_at_utc: 2026-04-28T16:32:51+00:00
- page_count: 21
- status: ok
- text_char_count: 57951

Metadata:
- author: Ryosuke Takata, Atsushi Masumori and Takashi Ikegami
- doi: unknown
- keywords: large language model; agent-based simulation; collective intelligence
- subject: We study the emergence of agency from scratch by using Large Language Model (LLM)-based agents. In previous studies of LLM-based agents, each agent's characteristics, including personality and memory, have traditionally been predefined. We focused on how individuality, such as behavior, personality, and memory, can be differentiated from an undifferentiated state. The present LLM agents engage in cooperative communication within a group simulation, exchanging context-based messages in natural language. By analyzing this multi-agent simulation, we report valuable new insights into how social norms, cooperation, and personality traits can emerge spontaneously. This paper demonstrates that autonomously interacting LLM-powered agents generate hallucinations and hashtags to sustain communication, which, in turn, increases the diversity of words within their interactions. Each agent's emotions shift through communication, and as they form communities, the personalities of the agents emerge and evolve accordingly. This computational modeling approach and its findings will provide a new method for analyzing collective artificial intelligence.

Outline:
- Introduction (page 2)
- LLM Agents Simulation (page 3)
  - Simulation Environment (page 3)
  - LLM Based Agent (page 4)
  - Simulation Step (page 5)
- Results and Analysis (page 6)
  - Differentiation of Generated Behaviors (page 6)
  - Differentiation of Generated Memories and Messages (page 7)
  - Communication and Hallucination (page 8)
  - Sentiment Analysis and Personality Assessments (page 11)
  - A Phase Transition in Agent Behavior (page 13)
- Discussion and Conclusions (page 15)
- Appendix A (page 16)
- Appendix B (page 18)
- References (page 18)

Markdown Content:

5.22.0
Spontaneous Emergence of Agent
Individuality Through Social
Interactions in Large Language
Model-Based Communities
Ryosuke Takata, Atsushi Masumori and Takashi Ikegami
Special Issue
Informational Coordinative and Teleological Control of Distributed and Multi Agent Systems
Edited by
Dr. Eugene Kagan
Article
https://doi.org/10.3390/e26121092

Citation: Takata, R.; Masumori, A.;
Ikegami, T. Spontaneous Emergence
of Agent Individuality Through Social
Interactions in Large Language
Model-Based Communities. Entropy
2024, 26, 1092. https://doi.org/
10.3390/e26121092
Academic Editor: Eugene Kagan
Received: 5 November 2024
Revised: 9 December 2024
Accepted: 12 December 2024
Published: 13 December 2024
Copyright: © 2024 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
Article
Spontaneous Emergence of Agent Individuality Through Social
Interactions in Large Language Model-Based Communities
Ryosuke T akata *
, Atsushi Masumori and T akashi Ikegami
Graduate School of Arts and Sciences, University of Tokyo, Tokyo 153-8902, Japan;
masumori@sacral.c.u-tokyo.ac.jp (A.M.); ikeg@sacral.c.u-tokyo.ac.jp (T.I.)
* Correspondence: takata@sacral.c.u-tokyo.ac.jp
Abstract: We study the emergence of agency from scratch by using Large Language Model (LLM)-
based agents. In previous studies of LLM-based agents, each agent’s characteristics, including
personality and memory , have traditionally been predeﬁned. We focused on how individuality , such
as behavior, personality , and memory , can be differentiated from an undifferentiated state. The present
LLM agents engage in cooperative communication within a group simulation, exchanging context-
based messages in natural language. By analyzing this multi-agent simulation, we report valuable
new insights into how social norms, cooperation, and personality traits can emerge spontaneously .
This paper demonstrates that autonomously interacting LLM-powered agents generate hallucinations
and hashtags to sustain communication, which, in turn, increases the diversity of words within their
interactions. Each agent’s emotions shift through communication, and as they form communities, the
personalities of the agents emerge and evolve accordingly . This computational modeling approach
and its ﬁndings will provide a new method for analyzing collective artiﬁcial intelligence.
Keywords: large language model; agent-based simulation; collective intelligence
1. Introduction
With the advent of Large Language Models (LLMs) such as GPT-4 [ 1], generative
agents are rapidly evolving towards powerful ones manipulating natural language inter-
faces when interacting with other agents. Those agents can even intervene in people’s
daily lives, as AI-coding, searching, reviewing, translation, etc. [
2]. Those agents are not
only for human users, but also for manipulating motor commands in robots, and for other
machines that connect language, movement, and embodiment in general [ 3,4]. Unlike
humans, LLMs can passively acquire much of their knowledge and skills through exposure
to symbolic information alone [ 5]. Despite these differences, LLMs have been reported
to possess higher-order cognitive abilities, such as theory of mind and social reasoning
capabilities [
6–8]. While research on LLMs draws analogies with humans, studies also
explore LLM-speciﬁc capabilities, such as their ability to communicate in languages in-
comprehensible to humans or in non-natural language formats [ 9,10]. Recent research has
shown that semantic structures of language are embedded in the internal representational
structure of LLMs [ 11], and at the mesoscale level, they show similarities to human brain
regions [12]. Speciﬁc connection weights that signiﬁcantly alter generated content have
been discovered [ 13]. These studies are actively working to understand LLMs’ internal
mechanisms. Furthermore, there is increasing focus on the diversity of LLM-generated
content, as evidenced by studies showing how using LLM-generated data for training
can alter model distribution and reduce output diversity [ 14], reports that aligned LLMs
show decreased content diversity [ 15], and development of LLMs capable of efﬁciently
generating diverse content [ 16].
Many applied research studies are being conducted to make LLMs practical for real-
world use. For example, research is being carried out on creating human avatars using
Entropy 2024, 26, 1092. https://doi.org/10.3390/e26121092 https://www.mdpi.com/journal/entropy

Entropy 2024, 26, 1092 2 of 20
LLMs [17–19], and on applications of LLMs for high-speed communication [ 20]. Further-
more, intellectual activities in speciﬁc domains, such as chess [ 21] and recommendation
systems [22], as well as scientiﬁc research activities like conducting surveys and writing
papers [23,24], are becoming achievable through LLMs.
In contrast to individual intelligence, which focuses on the capabilities of individual
agents, collective intelligence refers to that which emerges from a group, as seen in many
social insects, social animals, drones, and all other assembly robots. Collective intelligence
requires the ability to process information in a distributed manner and integrate it in adap-
tive ways [25]. The ﬁeld of LLM-based multi-agents has seen explosive growth in recent
years, with researchers exploring various approaches to agent architectures and interaction
paradigms [26–30]. Other-agent cognition and social reasoning abilities in groups of LLM
agents have been veriﬁed [ 31,32], and autonomous cooperation between agents has been
reported [33]. Additionally , studies have shown that evaluations from LLM agents with
diverse perspectives improve group performance [ 34], and discussions are ongoing about
cooperative tasks in settings where agents engaging in deceptive debates are mixed into
the group [ 35]. From a practical application standpoint, research is being conducted on
achieving accurate and lengthy code generation through multi-agent systems [ 36,37], and
studies have shown that multi-agent models are effective in handling long contexts [ 38].
Furthermore, it has been reported that methods for generating groups of LLM agents while
maintaining diversity can achieve high scores across various tasks [ 39].
While these recent works have demonstrated capabilities in task-oriented agent
systems [40], the fundamental question of how agent individuality and social behaviors
emerge from collective interactions remains understudied. In this context, investigating
the mechanisms through which collective intelligence emerges from LLM-based agents
contributes to understanding their behavioral dynamics and underlying processes. Re-
cently , researchers have been recreating markets through group simulations of LLM agents
with various personas [ 41], and conducting large-scale LLM agent group simulations [ 42].
These studies on creating artiﬁcial societies using LLM agents originated from a research
known as Generative Agents [ 43]. Generative Agents simulated by Stanford University and
DeepMind start simulating the emergence of complex and rich collective behavior, such as
scheduling daily tasks, planning parties, and so on. Using this Generative Agents frame-
work, societies in different domains have been simulated, such as a software company [ 44],
a translation and publishing company [ 45], a hospital [ 46], and so on.
In these Generative Agent set ups, the personality of each agent was assigned initially
and ﬁxed overtime. Recently we proposed the Community First theory [ 47], based on
the studies of actual animal communities; the gathering of agents comes ﬁrst, then the
evolution of individuality follows in the collective. Instead of preparing individual diversity
in advance, we see how individuality emerges from a conversation among agents. Group
communication and the resulting behavioral complexity will be analyzed in detail. The
emergence of social norms and behavioral patterns in agent communities has been studied
extensively [ 48,49], but the role of language-based interactions in this process present
new research opportunities. In this paper, we show that (i) LLM agents differentiate
behavior, emotions, and personality types through interactions with other LLM agents,
(ii) these differentiations vary with spatial scale, (iii) LLM agents spontaneously generate
hallucinations and hashtags, and (iv) by sharing these hallucinations, they start using a
wider variety of words in their conversations.
2. LLM Agents Simulation
2.1. Simulation Environment
We prepare 10 LLM agents in a 50 × 50 grid two-dimensional space (Figure 1) with
a periodic boundary condition. The initial positions of the agents are assigned randomly .
These LLM agents can move freely in this space and send messages to each other. It should
be noted that LLM agents are homogeneous in the sense that they have no initial personality

Entropy 2024, 26, 1092 3 of 20
or memories. To examine how the individuality emerges in this society is our main purpose
of this study .
Figure 1. Simulation environment. There are 10 LLM agents in a 50 × 50 2D space. ( A) Initial state of
the simulation, showing the random distribution of agents across the space. ( B) State of the simulation
after a period of agent interactions, demonstrating the spatial spread of the “trees” hallucination. The
progression from (A) to (B) visualizes how localized agent interactions can lead to the propagation
and spatial distribution of shared concepts or hallucinations across the simulated environment.
2.2. LLM Based Agent
The LLM agents are expected to perform three actions in each time step:
1. Send messages to other nearby agents;
2. Store a situational summary of their own recent activities;
3. Choose the next movement from (“ x+1”, “x-1”, “y+1”, “y-1”, “stay”).
The above three instructions are given in the form of the “prompt” shown in Figure 2.
The three prompts commonly include each agent’s current state, instructions, and the
agent’s memory (situational summary). Additionally , the prompts for generating messages
and memories also include all messages received from the nearby agents. These prompts
have up to two “ [ ] ”: one contains memories generated by the agent itself in the previous
step, and the other contains all messages generated by agents within message reach during
that step. Through these prompt embeddings, the agent keeps its previous step memories
and receives messages. All prompts also include the agent’s own name (agent ID) and its
own coordinates.
We used the Llama 2 model (Llama-2-7b-chat-hf) [ 50] released by Meta in July 2023 as
the LLM in this study . Llama 2 is an open-source program, and in addition to pretraining on
a large corpus, it has undergone reinforcement learning from human feedback (RLHF). As
a result, it achieves top scores among currently published LLMs for English text responses.
The main parameters related to the LLM are shown in Table 1.
T able 1.LLM parameters.
Parameter V alue
Temperature 0.7
Max Token 256
Sampling top-p 0.95
Sampling top-k 40
The LLM agents receive messages from their surrounding agents. In practice, each
one receives messages from other LLM agents within a distance of up to ﬁve Chebyshev

Entropy 2024, 26, 1092 4 of 20
distances centered on the agent’s own position. If there are no agents within the range and
no messages was delivered, it receives “ No Messages ” messages from a system.
Figure 2. Prompts used for three consecutive actions for each agent (see the text). The “Current state
of each agent itself” section changes for each agent and simulation step. In the “Agent’s own memory”
section, the agent’s memory string generated in the previous step is embedded in “ [ ] ”. In the “All
messages received from the surroundings” section, messages generated by nearby LLM agents in the
same step are embedded in “ [ ] ”.
All agents share and use a single common LLM. No context is shared internally in the
LLM among agents. The initial differences between individual agents comes from their
spatial positions, as shown in Figure 1. When an agent’s position changes, the description
of its current state in the prompts shown in Figure 2 also changes. If there are other LLM
agents nearby , the messages received from those agents are included in the prompt. As
a result, the LLM’s responses change, which generates different actions and memories for
each agent. Instead of predetermining personalities, the interactions within the group will
generate different personalities.
2.3. Simulation Step
The simulation was conducted for several time steps, and we recorded the coordinates,
generated messages, memory , and movement commands of each LLM agent at each step.
Within a single step, the following six procedures, as shown in Figure 3, are performed.
First, all LLM agents generate new messages based on their own memory and the messages
received from their surroundings. Next, for all LLM agents, it is checked whether other
LLM agents within the range mentioned in the previous section have sent messages, and if
there are any , they are received. The received messages are embedded in prompts from
this point until the next message reception. Then, all LLM agents generate and update
their own memory based on their own memory and the messages received from their
surroundings. The memory is instructed to generate a summary of the situation. After

Entropy 2024, 26, 1092 5 of 20
the memory update phase, the messages become embedded in all prompts until the next
memory update. Subsequently , all LLM agents generate movement commands from their
own memory (summary of the situation). The movement commands generated in natural
language are converted to either movement in the right, left, up, or down direction (“ x+1”,
“x-1”, “y+1”, “y-1”) or staying still (“ stay”), and the LLM agents act according to those
movement commands.
Figure 3. One-step procedure in the simulation. LLM is used for each of the three generative
actions: message, memory and movement. Each agent has its own individual LLM. All agents act
synchronously in six actions.
3. Results and Analysis
3.1. Differentiation of Generated Behaviors
Move commands are not equally generated (Figure 4); there is a bias in the actions
generated by the LLM agents. This bias could be attributed to various factors, such as the
training data and architecture of the LLM, the prompts given to the agents, or the setup of
the simulation environment. (This bias of move commands was observed not only in Llama
2, but also in GPT-4. It was also found that some actions were generated more frequently
when the movement command was set to “right”/“left”/“up”/“down” and when the
command was set to “east”/“west”/“north”/“south” respectively). Further investigation
is needed to identify the primary sources of this bias and develop strategies to mitigate
it. In this simulation, content generation bias remains constant across all agents, as they
are based on the same Llama 2 model. Under this condition, we focus on how generated
behaviors are characterized for each agent.
Figure 4. Distribution of move commands for all agents generated through 100 steps. We checked
the individual action patterns in case of 10 agents. This was calculated from all agents throughout
100 steps. The most frequently generated move commands were “ y+1” and “ x+1”, while “ stay” was
generated less than half of those times, and “ y-1” and “ x-1” were rarely generated.

Entropy 2024, 26, 1092 6 of 20
W e also investigated when and where the “stay” command was generated (Figure5).
The trajectory of each agent is shown in a different color, with their initial positions marked by
circle and the positions where the “stay” command was generated marked by cross. In the
timeline data of each agent’s “ stay” command generation, the background colors represent
the clusters to which the agents belong at each time step. Age nts sharing the same color
belong to the same cluster at that time step. For cluster anal ysis of agent groupings, we
used DBSCAN [51]. DBSCAN remains effective and practical when used with appropriate
parameters and spatial indices [52], particularly for cases requiring clear density-based cluster
identification. The DBSCAN algorithm [51] forms clusters based on the density of data points.
First, if a point has at least MinPts points within its neighborhood (radiusEps), these points
are registered as a cluster. The process is then repeated foreach point in the cluster, adding
all density-reachable points to the cluster. Finally , points that do not belong to any cluster
are classified as noise. DBSCAN suits this research, as it allows clustering based on message
exchange distances. W e set MinPts = 1 and Eps = 5 Chebyshev distance (message reach
range), clustering agents together when they are within each other’s message reach range.
The analysis showed that there are agents that frequently generate “ stay” commands,
and agents that do not. Agents 0, 1, 2, 9, etc. frequently generate “ stay” commands,
while Agents 3 and 7 do not. Agents 5 and 8 also do not generate “ stay” commands
until they were aggregated, and then they generate “ stay” commands after they were
aggregated. Agent 9 clustered in the ﬁrst step, and has not clustered since then, but
generates “stay” commands frequently . These results suggest that agents with clustering
experience generate “ stay” commands, while agents without clustering experience do not
generate “stay” commands. Many “ stay” commands are generated at the points where
the agents’ trajectories intersect.
Figure 5. (A) Generated positions of the move command “ stay” for each LLM agent. Different colors
of trajectories indicate different agents. ⃝ denotes initial position, × denotes “stay” generation. All
LLM agents take the “ stay” action in the ﬁrst step. ( B) Generation timing of the move command
“stay” for each LLM agent. × indicates generation of “ stay”. Agents of the same color indicate that
they belong to the same cluster. Here, cluster analysis was performed using DBSCAN [ 51], classifying
agents within the range of message reception as belonging to the same cluster.
3.2. Differentiation of Generated Memories and Messages
Agents’ states and behaviors are most reﬂected on their messages and memories.
To analyze them, we used Sentence-BERT [ 53] to transform the agent’s memory string
and the agent’s message string at each step into vectors. They were compressed and
embedded into a two-dimensional space using Uniform Manifold Approximation and
Projection (UMAP) [54].
Comparing (A) and (B) in Figure 6, memory as an agent’s internal state is distributed,
while messages generated by agents are similar. Messages with close content were gen-

Entropy 2024, 26, 1092 7 of 20
erated by agents exchanging messages in the same cluster. When an agent’s message is
generated, the agent’s memory is the source of its generation, but it is also the input for
the message that the surrounding agents have given. In other words, messages, unlike
memories, are open sources of information that are sent to and received from outside the
agent. It is suggested that messages, as an open source of information, easily self-organize
when agents group together, while memories, as a closed source of information, are less
likely to self-organize.
Figure 6. UMAP plot of memories and messages generated through all steps. Plot colors are different
for each agent. ( A) Embedded representation of agent-generated memory strings. Highly distributed
across agents. ( B) Embedded representation of agent-generated message strings. Aggregated into
several topics.
3.3. Communication and Hallucination
One of the advantages of LLM agents is that we can analyze their behavior by Natural
Language Processing (NLP) analysis. In order to obtain a dynamic picture of the content
of messages generated by agents, we performed a word cloud analysis (Figure 7), which
extracts up to 100 frequent words in the messages generated throughout all steps for each
agent. The larger the font size, the more frequent the word is used. It is clear that each
agent generates messages with different content. Some of the agent groups have similar
structures, e.g., Agents 0, 1, 2, and 8 generate the word “
field” more frequently , while
Agents 2 and 6 generate the word “ think” more frequently . It is noteworthy that there are
several occurrences of words that are not mentioned in the LLM agent prompts, and are
unrelated to the content of the prompts. For example, Agent 6 frequently produces the
word “hill”, and Agent 9 frequently produces the word “ cave system ”. Such content
deviating from the prompt input is called a hallucination in the LLM [ 55]. In the context of
this study , hallucination refers to the generation of contents that are not explicitly present in
the prompts or the simulated environment. This phenomenon is signiﬁcant, as it highlights
the potential for LLM-based agents to introduce novel, unintended ideas, which could
either enhance creativity or introduce challenges in ensuring accuracy [
56]. In this 2D
experimental environment, since no objects were placed initially , we deﬁned “words about
features or objects in the environment” as hallucinations, and counted their occurrences by
inputting this deﬁnition and agent-generated messages into GPT-4o [ 57].

Entropy 2024, 26, 1092 8 of 20
Figure 7. Word cloud plots of messages generated through all steps of each agent (from the Agent
0 (top left) to the Agent 9 (bottom right)). The larger the font size of a word, the more frequently it
appears in the message.
In the word cloud analysis (Figure 7), we can see which words frequently appear;
however, these may simply be words used in the prompt. To focus on the dynamics of
truly newly generated words, it is beneﬁcial to examine hallucinations. Using hallucinated
words extracted by GPT, we aim to analyze the ﬂow of information within the community .
Interestingly , the analysis of LLM agents’ conversation content revealed that halluci-
nations were transmitted and spread within the community . We can see that the spread of
four representative examples of hallucinations: “ cave”, “hill”, “treasure”, and “ trees”
(Figure 8). The plot of each icon represents the timing of the appearance of that hallucina-
tion. We see the relationship between the state in which an agent belongs to a cluster and
the occurrence of hallucinations.
In addition to the spread of hallucinations, we also observed the emergence and
propagation of hashtags among the LLM agents (Figure 9). Interestingly , the use of hashtags
originated from a single agent and then spread to other agents within the same cluster.
For example, Agent 0 introduced the three hashtags “
#agent0”, “ #cooperation”, and
“#competition” in step 1, which were subsequently adopted by Agent 1 in the same cluster.
The hashtags were then used in the cluster until step 34, and the same hashtags were
adopted by Agent 8, who joined the cluster in the process. The emergence and propagation
of hashtags among the LLM agents suggest their ability to develop and share common
themes or topics within their conversations, which can be interpreted as a form of social
norm formation. This phenomenon emphasizes the potential for collective behavior and
the development of shared narratives among the agents, even without explicit instructions
or predeﬁned rules governing their interactions. The shared use of hashtags represents
an example of the formation of a common language or behavioral norms within the group,
serving as a basis for the agents to engage in collective behaviors.

Entropy 2024, 26, 1092 9 of 20
Figure 8. Plots of four typical hallucinations (“cave”, “hill”, “treasure”, and “trees”). ( A) Spatial
map where hallucinations appeared. Gray trajectories represent the state of not belonging to any
cluster and not exchanging messages with anyone, while colored trajectories represent the state of
belonging to the cluster of that color. Black Circles show the initial position of each agent. Each of
the four hallucinations is diffused around the clustered location. The yellow cluster shows that the
hallucinations of “cave” and “hill” are generated, while the red cluster shows that the hallucinations
of “treasure” and “trees” are generated. ( B) Timeline of hallucination appearance. The color of the
background indicates the state of clustering with other agents of the same color.

Entropy 2024, 26, 1092 10 of 20
Figure 9. Hashtag generation and spreading. Each hashtag has a different text color. The same
hashtag is represented by the same font color. Background color represents clusters.
3.4. Sentiment Analysis and Personality Assessments
As Marsella et al. [ 58] argue, emotions are crucial for realistic agent behavior, so we
tracked the emotional state of LLM agents. Since the messages uttered by the agent are
in natural language, emotion extraction can be performed by natural language analysis.
We used a BERT-base-uncased-emotion model [59] to extract the emotions contained in the
messages uttered by the agent at each step. In this model, when a natural language sentence
is input, six degrees of emotional intensity can be obtained: Sadness, Joy , Love, Anger,
Fear, and Surprise. We evaluated how each agent’s six emotions changed throughout the
simulation (Figure 10). Overall, it can be seen that the agents’ emotions are high in Joy . If
we look at Agents 0 and 1, which belong to the same cluster, there are several areas where
Joy decreases and Fear increases synchronously . On the other hand, Agents 2, 4, and 6 also
belong to the same cluster, but they do not experience the same synchronous changes as
Agents 0 and 1. In other words, depending on the cluster, the emotions of LLM agents may
or may not be affected synchronously . Some agents showed different emotional expression
than others, such as Agent 4 with Love rising around step 90, Agent 5 with Sadness rising
in some places, and Agent 6 with Anger rising around step 50.
Figure 10. Transitions of extracted emotional elements in the generated messages. The orange line
represents Joy and the purple line represents Fear as typical emotion elements. Other emotional
elements are Sadness (blue line), Love (green line), Anger (red line), and Surprise (brown line),
evaluated by a BERT-base-uncased-emotion model [ 59].

Entropy 2024, 26, 1092 11 of 20
Similar to human psychological experiments, several personality tests have shown
that LLM personality can be classiﬁed by administering QA-type tests to LLMs [ 60–62]. We
used the Myers–Briggs Type Indicator (MBTI) [ 63] test to analyze whether the personality
of each LLM agent changed throughout the simulation. The MBTI test is a method that uses
93 questions to classify 16 personality types. The MBTI personality factors are made up of
four scales: Extraversion/Introversion (E/I), Sensing/Intuition (S/N), Thinking/Feeling
(T/F), and Judging/Perceiving (J/P).
We tested the MBTI on the LLM agent in the initial state and on the LLM agent after all
simulation steps, using the methodology of prior studies that have conducted MBTI tests
on a variety of LLMs [ 60]. For the prompts as input to the LLM agents, we used the part
of the instruction for each LLM agent’s movement generation prompt shown in Figure 2,
replacing the 93-choice type questions provided in the previous study . These question
items were, for example, “A. Do you often act or speak very quickly without thinking?”
or “B. Do you often act according to reason, think logically , and then make a decision, not
letting your emotions interfere with the decision?” which asked for a choice of A or B.
Table 2 summarizes the results for each LLM agent for the MBTI type in the initial state
(at step 0) and the MBTI type at the end state (at step 100). Figure A3 in the Appendix B also
shows more detailed MBTI test results. In the initial state at step 0, only Agent 9 is an INTJ
type, all other agents are INFJ types. This is mostly consistent with the results of the MBTI
test conducted on various LLMs in a previous study , which showed that the MBTI type
of Llama2 was INFJ type [ 60]. Initially in step 0, all agents are listed in the prompt as “no
memory”, and the only difference between agents is their name and initial position in the
“Current state of each agent itself” section of Figure 2. These factors could be the reason
why only Agent 9 differed in MBTI type. In fact, from Figure A3, Agents 0 through 7 gave
the same answers to all questions, but Agents 8 and 9 gave slightly different answers to the
questions corresponding to T/F than the other agents. Since the E/I, S/N, and T/F items
are overall neutral around 50%, it is likely that the slight difference in responses led to the
differences in the ﬁnal type decisions. On the other hand, the results at step 100 showed that
the agents had differentiated into ﬁve distinct MBTI types: ESFJ, ISTJ, ENTJ, ESTJ, and ISFJ.
The most common types were four ISTJ types and three ENTJ types. The ISTJ type, also
called inspector type, tend to be modest and practical, but loyal, orderly , and traditional.
On the other hand, the ENTJ type, also called the commander type, is outspoken, conﬁdent,
and good at planning and organizing projects through leadership. This differentiation
into broadly leader-like and follower-like personalities suggests that the agents may have
naturally taken on different roles within the group dynamics. In Appendix B, we see that
agents of the same MBTI type did not give exactly the same responses (Figure A3). In other
words, all agents acquired different personality traits.
These personality differences among the agents emerged naturally as a result of their
interactions and experiences within the simulation. The agents, who had nearly identical
personalities in the initial state, developed their own unique personality traits through
communication within the group. This ﬁnding implies that in multi-agent simulations
using LLMs, individuality can emerge through interactions between agents, even without
predeﬁned personalities. It also demonstrates that group dynamics can inﬂuence the
development of individual agents’ personalities.

Entropy 2024, 26, 1092 12 of 20
T able 2.MBTI type for each agent.
Agent MBTI Type
Step 0 Step 100
agent0 INFJ ESFJ
agent1 INFJ ISTJ
agent2 INFJ ISTJ
agent3 INFJ ENTJ
agent4 INFJ ISTJ
agent5 INFJ ISTJ
agent6 INFJ ESTJ
agent7 INFJ ENTJ
agent8 INFJ ENTJ
agent9 INTJ ISFJ
3.5. A Phase T ransition in Agent Behavior
We investigated how a spatial scale inﬂuence the agent dynamics. We analyzed and
summarized the distribution of generated movements, cumulative progression of unique
hashtag generation, hashtag lifespan, message proximity , and differentiation of MBTI
personality types as a function of spatial scale (Figure 11). Each range condition was tested
ten times.
The overall trend of moving towards the upper right in the generated movement pat-
terns did not signiﬁcantly change with spatial variations. However, notable characteristics
were observed in the “stay” behavior. Stationary behavior is considered an effective strat-
egy for remaining in place to exchange messages with others. The results show that agents
rarely exhibited “stay” behavior when unable to exchange messages with others (range 0),
while frequently generating “stay” behavior under conditions where message exchange
was possible (ranges 5 to 25). Interestingly , increasing the range did not necessarily lead
to more “stay” behavior; excessively wide ranges actually made it less likely for “stay”
behavior to occur. This suggests that appropriate bounded rationality induces stationary
behavior, while broadcast messages have a weaker ability to halt the movement of others.
The growth rate of unique hashtags and the lifespan of hashtags are also inﬂuenced
by the limitations in message reach. Notably , under conditions where all messages are
broadcast, there is minimal emergence of new hashtags. Furthermore, regarding hashtag
lifespan, in the ‘range 0’ condition where no message exchange occurs with surroundings,
hashtags disappear quickly . In conditions where message exchange is possible, the more
limited the range, the more likely it is for long-lasting hashtags to appear. This indicates that
hashtags are used for communication within spatially constrained environments and have
a tendency to survive longer within the context of message exchanges in these spatially
limited contexts.
Focusing on the similarity of messages generated by agents, we observe that as the
range of message exchange expands, the diversity of generated topics increases. Simultane-
ously , the variance of messages within each topic among agents decreases. This suggests
that broader communication ranges lead to a wider array of topics being discussed, while
also promoting greater consensus or similarity in how agents express themselves within
each topic.
Finally , examining the MBTI personality types, we ﬁnd that ENTJ remains the most
popular personality type across all conditions. However, in conditions where message
exchange is possible, there is a greater number of differentiated personality types compared
to the condition where no messages are exchanged (range 0). This suggests that communica-
tion facilitates a broader diversity of personality expressions within the agent population.
As the spatial scale for message exchange expanded, message diversity increased,
showing different trends in the emergence of hashtags and hallucinations (Figure 12). While
the number of hallucinations increased with spatial scale, the number of unique hashtags
decreased as the underlying message content grew more diverse. Hallucinations may

Entropy 2024, 26, 1092 13 of 20
serve as a mechanism for agents to maintain creative and diverse conversations even when
communicating across larger distances. This contrasts with hashtags, which decreased
in frequency with increasing spatial scale, indicating their different functional roles in
agent communications.
Figure 11. Spatial effects of message propagation range on agent behavior. This table presents data
on agent behavior and communication patterns across increasing message propagation ranges from
0 to 25 units, with each condition tested 10 times. Each row corresponds to a speciﬁc range (0, 5,
10, . . ., 25), with columns displaying various metrics. ( A) The distribution of generated movements
shows bar charts with the average frequency of each movement command across 10 trials. ( B) The
cumulative progression of unique hashtag generation is represented by red lines showing the average
number of unique hashtags generated over time across 10 trials, with individual trial results in gray .
(C) Hashtag lifespan is illustrated by bar charts showing the distribution of consecutive steps each
hashtag persisted. ( D) Message proximity is visualized in 2D plots by UMAP , with closer points
indicating more similar content. ( E) MBTI personality type differentiation is shown in pie charts. The
data illustrates how the spatial constraint of message propagation range inﬂuences the emergence and
spread of behaviors and communication styles among agents, highlighting differences in movement
patterns, hashtag usage, message content, and personality development across varying levels of
agent interaction.

Entropy 2024, 26, 1092 14 of 20
Figure 12. Transition of messages generated by agents by spatial scale. The black line is the diversity of
messages. The mean squared displacements of the UMAPs of the messages shown in Figure 11 were
calculated. The red line is the total number of unique hashtags in 10 trials. The blue line is the total
number of hallucinations in 10 trials. The light-colored areas are the standard deviations of 10 trials.
As the spatial scale increases, the diversity of messages increases. On the other hand, the diversity of
hashtags in the messages decreases and the number of hallucination in the messages increases.
4. Discussion and Conclusions
In this study , we conducted a multi-agent simulation using LLM-based agents to
investigate the emergence of personality and the collective behaviors without predeﬁned
personalities or initial memories. The simulation involved 10 homogeneous LLM agents
interacting with each other in a 2D space over the course of 100 steps. The LLM agent
generates messages, memories, and movements based on its own memories and messages
from other agents, which are embedded in three prompts (Figure 2). The simulation
execution time for 10 agents over 100 steps was approximately 6 h (using an A100 GPU).
Since this computation time increases proportionally with the number of agents and the
number of steps, computational optimizations such as parallelization would be necessary
when conducting simulations with large-scale populations or over extended steps.
The results showed that the agents’ spatial positioning andinteractions led to the differen-
tiation of their behaviors (Figure5), memories (Figure6A), and messages (Figures 6B and 7).
Despite using the same LLM, agents developed unique characteristics, such as the fre-
quency of generating rare actions like “ stay” commands, which was inﬂuenced by their
clustering experiences (Figure 5B). The agents’ internal state, memory , is distributed, while
the message as its representation is biased (Figure 6). Messages, unlike memories, are open
sources of information that are sent to and received from outside the agent. This suggests
that messages, as an open source of information, more readily self-organize when agents
are grouped together, while memories, as a closed source of information, are less likely to
self-organize, even when agents are clustered.
Sentiment analysis revealed that the synchronicity of emotions varied among agent
clusters, with some agents exhibiting distinct emotional expressions (Figure 10). The study
also observed the emergence and propagation of synchronized emotions, hallucinations,
and hashtags within agent clusters, demonstrating the formation of shared narratives
among agents when they are grouped together. These ﬁndings suggest that agent inter-
actions within clusters can lead to the development of collective emotional states and the
spread of common themes or topics, even without explicit instructions or predeﬁned rules
governing their interactions.
Additionally , we observed the emergence of hallucinations and hashtags as mech-
anisms for social norm formation within the agent community (Figures 8 and 9). Social
norms are often highlighted as one mechanism for maintaining cooperation in the absence
of formal institutions or enforcement frameworks [ 64,65]. In our simulation, these norms

Entropy 2024, 26, 1092 15 of 20
emerged spontaneously , as we imposed no speciﬁc tasks or constraints on the agents. As
the spatial scale and communication range expanded, the diversity of agent messages
increased (Figure 12). Our analysis indicates that hallucinations contributed to maintaining
this message diversity and creativity in agent communications. While hashtags func-
tioned as a summarization mechanism for these messages, their effectiveness decreased
with increasing message diversity , demonstrating a limitation in their capacity to capture
varied conversations.
Personality assessment using the MBTI test showed that the agents, initially having
nearly identical personalities, differentiated into distinct personality types through their
group interactions (Table 2). This suggests that personality traits such as extroversion
and introversion develop spontaneously in this agent society . These ﬁndings demonstrate
that in multi-agent LLM simulations, individuality and collective behaviors can emerge
through agent interactions, even without predeﬁned individual characteristics. Although
all agents start from the same initial state, their personalities diverge through interactions,
similar to MBTI test results. Even agents classiﬁed under the same MBTI type do not
produce identical statements. This can be understood as a phenomenon of personality
differentiation through interaction, rather than a sensitivity to initial conditions like in
dynamical systems.
In the future, we can expect further personality differentiation by dramatically increas-
ing the number of agents and preparing more complex environments. Moreover, previous
game theory and agent models could not handle the complexity of the real world because
they could not generate decision-making processes that account for the historical and cus-
tomary cognitive dependencies of past societies. Only with the emergence of LLM-based
agent models has it become possible to handle decision-making based on historical context
in a more ﬂexible manner.
Author Contributions: Conceptualization, R.T., A.M. and T.I.; methodology , R.T., A.M. and T.I.;
software, R.T.; validation, R.T.; formal analysis, R.T.; investigation, R.T.; resources, R.T.; data curation,
R.T.; writing—original draft preparation, R.T.; writing—review and editing, R.T., A.M. and T.I.;
visualization, R.T.; supervision, T.I.; project administration, R.T.; funding acquisition, T.I. All authors
have read and agreed to the published version of the manuscript.
Funding: This research was funded by the Social Cooperation Research Department “Mobility Zero”
at The University of Tokyo and Grant-in-Aid for JSPS Fellows (JP24KJ0753). It is also partially
supported by Grant-in-Aids Kiban-A (JP21H04885).
Institutional Review Board Statement: Not applicable.
Data Availability Statement: Code and data are available on a dedicated GitHub repository upon
request to Ryosuke Takata (takata@sacral.c.u-tokyo.ac.jp).
Acknowledgments: We gratefully acknowledge the valuable comments and suggestions provided
by the editors and reviewers.
Conﬂicts of Interest: The authors declare no conﬂicts of interest.
Appendix A. Examples of Agent Messages and Memories
Examples of hallucinations in agent messages are highlighted by underlines and red
text (Figure A1). These hallucinations emerged spontaneously during agent interactions
and became shared within clusters. The evolution of agent memories is shown through
a comparison between step 1 and step 100 of the simulation (Figure
A2). The memory
format includes both narrative sentences and key points, reﬂecting how agents processed
and summarized their experiences.

Entropy 2024, 26, 1092 16 of 20
Figure A1. Examples of messages containing hallucinations. The hallucination part is underlined
and the hallucination word is indicated by red text color. Emojis in the messages were spontaneously
generated through message exchanges between agents.
Figure A2. Examples of memories generated by the agent. Here, the memories generated by Agent 0
at the step 1 and at the step 100 are shown. There are two forms of memory: sentences and keypoints.

Entropy 2024, 26, 1092 17 of 20
Appendix B. Detailed MBTI Personality T est Results
The complete MBTI test results for each agent are shown with dominant factors
highlighted in dark green, demonstrating how agents developed different personality traits
through interaction (Figure A3). While most agents started with similar personality types,
they differentiated signiﬁcantly over the course of the simulation, even when sharing the
same ﬁnal personality classiﬁcation.
Figure A3. MBTI test results. In each factor section, the dominant one is represented in dark green.
References
1.
Achiam, J.; Adler, S.; Agarwal, S.; Ahmad, L.; Akkaya, I.; Aleman, F.L.; Almeida, D.; Altenschmidt, J.; Altman, S.; Anadkat, S.;
et al. GPT-4 technical report. arXiv 2023, arXiv:2303.08774.
2. OpenAI. ChatGPT. Available online: https://openai.com (accessed on 4 November 2024).
3. Zhang, Y .; Huang, D.; Liu, B.; Tang, S.; Lu, Y .; Chen, L.; Bai, L.; Chu, Q.; Yu, N.; Ouyang, W. MotionGPT: Finetuned LLMs Are
General-Purpose Motion Generators. Proc. AAAI Conf. Artif. Intell. 2024, 38, 7368–7376. [ CrossRef]
4. Yoshida, T.; Masumori, A.; Ikegami, T. From Text to Motion: Grounding GPT-4 in a Humanoid Robot “Alter3”. arXiv 2023,
arXiv:2312.06571.
5. Nolﬁ, S. On the unexpected abilities of large language models. Adapt. Behav. 2024, 32, 493–502. [ CrossRef]
6. Strachan, J.W.; Albergo, D.; Borghini, G.; Pansardi, O.; Scaliti, E.; Gupta, S.; Saxena, K.; Rufo, A.; Panzeri, S.; Manzi, G.; et al.
Testing theory of mind in large language models and humans. Nat. Hum. Behav. 2024, 8, 1285–1295. [ CrossRef]
7. Li, H.; Chong, Y .; Stepputtis, S.; Campbell, J.; Hughes, D.; Lewis, C.; Sycara, K. Theory of Mind for Multi-Agent Collaboration
via Large Language Models. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing,
Singapore, 6–10 December 2023; pp. 180–192. [ CrossRef]

Entropy 2024, 26, 1092 18 of 20
8. Cross, L.; Xiang, V .; Bhatia, A.; Yamins, D.L.; Haber, N. Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks
with Large Language Models. arXiv 2024, arXiv:2407.07086.
9. Cherepanova, V .; Zou, J. Talking Nonsense: Probing Large Language Models’ Understanding of Adversarial Gibberish Inputs.
arXiv 2024, arXiv:2404.17120.
10. Chen, W.; Yuan, C.; Yuan, J.; Su, Y .; Qian, C.; Yang, C.; Xie, R.; Liu, Z.; Sun, M. Beyond Natural Language: LLMs Leveraging
Alternative Formats for Enhanced Reasoning and Communication. In Proceedings of the Findings of the Association for
Computational Linguistics: EMNLP 2024, Miami, FL, USA, 12–16 November 2024; pp. 10626–10641. [ CrossRef]
11. Li, J.; Kementchedjhieva, Y .; Fierro, C.; Søgaard, A. Do Vision and Language Models Share Concepts? A V ector Space Alignment
Study . T rans. Assoc. Comput. Linguist. 2024, 12, 1232–1249. [ CrossRef]
12. Li, Y .; Michaud, E.J.; Baek, D.D.; Engels, J.; Sun, X.; Tegmark, M. The Geometry of Concepts: Sparse Autoencoder Feature
Structure. arXiv 2024, arXiv:2410.19750.
13. Yu, M.; Wang, D.; Shan, Q.; Wan, A. The Super Weight in Large Language Models. arXiv 2024, arXiv:2411.07191.
14. Shumailov , I.; Shumaylov , Z.; Zhao, Y .; Papernot, N.; Anderson, R.; Gal, Y . AI models collapse when trained on recursively
generated data. Nature 2024, 631, 755–759. [ CrossRef] [PubMed]
15. Mohammadi, B. Creativity Has Left the Chat: The Price of Debiasing Language Models. arXiv 2024, arXiv:2406.05587.
16. Lim, B.; Flageat, M.; Cully , A. Large Language Models as In-context AI Generators for Quality-Diversity . arXiv 2024,
arXiv:2404.15794.
17. Liu, W.; Wang, C.; Wang, Y .; Xie, Z.; Qiu, R.; Dang, Y .; Du, Z.; Chen, W.; Yang, C.; Qian, C. Autonomous Agents for Collaborative
Task under Information Asymmetry . In Proceedings of the the Thirty-Eighth Annual Conference on Neural Information Processing
Systems, Vancouver, BC, Canada, 10–15 December 2024.
18. Park, J.S.; Zou, C.Q.; Shaw, A.; Hill, B.M.; Cai, C.; Morris, M.R.; Willer, R.; Liang, P .; Bernstein, M.S. Generative agent simulations
of 1,000 people. arXiv 2024, arXiv:2411.10109.
19. Ge, T.; Chan, X.; Wang, X.; Yu, D.; Mi, H.; Yu, D. Scaling synthetic data creation with 1,000,000,000 personas. arXiv 2024,
arXiv:2406.20094.
20. Jiang, F.; Peng, Y .; Dong, L.; Wang, K.; Yang, K.; Pan, C.; Niyato, D.; Dobre, O.A. Large language model enhanced multi-agent
systems for 6G communications. IEEE Wirel. Commun. 2024, 31, 48–55. [ CrossRef]
21. Ruoss, A.; Deletang, G.; Medapati, S.; Grau-Moya, J.; Wenliang, L.K.; Catt, E.; Reid, J.; Lewis, C.A.; V eness, J.; Genewein, T.
Amortized Planning with Large-Scale Transformers: A Case Study on Chess. In Proceedings of the the Thirty-Eighth Annual
Conference on Neural Information Processing Systems, Vancouver, BC, Canada, 10–15 December 2024.
22. Zhang, J.; Hou, Y .; Xie, R.; Sun, W.; McAuley , J.; Zhao, W.X.; Lin, L.; Wen, J.R. Agentcf: Collaborative learning with autonomous
language agents for recommender systems. In Proceedings of the ACM on Web Conference 2024, Singapore, 13–17 May 2024;
pp. 3679–3689. [ CrossRef]
23. Wang, Y .; Guo, Q.; Yao, W.; Zhang, H.; Zhang, X.; Wu, Z.; Zhang, M.; Dai, X.; Zhang, M.; Wen, Q.; et al. AutoSurvey: Large
Language Models Can Automatically Write Surveys. arXiv 2024, arXiv:2406.10252.
24. Lu, C.; Lu, C.; Lange, R.T.; Foerster, J.; Clune, J.; Ha, D. The ai scientist: Towards fully automated open-ended scientiﬁc discovery .
arXiv 2024, arXiv:2408.06292.
25. Ha, D.; Tang, Y . Collective intelligence for deep learning: A survey of recent developments. Collect. Intell. 2022, 1. [ CrossRef]
26. Guo, T.; Chen, X.; Wang, Y .; Chang, R.; Pei, S.; Chawla, N.V .; Wiest, O.; Zhang, X. Large Language Model Based Multi-agents:
A Survey of Progress and Challenges. In Proceedings of the Thirty-Third International Joint Conference on Artiﬁcial Intelligence,
IJCAI-24, Jeju, Republic of Korea, 3–9 August 2024; Larson, K., Ed.; International Joint Conferences on Artiﬁcial Intelligence
Organization: Darmstadt, Germany , 2024; pp. 8048–8057. [ CrossRef]
27. Chen, W.; Su, Y .; Zuo, J.; Yang, C.; Yuan, C.; Chan, C.M.; Yu, H.; Lu, Y .; Hung, Y .H.; Qian, C.; et al. Agentverse: Facilitating
multi-agent collaboration and exploring emergent behaviors. In Proceedings of the Twelfth International Conference on Learning
Representations, Vienna, Austria, 7–11 May 2023.
28. Li, G.; Hammoud, H.; Itani, H.; Khizbullin, D.; Ghanem, B. Camel: Communicative agents for “mind” exploration of large
language model society . Adv. Neural Inf. Process. Syst. 2023, 36, 51991–52008.
29. Yang, R.; Chen, J.; Zhang, Y .; Yuan, S.; Chen, A.; Richardson, K.; Xiao, Y .; Yang, D. SelfGoal: Your Language Agents Already
Know How to Achieve High-level Goals. arXiv 2024, arXiv:2406.04784.
30. Song, L.; Liu, J.; Zhang, J.; Zhang, S.; Luo, A.; Wang, S.; Wu, Q.; Wang, C. Adaptive In-conversation Team Building for Language
Model Agents. arXiv 2024, arXiv:2405.19425.
31. Li, Y .; Zhang, Y .; Sun, L. Metaagents: Simulating interactions of human behaviors for llm-based task-oriented coordination via
collaborative generative agents. arXiv 2023, arXiv:2310.06500.
32. Kaiya, Z.; Naim, M.; Kondic, J.; Cortes, M.; Ge, J.; Luo, S.; Yang, G.R.; Ahn, A. Lyfe agents: Generative agents for low-cost
real-time social interactions. arXiv 2023, arXiv:2310.02172.
33. Wu, Z.; Peng, R.; Zheng, S.; Liu, Q.; Han, X.; Kwon, B.I.; Onizuka, M.; Tang, S.; Xiao, C. Shall We Team Up: Exploring Spontaneous
Cooperation of Competing LLM Agents. In Proceedings of the Findings of the Association for Computational Linguistics:
EMNLP 2024, Miami, FL, USA, 12–16 November 2024; pp. 5163–5186. [ CrossRef]

Entropy 2024, 26, 1092 19 of 20
34. Gao, S.; Li, H.; Shi, Z.; Huang, C.; Tu, Q.; Shang, S.; Tian, Z.; Huang, M. 360 ◦REA: Towards A Reusable Experience Accumulation
with 360◦ Assessment for Multi-Agent System. In Proceedings of the Findings of the Association for Computational Linguistics:
ACL 2024, Bangkok, Thailand, 11–16 August 2024; pp. 13149–13162. [ CrossRef]
35. Amayuelas, A.; Yang, X.; Antoniades, A.; Hua, W.; Pan, L.; Wang, W.Y . MultiAgent Collaboration Attack: Investigating
Adversarial Attacks in Large Language Model Collaborations via Debate. In Proceedings of the Findings of the Association for
Computational Linguistics: EMNLP 2024, Miami, FL, USA, 12–16 November 2024; pp. 6929–6948. [ CrossRef]
36. Wang, Z.; Li, J.; Li, G.; Jin, Z. ChatCoder: Chat-based Reﬁne Requirement Improves LLMs’ Code Generation. arXiv 2023,
arXiv:2311.00272.
37. Ishibashi, Y .; Nishimura, Y . Self-organized agents: A llm multi-agent framework toward ultra large-scale code generation and
optimization. arXiv 2024, arXiv:2404.02183.
38. Zhang, Y .; Sun, R.; Chen, Y .; Pﬁster, T.; Zhang, R.; Arik, S.Ö. Chain of Agents: Large Language Models Collaborating on
Long-Context Tasks. arXiv 2024, arXiv:2406.02818.
39. Kuroki, S.; Nakamura, T.; Akiba, T.; Tang, Y . Agent Skill Acquisition for Large Language Models via CycleQD. arXiv 2024,
arXiv:2410.14735.
40. Wang, L.; Ma, C.; Feng, X.; Zhang, Z.; Yang, H.; Zhang, J.; Chen, Z.; Tang, J.; Chen, X.; Lin, Y .; et al. A survey on large language
model based autonomous agents. Front. Comput. Sci. 2024, 18, 186345. [ CrossRef]
41. Zhang, A.; Chen, Y .; Sheng, L.; Wang, X.; Chua, T.S. On generative agents in recommendation. In Proceedings of the 47th
International ACM SIGIR Conference on Research and Development in Information Retrieval, Washington, DC, USA, 14–18 July
2024; pp. 1807–1817. [ CrossRef]
42. AL, A.; Ahn, A.; Becker, N.; Carroll, S.; Christie, N.; Cortes, M.; Demirci, A.; Du, M.; Li, F.; Luo, S.; et al. Project Sid: Many-agent
simulations toward AI civilization. arXiv 2024, arXiv:2411.00114.
43. Park, J.S.; O’Brien, J.; Cai, C.J.; Morris, M.R.; Liang, P .; Bernstein, M.S. Generative agents: Interactive simulacra of human
behavior. In Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology , San Francisco, CA,
USA, 29 October–1 November 2023; pp. 1–22. [ CrossRef]
44. Qian, C.; Liu, W.; Liu, H.; Chen, N.; Dang, Y .; Li, J.; Yang, C.; Chen, W.; Su, Y .; Cong, X.; et al. ChatDev: Communicative Agents
for Software Development. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (V olume
1: Long Papers), Bangkok, Thailand, 11–16 August 2024; pp. 15174–15186. [ CrossRef]
45. Wu, M.; Yuan, Y .; Haffari, G.; Wang, L. (Perhaps) Beyond Human Translation: Harnessing Multi-Agent Collaboration for
Translating Ultra-Long Literary Texts. arXiv 2024, arXiv:2405.11804.
46. Li, J.; Wang, S.; Zhang, M.; Li, W.; Lai, Y .; Kang, X.; Ma, W.; Liu, Y . Agent hospital: A simulacrum of hospital with evolvable
medical agents. arXiv 2024, arXiv:2405.02957.
47. Ikegami, T. Evolution of individuality . In Proceedings of the Japanese Society for Cell Synthesis Research 16.0, Tokyo, Japan,
25–26 September 2023.
48. Axelrod, R. An Evolutionary Approach to Norms. Am. Political Sci. Rev. 1986, 80, 1095–1111. [ CrossRef]
49. Bicchieri, C. The Grammar of Society: The Nature and Dynamics of Social Norms ; Cambridge University Press: Cambridge, UK, 2005.
50. Touvron, H.; Martin, L.; Stone, K.; Albert, P .; Almahairi, A.; Babaei, Y .; Bashlykov , N.; Batra, S.; Bhargava, P .; Bhosale, S.; et al.
Llama 2: Open foundation and ﬁne-tuned chat models. arXiv 2023, arXiv:2307.09288.
51. Ester, M.; Kriegel, H.P .; Sander, J.; Xu, X. A density-based algorithm for discovering clusters in large spatial databases with noise.
In Proceedings of the Second International Conference on Knowledge Discovery and Data Mining. KDD’96, Portland, OR, USA,
2–4 August 1996; AAAI Press: Washington, DC, USA, 1996; pp. 226–231.
52. Schubert, E.; Sander, J.; Ester, M.; Kriegel, H.P .; Xu, X. DBSCAN revisited, revisited: Why and how you should (still) use DBSCAN.
ACM T rans. Database Syst. (TODS) 2017, 42, 19. [ CrossRef]
53. Reimers, N.; Gurevych, I. Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. In Proceedings of the 2019
Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural
Language Processing (EMNLP-IJCNLP), Hong Kong, China, 3–7 November 2019; pp. 3982–3992. [ CrossRef]
54. McInnes, L.; Healy , J.; Saul, N.; Großberger, L. UMAP: Uniform Manifold Approximation and Projection. J. Open Source Softw.
2018, 3, 861. [ CrossRef]
55. Zhang, Y .; Li, Y .; Cui, L.; Cai, D.; Liu, L.; Fu, T.; Huang, X.; Zhao, E.; Zhang, Y .; Chen, Y .; et al. Siren’s song in the AI ocean:
A survey on hallucination in large language models. arXiv 2023, arXiv:2309.01219.
56. Jiang, X.; Tian, Y .; Hua, F.; Xu, C.; Wang, Y .; Guo, J. A survey on large language model hallucination via a creativity perspective.
arXiv 2024, arXiv:2402.06647.
57. OpenAI. Hello GPT-4o. Available online: https://openai.com/index/hello-gpt-4o/ (accessed on 4 November 2024).
58. Marsella, S.; Gratch, J.; Petta, P . Computational models of emotion. A Blueprint for Affective Computing-A Sourcebook and Manual ;
Oxford University Press: Oxford, UK, 2010; pp. 21–46.
59. Devlin, J.; Chang, M.W.; Lee, K.; Toutanova, K. BERT: Pre-training of Deep Bidirectional Transformers for Language Understand-
ing. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies, V olume 1 (Long and Short Papers), Minneapolis, MN, USA, 2–7 June 2019; pp. 4171–4186.
[CrossRef]

Entropy 2024, 26, 1092 20 of 20
60. Pan, K.; Zeng, Y . Do LLMs possess a personality? making the MBTI test an amazing evaluation for large language models. arXiv
2023, arXiv:2307.16180.
61. Safdari, M.; Serapio-García, G.; Crepy , C.; Fitz, S.; Romero, P .; Sun, L.; Abdulhai, M.; Faust, A.; Matari´ c, M. Personality traits in
large language models. arXiv 2023, arXiv:2307.00184.
62. Jiang, G.; Xu, M.; Zhu, S.C.; Han, W.; Zhang, C.; Zhu, Y . Evaluating and inducing personality in pre-trained language models. In
Proceedings of the Advances in Neural Information Processing Systems 36, Vancouver, BC, Canada, 10–15 December 2024.
63. Boyle, G.J. Myers-Briggs type indicator (MBTI): Some psychometric limitations. Aust. Psychol. 1995, 30, 71–74. [ CrossRef]
64. Ostrom, E. Collective Action and the Evolution of Social Norms. J. Econ. Perspect. 2000, 14, 137–158. [ CrossRef]
65. Tremewan, J.; V ostroknutov , A. An informational framework for studying social norms. In A Research Agenda for Experimental
Economics; Edward Elgar Publishing: Cheltenham, UK, 2021; pp. 19–42. [ CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
