# 05_Mou2024_Social_Simulation_LLM_Agents_Survey

Source PDF: `/Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/review_library/05_Mou2024_Social_Simulation_LLM_Agents_Survey.pdf`

Extraction backend: `PyMuPDF`

## Page 1

From Individual to Society: A Survey on Social Simulation Driven by Large
Language Model-based Agents
Xinyi Mou1∗, Xuanwen Ding2∗, Qi He1∗, Liang Wang3∗,
Jingcong Liang1 , Xinnong Zhang1 , Libo Sun1 , Jiayu Lin1 ,
Jie Zhou2 , Xuanjing Huang1 and Zhongyu Wei1,4†
1Fudan University
2East China Normal University
3Harbin Institute of Technology, Shenzhen
4Shanghai Innovation Institute
zywei@fudan.edu.cn
Abstract
Traditional sociological research often relies on hu-
man participation, which, though effective, is ex-
pensive, challenging to scale, and with ethical con-
cerns.
Recent advancements in large language
models (LLMs) highlight their potential to simu-
late human behavior, enabling the replication of in-
dividual responses and facilitating studies on many
interdisciplinary studies.
In this paper, we con-
duct a comprehensive survey of this field, illus-
trating the recent progress in simulation driven by
LLM-empowered agents. We categorize the sim-
ulations into three types: (1) Individual Simula-
tion, which mimics specific individuals or demo-
graphic groups; (2) Scenario Simulation, where
multiple agents collaborate to achieve goals within
specific contexts; and (3) Society Simulation, which
models interactions within agent societies to re-
flect the complexity and variety of real-world dy-
namics. These simulations follow a progression,
ranging from detailed individual modeling to large-
scale societal phenomena. We provide a detailed
discussion of each simulation type, including the
architecture or key components of the simulation,
the classification of objectives or scenarios and the
evaluation method. Afterward, we summarize com-
monly used datasets and benchmarks. Finally, we
discuss the trends across these three types of sim-
ulation. A repository for the related sources is at
https://github.com/FudanDISC/SocialAgent.
1
Introduction
Social science investigates human behavior and social struc-
tures to understand how societies function. Traditional so-
ciological research heavily relies on human participation to
conduct experiments and gather data. Questionnaires [1, 2]
and psychological experiments [3, 4] are commonly used
∗These authors contributed equally.
†Corresponding author.
to test theoretical hypotheses, understand social phenomena,
and predict collective outcomes. While these methods can
provide highly authentic data, they are expensive, challeng-
ing to scale, and involve certain ethical risks.
Recently, large language models (LLMs) have demon-
strated impressive capabilities in human-level reasoning and
planning [5–9]. They can perceive the environment, make
decisions, and take corresponding actions, showcasing their
potential as autonomous agents that can serve as human sub-
stitutes. In appropriate settings, LLM-driven agents can ac-
curately simulate responses from corresponding individuals
by leveraging their role-playing abilities [10, 11], a property
known as algorithmic fidelity [12, 13]. This characteristic
makes LLM-driven agents highly valuable in simulating hu-
man behavior. By reproducing individual response patterns
in specific scenarios, LLM-driven agents help researchers to
better understand, validate, and predict human reactions.
Just as individuals do not exist independently within so-
ciety, in addition to separate individual agents, interactions
between multiple agents have also been widely studied to
solve specific problems or simulate complex dynamics in the
real world [14, 15].
On one hand, LLMs can be special-
ized as agents with detailed knowledge and skills, leverag-
ing collective intelligence to solve complex problems, such as
software development [16, 17], automatic diagnosis [18, 19]
and judicial decision-making [20]. In this case, multiple au-
tonomous agents collaborate on planning, discussion, and
decision-making, reflecting the cooperative nature of human
groups when solving problems. On the other hand, simple in-
teractions between multiple agents can lead to the emergence
of complex collective behaviors or patterns [21–23], thereby
replicating complex social dynamics in the real world, such
as opinion dynamics [24–26] and macroeconomics phenom-
ena [27]. Such simulations provide valuable tools for under-
standing, analyzing, and predicting complex phenomena that
may be difficult or impractical to observe directly in real life,
offering strong support for decision-making in areas such as
policy-making and social management.
This research field is rapidly expanding, with papers focus-
ing on various aspects. Considering the purpose of simulation
and the varying demands for diversity, scale, and accuracy
arXiv:2412.03563v1  [cs.CL]  4 Dec 2024

## Page 2

Individual Simulation
Name: David
Gender: Male
Age: 29
Race: White
Occupation: Engineer
…
Profile
Memory
Planning
Action
Environment
Sharing
Opinions
Epidemic
Modeling
Finishing a
Morning Routine
Scenario Simulation
Society Simulation
Composition
Network
Social Influence
Outcomes
Demand for Precision of Individual Simulation
Demand for Diversification and Scale of Individual Simulation
Role
Organization
Communication
Figure 1: Illustration of simulations empowered by LLM-driven agents. We categorize the simulations into individual simulation, scenario
simulation and society simulation. From left to right, the diversity and scale of individual modeling generally increase. Conversely, from
right to left, the granularity of individual modeling becomes more refined.
in individual modeling, we categorize the existing work into
three types, as illustrated in Figure 1:
1. Individual Simulation: leveraging LLM-based agents
to mimic specific individuals or groups of people sharing
common demographic characteristics [10, 11, 28]. This
line of research focuses on the replication of features of
a single person, e.g., personality, and has not involved
multi-agent interactions.
2. Scenario Simulation: organizing a group of agents in a
concentrated scenario, driven by specific goals or tasks,
such as software development [16, 17], question answer-
ing [29] and paper reviewing [30].
Such simulations
are usually focused on small-scale agents within specific
scenarios, emphasizing the collective wisdom of agents
with specialized expertise.
3. Society Simulation: simulating more complex and di-
verse behaviors in the agent society to explore so-
cial dynamics in real-world applications. Such simu-
lations could test social science theories within a small
scope [31] or populate virtual spaces and communities
with large-scale realistic social phenomena [32, 33]. The
composition of individuals in such simulations is more
complex and diverse.
These three types of simulations exhibit a progressive rela-
tionship. Individual simulation models a specific person or a
type of person, serving as the foundation for scenario simula-
tion and society simulation. Theoretically, society simulation
can encompass a chaotic world composed of countless sub-
scenarios, though current work focuses on specific scenarios.
Although this field has seen rapid growth, with some sur-
veys summarizing agent architectures [7, 9, 15] or certain as-
pects of single-agent ability or multi-agent systems [11, 14,
34], there is an absence of a systematic review to summarize
the work from the individual to society, providing a compre-
hensive blueprint for this field. This motivates us to present
this survey, aiming to contribute to the research and devel-
opment of simulations driven by LLM-based agents, as well
as a wider range of interdisciplinary studies. To comprehen-
sively describe our landscape, we organize our survey as fol-
lows. After a brief introduction to the background in § 2,
we begin in § 3 by detailing how to conduct individual sim-
ulation through discussions of (1) the architecture of a single
agent, (2) construction method of individual simulation, (3)
the classification of objectives, and (4) the evaluation of indi-
vidual simulation. Next, in § 4, we summarize scenario sim-
ulation, including (1) the elements that constitute a scenario
simulation system, (2) the classification of scenarios, and (3)
the evaluation of scenario simulation, exploring how multiple
agents collaborate to achieve objectives within a single sce-
nario. Following this, in § 5, we introduce society simulation,
examining how multi-agent systems can construct complex
social dynamics through (1) the social construction elements
of society simulation, (2) the classification of society simula-
tion scenarios, and (3) the evaluation of society simulation. In
§ 6, we summarize existing datasets and benchmarks. Based
on the earlier sections, we analyze trends in these three as-
pects in § 7 and present the conclusion in § 8.

## Page 3

Construction
Prompting
Training
Architecture
Profile
Memory
Planning
Action
Objective
Characters
Demographics
Evaluation
Static
Interactive
Subjective
Objective
Level
Strategy
Support
Construction
Form
manual, LLM generation
descriptions, conversaions
Type
Operation
short-term, long-term
writing, retrieval, reflection
Type
empathetic planning
Situation
Domain
dialogue, cafted situation
closed, open domain
Pre-training
Finetuning
Reinforcement learning
Prompt engineering
“You are an expert…”
“You are a helpful assistant…”
Integrate
Virtual
Real
subjective planning
Evaluate
Figure 2: Illustration of individual simulation blueprint. An individual agent is typically composed of an architecture with modules involving
profile, memory, planning, and action through construction method, prompting or training, to simulate specific objectives like characters or
demographics . Individual simulation can be evaluated statically and interactively with different dimensions being observed.
2
Background
2.1
Large Language Model-based Agents
Benefiting from the large-scale parameters and pre-training
on vast amounts of data, the recently emerging large language
models have shown great potential in achieving human-like
intelligence [6, 35, 36]. This has sparked a rise in the research
of LLM-empowered agents, where the key idea is to equip
the LLMs with human capabilities such as memory [37, 38],
planning [39, 40] and tool usage [41, 42]. The memory mod-
ule enables agents to store and operate historical informa-
tion to facilitate future actions. Memory of different struc-
tures [32, 43] and formats [44, 45] have been integrated into
LLM-based agents. The planning module helps agents to de-
compose complex tasks into subtasks, where various planning
strategies [5, 39] are adopted. The tool-usage module allows
agents to make use of external tools or resources [39, 46] to
solve tasks. Overall, these modules assist agents in operating
more effectively in complex and diverse environments.
2.2
Multi-agent Systems
To realize complex scenarios, a single agent is never enough.
A system where interaction between multiple agents is in-
volved is referred to as a multi-agent system (MAS). The
agents may have a common goal, such as working together
to accomplish a task [16, 17] or solve a problem [29], or
they may just have self-interested goals that can cause them to
compete for limited resources [47]. In a multi-agent system,
each agent may be assigned distinct roles and skills, as well
as distinct tasks. These agents can be organized in various
ways, such as layered or centralized structures [48–50], and
can communicate through different methods [51–53]. These
factors significantly influence the effectiveness and efficiency
of multi-agent interactions.
3
Individual Simulation
Individual simulation focuses on designing a modular ar-
chitecture that integrates individualized data for the construc-
tion of agents and simulating the specific objective with high
fidelity. In this section, we first outline the basic architecture
of the agent in the individual simulation with four key compo-
nents in §3.1. Then, two construction methods are discussed
in §3.2 to implement the integration of individualized data
into objectives introduced in §3.3. The evaluation methods
are examined from different perspectives in §3.4. The overall
framework is presented in Figure 2 and representative works
are summarized in Table 1.
3.1
Architecture
To effectively accomplish individual simulation, it is essential
to construct an agent architecture that can accurately repli-
cate the features of the individual. This requires a balance
between theoretical abstraction and practical implementation
to capture the complexity of human behaviors. Typically, this
architecture is modularized into four core components: pro-
file, memory, planning, and action.

## Page 4

Objectives
Paper
Aritecture
Construtction
Profile
Memory
Planning
Action Domain
Characters
Brahman et al. [54]
Dialogue/Description
Short-term
-
Open/Closed
Parametric
Chen et al. [55]
Dialogue/Description
Short-term
-
Open
Parametric /Non-
parametric
Schwitzgebel et al. [56]
Dialogue
Short-term
-
Open
Parametric
Generative Agents [57]
Description
Short/Long-term
-
Open
Nonparametric
Agrawal et al. [58]
Dialogue/Description
Short-term
-
Open
Parametric
ChatHaruhi [59]
Dialogue
Short-term
-
Open
Parametric
LiveChat [60]
Dialogue/Description Short/Long-term
-
Open/Closed
Parametric
RoleLLM [28]
Description/Dialogue
Short-term
-
Open/Closed
Parametric
CharacterLLM [10]
Description
Short-term
Subjective
Open
Parametric
InCharacter [61]
-
Short-term
-
Open/Closed
-
CharacterGLM [62]
Description/Dialogue
Short-term
-
Open
Parametric
RoleEval [63]
Description
Short-term
-
Closed
Parametric
CharacterEval [64]
Dialogue
Short-term
-
Open
Nonparametric
Neeko [65]
Description
Short-term
-
Open
Parametric
Character is Destiny [66]
Description
Short/Long-term
-
Closed
Nonparametric
Yuan et al. [67]
Description
Short-term
-
Open/Closed
Nonparametric
Capturing Minds [68]
Description/Dialogue Short/Long-term
Subjective
Open/Closed
Parametric
MMRole [69]
Description
Short-term
-
Open
Parametric
Yu et al. [70]
Dialogue
Short-term
-
Open
Parametric
Rational sensibility [71]
-
Short-term
Empathetic
Closed
Parametric
Demographics
Karra et al.[72]
Dialogue/Description
Short-term
-
Closed
Parametric
Jiang et al. [73]
Description
Short-term
-
Closed
Nonparametric
Liu et al. [74]
Description
Short/Long-term
-
Open
Parametric
Out of One, Many [12]
Description
Short-term
-
Open
Nonparametric
Simulated Economic
Agents [75]
Description
Short-term
-
Closed
Nonparametric
The wall street neophyte
[76]
Description
Short-term
Empathetic
Closed
Nonparametric
Toxicity in ChatGPT [77]
Description
Short-term
-
Open
Nonparametric
Song et al. [78]
Description
Short-term
-
Closed
Nonparametric
Marked Personas [79]
Description
Short-term
-
Open
Nonparametric
Wang et al. [80]
Description
Short/Long-term
-
Open
Nonparametric
Serapio-Garc´ıa et al. [81]
Description
Short-term
-
Open
Nonparametric
Huang et al. [82]
Description
Short-term
-
Closed
Nonparametric
CharacterChat [83]
Description
Short/Long-term
-
Open
Nonparametric
Conversational health
agents [84]
Description
Short/Long-term Empathetic
Open
Nonparametric
Chen et al. [85]
Description
Short/Long-term
-
Closed
Nonparametric
EconAgent [86]
Description
Short/Long-term
-
Open
Nonparamaetric
Shea et al. [87]
Dialogue
Short-term
-
Open
Parametric
Be Selfish, But Wisely [88]
Dialogue
Short-term
-
Open
Parametric
Chain of Empathy [89]
-
Short-term
Empathetic
Open
Nonparametric
Bias Runs Deep [90]
Description
Short-term
-
Open
Nonparametric
Li et al. [91]
Dialogue
Short-term
-
Open
Parametric
Xie et al. [92]
Description
Short-term
Subjective
Closed
Nonparametric
Lee et al. [93]
Description
Short-term
-
Closed
Nonparametric
CultureLLM [94]
Dialogue
Short-term
-
Open
Parametric
ControlLM [95]
-
Short/Long-term
-
Open
Nonparamatric
Random Silicon Sampling
[96]
Description
Short-term
-
Closed
Nonparametric
Bisbee et al. [97]
Description
Short-term
-
Closed
Nonparametric
PersonaHub [98]
Description
Short-term
-
Open
Parametric
Qu et al. [99]
Description
Short-term
-
Closed
Nonparametric
Interactive Agents [100]
Description
Short-term
-
Open
Nonparametric
Table 1: A list of representative works of individual simulation.

## Page 5

3.1.1
Profile
Profile differentiates the unique characteristics of simulated
individuals, encompassing attributes, behaviors, and con-
straints. The profiles differ in the ways of construction and
their forms.
Profile Construction
Profile construction refers to the pro-
cess of collecting individual-related information, which can
be categorized into manual modification and LLM generation.
Manual modification takes advantage of publicly available
data to create high-quality profiles through a human-guided
process. According to the collected sources, manual mod-
ification can also be classified into three categories: hand-
crafting, online communities, and historical works. Hand-
crafting manually organized some coarse strength informa-
tion, such as well-known characters [101] and specific per-
sonalities [77, 79], while online communities construct pro-
files built on the web data like Wikipedia [10] and social
media [60], where the profile implicitly exists in conversa-
tions and materials. In addition, literary works serve as addi-
tional descriptions that reflect the author’s thoughts [56] and
characters in the storyline [54, 59]. LLM generation auto-
matically generates the expected persona-based information
profiles by prompting LLMs with essential individual de-
tails [28, 61, 83]. This method explores diverse profiles with
ease, while the quality needs human supervision with caution.
Profile Form
Profile form defines the format of individual
information, which can be categorized into descriptions and
conversations. Descriptions directly describe basic individual
information or identity with details like name, age, and gen-
der [101, 102]. While descriptions can intuitively reflect the
basic attributes of an individual, deeper contextual informa-
tion can also be ignored. On the contrary, conversations im-
plicitly reflect the character profile through dialogue. A sub-
stantial amount of conversational data is derived from sources
such as films, literary works, and scripts [54, 70, 103, 104].
Considering the extensive commonsense knowledge learned
by LLMs in the pre-training stage, recent works leverage
LLMs to generate individual dialogues [59, 98], which de-
fines the artistic genre through six essential elements to gen-
erate detailed drama scripts [105] and imitates speaking styles
through context learning [28, 65].
3.1.2
Memory
Memory is designed to store perceived or generated informa-
tion, helping agents maintain consistency and continuity of
behavior and overcome the limited context window of LLMs.
Considering the complexity of memory, researchers struggle
to design more efficient memory types and operations.
Memory Type
Based on the temporal span of stored
content,
memory can be commonly divided into two
types, namely short-term memory and long-term mem-
ory.
Short-term memory records the instant local infor-
mation that the agent perceives, which can be further di-
vided into simulation contents and simulation supplements.
Simulation contents include essential interaction data like
user instructions [56, 77], dialogue history [106, 107],
and user/environment responses [76].
Simulation supple-
ments provide additional environmental information includ-
ing scene descriptions [58, 76] and scene-related experi-
ences [10, 66], which navigate agents through the simula-
tion to perform tasks appropriately. Long-term memory stores
persistent global information, preventing deviations from in-
tended goals, which holds extensive individual-specific in-
formation stably, including past experiences and behaviors,
current knowledge, and skills [66, 86]. With the proposal of
using the vector database as the long-term memory hub, the
management, retrieval, and organization of memory is more
effective [108].
Memory Operation
Memory operations stand for the con-
tinuous updating and utilization of memory by the agent.
The common memory operations include three types, namely
memory writing, memory retrieval, and memory reflection.
Memory writing aims to incorporate the relevant historical
content into the memory. This process mirrors human mem-
ory formation, where useful information is retained for future
retrieval. The memories to be written vary from user-specific
dialogue history [103], new skills [109], to selected papers
and other forms [110].
Memory retrieval serves to extract valuable content from
memory based on customized requirements. The overall per-
formance of the individual simulation highly relies on the
effectiveness of memory retrieval since simulations are sen-
sitive to the context. Traditional retrieval technologies rely
on similarity such as keyword matching [111] and embed-
ding vectors [108], while recent works introduce the retrieval
model to select the most relevant information [112, 113].
Memory reflection mirrors the human ability to recon-
sider past behaviors and opinions. Specifically, it helps the
agent to organize, refine, and elevate memories into more ab-
stract and insightful concepts. Generative Agents [57] main-
tains a comprehensive record of agents’ experiences with a
tree-structured reflection process to optimize memory usage.
ProAgent [114] incorporates memory reflection with valida-
tion and belief correction to improve the agent’s planning and
decision-making. Voyager [109] allows agents to reflect on
their behavior and update their skill libraries through self-
verification. Although the application scenarios of memory
reflection are still limited, it shows great improvement in en-
hancing performance and increasing the depth of simulations,
especially in complex environments.
3.1.3
Planning
Planning is the process of deciding on a series of actions
aimed at achieving specific goals. Traditional planning tasks
typically focus on solving particular problems, such as mathe-
matical reasoning [115] or embodied tasks [116, 117]. At the
individual simulation level, however, agents are expected to
go beyond mere problem-solving. They should also be able to
simulate personalized thinking and emotional responses dur-
ing interactions with specific individuals. This extends plan-
ning into two additional categories: empathetic planning and
subjective planning.
Empathetic planning
Empathetic planning refers to an
agent’s ability to infer and perceive the behavior and emo-
tions of others before taking action. It involves using Chain-
of-Thought (CoT) reasoning to understand the situations of
others and make adaptive decisions or judgments [71, 76, 89].

## Page 6

This allows the agent to tailor its actions based on the emo-
tional and behavioral context, guiding the acquisition of per-
sonalized feedback.
Subjective planning
Subjective planning refers to the ac-
tions an agent takes based on its own thoughts and feelings,
in line with its predefined role or identity. This can involve
utilizing inner monologues from simulated characters to fine-
tune LLMs [10, 68] or using CoT to guide LLMs to express
themselves according to their own beliefs [92]. This form of
planning is driven by the agent’s internal state, rather than by
external stimuli or the needs of others.
3.1.4
Action
Action refers to the direct interaction between LLMs and their
environment. Action encompasses two key aspects: the ac-
tion situation, which describes the context in which actions
occur, and the action domain, which defines the requirements
for action space. Action serves as the interface for simulating
human behavior, allowing LLMs to execute tasks that mimic
real-world actions and responses. This interaction enables a
deeper understanding of human-like decision-making and ex-
ecution in various scenarios.
Action Situation
With individual simulations focusing on
more and more diverse and complicated situations, various
action situations spring out accordingly, ranging from dia-
logue [118], games [119], real word [106], etc. Typically,
action situations can be divided into simple dialogues and
crafted situations.
Simple dialogues are few-turn conversations without re-
stricted environments, such as constructing dialogues be-
tween two characters [54].
Recent researches utilize sim-
ple dialogues to induce potential attributes within the models,
involving personality [72, 73], traits [81] and toxicity [77].
Other works conduct evaluations of persona with interview-
ing [61] or questionnaire [120] with simple dialogues to fa-
cilitate their experiment.
Crafted situations are elaborately designed environments
including detailed rules and surrounding descriptions. Com-
mon situations like games are modified from simple dia-
logues. They leverage game rules to provide a settled vir-
tual topic for both users and agents to play in, especially in
the board role-playing games [119, 119] [121]. Besides, re-
searchers have developed a more delicate environment called
sandbox [111], which not only includes rules but establish an
objective environment. To further enrich the individual simu-
lation situation, some authors add some elements existing in
scripts like facial expression, tiny movements [58, 105], and
nuanced information from environment images [69].
Action Domain
The Action domain can be commonly di-
vided into close domain and open domain based on the re-
striction of action space.
Closed domain simulation occurs when the available ac-
tion space is limited. In simple situations such as completing
questionnaires testing [72], making decisions from a set of
options [75], or rating with predefined standards [61], the ac-
tion space of LLMs is determined by researchers ahead of
simulation to make responses predictable. In practical sce-
narios, LLMs are required to choose tools [112, 122] or se-
lect specific functions to complete concrete tasks, like rec-
ommending, browsing, and compiling. Individual simulation
with agents in closed-domain tasks can improve human work
efficiency, extending beyond entertainment purposes.
Open domain simulation places few restrictions on actions,
allowing LLMs to generate responses freely. This approach
more closely resembles real-world conditions, but also de-
mands higher standards for individual simulation. Among
various open-domain tasks, taking actions through conver-
sation is a popular method for simulating individual behav-
ior [54, 59, 62, 65], in which the varied settings stimu-
late LLMs’ potential for individual simulation and allow re-
searchers to oversee simulations across diverse and nuanced
dimensions. Another growing method of open-domain simu-
lation is scenario-based interaction, where LLMs are assigned
roles and are required to interact in crated situations like sand-
box [108, 109] or established game settings [119, 121].
3.2
Construction
Construction indicates the process of integrating individual
data into the established model of LLMs, which aligns the
design model and the individual, thus creating the simu-
lating LLMs.
Generally, construction methods are distin-
guished into two types, namely nonparametric prompting
and parametric training.
3.2.1
Nonparametric Prompting
Nonparametric prompting, i.e.
prompt engineering, is a
method of interacting with LLMs by designing and opti-
mizing input prompts. In some individual simulations, the
description-based profile is implemented by a system prompt.
Researchers often create system prompts that begin with “You
are a...” to assign models specific demographic features and
roles [77].
Besides, LLM outputs are enhanced in some
works through few-shot prompting by providing specific ex-
amples to inject detailed information and improve response
quality. Moreover, incorporating problem-specific details di-
rectly within prompt structures can significantly enhance the
effectiveness of the simulation.
Short-term memory is often implemented by nonparamet-
ric prompting. For situation-based individual simulations, en-
vironment descriptions and behavior rules are typically con-
veyed through prompt engineering [121]. Since situational
information is generally objective and must be followed, em-
phasizing this information directly in the input is a rather ef-
fective method for constructing simulations. However, due
to the context window limitations of LLMs, the quality of
the profile prompt significantly restricts prompt-based indi-
vidual simulations. Moreover, the preset template configura-
tions as the “assistant” within LLMs pose a major challenge
for prompt engineering in individual simulations [83].
3.2.2
Parametric Training
Parametric training modifies the model by directly updating
the LLM parameters with given data. The training methods
can be generally categorized into pre-training, finetuning, and
reinforcement learning.
Pre-training
The pre-training method in individual sim-
ulation focuses on aligning the original LLMs with basic

## Page 7

individual-related data and setting up a fundamental knowl-
edge of individuals for LLMs.
The targets of training
datasets vary in recent studies, including individual descrip-
tions [113], literature summaries [54], and philosophical
works or utterances [56].
Finetuning
The finetuning method is designed for adapt-
ing LLMs for individual simulation in specific tasks and
situations.
Researchers collect and modify supervised in-
struction datasets tailored for specific situations and fine-tune
their models to equip them with the corresponding capabili-
ties. Using persona-enhanced datasets is an effective method
to regulate the models’ behavior in individual simulation,
which is constructed by adding instruction tuning samples
of the simulated individual’s behavior [68, 98]. LoRA fine-
tuning method can integrate multiple characters into a sin-
gle model [65, 123].
In multimodal finetuning scenarios,
both visual and textual information are considered to signif-
icantly enhance LLMs’ simulation behavior in multimodal
contexts [69, 113]. Compared to prompt engineering, fine-
tuning leverages large datasets more effectively and reduces
the limitations imposed by the pre-training phase of LLMs.
Reinforcement
Learning
The
reinforcement
learning
method is used to refine models in dynamic environments
with the goal of maximizing cumulative rewards. In sim-
ulations involving conversations and dialogues, the quality
of the LLM’s responses directly influences the rewards it
receives [87, 124, 125], which encourages the model to
learn the appropriate ways to respond in dialogues.
By
modifying the reward function, researchers can influence the
model’s preference and thus manage to mimic the personas
of the simulated individuals [88]. As individual simulations
become more diverse and complex, reinforcement learning
plays a crucial role in improving the dynamic behavior of
simulated LLMs.
3.3
Simulation Objectives
The simulation objectives of individual simulation for vari-
ous purposes can be divided into two categories: (1) Demo-
graphics: a group of people who share the same character-
istics, such as psychological traits (e.g., INTJ) or identity-
related features (e.g., farmers). (2) Characters: a specific
individual, whether real or virtual, who is widely recognized
by groups of people.
3.3.1
Demographics
Demographic individuals refer to a group of people who share
the same features. In an abstract sense, demographics can be
understood as the centroid of an embedding space that rep-
resents common opinions and beliefs, essentially clustering
individual embeddings for classification purposes [91]. De-
mographic simulation involves assigning an identity, such as
“student,” to LLMs and guiding the simulators to perform
specific tasks. Early demographic simulations have focused
on investigating the internal demographic attributes within
pre-trained models [74, 126], laying the groundwork for fur-
ther simulations. Additionally, these simulations are used to
reflect opinion surveys [93] or evaluate preferences and bi-
ases [99, 127] of particular groups. With the ability to scale
synthetic dialogue [63, 98, 128] involving specific personas,
demographic simulations can also contribute to societal sim-
ulation studies [111]. In most cases, demographic simulation
is implemented through nonparametric prompting. Many re-
searchers in this field focus on designing tasks, such as ques-
tionnaires or social experiments [75], to fully tap into the sim-
ulating potential of LLMs.
3.3.2
Characters
Characters are distinct individuals who differ from one an-
other. They may be ordinary platform users, well-known pub-
lic figures, or fictional characters from novels. Researchers
favor these characters because they enhance the expertise of
LLMs in specific domains and challenge the learning capa-
bilities of these models. From Haruhi and Li Yunlong [59]
to Beethoven [66], individual simulations select their protag-
onists from both real and virtual worlds.
Real Characters
Real characters, typically famous figures,
are associated with high-quality data from platforms like
Wikipedia and social media, making it easier to establish ob-
jective profiles and evaluate simulations. Many LLMs fo-
cus on historical figures, celebrities across various periods
and backgrounds [10, 129], characters from online encyclo-
pedias [64], and popular livestreamers on Douyin [60]. Since
LLMs often have prior knowledge of these individuals, creat-
ing their profiles is relatively straightforward. Real and sim-
ulated characters are also used to test LLM simulation capa-
bilities, such as in philosopher simulations [56].
Virtual Characters
Virtual characters are fictional roles
created in novels, movies, and video games.
Advance-
ments in virtual character simulation can significantly ben-
efit entertainment sectors like the gaming industry and theme
parks.
Many researchers have drawn inspiration from fa-
mous fictional characters, such as Harry Potter [55], Sun
Wukong [62], and Tong Xiangyu [130]. Additionally, some
experiments design virtual characters [119] with specific at-
tributes or objectives.
However, despite the attention vir-
tual character simulation attracts, developing virtual individ-
ual LLMs presents challenges, particularly in ensuring the
quality and reliability of their datasets. Most simulations of
virtual characters are designed for interactive conversations,
enhancing user experience in various entertaining scenarios.
3.4
Evaluation
To measure the performance of individual simulations, pro-
vide insights into their feasibility, and guide improvements
to simulation architectures, researchers have developed di-
verse evaluation standards and methods, ranging from simple
to complex approaches. These methods can be categorized
into static evaluation and interactive evaluation.
3.4.1
Static Evaluation
Static evaluation refers to the dialogue-based assessment of
LLMs by directly inducing their generation and measuring
their quality. It can be categorized into subjective evaluation,
which involves assessments by both LLMs and human eval-
uators, and objective evaluation, which utilizes mathematical
tools for analysis.

## Page 8

Evaluation
Sub-Task
System
Automatic
Human
Level
Strategy
Task
LLM
System
Scenario
Dialog-Driven
Task-Driven
Evaluate
Integrate
Role
Environment
Coordinator
Integrator
Planner
Communicator
Worker
Participants
Directors
Configuration
State
Tool
History
Organization
Structure
Mode
Communication
Format
Style
Figure 3: Illustration of scenario simulations. Given a specific scenario, building a multi-agent system involves modeling environment, roles,
organization, and communication with detailed modules or mechanisms adjusted to the targeted scenario being supported. After simulating
the scenario, the desired output, typically the result of a task or problem, is obtained and evaluated using different levels and strategies.
Subjective Evaluation
Subjective evaluation refers to as-
sessments conducted by humans or LLMs based on subjec-
tive standards. It often involves leveraging conversations with
varying forms and contexts. Interview techniques are widely
adopted [28, 61] because they can effectively prompt LLMs
to generate expected responses. Other approaches, such as
utterance imitation [77], are also favored in some research.
Once dialogues are generated, some studies utilize advanced
LLMs to evaluate the output on a given scale [61, 65, 130],
considering performance dimensions.
These dimensions
range from psychology-based metrics, such as the Big Five
Personality Traits (BFI) and Myers-Briggs Type Indicator
(MBTI), to language-based factors like grammar and tone.
Human annotators are often involved in experiments to pro-
vide human reference points [57, 84, 131].
Objective Evaluation
Objective evaluation refers to as-
sessments based on objective indicators, utilizing mathemat-
ical and statistical tools. It takes advantage of mathemati-
cal tools to grade the generation of simulating LLMs. Ex-
amination commonly involves option choosing(or question-
naire) [72], ranking [60] and question answering [102]. Ac-
curacy [91, 106], F1 score, recall [132, 133] are used in
option choosing and ranking. In the examination of gener-
ation(question answering), text sequence related tools such
as perplexity [58, 118, 134], ROUGE-L [55, 74, 106] and
BLUE [60, 74, 132, 134] are broadly used in the evaluation,
especially those with a reference version [55]. Objective Ex-
amination is a more credible method of evaluating the per-
formance of LLMs in individual simulation. However, it is
highly restricted, and occasionally, specific objective tools
must be developed to facilitate the evaluation of simulation
in given dimensions.
3.4.2
Interactive Evaluation
Interactive evaluation refers to a circumstance-based assess-
ment that creates a detailed interactive environment to mea-
sure the ability of individual simulations in complex scenar-
ios. It is commonly applied in areas such as game perfor-
mance [119, 121], task completion [112, 135, 136], and nu-
anced role-playing [88, 104]. Three key features of interac-
tive evaluation are the carefully designed environment, real-
time interactive external responses, and multi-stage assess-
ments. Information about the crafted environment has been
introduced in §3.1.4. Real-time interactive external responses
refer to the feedback from the external environment in reac-
tion to the outputs of simulating LLMs. Agent-environment
interactions construct multiple dialogues between the LLMs
and the environment.
These interactions help reveal the
LLMs’ capabilities in complex contexts, leading to more dy-
namic simulations. Single-aspect measurements are insuffi-
cient for interactive evaluation, so many studies adopt evalu-
ated objectives that range from specific actions to hybrid ac-
tions [110], or from single-turn interactions to multi-turn dia-
logues [10]. Other studies assess generation quality, focusing
on aspects such as accuracy relative to ground truth, nuanced
simulations like tone imitation [28, 107], and self-reporting
consistency [137]. In interactive evaluation, researchers pri-
oritize not only accuracy but also the degree to which the sim-
ulation resembles real-world scenarios.

## Page 9

4
Scenario Simulation
In the real world, individuals do not function in isolation.
They frequently engage in collaborative efforts to complete
tasks within specific scenarios. This raises a crucial question:
can LLM-based agents cooperate like humans or even sur-
pass human performance in achieving collective intelligence?
To answer this question, researchers simulate the interactions
and collaborations of multiple individuals across various sce-
narios [16, 17, 147], ranging from everyday conversations to
complex professional tasks, to enhance collective intelligence
and problem-solving capabilities. A scenario simulation typ-
ically starts with designing a multi-agent system that includes
constructing the scenario environment, modeling agent roles,
and establishing organizational structures and communica-
tion protocols to manage interactions among agents.
In this section, we begin discussing the system composi-
tion of a scenario simulation with four key aspects in §4.1.
Following this, we summarize several scenarios that have re-
cently attracted the attention of researchers in §4.2. Finally,
we review the methods and metrics commonly used for eval-
uating scenario simulations in §4.3. The overall framework
is presented in Figure 3 and representative works are summa-
rized in Table 2.
4.1
System
The diversity of scenarios presents challenges in proposing
a unified system applicable to scenarios. Most of the cur-
rent systems can be summarized as “agents organized to play
roles in dedicated environments through constrained com-
munications”. Based on this general description, we iden-
tify four key concepts in scenario simulations: environment,
role, organization and communication.
4.1.1
Environment
The environment in scenario simulation defines the specific
contexts in which agents operate and interact with each other.
Just as humans gather information from their surroundings,
agents depend on the environment to receive input from var-
ious sources. These signals guide the behaviors and strate-
gies of agents within the system.
Thus, a comprehensive
understanding of the environment paves the way for agents’
decision-making and task continuity. We analyze the envi-
ronment of existing work by focusing on four key aspects:
configuration, state, history and tools.
Configuration
The environment configuration provides ba-
sic information, especially essential elements necessary for
the tasks and goals in the scenario. The system will initialize
agents accordingly so that they interact with clear objectives.
More specifically, an environment configuration may include
events in the environment and profiles of agents.
Events are represented as a primary focus that needs to
be resolved, such as the specific cases brought before the
court [20, 181, 185, 186], and the topics that serve as the basis
for multi-agent debates. [29, 144–149].
Profile refers to personalized information relevant to the
agents specific to the scenario. Different from the basic at-
tributes described in individual simulation, this module en-
compasses various aspects of the agents’ identities, including
their interests, goals, and roles [17, 142, 172]. Agents can
also be configured to have access to external resources, such
as related research papers [171], predefined strategies [142]
or disease information [18].
State
Environment states encompass the information pro-
vided by the environment during scenario execution (config-
urations are fixed at the beginning instead). They directly
influence the agents’ decision-making and behavior. Accord-
ing to how agents receive them, states can be further divided
into observation and feedback.
Observation involves changes in the environment and the
current state of surrounding entities. For example, proper-
ties and spatial positions [164, 189, 194, 197] of other agents
are provided to agents to inform real-time decision-making.
Moreover, continuously updating agents’ physical states are
utilized to establish real-time spatial relationships with their
environment and neighboring agents [161, 194, 197, 198].
Feedback consists of responses received by agents after
they perform actions, which guide future strategy adjust-
ments. Some studies [162, 164, 190] describe how agents’
cognitive states and strategies are modified based on feedback
after each interaction, allowing them to simulate human-like
adaptability. Meanwhile, feedback on market events or deci-
sions made by others [162, 182] and execution results from
external tools [17, 147, 177] are provided, to facilitate strat-
egy adjustment and guide future actions.
History
As the scenario runs, past states and interactions
accumulate into a series of history records. Agents can lever-
age them to adapt to new situations and refine strategies, en-
suring more coherent and effective task performance in dy-
namic environments. We summarize four widely used meth-
ods to process and utilize the history, including direct integra-
tion, refinement, summarization and memory mechanisms.
Direct integration appends the history to the current in-
put without modification. Agents may retain task continu-
ity by incorporating past dialogue directly into the current
session [29, 145, 147, 166]. Excessive content is truncated
to fit token limits while preserving key historical informa-
tion [194, 196].
Refinement iteratively updates and enhances responses
based on the history.
Ma et al. [149] uses a subgraph-
focusing mechanism to refine answers, allowing agents to op-
timize outcomes after each reasoning step. Similarly, Weiss
et al. [183] and D’Arcy et al. [30] iteratively improves initial
answers to converge to more accurate results.
Summarization distills essential insights from the history.
This can be achieved by synthesizing core actions from mul-
tiple plans to establish a reference for diverse scenarios [161],
summarizing reports from multiple agents to consolidate find-
ings [168], and sharing key solutions subtasks [177] to avoid
lengthy dialogue histories.
Memory mechanisms process the history through agents’
memory modules. This dynamic approach enables agents to
preserve relevant information both within and across sessions
[26, 48, 173, 180, 182, 195, 199, 200]. In addition, Hong
et al. [17] proposed shared message pools to further enhance
communication efficiency, where agents exchange structured
messages directly and retrieve information in a personalized

## Page 10

Scenario
Task
Paper
Environment
Director Role
Organization Communication
Configuration State History Tools Planner Coordinator Integrator
Dialog-
Driven
Social
Interaction
Sotopia [138]
✓
✓
✓
static,single
UNL
Elicitron [139]
✓
✓
static,multi
UNL
APAM [140]
✓
✓
static,single
UNL
SimuLife++ [141]
✓
✓
static,single
UNL
Self-Emotion [142]
✓
✓
✓
dynamic,single
UNL
Question
Answering
ICL-AIF [143]
✓
✓
✓
static,single
UNL
FORD [144]
✓
✓
✓
static,multi
UNL
du et al. [29]
✓
✓
static,single
UNL
MAD [145]
✓
✓
✓
static,single
UNL
ChatEval [146]
✓
✓
✓
static,single
UNL
AutoGen [147]
✓
✓
✓
dynamic,single
UNL
AmazonHistoryPrice [148]
✓
✓
static,single
UNL
DoG [149]
✓
✓
✓
dynamic,single
UNL
ChatLLM [49]
✓
static,single
UNL
Game
xu et al.[150]
✓
✓
static,multi
UNL
ReCon [151]
✓
✓
static,multi
UNL
MachineSoM [152]
✓
✓
dynamic,single
UNL
AvalonBench [153]
✓
✓
static,multi
UNL
lan et al. [154]
✓
✓
static,multi
UNL
xu et al. [155]
✓
✓
static,multi
UNL
ThinkThrice [156]
✓
✓
dynamic,single
UNL
CodeAct [157]
✓
✓
static,multi
UNL
wu et al. [158]
✓
✓
static,multi
UNL
WWQA [159]
✓
✓
✓
✓
static,multi
UNL
PLAYER [160]
✓
✓
dynamic,multi
UNL
GITM [161]
✓
✓
✓
✓
static,multi
UNL
sreedhar et al. [162]
✓
✓
✓
static,single
UNL
AmongAgents [163]
✓
✓
✓
static,multi
UNL
S-Agents [164]
✓
✓
✓
✓
✓
dynamic,single
UNL
Task-
Driven
Foundational
and Applied
Science
VIDS [165]
✓
✓
dynamic,multi
UNL
DR-CoT [166]
✓
✓
static,single
UNL
ChatGPT Research Group [167]
✓
✓
✓
✓
dynamic,multi
UNL
MedAgents [168]
✓
✓
✓
dynamic,multi
UNL,SL
MARG [30]
✓
✓
✓
static,multi
UNL
AI Hospital [19]
✓
✓
✓
static,multi
UNL,SL
REVIEWER2 [169]
✓
static,multi
UNL
CosmoAgent [170]
✓
✓
✓
dynamic,single
UNL
FPS [26]
✓
✓
dynamic,single
UNL
ResearchAgent [171]
✓
✓
static,multi
UNL
Agent Hospital [18]
✓
✓
dynamic,multi
UNL,SL
CulturePark [50]
✓
✓
✓
dynamic,single
UNL
SynthPAI [172]
✓
✓
✓
dynamic,single
UNL
DreamFactory [173]
✓
✓
✓
static,multi
UNL,SL
AutoTQA [174]
✓
✓
✓
✓
✓
static,multi
UNL
DERA [175]
✓
✓
✓
static,single
UNL
Software
Development
Self-collaboration [176]
✓
✓
dynamic,multi
UNL
ChatDev [177]
✓
✓
✓
✓
static,multi
UNL,SL
MetaGPT [17]
✓
✓
✓
✓
✓
✓
static,multi
SL
Experiential Co-Learning [178]
✓
✓
✓
✓
dynamic,multi
UNL,SL
AutoCodeRover [179]
✓
✓
✓
static,multi
UNL,SL
IER [180]
✓
✓
dynamic,single
UNL,SL
Other
Industries
Blind Judgement [181]
✓
static,single
UNL
TradingGPT [182]
✓
✓
✓
dynamic,single
UNL
Information Bazaar [183]
✓
✓
static,single
UNL
SimuCourt [20]
✓
✓
✓
✓
static,multi
UNL,SL
MATHVC [184]
✓
✓
✓
static,multi
UNL
baker et al.[185]
✓
✓
static,multi
UNL
LawLuo [186]
✓
✓
✓
dynamic,multi
UNL
MAIC [187]
✓
✓
✓
✓
dynamic,multi
UNL
CAMEL [188]
✓
✓
✓
static,single
UNL
SwiftSage [189]
✓
✓
✓
static,single
UNL
Multi-Agent Collaboration [190]
✓
✓
✓
✓
dynamic,single
UNL
CoELA [191]
✓
✓
✓
static,multi
UNL
RoCo [192]
✓
✓
✓
static,single
UNL
AgentVerse [193]
✓
✓
✓
✓
✓
dynamic,multi
UNL
Scalable [194]
✓
✓
✓
✓
dynamic,single
UNL
AutoAgents [195]
✓
✓
✓
✓
dynamic,single
UNL
OpenAgents [196]
✓
✓
✓
✓
dynamic,single
SL
TWOSOME [197]
✓
✓
static,single
-
ReAd [198]
✓
✓
✓
✓
dynamic,single
UNL
MACNET [48]
✓
✓
dynamic,single
UNL
Table 2: A list of representative works of scenario simulation. UNL: unstructured natural language; SL: structured language.

## Page 11

manner.
Tools
External tools offer specialized functionalities related
to scenario simulation tasks, enabling more accurate and pre-
cise outcomes. The spectrum of tools utilized in scenario sim-
ulation encompasses a wide range, from programming lan-
guages such as Python and SQL to APIs facilitating exter-
nal interactions. Generally, Python is mainly employed to
execute and verify programmes [17, 147, 177]. SQL [174]
and knowledge graphs query tools [149, 171] have been har-
nessed to retrieve external structured data. In certain scenar-
ios, task-related tools such as calculators, predefined tools,
and APIs [195, 196] are also utilized to provide intermediate
results, simplifying the processing workflow of agents.
4.1.2
Role
In scenario simulations, we assign agents distinct roles based
on their tasks and functionalities. As demonstrated in Fig-
ure 3, there are two groups of roles in a typical setting: par-
ticipants carry out the tasks within the scenario, and directors
manage the task execution processes while providing neces-
sary assistance. Each role has its own responsibility that em-
phasizes different aspects of the system’s operations. They
collaborate to achieve the system’s overall goals.
Participants
Participants are the key members that actively
engaged in task execution and discussion. Their organization
and communication are the core of task completion in sce-
nario simulations. Participants can be further classified into
communicators and workers according to their tasks.
Communicators primarily focus on communication, such
as information exchange, feedback, and task guidance.
Specifically, this kind of agents can process information for
certain disciplines and research applications [175, 181] and
advocate diverse viewpoints [49, 144], claims [145] and un-
derlying needs [50, 139].
Workers are directly involved in task execution and opera-
tions, demonstrating specialized skills and efficiency. This
typically includes the common professional roles present
in each scenario, such as coder and tester in software de-
velopment [176], buyer and seller in negotiations [143],
doctors and medical professional agents in healthcare do-
main [18, 166], and receptionist, lawyer, and secretary in the
legal contexts [186].
Directors
While participants execute most of the tasks, di-
rectors can provide essential support in crucial aspects such
as planning procedures, coordinating communication, and in-
tegrating results. We name them Planners, Coordinators and
Integrators respectively.
Planners play a vital role in task definition and strate-
gic formulation, facilitating effective inter-agent collabora-
tion through tasks such as defining objectives, analyzing user
requirements, and optimizing execution plans. Task-specific
agents [188], central planners [193], analysts [176] and de-
composer [161] are responsible for breaking down require-
ments and dividing overarching objectives into specific sub-
goals. Product managers [17] contribute by creating detailed
product requirements documents. Other planners can also re-
fine execution plans according to task requirements [194],
optimize the process by maximizing the advantage func-
tion [164] and develop plans based on user inquiries [174].
Coordinators are responsible for managing and coordinat-
ing the collaboration between agents to ensure effective task
execution, monitor progress, and facilitate cooperation. The
project managers [17, 167] in software development over-
see task distribution and project progress, ensuring efficient
collaboration among team members throughout the develop-
ment cycle. Judge assistant agents [20] aids in organizing
information during court proceedings, and the main contact
agents [50] manage intercultural conversations. Additionally,
the secretary agents [170] manage interactions among civi-
lization agents. Meanwhile, coordinators also provide feed-
back to guide better interactions. Critic agents [143] evalu-
ate negotiation strategies and guide agents through iterative
learning processes. Judge agents [144, 145, 201] serve as
an authoritative evaluator, assessing arguments and perfor-
mances during debates.
Integrators encompass various decision-making and sum-
marization functions critical for guiding the system’s trajec-
tory.
Deciders [175] autonomously evaluate contributions
from the researcher to make informed judgments on the dia-
logue’s outcome. Summarizer agents [146] enhance commu-
nication clarity by providing concise summaries of discus-
sions after each iteration, effectively integrating key points
into the ongoing dialogue. In medical scenarios, medical re-
port assistants [168] compile analyses into a cohesive docu-
ment that supports collaborative expert discussions, while the
medical decision maker ensures that final decisions reflect the
collective expertise of the specialists involved. Additionally,
the chief physician [19] evaluates diagnostic performance
based on accuracy and effectiveness, reinforcing the system’s
overall reliability. In legal contexts, the judge [20] oversees
judicial processes, making critical decisions grounded in le-
gal arguments and assessing the evidence presented.
4.1.3
Organization
Effective task execution necessitates careful coordination and
scheduling of the interactions between individual agents. The
organizational structures establish how each agent collabo-
rates with others to achieve a goal. Typically, we can depict
an organization schema by its mode and structure.
Mode
The organizational structure determines whether the
relationships among agents remain stable or evolve dynami-
cally throughout the simulation process. In terms of how to
organize agents, there are mainly two modes in existing re-
search, i.e., static and dynamic mode.
Static mode refers to the organizational structure prede-
fined based on the nature of the tasks.
Agents communi-
cate and work in an orderly manner according to these static
structures. The static mode can be further divided into single-
stage and multi-stage setups. In the single-stage setup, agents
follow a fixed structure in multiple rounds of communica-
tion, such as structured debates [143, 146, 175, 188], skill
training [140, 141] and integrating ideas [49, 181]. In the
multi-stage setup, tasks are divided into distinct stages, and
the organization may change with stages. This can be found
in the design, coding, and testing stages in software devel-
opment scenarios following the waterfall model or standard-

## Page 12

ized operating procedures [17, 177], and multi-stage pro-
cess in judicial scenarios [20, 185] and problem-solving pro-
cesses [149, 161, 191].
Dynamic mode explores more open and adaptive orga-
nizational structures, often relying on dynamic and heuris-
tic communication.
This also includes both single-stage
and multi-stage setups. The single-stage setup emphasizes
agent collaboration and adaptability in a single stage. The
agents can be flexibly created and recruited [149, 193, 195,
196, 202], coordinated through liaison agents [50, 170], and
self-organized [164].
The multi-stage setup mainly fea-
tures dynamic discussions among agents. Agents can be in-
volved across multiple stages, but they can communicate au-
tonomously based on the current state [167, 168, 176, 186,
187].
Structure
The organization structure, meanwhile, reflects
how agents are connected with each other. Typically, an orga-
nization can be layered, centralized or decentralized. Layered
structures adopt a hierarchical framework, with agents as-
signed to distinct levels. Interactions are predominantly con-
fined to agents within the same level or occur between ad-
jacent layers, thereby facilitating a controlled and organized
flow of information[49, 177, 181]. Centralized structures of-
ten involve a high-level role (e.g., coordinator) that serves as
the core of the organization, overseeing communication and
functioning as the central hub for interactions among other
agents[19, 50, 170]. Decentralized structures, in contrast, is
more flattened, where agents can engage in peer-to-peer in-
teractions as needed[145, 146, 149].
4.1.4
Communication
The communication between agents controls the transmission
of information. To better understand the internal mechanism
of communication, we dissect communication from its format
and style.
Format
From the perspective of information format, there
exist two common communication protocols: unstructured
natural language and structured language.
Unstructured natural language is most commonly used in
multi-agent communication, enabling flexible and immediate
exchanges through free-form, conversational language that
mirrors human dialogue [29, 140, 141, 143, 144, 167, 175,
188]. Communication based on natural language is diverse
and flexible, but it can also suffer from issues such as ambi-
guity and redundancy.
Structured language, such as code and JSON documents,
is another protocol that may alleviate the issues from natural
language. In software development, agents transit informa-
tion between phases through code [17, 177]. In the medical
domain, structured summaries of reports are utilized to gain
key insights [168]. In addition to predefined formats, agents
can also autonomously choose the appropriate format during
interactions to improve efficiency [51, 203]. Recently, more
complex communication protocols using more than one lan-
guage have been designed to improve communication [53].
Style
Communication, by nature, can be cooperative or
competitive regarding its style. In cooperative communica-
tion, agents share a common objective, aiming to optimize
collective outcomes, like software development[17, 176,
177], medical diagnosis[19, 168], and case handling[181,
186]. In contrast, agents in competitive communication typi-
cally hold differing viewpoints and positions, each striving to
achieve individual objectives. Such scenarios are commonly
found in settings like games[150, 151, 159] and debates[143–
145], where agents maintain opposing stances and seek to
outmaneuver each other.
4.2
Scenario
Using the collective capabilities of agents with specialized
expertise, scenario simulations have been applied to various
domains. Here we divide different scenarios into two groups:
dialog-driven ones that cover social interaction and question-
answering, and task-driven ones that focus on specialized
tasks.
4.2.1
Dialog-Driven Scenario
Dialog-driven scenarios encompass scenarios in people’s
daily lives where the dialog itself is centered, such as those
for social or entertainment purposes. These scenarios share
a common emphasis on tackling general goals that are not
related to any specific task or domain.
We identify three
primary types of dialog-driven scenarios: social interaction,
question-answering, and game scenarios.
Social Interaction
Some works focus on task completion
in simple social interaction scenarios, typically involving so-
cial tasks between two or a few agents, such as persuasion or
comforting a partner. Zhou et al. [138] discusses the social
intelligence of agents in social scenarios, revealing signifi-
cant performance differences among models across different
dimensions. The exploration in social intelligence is further
extended to objective action-level evaluation [204] and di-
verse scenarios and others’ information reasoning[205]. Fur-
thermore, some works propose interactive learning meth-
ods [140, 206, 207] to help learn social skills.
Question Answering
Another mainstream scenario is the
question answering, emphasizing collaborative processes,
strategic reasoning, and integration to enhance model per-
formance.
On the one hand, some studies focus on im-
proving reasoning through debate. FORD [144] facilitates
a three-stage commonsense reasoning debate, demonstrating
that LLMs can reach consensus even amidst inconsistencies.
MAD [29], involves agents debating under a judge’s super-
vision, addressing the Degeneration-of-Thought problem. In
addition, a “society of minds” approach [29] is presented to
guide multiple debate rounds, improving mathematical rea-
soning and factual accuracy while reducing hallucinations.
On the other hand, some works focus on optimizing strategies
in strategic reasoning and negotiation. OG-Narrator [148]
is proposed to improve negotiation strategies, increasing the
Buyers’ deal success rates. Ma et al. [149] utilize a subgraph-
focusing mechanism and a multi-role debate team to im-
prove reasoning accuracy and reliability, outperforming ex-
isting methods.
Game
Games provide a unique platform for exploring sce-
nario simulation, evolving from basic game reproduction to
complex social dynamics. Early studies, such as [150, 151],

## Page 13

introduce Werewolf and Avalon to examine LLM perfor-
mance in communication games, specifically investigating
how LLMs handle aspects like trust and leadership. Build-
ing on these complex interactions, reinforcement learning
frameworks in [155, 158] allow agents to adapt their strate-
gies, achieving near-human-level decision-making. To ex-
plore deeper social phenomena, [158, 160] expand on game
dynamics by incorporating tools that enhance memory, rea-
soning, and adaptability. Additionally, [159] examines the
role of opinion leadership, while [156, 157, 208] tackle ad
hoc teamwork, where agents adapt and collaborate without
predefined protocols, revealing both the challenges and po-
tential of LLM agents in team-based collaboration.
4.2.2
Task-Driven Scenario
In task-driven scenarios, agents role-play personas with spe-
cific functions for a certain task or task-set. Most of these
scenarios fall into one or more specific domains related to
the tasks. Here, agents are increasingly leveraged to solve
complex, domain-specific problems by automating tasks and
improving decision-making processes.
Foundational and Applied Science
Science domains, such
as medicine, mathematics, data science, and content analy-
sis, have been popular experimental fields for scenario sim-
ulation. In the medical domain, medical reasoning and au-
tomating diagnostic processes have been refined through in-
novative methodologies such as chain-of-thought prompting
and multi-agent collaboration[18, 166, 168, 209].
Zheng
et al.[167] integrates ChatGPT with Bayesian optimization
techniques to enhance research workflows in chemistry lab-
oratories, demonstrating significant improvements in effi-
ciency and productivity. Hassan et al.[165] introduce a con-
versational framework that enables seamless interaction with
machine learning models, specifically for tasks like data visu-
alization and predictive analytics. These studies demonstrate
the potential of LLM-based agents to transform traditional re-
search patterns.
Software Development
Recent research has increasingly
focused on harnessing agents to address complex challenges
in software development and life-cycle management. Early
works focus on designing frameworks for collaborative code
generation. Dong et al. [176] presents a self-collaboration
framework where LLM agents function as distinct “experts,”
each managing specific subtasks to facilitate autonomous col-
laborative code generation. Building on this, ChatDev[177],
a chat-powered framework utilizes unified language-based
communication among agents to effectively address design,
coding, and testing phases. Meanwhile, Hong et al. [17] en-
hances LLM collaborations by encoding Standardized Oper-
ating Procedures into prompts, enabling agents to verify re-
sults and produce coherent solutions through an assembly line
approach. Afterward, some works focus on enabling agents
to learn from past experiences and refine their processes over
time [178, 180]. Further efforts focus on autonomous issue
resolution and program understanding [179]. These studies
show the potential of multi-agent collaboration in software
engineering, offering robust tools for automatic development
and management.
Other Industries
In the realm of broad social science,
several studies leverage multi-agent systems to enhance
decision-making processes across diverse fields, such as jour-
nalism [210], judiciary, economics, and education. In the ju-
dicial field, legal consultations have been improved through
LawLuo [186], which simulates collaborative discussions.
Hamilton et al. [181] and He et al. [20] design multi-agent
systems to simulate U.S. Supreme Court decisions and court
trials through detailed steps such as debate, resource retrieval,
and decision refinement, complemented by additional bench-
marks that enhance legal article generation. In the economic
sector, Li et al. [182] propose a multi-agent framework with
layered memory to improve LLM performance in stock trad-
ing. Additionally, Weiss et al. [183] address the buyer’s in-
spection paradox in information markets by simulating a mar-
ketplace where intelligent agents use LLMs to navigate infor-
mation access and biases, exploring the impact of pricing and
budgets on outcomes. In the education domain, MAIC [187],
a system simulating AI-enhanced classrooms has contributed
to the development of a comprehensive AI-driven online ed-
ucation platform. Yue et al. [184] presents MATHVC, an
LLM-driven virtual classroom designed to simulate interac-
tions among students, thereby fostering the development of
mathematical skills.
4.3
Evaluation
For scenario simulations, the evaluation focuses on how well
the tasks of the scenarios are solved. Based on the scope
of the evaluation, it can be categorized into task evaluation,
sub-task evaluation and system evaluation, each employing
various automatic, LLM-based, and human evaluation meth-
ods to assess performance.
Task Evaluation
Task Evaluation measures the overall per-
formance of tasks assigned to the scenario. The evaluation
can carried out in automatic ways or by LLMs or humans. In
terms of automatic evaluation, predefined metrics and math-
ematical tools are used to objectively assess the task out-
comes, such as accuracy [144, 181], pass@k [188] for coding
tasks, success rate, and coverage for exploration [161], and
deal price for negotiation [143]. These methods are efficient
and scalable but may overlook complex behaviors.
Thus,
LLMs [49] and human experts [145, 188] have been applied
to provide more nuanced evaluation for qualitative tasks and
compare solutions based on specific criteria.
Sub-Task Evaluation
Sub-task Evaluation assesses the
completion of sub-tasks within a scenario simulation and
their impact on overall task performance.
It serves as a
process evaluation for the execution of complex tasks. The
automatic evaluation uses metrics like transport rate, aver-
age steps, task success rate, re-plan attempts, and efficiency
improvement to assess sub-task performance and strategy ef-
ficiency [191, 192]. Completeness, executability, and con-
sistency metrics are often applied in software generation
tasks [177, 178]. LLM-based evaluation focuses on pairwise
comparisons or win rate judgments, capturing qualitative as-
pects of sub-task performance [177].
Meanwhile, human
evaluation relies on participants to provide subjective assess-
ments on metrics such as executability, revision costs, or com-

## Page 14

Scenario
Social Construction Element
General Economic
Sociology and Politics
Support
Evaluation
Micro
System
Level
Online Platform
Composition
Network
Social Influence
Outcome
age
gender
…
Relation
offline
online
opinion
norm
Social Media
RecSys
Economics
Game Theory
Politics
…
…
…
Macro
Evaluate
Subjective
Objective
Strategy
Sociology
Figure 4: Illustration of society simulations. To construct society simulations, the corresponding society’s construction elements, i.e., com-
position, network, social influence and outcomes need to be carefully designed. Building on this, various scenarios can be simulated. The
performance of individuals and the overall performance of the system are evaluated.
ment quality, offering practical insights into sub-task perfor-
mance [17, 30].
System Evaluation
System Evaluation aims to capture the
effectiveness and efficiency of the system in a scenario simu-
lation as a whole. Automatic evaluation relies on metrics such
as token consumption, task success rate, and human-likeness
scores to measure the efficiency and realism of agents [197].
Additional metrics like accuracy, precision, recall, and F1
scores are used to assess system accuracy and consistency
in diagnostic or predictive tasks [19].
LLM-based evalua-
tion often involves GPT-4 to assess qualitative aspects, such
as human-likeness or diagnostic report quality [18, 197].
Human evaluation typically involves subjective assessments,
such as rating instructional content for tone, clarity, and sup-
portiveness on a Likert scale [187], often used to complement
automatic methods and capture human perspectives on sys-
tem outputs.
5
Society Simulation
While scenarios discuss multi-agent interactions in rela-
tively focused and small-scale contexts and provide solutions
within specific domains, society is more complex than a sim-
ple scenario. Its complexity lies in many aspects, such as the
diversity of its components, the variety of structures, and non-
linear effects [259]. Considering this, a series of studies fo-
cus on society simulation. In terms of research topic, society
simulation generally hopes to investigate societal and macro-
level results. In terms of research purpose, society simulation
does not aim to solve a task or problem, instead, it focuses
on revealing and explaining emergent behaviors and the out-
comes of interactions among numerous agents. Society sim-
ulations have been a vital tool for theoretical validation and
predicting social dynamics.
In this section, we summarize the components of social
construction to capture the key features reflected in society
simulations in §5.1. Then, we present the different categories
of scenarios in society simulation in §5.2.
After that, we
introduce the evaluation of society simulation in §5.3. The
overall framework is illustrated in Figure 4 and representa-
tive works are summarized in Table 3.
5.1
Social Construction Elements
Considering the complexity of society, a major challenge in
society simulation is bridging the gap between individual and
societal scales. Some core elements serve as the foundation
for modeling social systems. We outline four key dimensions
that underpin societal structures and dynamics: composition,
network, social influence, and outcomes.
5.1.1
Composition
Society is composed of massive and diverse individuals. This
diversity, also referred to as heterogeneity [259] in social sci-
ence, encompasses a wide range of beliefs, preferences, be-
haviors, normative values, and positions within social struc-
tures. Modeling this diversity is essential for capturing the
varied behavioral patterns and complex social dynamics that
emerge from individual differences within a social system.
Individual Composition
To model a diverse society, the
composition of individuals in society needs to be determined.

## Page 15

Scenario
Field
Paper
# Agents
Construction Element
Composition Network Social Influence Outcome
General
Economic
Game Theory
and
Strategic Interactions
Agent-trust [211]
(0, 10]
✓
✓
✓
LELMA [212]
(0, 10]
✓
✓
Economics Arena [213]
(0, 10]
✓
✓
Fontana et al. [214]
(0, 10]
✓
✓
SABM [215]
(0, 10]
✓
✓
✓
✓
Noh and Chang. [216]
(0, 10]
✓
✓
✓
Mozikov et al. [217]
(0, 10]
✓
✓
Wu et al. [218]
(10, 100]
✓
✓
✓
CompeteAI [219]
(10, 100]
✓
✓
✓
✓
WarAgent [47]
(10, 100]
✓
✓
✓
✓
Economic
Contexts
Horton [220]
(10, 100]
✓
✓
EconAgent [27]
(10, 100]
✓
✓
SRAP-Agent [221]
(10, 100]
✓
✓
✓
✓
Ghaffarzadegan et al.[222]
(10, 100]
✓
✓
✓
EC [223]
(10, 100]
✓
✓
✓
✓
Williams et al. [224]
(100, ∞)
✓
✓
✓
✓
AgentTorch [225]
(100, ∞)
✓
✓
✓
Sociology
and
Political Science
Public Opinion
Survey
Argyle et al. [12]
(100, ∞)
✓
✓
Lee et al. [226]
(100, ∞)
✓
✓
Chaudhary and Chaudhary [13] (100, ∞)
✓
✓
ElectionSim [227]
(100, ∞)
✓
✓
GABSS [228]
(100, ∞)
✓
✓
✓
✓
Park et al. [229]
(100, ∞)
✓
✓
Sun et al. [96]
(100, ∞)
✓
✓
Individual
and
Organizational
Behavior Observation
Aher et al. [230]
(0, 10]
✓
✓
Zhang et al. [152]
(0, 10]
✓
✓
Lyfe Agents [231]
(0, 10]
✓
✓
✓
✓
CRSEC [232]
(0, 10]
✓
✓
✓
✓
Chuang et al.[24]
(0, 10]
✓
✓
✓
✓
ChoiceMates [233]
(0, 10]
✓
✓
✓
✓
Jarrett et al.[234]
(0, 10]
✓
✓
AgentReview [235]
(0, 10]
✓
✓
✓
Generative Agents [32]
(10, 100]
✓
✓
✓
✓
AGA [236]
(10, 100]
✓
✓
✓
✓
MineLand [237]
(10, 100]
✓
✓
✓
✓
Chuang et al. [31]
(10, 100]
✓
✓
✓
✓
CareerAgent [238]
(10, 100]
✓
✓
✓
✓
Suzuki and Arita [239]
(10, 100]
✓
✓
✓
Chuang et al.[240]
(100, ∞)
✓
✓
Li et al. [241]
(100, ∞)
✓
✓
✓
MATRIX [242]
(100, ∞)
✓
✓
Online
Platform
Social
Platforms
Cai et al.[243]
(0, 10]
✓
✓
FPS [26]
(10, 100]
✓
✓
✓
✓
FUSE [244]
(10, 100]
✓
✓
✓
✓
Wang et al.[245]
(10, 100]
✓
✓
✓
✓
Concordia [246]
(10, 100]
✓
✓
✓
✓
Social Simulacra [247]
(100, ∞)
✓
✓
✓
✓
S3 [248]
(100, ∞)
✓
✓
✓
✓
T¨ornberg et al. [249]
(100, ∞)
✓
✓
✓
✓
Y Social [250]
(100, ∞)
✓
✓
✓
✓
TIS [251]
(100, ∞)
✓
✓
✓
✓
HiSim [25]
(100, ∞)
✓
✓
✓
✓
OASIS [33]
(100, ∞)
✓
✓
✓
✓
MindEcho [252]
(100, ∞)
✓
✓
BASES [253]
(100, ∞)
✓
Recommendation
Environments
InteRecAgent [254]
(0, 10]
✓
Rec4Agentverse [255]
(0, 10]
✓
✓
RecAgent [256]
(10, 100]
✓
✓
✓
✓
Agent4Rec [257]
(100, ∞)
✓
✓
✓
✓
AgentCF [258]
(100, ∞)
✓
✓
✓
✓
Table 3: A list of representative works of society simulation.

## Page 16

There are three main approaches to determining the compo-
sition of individuals in a system simulating a microcosm of
society.
Some works rely on virtual individual synthesis,
often not focused on alignment with the real world, aim-
ing to ensure that the system includes users with a variety
of attributes, typically by generating virtual individuals with
the help of LLMs or humans [31, 260]. Other works uti-
lize existing datasets, such as MovieLens-1M [256, 257],
to define user composition within a simulated recommenda-
tion platform. Agents are initialized on the basis of the user
information within these datasets, reflecting the distribution
of users in that context. Recently, an increasing number of
studies have focused on real-world distribution replication,
such as the composition of users on social platforms [33]
or the distribution of voters in surveys [227].
For small-
scale individual sets, individual data are typically collected
manually [229, 233].
In cases where large-scale popula-
tions are required or obtaining real data is difficult, individu-
als may be sampled based on real-world macro distributions
or generated by LLMs to match desired attribute distribu-
tion [12, 226, 227].
Trade-off between Simulation Precision and Scale
When
simulating individuals in society simulations, many studies
adopt detailed role modeling to enhance the authenticity of
agent behavior. Beyond common demographic attributes, this
may include factors such as an individual’s past statements
and interaction history [32, 214, 219, 256, 257]. However, as
the number of individuals increases, such fine-grained model-
ing becomes expensive. Consequently, a trade-off often arises
between the precision of individual modeling and the scale of
the simulation. In large-scale simulations, to reduce computa-
tional costs, the details of each agent are typically simplified,
by retaining only the most essential and common characteris-
tics [224, 225] or compressing auxiliary dialogue information
into shared memory [236].
Special Modeling on Outliers
As previously mentioned,
the composition of individuals in society is diverse. However,
not all individuals play an equally significant role. Some in-
dividuals, whose attributes or behaviors significantly deviate
from the majority, are referred to as outliers [259]. Compared
to average individuals, outliers often introduce variability and
unpredictability to society. Examples include celebrities and
opinion leaders [251, 252], who frequently hold prominent
positions within social structures and amplify their influence.
In situations with limited resources, some studies [25] priori-
tize detailed modeling of these core content producers, while
simplifying the modeling for the majority. Meanwhile, in-
tervention policies based on simulation results often focus
on these key nodes in networks [261], aiming to influence
the overall system’s behavior by blocking or interfering with
them.
5.1.2
Network
Social interactions are often conducted through social net-
works, which can be described using graph structures where
nodes represent individuals and edges represent their rela-
tions. The network determines the direction of information
and influence dissemination. In social science, it has been ob-
served that homophily of individuals can increase the likeli-
hood of communication. Highly similar individuals are more
likely to establish connections compared to those with greater
differences [262, 263]. This principle also informs the con-
struction of networks in society simulations. The methods
for constructing social networks vary across different scenar-
ios. Here, we divide them into offline networks and online
networks.
Offline Network
An offline network represents connec-
tions formed through in-person interactions, such as face-to-
face communication or the spread of opinions and diseases
in physical settings. On the one hand, some studies aim to
simulate interactions in virtual worlds, thus determining the
connections between agents in a random or predefined man-
ner [32, 232, 236]. On the other hand, when some studies
aim to simulate the spread of a disease or event information
in the real world, considering the difficulty of obtaining real
data, they often estimate the social relations using external
algorithms or agents themselves [224, 228].
However, in
studies with a large scale of agents, the network relationships
between individuals are sometimes ignored, and individuals
are treated as independent [227]. Alternatively, some studies
provide rough information, such as community statistics, in
place of specific details about the agents’ neighbors [225].
Online Network
An online network is a digital structure
where individuals or entities interact through platforms, such
as online social platforms and recommendation platforms,
forming connections based on activities, relationships, or
shared interests. At the beginning, some studies randomly
initialize the social relations for users existing datasets [256]
or synthesized users [26], while other efforts have focused
on crawling authentic social relationships from social media
platforms like Weibo [248] and Twitter [25]. However, as the
scale of individuals increase, it may be challenging to obtain
all of their authentic relationships. Therefore, some studies
construct networks using a small portion of real relationship
data combined with a large amount of synthetic relationship
data [33], or connect similar users based on the assumption
of homophily [242].
5.1.3
Social Influence
Social influence refers to the influence agents have on others
and the influence they receive from others during interactions.
This is also known as embeddedness in social sciences [259],
which suggests that individuals behavior and decisions are
influenced by their environment. When conducting society
simulations, it is necessary to consider the modeling of such
social influence.
Influence Received by the Influencee
The same informa-
tion may produce different effects when received by individ-
uals with different traits. Currently, most studies have mod-
eled how the influence received by the recipient varies based
on their profile [26, 33, 248]. This can be easily achieved
by integrating the individual’s profile, memory and the infor-
mation received from others into the same context. Building
this, a few works further induce additional mechanisms such
as cognitive bias [24] and reflection on norms [232] to en-
hance agents’ understanding and perception of the received
messages.

## Page 17

Influence Exerted by the Influencer
The same message
conveyed by different individuals can result in varying so-
cial impacts. The Pareto distribution and the Matthew Ef-
fect [25, 256] indicate that information, influence, or attention
tends to concentrate on a small group of individuals who are
already dominant in the community. Therefore, when simu-
lating social interactions, the identity, status, and reputation
of the information sender are also crucial. Some studies start
with real-world data to conduct detailed modeling of opinion
leaders [251, 252]. Other studies, instead of focusing on the
role of the influencer, model the influence exerted by the in-
fluencer by incorporating the relation information such as so-
cial impression memory [236] and share party affiliation [31].
In addition to the influence exerted by individuals, research
has found that as group size increases, the impact of a single
influencer may diminish. However, the influence of the group
on individuals often drives them to align their behavior with
the group, leading to the emergence of the herd effect [33].
5.1.4
Outcomes
Social emergence suggests that the collective behaviors or
phenomena arise from individual interactions are not a linear
sum of individual actions but rather complex patterns emerge
from the interactions [21, 259]. These interaction outcomes
may be measurable macro results, such as voting results and
public opinion levels, or they may also be qualitative social
phenomena and norms. Next, we will discuss these two types
of outcomes separately.
Macro Statistical Results
Macro statistical results are typ-
ically the focus of existing studies, as they are closely re-
lated to predefined research objectives such as market re-
search, election predictions, and public opinion forecasting.
These studies often aim to calculate the sum or average of
the choices or opinions of all agents in the system. To get a
static opinion distribution, some studies overlook the social
interactions and instead directly sum up individual choices to
obtain macro outcomes [96, 227], simplifying the complex-
ity of social dynamics. Another line of research focuses on
the change of indicators by modeling multiple rounds of in-
teractions among the agents over a period of time and then
statistically analyzing the results [27, 215, 218, 248, 249].
Formation of Social Phenomena and Social Norms
In
addition to the quantifiable macro results, some social phe-
nomena and social norms are also important outcomes of so-
cial interactions. On the one hand, some studies have identi-
fied the bubble effect in recommendation systems [257], echo
chambers in social media [25, 33, 245], Matthew effect in
competitive agent interactions [219], and spontaneous coop-
eration of competing agents [218] by calculating additional
metrics or observing the trends of primary indicators. On
the other hand, some studies examine social norms as an im-
portant byproduct of social interactions. This includes sim-
ulating and testing whether community rules can shape de-
sired social norms [247], constructing normative architecture
to observe the emergence of social norms [232], studying how
social media language evolves in the presence of regulatory
constraints [243], and observing changes in social norms in
real-world scenarios such as autonomous driving [264].
5.2
Scenario
Society simulation has been widely applied to various sce-
narios related to human society. These scenarios cover dif-
ferent aspects of daily human life, and existing studies can
be categorized into three primary areas: general economics,
sociology and political science, as well as online platforms.
5.2.1
General Economics
Simulations in general economics analyze decision-making
and behaviors related to resource allocation and competition.
These studies primarily investigate how agents make deci-
sions influenced by economic incentives, market rules and
resource constraints, while also examining how interactions
among groups shape broader economic trends.
Game Theory and Strategic Interactions
Some research
mainly focuses on game theory and strategic interaction.
These scenarios typically involve small groups of agents, with
a primary focus on the complex interactions between agents.
Some works use classic game theory games, such as the Pris-
oner’s Dilemma, to explore agent behavior in game-theoretic
scenarios, including trust behavior [211], logic reasoning
and decision-making [212], rationality and strategic reason-
ing ability [213], cooperation tendencies [214] and how
emotional states can disrupt rational decision-making [217].
Other studies focus on real-world scenarios other than the
games, such as spontaneous cooperation in competitive envi-
ronments [218], complex market behaviors in firm competi-
tion [215], and competition between restaurant and customer
agents [219]. Overall, the former kind of scenarios simpli-
fies the environment, making it easier to conduct controlled
research on agent behavior, while the latter provides more in-
sights for real-world applications.
Economic Contexts
In addition to close studies on game
theory and strategic interactions, some studies focus on the
use of agents and their interactions within economic envi-
ronments. Horton [220] examines economic agents driven
by LLMs in various experiments to replicate human be-
havior in economic scenarios.
EconAgent [27] introduces
agents for macroeconomic simulation, emphasizing the in-
fluence of macroeconomic trends. SRAP-Agent [221] pro-
poses a framework for simulating and optimizing scarce re-
source allocation in economics, specifically in public housing
allocation scenarios. Besides, some studies involve broader
macroeconomic domains, using agents to simulate and pre-
dict the spread of diseases and the change in unemployment
rates [224, 225].
5.2.2
Sociology and Political Science
Society simulation has been widely used in sociological and
political science research. These studies range from small-
scale laboratory experiments that validate theories and hy-
potheses to large-scale social surveys aimed at understanding
public choices. The goal is to leverage agents as substitutes
for humans in studying human behavior within sociological
and political contexts.
Public Opinion Survey
A mainstream application of soci-
ety simulation is public opinion survey, which aims to pre-
dict the perspectives of specific groups toward a given sub-

## Page 18

ject through simulation and aggregate their opinions to sup-
port advanced needs such as election forecasting and public
administration. Argyle et al. [12] first propose that LLMs
could serve as silicon samples of humans, through several
large-scale surveys conducted in the United States. Build-
ing on this, some studies have expanded their focus to sce-
narios of opinion surveys [13, 226, 240], such as election
polls [227] and response to public administration crisis [228],
delving deeper into issues like population complexity and al-
gorithmic bias. Recently, agents have demonstrated the po-
tential to replicate participants’ responses in individual inter-
views [229]. These studies lay the foundation for new tools
to investigate individual and collective behavior.
Individual and Organizational Behavior Observation
Other studies focus on observing individual or organizational
behavior in common or specific settings. Some works do not
specify a particular scenario but instead observe agents’ so-
cial interactions and potential phenomena in daily life within
a sandbox environment [32, 231, 232, 237]. Other studies aim
to validate theories or hypotheses in specific scenarios, such
as the wisdom of partisan crowds [31], information manage-
ment [233], organizational behavior management [238], and
the evolution of personality traits [239].
5.2.3
Online Platform
Online Platforms are a vital component of society simulation,
offering a practical means to study complex social phenom-
ena in digital environments. These platforms, ranging from
social media to online communities, allow agents to simulate
real-world interactions and study dynamics such as opinion
formation, information spread, and collective behaviors.
Social Platforms
Online social platforms have long served
as an important testing ground for studying the propagation
of information and the evolution of opinions. These stud-
ies typically recreate environments similar to popular so-
cial platforms, such as Twitter, Reddit, and Weibo, with ac-
tion spaces that include behaviors like sharing, commenting,
and liking. By simulating these scenarios, researchers can
model the spread of information and track changes in user
attitudes following events, covering a wide range of topics
such as general news, rumors, and the role of opinion leaders
[26, 243, 244, 248, 250, 251]. In such scenarios, the roles
and relationships of agents play a critical role in ensuring
realistic simulations. Initially, many studies relied on real-
world data scraped from platforms to maintain consistency
[25, 248]. However, as the scale of these simulations grew
and data acquisition became more challenging, researchers
began exploring the use of synthetic data [33]. Furthermore,
to accommodate the increasing demand for simulating larger
numbers of agents, some studies have developed large-scale
society simulation platforms [265, 266], employing parallel
processing and other strategies to enhance simulation effi-
ciency.
Recommendation Environments
Another widely studied
scenario is the recommendation environment, where these
works use agents to simulate user responses in order to vali-
date and improve recommendation algorithms [254, 255]. A
key feature across these studies is the use of agents to em-
ulate personalized behaviors such as item selection, prefer-
ences, and emotional responses, often integrating user mem-
ory and contextual factors [256–258].
Additionally, some
approaches incorporate external knowledge or self-reflection
mechanisms, allowing agents to adapt and learn from their
interactions over time [267]. These studies collectively show
how LLMs can bridge the gap between traditional recom-
mender systems and more interactive, human-like behavior
simulations, offering new ways to improve recommendation
accuracy and better understand user dynamics.
5.3
Evaluation
For society simulations, the evaluation primarily focuses on
the comparison between the simulation results and real-world
data, with assessments centered on micro level, macro level
and system level.
Micro-level Evaluation
Individual simulation accuracy is
key to society simulation.
Therefore, micro-level evalua-
tion of society simulation has received widespread atten-
tion.
Initially, evaluations in non-real-world simulations
draw on the Turing test, assessing agent behavior’s resem-
blance to human behavior, often subjectively by humans or
LLMs [32, 236, 268]. For specific scenarios, metrics like
partisan bias and human likeness index are proposed [31].
When simulations target real-world scenarios with available
empirical data, automated metrics like emotion, attitude, be-
havior consistency, and user taste alignment can be designed
for more objective evaluations by comparing simulation con-
tent with real-world data [25, 248, 257].
Macro-level Evaluation
Social interactions often lead to
collective outcomes, so it is important to evaluate whether
macro-level outcomes show patterns and trends that are con-
sistent with the real world. For sociology and online plat-
forms, attention is typically given to whether the scale of
propagation, the distribution and trends of collective opin-
ions and traits align with those of the real world. In addi-
tion to qualitative methods such as subjective evaluation [248,
257], some studies have proposed quantitative metrics, such
as fitted parameters, correlation coefficients and change of
toxicity of community content to measure this differences
objectively [25, 26, 33, 249]. Similarly, in economic sim-
ulation, the evaluation of simulated economic systems de-
pends on whether they can reproduce the most representative
macroeconomic laws [27].
System-level Evaluation
System-level evaluation is con-
cerned with assessing the overall performance of a simula-
tion system, irrespective of the specific content being sim-
ulated. With the growing number of agents in simulation,
the focus of contemporary research has been on system ef-
ficiency and associated costs. Efficiency is assessed through
various metrics, such as the time it takes to run a simulation,
the resources that are utilized during the process, and how
well the simulation can scale with an increasing number of
agents [33, 256, 266]. These metrics are crucial for under-
standing how well the system can handle complexity and the
demands of larger simulations. On the cost side, evaluations
often center on the number of tokens consumed during the
simulation or the financial expenditure incurred [236].

## Page 19

Domain
Dataset
Type
Source
# individual num # dialogue num Paper Link
Characters
Final Dialogue Dataset
Dialogue
Wikipedia
/
22,311
[269] Link
P-weibo Dataset
Dialogue/Description
Weibo
/
2,000,000
[103]
/
P-Ubuntu dialogue corpus
Dialogue/Description
Corpus
/
2,000,000
[103]
/
LISCU Dataset
Description
Books, Summaries
9,499
/
[54]
Link
FoCus Dataset
Description
Wikipedia
/
86,712
[102] Link
ConvAI2 benchmark dataset
Description
Human
/
18,878
[118]
/
HPD Benchmark
Dialogue/Description
Books
1
about 2,500
[55]
Link
LaMP Benchmark
Description
/
/
/
[113] Link
Multimodal Persona Chat
Image/Dialogue
Reddit
/
15,000
[133] Link
LiveChat
Description/Dialogue
Douyin
351
1,330,000
[60]
Link
COMSET
Dialogue
Strips
13
53,903
[58]
Link
ChatHaruhi Dataset
Dialogue
Movies, Script
32
54,000
[59]
Link
RoleBench
Dialogue
Scripts
100
168,093
[28]
Link
Character-LLM Dataset
Description
/
9
14,400
[10]
Link
PersonaChat Dataset
Description
/
/
/
[270] Link
CharacterDial
Description/Dialogue
Literary Resources,LLM ,Human
250
1,034
[62]
Link
Synthetic Persona Chat
Description/Dialogue
LLM
10,371
21,907
[104] Link
RoleEval Dataset
Description
Wikipedia, Baidu, Fandom, Moegirlpedia
300
6,000
[63]
Link
CharacterEval Dataset
Description/Dialogue
Novels,Scripts
77
1,785
[64]
Link
Life Choice Dataset
Description
Books
1,401
/
[66]
/
Cross Dataset
Description
Books
/
/
[67]
Link
MMRole-Data
Description/Dialogue/Image
Wikipedia,Baidu
85
14000
[69]
Link
RP Dataset
Dialogue
Novels,Scripts
331
3552
[70]
Link
MPI dataset
Description
/
/
/
[73]
Link
Demographics
Who is GPT3 Dataset
/
/
/
/
[271] Link
Dataset Movielens 1M
/
/
/
/
[80]
Link
EmotionBench
/
/
/
/
[82]
Link
OpinionQA Dataset
/
Surveys
/
/
[91]
Link
CultureLLM Dataset
Dialogue
Survey
/
/
[94]
Link
PersonaHub Dataset
Description
LLM
200,000
375,000
[98]
Link
Table 4: Summary of commonly used datasets for individual simulation.
6
Datasets and Benchmarks
6.1
Individual Simulation
We summarize commonly used datasets for scenario simu-
lation in Table 4. Datasets for individual simulation can be
classified into two types: description datasets and dialogue
datasets. Description datasets include individual-specific in-
formation, such as life experiences, relationships, and ba-
sic demographic details like career, age, and gender, often
sourced from literature summaries or search engines like
Baidu and Wikipedia. Dialogue datasets consist of single-
turn or multi-turn conversations in specific scenarios, created
by extracting relevant plots for targeted characters or gather-
ing utterances from social media. Some datasets are designed
specifically for evaluation, combining basic personal infor-
mation with customized questions or tasks to assess simula-
tion performance.
6.2
Scenario Simulation
We summarize commonly used datasets for scenario simula-
tion in Table 5, comprising dialog-driven and task-driven sce-
narios. The datasets cover a wide range of formats, including
QA, multiple-choice, rating, code, and game. We observed
that QA and multiple-choice formats dominate the data types,
while domain-specific datasets like judicial, game, and me-
dia prefer to preserve domain-tailored data type. Based on
task complexity, datasets are categorized into three levels:
easy, medium, and hard. Additionally, according to the col-
lection methods, datasets are classified as human-annotated,
real-world, or synthetic.
6.3
Social Simulation
We summarize commonly used datasets or benchmarks for
social simulations in Table 6. In social simulations, datasets
often consist of two parts: those for initialization of agents
and those for evaluation.
Data used for agent initializa-
tion typically contain profiles and potential relations between
agents, to help initialize the simulation settings. In contrast,
datasets for evaluation provide the reference data of behav-
iors of real-world individuals.
These datasets are sourced
in various ways, such as public surveys, existing datasets
like MovieLens and Amazon-Book, and crawling from on-
line platforms like Twitter.
7
Trend of Social Simulations
7.1
Trend of Individual Simulation
Evolving from social science, individual simulation pow-
ered by LLMs has progressed through three distinct stages,
namely coarse simulation, more nuanced simulation, and
situation-oriented simulation, which is depicted in Fig-
ure 5. Since June 2022, researchers started to focus on coarse
simulations, especially for superficial traits like testing the
personalities of LLMs and simulating well-known charac-
ters [81, 137]. After August 2023, the trends shifted towards
more refined simulations of specific individuals, with studies
evaluating the cognitive aspects of simulated models [61, 67]
and improving their simulation capabilities [65, 84]. By May
2024, researchers began conducting individual simulations in
specific scenarios [70, 111], further expanding the complex-
ity and realism of these simulations.

## Page 20

Domain
Datasets
Type
Complexity
# case
Collection
Used by
Data Link
Dialog-
Driven
MiniWob++
Web Interaction
Hard
/
human
[147]
Link
SOTOPIA
Open-Ended Environment
Hard
/
human
[138]
Link
WebQuestions
QA
Easy
5,810
human
[149]
Link
WebQSP
QA
Easy
4,737
human
[149]
Link
CWQ
QA
Easy
34,689
human
[149]
Link
GrailQA
QA
Easy
64,331
human
[149]
Link
Natural Questions
QA
Easy
323,045
human
[147]
Link
FairEval
QA
Medium
80
human
[146]
Link
MMLU
Multiple-Choice
Hard
115,700
real world
[29, 152, 168, 172, 197]
Link
BIG-bench
/
Hard
/
human
[29, 152, 193]
Link
MetaQA
QA
Medium
407,513
real world, human
[149]
Link
AmazonHistoryPrice
Product Info
Hard
930
real world
[148]
Link
MATH
Math Problem
Medium
12,500
real world
[147]
Link
Arithmetic
Math Expression
Easy
/
human
[29]
Link
Counter-Intuitive AR
Reasoning Problem
Easy
200
human
[145]
Link
CommonMT
Translation Triple
Medium
1,200
human
[145]
Link
Overcooked-AI
Game
Medium
/
human
[198]
Link
AVALONBENCH
Game
Easy
/
human
[153]
Link
Jubensha
Game
Medium
1,115
real world
[156]
Link
FanLang-9
Game
Easy
18,800
real world
[158]
Link
WellPlay
QA
Hard
1,482
human
[160]
Link
WWQA
QA
Medium
2,053
synthetic
[159]
Link
Biographies
Biographies
Easy
524
real world
[29]
Link
ALFWorld
Embodied Environment
Medium
3,827
human
[147]
Link
ED dataset
Conversational
Hard
24,850
human
[142]
Link
Topical-Chat
Conversational
Medium
10,784
human
[146]
Link
COPA
Multiple-Choice
Easy
500
real world
[144]
Link
αNLI
Multiple-Choice
Easy
1,507
human
[144]
Link
CSQA
Multiple-Choice
Easy
1,221
human
[144]
Link
Social IQa
Multiple-Choice
Easy
1,935
human
[144]
Link
PIQA
Multiple-Choice
Easy
1,838
human
[144, 197]
Link
StrategyQA
Multiple-Choice
Easy
2,290
human
[144]
Link
e-CARE
Multiple-Choice
Easy
2,122
human
[144]
Link
Task-
Driven
WiKiTQ
QA
Easy
22,033
real world
[174]
Link
TabFact
QA
Hard
118,275
real world, human
[174]
Link
FeTaQA
QA
Hard
10,330
real world, human
[174]
Link
HumanEval
Code
Easy
164
real world
[17, 172, 176, 193]
Link
MBPP
Code
Easy
974
real world
[17, 176]
Link
APPS
Code
Easy
/
real world
[176]
Link
Code
Conversational
Hard
50,000
synthetic
[188]
Link
CoderEval
Code
Medium
230
real world
[176]
Link
SRDD
Software Requirement
Medium
1,200
synthetic
[172, 177, 178, 180]
Link
SoftwareDev
Task Prompt
Hard
70
human
[17]
Link
SWE-bench
Code
Easy
2,294
real world
[179]
Link
AI Society
Conversational
Easy
25,000
synthetic
[188]
Link
SynthPAI
Comment
Hard
7,823
synthetic
[48]
Link
ScienceWorld
Interactive Environment
Hard
/
human
[189]
Link
Science
QA
Medium
60,000
synthetic
[188]
Link
TriviaQA
QA
Easy
650,000
real world
[195]
Link
MT-bench
QA
Medium
80
human
[195]
Link
RoCoBench-Text
QA
Medium
269
human
[192]
Link
PubMedQA
QA
Medium
273,500
human, synthetic
[168]
Link
MedQA
Multiple-Choice
Medium
61,097
real world
[168, 175]
Link
DDXPlus
Medical Record
Hard
1,300,000
synthetic
[166]
Link
MedMCQA
Multiple-Choice
Hard
194,000
real world
[168]
Link
MVME
Medical Record
Medium
506
real world
[19]
Link
ARIES
Review Comment
Easy
3,900
human, synthetic
[30]
Link
Reviewer2
Review
Easy
99,727
human, synthetic
[169]
Link
GSM8K
Math Problem
Easy
8,500
human
[29, 184]
Link
MGSM
Math Problem
Hard
2,750
human
[193]
Link
Math
QA
Hard
50,000
synthetic
[152, 188]
Link
SimuCourt
Legal Cases
Medium
420
real world
[20]
Link
KINLED
Conversational
Medium
10,546
human, synthetic
[186]
Link
Supreme Court Database
Legal Cases
Easy
9,095
real world
[181]
Link
TDW-MAT
Embodied Environment
Medium
/
human
[191]
Link
C-WAH
Embodied Environment
Medium
/
human
[191]
Link
RoCoBench
Embodied Environment
Medium
/
human
[192]
Link
FED
Dialogue Response
Medium
4,712
human
[193]
Link
CulturePark
Conversational
Medium
41,000
synthetic
[50]
Link
CommonGen-Hard
Concept
Easy
200
human
[172, 193]
Link
ARC Challenge
Multiple-Choice
Easy
2,590
human
[197]
Link
HellaSwag
Multiple-Choice
Easy
70,000
synthetic
[197]
Link
UCF101
Video Clip
Medium
7,000
human
[173]
Link
HMDB51
Video Clip
Medium
13,320
real world
[173]
Link
Table 5: Summary of commonly used datasets for scenario simulation.

## Page 21

Scenario
Dataset
Init. Eval.
Content
# case
Simulation Objectives
Used by
Data Link
General
Economics
2018 U.S. population
✓
profile
100 people
macroeconomic activities
[27]
Link
public government data
✓
rent information
51 users
resource allocation
[221]
Link
names-dataset 3.1.0
✓
profile
1,000 people
epidemic modeling
[224]
Link
big-five-data
✓
profile
1,000 people
epidemic modeling
[224]
Link
American Community Survey
✓
profile
8.4M people
epidemic modeling
[225]
Link
Bureau of Labor Statistics
✓
labor statistics
8.4M people
unemployment rate
[225]
Link
CDC
✓
infection rate
8.4M people
epidemic modeling
[225]
Link
Sociology
and
Political Science
ANES
✓
✓
profile,answer
15,626 responses
voting
[12, 96, 227]
Link
Pigeonholing Partisans
✓
✓
profile,answer
2,107 responses
partisan bias
[12]
Link
Global Warming
✓
✓
profile,answer
2,310 responses
opinion
[226]
/
Twitter
✓
statements
1,006,517 users
voting
[227]
/
Interview
✓
✓
profile,answer
1,002 users
opnion and behavior
[229]
Link
Name
✓
name
500 names
/
[230]
Link
Ultimatum Game
✓
money allocation
10,000 pairs
money allocation
[230]
Link
Garden Path Sentences
✓
garden path sentences
96 sentences
language parsing
[230]
Link
Wisdom of Crowds
✓
answers to questions
15,000 answers
wisdom of crowds
[230]
Link
Milgram Shock Experiment
✓
behavior records
100 people
obedience behavior
[230]
Link
15 Topics
✓
profile, opinion
10 users
opinion dynamics
[24]
Link
Formative Study
✓
✓
profile, interview
14 users
information
management
[233]
/
User Study
✓
✓
profile, interview
36 users
information
management
[233]
/
collective decision-making
✓
✓
profile, opinion
2,290 users
collective
decision-making
[234]
/
Becker-2019
✓
✓
profile, answers
1,120 users
wisdom of crowds
[31]
Link
Controversial Beliefs Survey
✓
✓
profile, opinion
564 users
opinion
[240]
/
Online
Platforms
FPS
✓
/
6 topics
opinion dynamics
[26]
/
Echo Chambers
✓
profile
3 networks
opinion polarization
[245]
/
Gender Discrimination
✓
✓
profile, opinion
8,563 users
opinion dynamics
[248]
/
Nuclear Energy
✓
✓
profile, opinion
17,945 users
opinion dynamics
[248]
/
ANES
✓
profile
500 users
partisan bias
[249]
Link
SAGraph
✓
✓
profile, interaction
40 300 influencers
influencer selection
[251]
/
Metoo
✓
✓
profile, opinion
1,000 users
opinion dynamics
[25]
Link
Roe
✓
✓
profile, opinion
1,000 users
opinion dynamics
[25]
Link
BLM
✓
✓
profile, opinion
1,000 users
opinion dynamics
[25]
Link
Twitter15
✓
✓
profile, behavior
198 news
rumor propagation
[33]
Link
Twitter16
✓
✓
profile, behavior
198 news
rumor propagation
[33]
Link
Reddit
✓
✓
profile, comment
116,932 comments
herd effect
[33]
/
MindEcho
✓
✓
profile, comment
14 KOL
key opinion leader
[252]
/
WARRIORS
✓
✓
profile,
search behavior
100,000 users
search behavior
[253]
/
Amazon Beauty
✓
✓
profile,
user-item interaction
15,577 users
user-item
interaction
[254]
Link
Steam
✓
✓
profile,
user-item interaction
281,205 users
user-item
interaction
[254, 257]
Link
MovieLens
✓
✓
profile,
user-item interaction
298,074 users
user-item
interaction
[254, 256, 257]
Link
Amazon Book
✓
✓
profile,
user-item interaction
/
user-item
interaction
[257]
Link
Amazon Review CD
✓
✓
profile,
user-item interaction
100 users
user-item
interaction
[258]
Link
Amazon Review Office
✓
✓
profile,
user-item interaction
100 users
user-item
interaction
[258]
Link
Table 6: Summary of commonly used datasets for society simulation. Init. means the data provides profile to initialize agents, and Eval.
means it provides data to validate the simulation effectiveness.

## Page 22

Jun. 2022
Aug. 2023
Apr. 2024
Coarse Simulation on
Superficial Features
Individual Simulation
More Nuanced Simulation on
Specific Characters
Situation-oriented
Simulation
Out of one, many [12]
Improving Personality Consistency [74]
The wall street neophyte [76]
Conversational Health Agents [84]
Chain of Empathy [89]
CultureLLM [94]
Faithful Persona-based Conversational Dataset [104]
Interactive Agents [100]
HIRPF [123]
Large Language Models Meet Harry Potter [55]
Creating a Large Language Model of a Philosopher [56]
LiveChat [60]
RoleLLM [28]
CharacterLLM [10]
InCharacter [61]
CharacterGLM [62]
Neeko [65]
Character is Destiny [66]
Evaluating Character Understanding [67]
Capturing Minds, Not Just Words [68]
MMRole [69]
Beyond Dialogue [70]
From Role-Play to Drama-Interaction [105]
Social Bench [111]
Demographic
Persona
Charactcer
Persona
Year
Figure 5: Illustration of individual simulation trend, which goes through coarse simulation, more nuanced simulation, and situation-oriented
simulation.
Jan. 2023
Jun. 2023
Feb. 2024
Simple Scenario
Scenario Simulation
Multi-Stage Scenario
Collaborative Scenario
Improving factuality and reasoning [29]
ChatLLM [49]
ICL-AIF [143]
FORD [144]
GITM [161]
MetaGPT [17]
Empirical Study on Werewolf [150]
Recon [151]
MachineSoM [152]
AvalonBench [153]
Self-Emotion [141]
DoG [149]
S-Agents [164]
AgentSense [205]
DERA [175]
Self-collaboration [176]
Blind Judgement [181]
CAMEL [188]
VIDS [165]
ChatDev [177]
TradingGPT [182]
Multi-Agent Collaboration [190]
CoELA [191]
RoCo [192]
AI Hospital [19]
MATHVC [184]
TWOSOME [197]
ReAd [198]
AGA [236]
Dialog-Driven
Scenario
Task-Driven
Scenario
Year
Figure 6: Illustration of scenario simulation trend, which goes through simple scenario, multi-stage scenario, and collaborative scenario.
7.1.1
Coarse Simulation on Superficial Features
Many individual simulation works born since June 2022,
the majority of which initially focus on simulating superfi-
cial features implied in human behaviors. A significant por-
tion of the effort was dedicated to collecting and standard-
izing character-related information to build persona-based
datasets [55, 56]. Additionally, eliciting the underlying de-
mographic personalities of prevailing LLMs posed a chal-
lenge in this early stage [81, 120]. The early trials on coarse
individual simulations shed light on LLMs’ attributes dur-
ing simulation, including hallucinations, inherent biases, and
stereotypes, which are proven to be crucial for future simula-
tions.
7.1.2
More Nuanced Simulation on Specific Characters
As individual simulation methods advanced, the precision of
simulations significantly improved. More nuanced aspects of
the individual simulation gained growing attention.
Some
works implement new functionalities and refine the mod-
els’ architecture, such as incorporating memory and plan-
ning modules [66, 84], while others focus on designing spe-
cific tasks for training and evaluation, like multi-dimensional
interviews [61] and simulation with rich information from
scene descriptions and experiential memories [28].
7.1.3
Situation-Oriented Simulation
Situation-oriented individual simulations begin within game
environments [119], where LLMs are required to make ap-
propriate decisions based on predefined rules. In more com-
plex environments, simulated individuals are supposed to in-
teract dynamically with their surroundings, responding to
real-time environmental feedback [100, 111]. Beyond tra-
ditional simulations like dialogue, situation-oriented simula-
tions expand into areas such as dramatic performances [105],

## Page 23

Mar. 2023
Jun. 2023
Feb. 2024
Constructing Preliminary
Environments
Society Simulation
Exploring Alignment on
Specific Scenarios
Scaling up and towards
Multi-Modal
Year
General Economics
Online Platform
Sociology and Politics
Epidemic Modeling [224]
Choicemates [233]
EconAgent [27]
Personality Traits [239]
Prisoner's Dilemma [214]
Holacracy view [277]
Social Simulacra [247]
RecAgent [256]
S^3 [248]
AgentCF [258]
Agent4Rec [257]
News Feed [249]
HiSim [25]
FPS [26]
Influencer Selection [251]
AgentTorch [225]
OASIS [33]
Generative Agents [57]
AgentSims [199]
WarAgent [47]
Wisdom of Partisan Crowds [31]
Public Administration Crisis [228]
CRSEC [232]
Instruments of Power [13]
Beyond Demographics [240]
ElectionSim [227]
Figure 7: Illustration of society simulation trend, which goes through three stages: constructing preliminary environments, exploring
alignment on specific scenarios, and scaling up while moving towards multi-modal.
digital game exploration [109], and 3D task execution [107].
As the complexity of these simulations grows, the demands
on the underlying architecture grow as well.
7.2
Trend of Scenario Simulation
The development of scenario simulation has progressed
through several distinct stages. Starting from January 2023,
different researches focused primarily on simple scenarios
concerning single objectives and facilitated basic contextual
interactions [144, 175, 181, 188]. By June 2023, the empha-
sis changed to multi-stage scenarios, incorporating multi-step
tasks that enabled agents to engage in sequential decision-
making and adaptive responses across varied contexts to
achieve the more complex goal [165, 182, 190, 192].
By
February 2024, research has increasingly focused on multi-
agent collaborative scenarios, emphasizing agents’ capabili-
ties to cooperate and adapt within complex, high-order simu-
lations [149, 164, 184, 236].
7.2.1
Simple Scenario
In the initial phase of scenario simulation, researchers fo-
cused on constructing simple scenarios that supported foun-
dational agent interactions. Much of this work concentrated
on dialogue-driven decision-making frameworks, which fa-
cilitated structured information exchange and agent align-
ment [49, 175, 188]. Additionally, studies explored the col-
laborative potentials of agents through multi-agent debate
frameworks, employing debate and critical feedback to as-
sess cooperative reasoning and performance enhancement in
LLMs [29, 143, 144]. Simultaneously, other studies applied
scenario simulations within specific domains—such as law,
software development, scientific analysis, and recommen-
dation systems—demonstrating the versatility of task-based
simulations in achieving domain-specific objectives [161,
176, 181].
7.2.2
Multi-Stage Scenario
Different from simple task-oriented scenarios, multi-stage
scenarios are no longer limited to mere agent interactions. In-
stead, they emphasize the fine-grained construction of scenar-
ios. This stage introduces multiple roles and task decompo-
sition as central elements, enabling agents to collaborate not
merely on single tasks but through incremental task break-
downs that require coordinated effort [191, 192]. In software
development, [17, 177] decomposed the development pro-
cess into multiple stages like design, coding and testing to
enhance the capacity for achieving complex objectives and
improving software quality.
Additionally, communication
games were introduced to investigate human behavior within
complex conversational scenarios, adding depth to interaction
analysis [150–153].
7.2.3
Collaborative Scenario
With the growing interest in scenario simulation, research
shifted toward collaborative scenarios, emphasizing advanced
social dynamics and cooperative strategies in agent interac-
tions. [197, 198] introduce reinforcement learning to align
LLM with embodied environments. To build efficient sce-
nario simulations, [236] focused on reducing LLM infer-
ence costs by modeling social relationships while [164] uti-
lized dynamic “agent trees” in environments like Minecraft,
enabling asynchronous task execution for efficient resource
gathering. In addition, [19, 141] simulated collaborative en-
vironments in the real world, reflecting complex social in-
teractions such as medical processes and the development of
social skills, with agents handling evolving multistep tasks.
7.3
Trend of Society Simulation
Since the concept of social simulation was first introduced by
Park et al. [247], numerous notable studies have emerged.
Broadly, the development of this field can be categorized into
three phases. Prior to June 2023, researchers concentrated
on constructing preliminary environments [32, 199, 224]. By
February 2024, the focus shifted toward exploring alignment

## Page 24

within specific scenarios, such as persona modeling and tar-
geted environments, marking the first significant surge of
publications [27, 248, 272].
Most recently, the trend has
moved towards scaling up and incorporating multi-modal ap-
proaches.
In this phase, large-scale precise modeling has
gained recognition, with other modalities such as vision and
voice being integrated into simulations [25, 158, 232, 273].
The main characteristics can be summarized as:
7.3.1
Constructing Preliminary Environments
The complexity of society simulation, to a certain extent,
stems from the complexity of the environment involved. So-
ciety simulation usually involve multiple interacting individ-
uals (such as people, organizations, groups, etc.), which act
in a specific environment (such as cities, markets, cyberspace,
etc.). Therefore, the pioneer work focuses on how to design a
specific environment to support society simulation. [32] built
an interactive sandbox environment by extending a LLM to
store a complete record of an agent’s experience and dynam-
ically synthesizing memory to plan behavior. [224] built an
epidemic spread simulation environment that simulates hu-
man behavior at the individual level to reproduce the spread
of an epidemic in a simulated environment. [199] created
an easy-to-use infrastructure that allows researchers to build
evaluation tasks by adding agents and buildings, providing a
visual and program-based platform for testing LLMs.
7.3.2
Exploring Alignment on Specific Scenarios
With the development of simulation environment technology,
society simulation has basically become operational. At this
time, to test the credibility of simulation, evaluating the align-
ment performance of agents with real situations on specific
tasks has gradually become an important research direction.
[248] use real social network data to measure the accuracy of
simulation by evaluating the behavior and decision-making
of agents at the individual and group levels in a simulated
social network environment. [27] evaluate the decision ra-
tionality of LLM agents by simulating macroeconomic ac-
tivities and comparing the performance of LLM agents with
traditional rule-based agents or language agents in generat-
ing classic macroeconomic phenomena such as inflation and
unemployment.
7.3.3
Scaling Up and towards Multi-Modal
Scaling up
Before LLM-based agents became widely
adopted for society simulation, researchers predominantly re-
lied on agent-based modeling (ABM) methods, where agents
were typically programmed to react based on predefined al-
gorithms. With the advent of LLM providing glimpses of
human-like intelligence [274], LLM-based agents entered the
spotlight. Given the good performance of LLM-based agents
in a series of specific scenarios, researchers began to expand
the scale of simulation. [25, 232] involve the core elements
of large-scale society simulation and study the interaction be-
tween agents and the generation of behavioral norms. [158]
proposed a proving ground for assessing advanced reasoning
capabilities of LLM agents in a large-scale society simulation
context.
Multi-Modal
With the development of language models,
using language agents for society simulation has become a
hot topic in research. It incorporates other modal information
elements such as vision in life into the simulation through text
descriptions. However, with a series of advances in the field
of Vision-Language Model(VLM) [36, 275, 276], researchers
began to incorporate VLM-based agents into society simu-
lation research. [273] provide rich multi-modal interaction
information and detailed annotations in large-scale scenar-
ios. [237] focus on simulating the perceptual limitations and
physical demands of the real world to facilitate more realistic
social interactions.
8
Conclusion
In this paper, we categorize LLM-driven social simulations
into three types: individual, scenario, and society simula-
tion, highlighting their progression from modeling individ-
ual behaviors to replicating complex social dynamics. By
systematically reviewing architectures, methods, and evalu-
ations across these categories, we provide a structured frame-
work for advancing research in this field. This work aims to
guide the development of LLM-based simulations and foster
interdisciplinary studies to address real-world challenges and
support decision-making.
References
[1]
Mark S Granovetter. The strength of weak ties. Amer-
ican journal of sociology, 78(6):1360–1380, 1973.
[2]
Daniel Katz and Robert Kahn. The social psychology
of organizations. In Organizational behavior 2, pages
152–168. Routledge, 2015.
[3]
SE ASCH. Effects of group pressure upon the mod-
ification and distortion of judgments. Groups, Lead-
ership and Men: Research in Human Relations, page
177, 1951.
[4]
Stanley Milgram. Behavioral study of obedience. The
Journal of abnormal and social psychology, 67(4):371,
1963.
[5]
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou,
et al. Chain-of-thought prompting elicits reasoning in
large language models. Advances in neural informa-
tion processing systems, 35:24824–24837, 2022.
[6]
Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yu-
taka Matsuo, and Yusuke Iwasawa.
Large language
models are zero-shot reasoners. Advances in neural in-
formation processing systems, 35:22199–22213, 2022.
[7]
Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yi-
wen Ding, Boyang Hong, Ming Zhang, Junzhe Wang,
Senjie Jin, Enyu Zhou, et al. The rise and potential of
large language model based agents: A survey. arXiv
preprint arXiv:2309.07864, 2023.
[8]
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran,
Tom Griffiths, Yuan Cao, and Karthik Narasimhan.
Tree of thoughts: Deliberate problem solving with
large language models. Advances in Neural Informa-
tion Processing Systems, 36, 2024.

## Page 25

[9]
Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang,
Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang,
Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei,
and Jirong Wen. A survey on large language model
based autonomous agents. Frontiers of Computer Sci-
ence, 18(6), March 2024.
[10]
Yunfan Shao, Linyang Li, Junqi Dai, and Xipeng
Qiu. Character-llm: A trainable agent for role-playing,
2023.
[11]
Jiangjie Chen, Xintao Wang, Rui Xu, Siyu Yuan, Yikai
Zhang, Wei Shi, Jian Xie, Shuang Li, Ruihan Yang,
Tinghui Zhu, et al. From persona to personalization: A
survey on role-playing language agents. arXiv preprint
arXiv:2404.18231, 2024.
[12]
Lisa P. Argyle,
Ethan C. Busby,
Nancy Fulda,
Joshua R. Gubler, Christopher Rytting, and David
Wingate.
Out of one, many: Using language mod-
els to simulate human samples.
Political Analysis,
31(3):337–351, February 2023.
[13]
Yaqub Chaudhary and Jonnie Penn. Large language
models as instruments of power: New regimes of au-
tonomous manipulation and control.
arXiv preprint
arXiv:2405.03813, 2024.
[14]
Taicheng Guo, Xiuying Chen, Yaqi Wang, Ruidi
Chang, Shichao Pei, Nitesh V Chawla, Olaf Wiest, and
Xiangliang Zhang. Large language model based multi-
agents: A survey of progress and challenges. arXiv
preprint arXiv:2402.01680, 2024.
[15]
Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jing-
tao Ding, Zhilun Zhou, Fengli Xu, and Yong Li. Large
language models empowered agent-based modeling
and simulation: A survey and perspectives. Humani-
ties and Social Sciences Communications, 11(1):1–24,
2024.
[16]
Chen Qian, Xin Cong, Wei Liu, Cheng Yang, Weize
Chen, Yusheng Su, Yufan Dang, Jiahao Li, Juyuan Xu,
Dahai Li, et al. Communicative agents for software
development. arXiv preprint arXiv:2307.07924, 2023.
[17]
Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng
Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven
Ka Shing Yau, Zijuan Lin, Liyang Zhou, et al.
Metagpt: Meta programming for multi-agent collab-
orative framework. arXiv preprint arXiv:2308.00352,
2023.
[18]
Junkai Li, Siyu Wang, Meng Zhang, Weitao Li,
Yunghwei Lai, Xinhui Kang, Weizhi Ma, and Yang
Liu.
Agent hospital:
A simulacrum of hospi-
tal with evolvable medical agents.
arXiv preprint
arXiv:2405.02957, 2024.
[19]
Zhihao Fan, Jialong Tang, Wei Chen, Siyuan Wang,
Zhongyu Wei, Jun Xi, Fei Huang, and Jingren Zhou.
Ai hospital: Interactive evaluation and collaboration
of llms as intern doctors for clinical diagnosis. arXiv
preprint arXiv:2402.09742, 2024.
[20]
Zhitao He, Pengfei Cao, Chenhao Wang, Zhuoran Jin,
Yubo Chen, Jiexin Xu, Huaijun Li, Xiaojian Jiang,
Kang Liu, and Jun Zhao.
Simucourt: Building ju-
dicial decision-making agents with real-world judge-
ment documents.
arXiv preprint arXiv:2403.02959,
2024.
[21]
Thomas C Schelling.
Dynamic models of segrega-
tion.
Journal of mathematical sociology, 1(2):143–
186, 1971.
[22]
Rainer Hegselmann and Ulrich Krause. Opinion dy-
namics driven by various ways of averaging. Compu-
tational Economics, 25:381–405, 2005.
[23]
Yun-Shiuan Chuang and Timothy T Rogers. Computa-
tional agent-based models in opinion dynamics: A sur-
vey on social simulations and empirical studies. arXiv
preprint arXiv:2306.03446, 2023.
[24]
Yun-Shiuan Chuang, Agam Goyal, Nikunj Harlalka,
Siddharth Suresh, Robert Hawkins, Sijia Yang, Dha-
van Shah, Junjie Hu, and Timothy T Rogers. Simu-
lating opinion dynamics with networks of llm-based
agents. arXiv preprint arXiv:2311.09618, 2023.
[25]
Xinyi Mou, Zhongyu Wei, and Xuanjing Huang. Un-
veiling the truth and facilitating change:
Towards
agent-based large-scale social movement simulation.
arXiv preprint arXiv:2402.16333, 2024.
[26]
Yuhan Liu, Xiuying Chen, Xiaoqing Zhang, Xing Gao,
Ji Zhang, and Rui Yan.
From skepticism to accep-
tance: Simulating the attitude dynamics toward fake
news. arXiv preprint arXiv:2403.09498, 2024.
[27]
N. Li, C. Gao, M. Li, et al. Econagent: Large language
model-empowered agents for simulating macroeco-
nomic activities. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Linguis-
tics (Volume 1: Long Papers), pages 15523–15536,
2024.
[28]
Zekun Moore Wang,
Zhongyuan Peng,
Haoran
Que, Jiaheng Liu, Wangchunshu Zhou, Yuhan Wu,
Hongcheng Guo, Ruitong Gan, Zehao Ni, Jian Yang,
Man Zhang, Zhaoxiang Zhang, Wanli Ouyang, Ke Xu,
Stephen W. Huang, Jie Fu, and Junran Peng. Rolellm:
Benchmarking, eliciting, and enhancing role-playing
abilities of large language models, 2024.
[29]
Yilun Du, Shuang Li, Antonio Torralba, Joshua B
Tenenbaum, and Igor Mordatch. Improving factuality
and reasoning in language models through multiagent
debate. arXiv preprint arXiv:2305.14325, 2023.
[30]
Mike D’Arcy, Tom Hope, Larry Birnbaum, and Doug
Downey. Marg: Multi-agent review generation for sci-
entific papers. arXiv preprint arXiv:2401.04259, 2024.
[31]
Yun-Shiuan Chuang,
Nikunj Harlalka,
Siddharth
Suresh, Agam Goyal, Robert Hawkins, Sijia Yang,
Dhavan Shah, Junjie Hu, and Timothy T Rogers. The
wisdom of partisan crowds: Comparing collective in-
telligence in humans and llm-based agents.
In Pro-
ceedings of the Annual Meeting of the Cognitive Sci-
ence Society, volume 46, 2024.

## Page 26

[32]
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai,
Meredith Ringel Morris, Percy Liang, and Michael S
Bernstein. Generative agents: Interactive simulacra of
human behavior. In Proceedings of the 36th annual
acm symposium on user interface software and tech-
nology, pages 1–22, 2023.
[33]
Ziyi Yang, Zaibin Zhang, Zirui Zheng, Yuxian Jiang,
Ziyue Gan, Zhiyu Wang, Zijian Ling, Jinsong Chen,
Martz Ma, Bowen Dong, et al. Oasis: Open agents
social interaction simulations on one million agents.
arXiv preprint arXiv:2411.11581, 2024.
[34]
Junwei Liu, Kaixin Wang, Yixuan Chen, Xin Peng,
Zhenpeng Chen, Lingming Zhang, and Yiling Lou.
Large language model-based agents for software engi-
neering: A survey. arXiv preprint arXiv:2409.02977,
2024.
[35]
Tom B Brown. Language models are few-shot learn-
ers. arXiv preprint arXiv:2005.14165, 2020.
[36]
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo
Almeida, Janko Altenschmidt, Sam Altman, Shyamal
Anadkat, et al. Gpt-4 technical report. arXiv preprint
arXiv:2303.08774, 2023.
[37]
Kevin A Fischer. Reflective linguistic programming
(rlp):
A stepping stone in socially-aware agi (so-
cialagi). arXiv preprint arXiv:2305.12647, 2023.
[38]
Lei Wang, Jingsen Zhang, Hao Yang, Zhiyuan Chen,
Jiakai Tang, Zeyu Zhang, Xu Chen, Yankai Lin, Rui-
hua Song, Wayne Xin Zhao, et al. User behavior sim-
ulation with large language model based agents. arXiv
preprint arXiv:2306.02552, 2023.
[39]
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik Narasimhan, and Yuan Cao. React:
Synergizing reasoning and acting in language models.
arXiv preprint arXiv:2210.03629, 2022.
[40]
Shibo Hao, Yi Gu, Haodi Ma, Joshua Jiahua Hong,
Zhen Wang, Daisy Zhe Wang, and Zhiting Hu. Rea-
soning with language model is planning with world
model. arXiv preprint arXiv:2305.14992, 2023.
[41]
Aaron Parisi, Yao Zhao, and Noah Fiedel.
Talm:
Tool augmented language models.
arXiv preprint
arXiv:2205.12255, 2022.
[42]
Timo Schick,
Jane Dwivedi-Yu,
Roberto Dess`ı,
Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke
Zettlemoyer, Nicola Cancedda, and Thomas Scialom.
Toolformer: Language models can teach themselves to
use tools. Advances in Neural Information Processing
Systems, 36, 2024.
[43]
Noah Shinn, Federico Cassano, Ashwin Gopinath,
Karthik Narasimhan, and Shunyu Yao.
Reflexion:
Language agents with verbal reinforcement learning.
Advances in Neural Information Processing Systems,
36, 2024.
[44]
Chenxu Hu, Jie Fu, Chenzhuang Du, Simian Luo,
Junbo Zhao, and Hang Zhao. Chatdb: Augmenting
llms with databases as their symbolic memory. arXiv
preprint arXiv:2306.03901, 2023.
[45]
Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye,
and Yanlin Wang. Memorybank: Enhancing large lan-
guage models with long-term memory. In Proceedings
of the AAAI Conference on Artificial Intelligence, vol-
ume 38/17, pages 19724–19731, 2024.
[46]
Jingqing Ruan, Yihong Chen, Bin Zhang, Zhiwei Xu,
Tianpeng Bao, Guoqing Du, Shiwei Shi, Hangyu Mao,
Ziyue Li, Xingyu Zeng, et al. Tptu: large language
model-based ai agents for task planning and tool usage.
arXiv preprint arXiv:2308.03427, 2023.
[47]
Wenyue Hua, Lizhou Fan, Lingyao Li, Kai Mei, Jian-
chao Ji, Yingqiang Ge, Libby Hemphill, and Yongfeng
Zhang.
War and peace (waragent): Large language
model-based multi-agent simulation of world wars.
arXiv preprint arXiv:2311.17227, 2023.
[48]
Chen Qian,
Zihao Xie,
Yifei Wang,
Wei Liu,
Yufan Dang, Zhuoyun Du, Weize Chen, Cheng
Yang, Zhiyuan Liu, and Maosong Sun.
Scal-
ing large-language-model-based multi-agent collabo-
ration. arXiv preprint arXiv:2406.07155, 2024.
[49]
Rui Hao, Linmei Hu, Weijian Qi, Qingliu Wu,
Yirui Zhang, and Liqiang Nie.
Chatllm network:
More brains, more intelligence.
arXiv preprint
arXiv:2304.12998, 2023.
[50]
Cheng Li, Damien Teney, Linyi Yang, Qingsong Wen,
Xing Xie, and Jindong Wang. Culturepark: Boosting
cross-cultural understanding in large language models.
arXiv preprint arXiv:2405.15145, 2024.
[51]
Weize Chen, Chenfei Yuan, Jiarui Yuan, Yusheng
Su, Chen Qian, Cheng Yang, Ruobing Xie, Zhiyuan
Liu,
and Maosong Sun.
Beyond natural lan-
guage: Llms leveraging alternative formats for en-
hanced reasoning and communication. arXiv preprint
arXiv:2402.18439, 2024.
[52]
Chau Pham, Boyi Liu, Yingxiang Yang, Zhengyu
Chen, Tianyi Liu, Jianbo Yuan, Bryan A Plummer,
Zhaoran Wang, and Hongxia Yang. Let models speak
ciphers: Multiagent debate through embeddings. In
The Twelfth International Conference on Learning
Representations, 2024.
[53]
Samuele Marro, Emanuele La Malfa, Jesse Wright,
Guohao Li, Nigel Shadbolt, Michael Wooldridge, and
Philip Torr.
A scalable communication protocol for
networks of large language models.
arXiv preprint
arXiv:2410.11905, 2024.
[54]
Faeze Brahman, Meng Huang, Oyvind Tafjord, Chao
Zhao, Mrinmaya Sachan, and Snigdha Chaturvedi.
”let your characters tell their story”: A dataset for
character-centric narrative understanding, 2021.
[55]
Nuo Chen, Yan Wang, Haiyun Jiang, Deng Cai, Yuhan
Li, Ziyang Chen, Longyue Wang, and Jia Li. Large
language models meet harry potter: A bilingual dataset
for aligning dialogue agents with characters, 2023.

## Page 27

[56]
Eric Schwitzgebel, David Schwitzgebel, and Anna
Strasser. Creating a large language model of a philoso-
pher, 2023.
[57]
Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai,
Meredith Ringel Morris, Percy Liang, and Michael S.
Bernstein. Generative agents: Interactive simulacra of
human behavior, 2023.
[58]
Harsh Agrawal, Aditya Mishra, Manish Gupta, and
Mausam.
Multimodal persona based generation of
comic dialogs. In Anna Rogers, Jordan Boyd-Graber,
and Naoaki Okazaki, editors, Proceedings of the 61st
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 14150–
14164, Toronto, Canada, July 2023. Association for
Computational Linguistics.
[59]
Cheng Li, Ziang Leng, Chenxi Yan, Junyi Shen, Hao
Wang, Weishi MI, Yaying Fei, Xiaoyang Feng, Song
Yan, HaoSheng Wang, Linkang Zhan, Yaokai Jia,
Pingyu Wu, and Haozhen Sun. Chatharuhi: Reviving
anime character in reality via large language model,
2023.
[60]
Jingsheng Gao, Yixin Lian, Ziyi Zhou, Yuzhuo Fu, and
Baoyuan Wang. Livechat: A large-scale personalized
dialogue dataset automatically constructed from live
streaming, 2023.
[61]
Xintao Wang, Yunze Xiao, Jen tse Huang, Siyu Yuan,
Rui Xu, Haoran Guo, Quan Tu, Yaying Fei, Ziang
Leng, Wei Wang, Jiangjie Chen, Cheng Li, and
Yanghua Xiao. Incharacter: Evaluating personality fi-
delity in role-playing agents through psychological in-
terviews, 2024.
[62]
Jinfeng Zhou, Zhuang Chen, Dazhen Wan, Bosi Wen,
Yi Song, Jifan Yu, Yongkang Huang, Libiao Peng,
Jiaming Yang, Xiyao Xiao, Sahand Sabour, Xiaohan
Zhang, Wenjing Hou, Yijia Zhang, Yuxiao Dong, Jie
Tang, and Minlie Huang.
Characterglm: Customiz-
ing chinese conversational ai characters with large lan-
guage models, 2023.
[63]
Tianhao Shen, Sun Li, Quan Tu, and Deyi Xiong.
Roleeval: A bilingual role evaluation benchmark for
large language models, 2024.
[64]
Quan Tu, Shilong Fan, Zihang Tian, and Rui Yan.
Charactereval: A chinese benchmark for role-playing
conversational agent evaluation, 2024.
[65]
Xiaoyan Yu, Tongxu Luo, Yifan Wei, Fangyu Lei,
Yiming Huang, Hao Peng, and Liehuang Zhu. Neeko:
Leveraging dynamic lora for efficient multi-character
role-playing agent, 2024.
[66]
Rui Xu, Xintao Wang, Jiangjie Chen, Siyu Yuan, Xin-
feng Yuan, Jiaqing Liang, Zulong Chen, Xiaoqing
Dong, and Yanghua Xiao. Character is destiny: Can
large language models simulate persona-driven deci-
sions in role-playing?, 2024.
[67]
Xinfeng Yuan, Siyu Yuan, Yuhan Cui, Tianhe Lin,
Xintao Wang, Rui Xu, Jiangjie Chen, and Deqing
Yang.
Evaluating character understanding of large
language models via character profiling from fictional
works, 2024.
[68]
Yiting Ran, Xintao Wang, Rui Xu, Xinfeng Yuan, Ji-
aqing Liang, Yanghua Xiao, and Deqing Yang. Captur-
ing minds, not just words: Enhancing role-playing lan-
guage models with personality-indicative data, 2024.
[69]
Yanqi Dai, Huanran Hu, Lei Wang, Shengjie Jin,
Xu Chen, and Zhiwu Lu. Mmrole: A comprehensive
framework for developing and evaluating multimodal
role-playing agents, 2024.
[70]
Yeyong Yu, Runsheng Yu, Haojie Wei, Zhanqiu
Zhang, and Quan Qian. Beyond dialogue: A profile-
dialogue alignment framework towards general role-
playing language model, 2024.
[71]
Linzhuang Sun, Yao Dong, Nan Xu, Jingxuan Wei, Bi-
hui Yu, and Yin Luo. Rational sensibility: Llm en-
hanced empathetic response generation guided by self-
presentation theory. arXiv preprint arXiv:2312.08702,
2023.
[72]
Saketh Reddy Karra, Son The Nguyen, and Theja Tu-
labandhula. Estimating the personality of white-box
language models, 2023.
[73]
Guangyuan Jiang, Manjie Xu, Song-Chun Zhu, Wen-
juan Han, Chi Zhang, and Yixin Zhu. Evaluating and
inducing personality in pre-trained language models,
2023.
[74]
Yifan Liu, Wei Wei, Jiayi Liu, Xianling Mao, Rui
Fang, and Dangyang Chen.
Improving personality
consistency in conversation by persona extending. In
Proceedings of the 31st ACM International Conference
on Information & Knowledge Management, volume 39
of CIKM ’22, page 1350–1359. ACM, October 2022.
[75]
John J. Horton. Large language models as simulated
economic agents: What can we learn from homo sili-
cus?, 2023.
[76]
Qianqian Xie, Weiguang Han, Yanzhao Lai, Min Peng,
and Jimin Huang. The wall street neophyte: A zero-
shot analysis of chatgpt over multimodal stock move-
ment prediction challenges, 2023.
[77]
Ameet Deshpande, Vishvak Murahari, Tanmay Ra-
jpurohit, Ashwin Kalyan, and Karthik Narasimhan.
Toxicity in chatgpt: Analyzing persona-assigned lan-
guage models, 2023.
[78]
Xiaoyang Song, Akshat Gupta, Kiyan Mohebbizadeh,
Shujie Hu, and Anant Singh.
Have large language
models developed a personality?:
Applicability of
self-assessment tests in measuring personality in llms,
2023.
[79]
Myra Cheng, Esin Durmus, and Dan Jurafsky. Marked
personas: Using natural language prompts to measure
stereotypes in language models, 2023.
[80]
Lei Wang, Jingsen Zhang, Hao Yang, Zhiyuan Chen,
Jiakai Tang, Zeyu Zhang, Xu Chen, Yankai Lin, Rui-
hua Song, Wayne Xin Zhao, Jun Xu, Zhicheng Dou,

## Page 28

Jun Wang, and Ji-Rong Wen. User behavior simula-
tion with large language model based agents, 2024.
[81]
Greg Serapio-Garc´ıa, Mustafa Safdari, Cl´ement Crepy,
Luning Sun, Stephen Fitz, Peter Romero, Marwa Ab-
dulhai, Aleksandra Faust, and Maja Matari´c. Person-
ality traits in large language models, 2023.
[82]
Jen tse Huang, Man Ho Lam, Eric John Li, Shujie
Ren, Wenxuan Wang, Wenxiang Jiao, Zhaopeng Tu,
and Michael R. Lyu. Emotionally numb or empathetic?
evaluating how llms feel using emotionbench, 2024.
[83]
Quan Tu, Chuanqi Chen, Jinpeng Li, Yanran Li, Shuo
Shang, Dongyan Zhao, Ran Wang, and Rui Yan. Char-
acterchat: Learning towards conversational ai with per-
sonalized social support, 2023.
[84]
Mahyar Abbasian, Iman Azimi, Amir M. Rahmani,
and Ramesh Jain. Conversational health agents: A per-
sonalized llm-powered agent framework, 2024.
[85]
Jiangjie
Chen,
Siyu
Yuan,
Rong
Ye,
Bod-
hisattwa Prasad Majumder, and Kyle Richardson.
Put your money where your mouth is: Evaluating
strategic planning and execution of llm agents in an
auction arena, 2024.
[86]
Nian Li, Chen Gao, Mingyu Li, Yong Li, and Qingmin
Liao. Econagent: Large language model-empowered
agents for simulating macroeconomic activities, 2024.
[87]
Ryan Shea and Zhou Yu.
Building persona consis-
tent dialogue agents with offline reinforcement learn-
ing, 2023.
[88]
Kushal Chawla, Ian Wu, Yu Rong, Gale M. Lucas, and
Jonathan Gratch. Be selfish, but wisely: Investigat-
ing the impact of agent personality in mixed-motive
human-agent interactions, 2023.
[89]
Yoon-Kyung Lee, Sowon Hahn, Seo-Yeon Bae, Inju
Lee, and Minjung Shin. Enhancing empathic reason-
ing of large language models based on psychotherapy
models for ai-assisted social support. Korean Journal
of Cognitive Science, 35(1):23–48, 03 2024.
[90]
Shashank Gupta, Vaishnavi Shrivastava, Ameet Desh-
pande, Ashwin Kalyan, Peter Clark, Ashish Sabhar-
wal, and Tushar Khot. Bias runs deep: Implicit rea-
soning biases in persona-assigned llms, 2024.
[91]
Junyi Li, Ninareh Mehrabi, Charith Peris, Palash
Goyal, Kai-Wei Chang, Aram Galstyan, Richard
Zemel, and Rahul Gupta. On the steerability of large
language models toward data-driven personas, 2024.
[92]
Chengxing Xie, Canyu Chen, Feiran Jia, Ziyu Ye,
Kai Shu, Adel Bibi, Ziniu Hu, Philip Torr, Bernard
Ghanem, and Guohao Li. Can large language model
agents simulate human trust behaviors?, 2024.
[93]
Sanguk Lee, Tai-Quan Peng, Matthew H. Goldberg,
Seth A. Rosenthal, John E. Kotcher, Edward W.
Maibach, and Anthony Leiserowitz.
Can large lan-
guage models estimate public opinion about global
warming? an empirical assessment of algorithmic fi-
delity and bias. PLOS Climate, 3(8):e0000429, August
2024.
[94]
Cheng Li, Mengzhou Chen, Jindong Wang, Sunayana
Sitaram, and Xing Xie. Culturellm: Incorporating cul-
tural differences into large language models, 2024.
[95]
Yixuan Weng, Shizhu He, Kang Liu, Shengping Liu,
and Jun Zhao. Controllm: Crafting diverse personali-
ties for language models, 2024.
[96]
Seungjong Sun, Eungu Lee, Dongyan Nan, Xiangy-
ing Zhao, Wonbyung Lee, Bernard J. Jansen, and
Jang Hyun Kim. Random silicon sampling: Simulat-
ing human sub-population opinion using a large lan-
guage model based on group-level demographic infor-
mation, 2024.
[97]
James Bisbee, Joshua D. Clinton, Cassy Dorff, Bren-
ton Kenkel, and Jennifer M. Larson.
Synthetic re-
placements for human survey data? the perils of large
language models. Political Analysis, 32(4):401–416,
2024.
[98]
Tao Ge, Xin Chan, Xiaoyang Wang, Dian Yu, Haitao
Mi, and Dong Yu. Scaling synthetic data creation with
1,000,000,000 personas, 2024.
[99]
Yao Qu and Jue Wang.
Performance and biases of
large language models in public opinion simulation.
Academy of Management Proceedings, 2024.
[100] Huachuan Qiu and Zhenzhong Lan. Interactive agents:
Simulating counselor-client psychological counseling
via role-playing llm-to-llm interactions, 2024.
[101] Zhilin Wang, Yu Ying Chiu, and Yu Cheung Chiu.
Humanoid agents: Platform for simulating human-like
generative agents, 2023.
[102] Yoonna Jang, Jungwoo Lim, Yuna Hur, Dongsuk Oh,
Suhyune Son, Yeonsoo Lee, Donghoon Shin, Seun-
gryong Kim, and Heuiseok Lim. Call for customized
conversation: Customized conversation grounding per-
sona and knowledge, 2022.
[103] Juntao Li, Chang Liu, Chongyang Tao, Zhangming
Chan, Dongyan Zhao, Min Zhang, and Rui Yan. Di-
alogue history matters! personalized response selec-
tionin multi-turn retrieval-based chatbots, 2021.
[104] Pegah Jandaghi, XiangHai Sheng, Xinyi Bai, Jay Pu-
jara, and Hakim Sidahmed.
Faithful persona-based
conversational dataset generation with large language
models, 2023.
[105] Weiqi Wu, Hongqiu Wu, Lai Jiang, Xingyuan Liu,
Jiale Hong, Hai Zhao, and Min Zhang. From role-play
to drama-interaction: An llm solution, 2024.
[106] Jiannan Xiang, Tianhua Tao, Yi Gu, Tianmin Shu,
Zirui Wang, Zichao Yang, and Zhiting Hu. Language
models meet world models: Embodied experiences en-
hance language models, 2023.
[107] Jiangyong
Huang,
Silong
Yong,
Xiaojian
Ma,
Xiongkun Linghu, Puhao Li, Yan Wang, Qing Li,

## Page 29

Song-Chun Zhu, Baoxiong Jia, and Siyuan Huang. An
embodied generalist agent in 3d world, 2024.
[108] Jiaju Lin, Haoran Zhao, Aochi Zhang, Yiting Wu,
Huqiuyue Ping, and Qin Chen. Agentsims: An open-
source sandbox for large language model evaluation,
2023.
[109] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Man-
dlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and An-
ima Anandkumar. Voyager: An open-ended embodied
agent with large language models, 2023.
[110] Xintao Wang, Jiangjie Chen, Nianqi Li, Lida Chen,
Xinfeng Yuan, Wei Shi, Xuyang Ge, Rui Xu, and
Yanghua Xiao. Surveyagent: A conversational system
for personalized and efficient research survey, 2024.
[111] Hongzhan Chen, Hehong Chen, Ming Yan, Wenshen
Xu, Xing Gao, Weizhou Shen, Xiaojun Quan, Chen-
liang Li, Ji Zhang, Fei Huang, and Jingren Zhou. So-
cialbench: Sociality evaluation of role-playing conver-
sational agents, 2024.
[112] Zhipeng Chen, Kun Zhou, Beichen Zhang, Zheng
Gong, Wayne Xin Zhao, and Ji-Rong Wen. Chatcot:
Tool-augmented chain-of-thought reasoning on chat-
based large language models, 2023.
[113] Alireza Salemi, Sheshera Mysore, Michael Bendersky,
and Hamed Zamani.
Lamp: When large language
models meet personalization, 2024.
[114] Ceyao Zhang, Kaijie Yang, Siyi Hu, Zihao Wang,
Guanghe Li, Yihang Sun, Cheng Zhang, Zhaowei
Zhang, Anji Liu, Song-Chun Zhu, Xiaojun Chang,
Junge Zhang, Feng Yin, Yitao Liang, and Yaodong
Yang. Proagent: Building proactive cooperative agents
with large language models, 2024.
[115] Lei Wang, Wanyu Xu, Yihuai Lan, Zhiqiang Hu, Yun-
shi Lan, Roy Ka-Wei Lee, and Ee-Peng Lim. Plan-
and-solve prompting: Improving zero-shot chain-of-
thought reasoning by large language models.
arXiv
preprint arXiv:2305.04091, 2023.
[116] Zhenyu Wu, Ziwei Wang, Xiuwei Xu, Jiwen Lu,
and Haibin Yan. Embodied task planning with large
language models. arXiv preprint arXiv:2307.01848,
2023.
[117] Chan Hee Song, Jiaman Wu, Clayton Washington,
Brian M. Sadler, Wei-Lun Chao, and Yu Su.
Llm-
planner: Few-shot grounded planning for embodied
agents with large language models, 2023.
[118] Itsugun Cho, Dongyang Wang, Ryota Takahashi, and
Hiroaki Saito. A personalized dialogue generator with
implicit user persona detection, 2022.
[119] Jonathan Light, Min Cai, Sheng Shen, and Ziniu Hu.
Avalonbench: Evaluating llms playing the game of
avalon, 2023.
[120] Keyu Pan and Yawen Zeng. Do llms possess a person-
ality? making the mbti test an amazing evaluation for
large language models, 2023.
[121] Kranti Chalamalasetti, Jana G¨otze, Sherzod Haki-
mov, Brielen Madureira, Philipp Sadler, and David
Schlangen.
Clembench: Using game play to evalu-
ate chat-optimized language models as conversational
agents, 2023.
[122] Haoqi Yuan, Chi Zhang, Hongcheng Wang, Feiyang
Xie, Penglin Cai, Hao Dong, and Zongqing Lu. Skill
reinforcement learning and planning for open-world
long-horizon tasks, 2023.
[123] Libo Sun,
Siyuan Wang,
Xuanjing Huang,
and
Zhongyu Wei.
Identity-driven hierarchical role-
playing agents.
arXiv preprint arXiv:2407.19412,
2024.
[124] Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda
Askell, Anna Chen, Nova DasSarma, Dawn Drain,
Stanislav
Fort,
Deep
Ganguli,
Tom
Henighan,
Nicholas Joseph, Saurav Kadavath, Jackson Kernion,
Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac
Hatfield-Dodds, Danny Hernandez, Tristan Hume,
Scott Johnston, Shauna Kravec, Liane Lovitt, Neel
Nanda, Catherine Olsson, Dario Amodei, Tom Brown,
Jack Clark, Sam McCandlish, Chris Olah, Ben Mann,
and Jared Kaplan. Training a helpful and harmless as-
sistant with reinforcement learning from human feed-
back, 2022.
[125] Joel Jang, Seungone Kim, Bill Yuchen Lin, Yizhong
Wang, Jack Hessel, Luke Zettlemoyer, Hannaneh Ha-
jishirzi, Yejin Choi, and Prithviraj Ammanabrolu. Per-
sonalized soups: Personalized large language model
alignment via post-hoc parameter merging, 2023.
[126] Xingxuan Li, Yutong Li, Lin Qiu, Shafiq Joty, and Li-
dong Bing. Evaluating psychological safety of large
language models, 2024.
[127] Sanguk Lee, Kai-Qi Yang, Tai-Quan Peng, Ruth Heo,
and Hui Liu.
Exploring social desirability response
bias in large language models: Evidence from gpt-4
simulations, 2024.
[128] Won Ik Cho, Yoon Kyung Lee, Seoyeon Bae, Jihwan
Kim, Sangah Park, Moosung Kim, Sowon Hahn, and
Nam Soo Kim. When crowd meets persona: Creat-
ing a large-scale open-domain persona dialogue cor-
pus, 2023.
[129] Xinyi Mou, Zejun Li, Hanjia Lyu, Jiebo Luo, and
Zhongyu Wei. Unifying local and global knowledge:
Empowering large language models as political ex-
perts with knowledge graphs. In Proceedings of the
ACM on Web Conference 2024, pages 2603–2614,
2024.
[130] Yuanchun Li, Hao Wen, Weijun Wang, Xiangyu Li,
Yizhen Yuan, Guohong Liu, Jiacheng Liu, Wenxing
Xu, Xiang Wang, Yi Sun, Rui Kong, Yile Wang, Han-
fei Geng, Jian Luan, Xuefeng Jin, Zilong Ye, Guanjing
Xiong, Fan Zhang, Xiang Li, Mengwei Xu, Zhijun Li,
Peng Li, Yang Liu, Ya-Qin Zhang, and Yunxin Liu.
Personal llm agents: Insights and survey about the ca-
pability, efficiency and security, 2024.

## Page 30

[131] Jinheon Baek,
Nirupama Chandrasekaran,
Silviu
Cucerzan, Allen herring, and Sujay Kumar Jauhar.
Knowledge-augmented large language models for per-
sonalized contextual query suggestion, 2024.
[132] Hezekiah J. Branch, Jonathan Rodriguez Cefalu,
Jeremy McHugh, Leyla Hujer, Aditya Bahl, Daniel
del Castillo Iglesias, Ron Heichman, and Ramesh Dar-
wishi. Evaluating the susceptibility of pre-trained lan-
guage models via handcrafted adversarial examples,
2022.
[133] Jaewoo Ahn, Yeda Song, Sangdoo Yun, and Gun-
hee Kim.
MPCHAT: Towards multimodal persona-
grounded conversation. In Anna Rogers, Jordan Boyd-
Graber, and Naoaki Okazaki, editors, Proceedings of
the 61st Annual Meeting of the Association for Com-
putational Linguistics (Volume 1: Long Papers), pages
3354–3377, Toronto, Canada, July 2023. Association
for Computational Linguistics.
[134] Jiwei Li, Michel Galley, Chris Brockett, Georgios P.
Spithourakis, Jianfeng Gao, and Bill Dolan.
A
persona-based neural conversation model, 2016.
[135] Zejun Wang, Jia Li, Ge Li, and Zhi Jin. Chatcoder:
Chat-based refine requirement improves llms’ code
generation, 2023.
[136] Nicholas Farn and Richard Shin. Tooltalk: Evaluating
tool-usage in a conversational setting, 2023.
[137] Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xu-
anyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kai-
wen Men, Kejuan Yang, Shudan Zhang, Xiang Deng,
Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng
Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang,
Yuxiao Dong, and Jie Tang. Agentbench: Evaluating
llms as agents, 2023.
[138] Xuhui Zhou, Hao Zhu, Leena Mathur, Ruohong
Zhang, Haofei Yu, Zhengyang Qi, Louis-Philippe
Morency, Yonatan Bisk, Daniel Fried, Graham Neu-
big, et al.
Sotopia: Interactive evaluation for so-
cial intelligence in language agents.
arXiv preprint
arXiv:2310.11667, 2023.
[139] Mohammadmehdi Ataei, Hyunmin Cheong, Daniele
Grandi, Ye Wang, Nigel Morris, and Alexander
Tessier.
Elicitron: An llm agent-based simulation
framework for design requirements elicitation. arXiv
preprint arXiv:2404.16045, 2024.
[140] Diyi Yang, Caleb Ziems, William Held, Omar Shaikh,
Michael S Bernstein, and John Mitchell. Social skill
training with large language models. arXiv preprint
arXiv:2404.04204, 2024.
[141] Zihan Yan, Yaohong Xiang, and Yun Huang. Social
life simulation for non-cognitive skills learning. arXiv
preprint arXiv:2405.00273, 2024.
[142] Qiang Zhang, Jason Naradowsky, and Yusuke Miyao.
Self-emotion blended dialogue generation in social
simulation agents. arXiv preprint arXiv:2408.01633,
2024.
[143] Yao Fu, Hao Peng, Tushar Khot, and Mirella Lap-
ata. Improving language model negotiation with self-
play and in-context learning from ai feedback. arXiv
preprint arXiv:2305.10142, 2023.
[144] Kai Xiong, Xiao Ding, Yixin Cao, Ting Liu, and Bing
Qin.
Examining inter-consistency of large language
models collaboration: An in-depth analysis via debate.
arXiv preprint arXiv:2305.11595, 2023.
[145] Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang,
Yan Wang, Rui Wang, Yujiu Yang, Zhaopeng Tu, and
Shuming Shi. Encouraging divergent thinking in large
language models through multi-agent debate.
arXiv
preprint arXiv:2305.19118, 2023.
[146] Chi Ming Chan, Wenhao Chen, Yi Su, et al. Chateval:
Towards better llm-based evaluators through multi-
agent debate. arXiv preprint arXiv:2308.07201, 2023.
[147] Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu,
Shaokun Zhang, Erkang Zhu, Beibin Li, Li Jiang, Xi-
aoyun Zhang, and Chi Wang.
Autogen: Enabling
next-gen llm applications via multi-agent conversation
framework. arXiv preprint arXiv:2308.08155, 2023.
[148] Tian Xia, Zhiwei He, Tong Ren, Yibo Miao, Zhu-
osheng Zhang, Yang Yang, and Rui Wang.
Mea-
suring bargaining abilities of llms:
A benchmark
and a buyer-enhancement method.
arXiv preprint
arXiv:2402.15813, 2024.
[149] Jie Ma, Zhitao Gao, Qi Chai, Wangchun Sun, Pinghui
Wang, Hongbin Pei, Jing Tao, Lingyun Song, Jun Liu,
Chen Zhang, et al. Debate on graph: a flexible and re-
liable reasoning framework for large language models.
arXiv preprint arXiv:2409.03155, 2024.
[150] Y. Xu, S. Wang, P. Li, et al. Exploring large language
models for communication games: An empirical study
on werewolf, 2023.
[151] Shenzhi Wang, Chang Liu, Zilong Zheng, Siyuan
Qi, Shuo Chen, Qisen Yang, Andrew Zhao, Chaofei
Wang, Shiji Song, and Gao Huang.
Avalon’s game
of thoughts: Battle against deception through recur-
sive contemplation. arXiv preprint arXiv:2310.01320,
2023.
[152] Jintian Zhang, Xin Xu, and Shumin Deng.
Explor-
ing collaboration mechanisms for llm agents: A social
psychology view.
arXiv preprint arXiv:2310.02124,
2023.
[153] Jonathan Light, Min Cai, Sheng Shen, and Ziniu Hu.
From text to tactic: Evaluating llms playing the game
of avalon. arXiv preprint arXiv:2310.05036, 2023.
[154] Yihuai Lan, Zhiqiang Hu, Lei Wang, Yang Wang, De-
heng Ye, Peilin Zhao, Ee-Peng Lim, Hui Xiong, and
Hao Wang.
Llm-based agent society investigation:
Collaboration and confrontation in avalon gameplay.
arXiv preprint arXiv:2310.14985, 2023.
[155] Zelai Xu, Chao Yu, Fei Fang, Yu Wang, and Yi Wu.
Language agents with reinforcement learning for

## Page 31

strategic play in the werewolf game. arXiv preprint
arXiv:2310.18940, 2023.
[156] Dekun Wu, Haochen Shi, Zhiyuan Sun, and Bang Liu.
Deciphering digital detectives: Understanding llm be-
haviors and capabilities in multi-agent mystery games.
arXiv preprint arXiv:2312.00746, 2023.
[157] Zijing Shi, Meng Fang, Shunfeng Zheng, Shilong
Deng, Ling Chen, and Yali Du. Cooperation on the
fly: Exploring language agents for ad hoc teamwork
in the avalon game. arXiv preprint arXiv:2312.17515,
2023.
[158] S. Wu, L. Zhu, T. Yang, et al. Enhance reasoning for
large language models in the game werewolf, 2024.
[159] Silin Du and Xiaowei Zhang.
Helmsman of the
masses? evaluate the opinion leadership of large lan-
guage models in the werewolf game. arXiv preprint
arXiv:2404.01602, 2024.
[160] Qinglin Zhu, Runcong Zhao, Jinhua Du, Lin Gui,
and Yulan He. Player*: Enhancing llm-based multi-
agent communication and interaction in murder mys-
tery games. arXiv preprint arXiv:2404.17662, 2024.
[161] Xizhou Zhu, Yuntao Chen, Hao Tian, Chenxin Tao,
Weijie Su, Chenyu Yang, Gao Huang, Bin Li, Lewei
Lu, Xiaogang Wang, et al.
Ghost in the minecraft:
Generally capable agents for open-world environments
via large language models with text-based knowledge
and memory. arXiv preprint arXiv:2305.17144, 2023.
[162] Karthik Sreedhar and Lydia Chilton. Simulating hu-
man strategic behavior: Comparing single and multi-
agent llms. arXiv preprint arXiv:2402.08189, 2024.
[163] Yizhou Chi, Lingjun Mao, and Zineng Tang. Amonga-
gents: Evaluating large language models in the interac-
tive text-based social deduction game. arXiv preprint
arXiv:2407.16521, 2024.
[164] Jiaqi Chen, Yuxian Jiang, Jiachen Lu, and Li Zhang.
S-agents: self-organizing agents in open-ended envi-
ronment. arXiv preprint arXiv:2402.04578, 2024.
[165] Md Mahadi Hassan, Alex Knipper, and Shubhra
Kanti Karmaker Santu. Chatgpt as your personal data
scientist. arXiv preprint arXiv:2305.13657, 2023.
[166] Cheng-Kuang Wu, Wei-Lin Chen, and Hsin-Hsi Chen.
Large language models perform diagnostic reasoning.
arXiv preprint arXiv:2307.08922, 2023.
[167] Zhiling Zheng, Oufan Zhang, Ha L Nguyen, Nakul
Rampal, Ali H Alawadhi, Zichao Rong, Teresa Head-
Gordon, Christian Borgs, Jennifer T Chayes, and
Omar M Yaghi. Chatgpt research group for optimiz-
ing the crystallinity of mofs and cofs. ACS Central
Science, 9(11):2161–2170, 2023.
[168] Xiangru Tang, Anni Zou, Zhuosheng Zhang, Yilun
Zhao, Xingyao Zhang, Arman Cohan, and Mark Ger-
stein. Medagents: Large language models as collabo-
rators for zero-shot medical reasoning. arXiv preprint
arXiv:2311.10537, 2023.
[169] Zhaolin Gao, Kiant´e Brantley, and Thorsten Joachims.
Reviewer2:
Optimizing review generation through
prompt generation. arXiv preprint arXiv:2402.10886,
2024.
[170] Mingyu Jin, Beichen Wang, Zhaoqian Xue, Suiyuan
Zhu, Wenyue Hua, Hua Tang, Kai Mei, Mengnan Du,
and Yongfeng Zhang.
What if llms have different
world views: Simulating alien civilizations with llm-
based agents. arXiv preprint arXiv:2402.13184, 2024.
[171] Jinheon Baek, Sujay Kumar Jauhar, Silviu Cucerzan,
and Sung Ju Hwang. Researchagent: Iterative research
idea generation over scientific literature with large
language models. arXiv preprint arXiv:2404.07738,
2024.
[172] Hanna Yukhymenko, Robin Staab, Mark Vero, and
Martin Vechev.
A synthetic dataset for personal at-
tribute inference.
arXiv preprint arXiv:2406.07217,
2024.
[173] Zhifei Xie, Daniel Tang, Dingwei Tan, Jacques Klein,
Tegawend F Bissyand, and Saad Ezzini.
Dream-
factory: Pioneering multi-scene long video genera-
tion with a multi-agent framework.
arXiv preprint
arXiv:2408.11788, 2024.
[174] Jun-Peng Zhu, Peng Cai, Kai Xu, Li Li, Yishen Sun,
Shuai Zhou, Haihuang Su, Liu Tang, and Qi Liu. Au-
totqa: Towards autonomous tabular question answer-
ing through multi-agent large language models. Proc.
VLDB Endow., 17(12):3920–3933, November 2024.
[175] Varun Nair, Elliot Schumacher, Geoffrey Tso, and
Anitha Kannan.
Dera:
enhancing large language
model completions with dialog-enabled resolving
agents. arXiv preprint arXiv:2303.17071, 2023.
[176] Yihong Dong, Xue Jiang, Zhi Jin, and Ge Li. Self-
collaboration code generation via chatgpt.
arXiv
preprint arXiv:2304.07590, 2023.
[177] Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen,
Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen,
Yusheng Su, Xin Cong, et al. Chatdev: Communica-
tive agents for software development.
In Proceed-
ings of the 62nd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 15174–15186, 2024.
[178] Chen Qian, Yufan Dang, Jiahao Li, Wei Liu, Weize
Chen, Cheng Yang, Zhiyuan Liu, and Maosong
Sun. Experiential co-learning of software-developing
agents. arXiv preprint arXiv:2312.17025, 2023.
[179] Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, and Ab-
hik Roychoudhury. Autocoderover: Autonomous pro-
gram improvement. In Proceedings of the 33rd ACM
SIGSOFT International Symposium on Software Test-
ing and Analysis, pages 1592–1604, 2024.
[180] Chen Qian, Jiahao Li, Yufan Dang, Wei Liu, YiFei
Wang, Zihao Xie, Weize Chen, Cheng Yang, Yingli
Zhang, Zhiyuan Liu, et al. Iterative experience refine-
ment of software-developing agents.
arXiv preprint
arXiv:2405.04219, 2024.

## Page 32

[181] Sil Hamilton.
Blind judgement:
Agent-based
supreme court modelling with gpt.
arXiv preprint
arXiv:2301.05327, 2023.
[182] Yang Li, Yangyang Yu, Haohang Li, Zhi Chen, and
Khaldoun Khashanah. Tradinggpt: Multi-agent system
with layered memory and distinct characters for en-
hanced financial trading performance. arXiv preprint
arXiv:2309.03736, 2023.
[183] Martin Weiss, Nasim Rahaman, Manuel Wuthrich,
Yoshua Bengio, Li Erran Li, Bernhard Sch¨”olkopf, and
Christopher Pal.
Rethinking the buyer’s inspection
paradox in information markets with language agents.
OpenReview, 2024.
[184] Murong Yue, Wijdane Mifdal, Yixuan Zhang, Jennifer
Suh, and Ziyu Yao. Mathvc: An llm-simulated multi-
character virtual classroom for mathematics education.
arXiv preprint arXiv:2404.06711, 2024.
[185] Zachary R Baker and Zarif L Azher. Simulating the
us senate: An llm-driven agent approach to modeling
legislative behavior and bipartisanship. arXiv preprint
arXiv:2406.18702, 2024.
[186] Jingyun Sun, Chengxiao Dai, Zhongze Luo, Yangbo
Chang, and Yang Li. Lawluo: A chinese law firm co-
run by llm agents. arXiv preprint arXiv:2407.16252,
2024.
[187] Jifan Yu, Zheyuan Zhang, Daniel Zhang-li, Shangqing
Tu, Zhanxin Hao, Rui Miao Li, Haoxuan Li, Yuanchun
Wang, Hanming Li, Linlu Gong, et al. From mooc to
maic: Reshaping online teaching and learning through
llm-driven agents. arXiv preprint arXiv:2409.03512,
2024.
[188] Guohao Li, Hasan Hammoud, Hani Itani, Dmitrii
Khizbullin, and Bernard Ghanem. Camel: Commu-
nicative agents for”” mind”” exploration of large lan-
guage model society. Advances in Neural Information
Processing Systems, 36:51991–52008, 2023.
[189] Bill Yuchen Lin, Yicheng Fu, Karina Yang, Faeze
Brahman,
Shiyu
Huang,
Chandra
Bhagavatula,
Prithviraj Ammanabrolu, Yejin Choi, and Xiang Ren.
Swiftsage:
A generative agent with fast and slow
thinking for complex interactive tasks.
Advances in
Neural Information Processing Systems, 36, 2024.
[190] Yashar Talebirad and Amirhossein Nadiri. Multi-agent
collaboration: Harnessing the power of intelligent llm
agents. arXiv preprint arXiv:2306.03314, 2023.
[191] Hongxin Zhang, Weihua Du, Jiaming Shan, Qinhong
Zhou, Yilun Du, Joshua B Tenenbaum, Tianmin Shu,
and Chuang Gan.
Building cooperative embodied
agents modularly with large language models. arXiv
preprint arXiv:2307.02485, 2023.
[192] Zhao Mandi, Shreeya Jain, and Shuran Song. Roco:
Dialectic multi-robot collaboration with large lan-
guage models. In 2024 IEEE International Conference
on Robotics and Automation (ICRA), pages 286–299.
IEEE, 2024.
[193] W. Chen, Y. Su, J. Zuo, et al. Agentverse: Facilitat-
ing multi-agent collaboration and exploring emergent
behaviors, 2023.
[194] Yongchao Chen, Jacob Arkin, Yang Zhang, Nicholas
Roy, and Chuchu Fan. Scalable multi-robot collabora-
tion with large language models: Centralized or decen-
tralized systems? In 2024 IEEE International Confer-
ence on Robotics and Automation (ICRA), pages 4311–
4317. IEEE, 2024.
[195] Guangyao Chen, Siwei Dong, Yu Shu, Ge Zhang,
Jaward Sesay, B¨”orje F Karlsson, Jie Fu, and Yemin
Shi.
Autoagents: A framework for automatic agent
generation. arXiv preprint arXiv:2309.17288, 2023.
[196] Tianbao Xie, Fan Zhou, Zhoujun Cheng, Peng Shi, Lu-
oxuan Weng, Yitao Liu, Toh Jing Hua, Junning Zhao,
Qian Liu, Che Liu, et al. Openagents: An open plat-
form for language agents in the wild. arXiv preprint
arXiv:2310.10634, 2023.
[197] Weihao Tan, Wentao Zhang, Shanqi Liu, Longtao
Zheng, Xinrun Wang, and Bo An.
True knowledge
comes from practice: Aligning llms with embodied en-
vironments via reinforcement learning. arXiv preprint
arXiv:2401.14151, 2024.
[198] Yang Zhang, Shixin Yang, Chenjia Bai, Fei Wu, Xiu
Li, Xuelong Li, and Zhen Wang.
Towards efficient
llm grounding for embodied multi-agent collaboration.
arXiv preprint arXiv:2405.14314, 2024.
[199] J. Lin, H. Zhao, A. Zhang, et al. Agentsims: An open-
source sandbox for large language model evaluation,
2023.
[200] Yuan Li, Yixuan Zhang, and Lichao Sun.
Metaa-
gents: Simulating interactions of human behaviors for
llm-based task-oriented coordination via collaborative
generative agents. arXiv preprint arXiv:2310.06500,
2023.
[201] Jingcong Liang, Rong Ye, Meng Han, Ruofei Lai,
Xinyu Zhang, Xuanjing Huang, and Zhongyu Wei. De-
batrix: Multi-dimensinal debate judge with iterative
chronological analysis based on llm. arXiv preprint
arXiv:2403.08010, 2024.
[202] Wei Liu, Chenxi Wang, Yifei Wang, Zihao Xie, Rennai
Qiu, Yufan Dang, Zhuoyun Du, Weize Chen, Cheng
Yang, and Chen Qian.
Autonomous agents for col-
laborative task under information asymmetry. arXiv
preprint arXiv:2406.14928, 2024.
[203] Weize Chen, Jiarui Yuan, Chen Qian, Cheng Yang,
Zhiyuan Liu, and Maosong Sun. Optima: Optimizing
effectiveness and efficiency for llm-based multi-agent
system. arXiv preprint arXiv:2410.08115, 2024.
[204] Chenxu Wang, Bin Dai, Huaping Liu, and Baoyuan
Wang. Towards objectively benchmarking social in-
telligence for language agents at action level. arXiv
preprint arXiv:2404.05337, 2024.
[205] Xinyi Mou, Jingcong Liang, Jiayu Lin, Xinnong
Zhang, Xiawei Liu, Shiyue Yang, Rong Ye, Lei

## Page 33

Chen,
Haoyu
Kuang,
Xuanjing
Huang,
et
al.
Agentsense: Benchmarking social intelligence of lan-
guage agents through interactive scenarios.
arXiv
preprint arXiv:2410.19346, 2024.
[206] Ruiyi Wang, Haofei Yu, Wenxin Zhang, Zhengyang
Qi, Maarten Sap, Graham Neubig, Yonatan Bisk,
and Hao Zhu.
Sotopia-pi:
Interactive learning of
socially intelligent language agents.
arXiv preprint
arXiv:2403.08715, 2024.
[207] Xuhui Zhou, Zhe Su, Tiwalayo Eisape, Hyunwoo Kim,
and Maarten Sap. Is this the real life? is this just fan-
tasy? the misleading success of simulating social in-
teractions with llms. arXiv preprint arXiv:2403.05020,
2024.
[208] Ran Gong, Qiuyuan Huang, Xiaojian Ma, Hoi Vo,
Zane Durante, Yusuke Noda, Zilong Zheng, Song-
Chun Zhu, Demetri Terzopoulos, Li Fei-Fei, et al.
Mindagent:
Emergent gaming interaction.
arXiv
preprint arXiv:2309.09971, 2023.
[209] Zhijie Bao, Qingyun Liu, Ying Guo, Zhengqiang Ye,
Jun Shen, Shirong Xie, Jiajie Peng, Xuanjing Huang,
and Zhongyu Wei.
Piors: Personalized intelligent
outpatient reception based on large language model
with multi-agents medical scenario simulation. arXiv
preprint arXiv:2411.13902, 2024.
[210] Xiawei Liu, Shiyue Yang, Xinnong Zhang, Haoyu
Kuang, Libo Sun, Yihang Yang, Siming Chen, Xuan-
jing Huang, and Zhongyu Wei.
Ai-press: A multi-
agent news generating and feedback simulation sys-
tem powered by large language models. arXiv preprint
arXiv:2410.07561, 2024.
[211] Chengxing Xie, Canyu Chen, Feiran Jia, Ziyu Ye,
Kai Shu, Adel Bibi, Ziniu Hu, Philip Torr, Bernard
Ghanem, and Guohao Li. Can large language model
agents simulate human trust behaviors? arXiv preprint
arXiv:2402.04559, 2024.
[212] Agnieszka Mensfelt, Kostas Stathis, and Vince Trenc-
senyi.
Logic-enhanced language model agents
for trustworthy social simulations.
arXiv preprint
arXiv:2408.16081, 2024.
[213] Shangmin Guo, Haoran Bu, Haochuan Wang, Yi Ren,
Dianbo Sui, Yuming Shang, and Siting Lu. Economics
arena for large language models.
arXiv preprint
arXiv:2401.01735, 2024.
[214] Nicol´o Fontana, Francesco Pierri, and Luca Maria
Aiello. Nicer than humans: How do large language
models behave in the prisoner’s dilemma?
arXiv
preprint arXiv:2406.13605, 2024.
[215] X. Han, Z. Wu, and C. Xiao. ”guinea pig trials” utiliz-
ing gpt: A novel smart agent-based modeling approach
for studying firm competition and collusion, 2023.
[216] Sean Noh and Ho-Chun Herbert Chang.
Llms with
personalities in multi-issue negotiation games. arXiv
preprint arXiv:2405.05248, 2024.
[217] Mikhail Mozikov, Nikita Severin, Valeria Bodishtianu,
Maria Glushanina, Mikhail Baklashkin, Andrey V
Savchenko, and Ilya Makarov. The good, the bad, and
the hulk-like gpt: Analyzing emotional decisions of
large language models in cooperation and bargaining
games. arXiv preprint arXiv:2406.03299, 2024.
[218] Zengqing Wu, Run Peng, Shuyuan Zheng, Qianying
Liu, Xu Han, Brian Kwon, Makoto Onizuka, Shaojie
Tang, and Chuan Xiao.
Shall we team up: Explor-
ing spontaneous cooperation of competing llm agents.
In Findings of the Association for Computational Lin-
guistics: EMNLP 2024, pages 5163–5186, 2024.
[219] Qinlin Zhao, Jindong Wang, Yixuan Zhang, Yiqiao
Jin, Kaijie Zhu, Hao Chen, and Xing Xie. Competeai:
Understanding the competition dynamics of large lan-
guage model-based agents. In Forty-first International
Conference on Machine Learning, 2024.
[220] John J Horton. Large language models as simulated
economic agents: What can we learn from homo sili-
cus? Technical report, National Bureau of Economic
Research, 2023.
[221] Jiarui Ji, Yang Li, Hongtao Liu, Zhicheng Du, Zhewei
Wei, Qi Qi, Weiran Shen, and Yankai Lin. Srap-agent:
Simulating and optimizing scarce resource allocation
policy with llm-based agent. In Findings of the Asso-
ciation for Computational Linguistics: EMNLP 2024,
pages 267–293, 2024.
[222] Navid
Ghaffarzadegan,
Aritra
Majumdar,
Ross
Williams, and Niyousha Hosseinichimeh. Generative
agent-based
modeling:
Unveiling
social
system
dynamics through coupling mechanistic models with
generative artificial intelligence.
arXiv preprint
arXiv:2309.11456, 2023.
[223] I de Zarz`a, J de Curt`o, Gemma Roig, Pietro Man-
zoni, and Carlos T Calafate.
Emergent cooperation
and strategy adaptation in multi-agent systems: An ex-
tended coevolutionary theory with llms. Electronics,
12(12):2722, 2023.
[224] R. Williams, N. Hosseinichimeh, A. Majumdar, et al.
Epidemic modeling with generative agents.
arXiv
preprint arXiv:2307.04986, 2023.
[225] Ayush Chopra, Shashank Kumar, Nurullah Giray-
Kuru, Ramesh Raskar, and Arnau Quera-Bofarull. On
the limits of agency in agent-based models.
arXiv
preprint arXiv:2409.10568, 2024.
[226] Sanguk Lee, Tai-Quan Peng, Matthew H Goldberg,
Seth A Rosenthal, John E Kotcher, Edward W
Maibach, and Anthony Leiserowitz.
Can large lan-
guage models capture public opinion about global
warming? an empirical assessment of algorithmic fi-
delity and bias.
arXiv preprint arXiv:2311.00217,
2023.
[227] Xinnong Zhang, Jiayu Lin, Libo Sun, Weihong
Qi, Yihang Yang, Yue Chen, Hanjia Lyu, Xinyi
Mou, Siming Chen, Jiebo Luo, et al.
Electionsim:

## Page 34

Massive population election simulation powered by
large language model driven agents.
arXiv preprint
arXiv:2410.20746, 2024.
[228] B. Xiao, Z. Yin, and Z. Shan. Simulating public admin-
istration crisis: A novel generative agent-based sim-
ulation system to lower technology barriers in social
science research, 2023.
[229] Joon Sung Park, Carolyn Q Zou, Aaron Shaw, Ben-
jamin Mako Hill, Carrie Cai, Meredith Ringel Morris,
Robb Willer, Percy Liang, and Michael S Bernstein.
Generative agent simulations of 1,000 people. arXiv
preprint arXiv:2411.10109, 2024.
[230] Gati V Aher, Rosa I Arriaga, and Adam Tauman Kalai.
Using large language models to simulate multiple hu-
mans and replicate human subject studies. In Interna-
tional Conference on Machine Learning, pages 337–
371. PMLR, 2023.
[231] Zhao
Kaiya,
Michelangelo
Naim,
Jovana
Kondic, Manuel Cortes, Jiaxin Ge, Shuying Luo,
Guangyu Robert Yang, and Andrew Ahn.
Lyfe
agents: Generative agents for low-cost real-time social
interactions. arXiv preprint arXiv:2310.02172, 2023.
[232] S. Ren, Z. Cui, R. Song, et al. Emergence of social
norms in large language model-based agent societies,
2024.
[233] Jeongeon Park, Bryan Min, Xiaojuan Ma, and Juho
Kim.
Choicemates:
Supporting unfamiliar online
decision-making with multi-agent conversational in-
teractions. arXiv preprint arXiv:2310.01331, 2023.
[234] Daniel Jarrett, Miruna Pislar, Michiel A Bakker,
Michael Henry Tessler, Raphael Koster, Jan Balaguer,
Romuald Elie, Christopher Summerfield, and Andrea
Tacchetti. Language agents as digital representatives
in collective decision-making. In NeurIPS 2023 Foun-
dation Models for Decision Making Workshop, 2023.
[235] Yiqiao Jin, Qinlin Zhao, Yiyang Wang, Hao Chen,
Kaijie Zhu, Yijia Xiao, and Jindong Wang.
Agen-
treview: Exploring peer review dynamics with llm
agents. arXiv preprint arXiv:2406.12708, 2024.
[236] Yangbin Yu, Qin Zhang, Junyou Li, Qiang Fu, and De-
heng Ye. Affordable generative agents. arXiv preprint
arXiv:2402.02053, 2024.
[237] Xianhao Yu, Jiaqi Fu, Renjia Deng, and Wenjuan Han.
Mineland: Simulating large-scale multi-agent inter-
actions with limited multimodal senses and physical
needs. arXiv preprint arXiv:2403.19267, 2024.
[238] Chen Zhu, Yihang Cheng, Jingshuai Zhang, Yusheng
Qiu, Sitao Xia, and Hengshu Zhu.
Generative or-
ganizational behavior simulation using large language
model based autonomous agents: A holacracy perspec-
tive. arXiv preprint arXiv:2408.11826, 2024.
[239] R. Suzuki and T. Arita. An evolutionary model of per-
sonality traits related to cooperative behavior using a
large language model. Scientific Reports, 14(1):5989,
2024.
[240] Yun-Shiuan Chuang, Zach Studdiford, Krirk Nirun-
wiroj, Agam Goyal, Vincent V Frigo, Sijia Yang, Dha-
van Shah, Junjie Hu, and Timothy T Rogers. Beyond
demographics: Aligning role-playing llm-based agents
using human belief networks, 2024.
[241] Chao Li, Xing Su, Haoying Han, Cong Xue, Chunmo
Zheng, and Chao Fan.
Quantifying the impact of
large language models on collective opinion dynamics.
arXiv preprint arXiv:2308.03313, 2023.
[242] Shuo Tang, Xianghe Pang, Zexi Liu, Bohan Tang, Rui
Ye, Xiaowen Dong, Yanfeng Wang, and Siheng Chen.
Synthesizing post-training data for llms through multi-
agent simulation.
arXiv preprint arXiv:2410.14251,
2024.
[243] Jinyu Cai,
Jialong Li,
Mingyue Zhang,
Munan
Li, Chen-Shu Wang, and Kenji Tei.
Language
evolution for evading social media regulation via
llm-based multi-agent simulation.
arXiv preprint
arXiv:2405.02858, 2024.
[244] Yuhan Liu, Zirui Song, Xiaoqing Zhang, Xiuying
Chen, and Rui Yan. From a tiny slip to a giant leap: An
llm-based simulation for fake news evolution. arXiv
preprint arXiv:2410.19064, 2024.
[245] Chenxi Wang, Zongfang Liu, Dequan Yang, and Xi-
uying Chen. Decoding echo chambers: Llm-powered
simulations revealing polarization in social networks.
arXiv preprint arXiv:2409.19338, 2024.
[246] Maximilian Puelma Touzel, Sneheel Sarangi, Austin
Welch, Gayatri Krishnakumar, Dan Zhao, Zachary
Yang, Hao Yu, Ethan Kosak-Hine, Tom Gibbs, An-
dreea Musulan, et al.
A simulation system towards
solving societal-scale manipulation.
arXiv preprint
arXiv:2410.13915, 2024.
[247] J. S. Park, L. Popowski, C. Cai, et al. Social simu-
lacra: Creating populated prototypes for social com-
puting systems.
In Proceedings of the 35th Annual
ACM Symposium on User Interface Software and Tech-
nology, pages 1–18, 2022.
[248] C. Gao, X. Lan, Z. Lu, et al. S3: Social-network sim-
ulation system with large language model-empowered
agents, 2023.
[249] Petter T¨ornberg, Diliara Valeeva, Justus Uitermark,
and Christopher Bail.
Simulating social media us-
ing large language models to evaluate alternative news
feed algorithms.
arXiv preprint arXiv:2310.05984,
2023.
[250] Giulio Rossetti, Massimo Stella, R´emy Cazabet,
Katherine Abramski, Erica Cau, Salvatore Citraro, An-
drea Failla, Riccardo Improta, Virginia Morini, and
Valentina Pansanella. Y social: an llm-powered social
media digital twin, 2024.
[251] Xiaoqing Zhang, Xiuying Chen, Yuhan Liu, Jianzhou
Wang, Zhenxing Hu, and Rui Yan.
A large-scale
time-aware agents simulation for influencer selec-
tion in digital advertising campaigns. arXiv preprint
arXiv:2411.01143, 2024.

## Page 35

[252] Rui Xu, Dakuan Lu, Xiaoyu Tan, Xintao Wang, Siyu
Yuan, Jiangjie Chen, Wei Chu, and Xu Yinghui. Min-
decho: Role-playing language agents for key opinion
leaders, 2024.
[253] Ruiyang Ren,
Peng Qiu,
Yingqi Qu,
Jing Liu,
Wayne Xin Zhao, Hua Wu, Ji-Rong Wen, and Haifeng
Wang.
Bases: Large-scale web search user simula-
tion with large language model based agents. arXiv
preprint arXiv:2402.17505, 2024.
[254] Xu Huang, Jianxun Lian, Yuxuan Lei, Jing Yao, Defu
Lian, and Xing Xie. Recommender ai agent: Integrat-
ing large language models for interactive recommen-
dations. arXiv preprint arXiv:2308.16505, 2023.
[255] Jizhi Zhang, Keqin Bao, Wenjie Wang, Yang Zhang,
Wentao Shi, Wanhong Xu, Fuli Feng, and Tat-Seng
Chua. Prospect personalized recommendation on large
language model-based agent platform. arXiv preprint
arXiv:2402.18240, 2024.
[256] Lei Wang, Jingsen Zhang, Xu Chen, Yankai Lin, Rui-
hua Song, Wayne Xin Zhao, and Ji-Rong Wen. Reca-
gent: A novel simulation paradigm for recommender
systems. arXiv preprint arXiv:2306.02552, 2023.
[257] A. Zhang, Y. Chen, L. Sheng, et al.
On generative
agents in recommendation, 2024.
[258] Junjie Zhang, Yupeng Hou, Ruobing Xie, Wenqi Sun,
Julian McAuley, Wayne Xin Zhao, Leyu Lin, and Ji-
Rong Wen. Agentcf: Collaborative learning with au-
tonomous language agents for recommender systems.
In Proceedings of the ACM on Web Conference 2024,
pages 3679–3689, 2024.
[259] Flaminio Squazzoni, Wander Jager, and Bruce Ed-
monds.
Social simulation in the social sciences: A
brief overview.
Social Science Computer Review,
32(3):279–294, 2014.
[260] Marcel Binz and Eric Schulz.
Turning large lan-
guage models into cognitive models. arXiv preprint
arXiv:2306.03917, 2023.
[261] Xinyi Li, Yu Xu, Yongfeng Zhang, and Edward C
Malthouse. Large language model-driven multi-agent
simulation for news diffusion under different network
structures. arXiv preprint arXiv:2410.13909, 2024.
[262] Jacqueline Johnson Brown and Peter H Reingen. So-
cial ties and word-of-mouth referral behavior. Journal
of Consumer research, 14(3):350–362, 1987.
[263] Gueorgi Kossinets and Duncan J Watts. Origins of ho-
mophily in an evolving social network. American jour-
nal of sociology, 115(2):405–450, 2009.
[264] Boxuan Wang, Haonan Duan, Yanhao Feng, Xu Chen,
Yongjie Fu, Zhaobin Mo, and Xuan Di. Can llms un-
derstand social norms in autonomous driving games?
arXiv preprint arXiv:2408.12680, 2024.
[265] Dawei Gao, Zitao Li, Xuchen Pan, Weirui Kuang, Zhi-
jian Ma, Bingchen Qian, Fei Wei, Wenhao Zhang,
Yuexiang Xie, Daoyuan Chen, et al. Agentscope: A
flexible yet robust multi-agent platform. arXiv preprint
arXiv:2402.14034, 2024.
[266] Xuchen Pan, Dawei Gao, Yuexiang Xie, Yushuo Chen,
Zhewei Wei, Yaliang Li, Bolin Ding, Ji-Rong Wen, and
Jingren Zhou.
Very large-scale multi-agent simula-
tion in agentscope. arXiv preprint arXiv:2407.17789,
2024.
[267] Yancheng Wang, Ziyan Jiang, Zheng Chen, Fan Yang,
Yingxue Zhou, Eunah Cho, Xing Fan, Xiaojiang
Huang, Yanbin Lu, and Yingzhen Yang.
Recmind:
Large language model powered agent for recommen-
dation. arXiv preprint arXiv:2308.14296, 2023.
[268] Tian Liang,
Zhiwei He,
Jen-tes Huang,
Wenx-
uan Wang, Wenxiang Jiao, Rui Wang, Yujiu Yang,
Zhaopeng Tu, Shuming Shi, and Xing Wang. Lever-
aging word guessing games to assess the intelli-
gence of large language models.
arXiv preprint
arXiv:2310.20499, 2023.
[269] Emily Dinan, Stephen Roller, Kurt Shuster, An-
gela Fan, Michael Auli, and Jason Weston.
Wiz-
ard of wikipedia: Knowledge-powered conversational
agents, 2019.
[270] Saizheng Zhang, Emily Dinan, Jack Urbanek, Arthur
Szlam, Douwe Kiela, and Jason Weston. Personalizing
dialogue agents: I have a dog, do you have pets too?,
2018.
[271] Maril`u Miotto, Nicola Rossberg, and Bennett Klein-
berg. Who is gpt-3? an exploration of personality, val-
ues and demographics, 2022.
[272] S. Wang, C. Liu, Z. Zheng, et al. Avalon’s game of
thoughts: Battle against deception through recursive
contemplation, 2023.
[273] H. Wang, J. Chen, W. Huang, et al. Grutopia: Dream
general robots in a city at scale, 2024.
[274] J. Browning. Personhood and ai: Why large language
models don’t understand us. AI & Society, pages 1–8,
2023.
[275] A. Radford, J. W. Kim, C. Hallacy, et al. Learning
transferable visual models from natural language su-
pervision. In Proceedings of the International Confer-
ence on Machine Learning, pages 8748–8763. PMLR,
2021.
[276] Haotian Liu,
Chunyuan Li,
Qingyang Wu,
and
Yong Jae Lee. Visual instruction tuning. Advances
in neural information processing systems, 36, 2024.
