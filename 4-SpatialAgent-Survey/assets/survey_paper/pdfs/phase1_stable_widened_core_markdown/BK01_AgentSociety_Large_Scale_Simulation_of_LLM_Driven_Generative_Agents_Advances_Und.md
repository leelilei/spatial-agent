# BK01 - AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society

## Stable Widened-Core Snapshot

- core_layer: `anchor_core`
- admission_status: `stable_anchor`
- corpus_tier: `Core`
- system_family: `AgentSociety`
- paper_refs: `Piao2025_AgentSociety`
- year: `2025`
- agent_count: `100+`
- environment_side_representation: `graph_based`
- agent_accessible_representation: `L3`
- behavioral_scale: `emergent_social_structure`
- behavior_type: `cooperation; conflict; mobility; norm_formation; other`
- evidence_status: `designed_affordance_only`
- spatial_behavior_coupling: `implicit`
- evaluation_method: `mixed`
- space_syntax_construct: `none`
- source_basis: `local_pdf_ocr_partial_review`
- artifact_class: `local_pdf`

## Representation Gap Note

Agent memories and environment feedback now clearly include location-bearing state, but the extracted evidence still supports only a conservative place- and movement-level representation.

## Original Artifact Pointer

- local_artifact_path: `assets/survey_paper/pdfs/phase1_core/07_AgentSociety_Piao2025.pdf`

## Source Content

Title: Introduction

Source PDF: D:\0-AI相关研究\1-spatialagent\spatial-agent\assets\survey_paper\pdfs\phase1_core\07_AgentSociety_Piao2025.pdf

Extraction:
- backend: pypdf
- extracted_at_utc: 2026-04-28T16:32:58+00:00
- page_count: 45
- status: ok
- text_char_count: 168642

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 2)
- AgentSociety: Design and Overview (page 3)
- LLM-driven Social Generative Agents (page 5)
  - Overview (page 5)
  - Emotion, Needs, and Cognition (page 8)
  - Mobility Behaviors (page 9)
  - Social Behaviors (page 10)
  - Economic Behaviors (page 11)
  - Workflow of LLM-driven Social Generative Agents (page 12)
- Real-world Societal Environment (page 14)
  - Overall (page 14)
  - Urban Space (page 15)
  - Social Space (page 15)
  - Economic Space (page 16)
- Large-scale Social Simulation Engine (page 17)
  - Overview (page 17)
  - System Architecture (page 18)
  - Group-based Distributed Execution (page 19)
  - MQTT-powered Agent Messaging System (page 20)
  - Utilities (page 21)
  - Toolbox for Social Experiments (page 22)
- Performance Evaluation (page 23)
  - Societal Environment Performance (page 24)
  - Agent Messaging System Performance (page 24)
  - Social Simulator Performance (page 25)
- Exemplary Social Experiments (page 27)
  - One Day Life (page 27)
  - Polarization (page 28)
  - Spread of Inflammatory Messages (page 30)
  - Universal Basic Income (page 32)
  - External Shocks of Hurricane (page 33)
- Related Works (page 35)
  - LLM-driven Agents (page 35)
  - Social Simulation (page 35)
- Discussion (page 36)
  - Three Levels of Social Simulator (page 36)
  - Social Simulator: New Paradigm of Computational Social Science (page 37)
  - From Policy Making, Risk Control, to Future Human-AI Society (page 37)
    - Policy making and social management for a smarter society (page 38)
    - Risk control and mitigation for a safer society (page 38)
    - Social simulator for the future human-AI society (page 38)
- Conclusion (page 39)

Markdown Content:

AgentSociety: Large-Scale Simulation of
LLM-Driven Generative Agents Advances
Understanding of Human Behaviors and Society
Jinghua Piao1† Yuwei Yan1† Jun Zhang1† Nian Li1 Junbo Yan1
Xiaochong Lan1 Zhihong Lu1 Zhiheng Zheng1 Jing Yi Wang1 Di Zhou2
Chen Gao3 Fengli Xu1 Fang Zhang4∗ Ke Rong2∗ Jun Su4∗ Yong Li1∗
Abstract
Understanding human behavior and society is a central focus in social sciences,
with the rise of generative social science marking a significant paradigmatic shift.
By leveraging bottom-up simulations, it replaces costly and logistically challenging
traditional experiments with scalable, replicable, and systematic computational
approaches for studying complex social dynamics. Recent advances in large lan-
guage models (LLMs) have further transformed this research paradigm, enabling
the creation of human-like generative social agents and realistic simulacra of so-
ciety. In this paper, we propose AgentSociety, a large-scale social simulator that
integrates LLM-driven agents, a realistic societal environment, and a powerful
large-scale simulation engine. Based on the proposed simulator, we generate social
lives for over 10k agents, simulating their 5 million interactions both among agents
and between agents and their environment. Furthermore, we explore the potential
of AgentSociety as a testbed for computational social experiments, focusing on
four key social issues: polarization, the spread of inflammatory messages, the
effects of universal basic income policies, and the impact of external shocks such as
hurricanes. These four issues serve as valuable cases for assessing AgentSociety’s
support for typical research methods – such as surveys, interviews, and interven-
tions – as well as for investigating the patterns, causes, and underlying mechanisms
of social issues. The alignment between AgentSociety’s outcomes and real-world
experimental results not only demonstrates its ability to capture human behaviors
and their underlying mechanisms, but also underscores its potential as an important
platform for social scientists and policymakers.
1 Department of Electronic Engineering, Beijing National Research Center for Information Science and Technol-
ogy (BNRist), Tsinghua University
2 Institute of Economics, School of Social Sciences, Tsinghua University
3 BNRist, Tsinghua University
4 School of Public Policy and Management, Tsinghua University
† These authors contributed equally to this work.
∗ Corresponding authors. E-mail: liyong07@tsinghua.edu.cn.
arXiv:2502.08691v1  [cs.SI]  12 Feb 2025

1 Introduction
Over the past decades, researchers across various fields – spanning social science, physical science,
and computational science – have made significant efforts to understand the functioning and develop-
ment of society along two dimensions: explanation and prediction [46, 61, 62]. Explanation seeks to
identify the causal mechanisms and underlying factors that drive observed social patterns, aiming
to offer a deeper understanding of why certain outcomes occur in society [ 46, 44]. Gaining such
an understanding often requires conducting social experiments, which can be costly to implement
and pose substantial practical and ethical challenges. On the other hand, prediction focuses on using
data to forecast future events or emergent behaviors, often without delving into the causal factors,
but instead concentrating on the accuracy of anticipating future trends [ 22, 46]. The framework
that combines explanation and prediction methods, forms the foundation of computational social
science [46]. However, as the physicist Richard Feynman famously stated, “What I cannot create, I
do not understand”, suggesting that true understanding goes beyond merely observing, explaining,
or predicting human behavior [ 31, 30]; instead, it requires the ability to generate the systems we
study [31, 30]. In this vein, a new paradigm of “generative social science” is rapidly emerging, which
emphasizes the bottom-up simulation of social systems to gain in-depth insights into their underlying
mechanisms and predict future outcomes [31, 30]. A well-established method in this paradigm is
agent-based modeling, which aims to model complex social dynamics by simulating the actions and
interactions of agents [30, 67, 103]. This method, compensating for the limitations of social experi-
ments, is widely applied in studies across social science [41, 18, 39], political science [27, 60, 64],
economics [10, 34], and other interdisciplinary fields [8, 38, 79, 80], advancing their understanding
of human behaviors and society through various simulations. However, the broader impact of these
studies has been hindered by the same long-standing issue: to what extent can these simulations
authentically replicate the complexities of real human society?
Indeed, the authenticity of these simulations depends on to what extent the most basic components
– i.e., the agents – behave like humans. However, most existing agents, driven by rules [29], equa-
tions [45], or even machine learning models [115], are limited in their ability to generate human-like
behaviors. For example, when simulating opinion dynamics, people’s opinions are often represented
as scalars or vectors, and their interactions as equations [15]. While this modeling approach offers
valuable insights, it is still far from reality, as people typically communicate using natural language,
rather than numeric values. Fortunately, recent advances in large language models (LLMs) have
shown promise in creating human-like agents [38, 99, 106]. Numerous studies have pointed out that
after being empowered by LLMs, these agents agents have generated human-like “minds” [92, 63, 55].
They not only possess basic cognition abilities, such as learning [ 106, 99], reasoning [ 102], and
decision-making [64, 38], but also demonstrate the capability to understand and predict the thoughts
and intentions of others [ 55, 92]. Furthermore, beyond exploring these agents’ minds, some re-
searchers have investigated their potential to mimic human behaviors [64, 80, 89, 108, 33, 48, 39, 77].
Their investigations have revealed that, through elaborate designs incorporating domain knowledge,
these LLM-driven agents can generate social behaviors, such as mobility [ 89, 108, 33], employ-
ment [64, 48], consumption [64, 48], and social interactions [39, 77]. While great efforts have been
made to examine specific facets of these agents, simulating a comprehensive social being remains
largely underexplored.
As the famous sociologist George Herbert Mead stated, “The self is something which has a develop-
ment; it is not initially there, at birth, but arises in the process of social experience and activity.” [70]
Therefore, the mere incorporation of minds and behaviors into these generative agents is insufficient
to create a social being; instead, social experience and activity, emerging from interactions with
other agents and the environment, are crucial. Several recent studies have provided substantial
empirical evidence supporting this point. Some have discovered that the collaboration of multiple
agents can generate believable social organizing behaviors [77] and solve complex tasks [63, 24].
Moreover, as the number of agents further scales up, large-scale interactions among them can lead to
the emergence of social norms and collectives [58, 80]. Meanwhile, the environment not only serves
as the ground for interactions among agents, but also provides critical feedback that guides their be-
haviors [6, 64, 98, 117]. For example, the widely-adopted gaming environment “Minecraft” provides
feedback, such as crafting materials, tools, or resources, enabling agents to adapt their behaviors,
solve tasks, and gain civilizational progression [98, 117, 6]. Overall, as highlighted by these studies,
a scalable framework supporting large-scale interactions and a realistic environment is foundational
2

to simulating a comprehensive social being and society. However, the current investigation of both
remains limited.
To address the above gaps, we proposeAgentSociety, a large-scale social generative simulator that
incorporates LLM-driven social generative agents, a realistic societal environment, and large-scale
interactions both among agents and between agents and the environment. Specifically, following
social theories from a broad range of fields, including psychology [ 68, 5], economics [ 25] and
behavioral sciencel [118], we first design a framework for LLM-driven social agents. These agents are
endowed with human-like “minds”, which include emotions, needs, motivations, and cognition of the
external world. Their behaviors such as mobility, employment, consumption, and social interactions
are dynamically driven by these internal mental states. Beyond individual agents, we construct a
realistic societal environment that seamlessly integrates urban, social, and economic spaces, providing
a rich foundation for agent interactions and self-evolution. At its core, society emerges from the
bottom-up interactions among individuals, where agent-level interactions collectively give rise
to complex social structures and phenomena. Recognizing that social systems exhibit emergent
behaviors shaped by scale, we develop a large-scale social simulation engine equipped with distributed
computing and an MQTT-powered high-performance messaging system. This enables simulations
with up to 10k agents, each engaging in an average of 500 interactions per day, capturing the
intricate dynamics of large-scale social systems. Based on the proposed large-scale social simulator,
we successfully reproduce behaviors, outcomes, and patterns observed in four real-world social
experiments, including polarization, inflammatory message spread, the effects of universal basic
income policies, and the impact of external shocks like hurricanes. These experiments not only cover
social research methods, such as surveys, interviews, and interventions, but also demonstrate the
simulator’s ability to replicate social dynamics, unlocking new possibilities for social scientists and
policymakers. Overall, AgentSociety marks a paradigm shift in AI for social science, enabling large-
scale, high-fidelity simulations that overcome traditional experimental limitations in costs, scalability,
and feasibility. By leveraging LLM-driven social generative agents, it facilitates deeper analysis,
prediction, and intervention in complex social systems, laying the foundation for computational social
science 2.0.
2 AgentSociety: Design and Overview
Society is a complex system, characterized by large-scale interactions among individuals with
diverse social behaviors, whose nonlinear dynamics often give rise to emergent phenomena and
unpredictable collective behaviors in a certain environment [ 87, 57, 30]. For example, in social
networks, interactions between individuals can result in the emergence of polarization [15]. Moreover,
financial market crashes, a classic phenomenon in economic systems, stem from the collective
behavior of market participants and the herding tendencies of individuals [ 91]. These emergent
phenomena, despite originating from individuals’ behaviors, cannot be fully explained or predicted
solely based on individual components [87, 57, 30]. Therefore, this requires us to adopt a bottom-up
perspective [30, 31, 29]: we should begin by simulating an individual social agent, and then generate
an artificial society by incorporating a realistic environment and facilitating large-scale interactions
among agents as well as between agents and their environment.
Therefore, we develop an evaluation framework to examine the capabilities of various LLM-driven
social simulators along these three key dimensions (Figure 1). We first focus on the most basic element
of the simulator, i.e., LLM-driven social generative agents. As discussed above, the design of these
agents can be divided into three levels: minds, social behaviors, and their coupling methods (M-B
coupling). At the mind level, researchers initially input a profile description into LLMs, enabling them
to role-play and respond like a real person with a similar profile [24]. However, such simple role-play
cannot guarantee the quality of behavior generation. Consequently, an increasing number of studies,
inspired by the pioneering work of Park et al. [77], incorporate agentic module design such as profile,
memory, reflection, and action, into their LLM-driven agents [39, 64]. In this way, these agents can
exhibit more human-like behaviors and generate responses that are coherent, context-aware, and
aligned with their designated profiles. Recently, some researchers have realized that agents designed
purely based on the commonsense knowledge of LLMs lack the social intelligence needed to mimic
a real social being. To improve this, they have drawn on some theories from psychology to create
agents with socially intelligent designs [101, 6]. However, they do not organically integrate theories
3

from multiple social science disciplines, which is central to our design of LLM-driven generative
social agents.
At the behavioral level, simulated behaviors can be broadly categorized into two types. The first
type includes complex behaviors, which involve multiple intricate steps and cannot be executed
solely by the agent itself. These behaviors require interaction with other agents or the environment,
such as socializing, engaging in economic activities, or navigating movement. The second type
comprises simpler behaviors, such as sleeping, which are relatively straightforward and do not demand
external interactions. To systematically evaluate these complex behaviors, such as movement, social
interaction, and economic activities, we have developed specific evaluation criteria. For mobility
behaviors, we examine whether the simulator simply models the switching of an agent’s position
(i.e., relocation) [101] or incorporates the entire process of mobility trajectory [89, 77]. For social
behaviors, we assess whether the agents merely engage in basic interactions [ 75] or demonstrate
organized social relationships, reflecting more human-like group dynamics [ 109, 77, 6, 72]. For
economic behaviors, we evaluate whether the agents recognize only the concept of “resources” (e.g.,
money in the real world or diamonds in Minecraft) [ 24] or perform advanced activities, such as
value-based resource exchanges grounded in logical reasoning and strategic decision-making [6, 64].
In the case of simpler behaviors, we focus on the level of constraints in the simulated activities. These
range from highly restricted tasks, such as choosing a favorite movie [110], to more autonomous and
creative undertakings, like organizing a party without external prompts [77, 101].
After introducing the minds and behaviors of agents, we further focus on understanding how behaviors
are generated from their minds, which we refer to as mind-behavior coupling. Some researchers have
adopted implicit modeling approaches, relying on the planning, memory, and reasoning capabilities
of LLMs to generate plausible behaviors [39, 64, 94]. In contrast, others have leveraged established
theories, (e.g. Maslow’s Hierarchy of Needs [68] and Theory of Planned Behavior [5]) to explicitly
model how behaviors are driven by minds [101]. This explicit modeling aims to create behaviors that
are not only plausible but also more closely aligned with human-like patterns [101].
As discussed above, a realistic societal environment serves as the foundation for simulating authentic
human behaviors and society. Current social simulators employ a range of strategies for environment
design, each with its own strengths and limitations. Dataset-based environments [ 24, 94] rely on
pre-existing data but lack the ability to provide dynamic, real-time feedback to agents’ behaviors. For
example, Sociodojo [24] For example, Sociodojo [24] incorporates pre-existing real-world time series
data to provide these agents with a sense of the external world. Text-based environments [75, 101],
often built based on LLMs, can offer some interactive feedback; however, their realism and objectivity
remain questionable, limiting their reliability for simulating complex scenarios. Rule-based virtual
environments, like Minecraft, provide richer and more objective feedback, but they still fall short
of capturing the intricate complexity of real human social systems [64, 6, 109]. To advance toward
a truly realistic social simulator, it is essential to design an environment that faithfully reflects the
multifaceted nature of human society. Such an environment should integrate key dimensions of urban
living, economic dynamics, and social relationships, while supporting diverse interactions among
agents and providing feedback on their behaviors.
After evaluating LLM-driven social generative agents and their environments, we further extend
our focus to examine the capabilities of the social simulation engine, particularly in terms of its
scalability and its potential to support social science research. The scale is a key factor in determining
its capacity to support research on complex social systems [87, 57, 30]. We classify the supported
scale into four levels: < 100, 100-1k, 1k-10k, and > 10k agents. Larger scales enable more intricate
simulations and provide a platform for studying emergent phenomena in greater detail. Moreover, the
engine’s ability to facilitate traditional social science methodologies, such as experiments, surveys,
and interviews, is also important. The extent to which the system supports these methods directly
influences its applicability across diverse research domains. By accommodating these methodologies,
the engine can bridge the gap between simulation-based research and real-world social science,
unlocking new opportunities for understanding and addressing societal challenges. Overall, Table 2
shows the comparison of different LLM-driven social simulators across the three key dimensions.
Existing platforms, although capable of simulating societies and human behaviors to some degree,
face substantial limitations in various areas. Since these platforms were not specifically designed for
social science research, they lack support for these methods. As a result, this aspect has not been
included in the table.
4

Minds
(M)
M-B
Coupling
Behaviors
(B)
Societal Environment
Minds
Mind-Behavior Coupling
Behaviors
    Social Simulation Engine
Role-play Agentic Module
Mobility Social
Interactions
Employment
& Consumption Others
Influence or Drive
Social Intelligence
Urban Social Economic
Data/Text/
Rules/Games
Realistic
Social Experiments Survey
 Interview
 Data Analysis
Toolbox for Social ScienceScale
<100 100-1k 1k-10k >10k
Figure 1: Evaluation framework for LLM-driven social simulators.
In this paper, we propose AgentSociety, a comprehensive large-scale social simulator designed
to integrate LLM-driven social generative agents, a realistic societal environment, and a robust
simulation engine. This simulator not only supports large-scale agents and their interactions, but
also facilitates advanced social science research. Figure 2 provides an overview of AgentSociety
and outlines the structure of this paper. AgentSociety consists of three key components: LLM-
driven social generative agents, a realistic societal environment, and a powerful simulation engine
that supports large-scale interactions. Extensive experiments demonstrate AgentSociety’s superior
performance and its potential as a valuable testbed for various social experiments. In particular, we
first introduce LLM-driven social generative agents in Section 3, which discusses the designs for
agents’ minds, complex social behaviors, and their coupling in detail. We then demonstrate our
real-world societal environment in Section 4, which includes our modeling of urban, social, and
economic spaces. Furthermore, we illustrate our large-scale social simulation engine in Section 5
and evaluate its performance in Section 6. Finally, we show a typical one day life of our simulated
agents in Section 7.1 and launch several social experiments based on our proposed large-scale social
simulator in Sections 7.2 - 7.5. These examples, covering polarization (Section 7.2), the spread of
inflammatory messages (Section 7.3), universal basic income 7.4, and external shocks of hurricanes
(Section 7.5), demonstrate the validity and authenticity of our proposed simulator.
3 LLM-driven Social Generative Agents
3.1 Overview
As discussed above, the rapid development of LLMs allows us to design human-like agents with not
only basic psychological states [1, 92], but also complex social behaviors such as mobility [89, 108,
33], employment [64, 48], consumption [64, 48], and social interactions [39, 77]. While these efforts
in specific areas have shown the human-level intelligence of LLMs, creating LLM-driven social
generative agents capable of simulating a comprehensive social being remains difficult. This difficulty
primarily lies in two aspects. First, human behaviors are inherently motivated by psychological
states [32, 69, 68, 5]. However, this crucial connection is largely absent in a vanilla LLM or existing
5

AgentSociety Key
Components
Example
Applications
Polarization
Section 7.2
Spread of Inflammatory Messages
Section 7.3
Universal Basic Income
Section 7.4
External Shocks
of Hurricane
Section 7.5
Social Agents
Section 3
Societal Environment
Section 4
Large-scale Interactions
Section 5
System Performance
Section 6
Figure 2: Overview of the proposed social simulator AgentSociety. AgentSociety consists of three key
components: LLM-driven social generative agents, a realistic societal environment, and a powerful
simulation engine that supports large-scale interactions. Based on these components, AgentSociety
not only demonstrates superior computational performance but also serves as a valuable testbed for
various social experiments.
agents designed for specific aspects. Second, different types of behaviors are highly interdependent.
For example, the decision of when and how people commute to work is shaped by the interplay
between their mobility and employment behaviors. Similarly, social interactions among individuals
often take place when people go shopping. These examples highlight the crucial interdependence
of human behaviors. Despite its significance, current LLMs and agents fail to capture this, limiting
their ability to accurately simulate realistic, complex human behaviors. Addressing these two aspects
requires deep insights into social science theories of human behavior, as well as advancements in
algorithmic design to integrate these insights into LLM-driven social generative agents.
Therefore, we propose a design for LLM-driven social generative agents, deeply rooted theories
from psychology (e.g. Maslow’s Hierarchy of Needs [ 68] and Theory of Planned Behavior [ 5]),
economics (e.g., Dynamic Stochastic General Equilibrium [25]), and behavioral science (e.g., Gravity
Model [118]). Figure 3 provides an overview of the proposed agents, which can be roughly divided
into four parts. First, each agent retains their profile, typically regarded as relatively stable (e.g.,
personality), and status, which is dynamic (e.g., emotion). In particular, the profile includes basic
demographics such as name, age, gender, and education, as well as personality. The status comprises
three key aspects: the agent’s current mental states, economic status, and social relationships. Mental
states reflect the agent’s inner experiences, while economic status and social relationships capture
their power and connections in the external world. The integration of the profile and status into
these LLM agents enables them to role-play like real people, providing the foundation for simulating
complex mental processes and behaviors.
Second, each agent is designed with three levels of mental processes: emotions, needs, and cognition.
Emotions reflect the agent’s immediate response to both internal and external stimuli, shaping its
behaviors and reactions. Needs serve as the underlying motivational drivers that guide an agent’s
actions, ranging from basic survival requirements to higher aspirations such as personal growth and
self-fulfillment. Cognition refers to the agent’s understanding of the world, e.g., its attitudes toward
climate change and political issues. By incorporating these three levels of mental processes (see
6

Table 1: Comparison of LLM-driven agents and social simulators.
Model Minds Mobility Economics Social Others M-B Scale Env.
RP. AM. SI. Relo. Traj. Res. Exc. Int. Rel. Con. Free Infl. Dri. #
D2A [101] ✓ ✓ ✓ ✓ ✓ ✓ <100 Text
Ecoagent [64] ✓ ✓ ✓ ✓ ✓ 100-1k Rules
OASIS [109] ✓ ✓ ✓ ✓ ✓ >10k Rules
GA1000 [78] ✓ ✓ ✓ 1k-10k ×
MATRIX [75] ✓ ✓ ✓ <100 Text
Sociodojo [24] ✓ ✓ <100 Data
GA [77] ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ <100 Rules
GenSim [94] ✓ ✓ ✓ >10k Data
Project Sid [6] ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ 1k-10k Rules
AgentScope [40] ✓ ✓ ✓ N/A N/A
HiSim [72] ✓ ✓ ✓ ✓ 100-1k Rules
S3 ✓ ✓ ✓ ✓ 1k-10k Rules
Agent4Rec [110] ✓ ✓ ✓ 1k-10k Rules
RecAgent [100] ✓ ✓ ✓ ✓ ✓ 100-1k Rules
Sotopia [116] ✓ ✓ <100 ×
Casevo [52] ✓ ✓ ✓ ✓ 100-1k Rules
Ours ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ >10k Society
Profile & Status Mental Process Social Behaviors
Environment
Basic Demographics
Personality & Mental States
Economic Status
Social Relationship
...
Memory: Flow of Objective Events & Flow of Subjective Experience
Emotions
Needs
Cognition
...
Physiological
Safety
Love & Belonging
Mobility
Social Interactions
Employment & Consumption
Other Behaviors
...
Role-play Inner
Workflow of LLM-driven Social Generative Agents
Figure 3: Overview of LLM-driven social generative agents.
the detailed design in Section 3.2), agents can autonomously perceive the external environment,
ultimately developing their cognition of it.
Third, social behaviors are the core of LLM-driven social generative agents, which serve as the
bridge between their internal mind and external environment. Given the importance and complexity
of various human behaviors, we explicitly model three types of social behaviors: mobility, social
interactions, as well as employment & consumption. In Sections 3.3-3.5, we detail the special designs
for these three behaviors. Other simple behaviors such as sleeping are directly handled by LLMs.
It is worth noting that these behaviors are conditioned by the agents’ profile and status, and driven
by their mental processes. Finally, we introduce the workflow of the overall LLM-driven social
generative agents in Section 3.6, illustrating the integration of their profiles, mental processes, and
social behaviors. This workflow enables the simulation of comprehensive, context-aware agents by
capturing both internal cognitive states and external interactions, ensuring realistic, dynamic social
behaviors within the simulation.
7

3.2 Emotion, Needs, and Cognition
Humans are driven by an intricate interplay of feelings, motivations, and thought processes that shape
their decisions and interactions [90, 7]. Grounded in psychological theories, our study integrates three
fundamental constructs, including emotion, needs, and cognition, to design agents that realistically
simulate adaptive and human-like behavior. Emotion, as the most dynamic layer of human psychology,
drives rapid responses to external situations and influences behavior [ 20, 16]. Needs, based on
Maslow’s hierarchy of needs theory, serve as motivational drivers, spanning from basic survival
requirements to higher aspirations like personal growth [3]. Modeling these needs enables agents
to adopt realistic motivations and prioritize actions in ways relatable to human behavior. Cognition,
informed by theories like Theory of Mind and Cognitive Appraisal Theory, involves advanced mental
processes that allow agents to evaluate complex situations, make thoughtful decisions, and adapt
to diverse situations [13, 88]. Drawing on these psychological theories, agents recognize their own
knowledge and the mental states of others while evaluating context sensitively, enabling effective and
goal-oriented social interactions [81]. By integrating these crucial elements, our study designs agents
that can respond dynamically to real-time changes while tailoring their actions to reflect human-like
characteristics and behaviors within complex social simulations. The overall modeling framework for
the psychological and cognitive aspects of the agent is illustrated in Figure 4.
EmotionMindsThoughtAttitude
Needs
Behavior
Memory
Figure 4: Modeling framework of emotion, needs, and cognition.
Emotion is a dynamic and foundational element of human psychology, driving rapid responses
to external events and influencing decision-making and behavior [ 90]. In our model, an agent’s
emotions are affected by its profile and status and are updated based on interactions with other agents
and the environment. We adopt the emotion measurement framework from Shvo et al. [90], which
involves the agent selecting a keyword to best describe its current emotional state, formulating a
sentence-based thought related to that emotion, and rating the intensity of six core emotions—sadness,
joy, fear, disgust, anger, and surprise—on a scale from 0 to 10. This method enables agents to track
and update their emotional states, providing a foundation for contextually appropriate and adaptive
behavior. These emotions then influence the agent’s actions, motivations, and cognitive processes,
establishing an interconnected system that guides decision-making. As we will explore in the next
section, emotional states directly impact the agent’s needs and cognitive evaluations, linking emotions
to higher-order motivational and reasoning functions.
The concept of needs is widely accepted in the field of psychology as the fundamental motivator
behind an individual’s pursuit of specific objectives and maintenance of social engagement. Emotions,
on the other hand, are seen as the immediate responses experienced by an individual. The concept of
needs, however, is believed to establish the underlying motivational mechanisms that guide sustained
behavior, thereby extending and contextualizing emotional fluctuations. The integration of needs and
emotions in the agent’s model enables the maintenance of consistent motivational pathways over time,
ensuring that transient affective states are grounded in enduring goals and priorities. In our approach,
we employ established psychological frameworks (e.g., Maslow’s hierarchy of needs [3]) to categorize
and structure these motivational forces. We adopt a hierarchical representation of needs to organize
motivational drives by their relative urgency and importance. This needs hierarchy is continuously
updated based on three interrelated factors: the agent’s active behaviors, uncontrollable or passive
external events, and its current psychological states. The integration of these elements enables
the system to dynamically adjust need priorities, ensuring that the agent responds appropriately to
both internal motivations and external pressures. Furthermore, needs do not merely reflect static
conditions but rather serve as a driving force for proactive behavior. Leveraging the Theory of Planned
8

Behavior [5], the agent formulates action plans specifically aimed at meeting or enhancing priority
needs. Through this design, the needs module provides a robust foundation for adaptive, socially
informed behavior. In conclusion, the modeled needs provide the necessary motivational basis that
informs and intersects with the agent’s cognitive processes, leading directly into the subsequent
discussion on cognition.
Cognition encompasses the higher-level processes involved in reasoning, planning, and decision-
making [13]. In our model, cognition is intricately connected to the agent’s emotional and attitudinal
updates. After the agent processes an action, a sentence is used to describe its behavior in relation to
the current context. These sentences is then used to update both the agent’s attitude towards specific
topics and its emotional state. Attitude, in this context, serves as a memory system, reflecting how
supportive or opposed the agent is to a particular topic, rating from 0-10. By continuously updating
both emotion and attitude through the agent’s actions and experiences, cognition ensures that the
agent adapts to its environment in a way that is consistent with human-like reasoning and emotional
depth. This process, in turn, influences the agent’s needs and motivations, bridging the gap to the
next level of analysis.
In summary, the integration of Emotion, Needs, and Cognition modules enables the agent to engage
in socially intelligent behavior, with each module contributing to the shaping of adaptive actions.
For instance, when the agent detects an unmet need for social interaction and determines a sequence
of actions—such as identifying potential contacts and sending messages—to satisfy this need. The
emotional state of the agent, influenced by the emotion module, affects the tone of communication,
prompting the agent to initiate conversation with a cheerful or light-hearted tone. As the social
interaction progresses, the outcome of the behavior—whether the interaction is perceived as successful
or not—is reflected in the emotion and cognition modules. This, in turn, results in an update to the
needs module, thereby establishing a continuous feedback loop that adapts the agent’s behavior in
response to both its environment and internal state.
3.3 Mobility Behaviors
Mobility serves as the fundamental basis for social agents to engage in interactions and fulfill their
demands. Mobility is not a random behavior but is needs-driven across multiple levels. For instance,
when an agent experiences hunger (a basic survival need), it must move to a restaurant to obtain
food; to attend a work meeting (an advanced professional need), commuting to an office becomes
necessary. These mobility behaviors directly serve specific goals, acting as physical carriers for
social interactions, economic activities, and other societal behaviors. In essence, the core challenge
of mobility modeling is to bridge the spatiotemporal gap between needs and behaviors. Without
effective mobility, agents cannot achieve role immersion or behavioral closure in complex social
environments.
As depicted in the previous section, the Needs of social agents exhibit a hierarchical structure: from
foundational needs (e.g., eating, resting) to safe and social needs (e.g., work, social gatherings). To
satisfy the needs, it requires implementation through a "Need - Plan - Behavioral Sequence" chain.
Taking social needs as an example, an agent first formulates a plan to "attend a friend’s gathering,"
which decomposes into behavioral sequences such as "scheduling time (Friday evening), selecting a
location (café), moving." Here, location selection becomes the direct driver of mobility — to reach
the target location. This spatiotemporal coupling establishes mobility as the critical execution step
for demand realization.
Following the needs-driven principle, the mobility module adopts a hierarchical decision framework
(shown in Fig. 5):
1. Intention Extraction: Derive core mobility intentions from demand hierarchies. For
example, when "social demand" is activated, the agent may extract a "move to social venue"
command.
2. Place Type Selection: Match demands with POI (Point of Interest) types in geographic
databases. If the intention is social interaction, venues like cafés or parks are filtered.
3. Radius Decision: Dynamically determine feasible ranges by integrating internal states
(e.g., age, stamina) and environmental parameters (e.g., weather, traffic). Heavy rain may
constrain the radius of indoor venues within 1 km or even stay at home.
9

4. Place Selection: Apply the Gravity model for spatial optimization:
Pij =
Sj/Dβ
ij
P Sk/Dβ
ik
, (1)
where Sj denotes the attractiveness of locationj, Dij is the distance, and β is the distance de-
cay coefficient. This model reduces LLM computational overhead while ensuring selections
align with human spatial patterns (e.g., proximity principle, agglomeration effects).
NeedandPlanMobilityBehaviorProfile
Agent Environment
Status
Step1:IntentionExtractionStep2:TypeSelection
Map
VariablesWeather
Temperature
Step3:RadiusDecision
Step4:PlaceSelection
GravityModel
Figure 5: Modeling of mobility behavior.
Mobility serves as a foundational behavioral module, operating as an integrative force within the
social agent’s action network. This enables multidimensional coordination across social, economic,
and environmental domains. The act of moving to a park, for instance, inherently carries the
potential for social synergy. Spontaneous encounters with acquaintances may emerge, catalyzing
dialogues, collaborative activities, or even serendipitous social events. These interactions exemplify
how mobility serves as a conduit for organic relationship-building. Concurrently, economic synergy
manifests through goal-oriented displacements. Commuting to workplaces directly sustains labor
productivity, while visiting commercial hubs like shopping malls create opportunities for consumption,
thereby linking physical movement to economic cycles. Beyond the human-centric interactions
discussed above, mobility also embodies environmental adaptation. Agents dynamically adjust
routes based on real-time traffic data or weather fluctuations, demonstrating responsiveness to spatial-
temporal constraints. Collectively, these synergies position mobility as the dynamic chassis of social
adaptability. It fulfills immediate demands and also provides the contextual infrastructure for complex,
layered interactions in urban ecosystems.
3.4 Social Behaviors
Cognition Social NetworkSocial Behavior
Social Relation
Family
Friends
Colleagues
Economy
Find person to interact
Send Message
Respond Message
Emotion ThoughtAttitude
Mobility
Economy News
 Action
Offline Event
 Action
Arrange Meeting
Figure 6: Modeling of social behavior.
10

Social behaviors play a critical role in our agent simulation framework. They enable the flow of
information and influence between agents, and further lead to the emergence of collective phenomena
through agent interactions. In real societies, people’s beliefs, opinions, and behaviors spread and
evolve primarily through social connections and communications. Therefore, modeling social
behaviors allows us to simulate how information and influence flow between agents affects both
individual and group dynamics. Our social module consists of two components: social relationships
defining the connections between agents, and social interaction behaviors enabling communication
between connected agents.
We include three types of social relationships in our framework: family bonds, friendships, and
colleagues. Each relationship has a strength value ranging from 0 to 100 representing social closeness
between agents. Agents communicate more frequently with high strength connections and adjust their
communication tone based on relationship type. For example, agents use more formal language with
colleagues and casual language with close friends. We maintain detailed interaction history between
connected agents, including message content and time, which influences how they communicate in
future interactions.
Our framework primarily focuses on modeling online social behaviors on online social networks.
Motivated by their social needs, agents select interaction partners based on relationship types and
strength. For instance, when sending casual messages, agents typically choose their best friends,
which are friends with the highest relationship strength. Target selection also considers the recipient’s
profile characteristics. When an agent wants to discuss specific topics, they select friends with relevant
expertise or experience. For example, an agent seeking advice about security issues would contact
friends who work as police officers. After selecting a target, agents start conversations. The content
of these messages is shaped by multiple factors: the agent’s current needs and intentions determine
the conversation topic, their thoughts and beliefs influence the specific content, and their emotional
state affects the message tone and style. When receiving messages, agents generate responses based
on their relationship strength with the sender, their chat history, and their current emotional state. Our
current framework primarily models online social interactions through messaging on online social
network, with plans to incorporate offline interactions. For example, when agents discover shared
interests in particular topics or need to have more detailed discussions, they can coordinate offline
meetings through online communication.
Social behaviors are deeply interconnected with agents’s emotional states, cognition, economic
behaviors, and mobility behaviors. An agent’s current emotions and beliefs directly influence how
they compose messages, while received messages can significantly alter their emotional state and
viewpoints. Positive interactions can improve mood and strengthen relationship bonds, while negative
interactions may lead to emotional distress and weakened connections. The exchange of economic
information through social interactions can trigger economic behaviors. For instance, when agents
receive news about job opportunities or market conditions from their social connections, they may
adjust their employment or consumption decisions accordingly. Similarly, social interactions often
lead to mobility behaviors, such as when agents receive event invitations or arrange offline meetings
with their connections.
Through this comprehensive social behavior modelling, we enable agents to engage in meaningful
interactions that both shape and are shaped by their internal states and external behaviors. Our social
module captures both relationship structures between agents and their interaction behaviors, allowing
agents to interact and influence each other as they do in real societies, and providing a foundation for
studying how information and influence spread in the simulated society.
3.5 Economic Behaviors
Economic behavior in daily life is a necessary component for sustaining life, with employment and
consumption being the core economic activities. These two behaviors occupy the majority of time
for social agents and further influence their psychological states, including cognition, emotional
well-being, and overall life satisfaction. Moreover, economic behavior is deeply intertwined with
other aspects of an agent’s daily life, such as mobility and social interactions. The satisfaction of
one need, whether it is economic or social, often triggers a cascade of related behaviors that span
across different domains of the agent’s life. For example, an agent’s decision to work longer hours to
increase their income may result in less time available for social interactions. Similarly, the decision
to spend more on consumption could lead to adjustments in an agent’s mobility patterns, such as
11

travel to different stores or even relocation to areas with better access to desired goods or services.
The modeling of economic behavior is shown in Figure 7.
Market Dynamics
Income
Savings
Consumption
Tax, Redistribution
Economic
News
Firm
Home
Store
Social behavior
Mobility behavior
Work propensity
Consumption propensity
Government
Economic behavior
Bank
Firm
Simulator
Figure 7: Modeling of economic behavior.
In terms of behavior modeling, we simulate the employment and consumption behavior of social
agents through the strength of their work and consumption propensity, and apply these behaviors in
a macroeconomic simulation environment [64]. Work propensity determines the agent’s working
hours and corresponding monthly income, while consumption propensity determines their monthly
consumption budget. Additionally, agents autonomously decide how to allocate this budget, including
where to spend the money and what to purchase. These behaviors are directly influenced by various
economic factors, including last month’s consumption, prices, taxes, and so on. These factors are
integrated into the agent decisions in a real-world context, where agents constantly adjust their
behavior in response to dynamic economic markets. In future work, we will further simulate agents’
complex economic behaviors in the labor and financial markets, including job changes, debt, and
investment, to model a more realistic socio-economic environment.
This framework can be used to simulate large-scale economic systems and to explore the potential
impacts of policy changes, economic shocks, and other factors on the overall behavior of social
agents within the system. By examining these dynamics, we can gain a deeper understanding
of the interactions between economic behaviors, psychological states, and social dynamics in a
comprehensive and integrated manner.
3.6 Workflow of LLM-driven Social Generative Agents
In this section, we introduce the workflow of our LLM-driven social agent, highlighting how the
agent’s internal psychological states (Emotion and Cognition) and its behaviors influence each other
and form a complete loop. This loop continuously adapts the agent’s actions based on its evolving
cognitive states, ensuring that behavior is dynamically aligned with both internal motivations and
external context. The core mechanism linking these psychological states to behavior is Memory,
which connects the agent’s cognitive states with its actions. This enables the agent to make adaptive
decisions that reflect its past experiences, current needs, and cognitive responses.
At the core of our solution is the use of Memory to link the agent’s internal psychological states
to its behavior. Memory acts as a bridge between the agent’s current emotions, cognition, and its
past experiences, ensuring that its actions are informed by both historical context and present needs.
Memory is not a passive system but actively shapes the agent’s decisions and behavior, enabling
continuous adaptation and coherence in its responses to changing situations. Specifically, Memory is
divided into three main components, each with a specific role in the agent’s overall operation:
• Profile: Stores the agent’s static attributes, such as demographic information (e.g., gender,
age), which remain constant and provide context for interpreting the agent’s behavior.
• Status: Records the agent’s dynamic state information in key-value pairs, including data
like current needs, satisfaction levels, and financial status, which directly influence decision-
making.
• Stream Memory: This is the core part of the memory system and tracks events and
perceptions over time. It is composed of two types of memory streams: Event Flow and
12

MindsNeedsEmotionAttitudeThoughts
BehaviorPlansNeedstoPlan
MobilitySocialOther
Economy
Memory TimelineE1E2E3E4C1 C2 C3
Figure 8: Workflow of social agents based on stream memory.
Perception Flow. Each stream is organized chronologically, with multiple MemoryNodes
in each stream. Each MemoryNode contains a description with three components: time,
location, and event description.
The Event Flow records events that occur over time, such as proactive actions by the agent, passive
external events, and environmental changes. These events are recorded in sequence, maintaining a
timeline of actions and occurrences.
The Perception Flow records the agent’s thoughts and attitudes towards the events in theEvent Flow.
Each node in the Perception Flow is linked to one or more nodes in the Event Flow, reflecting how
the agent perceives or reacts to a specific event. This integration allows for a nuanced representation
of both the agent’s cognitive appraisals and emotional responses.
The agent’s behavior is driven by its current state, which influences the decision-making process and
the actions taken. The following steps outline the agent’s workflow:
1. Action Determination: The agent assesses its current state (from the Status memory) and
decides on a course of action based on its emotional and cognitive evaluations. For example,
if the agent needs social interaction and is in a positive emotional state, it may choose to
initiate a social conversation.
2. Event Feedback: After performing the action, the agent receives feedback. For example,
if the agent attempts to move to a social gathering, it checks whether the movement was
successful (e.g., did it reach the correct location, considering environmental factors like
weather).
3. Memory Update: The event and its feedback are recorded in the Event Flow, and the
associated Perception Flow is updated with the agent’s emotional and cognitive responses to
the event.
4. Emotion and Cognition Analysis : The Emotion and Cognition modules analyze the
outcome of the event (e.g., whether the movement was successful) and update the agent’s
emotional state and attitude accordingly. This feedback may affect the agent’s future
decisions and actions.
5. Passive and Environmental Events: In the case of passive events or environmental stimuli,
the same memory processing logic is applied. The agent perceives the event, updates the
Event Flow, and modifies its Perception Flow accordingly.
The Memory system, organized along a time axis, reflects the natural flow of events in the physical
world. This memory framework allows the agent to integrate its ongoing experiences with past events,
creating a dynamic, evolving representation of its environment and internal states. By leveraging
13

Stream Memory, the agent adapts its behavior over time in a way that mirrors human cognition,
emotional responses, and decision-making, providing a coherent and context-aware foundation for
socially intelligent behavior.
4 Real-world Societal Environment
4.1 Overall
Mobility
Urban Space Social Space Economic Space
Roadnet
AOI
POI
Drive Walk
Bus Taxi
OnlineOffline
Filter / Ban
Social Network
Message
Supervisor
Account
Book
Firm
Person Bank
Government
NBS
Labor
Wage
GDP…
Tax
Interest
Consumption…
Societal
Environment
Mobility Social Interactions Employment &
Consumption
Social
Behaviors
Figure 9: Overview of the societal environment.
According to the introduction above, in the design and simulation of social agents, mobility behaviors,
social behaviors, and economic behaviors like employment and consumption are essential external
capabilities. In the real world, the manifestation of these behaviors is grounded in corresponding
objective entities, not merely in human subjective cognition. For example, mobility behaviors imply a
continuous change in spatial and temporal location. Therefore, if we rely solely on the knowledge and
capabilities of LLMs to conduct such simulations without incorporating modeling of the operational
laws and constraints of the real world, the simulation results are likely to be influenced by the
"hallucinations" of LLMs [49], resulting in outcomes that diverge from actual realities. To address
this issue, we need to provide a realistic and reliable environment for simulating social agents. The
environment should include the following features:
• Appropriate modeling of real-world operational principles to reflect physical constraints and
costs, and provide feedback on behaviors;
• Environmental data sourced from the real world or aligned with real-world principles;
• Interfaces to enable interaction with agents.
Such an environment will serve as a virtual mapping of the objective aspects of the world in social
simulations, enabling the design of social agents to focus solely on subjective human behavioral logic.
By offloading tasks such as numerical computations, where LLMs cannot guarantee absolute accuracy,
this approach simplifies agent design and allows researchers to concentrate on core objectives.
In alignment with this objective, we encode expert knowledge to construct a real-world societal
environment as depicted in Figure 9, designed to support the simulation of mobility behaviors,
social behaviors, and economic behaviors. The entire environment is divided into three spaces. The
14

urban space constructs a city road network supporting mobility simulation and incorporates elements
such as Area of Interest (AOI) and Point of Interest (POI). It implements common transportation
modes including driving, walking, public transit, and taxi services, providing agents with realistic
positional feedback as well as temporal and monetary costs associated with different travel choices.
The social space builds upon agents’ social networks, offering support for offline and online social
interactions. A critical and authentic design feature in this space is the supervisor, which monitors
social media content, filters messages based on algorithmic rules, and enforces bans on specific
users or connections when necessary. The economic space reconstructs fundamental elements
of macroeconomics, modeling economic behaviors of individuals, firms, governments, and banks
through the implementation of account books. These behaviors encompass employment, consumption,
taxation, interest mechanisms, while a dedicated statistical bureau is established to monitor economic
indicators like GDP. The following subsections will elaborate on the corresponding environmental
spaces for the agent behaviors respectively.
4.2 Urban Space
To address the needs of social agents for moving and interacting with different places, accurate
modeling of urban space is essential. The urban space must capture both the physical movement
pattern of individuals and their interactions with diverse urban locations.
Inspired by traffic simulation platforms such as SUMO [17] and CityFlow [112], also leveraging the
spatial abstraction schemas of OpenStreetMap, the urban space is structured into two interdependent
layers, the static infrastructure attributes and dynamic mobility behaviors.
The static attribute layer includes road networks, defined by lanes, roads and junctions to encode
traffic accessibility, as well as functional zones, which are Areas of Interest (AOIs) and Points of
Interest (POIs). AOIs delineate regions with specific purposes, such as residential neighborhoods or
commercial districts, while POIs represent granular interaction targets like retail stores.
The dynamic behavior layer extends this static foundation by simulating multi-modal mobility
through a discrete time-stepping mechanism. Individual movements, including positions, speeds,
and accelerations are updated dynamically according to kinematic principles and predefined rules.
Operational logic begins with agents formulating movement intentions based on their internal
needs and goals, then these intentions are translated into specific instructions guiding individuals’
movements within the space, which include driving, walking, taking the bus, or taking a taxi. For all
means of transportation, path-planning algorithms generate optimal routes. Driving follows the IDM
model [95] for acceleration and the MOBIL model [54, 35] for lane-changing decisions. Pedestrians
navigate sidewalks at a constant speed and follow the traffic signals at junctions to avoid collisions
with vehicles. Buses operate on fixed schedules, while passengers conduct the processes of boarding,
alighting, and transferring. For taxis, a global dispatch system simulates sending the nearest available
taxi to respond to ride requests, ensuring efficient service and minimal wait times for passengers.
For the simulation environment to function accurately, we apply rich data sources. Road networks and
AOIs are extracted from OpenStreetMap, undergoing topological simplification to produce structured
representations. POI data, acquired via API from SafeGraph.
We implement Python-based APIs to bridge the simulation space and agents,providing bidirectional
interaction capabilities. Configuration interfaces allow for initializing agent positions, assign travel
plans (e.g., destinations and transportation modes), and reset simulation states. Query interfaces
enable real-time monitoring of agent kinematics status and simulation metadata such as simulation
timestamps.
By harmonizing static urban infrastructure, dynamic mobility behaviors, and multi-source geospatial
data, our urban space establishes a high-fidelity decision-making sandbox for agents.
4.3 Social Space
Social behavior is a prerequisite for constructing an agent society. The occurrence of social behaviors
requires the support of an authentic social environment. The social environment provides management
https://openstreetmap.org/
https://openstreetmap.org/
https://www.safegraph.com/
15

of social relationships, as well as modeling and simulation of social behaviors, which will enable
mutual influence and collaboration among agents, generating richer and more authentic social
phenomena.
Therefore, the incorporation of the social space within the societal environment is particularly crucial.
The primary component of the social space is the social network, which is provided and loaded by
users. Social networks model relationships between individuals, encompassing the connections and
connection strengths between each agent and others. This network will be used by agents to evaluate
potential social interaction targets. Both the relationships and connection strengths within social
networks are mutable during simulations. Based on social networks, social spaces encompass both
online and offline interactions. Although agent design primarily focuses on online social behaviors,
offline interactions based on spatial proximity remain an indispensable component in constructing
realistic environments. For online social interactions, to realistically simulate the operational logic of
social media platforms, we also introduce the concept of the supervisor. The supervisor will identify
content in online social messages, filter messages according to user-specified algorithms or rules, and
support the blocking of specific users or connections, thereby simulating the intervention process of
social media platforms in information propagation.
In implementation, the social network is stored as data items within agents. Both offline and online
social interactions are simplified into sending messages to specific targets through the agent message
system which will be introduced in Section 5.4. The supervisor is implemented as preprocessing
middleware before message transmission, and a centralized program is provided to handle message
processing collectively for updating rules and algorithms.
In summary, the social space not only supports the simulation of realistic social interactions between
agents but also establishes intervention capabilities over social propagation within agent societies.
This framework will serve as a crucial foundation for conducting research on real-world social
propagation phenomena using LLM-driven social agents.
4.4 Economic Space
The economic space includes the modeling of several key elements in the macroeconomics [ 104,
64]. Specifically, firms convert the labor input of social agents into goods production and pay the
corresponding wages to the agents. Furthermore, firms adjust the wages of agents and goods price
flexibly based on the supply and demand relationships in the consumption market. The government
levies income tax on agents’ earnings according to specified tax rates. The banks pay interest to
agents based on their savings each year, with the interest rate adaptively adjusted according to the
Taylor Rule [104]. The National Bureau of Statistics regularly compiles macroeconomic indicators,
such as real GDP, average working hours per person, and per capita consumption levels.
Building upon the modeling of the four key economic entities—firms, agents, the government, and
banks—the economic simulator further captures the dynamic processes and interactions that drive the
functioning of a realistic economic system. By integrating income generation, expenditure, savings,
taxation, and policy-driven adjustments, the simulator provides a comprehensive representation of
economic cycles.
Agents are the fundamental economic participants, generating income through labor in firms. This
income is subject to taxation, with a portion deducted based on a progressive tax structure, while the
remaining disposable income is allocated between consumption and savings. Agents use their dispos-
able income to purchase goods and services, thereby fueling market demand. The funds allocated
to savings are deposited into banks, where they accrue interest, influencing future consumption and
investment decisions.
Firms act as producers in the economy, utilizing labor from agents to generate production output.
They pay wages to agents, creating a cyclical flow of income within the system. Firms dynamically
adjust goods prices and wages in response to market supply and demand, ensuring equilibrium in the
consumption market. Their revenue comes from the sales of goods, which is reinvested into further
production or held as retained earnings for future expansion. The government collects tax revenue
from agents based on their earnings and redistributes financial resources to regulate economic activity.
It influences the economy through fiscal policy, adjusting tax rates to manage income distribution
and public sector financing. These funds may be directed toward public expenditures, which are not
explicitly modeled in this simulator but could represent infrastructure, social programs, or government
16

services. Banks function as financial intermediaries, receiving savings deposits from agents and
providing them with interest payments. The interest rate is dynamically adjusted according to the
Taylor Rule, incorporating monetary policy mechanisms into the simulation. This impacts agents’
saving and spending behavior, as higher interest rates encourage savings while lower rates stimulate
consumption. Banks also serve as liquidity providers, ensuring the efficient allocation of financial
resources within the economy.
The National Bureau of Statistics (NBS) compiles and analyzes macroeconomic indicators to monitor
economic performance. It collects data on real GDP, income distribution, total tax revenue, per
capita consumption, and average interest earnings. These aggregated statistics offer insights into
systemic trends and policy effectiveness, enabling the evaluation of economic stability and the long-
term impact of market dynamics. By structuring the simulation as an economic settlement system,
where each entity interacts through well-defined financial flows, this framework achieves a holistic
representation of economic operations. It serves as a valuable tool for analyzing the relationships
between micro-level decision-making and macroeconomic trends, providing insights into market
behaviors, policy interventions, and the overall functioning of economic systems.
While the economic simulator successfully models key economic flows, it does not explicitly capture
critical aspects such as the goods market and the labor market. These omissions limit the realism of
the model and represent areas for future refinement. The goods market is simplified by assuming
firms adjust prices based on aggregate demand, but it does not account for detailed supply and demand
dynamics, competition, or market shocks. Similarly, the labor market is abstracted, with agents
receiving wages without modeling unemployment or the negotiation processes between workers and
firms. Including these elements could enhance the model’s ability to simulate real-world economic
fluctuations. Despite these limitations, the simulator provides valuable insights into the interactions
between agents, firms, the government, and banks. Future improvements could focus on integrating
more detailed models of the goods and labor markets, helping to better replicate complex economic
systems and improving policy analysis. In conclusion, while the current model is a simplified
representation, it offers a strong foundation for exploring economic interactions and can be further
enhanced by incorporating missing market dynamics for more accurate predictions.
5 Large-scale Social Simulation Engine
5.1 Overview
Although the large-scale social simulator introduced in this paper may appear as a simple combination
of LLM multi-agent systems (social agents) and tool call (environment), the reality of human society
characterized by independent thinking in decision-making and collaboration driven by language
communication promotes us to fundamentally rethink the system architecture design and imple-
mentation of the large-scale social simulation engine. Existing multi-agent execution frameworks
such as CAMEL [63] and AgentScope [40] typically take inter-agent collaboration as the founda-
tional principle of system architecture design, constructing Standard Operating Procedures (SOPs)
through message-passing processes among agents to determine the sequence of agent execution. Such
frameworks are particularly well-suited for multi-agent execution scenarios with well-defined agent
execution sequences, as exemplified by programming tasks [47, 82] and conversational games [107],
as they can significantly simplify complex agent interaction processes. However, in real-world
contexts, individual behavioral decision-making emerges from the autonomous integration of current
memory, cognitive states, and environmental constraints, rather than being strictly contingent upon
specific inputs from other agents or environments. Therefore, a pivotal challenge in system architec-
ture design lies in faithfully simulating this "asynchronous" phenomenon within the large-scale social
simulator, while strategically leveraging such intrinsic behavioral patterns to optimize simulation
execution efficiency.
As a solution to the aforementioned challenge, we draw inspiration from the operational logic of
the real world by treating each agent as an independent simulation unit. There are no explicit
dependencies or execution orders between agents. Instead, they exchange information and mutually
influence each other through a messaging system. For the parallel execution of independent simulation
units, to fully leverage the multi-core computing capabilities of modern computer systems and
distributed computing paradigms for horizontal scaling of simulation scale, we adopt the highly
mature Ray framework [71] to implement distributed computing and conceal I/O latency through
17

Python’s asyncio mechanism. As the simulation scale increases, we identify that TCP port resources
become a bottleneck, and excessive reliance on inter-process communication to coordinate the entire
system leads to decreased execution efficiency. Therefore, we introduce an intermediate structure
named agent group to enable multiple agents to operate within a single process, thereby balancing
communication costs with parallel acceleration while allowing connection reuse for network calls
such as LLM API calls. For the messaging system supporting inter-agent information exchange, it
needs to support massive concurrent connections, high-throughput and reliable message transmission,
though being latency-insensitive. This characteristic closely resembles the Internet of Things (IoT)
scenarios where applications must handle message delivery across millions of devices. Inspired by
this similarity, we have introduced MQTT, the communication protocol that has achieved tremendous
success in IoT communications, to construct our agent messaging system. Following best practices
from existing agent execution frameworks, we provide comprehensive utilities including multiple
LLM API adapters, a retry mechanism,a JSON parser, a metric recorder, and diverse logging
capabilities including both local file output and database storage. Leveraging these logged processes,
we develop real-time interactive visualization interfaces. Furthermore, specifically designed for social
experimentation requirements, we implement a specialized toolbox including interviews, surveys,
and interventions.
In the following content, we will first introduce the whole system architecture in Section 5.2. We
then dive into the key designs including group-based distributed execution in Section 5.3 and MQTT-
powered agent messaging system in Section 5.4. The utilities and toolbox for social experiments will
be discussed in Section 5.5 and Section 5.6 respectively.
5.2 System Architecture
Shared Services
LLM API
 Database
MQTT Server
 Metric Recorder
mlflow Client
Process #1
Ray Actor
Agent Group
Subprocess
Ray Cluster
Agents
@ray.remote
Agent Simulation Env Client Database Client mlflow Client
Environment Simulator
LLM Client
MQTT Client
Env Client
Database Client
mlflow Client
Process #2
Ray Actor
Agent Group
Agents
LLM Client
MQTT Client
Env Client
Database Client
GUI Backend
Experiment 1
Process #3 Process #4
GUI Frontend
Ray Cluster
Agent Simulation
Environment Simulator
Experiment N
…
Figure 10: System architecture of the large-scale social simulation engine.
To avoid unnecessary redundant development and leverage the advancements from the open-source
community, the system architecture of the large-scale social simulation engine is primarily con-
structed using advanced and mature open-source software or libraries. As shown in Figure 10, the
overall system architecture consists of shared services common to all social simulation experiments,
simulation tasks corresponding to each experiment, and an optional GUI component.
The shared services include the following components:
https://mqtt.org/
18

• LLM API: LLMs serve as the most critical component of the simulator, acting as the "soul"
of agents. For the simulation engine, LLMs provide a standard "request-response" process
through APIs to handle tasks described in agent prompts. The LLM API can utilize public
services like OpenAI or DeepSeek, or be deployed through local inference engines such as
vllm [56] and ollama.
• MQTT Server: The architecture employs the high-performance IoT protocol MQTT for
inter-agent message transmission, simulating real-world human language interactions and
collaboration patterns. The MQTT server enables protocol-compliant message delivery to
clients. We select a high-performance MQTT server named emqx for this purpose.
• Database: The database in the architecture is solely used for storing simulation results
for subsequent analysis or visualization. We choose PostgreSQL for its unique high-
performance batch writing capability through the SQL command COPY FROM , ensuring
efficient data storage.
• Metric Recorder: Recording specific metrics during simulations enables researchers to
compare experimental results across different studies and derive valuable scientific insights.
To facilitate research collaboration, we opt for mlflow with centralized server capabilities,
rather than local storage-based metric recording tools like tensorboard.
The primary purpose of the large-scale social simulation engine is to execute social simulation
experiments, which consist of a set of computational tasks comprising environment simulation and
agent execution. In implementation, an experiment corresponds to an Agent Simulation object.
This object will create and manage environment simulators through subprocess mechanisms, while
utilizing the Ray framework to create multiple agent groups that execute agents through multi-process-
based distributed computing. According to Ray framework design, each agent group functions as
a Ray actor operating within a single process. The Ray framework enables managed Ray actors
to work across different machines. By adding other machines to the head node during Ray cluster
initialization, distributed computing can be easily achieved to horizontally scale computational
resources for social simulation tasks. Within each agent group, clients connecting to the shared
services and the environment simulator are initialized, enabling multiple agents to work concurrently
using these client connections. Different experiments will share all shared services while utilizing
distinct Ray clusters and environment simulators to prevent mutual interference. The GUI with a
backend and a frontend connects to the database and MQTT server to enable the visualization of
simulation results, and allows users to directly interact with simulated agents by conducting dialogues
or sending questionnaires.
In conclusion, the system architecture integrates multiple cutting-edge open-source softwares to
deliver comprehensive capabilities for social simulation and enables researchers to focus exclusively
on social agent design, including distributed computing, LLMs, message transmission, data storage,
and metric management.
5.3 Group-based Distributed Execution
Based on the above description of the system architecture, we aggregate multiple agents into a group
called an agent group, and use a single process to execute each group of agents to achieve the effect
of distributed computing acceleration. This design addresses the contradiction between limited TCP
port resources and the massive number of agents. Specifically, if each individual agent were treated
as a separate process and independently connected to shared services to simulate autonomous human
decision-making in the real world, the large number of TCP connections would exhaust the TCP
port resources of the MQTT server, the database, and the metric recorder (with an upper limit of
65,535 ports), leading to failures due to insufficient TCP port resources. Therefore, how to implement
connection reuse to reduce TCP port resource consumption while ensuring independent execution of
multiple agents constitutes a critical issue that needs to be addressed in agent execution.
https://platform.openai.com/docs/overview
https://platform.deepseek.com/
https://ollama.com/
https://www.emqx.com/en
https://www.postgresql.org/
https://mlflow.org/
https://www.tensorflow.org/
19

CPU IO
Vanilla Python(Only 1 Process)
Distributed Execution by Ray
(Multiple Processes) Ray with asyncio (Multiple Processes & Coroutines)
CPU IO CPU IO CPU IO CPU IO CPU
Actor #1 CPU IO CPU IO
Actor #2 CPU IO CPU IO
Actor #3 CPU IO CPU IO
Actor #4 CPU IO CPU IO
Actor #1
CPU
IO
CPU
IO
IO
CPU
await
CPU
IO
IO
CPU
IO
await
Actor #2
CPU
IO
CPU
IO
IO
CPU
await
CPU
IO
IO
CPU
IO
await
+ Ray
+ asyncio
Figure 11: Asynchronous multi-process parallel execution using Ray and asyncio.
To address this issue, we evenly distribute agents into multiple agent groups, each configured with an
LLM API client, an MQTT client, an environment client, a database client, and a metrics recorder
client. All clients are implemented using asynchronous calls and support parallel execution. Since
LLM-driven social simulations are I/O-intensive tasks, primarily consuming time in LLM calls and
environment interactions. Leveraging the asynchronous I/O capabilities provided by asyncio and
multi-process parallel execution powered by Ray shown in Figure 11, the engine allows multiple
agents to concurrently send LLM requests while fully utilizing CPU resources for computational
tasks in agent design like running gravity models, effectively avoiding time waste caused by waiting
for LLM responses. The asynchronous approach with connection reuse does not impose specific
constraints on agent execution order, ensuring independence among agents. By organizing agents
into groups, the total number of TCP ports required by the system can be reduced to a multiple of
the number of agent groups (depending on optional services such as metrics recording), thereby
preventing issues caused by TCP port exhaustion. However, immutable fixed-number grouping would
result in the overall system efficiency being constrained by the slowest group. Therefore, adaptive
load balancing and dynamic scheduling across groups represent an important direction for future
research.
In summary, by combining group-based asynchronous and parallel execution with distributed imple-
mentation to enhance simulation efficiency, we successfully address the critical issue of execution
failures caused by port exhaustion.
5.4 MQTT-powered Agent Messaging System
MQTT Server
MQTT Client
Agent Group #1
MQTT Client
Agent Group #N
…GUI
exps/<exp_uuid>/agents/<agent1_uuid>/#
exps/<exp_uuid>/agents/<agent2_uuid>/#
exps/<exp_uuid>/agents/<agent3_uuid>/#
exps/<exp_uuid>/agents/<agent4_uuid>/#
exps/<exp_uuid>/agents/<agent5_uuid>/#
exps/<exp_uuid>/agents/<agent6_uuid>/#
Subscribe
Publish
Subscribe
Publish
Publish …
…
Figure 12: Overview of MQTT-powered agent messaging system.
Communication between agents is an essential component in constructing social simulations based
on LLM-powered multi-agent systems. The transmission of textual messages among agents simulates
real-world human communication and collaboration through language, which will facilitate the
emergence of group behaviors and thereby further approximate the operational laws of the real
world. Expanding on this, developing a messaging system that connects agents will enable users or
external programs to directly access and intervene in the agents’ behaviors. This will support more
sophisticated social experiments and interactive applications.
20

To achieve the aforementioned agent messaging system, we need a messaging system capable of
delivering messages to hundreds of thousands of specific agents by IDs. In the IoT domain, MQTT is
a protocol designed to enable communication between millions of IoT devices and control centers, em-
ploying a publish/subscribe architecture. Publishers send messages to specified IDs, while subscribers
monitor specific IDs or designated prefixes to receive messages. MQTT utilizes a lightweight packet
structure tailored for low-bandwidth IoT environments, delivering reliable messaging with minimal
resource consumption. Although originally designed for IoT device connectivity, this protocol aligns
perfectly with the communication requirements of agents in the large-scale social simulator. We
therefore adopt this protocol to implement our agent messaging system as shown in Figure 12. During
implementation, we designate the following topics and their corresponding message meanings:
• exps/<exp_uuid>/agents/<agent_uuid>/agent-chat: Used for sending messages
from one agent to the target agent within the experiment.
• exps/<exp_uuid>/agents/<agent_uuid>/user-chat: Used for users to send chat
messages to the target agent within the experiment via the GUI.
• exps/<exp_uuid>/agents/<agent_uuid>/user-survey: Used for users to send struc-
tured JSON-formatted surveys to the target agent within the experiment via the GUI.
Under this topic configuration, each agent only needs to subscribe to messages prefixed with
exps/<exp_uuid>/agents/<agent_uuid>/. This approach reduces development costs while
maintaining compatibility for future extensions to the messaging system’s functionality.
In summary, by integrating the advanced IoT communication protocol MQTT, we achieve low-cost
development to simultaneously connect hundreds of thousands of agents while ensuring reliable
agent message transmission. This solution also enables user input through GUIs and supports
future functional extensions, thereby filling a crucial gap in the architecture of the large-scale social
simulation engine.
5.5 Utilities
In addition to the aforementioned key technical designs for social agents, we also provide a rich set
of utilities to facilitate the development of social agents. The design philosophy of most of these
utilities is primarily inspired by AgentScope [40].
LLM API Adapter. We implement calls to OpenAI API-compatible LLMs through the openai
python library, including OpenAI, DeepSeek, Qwen, etc. Additionally, we also support calls
to ChatGLM. Through the LLM API adapter, we allow users to freely select their preferred or
partnered LLMs for inference by modifying configurations, which enhances the system’s flexibility
and compatibility.
Retry Mechanism. To prevent abnormal results returned by the LLM API from affecting experiments,
the system incorporates a retry mechanism. When invoking the LLM API, if erroneous responses are
detected, the system will automatically reinitiate the call. The default number of retries is set to 3.
JSON Parser. Since prompts often require LLMs to return responses in JSON format to facilitate
parsing into program-processable results, we develop a JSON parser. This parser automatically
identifies JSON code blocks in responses, removes Markdown code block delimiters (prefix and
suffix), and converts the content into Python objects.
Metric Recorder. To assist researchers in recording various statistical metrics during experiments,
such as total GDP and agent state averages, we adapt the mlflow API and implement a parallel-safe
metric logging utility class and functions.
Logging and Saving. Logging and saving simulation processes and results serve as the foundation
driving subsequent data analysis and visualization. Saving as much data as possible will facilitate
richer and more profound research insights. Accordingly, we design both local file storage using
the A VRO format and PostgreSQL database as online storage. Both storage approaches employ
https://pypi.org/project/openai/
https://bailian.console.aliyun.com/
https://bigmodel.cn/
https://avro.apache.org/
21

similar schemas to archive social agent profiles, agent states during simulations, thoughts and
dialogues, and survey outcomes. Additionally, experimental metadata including IDs, names, durations,
configurations, and error messages is systematically recorded.
GUI. To help people directly observe the behavior of social agents in environments and allow users
to engage in direct conversations or surveys with the agents, we develop a GUI program. The GUI
program includes functionalities for experiment management, survey administration, and real-time
monitoring or playback of experiments. During real-time monitoring, users can interact with agents
through instant conversations or send surveys, with these communications being transmitted via the
agent messaging system while awaiting responses. Additionally, during both real-time monitoring
and playback, users can view agent-related records stored in a PostgreSQL database, including their
locations, profiles, status history, thought and dialogue history, and survey response histories. We
aim for this GUI to help users build intuitions about agent societies and facilitate deeper analysis and
applications.
5.6 Toolbox for Social Experiments
In the realm of social sciences, various research methods are employed to study human behavior,
motivations, and responses in different contexts. In real-world settings, it is often difficult to find
controlled environments for conducting social experiments that mirror the complexity of human
interactions. This is where interventions come into play—creating specific social experimental
conditions that allow researchers to simulate and manipulate real-life scenarios. Besides, two widely
used methods are interviews and surveys, both of which allow researchers to collect data from
individuals, explore their opinions, and understand the underlying psychological factors influencing
their actions. These methods are vital for generating insights into how people think, feel, and act in
specific situations. Large-scale agent-based simulations provide a powerful tool for addressing these
challenges, enabling the design of controlled experiments with a high degree of realism. This section
details the tools available for conducting interventions, interviews, and surveys with agents in a social
experiment. These tools offer flexibility in data collection and manipulation, supporting the design
and execution of robust social experiments.
Intervention. Intervention refers to the manipulation of an agent’s behavior or state to observe how
changes influence its actions, thoughts, and emotional responses. Interventions are crucial for setting
up experimental conditions in social experiments. There are three primary types of intervention in
our system:
• Agent Configuration: This type of intervention involves directly modifying the internal
settings of the agent before the simulation starts. These settings may include altering an
agent’s personality traits, goals, or preferences. Since this intervention occurs before the
simulation, it ensures that the agent’s behavior aligns with the experimental conditions right
from the start.
• State Manipulation: This intervention occurs during the simulation and allows researchers
to modify the agent’s current state. By altering an agent’s profile, mood, or ideas, researchers
can influence its behavior. For instance, modifying the agent’s emotions can impact its
decision-making and social interactions.
• Message Notification: This method involves sending a text message to the agent, triggering
a response. For example, a message such as "Severe weather changes expected, a hurricane
is coming" could be used to observe how the agent adjusts its plans or behavior in response
to external threats. This type of intervention can be introduced at any point during the
simulation, offering flexibility in creating different experimental conditions.
The intervention process can be summarized as:
Pre-Simulation Configuration
Agent Settings
− − − − − − − →Agent Behavior Start
During Simulation
Memory Manipulation
− − − − − − − − − − − →Behavior Adjustments
During Simulation
Message Notification
− − − − − − − − − − − →Behavior Modification
These intervention techniques allow for dynamic and flexible modifications of the agent’s behavior,
providing valuable insights into the impact of specific changes on social interactions and decision-
making.
22

Interview and Survey. An interview is a process of one-on-one or group-based questioning and
answering, typically used to gather detailed, qualitative information from participants. In our platform,
users can directly communicate with agents through either a front-end interface or programmatically
via code. The system uses MQTT to distribute the user’s questions to the relevant agents. The agent
then answers these questions by processing both its internal state and the surrounding environmental
context. Importantly, this process is designed so that the agent can respond without interrupting
its ongoing actions. This allows for real-time interaction while maintaining the flow of the agent’s
behavior. The interaction flow is depicted as:
Question
MQTT
− − − →Agent Processing
Answer
− − − − →User Response
This ensures that the agent can participate in interviews seamlessly while continuing its primary tasks
and goals.
A survey is a structured form of data collection, where a series of interview questions are combined
based on a specific set of rules. These rules include response formats (e.g., multiple-choice, ranking)
and the unique design elements determined by the survey creator (e.g., question order). Surveys
are typically used to gather quantitative data across a larger sample, offering a broader perspective
on trends or patterns. In our system, the structured survey is distributed to agents via MQTT, just
like interviews. However, the primary difference is that the agent’s responses follow a predefined
structure, ensuring consistent data collection across multiple agents. The agent processes the survey
questions sequentially, answering them from top to bottom after analyzing the format and response
rules. This structured data is then compiled into a format that is easy for the user to analyze. The
survey response process is modeled as:
Survey
MQTT
− − − →Agent Parsing and Responding
Structured Answer
− − − − − − − − − →Data Processing
This ensures that data collection is organized, reliable, and easy to process for social experiment
analysis.
The ability to conduct interventions, interviews, and surveys within our platform provides a powerful
toolkit for researchers conducting social experiments. These tools offer a structured approach to data
collection and behavioral modification, making it possible to simulate real-world social conditions in
a controlled environment. The flexibility to manipulate an agent’s settings, memory, and responses in
real-time ensures that a wide variety of social experiment scenarios can be tested, from understanding
individual behaviors to studying collective dynamics. This makes large-scale agent simulations an
invaluable resource for conducting complex social science research.
6 Performance Evaluation
In this section, we will analyze the performance of our proposed large-scale social simulator through
a series of comprehensive experiments in order to reveal its strengths and limitations from different
aspects. The experiments focus on the following key research questions:
• RQ1: What is the performance of the implementation of the societal environment?
• RQ2: What is the performance of the MQTT-powered agent messaging system compared to
alternative communication approaches?
• RQ3: What is the performance of the large-scale social simulator built from the above
components with LLM-driven agents?
All experiments were conducted on Huawei Cloud c7.16xlarge.4 cloud servers to ensure comparability
of results. To mitigate potential interference from rate-limiting effects inherent in LLM API calls
during large-scale social simulator execution, we chosen the DeepSeek API platform that officially
claims no request limit. Related experiments were specifically scheduled during DeepSeek’s off-peak
hours (05:00-07:00 local time) to maximize the LLM API throughput. According to a DeepSeek
website statement, the model used during the experiments was DeepSeek-V3 [65].
In the following content, we will present the experimental settings, results, and further discussion to
address RQ1 in Section 6.1. Those about RQ2 will be discussed in Section 6.2. Finally, in Section 6.3,
we will conduct detailed experiments to answer RQ3.
https://platform.deepseek.com/
https://api-docs.deepseek.com/quick_start/rate_limit
23

6.1 Societal Environment Performance
To evaluate the interaction performance with our simulation environment, we conducted a series of
experiments to show our environment is able to handle high concurrency tasks from massive agents.
Experimental Settings. We utilized the Social Environment Simulator tool-chain to generate varying
numbers of individuals: 1,000, 10,000, 100,000, and 1,000,000, as the specific load for the simulator
itself. The departure times of these individuals were distributed according to a typical weekday
pattern, and all simulations were set starting from the morning peak hour of 8:30.
The test queries were divided into setting queries and fetching data queries at a ratio of 1:999, meaning
one setting query after 999 steps of fetching query for each agent. This ratio was chosen because it
is close to the actual request distribution in real agent simulations with our framework. We limited
the maximum number of Social Environment Simulator processes from 2, 4, 8, 16, to 32. Each
experimental setup was repeated five times, lasting for 10 seconds, with queries per second ranging
from 102 to 105.
Performance Metrics. We conducted two experiments to evaluate our environment simulation
performance. First, we measured the simulation speed with the metric of calculating the time
consumption per simulation step, with the simulation time set to 24 hours. Second, we assessed
concurrency performance by measuring the increase in queries per second (qps) along with the change
in time consumption per simulation step.
Evaluation Results. The result of simulation speed is shown in Table 2. The results indicate that
even as the number of individuals and query rates increased significantly, performance degradation
was minimal, suggesting that our platform can effectively and timely handle massive interactions
between agents and the simulation platform.
Table 2: Mean time per step with different numbers of agents.
# of Agents Mean Time per Step (s) ± SD
103 8.578×10−3 ± 3.0 × 10−5
104 9.129×10−3 ± 1.5 × 10−5
105 1.800×10−2 ± 5.66 × 10−4
106 0.1680 ± 5.34×10−4
In conclusion, the simulation environment is capable of supporting extensive interactions without
significant degradation, making it solid for large-scale social simulations.
6.2 Agent Messaging System Performance
To validate the comparative advantages of MQTT over other messaging systems, we evaluated various
commonly used publish/subscribe systems or message queue systems, including Redis, RabbitMQ,
and Kafka.
Experimental Settings. To simulate real-world usage as closely as possible and comprehensively
evaluate the systems’ capabilities in terms of supported agent count and message throughput, we
designed the following experimental procedure. We assumed a total of 100,000 agents, with each
message containing 100 bytes of data. Each agent sends messages to 10 randomly selected agents.
Given the maximum available CPU cores are limited to 32, we selected parallel process counts from
{2, 4, 8, 16, 32} and reported the configuration achieving peak throughput. As simulator startup time
constitutes a small proportion of total simulation duration, initialization overhead was excluded from
measurements. We specifically recorded the time interval between message transmission initiation
and complete reception to calculate message throughput across different systems.
Compared Approaches. We briefly introduce the comparative methods as follows:
• Redis Pub/Sub: A lightweight in-memory publish/subscribe subsystem in Redis optimized
for real-time messaging with minimal latency. It uses a broadcast model where messages
are transient and not persisted, making it suitable for ephemeral data or scenarios requiring
https://redis.io/
24

high-speed communication. However, its lack of message durability and limited scalability
in high-volume environments may constrain its use in mission-critical applications.
• RabbitMQ: A robust message broker implementing the AMQP (Advanced Message Queu-
ing Protocol) standard. It supports complex routing logic, message persistence, and acknowl-
edgment mechanisms, ensuring reliable delivery. Its flexible exchange types (e.g., direct,
topic, fanout) and queue management make it ideal for enterprise workflows, though its
overhead increases with transactional guarantees.
• Kafka: A distributed streaming platform designed for high-throughput, fault-tolerant, and
persistent log-based messaging. Kafka organizes data into partitioned topics, enabling
horizontal scalability and parallel processing. Its append-only log structure and consumer
offset tracking make it well-suited for large-scale event streaming, real-time analytics, and
data pipelines, though it introduces complexity for lightweight use cases.
It is worth noting that all services are running on the experimental machine, and the distributed
version is not utilized.
Evaluation Methods and Metrics. In the evaluation of a messaging system, the most critical metric
is throughput, which refers to the number of messages that can be transmitted per second. Once the
throughput meets the requirements, we will further consider whether the software system provides
user-friendly auxiliary tools to help monitor the service’s operational status or facilitate testing and
configuration, such as dashboards. For throughput requirements, assuming all agents are always
attempting to communicate with other agents and the LLM generates a message every 5 seconds, the
minimum throughput the system needs to support would be 20,000 msg/s.
Evaluation Results. We conducted five tests on various messaging systems and calculated the mean
and standard deviation of throughput, as presented in Table 3. From the results, we observe that
MQTT, Redis Pub/Sub, and RabbitMQ meet the throughput requirements under the aforementioned
extreme conditions. Among them, RabbitMQ’s performance was only slightly above the throughput
requirement, thus it was the first to be excluded. The results for Kafka were not reported because it
could not even complete the initialization of 100,000 agents within 5 minutes; hence, no specific test
results were available. Although MQTT’s throughput is approximately half that of Redis Pub/Sub,
its built-in GUI tools can effectively assist users in simple service monitoring, debugging, and
testing, which constitutes the primary reason for our ultimate selection of MQTT as the default
implementation for the agent messaging system. Regarding Redis Pub/Sub’s high-performance
characteristics, we propose that the simulation engine should support flexible user specification
of backend implementations for agent messaging systems in the future, thereby accommodating
application scenarios with stringent requirements for inter-agent communication.
Table 3: Comparison of different messaging systems.
System Best Parallel Process Number Throughput (msg/s) Auxiliary Tools
MQTT (emqx v5.8.1) 32 44, 702.1 ± 111.3 Built-in GUI
Redis Pub/Sub (v6.2) 16 81, 216.2 ± 333.6 -
RabbitMQ (v4.0.5) 16 23, 667.3 ± 1, 777.7 Built-in GUI
6.3 Social Simulator Performance
To evaluate the scalability and efficiency of the proposed social simulation framework, we conducted
a series of experiments designed to replicate the execution of large-scale intelligent agents under
realistic conditions.
Experimental Settings. The experiments were conducted on a 64-core machine, with 32 cores
allocated to running the environment and the remaining 32 cores dedicated to executing the simulation
engine.Testing was performed during the system’s low utilization period, while targeting simulation
time intervals where agent activities were relatively high to ensure representative measurements.
We evaluated the system throughput by simulating {103, 104} agents, The number of processes was
varied as {8, 16, 32}.
https://www.rabbitmq.com/
https://kafka.apache.org/
25

Performance Metrics. To evaluate the system’s performance, the following metrics were collected:
• Total execution time: The total time required for all agents to complete five interaction
rounds.
• Token usage statistics: The total number of input and output tokens utilized during the
simulation.
• LLM time cost distribution: The distribution of response times for calls to the LLM API,
providing insights into latency variability.
• Environment time cost distribution: The distribution of response times for calls to the
environment API, measured to evaluate internal system performance.
Evaluation Results. The evaluation results are summarized in Table 4, which demonstrates the
system’s scalability as the number of agents increases and highlights the performance impact of
distributed computing. Specifically, the table shows how performance metrics such as LLM call time
and environment response time vary with different group configurations (8, 16, and 32).
Figure 13 presents four distribution plots that illustrate key metrics in large-scale LLM interactions
with 10k agents under varying group configurations. The first two plots, Figure 13a and Figure 13b,
show the distributions of input and output tokens, respectively. These plots reveal that token usage
patterns remain remarkably stable across different configurations, indicating that parallelization does
not significantly alter the overall amount of data being processed. In contrast, Figure 13c shows the
distribution of LLM API call times, revealing that the time required for API calls is more sensitive to
the level of parallelization. Finally, Figure 13d presents the environment time cost distribution, which
illustrates how the environment’s responsiveness fluctuates with the number of groups.
Table 4: Performance metrics for different configurations.
Parameters Average Time Cost
#Agents #Groups LLM Calls ITs (/call) OTs (/call) All (s/round) LLM (s/call) Env (ms/call)
103 8 4803.0 430.04 79.17 82.45 4.51 12.26
103 16 3120.8 398.78 77.18 41.17 2.92 14.31
103 32 4790.4 412.82 75.56 43.30 2.94 9.55
104 8 54135.4 430.35 75.84 5681.18 52.54 33.55
104 16 54002.2 430.24 75.80 1422.48 3.53 33.55
104 32 54075.0 430.47 76.14 458.82 8.05 30.53
The Average Time Cost analysis provides deeper insights into the system’s performance, as sum-
marized in Table 4. The total time per round (All) decreases as the number of groups increases,
demonstrating the positive impact of parallelization on processing efficiency. This trend reflects the
effectiveness of the distributed parallel framework, which optimally utilizes multi-core computa-
tional power, minimizing the CPU bottleneck and enabling the system to handle larger agent scales
efficiently. However, the LLM time remains the primary bottleneck in the system, even under fully
parallel conditions. Despite the reduction in execution time with more groups, LLM API calls still
represent a significant portion of the total execution time. This is due to the nature of the external API
calls, where server-side load introduces variability and causes unpredictable performance fluctuations.
As shown in the evaluation results, the environment time (Env) remains minimal, in the millisecond
range, which indicates that the system is capable of supporting large-scale simulations with minimal
impact from the environment processing.
The experimental findings also highlight that the execution efficiency of large-scale agents is pri-
marily constrained by the LLM API calls. Under fully parallel conditions, this constraint becomes
more pronounced, making LLM performance a critical factor in scaling agent-based simulations.
To achieve more stable operation for larger-scale simulations (e.g., >104 agents), researchers may
consider deploying a private LLM inference service. While this approach could offer more reliable
performance, it comes with substantial initial costs, including GPU deployment and model configura-
tion selection. The token distribution data in this study could serve as a reference for estimating GPU
resources and model configurations required for such a deployment.
In conclusion, the experiments demonstrate the simulation engine’s ability to efficiently handle
large-scale agent execution. However, the findings also emphasize the need for careful consideration
26

(a) Input Token Distribution
 (b) Output Token Distribution
(c) LLM Time Cost Distribution
 (d) Environment Time Cost Distribution
Figure 13: Distribution analysis for 10k agents.
of LLM API performance and the trade-offs involved in private deployment options. To improve
stability and scalability, further research should focus on optimizing the LLM infrastructure or
exploring alternative solutions for large-scale intelligent agent simulations.
7 Exemplary Social Experiments
7.1 One Day Life
This section presents a self-directed day in the life of a socially intelligent agent, illustrating how
it navigates daily tasks while balancing internal needs, emotional states, and cognitive processes.
Through a simulated 24-hour scenario, we examine how the agent’s dynamic priorities influence
its decisions across three domains: mobility (e.g., route planning with energy constraints), social
interaction (e.g., adapting communication style to context), and economic behavior (e.g., resource
allocation under uncertainty). This micro-level analysis serves to validate the coherence of its
behavioral patterns and their alignment with human-like temporal rhythms. The one day life journey
for a specific person is shown as Tab.6.
By examining this one-day life scenario, we can see how the agent’s needs drive the formation of a plan
and lead to specific actions (mobility, social, economy, other), all of which are continuously shaped
by the agent’s cognition. Through this table, the agent demonstrates behaviors that reflect realistic
decision-making processes across various domains—managing its hunger, social connections, work
responsibilities, and leisure. Such a framework helps researchers evaluate the consistency and depth
of the agent’s behavior, providing a solid basis for exploring more complex social interactions and
collective dynamics in virtual environments. Besides, Tab 5 summarizes the number of interactions
between the social agent and various environmental spaces during a typical day.
Based on the Social Agent’s capability to simulate a one-day life, we further conducted simulation
experiments in the domains of cognition, social interaction, economics, and mobility. These experi-
ments were designed to validate the Social Agent’s proficiency in capturing behaviors across various
domains, as illustrated in Fig.14.
27

Table 5: Daily environment interactions per agent.
Space Interaction Type Counts
Urban Space Get 465.67
Set 4.27
Economy Space Get 9.26
Set 3.30
Social Space SendMessage 9.08
Sum ALL 491.68
DailyLifeofSocialAgent
Needs
Behavior
Experiments
Mobility
Social
Economy
Cognition
MemoryStatesProfile
Columbia
1,000AgentsWeatherChange
ActivityLevelActivityLevel
ExternalShocksofHurricane
Texas
100AgentsCash distributionEconomic MetricSocial Metric
New York
100AgentsCurrent GunControlPolicyOpinion DistributionSocial NetworkPolarizationExperiment
100Agents
Spread of InflammatoryMessages
Social Network
InflammatoryMessages
Information PropagationEmotion DynamicsUBIExperiment
BehaviorSpace
Figure 14: Experiment configuration overview.
7.2 Polarization
Polarization is a phenomenon where opinions within a population become increasingly divided, often
forming distinct clusters that are difficult to reconcile. Understanding polarization is critical because
it influences how societies debate, make decisions, and implement solutions to pressing challenges.
By studying the factors that drive polarization, researchers can uncover why divisions deepen over
time and how they can be addressed. This research provides valuable insights into fostering more
(a) Large-scale Simulation
 (b) Self-driven Daily Life
Figure 15: Large-scale social simulation.
28

Table 6: One Day Life
Actions Mind
(08:00–12:30)
• Commute to office (Mobility)
• Respond to priority emails (Economy)
• Attend project planning meeting (Econ-
omy)
• Coordinate cross-department tasks (Econ-
omy)
• Need: Safe
• Emotion: Resentment
• Cognition: "Sequential task execu-
tion ensures workflow integrity"
(12:30–13:30)
• Commute via grocery store (Mobility)
• Compare product prices (Economy)
• Prepare lunch (Other)
• Eat (Other)
• Need: Hungry
• Emotion: Disappointment
• Cognition: "Economic constraints
necessitate adaptive consumption
patterns"
(13:30-14:00)
• Browse social networking sites (Social)
• Find friend to contact with (Social)
• Send message to friend (Social)
• Need: Social
• Emotion: Gratification
• Cognition: "Social capital accu-
mulation facilitates opportunity
discovery"
(14:00-18:00)
• Develop quarterly budget (Economy)
• Mentor junior staff (Other)
• Inspect branch office locations (Mobility)
• Submit audit report (Economy)
• Need: Safe
• Emotion: Relief
• Cognition: "Multi-layered verifi-
cation prevents operational risks"
(18:00–20:00)
• Go back home (Mobility)
• Check refrigerator (Other)
• Prepare dinner (Other)
• Eat dinner (Other)
• Need: Hungry
• Emotion: Gratification
• Cognition: "Having finished the
day’s work, I was pleased with my-
self"
(20:00–22:00)
• Browse webpages(Other)
• Play video games(Other)
• Need: Whatever
• Emotion: Relief
• Cognition: "Entertainment makes
me feel relaxed"
(22:00–24:00)
• Complete bedtime routine (Other)
• Go to sleep (Other)
• Need: Tired
• Emotion: Satisfaction
• Cognition: "Resource allocation
efficiency impacts systemic stabil-
ity"
29

(a) (b) (c)
Figure 16: Opinion changes on the political issue of Gun Control across three experimental setups.
cohesive societies, promoting constructive dialogue, and navigating complex issues in a way that
incorporates diverse perspectives.
To investigate the dynamics of polarization, an experimental setting is designed to simulate discussions
among agents focused on a specific policy issue: gun control. In the control group, agents engage
in discussions about the gun control issue, with opinions naturally divided between support and
opposition. No external interventions are introduced in this setting, allowing opinions to evolve
organically through agents’ autonomous social interactions. Two treatment groups are introduced
to study the effects of persuasive messages on opinion dynamics. In one treatment group, agents
are only exposed to persuasive messages that align with their existing opinions, which we refer to
as the homophilic interaction group. In the other treatment group, agents only receive persuasive
messages with opposing opinions, which is the heterogeneous interaction group. This experimental
setup provides a ground to analyze how different opinions contribute to the formation of polarization.
Figure 16 presents the opinion changes on the political issue of Gun Control across three experimental
setups: (a) the control group, (b) the homophilic interaction group, and (c) the heterogeneous interac-
tion group. In the control group, where agents engage in discussions without external interventions,
39% of agents adopt more polarized opinions, while 33% become more moderate after interactions.
By contrast, in the homophilic interaction group, a clear polarization pattern emerges, with 52% of
agents becoming more polarized. This result suggests the effect of echo chambers, where excessive
interactions with like-minded peers can potentially intensify opinion polarization. In the heteroge-
neous interaction group, 89% of agents adopt more moderate opinions, and 11% are persuaded to
adopt opposing viewpoints. This indicates that exposure to opposing content and opinions could be
an effective mitigation strategy for curbing polarization.
7.3 Spread of Inflammatory Messages
Information propagation in social networks is a fundamental research problem in social computing.
Social networks enable users to share various types of content such as news, personal status updates
and public discussions. Among these information flows, inflammatory messages containing extreme
opinions and inaccurate claims present significant challenges. These messages can quickly spread
across social networks and increase conflicts in online discussions. Standard information diffusion
models cannot fully explain how inflammatory messages propagate [84, 21], because user sharing
behaviors often deviate from typical patterns when encountering such content. Additionally, current
content moderation systems on social platforms face difficulties in balancing effective content filtering
with maintaining regular user communications. Simulation experiments offer a practical approach to
analyze these propagation dynamics and test different intervention methods, providing insights that
complement real-world social network studies.
To investigate the spread of inflammatory messages, we design experiments based on a real-world
event, the case of the chained woman in Xuzhou [39]. Using a population of hundreds of agents, our
experiments consist of four parts. In the control group, we place non-inflammatory seed messages at
selected nodes and observed the natural progression of information spread and emotional evolution
within the group. For the experimental group, we introduce emotionally charged, selectively expressed
inflammatory messages at certain nodes to examine whether these would alter the trajectory of
30

information spread and emotional dynamics. To simulate the suppression of inflammatory messages,
we implemented two intervention strategies: node intervention and edge intervention. In both
approaches, the social platform monitors messages sent by agents, using large language models
to determine if content is inflammatory. Under node intervention, accounts that repeatedly share
harmful inflammatory content above a certain threshold are suspended. With edge intervention, when
inflammatory content is detected traveling between two nodes, the social connection between them is
permanently removed. We track how these interventions affect both information propagation patterns
and the evolution of group emotions. Finally, we conduct interviews with agents to understand their
motivations for sharing messages, helping us uncover the underlying psychological and social factors
that drive information-sharing behavior when encountering inflammatory content.
0 5 10 15 20 25 30
Time Step
0.0
0.2
0.4
0.6
0.8
1.0Information Spread
Control Group
Experimental Group
Node Intervention
Edge Intervention
(a) Information Spread over Time
0 5 10 15 20 25 30
Time Step
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7Emotional Intensity
Control Group
Experimental Group
Node Intervention
Edge Intervention (b) Emotional Intensity over Time
Figure 17: Simulation results of the spread of inflammatory messages.
Our experimental results are shown in Figure 17. The experimental results demonstrate distinct
patterns in information propagation dynamics and emotional responses across different intervention
strategies. Our findings validate that inflammatory messages exhibit unique diffusion characteristics
compared to regular content in social networks. The experimental group, where inflammatory
messages are introduced, shows substantially higher information reach than the control group with
non-inflammatory content, confirming that inflammatory messages possess stronger viral potential in
social networks. This observation aligns with previous findings about the deviation of inflammatory
content from standard diffusion patterns [84, 21].
The intervention strategies demonstrate varying degrees of effectiveness in managing inflammatory
content spread. Node-level intervention, which suspends accounts that frequently share inflammatory
content, proves to be the more effective approach in containing information propagation. Edge-
level intervention, while showing moderate containment effects, is less efficient than node-based
approaches. This difference suggests that targeting individual spreading behaviors might be more
effective than modifying network structure for content moderation.
The emotional intensity measurements provide additional insights into the intervention dynamics.
The experimental group exhibits markedly elevated emotional responses compared to the control
group, indicating that inflammatory messages significantly amplify emotional engagement within
the network. Node intervention demonstrates superior effectiveness in moderating these emotional
responses, achieving substantial reduction in overall emotional intensity. Edge intervention, though
less effective than node-based approaches, still shows notable moderation effects on emotional
dynamics.
Interview analysis reveals key factors that drive inflammatory message sharing behavior, as shown
in the word cloud in Figure 18. The responses mainly focus on emotional reactions and social
responsibility. Analysis shows that strong emotions, especially sympathy and worry, often trigger
sharing behaviors. Many agents share information because they feel they have a duty to let others
know about important social issues. The interviews show that agents think about the broader social
impact when sharing information, seeing it as a way to join public discussions. Agents also show clear
goals in their sharing behavior, mainly wanting to increase public attention and get responses from
institutions. These findings suggest that inflammatory message spread is driven by both emotional
31

Figure 18: Agent opinions on the chained woman incident.
factors and social awareness. Understanding why agents share such messages helps us develop better
content moderation strategies in social networks.
These experimental results demonstrate three key findings in inflammatory content management.
First, inflammatory messages show stronger viral potential and trigger higher emotional responses
compared to regular content. Second, node-level intervention is more effective than edge-level
intervention in both containing information spread and moderating emotional intensity. Third,
through agent interviews, we find that emotional factors and social responsibility drive sharing
behaviors. These findings provide empirical evidence for designing content moderation systems,
suggesting that user-level interventions combined with consideration of emotional and social factors
may lead to more effective control of inflammatory content in social networks.
7.4 Universal Basic Income
Universal Basic Income (UBI) has always been a highly controversial macroeconomic policy. The
implementation cost of UBI is enormous, and the outcomes of UBI policies around the world have
shown inconsistent effects on both the participants and economic development. Therefore, accurately
understanding the impact of UBI on the socio-economic environment and its underlying reasons is
crucial in determining whether UBI policies should be implemented in the real world to alleviate
poverty. Based on our simulation platform, we conduct intervention experiments on UBI and explore
its effects on both agents and the macroeconomics.
We conduct two macroeconomic simulations based on the demographic distribution of residents in
cities that have implemented UBI policies (Texas, USA). One simulation is without the UBI policy,
while the other incorporates UBI intervention, where each agent is given a monthly unconditional
payment of $1,000. By comparing the economic and social metrics generated from both simulations,
we explore the impact of the UBI policy and assess whether these influence align with the outcomes
observed in Texas’ UBI social experiment.
The basic simulation results are shown in the Figure 19, including the simulated curves of real GDP
and agent consumption levels. As can be seen, as the simulation progresses, the fluctuations in the
curves become smaller, indicating that the economic system is stabilizing.
We introduce the UBI policy at step 96 of the simulation and compare the economic and social metrics
of the two simulation results over the next 24 steps in Figure 20, namely agent consumption levels
and depression levels, with depression levels assessed through surveys using the widely recognized
Center for Epidemiologic Studies Depression Scale (CES-D) [83]. The comparison shows that the
UBI policy increases consumption levels and reduces depression levels, which is similar to the impact
observed in Texas’ UBI policy [14], thus validating the realism of the simulation.
32

0 25 50 75 100 125
step
0.8
1.0
1.2
1.4Real GDP
1e6
(a) Real GDP
0 25 50 75 100 125
step
0
5000
10000
15000Consumption (b) Consumption Level
Figure 19: Simulation results of the economic system.
w/ UBI w/o UBI
Experiment
6500
7000
7500
8000Consumption
(a) Consumption Level
w/ UBI w/o UBI
Experiment
17
18
19
20
21
22Depression (b) Depression Level
Figure 20: The comparison of economic and social metrics.
We also interview agents about their views on the UBI policy, which are summarized in the word
cloud in Figure 21. The results show that the impact of the UBI policy is mainly related to key terms
such as interest rates, long-term benefits, savings, and necessities of life, reflecting the common
perceptions of UBI policy in the real world.
Figure 21: Agent opinions on UBI policy.
7.5 External Shocks of Hurricane
The impact of external disasters on human mobility is a critical area of study due to their profound
effects on societal structures and individual behaviors. Understanding how such events influence
human movement patterns is essential for enhancing emergency response strategies and mitigating
potential risks. Hurricanes, as severe natural disasters, pose significant threats to human life and
property. The destruction of infrastructure, displacement of populations, and disruption of daily
activities necessitate a comprehensive understanding of human mobility during such events.
33

The experiment focuses on Hurricane Dorian, which impacted the southeastern United States in
2019. The city of Columbia, South Carolina, serves as the primary case study due to its significant
population density and the availability of detailed mobility data. The analysis utilizes two primary
data sources:
• SafeGraph Data: Provides comprehensive information on points of interest (POIs) and
human mobility patterns (from 2019.8.28 - 2019.9.5).
• Census Block Group (CBG) Data: Offers demographic profiles of residents, facilitating
the sampling of city residents’ profiles (including gender, age, race, income, home cbg, etc.).
These datasets are integrated to model and analyze the movement behaviors of social agents during
the hurricane event.
Specifically, the experiment involves 1,000 social agents, and incorporates real-time weather updates
to influence agent behaviors, thereby reflecting the dynamic nature of human responses to the
hurricane. We evaluate mobility patterns through two metrics: 1) Activity Level ( Traveling Individuals
Area Population ),
visualized through three phase-specific maps. The results are shown as Fig.22. 2) Total Daily Trips
(9-day normalized time-series). The result is shown as Fig.23.
According to Fig. 22, the hurricane significantly impacts the mobility behavior of the social agent.
Before the hurricane, the average activity level (defined as the ratio of travelers to the total population)
across the CBGs remained between 70% and 90%. However, when the hurricane arrived, the activity
level sharply decreased to approximately 30%, indicating a significant reduction in mobility behavior.
After the hurricane passed, the activity level gradually returned to normal levels. This analysis
suggests that the social agent could adapt its mobility demand effectively based on environmental
information, mimicking human behavior in response to extreme weather events.
(a) Before landfall (8.28-8.30)
 (b) Landfall (8.31-9.2)
 (c) After landfall (9.3-9.5)
Figure 22: Activity level spatial distributions.
The line graph presented above (Fig. 23) compares the daily outflow patterns of the real data with the
simulated visits over the course of the experiment. Both the real and simulated data exhibit similar
trends, with a noticeable decline in visit activity around August 30th, corresponding to the onset of the
hurricane impact, followed by a significant recovery in early September. Notably, while the simulated
visits closely follow the general trend of the real data, slight deviations are observed, particularly
during the hurricane’s peak. This suggests that the social agent’s behavior, while generally aligned
with actual human patterns, may exhibit some discrepancies in terms of the magnitude and speed
of response. However, the overall similarity in the temporal progression of visits indicates that the
simulation captures key aspects of human mobility under the influence of extreme weather events,
validating the social agent’s effectiveness in approximating real-world behavior.
The results effectively demonstrate that the constructed social agents, within the framework of the
social simulator, can accurately replicate human mobility behaviors and group characteristics during
a hurricane event. This validation underscores the simulator’s potential as a tool for analyzing
and understanding human responses to external shocks, thereby contributing to improved disaster
preparedness and response strategies.
https://www.safegraph.com/
https://docs.safegraph.com/docs/open-census-data
34

Figure 23: Normalized daily trips.
8 Related Works
The literature related to the work mainly consists of two kinds of work: large language model-driven
agents and social simulation.
8.1 LLM-driven Agents
Large Language Models (LLMs) exhibit astonishing language capabilities [99]. Since the language
ability is one of the most fundamental abilities of human intelligence, LLMs demonstrate excellent
performance in numerous tasks. Furthermore, researchers use LLMs as “brains" to construct LLM-
driven agents, endowing them with memory management, interactive interfaces, and expanded action
space [56].
The research on LLM-driven agents mainly consists of two parts [106]. One type uses LLM agents
as a tool for intelligent decision making [111, 85, 50]. By leveraging their individual capabilities,
these agents solve practical problems and serve as human assistants. This kind of work primarily
focuses on reasoning ability, tool using, learning, etc. For example, Boiko et al. [19] construct an
agent with large language models to autonomously conduct chemical experiments, by providing
computers to browse experimental tutorials and devices controlling interface for the experiments. The
other type of LLM-driven agents starts with the concept of agent-based modeling and agent-based
simulation [64, 39, 38]. Given that large language model agents exhibit human-like behaviors, they
can be made to engage in role-playing and imitating human behavior.
The primary research tries to reproduce the human response with large language model agents [77,
110, 39] or explain the gap better human and LLM agents [51]. These works borrow the memory and
reasoning mechanism of humankind [43, 114] to design various internal mechanisms on the basis of
large language models as brains. Some other work [76, 66] further design fine-tuning or alignment
strategies to enhance the agent’s role-playing abilities.
Overall, large language model agent is a field that is rapidly advancing with the development of LLM
and our understanding of LLM, especially in the ability to simulate real humans. However, there is
no platform to really unleash agent’s ability to simulate in the real world, which we aim to address in
this paper.
8.2 Social Simulation
Social simulation stands as a core technology in computational social science, generally categorized
into macrosimulation [ 96] and microsimulation [ 36]. The former typically models interactions
between macro-level variables by defining complex equations, while the latter adopts a bottom-
up approach to simulate emergent phenomena through granular agent behaviors. Among these,
microsimulation, which is often termed agent-based simulation, has become the more widely adopted
method. It operates by defining rules or models to govern individual agent behaviors, with the goal of
replicating and predicting real-world societal dynamics.
35

Cellular automata [105] represent a seminal class of agent-based modeling and simulation in early
research. Another notable example is Game of Life [ 26], which simulates the evolution and inter-
actions of lifeforms in a two-dimensional grid-based world. Subsequent advancements, such as
Sugarscape model [29], expanded the action space of simulated agents, enabling the exploration of
broader phenomena through rule-governed agent behaviors. For the applications in social sciences,
primary ABM research has focused on social interaction, economics, etc. For social interaction,
these key studies investigate collective behavior (e.g., cooperation) [42] and system dynamics (e.g.,
information propagation and crowd dynamics) [73], etc. For the economic domain, representative
work [37, 23, 12] targets macroeconomic systems, market dynamics, etc.
In recent years, within the field of computational social science, researchers have increasingly adopted
deep neural network-based models to simulate individual agents [ 97, 53]. However, significant
limitations persist, primarily due to the inherent complexity of modeling human behavior. Over the
past two years, large language models (LLMs) have emerged prominently, demonstrating human-
like cognitive capabilities, including contextual understanding, logical reasoning, and interactive
communication [74, 59]. This breakthrough has catalyzed growing interest in LLM-driven agent-
based simulations [38].
A pioneering example is the Generative Agent [77], which constructs a small-scale society within a 2D
game engine. Here, LLM-powered agents autonomously plan daily activities, exchange information,
and adapt to environmental stimuli. Researchers observed intriguing emergent phenomena, such as
self-organized information diffusion and collaborative group behaviors, revealing the potential of
LLMs to capture nuanced social dynamics. The authors further combine the large language models
with the real data of 1,000 human participants to simulate feedback [78]. Acerbi et al. [2] simulate
the information propagation and find human-like bias in the results of large language model agents.
S3 [39] further utilizes LLM-empowered agents to simulate individual-level and population-level
behaviors within the social network. In the economic domain, LLM agent-based simulations have
also achieved significant progress. For instance, EconAgent [64] has developed a macroeconomic
market simulation framework powered by large language agent-based models, with the simulation
outcomes aligning closely with established stylized facts. Beyond social interactions and economic
behaviors, researchers are expanding agent-based simulations to explore a broader spectrum of topics
in social sciences. For example, Zhang et al. [113] built a framework with large language model
agents to predict the results of the 2024 US Presidential Election.
Existing studies remain narrowly focused on isolated problems and rely on simplified environments,
such as text-based [4] or simplistic game environments [ 77], with limited attention to real-world
environment fidelity, revealing notable limitations. Besides, researchers have begun exploring
methods to scale up LLM-driven agents to support larger populations [94, 100, 109]. Nevertheless,
these efforts continue to grapple with critical limitations, including computational inefficiencies and
inaccurate user behaviors. Our proposed AgentSociety, consisting of LLM-driven generative social
agents, a realistic societal environment, and a powerful engine for large-scale simulations, overcomes
these limitations and advances the field of social simulation.
9 Discussion
9.1 Three Levels of Social Simulator
As an important interdisciplinary research, the development of social simulators can be categorized
into three levels. Research at the first level mainly focuses on constructing social twin systems, which
create a one-to-one mapping of real-world individuals. Such systems are always used to track and
detect real-world social behaviors. At the second level, on top of the mirroring world, it can predict
future changes and support intervention experiments in this society. By comparing the impacts of
different intervention measures on the simulated society, the performance of different policies can
be evaluated. The third level represents a further breakthrough in blurring the boundaries between
the real and virtual worlds, leading to a coexistent hybrid world that integrates the simulator with
real society. Specifically, the simulated individuals can interact with real-world individuals, and their
decisions will influence each other. Furthermore, decisions made based on the social simulator can
actually impact real society.
The social generative simulator developed in this paper is a pioneering attempt and exploration of
the third, i.e., the highest-level social simulator, and provides effective solutions. Specifically, the
36

social simulator based on large language model-driven agents demonstrates its advantages in the
following aspects. First, through the high-fidelity behavior imitation and generation capabilities of
large language model agents, the role-playing simulation of the real individual is achieved. That
is, agents built on human-like memory mechanisms can accurately reproduce user states in various
aspects such as cognition, social interaction, economy, etc. Second, this platform enables accurate
prediction of individual future behaviors and group evolution trends through precise short-term or
long-term simulations. The experiments also validate the effectiveness of evolution under different
intervention conditions, demonstrating the value of the platform as an assistance tool for decision-
making. Last, this platform’s simulated society coexists with the real physical society. By coupling
with a real-time urban simulator, its simulation process can be synchronized with and interact with
real society. In short, our platform could be considered as the recent advance of social simulators on
the highest level.
9.2 Social Simulator: New Paradigm of Computational Social Science
Computational social science is an interdisciplinary research area where various computational
approaches are used for social sciences. Essentially, the core distinction between computational
social science and traditional social science lies in the introduction of diverse computational methods.
In other words, these studies attempt to address the challenges of social science research using
computational approaches. Generally, related work can be understood from three perspectives. First,
as an explanation tool, it involves pattern recognition and mining from data, such as uncovering macro-
level patterns and key characteristics in the evolution of social networks. The second category is the
predictive paradigm, which involves constructing computational models to forecast future changes in
system variables, such as predicting the number of individuals who will forward a specific message
in a social network. Recently, some researchers have attempted to use LLMs as “silicon samples”
for social experiments [11, 9, 86, 93, 4, 28]. Their experiments have demonstrated the capability
of LLMs to generate human-like experimental samples in studies from political science [ 9, 11],
psychology [28, 93], and behavioral science [11]. However, these “silicon samples” are primarily
limited to basic role-playing configurations, overlooking the effects of psychological processes,
complex social behaviors, and societal environments on experimental outcomes. Moreover, these
limitations constrain the scope of the experiments, making some complex designs, such as the
distribution of universal basic income, infeasible.
Beyond these two categories, there is a third simulation paradigm of agent-based modeling, which
simulates each individual in a bottom-up manner, by constructing rule-based or model-based agents.
However, existing computational social science research faces substantial difficulties in simulation
(primarily due to the lack of effective methods for achieving precise simulation), and thus, this
paradigm has not truly surpassed the first two. Some famous examples of agent-based modeling in
social sciences include the Epidemic Spread Models, Schelling’s Segregation Model, the Sugarscape
model, etc. While these models can, to some extent, reproduce the patterns of change in macro-level
variables, they involve significant simplifications, and the realism of individual behaviors within
them is very limited. For instance, in the research of economics, although methods with agent-based
modeling were proposed early on, it is widely acknowledged by economists that ABM model has not
achieved the precision of predictive models. Furthermore, another challenge in computational social
science is the difficulty in accessing, intervening in, and controlling the subjects (human individuals)
of research. The computational models of computational sociology and field experiments are often
isolated; typically, the data is collected first, followed by the design and application of computational
models. The human participants are difficult to select, observe in depth, and interact in the long term.
Therefore, the large-scale social simulator proposed in this work represents a breakthrough as a
fourth paradigm for computational social science: an agent-based simulation paradigm centered on
highly realistic human-like agents. This paradigm supports analysis, prediction, and high-precision
bottom-up simulation, allowing for arbitrary selection, intervention, and control of experimental
subjects. It facilitates various computational social science research endeavors, including theory
validation, pattern discovery, etc.
9.3 From Policy Making, Risk Control, to Future Human-AI Society
In the above experiments, we have validated specific application examples of the large-scale social
simulator. From a broader perspective, we contend that the utility of such a simulator extends far
37

beyond these implementations, encompassing urgent societal governance challenges, widely debated
AI risks, and more forward-looking futuristic societal applications.
9.3.1 Policy making and social management for a smarter society
Traditional decision-making processes for society management primarily rely on mining and analyz-
ing historical data to construct computational models for evaluating policy effectiveness. However,
this approach fundamentally fails to address the rapidly evolving nature of human societies. The
social conditions during policy deployment often diverge significantly from those when models were
originally formulated, rendering presumed optimal strategies obsolete. Furthermore, social gover-
nance decisions require comprehensive integration of multidimensional factors, and identifying truly
optimal strategies for highly complex societies constitutes a computationally intractable challenge.
The simulation capabilities of the large-scale social simulator developed in this work position it as
a valuable tool for social decision-makers and urban administrators. By configuring diverse initial
states, social agents, and interaction mechanisms, it serves as a high-fidelity platform for policy
outcome evaluation. Leveraging the simulator’s acceleration engine for computational efficiency,
multiple parallel experiments can be deployed to compare the long-term consequences of alternative
decision strategies, thereby enabling data-driven policy selection.
Notably, the simulator enables expansive exploration of decision spaces. Specifically, social man-
agement interventions can incorporate rich combinations of multidimensional policy actions. This
framework not only facilitates the selection of superior strategies through counterfactual simulation-
based parallel experiments but also inspires novel, precise, and composite policy solutions previously
unconsidered in conventional approaches.
9.3.2 Risk control and mitigation for a safer society
The large-scale social simulators can also be used in risk control and mitigation, which represents a
transformative approach to addressing emerging challenges in modern, hyper-connected societies. To
advance societal safety, the large-scale social simulator exhibits substantial advantages across three
critical dimensions:
First, it enables a transition from static analysis to dynamic simulation. Traditional risk models, reliant
on historical data, fail to capture rapidly evolving social dynamics such as emergent public opinion
crises or AI algorithmic failures. By constructing a continuously updated digital twin of society, the
simulator demonstrates sustained predictive capabilities for tracking security risk evolution.
Second, it expands from single-domain to cross-domain risk assessment. Conventional approaches
predominantly focus on isolated domains (e.g., social networks or economic systems), neglecting
interdomain cascading effects. In reality, risks and societal crises often propagate through cascade
effects and exhibit amplification due to cross-domain coupling. The simulator developed in this work
addresses this gap by enabling co-modeling of micro-level agent behaviors across multiple domains,
thereby equipping decision-makers to anticipate and mitigate butterfly-effect crises.
Third, it addresses the oversight of low-probability, high-impact events in long-tail distributions.
Extreme scenarios (such as systemic AI failures all around the world) are frequently dismissed as
statistically negligible despite their catastrophic societal consequences. Our simulator employs Monte
Carlo methods to generate vast ensembles of extreme scenarios, systematically assessing societal
system resilience and informing robust contingency planning.
Therefore, through dynamic, cross-domain, and holistic simulation, the large-scale social simulator
significantly enhances risk identification, control, and mitigation—paving the way for a safer, more
resilient society.
9.3.3 Social simulator for the future human-AI society
Building upon the aforementioned practical applications, we propose a bolder and more open-ended
discussion on the value of large-scale social simulators for next-stage human society.
First, the large-scale social simulator—or its future iterations—could serve as foundational infrastruc-
ture for transitioning toward a digital human society. Currently, these simulators integrate multimodal
data (behavioral logs, social networks) to create initial digital twins of individuals, enabling basic
38

human-like capabilities. Future advancements through the integration of advanced interfaces (e.g.,
neural linkages, emotion-capturing sensors) will unlock richer, more dynamic simulations that mirror
real-world complexity.
Second, the large-scale social simulator functions as a strategic sandbox for exploring future societal
architectures. The morphology and structure of future societies remain enigmatic yet critically
important. For instance, Singapore’s “Virtual City Lab" employs simulations to predict the impact of
sea-level rise on urban functional zones by 2050. Similarly, the simulator could model the coupled
effects of energy, transportation, and housing systems in hyper-dense cities, comparing the resilience
of “vertical megacities" versus “distributed satellite city" paradigms.
Third, in the near future, the coexistence of humans and AI will be common in our society. The large-
scale social simulator developed in this project currently focuses on deploying large language model
agents to simulate human individuals. However, future societies will have more complex issues arising
from varying degrees of AI integration: unemployment curves under different AI adoption rates,
superintelligent AIs’ influence on public decision-making (e.g., AI legislators), societal responses to
the expansion of AI rights such as property ownership, etc.
In short, for future societies, the large-scale social simulator can serve as an indispensable instrument
for understanding societal structures and providing profound insights.
10 Conclusion
In this work, we introduce AgentSociety, a large-scale social generative simulator that integrates
LLM-driven agents, a realistic societal environment, and large-scale interactions, enabling authentic
simulations of human behavior and societal dynamics. By bridging the gap between traditional
agent-based modeling and real-world complexity, it advances generative social science and provides
a powerful tool for analyzing, predicting, and intervening in complex social systems. The successful
replication of real-world social experiments underscores AgentSociety’s authenticity and practicality,
positioning it as both an experimental testbed for social scientists and a practical policy evaluation
platform for policymakers. More broadly, AgentSociety marks a significant advancement in the
evolution of computational social science 2.0, shifting from a tool for static analysis to a dynamic,
interactive platform for exploring complex social systems. Its ability to model and assess the impact
of macro-level policies such as carbon taxes, industry transformation, and social welfare reforms
allows it to provide a low-cost, low-risk environment for testing and refining policy interventions. In
addition, AgentSociety serves as a powerful tool for predicting and mitigating social crises, tracking
the spread of extreme ideologies, and analyzing group polarization, while also testing potential
interventions for crisis management. Looking ahead, AgentSociety holds the promise of becoming a
central platform for exploring the future of human society, where AI and humans coexist. It offers a
space to test innovative governance models, investigate the impact of emerging technologies, and
even redefine legal and ethical frameworks in an AI-driven world.
References
[1] Suhaib Abdurahman, Mohammad Atari, Farzan Karimi-Malekabadi, Mona J Xue, Jackson
Trager, Peter S Park, Preni Golazizian, Ali Omrani, and Morteza Dehghani. Perils and oppor-
tunities in using large language models in psychological research. PNAS nexus, 3(7):pgae245,
2024.
[2] Alberto Acerbi and Joseph M Stubbersfield. Large language models show human-like content
biases in transmission chain experiments. Proceedings of the National Academy of Sciences,
120(44):e2313790120, 2023.
[3] Alma Acevedo. A personalistic appraisal of maslow’s needs theory of motivation: From
“humanistic” psychology to integral humanism. Journal of business ethics , 148:741–763,
2018.
[4] Gati V Aher, Rosa I Arriaga, and Adam Tauman Kalai. Using large language models to
simulate multiple humans and replicate human subject studies. In International Conference on
Machine Learning, pages 337–371. PMLR, 2023.
[5] Icek Ajzen. The theory of planned behavior. Organizational Behavior and Human Decision
Processes, 1991.
39

[6] Altera AL, Andrew Ahn, Nic Becker, Stephanie Carroll, Nico Christie, Manuel Cortes, Arda
Demirci, Melissa Du, Frankie Li, Shuying Luo, et al. Project sid: Many-agent simulations
toward ai civilization. arXiv preprint arXiv:2411.00114, 2024.
[7] Abdulrahman Essa Al Lily, Abdelrahim Fathy Ismail, Fathi M Abunaser, Firass Al-Lami, and
Ali Khalifa Atwa Abdullatif. Chatgpt and the rise of semi-humans. Humanities and Social
Sciences Communications, 10(1):1–12, 2023.
[8] Li An, V olker Grimm, Abigail Sullivan, BL Turner Ii, Nicolas Malleson, Alison Heppenstall,
Christian Vincenot, Derek Robinson, Xinyue Ye, Jianguo Liu, et al. Challenges, tasks, and
opportunities in modeling agent-based complex systems. Ecological Modelling, 457:109685,
2021.
[9] Lisa P Argyle, Ethan C Busby, Nancy Fulda, Joshua R Gubler, Christopher Rytting, and David
Wingate. Out of one, many: Using language models to simulate human samples. Political
Analysis, 31(3):337–351, 2023.
[10] W Brian Arthur. Out-of-equilibrium economics and agent-based modeling. Handbook of
computational economics, 2:1551–1564, 2006.
[11] Ashwini Ashokkumar, Luke Hewitt, Isaias Ghezae, and Robb Willer. Predicting results of
social science experiments using large language models. Work. Pap., New York Univ., New
York, NY, 2024.
[12] Robert L Axtell and J Doyne Farmer. Agent-based modeling in economics and finance: Past,
present, and future. Journal of Economic Literature, pages 1–101, 2022.
[13] Albert Bandura. Human agency in social cognitive theory. American psychologist, 44(9):1175,
1989.
[14] Alexander W Bartik, Elizabeth Rhodes, David E Broockman, Patrick K Krause, Sarah Miller,
and Eva Vivalt. The impact of unconditional cash transfers on consumption and household
balance sheets: Experimental evidence from two us states. Technical report, National Bureau
of Economic Research, 2024.
[15] Fabian Baumann, Philipp Lorenz-Spreen, Igor M Sokolov, and Michele Starnini. Emergence
of polarized ideological opinions in multidimensional topic spaces. Physical Review X ,
11(1):011012, 2021.
[16] Alec T Beall and Jessica L Tracy. Emotivational psychology: How distinct emotions facilitate
fundamental motives. Social and Personality Psychology Compass, 11(2):e12303, 2017.
[17] Michael Behrisch, Laura Bieker, Jakob Erdmann, and Daniel Krajzewicz. Sumo–simulation
of urban mobility: an overview. In Proceedings of SIMUL 2011, The Third International
Conference on Advances in System Simulation. ThinkMind, 2011.
[18] Brian JL Berry, L Douglas Kiel, and Euel Elliott. Adaptive agents, intelligence, and emergent
human organization: Capturing complexity through agent-based modeling. Proceedings of the
National Academy of Sciences, 99(suppl_3):7187–7188, 2002.
[19] Daniil A Boiko, Robert MacKnight, Ben Kline, and Gabe Gomes. Autonomous chemical
research with large language models. Nature, 624(7992):570–578, 2023.
[20] Mathieu Bourgais, Patrick Taillandier, Laurent Vercouter, and Carole Adam. Emotion modeling
in social simulation: a survey. Journal of Artificial Societies and Social Simulation, 2018.
[21] William J Brady, Julian A Wills, John T Jost, Joshua A Tucker, and Jay J Van Bavel. Emotion
shapes the diffusion of moralized content in social networks. Proceedings of the National
Academy of Sciences, 114(28):7313–7318, 2017.
[22] Leo Breiman. Statistical modeling: The two cultures (with comments and a rejoinder by the
author). Statistical science, 16(3):199–231, 2001.
[23] Shu-Heng Chen, Chia-Ling Chang, and Ye-Rong Du. Agent-based economic models and
econometrics. The Knowledge Engineering Review, 27(2):187–219, 2012.
[24] Junyan Cheng and Peter Chin. Sociodojo: Building lifelong analytical agents with real-world
text and time series. In The Twelfth International Conference on Learning Representations,
2024.
40

[25] Lawrence J Christiano, Martin Eichenbaum, and Charles L Evans. Nominal rigidities and the
dynamic effects of a shock to monetary policy. Journal of political Economy, 113(1):1–45,
2005.
[26] John Conway et al. The game of life. Scientific American, 223(4):4, 1970.
[27] Scott De Marchi and Scott E Page. Agent-based models. Annual Review of political science,
17(1):1–20, 2014.
[28] Dorottya Demszky, Diyi Yang, David S Yeager, Christopher J Bryan, Margarett Clapper,
Susannah Chandhok, Johannes C Eichstaedt, Cameron Hecht, Jeremy Jamieson, Meghann
Johnson, et al. Using large language models in psychology. Nature Reviews Psychology,
2(11):688–701, 2023.
[29] Joshua M Epstein. Growing Artificial Societies: Social Science from the Bottom Up . The
Brookings Institution Press, 1996.
[30] Joshua M Epstein. Agent-based computational models and generative social science. Com-
plexity, 4(5):41–60, 1999.
[31] Joshua M Epstein. Generative social science: Studies in agent-based computational modeling.
Princeton University Press, 2012.
[32] Michael W Eysenck and Mark T Keane. Cognitive psychology: A student’s handbook .
Psychology press, 2020.
[33] Jie Feng, Yuwei Du, Jie Zhao, and Yong Li. Agentmove: Predicting human mobility anywhere
using large language model based agentic framework. arXiv preprint arXiv:2408.13986, 2024.
[34] Ling Feng, Baowen Li, Boris Podobnik, Tobias Preis, and H Eugene Stanley. Linking agent-
based models and stochastic models of financial markets.Proceedings of the National Academy
of Sciences, 109(22):8388–8393, 2012.
[35] Shuo Feng, Xintao Yan, Haowei Sun, Yiheng Feng, and Henry X Liu. Intelligent driving
intelligence test for autonomous vehicles with naturalistic and adversarial environment.Nature
communications, 12(1):748, 2021.
[36] Francesco Figari, Emanuela Lezzi, et al. Empirical evidence using microsimulation models in
the social sciences. New Horizons in Modeling and Simulation for Social Epidemiology and
Public Health, pages 107–148, 2021.
[37] Mauro Gallegati and Alan Kirman. Reconstructing economics: Agent based models and
complexity. Complexity Economics, 1(1):5–31, 2012.
[38] Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao Ding, Zhilun Zhou, Fengli Xu, and
Yong Li. Large language models empowered agent-based modeling and simulation: A survey
and perspectives. Humanities and Social Sciences Communications, 11(1):1–24, 2024.
[39] Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao, Jinghua Piao, Huandong Wang, Depeng
Jin, and Yong Li. S3: Social-network simulation system with large language model-empowered
agents. arXiv preprint arXiv:2307.14984, 2023.
[40] Dawei Gao, Zitao Li, Xuchen Pan, Weirui Kuang, Zhijian Ma, Bingchen Qian, Fei Wei,
Wenhao Zhang, Yuexiang Xie, Daoyuan Chen, et al. Agentscope: A flexible yet robust
multi-agent platform. arXiv preprint arXiv:2402.14034, 2024.
[41] Nigel Gilbert and Pietro Terna. How to build and use agent-based models in social science.
Mind & Society, 1:57–72, 2000.
[42] Robert L Goldstone and Marco A Janssen. Computational models of collective behavior.
Trends in cognitive sciences, 9(9):424–430, 2005.
[43] Jing Guo, Nan Li, Jianchuan Qi, Hang Yang, Ruiqiao Li, Yuzhen Feng, Si Zhang, and
Ming Xu. Empowering working memory for large language model agents. arXiv preprint
arXiv:2312.17259, 2023.
[44] Peter Hedström and Petri Ylikoski. Causal mechanisms in the social sciences. Annual review
of sociology, 36(1):49–67, 2010.
[45] Dirk Helbing and Peter Molnar. Social force model for pedestrian dynamics. Physical review
E, 51(5):4282, 1995.
41

[46] Jake M Hofman, Duncan J Watts, Susan Athey, Filiz Garip, Thomas L Griffiths, Jon Kleinberg,
Helen Margetts, Sendhil Mullainathan, Matthew J Salganik, Simine Vazire, et al. Integrating
explanation and prediction in computational social science. Nature, 595(7866):181–188, 2021.
[47] Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili
Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, et al. Metagpt: Meta programming for
multi-agent collaborative framework. arXiv preprint arXiv:2308.00352, 2023.
[48] John J Horton. Large language models as simulated economic agents: What can we learn from
homo silicus? Technical report, National Bureau of Economic Research, 2023.
[49] Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Haotian Wang, Qiang-
long Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, et al. A survey on hallucination in large
language models: Principles, taxonomy, challenges, and open questions. ACM Transactions
on Information Systems, 2023.
[50] Qian Huang, Jian V ora, Percy Liang, and Jure Leskovec. Benchmarking large language models
as ai research agents. In NeurIPS 2023 Foundation Models for Decision Making Workshop,
2023.
[51] Yue Huang, Zhengqing Yuan, Yujun Zhou, Kehan Guo, Xiangqi Wang, Haomin Zhuang,
Weixiang Sun, Lichao Sun, Jindong Wang, Yanfang Ye, et al. Social science meets llms: How
reliable are large language models in social simulations? arXiv preprint arXiv:2410.23426,
2024.
[52] Zexun Jiang, Yafang Shi, Maoxu Li, Hongjiang Xiao, Yunxiao Qin, Qinglan Wei, Ye Wang,
and Yuan Zhang. Casevo: A cognitive agents and social evolution simulator. arXiv preprint
arXiv:2412.19498, 2024.
[53] Hamdi Kavak, Jose J Padilla, Christopher J Lynch, and Saikou Y Diallo. Big data, agents, and
machine learning: towards a data-driven agent-based modeling approach. In Proceedings of
the Annual Simulation Symposium, pages 1–12, 2018.
[54] Arne Kesting, Martin Treiber, and Dirk Helbing. General lane-changing model mobil for
car-following models. Transportation Research Record, 1999(1):86–94, 2007.
[55] Michal Kosinski. Evaluating large language models in theory of mind tasks. Proceedings of
the National Academy of Sciences, 121(45):e2405460121, 2024.
[56] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu,
Joseph Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large
language model serving with pagedattention. In Proceedings of the 29th Symposium on
Operating Systems Principles, pages 611–626, 2023.
[57] James Ladyman, James Lambert, and Karoline Wiesner. What is a complex system? European
Journal for Philosophy of Science, 3:33–67, 2013.
[58] Shiyang Lai, Yujin Potter, Junsol Kim, Richard Zhuang, Dawn Song, and James Evans.
Evolving ai collectives to enhance human diversity and enable self-regulation. arXiv preprint
arXiv:2402.12590, 2024.
[59] Andrew K Lampinen, Ishita Dasgupta, Stephanie CY Chan, Hannah R Sheahan, Antonia
Creswell, Dharshan Kumaran, James L McClelland, and Felix Hill. Language models, like
humans, show content effects on reasoning tasks. PNAS nexus, 3(7):pgae233, 2024.
[60] Michael Laver and Ernest Sergenti. Party competition: An agent-based model, volume 20.
Princeton University Press, 2011.
[61] David Lazer, Alex Pentland, Lada Adamic, Sinan Aral, Albert-László Barabási, Devon Brewer,
Nicholas Christakis, Noshir Contractor, James Fowler, Myron Gutmann, et al. Computational
social science. Science, 323(5915):721–723, 2009.
[62] David MJ Lazer, Alex Pentland, Duncan J Watts, Sinan Aral, Susan Athey, Noshir Contractor,
Deen Freelon, Sandra Gonzalez-Bailon, Gary King, Helen Margetts, et al. Computational
social science: Obstacles and opportunities. Science, 369(6507):1060–1062, 2020.
[63] Guohao Li, Hasan Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard Ghanem. Camel:
Communicative agents for" mind" exploration of large language model society. Advances in
Neural Information Processing Systems, 36:51991–52008, 2023.
42

[64] Nian Li, Chen Gao, Mingyu Li, Yong Li, and Qingmin Liao. Econagent: large language
model-empowered agents for simulating macroeconomic activities. In Proceedings of the 62nd
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pages 15523–15536, 2024.
[65] Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang Zhao,
Chengqi Deng, Chenyu Zhang, Chong Ruan, et al. Deepseek-v3 technical report. arXiv
preprint arXiv:2412.19437, 2024.
[66] Ruibo Liu, Ruixin Yang, Chenyan Jia, Ge Zhang, Denny Zhou, Andrew M Dai, Diyi Yang, and
Soroush V osoughi. Training socially aligned language models on simulated social interactions.
arXiv preprint arXiv:2305.16960, 2023.
[67] Charles M Macal and Michael J North. Tutorial on agent-based modeling and simulation. In
Proceedings of the Winter Simulation Conference, 2005., pages 14–pp. IEEE, 2005.
[68] AH Maslow. A theory of human motivation. Psychological Review, 2:21–28, 1943.
[69] Saul McLeod. Maslow’s hierarchy of needs. Simply psychology, 1(1-18), 2007.
[70] George Herbert Mead. Mind, self, and society from the standpoint of a social behaviorist.
Chicago, 1934.
[71] Philipp Moritz, Robert Nishihara, Stephanie Wang, Alexey Tumanov, Richard Liaw, Eric
Liang, Melih Elibol, Zongheng Yang, William Paul, Michael I Jordan, et al. Ray: A distributed
framework for emerging {AI} applications. In 13th USENIX symposium on operating systems
design and implementation (OSDI 18), pages 561–577, 2018.
[72] Xinyi Mou, Zhongyu Wei, and Xuanjing Huang. Unveiling the truth and facilitating change: To-
wards agent-based large-scale social movement simulation. arXiv preprint arXiv:2402.16333,
2024.
[73] Akira Namatame and Shu-Heng Chen. Agent-based modeling and network dynamics. Oxford
University Press, 2016.
[74] Graziella Orrù, Andrea Piarulli, Ciro Conversano, and Angelo Gemignani. Human-like
problem-solving abilities in large language models using chatgpt. Frontiers in artificial
intelligence, 6:1199350, 2023.
[75] Xianghe Pang, Shuo Tang, Rui Ye, Yuxin Xiong, Bolun Zhang, Yanfeng Wang, and Si-
heng Chen. Self-alignment of large language models via monopolylogue-based social scene
simulation. In Forty-first International Conference on Machine Learning, 2024.
[76] Xianghe Pang, Shuo Tang, Rui Ye, Yuxin Xiong, Bolun Zhang, Yanfeng Wang, and Siheng
Chen. Self-alignment of large language models via multi-agent social simulation. In ICLR
2024 Workshop on Large Language Model (LLM) Agents, 2024.
[77] Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang,
and Michael S Bernstein. Generative agents: Interactive simulacra of human behavior. In
Proceedings of the 36th annual acm symposium on user interface software and technology,
pages 1–22, 2023.
[78] Joon Sung Park, Carolyn Q Zou, Aaron Shaw, Benjamin Mako Hill, Carrie Cai, Mered-
ith Ringel Morris, Robb Willer, Percy Liang, and Michael S Bernstein. Generative agent
simulations of 1,000 people. arXiv preprint arXiv:2411.10109, 2024.
[79] Jinghua Piao, Jiazhen Liu, Fang Zhang, Jun Su, and Yong Li. Human–ai adaptive dynamics
drives the emergence of information cocoons. Nature Machine Intelligence, 5(11):1214–1224,
2023.
[80] Jinghua Piao, Zhihong Lu, Chen Gao, Fengli Xu, Fernando P Santos, Yong Li, and James
Evans. Emergence of human-like polarization among large language model agents. arXiv
preprint arXiv:2501.05171, 2025.
[81] David V Pynadath, Mei Si, and Stacy C Marsella. Modeling theory of mind and cognitive
appraisal with decision-theoretic agents. Social emotions in nature and artifact: emotions in
human and human-computer interaction, pages 70–87, 2011.
[82] Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize
Chen, Yusheng Su, Xin Cong, et al. Chatdev: Communicative agents for software development.
In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 15174–15186, 2024.
43

[83] Lenore Sawyer Radloff. The use of the center for epidemiologic studies depression scale in
adolescents and young adults. Journal of youth and adolescence, 20(2):149–166, 1991.
[84] Daniel M Romero, Brendan Meeder, and Jon Kleinberg. Differences in the mechanics of
information diffusion across topics: idioms, political hashtags, and complex contagion on
twitter. In Proceedings of the 20th international conference on World wide web, pages 695–704,
2011.
[85] Jingqing Ruan, Yihong Chen, Bin Zhang, Zhiwei Xu, Tianpeng Bao, Hangyu Mao, Ziyue
Li, Xingyu Zeng, Rui Zhao, et al. Tptu: Task planning and tool usage of large language
model-based ai agents. In NeurIPS 2023 Foundation Models for Decision Making Workshop,
2023.
[86] Marko Sarstedt, Susanne J Adler, Lea Rau, and Bernd Schmitt. Using large language models
to generate silicon samples in consumer and marketing research: Challenges, opportunities,
and guidelines. Psychology & Marketing, 41(6):1254–1270, 2024.
[87] RK Sawyer. Social Emergence: Societies as Complex Systems. Cambridge University Press,
2005.
[88] Tim Schürmann and Philipp Beckerle. Personalizing human-agent interaction through cognitive
models. Frontiers in Psychology, 11:561510, 2020.
[89] Chenyang Shao, Fengli Xu, Bingbing Fan, Jingtao Ding, Yuan Yuan, Meng Wang, and Yong
Li. Beyond imitation: Generating human mobility from context-aware reasoning with large
language models. arXiv preprint arXiv:2402.09836, 2024.
[90] Maayan Shvo, Jakob Buhmann, and Mubbasir Kapadia. An interdependent model of personal-
ity, motivation, emotion, and mood for intelligent virtual agents. In Proceedings of the 19th
ACM international conference on intelligent virtual agents, pages 65–72, 2019.
[91] Didier Sornette. Why stock markets crash: critical events in complex financial systems .
Princeton university press, 2009.
[92] James WA Strachan, Dalila Albergo, Giulia Borghini, Oriana Pansardi, Eugenio Scaliti,
Saurabh Gupta, Krati Saxena, Alessandro Rufo, Stefano Panzeri, Guido Manzi, et al. Testing
theory of mind in large language models and humans. Nature Human Behaviour, pages 1–11,
2024.
[93] Seungjong Sun, Eungu Lee, Dongyan Nan, Xiangying Zhao, Wonbyung Lee, Bernard J Jansen,
and Jang Hyun Kim. Random silicon sampling: Simulating human sub-population opinion
using a large language model based on group-level demographic information. arXiv preprint
arXiv:2402.18144, 2024.
[94] Jiakai Tang, Heyang Gao, Xuchen Pan, Lei Wang, Haoran Tan, Dawei Gao, Yushuo Chen,
Xu Chen, Yankai Lin, Yaliang Li, et al. Gensim: A general social simulation platform with
large language model based agents. arXiv preprint arXiv:2410.04360, 2024.
[95] Martin Treiber, Ansgar Hennecke, and Dirk Helbing. Congested traffic states in empirical
observations and microscopic simulations. Physical review E, 62(2):1805, 2000.
[96] Klaus G Troitzsch. Social science microsimulation. Springer Science & Business Media,
1996.
[97] Sander van der Hoog. Deep learning in (and of) agent-based models: A prospectus. arXiv
preprint arXiv:1706.06302, 2017.
[98] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi
Fan, and Anima Anandkumar. V oyager: An open-ended embodied agent with large language
models. arXiv preprint arXiv:2305.16291, 2023.
[99] Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen,
Jiakai Tang, Xu Chen, Yankai Lin, et al. A survey on large language model based autonomous
agents. Frontiers of Computer Science, 18(6):186345, 2024.
[100] Lei Wang, Jingsen Zhang, Hao Yang, Zhi-Yuan Chen, Jiakai Tang, Zeyu Zhang, Xu Chen,
Yankai Lin, Hao Sun, Ruihua Song, et al. User behavior simulation with large language
model-based agents for recommender systems. ACM Transactions on Information Systems,
2024.
44

[101] Yiding Wang, Yuxuan Chen, Fangwei Zhong, Long Ma, and Yizhou Wang. Simulating
human-like daily activities with desire-driven autonomy. arXiv preprint arXiv:2412.06435,
2024.
[102] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le,
Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models.
Advances in neural information processing systems, 35:24824–24837, 2022.
[103] U Wilensky. An Introduction to Agent-Based Modeling: Modeling Natural, Social, and
Engineered Complex Systems with Netlogo. The MIT Press, 2015.
[104] Sarah Wolf, Steffen Fürst, Antoine Mandel, Wiebke Lass, Daniel Lincke, Federico Pablo-Marti,
and Carlo Jaeger. A multi-agent model of several economic regions. Environmental modelling
& software, 44:25–43, 2013.
[105] Stephen Wolfram. Cellular automata. Los Alamos Science, pages 09–01, 1983.
[106] Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang,
Junzhe Wang, Senjie Jin, Enyu Zhou, et al. The rise and potential of large language model
based agents: A survey. arXiv preprint arXiv:2309.07864, 2023.
[107] Yuzhuang Xu, Shuo Wang, Peng Li, Fuwen Luo, Xiaolong Wang, Weidong Liu, and Yang Liu.
Exploring large language models for communication games: An empirical study on werewolf.
arXiv preprint arXiv:2309.04658, 2023.
[108] Yuwei Yan, Qingbin Zeng, Zhiheng Zheng, Jingzhe Yuan, Jie Feng, Jun Zhang, Fengli Xu, and
Yong Li. Opencity: A scalable platform to simulate urban activities with massive llm agents.
arXiv preprint arXiv:2410.21286, 2024.
[109] Ziyi Yang, Zaibin Zhang, Zirui Zheng, Yuxian Jiang, Ziyue Gan, Zhiyu Wang, Zijian Ling,
Jinsong Chen, Martz Ma, Bowen Dong, et al. Oasis: Open agents social interaction simulations
on one million agents. arXiv preprint arXiv:2411.11581, 2024.
[110] An Zhang, Yuxin Chen, Leheng Sheng, Xiang Wang, and Tat-Seng Chua. On generative
agents in recommendation. In Proceedings of the 47th international ACM SIGIR conference
on research and development in Information Retrieval, pages 1807–1817, 2024.
[111] Chaoyun Zhang, Shilin He, Jiaxu Qian, Bowen Li, Liqun Li, Si Qin, Yu Kang, Minghua Ma,
Qingwei Lin, Saravan Rajmohan, et al. Large language model-brained gui agents: A survey.
arXiv preprint arXiv:2411.18279, 2024.
[112] Huichu Zhang, Siyuan Feng, Chang Liu, Yaoyao Ding, Yichen Zhu, Zihan Zhou, Weinan
Zhang, Yong Yu, Haiming Jin, and Zhenhui Li. Cityflow: A multi-agent reinforcement learning
environment for large scale city traffic scenario. In The world wide web conference, pages
3620–3624, 2019.
[113] Xinnong Zhang, Jiayu Lin, Libo Sun, Weihong Qi, Yihang Yang, Yue Chen, Hanjia Lyu, Xinyi
Mou, Siming Chen, Jiebo Luo, et al. Electionsim: Massive population election simulation
powered by large language model driven agents. arXiv preprint arXiv:2410.20746, 2024.
[114] Zeyu Zhang, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Quanyu Dai, Jieming Zhu, Zhenhua
Dong, and Ji-Rong Wen. A survey on the memory mechanism of large language model based
agents. arXiv preprint arXiv:2404.13501, 2024.
[115] Stephan Zheng, Alexander Trott, Sunil Srinivasa, David C Parkes, and Richard Socher. The
ai economist: Taxation policy design via two-level deep multiagent reinforcement learning.
Science advances, 8(18):eabk2607, 2022.
[116] Xuhui Zhou, Hao Zhu, Leena Mathur, Ruohong Zhang, Haofei Yu, Zhengyang Qi, Louis-
Philippe Morency, Yonatan Bisk, Daniel Fried, Graham Neubig, et al. Sotopia: Interactive
evaluation for social intelligence in language agents. arXiv preprint arXiv:2310.11667, 2023.
[117] Xizhou Zhu, Yuntao Chen, Hao Tian, Chenxin Tao, Weijie Su, Chenyu Yang, Gao Huang, Bin
Li, Lewei Lu, Xiaogang Wang, et al. Ghost in the minecraft: Generally capable agents for
open-world environments via large language models with text-based knowledge and memory.
arXiv preprint arXiv:2305.17144, 2023.
[118] George Kingsley Zipf. The p 1 p 2/d hypothesis: on the intercity movement of persons.
American sociological review, 11(6):677–686, 1946.
45
