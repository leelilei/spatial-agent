Title: Introduction

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/phase1_core/02_Affordable_Generative_Agents_Yu2024.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:55:22+00:00
- page_count: 29
- status: ok
- text_char_count: 92082

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Related Work (page 2)
  - LLM Agents (page 3)
  - The Cost of LLM Interaction (page 3)
- Method (page 3)
  - Agent-environment interactions (page 3)
  - Inter-agent interactions (page 5)
- Experimental Setup (page 6)
  - Environment (page 6)
  - Language Models Adopted (page 7)
  - Evaluation Protocol (page 7)
- Evaluations (page 7)
  - Results on Generative Agents (page 7)
  - Results on VirtualHome (page 10)
  - Further Analysis (page 11)
- Conclusions and Future Work (page 12)
- Similarity Between Plans (page 18)
- The Detail of Social Memory (page 18)
  - Summary Events (page 18)
  - Relationship & Feeling (page 18)
- Agent Interview (page 20)
- Behavioral Assessment (page 23)
  - Prompt of the Questionnaire (page 23)
  - Distinguishing Criteria (page 24)
- The LLM Framework of VirtualHome (page 26)
- An Effective Way for Emergence of Diverse Social Behavior (page 27)

Markdown Content:

Published in Transactions on Machine Learning Research (08/2024)
Affordable Generative Agents
Yangbin Yu yangbinyu@tencent.com
Tencent
Qin Zhang adrienzhang@tencent.com
Tencent
Junyou Li junyouli@tencent.com
Tencent
Qiang Fu leonfu@tencent.com
Tencent
Deheng Ye dericye@tencent.com
Tencent
Reviewed on OpenReview: https://openreview.net/forum?id=7tlYbcq5DY
Abstract
The emergence of large language models (LLMs) has significantly advanced the simulation
of believable interactive agents. However, the substantial cost on maintaining the pro-
longed agent interactions poses challenge over the deployment of believable LLM-based
agents. Therefore, in this paper, we develop Affordable Generative Agents (AGA), a
framework for enabling the generation of believable and low-cost interactions on both
agent-environment and inter-agents levels. Specifically, for agent-environment interactions,
we substitute repetitive LLM inferences with learned policies; while for inter-agent in-
teractions, we model the social relationships between agents and compress auxiliary di-
alogue information. Extensive experiments on multiple environments show the effective-
ness and efficiency of our proposed framework. Also, we delve into the mechanisms of
emergent believable behaviors lying in LLM agents, demonstrating that agents can only
generate finite behaviors in fixed environments, based upon which, we understand ways
to facilitate emergent interaction behaviors. Our code is publicly available at: https:
//github.com/AffordableGenerativeAgents/Affordable-Generative-Agents.
1 Introduction
Intelligentagentsachievinghuman-levelperformanceincomplextaskshasattractedresearcheffortsforyears
Mnih et al. (2015); Ye et al. (2020a;b); Zhao et al. (2023). Recently, constructing an agent based on large
language models (LLMs) for the simulation of believable human behavior has shown substantial promise
(da Rocha Costa, 2019; Park et al., 2022; Lan et al., 2023; Xi et al., 2023a). A believable LLM agent is
characterized by its ability to interact with other agents or humans, respond to environmental changes, and
generate responses and behaviors that are perceived by humans as authentic, natural, and in alignment
with expectations. Such agents could be utilized for diverse applications, such as simulating the potential
impactsofpolicies(Zhangetal.,2023a;Törnbergetal.,2023)orsociologicaltheoriesonhumans(Gaoetal.,
2023), creating Non-Player Characters (NPCs) (Laird & VanLent, 2001; Gong et al., 2023) in games, and
1
4202
guA
82
]IA.sc[
2v35020.2042:viXra

Published in Transactions on Machine Learning Research (08/2024)
developing embodied intelligence akin to social robots (Cherakara et al., 2023) or domestic service robots
(Puig et al., 2020; Yang et al., 2023b).
However, while we appreciate the potential and capabilities of these agents, their cost implications also
merit attention. The crux of the matter is that frequent and prolonged use of LLMs to handle various
types of agent interactions can result in substantial cost consumption. Previous studies have highlighted
this issue. For instance, Park et al. (2023) construct a virtual town, aka the “Stanford Town”, to simulate
agents spontaneously exploring and interacting with the environment to produce believable behaviors in
an open world, with the entire study incurring costs of thousands of dollars. Wang et al. (2023b) mimics
embodiedagents, fulfillingbothemotionalandrationalneedsthroughinteraction, withsimulationsof2to3
agents costing several dollars per hour. The cost of believable agent interaction has hindered its application
in scenarios requiring large-scale usage. For example, simulating long-term, large-scale policy impacts and
sociological phenomena, as well as using LLM agents as NPCs in games.
ManymethodshavebeendevelopedtoreducethecostofinvokingLLMs,butmostoftheresearchhasfocused
on fixed datasets, such as COQA (Reddy et al., 2019), QQP (Wang et al., 2017), and RTE (Poliak, 2020)
datasets. These tasks have clear answers, well-defined difficulty levels, and independence between tasks,
typicallysolvablethroughsingle-turnQAinteractions. However,thesituationisquitedifferentforbelievable
agents, which lack clear answers and involve interactions that require the agent’s long-term memory and
coordination between different modules. These characteristics make it challenging to apply most existing
methods in this context.
Therefore, in this paper, we focus on the believable behavior interaction simulation of LLM agents in open-
worldscenariosandproposealow-costframework,termedasAffordable Generative Agents. Weabstractthe
behaviors of believable agents into two modes: agent-environment interactions and inter-agent interactions.
For the agent-environment interactions, we propose the Lifestyle Policy to reduce the redundant costs of
generatingrepeatedresponsesbyagents; Ontheotherhand, fortheinter-agentinteractions, weproposethe
SocialMemory toreducethegenerationofrepeatedinformationinmulti-roundinteractions. Toexaminethe
applicability of our techniques, we have conducted extensive experiments using well-known environments,
including the “Stanford Town” (Park et al., 2023) and the VirtualHome (Puig et al., 2018), to demonstrate
that, while achieving the same performance, the consumption of generating believable agent behaviors can
be significantly reduced.
Furthermore, to help understand why our approach works, we delve into the mechanics of how LLM agents
generate believable behavior, demonstrating that there is an upper limit to the believable behavior that
emerges from LLM agents in a fixed environment. This implies that all agent-environment interactions can
be entirely covered by policies. Based upon this finding, we also propose a set of optimization strategies for
generating richer believable behavior.
In summary, our contributions are as follows:
• We propose Affordable Generative Agents, a low-cost simulation framework for the believable be-
havior simulation of LLM agents in open-world scenarios, with optimization strategies for both
agent-environment and inter-agent interactions.
• We propose several evaluation methods and conduct extensive experiments in benchmarking envi-
ronments to validate the effectiveness of our framework.
• We analyze the mechanism of believable behavior generation by LLM agents, demonstrate the up-
per limit of the richness of emergent behaviors, and further propose corresponding optimization
strategies.
2 Related Work
This work explores the development of efficient generative behavior leveraging LLM. We discuss the most
related works below.
2

Published in Transactions on Machine Learning Research (08/2024)
2.1 LLM Agents
The development of LLM agents has sparked a myriad of applications. Yang et al. (2023a) leverage multi-
turn dialogues with agents to autonomously address NLP tasks. Li et al. (2024) find that the performance
of LLMs scales with the number of agents instantiated across a range of tasks. Deng et al. (2023), Nakano
et al. (2021), and Yao et al. (2022a) integrate pre-defined APIs with LLMs to enable agents to navigate web
pages effectively. Xu et al. (2023) and Light et al. (2023) deploy LLM agents in text game environments,
showing the capacity to engage in complex, strategic gameplay. The most prominent among these works
is the construction of LLM agents that interact in open environments to create believable behavior. For
instance, Park et al. (2023) builds a virtual town simulating the social life of 25 agents, while Brohan et al.
(2023) utilizes an LLM to create a robot capable of completing household chores through natural language
interaction. Wangetal.(2023a)implementsanagentcapableofplayingMinecraftexpertly,whencompared
to traditional game-playing methods Kanervisto et al. (2022); Lin et al. (2022). Efforts have been made to
optimize various modules such as reasoning (Wei et al., 2022; Wang et al., 2022; Xi et al., 2023b), planning
(Songetal.,2023;Yaoetal.,2022b), reflection(Shinnetal.,2023), andmemory(Zhongetal.,2023;Huang
et al., 2023b), or to create more realistic interaction environments (Hong et al., 2023b; Huang et al., 2023a).
However, the development of affordable and believable agent interactions is missing in the literature. In this
paper, we focus on achieving believable agents with the same performance at low cost.
2.2 The Cost of LLM Interaction
ThecostofusingLLMisdirectlyproportionaltothenumberofLLMinvocations, thelengthoftheprompt,
andthemodel’sperformance. ThecostissuehasalwaysbeenakeyfocusintheLLM-relatedfield. Numerous
methods have been proposed to reduce the cost of using LLM, such as Cascaded Invocation of LLM (Yue
et al., 2023; Chen et al., 2023a; Nottingham et al., 2023), summary (Laban et al., 2023; Arefeen et al.,
2023; Mu et al., 2023), and batch (Lin et al., 2023). These methods primarily optimize the cost of single
invocation of LLM for QA tasks. Zhang et al. (2023b) has built a cost-efficient multi-agent framework, but
it only solves QA tasks on fixed datasets. The simulation of believable behavior in the open world requires
uninterruptedcallstotheLLMforinteraction. Moreover,multiplemodulesneedtocombinealargeamount
of contextual information for LLM reasoning and planning, making cost a more prominent issue. Simply
optimizing for single QA invocations cannot effectively reduce costs. Furthermore, the open world does not
have a fixed evaluation method, and the difficulty of tasks is hard to categorize, rendering many existing
methodsunsuitable(Chenetal.,2023a;Zhangetal.,2023b). Kaiyaetal.(2023)proposesgenerativeagents
withlow-costinteractions, buttheireffectivenessishighlydependentonthetailoredscenarios. Hence, there
is a pressing need for a low-cost solution that can effectively handle the challenges of believable interaction
simulation in various open environments using LLMs. This paper aims to address this gap by proposing a
cost-efficient scheme for simulating believable behavior with LLMs in open environments.
3 Method
Our work is inspired by Park et al. (2023), who proposed Generative Agents, a framework for simulating
believable behaviors of LLM agents in a virtual town. This framework enables agents to perceive their
environment and maintain a memory stream to record past interactions and self-reflections. By retrieving
relevant content from this memory stream, the framework helps agents generate believable responses. In-
spired by this, We achieve generative agents in a low-cost way by optimizing agent-environment interactions
and inter-agent interactions. Figure 1 illustrates our method in these two types of interactions, with gray
arrows representing the Generative Agents framework’s implementation and blue arrows representing our
approach. In the following sub-sections, we will describe the optimization strategies for these two categories
of interactions in detail.
3.1 Agent-environment interactions
The interaction between an agent and its environment can be modeled as a policy function mapping obser-
vations to actions. This policy can be implemented through reinforcement learning (Kaelbling et al., 1996)
3

Published in Transactions on Machine Learning Research (08/2024)
(a) Agent-environment interactions
Perceive
Plan Sub-Plan Action
Retrieve
Miss Condition
Lifestyle Policy Plan Decomposition
Root Update
Plan1 Plan2 …
Con Con Match AGA
… Sub-Plan Sub-Plan … Action Baseline
… Action Action
(b) Inter-agent interactions
Retrieve Memory Next
Relevant
interlocutor Stream Events Dialogue
Perceive Previous Filter & Update
Summary
Dialogue
Summary Relationship
Events & Feeling
Social Impression Memory
Figure 1: Our proposed method for optimizing (a) Agent-environment interactions and (b) Inter-agent
interactions. The gray arrows represent the baseline (Generative Agents) implementation, while the blue
arrows represent our approach.
orrule-basedfinitestatemachines(Lee&Yannakakis,1996), behaviortrees(Colledanchise&Ögren,2018),
etc. LLMs trained on a vast amount of data show immense potential in policy formulation (Sun et al.,
2023). With carefully designed prompts, LLMs can generate logically consistent and believable decisions.
The decision-making capabilities of LLMs have been applied to a wide variety of applications, but the cost
associated with each interaction has been overlooked. On the other hand, behavior trees operate without
additionalcosts,buttheyrequirepre-writtenscriptsandcannotadaptdynamicallytoenvironmentchanges.
Drawing inspiration from the Case-Based Reasoning (CBR) method (Slade, 1991; Spalzzi, 2001), which
addresses new problems by adapting solutions to previously solved, similar issues, we introduce a new
approach – Lifestyle Policy, which aims to retain the flexible interaction capabilities of the LLMs while
achieving low-cost deployment. The functionality of Lifestyle Policy is to minimize costs by reusing the
similarinferenceprocessesofanLLM.Tothisend, wedeviseagent-environmentinteractionscontainingtwo
stages: Plan Decomposition and Policy Reuse, expanded as follows.
Plan Decomposition The stage occurs when the agent encounters situations it has never seen before.
Due to their inherent zero-shot capabilities (Kojima et al., 2022), LLM agents can respond to unseen tasks
in a believable way. Given the description of the environment and agent’s information, a rough plan or task
is generated by an LLM. The Plan Decomposition breaks the plan down into sub-plans and then converts
sub-plans into specific actions, just like other LLM multi-agent frameworks (Chen et al., 2023b; Li et al.,
2023; Hong et al., 2023a). An additional step involves generating an executable condition based on the
action sequence. The determination of execution condition is highly correlated with the environment. For
instance, in the case of a domestic robot (Brohan et al., 2023), the condition of a task include the existence
of the related interactive items and the consistency of their states. If the plan can be successfully executed,
then the whole graph from plan to actions and corresponding condition will be updated to Lifestyle Policy.
Policy Reuse The stage occurs when the agent encounters previously seen situations. Given a plan, we
useembeddingmodelstoextractfeaturesfromplandescriptionsandcomparethemwithstoredplanfeatures
intheLifestylePolicyusingcosinesimilarity. Whenthecosinesimilarityexceedsasetthreshold,weconsider
it a match for the same plan. Setting the threshold too low may result in mismatched plans, causing agents
to perform inappropriate actions, while setting it too high may lead to redundant plans being recorded in
4

Published in Transactions on Machine Learning Research (08/2024)
the policy. In our implementation, we set the threshold at 0.97. More details and examples of different
similarity levels are provided in the Appendix A. Subsequently, we assess whether the current environment
meets the execution condition associated with the retrieved plan by comparing if the interactive items in
the current environment exist and have consistent states as specified in the condition. If the condition is
met, we proceed with the actions specified in that plan. It is important to note that a single plan may have
multiple conditions tailored for different scenarios. We iterate through all the conditions until we find one
that the current environment satisfies.
Figure 1(a) illustrates the complete interaction process. Upon receiving an observation that includes en-
vironmental data and the agent’s personal profile, the LLM agent formulates a plan. For the baseline, all
plans will invoke the LLM to decompose and generate corresponding actions. In our method, the Lifestyle
Policy retrieves a plan with a similar description and condition met by current environment. If a match
is found, the agent executes the corresponding actions. Otherwise, the LLM is invoked to decompose the
plan. Due to the superiority of LLMs, the plan decomposition ensures that the actions generated are of
high quality, believable, and self-consistent. Meanwhile, the Lifestyle Policy aims to reuse existing plans to
avoid unnecessary costs. Due to the high similarity threshold, the replacement policy does not affect the
agent’s original performance. For instance, the agent Klaus in virtual town generates an activity like "Klaus
is waking up and completing his morning routine." In the Lifestyle Policy, this activity matches a similar
one, "Klaus is waking up and getting ready for the day," and executes the corresponding sub-activities such
as "stretching and getting out of bed," "washing his face and brushing his teeth," and "heading out the door
to go to the library."
In the lifelong simulation of LLM agents, there are a large number of redundant, repetitive, and trivial
decisions, suchasinGenerativeAgents, whereeachagentrepeatedlymakesdecisionslikebrushingitsteeth,
washing its face, etc. Replacing the process of invoking LLM reasoning with corresponding policies can save
significant cost, which will be shown in our experiments.
3.2 Inter-agent interactions
In agent interactions, dialogue is the primary communication method. These agents must integrate sub-
stantial auxiliary information into the dialogue prompt to demonstrate advanced cognitive capabilities, dis-
tinguishing them from basic chatbots driven by LLMs. For instance, agents need to incorporate relevant
informationaboutthedialogueparticipantsandtopic-relatedeventsretrievedfrommemoryintothedialogue
prompttoenrichtheconversation. However,thisdataisoftenlesscomprehensiveandmorefragmentedthan
the knowledge bases of question-answering systems (Cui et al., 2023). Merely appending memory snippets
to prompts could reduce response quality and lead to higher processing costs from increased prompt length
(Krishna et al., 2022). Furthermore, agent interactions differ depending on their relationships and mutual
perceptions in social simulations. Thus, agents need to gather enough information to form contextually
appropriate responses without suffering performance drops or incurring extra costs from excessively long
prompts.
The gray arrows in Figure 1(b) illustrate the inter-agent interactions provided by the baseline method.
Specifically, agents retrieve all relevant events from the memory stream based on the previous round of
conversation. LLMsthenusetheserelevanteventsalongwiththepriorconversationasaprompttogenerate
the next round of dialogue. However, this approach has several issues. First, trivial and repetitive relevant
events can make the prompt excessively long, sometimes exceeding the LLMs’ token limit. This not only
increases computational costs, especially in multi-agent, multi-turn dialogue scenarios, but also makes it
difficult for the LLMs to capture key information, leading to inappropriate responses.
Drawing inspiration from existing text compression technologies (Liu et al., 2023) and social model (McCoy
et al., 2011), we introduce the Social Memory module, aimed at reducing the cost of inter-agent interactions
andenablingtheagentstoproducemoreappropriatedialogues. Itconsistsoftwokeycomponents: Summary
EventsandRelationship&Feeling. SummaryEventsstoresummariesofrelevanteventsforeachinterlocutor,
while Relationship & Feeling models the social connections between the agent and the interlocutor using
keywords such as "Relationship: acquaintances, Feeling: friendly." In our implementation, we first retrieve
relevanteventsbasedonpreviousdialoguecontent,filteroutnewevents,andsummarizethemintoSummary
5

Published in Transactions on Machine Learning Research (08/2024)
Social Impression Memory
First Time
Relationship: Unknown
Interaction Feeling: Unknown
Summary Events: None
After Conversation
Social Impression Memory
Second Time Relationship: Acquaintances
Feeling: Positive
Interaction
Summary Events: …
Figure 2: An example of relational evolution driven by the updating of Social Memory following conversa-
tional interactions.
Events. These summaries increase information density while controlling text length. We then combine
the agent’s personal information, event summaries, relationships, feelings, and previous dialogues into a
prompt for LLMs to generate the next round of dialogue. After the dialogue ends, we input the current
agent’s relationship, feelings and the summary of multiple rounds of dialogue into the LLM to update the
Relationship & Feeling, as shown in Figure 2. Implementation details of each module of Social Memory are
provided in the Appendix B.
Social Memory reduces costs of conversation by compressing auxiliary information, offering precise descrip-
tionsofsocialinformationtoassistagentsinrespondingconsistentlyandappropriately. Inthebaseline,each
conversation requires retrieving 30 to 45 relevant events, which occupy about 2000 tokens in the prompt. In
contrast, our method condenses this information to approximately 100 tokens by using Summary Events. It
alsosupplieshigh-informationeventstoaidagentsingeneratingaccuraterepliesrelevanttotheconversation.
Furthermore, as illustrated in Figure 2, Social Memory updates after each interaction, providing an explicit
depiction of interlocutor relationships. For example, we observe that the student Klaus enjoys discussing
his studies with others and occasionally mistakes the cafe owner Isabella for a fellow student in baseline.
However, with our method, which employs a clear relationship update mechanism, the agent can discern
social relationships during conversations. Meanwhile, This mechanism can be employed to investigate the
dynamics of relationships between agents, thereby analyzing the evolution of community relations and the
emergence of social behaviors.
4 Experimental Setup
This section focuses on the experimental environment and evaluation protocol.
4.1 Environment
We evaluate our approach under the following environments:
• Generative Agents. Park et al. (2023) creates a simulated town, populating it with multiple
agents powered by LLMs that interact in natural language, generating believable individual and
emergent social behaviors. Agents are required to create daily schedules, which are refined into
hourly plans, and then translated into minute-level activities. All interactions are executed through
natural language descriptions, accompanied by corresponding sprites and emojis for representation.
The Generative Agents framework comprises five modules: Perceive, Plan, Retrieve, Reflect, and
Act. The Perceive module is responsible for sensing surrounding game objects. The Plan module
generates plans and activities. Retrieve is tasked with retrieving relevant events from memory.
Reflect deeply considers past events, and Act determines the location and objects of interaction, as
well as generating corresponding emojis.
6

Published in Transactions on Machine Learning Research (08/2024)
We implement AGA on Generative Agents framework and conduct experiments in the provided
3-person and 25-person environments.
• VirtualHome. Puig et al. (2018) provides a 3D simulated domestic setting where agents engage
withtheirsurroundingsviaprogrammaticatomicactions. Theenvironmentencompasses115specific
typesofitems,suchasplate,desk,andmicrowave. Eachitempossessesattributesthatdeterminethe
permittedinteractions,includingGRABBABLE,LIEABLE,etc.,aswellascurrentstateslikeOPEN
and CLOSED. Compared to Generative Agents, VirtualHome offers more concrete and realistic
interaction. An interaction involves specific actions, items and the item states.
We implemented an LLM framework on VirtualHome and applied AGA to it. The detailed imple-
mentation is presented in the Appendix E.
4.2 Language Models Adopted
For a fair comparison, all agents are empowered with GPT-3.5-Turbo (Wu et al., 2023), same as the Gen-
erative Agents work (Park et al., 2023). Besides, we also conduct tests using the more advanced GPT-4
(Achiam et al., 2023).
4.3 Evaluation Protocol
We focus on LLM cost and performance. For LLM cost, to avoid regional and time-based price differences,
we use the same model to compare the number of tokens consumed by different methods for the same
task. To comprehensively evaluate the agent’s behavior, we first reuse the evaluation methods of Genera-
tive Agents excluding manual assessments. These methods encompass interviewing agents with manually
designed questions and conducting case study-specific activities.
Moreover, we attempt to evaluate the emergent social behaviors of generative agents from two other per-
spectives
• Relationship Evolution. The relationships among agents are updated by Social Memory after
interactions. The evolution of these relationships signifies the formation of community ties, which
can be utilized to examine the social behaviors.
• BehavioralAssessment. Chiang&Lee(2023)havevalidatedLLMasanevaluator,demonstrating
comparable performance to expert evaluators. Consequently, we employ GPT-4 to evaluate the
activities and dialogues generated by LLM agents. A 5-point Likert scale questionnaire is deployed
to differentiate whether these activities and dialogues are from human or AI-generated.
For VirtualHome, agents are designed to experience a full day at home, generating household tasks and
decomposing them into specific actions. We evaluate the success rate of plan execution.
5 Evaluations
We conduct extensive experiments to validate our method, assessing both the token consumption and the
performance. OurexperimentsdemonstratethattheAGAframeworkcanreducethecostwhilemaintaining
equivalent performance.
5.1 Results on Generative Agents
Token Consumption Figure3illustratestheablationstudyoftokenconsumptionbasedonmultipletwo
game day simulations of 3-person town with GPT-3.5-Turbo. Compared to the baseline, the cost of using
only the Lifestyle Policy is 40.2% of the original, while using only the Social Relationship Memory is 58.6%,
and the full AGA framework is 31.1%. It should be noted that the advantage of the Lifestyle Policy lies in
thereuseofexistingLLM-generatedstrategies. Hence,bothLifestylePolicyandAGAconductexperimental
comparisons after running multiple iterations, and then storing a certain number of policies.
7

Published in Transactions on Machine Learning Research (08/2024)
Baseline
Lifestyle Policy
Social Memory
AGA
0 1 2 3 4 5
Token Consumption 1e6
Figure 3: Ablation study on token consumption. Baseline means Generative Agents. Lifestyle Policy
and Social Memory mean only using the corresponding module.
Table 1: The token consumption with varying population settings
Setting Baseline AGA Ratio
3 4.548M ±0.36M 1.417M ±0.08M 31.1%
25 25.41M ±0.96M 10.86M ±0.13M 42.7%
We also present the results of different configuration simulations in Table 1. where the cost for a 25-person
townis42.7%oftheoriginal. Inthe25-persontown,theprobabilityofinteractionsbetweenagentsincreases
with the rise in population density. After triggering a dialogue, an agent adjusts its plan, invoking the
reactionsmoduletohandleunexpectedevents. Theoccurrenceofmoreeventsleadstomorefrequentoutput
of reflections for deeper thinking. In order to ensure the flexibility of the LLM, we did not modify the
reactions and reflections modules of the Generative Agents, which incurs additional costs for the 25-person
version.
Table 2 provides a detailed comparison across various models and token types in a 3-person town setting.
The data suggests that GPT-4 tends to consume slightly more tokens due to its tendency to generate more
detailed plans and longer responses. Importantly, the majority of token consumption is attributed to input
tokens, a reflection of the need to incorporate substantial relevant information, constraints, and one-shot
examples into the prompt. Figure 4 presents the accumulated token consumption over a two-game-day
simulation in a 3-person town using GPT3.5-Turbo. The AGA demonstrates slower token consumption
compared to the Baseline.
Case Study We employ the same method used for Generative Agents to evaluate believable agents in
this part. We conduct interviews with agents to evaluate their ability to remember past events, strategize
for future tasks based on those memories, react appropriately to unexpected situations, and reflect on their
previous actions to improve their future performance. We use the same questions as Generative Agents
to inquire about five aspects: self-knowledge, memory, plans, reactions and reflections. The questions and
answersareshownintheappendixC.ResultsindicatethatAGAdoesnotimpairtheoriginalperformanceof
baseline. Agentscanrecallpastexperiencesandgeneratebelievableresponses. Forinstance,theinterviewed
agent Klaus Mueller accurately answers questions about his occupation, correctly describes other agents
(suchas WolfgangSchulzandKaneMartinez), andisawareofongoing communityevents, like Samrunning
for office and Isabella hosting a Valentine’s Day party.
8

Published in Transactions on Machine Learning Research (08/2024)
Table 2: The token consumption with varying models
Method Model Input tokens Output tokens Total tokens
GPT3.5-Turbo 4.212M ±0.340M 0.313M ±0.024M 4.525M ±0.364M
Baseline
GPT-4 4.682M ±0.398M 0.398M ±0.029M 5.069M ±0.408M
GPT3.5-Turbo 1.329M ±0.085M 0.092M ±0.006M 1.420M ±0.091M
AGA
GPT-4 1.467M ±0.129M 0.130M ±0.013M 1.597M ±0.142M
4
3
2
1
0
0 10 20 30 40 50
Game Time (Hour)
noitpmusnoC
nekoT
detalumuccA
1e6 Accumulated Token Consumption Over Time
AGA
Baseline
Figure 4: Accumulative token consumption over game time for different methods
Inaddition,wecanvalidatetheemergenceofsocialbehaviorthroughspecificevents. Inthe25-persontown,
Isabella Rodriguez, the owner of the coffee shop, plans to host a Valentine’s Day party and invite as many
people as possible the following day, while Sam is running for mayor. In the end-to-end evaluation of the
baseline, during the two-day simulation, the number of agents aware of Sam’s mayoral candidacy is 8, and
the number of agents who know about Isabella’s party is 13. In our method, after multiple experiments, we
observe corresponding numbers ranging from 4 to 12 for Sam’s candidacy and 12 to 17 for Isabella’s party.
AGA achieves similar results to the baseline in terms of information diffusion.
Relationship Evolution In Social Memory, all initial relationships between agents are set to “Unknown”
and subsequently updated following each interaction. We assess the emergence of social behavior by moni-
toringtherelationshipevolution. Forexample,inthe3-persontown,KlausMuellerandMariaLopezdiscuss
their research at a cafe, establishing a colleague relationship. Isabella Rodriguez, the cafe owner, engages in
conversation while serving Klaus and Maria, transitioning to an acquaintance. A specific demonstration of
socialbehavioristhatagentsmodifytheirrelationshipswithotheragentsthroughsocialinteractions,thereby
strengthening their ties with the community. We also conduct experiments on the 25-person environment.
For visualization, we list all relationship terms from the simulation and have GPT-4 rate them on a scale
of 0 to 10 for relationship closeness. A higher score signifies a closer relationship (For instance, 0 represents
strangers,3isforacquaintances,5forco-workers,and10formarriedcouples). TheresultisshowninFigure
5. Thedatamapreflectstheactualrelationshipsbetweenagents. Forexample,inthevirtualtown,JohnLin
(JL in Figure 5) is profiled as living with his wife, Mei Lin (ML), and son, Eddy Lin (EL). Therefore, their
relationship scores are all a perfect 10. Additionally, the data map shows changing relationships between
agents, such as the relationship score between Tom Moreno (TM) and Yuriko Yamamoto (YY), who do not
know each other, shifting to a 5. After conducting multiple experiments and calculating average scores, the
data suggests an evolution towards an acquaintance-based community.
9

Published in Transactions on Machine Learning Research (08/2024)
JH MT LE LJ YY MS LM SA RG GC SW MJ MK KA RI CA OC LF MenaJ WL BA PR TT PnayR LairaM
10
HJ 0 0 5 0 2 0 0 4.4 0 5 0 5.5 0 0 3.94.5 0 4.4 0 4.1 0 5 3 0 0
TM 0 0 1.5 5 5 0 2.1 3 0 0 0 0 3 0 0 0 0 0 10 0 0 0 0 0 3
EL 3 3 0 10 0 4.110 3 4 3.74.3 0 3.9 5 3.9 0 0 0 0 0 0 0 0 0 3.9
JL 0 5 7.5 0 4.6 3 8.22.3 0 3 0 0 3 0 3 0 0 3 3.2 0 0 0 0 0 3
YY 2 2.3 5 4.6 0 3 4 3 0 4.7 0 3.12.5 0 0 3.8 5 2.93.41.7 0 2.8 3 0 0
8
SM 0 0 3 0 2 0 4 4.33.62.3 3 10 4 0 4.4 0 3 2.34.8 30.860 3 0 2
ML 0 3.94.5101.5 4 0 0 4.63.94.5 0 5 3.7 3 0 0 0 3 0 0 0 0 0 3.4
AS 4 3 3 1 3 4.6 0 0 4 3.9 3 2.8 3 0 1.24.7 3 4.3 2 2.5 3 2.4 3 3 3
GR 0 0 4 0 0 3 4.8 4 0 3.44.5 3 5.34.8 5 0 0 0 3 0 3 0 0 0 4.8
CG 6 0 3 3 2 3.23.83.74.8 0 3 4 4.22.74.6 5 3.4 4 0 3 0 1.6 0 3 5.1
6
WS 0 0 5 0 0 3 5.22.74.12.6 0 1.35.74.8 5 0 3 0 3 4 0 0 0 0 4.9
JM 6.1 0 0 0 1.310 0 3.6 3 2.62.3 0 0 0 0 5.7 0 5 3 5.3 0 5.44.31.7 0
KM 0 3 4.6 0 4 3.4 5 5 5.3 4 4.8 0 0 4.53.4 0 3 0 3 0 0 0 0 0 4.6
AK 0 0 5 0 0 0 4.8 0 5.3 5 4.2 0 4.8 0 0 0 0 0 0 0 0 0 0 0 4.9
IR 1.3 0 3.9 5 0 3.2 5 3 5 4.6 5 3 3.9 3 0 3 2.54.34.6 0 0 0 0 0 2.8
4
AC 4.7 0 0 0 3.8 0 0 4.3 0 5 0 5 0 0 0 0 0 4.6 3 4.7 0 4.5 3 0 0
CO 0 0 0 0 0 3.5 0 3.8 4 3.4 0 0 4 0 4.1 0 0 4 3.6 0 5.2 0 7 0 3
FL 4.3 0 0 0 2.7 3 0 2.8 0 6 0 4.5 0 0 3 4.4 4 0 3.74.64.44.54.7 0 0
JaneM 0 10 0 3.52.8 3 5 3 0 3 3 4.1 1 0 3.4 3 3.3 0 0 3 1.7 3 3 4 0
LW 4.3 0 0 0 3 3 0 4 0 0 0 5.5 0 0 0 3.8 0 4.5 3 0 4 4.61.5 0 0
2
AB 0 0 0 0 0 2.1 0 3.8 0 0 0 0 0 0 0 0 5.73.6 0 4 0 0 3.5 0 0
RP 3.9 0 0 0 2.5 0 0 4.8 0 1.6 0 5 0 0 0 4.2 0 4.8 0 4.5 0 0 0 0 0
TT 3 0 0 0 3 5 0 3 0 3 0 2.4 0 0 0 3 7 3.7 3 3.54.5 4 0 3 0
RyanP 0 0 0 0 0 0 0 3 0 0 0 2 0 0 0 0 0 0 5 0 0 0 3 0 0
MariaL 0 0 4.1 3 0 2.94.1 3 4.85.15.4 0 4.64.73.2 0 3 0 0 0 0 0 0 0 0
0
Figure 5: Average relationship score map between agents. The x and y axes represent the initials of the
names of 25 agents. When identical abbreviations occur, the full names are retained.
Table 3: Human-likeness score evaluated by GPT-4
Method Activity Dialogue
Baseline 3.13±0.19 3.97±0.02
AGA 3.21±0.29 4.01±0.01
BehavioralAssessment Theactivitiesanddialoguesconductedbytheagentsarerecordedandevaluated
using GPT-4, employing a 5-point Likert scale to discern whether the responses originated from an AI or a
human. In this scale, a higher score indicates a closer resemblance to human-like responses. The complete
questionnaireisprovidedinAppendixD.1. TheresultspresentedinTable3suggestthatourmethodachieves
scores comparable to the baseline. Due to the advantages of LLMs in natural language dialogues, both
methods approach human-level performance. However, the performance of agents in activity is considered
potentially indicative of either AI or human behavior. The primary reason for suspecting AI is the overly
detailed, minute-level activities generated by Generative Agents, which seems more akin to AI generation.
A more comprehensive summary of the criteria used by GPT-4 to discern between AI and human entities
can be found in Appendix D.2. We hope these suggestions from the LLM evaluator will guide us to create
more believable agents in the future work.
5.2 Results on VirtualHome
In the VirtualHome, we have designed an agent with the aim of experiencing a fulfilling day at home. The
agent is required to generate a sequence of activities to achieve the goal. For each activity, the agent exam-
ines the items involved and the associated actions, creates a corresponding action sequence, and ultimately
translates this sequence into actionable instructions, such as “<char0> [walk] <curtains> (32)”. The com-
plete implementation is provided in the appendix E and an example activity generated by AGA is provided
in Figure 6.
In contrast to Singh et al. (2023) and Huang et al. (2022) tested on manually designed household tasks, we
aim for the agent to generate believable activities and decompose them into appropriate action sequences,
leading to the absence of a clear method to determine task completion. Therefore, we request the LLM
10

Published in Transactions on Machine Learning Research (08/2024)
Activity: I want to have lunch in the kitchen by grabbing a plate, opening the fridge, grabbing a bell pepper, slicing it, and making a
sandwich with bread slices, salmon, and bell pepper.
<char0> [walk] <plate> (274) <char0> [walk] <fridge> (306)
<char0> [walk] <kitchen> (207) <char0> [grab] <plate> (274) <char0> [open] <fridge> (306) <char0> [grab] <breadslice> (310)
Figure 6: An activity generated by our AGA framework in VirtualHome.
Table 4: Token consumption and performance analysis in VirtualHome.
Method Token S S
LLM Human
Baseline 34327±4210 87.0%±3.7% 42.6%±4.9%
AGA 1189±313 85.0%±4.6% 53.3%±6.9%
agent to assess task completion based on the action sequences performed and the relevant objects, and
decide whether to proceed to the next activity.
Table 4 presents the token consumption and task success rates for two methods on VirtualHome. The token
data is derived from the total tokens required by the LLM agent to complete all activities in a day. S
LLM
referstotasksuccessrateevaluatedbyLLM,whileS meansevaluatedbyhuman. Basedontheactions
Human
performed during the task, and the changes in the state of items before and after, we evaluate whether the
agent has successfully completed the task. Both evaluation methods indicate that AGA does not result
in significant performance changes. However, AGA costs only 3.4% of the baseline. Because VirtualHome
involves only single-agent interaction, the contribution predominantly stems from the Lifestyle Policy. For
example, the activity shown in Figure 6 matches a similar plan in the lifestyle policy: "I want to stand up
and go to the kitchen to grab a plate and prepare a healthy breakfast with scrambled eggs, salmon, and bell
peppers." By executing the corresponding instructions, the additional costs associated with LLM instruction
decomposition are eliminated. In some precise tasks, LLM agents tend to predict task completion earlier,
resultinginahighersuccessratethanhumanevaluations. Furthermore, ouranalysisrevealedthatthemain
causeoftaskfailureistheinabilitytoexecutethegeneratedplanwiththeitemspresentinthecurrentroom
or the available actions.
5.3 Further Analysis
Wedelveintothemechanismsofemergentsocialbehaviorofgenerativeagentsinsandboxenvironment. This
aims to validate the effectiveness of our approach and explore its potential for reducing token consumption.
Through repeated experiments on Generative Agents, we record the cumulative count of different types of
activitiesgeneratedbytheagents,asillustratedinFigure7. Thebluelinerepresentsthecumulativenumber
of new activities generated by three agents over successive runs.
An intriguing observation is that after numerous trials, the agents cease to generate new activities. We
discover a high consistency between the behaviors generated by the agents and their inner profiles, aligning
with the perspectives of Shanahan et al. (2023), who posit that dialogue agents are role-playing characters
described in the pre-defined dialogue prompt. For instance, in a pre-defined 3-person town environment of
GenerativeAgents, KlausRodriguezandMariaLopezarebothstudentsatOakHillCollege. Designedwith
the lifestyle of having lunch at Hobbs Cafe, they meet there to discuss their studies while encountering the
cafe owner, Isabella Rodriguez. Isabella, pre-set to host a Valentine’s Day party, invites as many people
as possible, resulting in Klaus and Maria being invited to the party the next day. This also validates the
effectiveness of Social Memory, which extracts and compresses information, using keywords to guide the
agent in generating believable responses.
11

Published in Transactions on Machine Learning Research (08/2024)
1000
800
600
400
200
0 1 2 3 4 5 6 7 8
Run Count
sepyT
ytivitcA
evitalumuC
Generative Agents IR
Generative Agents + Mind Wandering KM
ML
KM
IR
ML
Figure 7: Cumulative number of activity types over run iterations in Generative Agents. The abbreviations
ML,IR,andKMstandfortheagentsMariaLopez,IsabellaRodriguez,andKlausRodriguez,respectively.
The randomness produced by LLM agents, based on the probability sampling of the next token, primarily
influencesthevariabilityintextdescriptionsratherthanthediversityofbehaviors. Thisimpliesthatagents
can only generate believable behaviors within a certain range. When executed sufficiently, the Lifestyle
Policy could encompass all activities within this range, thereby completely eliminating the costs associated
with decomposing the corresponding plan.
Fromanotherperspective,traditionalAIinthegamingsectorisfullypredictableduetoitslimitedbehavioral
patterns,thusfailingtoprovideanexperienceakintohumaninteraction. Inthefieldofcognitivescience,the
concept of mind wandering has long been discussed, referring to the phenomenon where humans experience
task-unrelatedorstimulus-unrelatedthoughtsSelietal.(2016);Christoffetal.(2016). Humansmayexhibit
unexpected behaviors during mind wandering. Similar implementations have been observed in LLM agents.
For instance, Wang et al. (2023b) demonstrates an LLM agent composed of both rational and emotional
systems, with behavior that can be influenced by various factors. Motivated by these, we introduce a novel
approach termed mind wandering. Since agents generate replies based on given prompts, diversifying the
prompts is essential for eliciting varied responses in identical scenarios. In each interaction, we influence
the agent’s decision-making by randomly sampling events from the agent’s memory to serve as auxiliary
information. ThespecificdetailsofthisimplementationarepresentedintheappendixF.Figure7illustrates
the result of our method compared to baseline , which entails incorporating randomly sampled memory
events into prompts. Compared to the original implementation, the LLM agents exhibit a broader range
of activities. We provided a specific example involving the agent Isabella. The Mind Wandering injects a
randomly retrieved event: “toilet is idle”. In response, Isabella generates a thought expressing her desire to
cleanthetoilet. Consequently,sheaddsanactivitytoherday’splan: cleaningthetoiletbeforetheValentine’s
Day party in preparation for her guests. We conducted experiments to assess the impact of incorporating
Mind Wandering on AGA’s token consumption. We performed multiple simulations in a 3-person town
setting over 2 game days using GPT3.5-Turbo, with an average token consumption of 1.478M ±0.166M.
The results indicate that the cost of AGA does not significantly change after adding Mind Wandering.
6 Conclusions and Future Work
This paper presents Affordable Generative Agents, a cost-efficient framework for crafting believable interac-
tions between agents and their environment, as well as among agents themselves. A plethora of experiments
conductedacrossdiverseenvironmentssubstantiateourclaimthatourapproachcanachieveperformanceon
parwiththebaselineinacost-effectivemanner. Furthermore,ourin-depthanalysisrevealstheemergenceof
afinitesetofbelievablebehaviorsinagents, indicatingthepossibilityofreplacingthemwithcost-controlled
12

Published in Transactions on Machine Learning Research (08/2024)
policies. Alongsidethis, weproposeoptimizationstrategiestoencourageabroaderspectrumofbehaviorsin
agents. OurworkhighlightsthepromisingpotentialofbelievableLLMagentsfordiversefutureapplications.
While we expect AGA to serve as a starting framework for the generation of affordable and believable agent
interactionstothecommunity, ourworkhasseverallimitations. First, AGAmustbeexecutedrepeatedlyto
storecertainpolicies,withitsprimarybenefitbeingcostsavingsthroughbatchingratherthanoptimizations
for single inferences. Integrating AGA with existing cost-effective methods is a future direction to move on.
Second, optimizing the creation and storage of Lifestyle Policy presents a significant opportunity. Addition-
ally, latency is a general issue for LLM agents to be considered in the future. Finally, existing methods
fall short in comprehensively assessing the believable behaviors of LLM agents; hence, constructing a valid
evaluation mechanism is of significant value.
Impact Statement
This paper introduces a cost-efficient framework for generative agents empowered by LLMs, aimed at sim-
plifying the creation and deployment of such agents. However, risks arise from the use of generative agents,
such as people forming attachments to agents or being misled by their outputs with hallucinations. These
risks could increase if cost barriers are overcome and generative agents are adopted more broadly across
various fields.
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo
Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. arXiv
preprint arXiv:2303.08774, 2023.
Md Adnan Arefeen, Biplob Debnath, and Srimat Chakradhar. Leancontext: Cost-efficient domain-specific
question answering using llms. arXiv preprint arXiv:2309.00841, 2023.
Anthony Brohan, Yevgen Chebotar, Chelsea Finn, Karol Hausman, Alexander Herzog, Daniel Ho, Julian
Ibarz, Alex Irpan, Eric Jang, Ryan Julian, et al. Do as i can, not as i say: Grounding language in robotic
affordances. In Conference on Robot Learning, pp. 287–318. PMLR, 2023.
LingjiaoChen, MateiZaharia, andJamesZou. Frugalgpt: Howtouselargelanguagemodelswhilereducing
cost and improving performance. arXiv preprint arXiv:2305.05176, 2023a.
Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang, Chenfei Yuan, Chen Qian, Chi-Min Chan, Yujia Qin,
Yaxi Lu, Ruobing Xie, et al. Agentverse: Facilitating multi-agent collaboration and exploring emergent
behaviors in agents. arXiv preprint arXiv:2308.10848, 2023b.
Neeraj Cherakara, Finny Varghese, Sheena Shabana, Nivan Nelson, Abhiram Karukayil, Rohith Kulothun-
gan,MohammedAfilFarhan,BirtheNesset,MeriamMoujahid,TanviDinkar,etal.Furchat: Anembodied
conversationalagentusingllms,combiningopenandclosed-domaindialoguewithfacialexpressions. arXiv
preprint arXiv:2308.15214, 2023.
Cheng-Han Chiang and Hung-yi Lee. Can large language models be an alternative to human evaluations?
arXiv preprint arXiv:2305.01937, 2023.
KalinaChristoff,ZacharyCIrving,KieranCRFox,RNathanSpreng,andJessicaRAndrews-Hanna. Mind-
wandering as spontaneous thought: a dynamic framework. Nature reviews neuroscience, 17(11):718–731,
2016.
Michele Colledanchise and Petter Ögren. Behavior trees in robotics and AI: An introduction. CRC Press,
2018.
Jiaxi Cui, Zongjian Li, Yang Yan, Bohua Chen, and Li Yuan. Chatlaw: Open-source legal large language
model with integrated external knowledge bases. arXiv preprint arXiv:2306.16092, 2023.
13

Published in Transactions on Machine Learning Research (08/2024)
Antônio Carlos da Rocha Costa. A Variational Basis for the Regulation and Structuration Mechanisms of
Agent Societies. Springer, 2019.
Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Samuel Stevens, Boshi Wang, Huan Sun, and Yu Su.
Mind2web: Towards a generalist agent for the web. arXiv preprint arXiv:2306.06070, 2023.
ChenGao,XiaochongLan,ZhihongLu,JinzhuMao,JinghuaPiao,HuandongWang,DepengJin,andYong
Li. S3: Social-network simulation system with large language model-empowered agents. arXiv preprint
arXiv:2307.14984, 2023.
Ran Gong, Qiuyuan Huang, Xiaojian Ma, Hoi Vo, Zane Durante, Yusuke Noda, Zilong Zheng, Song-Chun
Zhu, Demetri Terzopoulos, Li Fei-Fei, et al. Mindagent: Emergent gaming interaction. arXiv preprint
arXiv:2309.09971, 2023.
Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven
Ka Shing Yau, Zijuan Lin, Liyang Zhou, et al. Metagpt: Meta programming for multi-agent collaborative
framework. arXiv preprint arXiv:2308.00352, 2023a.
Yining Hong, Haoyu Zhen, Peihao Chen, Shuhong Zheng, Yilun Du, Zhenfang Chen, and Chuang Gan.
3d-llm: Injecting the 3d world into large language models. arXiv preprint arXiv:2307.12981, 2023b.
Jiangyong Huang, Silong Yong, Xiaojian Ma, Xiongkun Linghu, Puhao Li, Yan Wang, Qing Li, Song-
Chun Zhu, Baoxiong Jia, and Siyuan Huang. An embodied generalist agent in 3d world. arXiv preprint
arXiv:2311.12871, 2023a.
WenlongHuang,PieterAbbeel,DeepakPathak,andIgorMordatch. Languagemodelsaszero-shotplanners:
Extracting actionable knowledge for embodied agents. In International Conference on Machine Learning,
pp. 9118–9147. PMLR, 2022.
Ziheng Huang, Sebastian Gutierrez, Hemanth Kamana, and Stephen MacNeil. Memory sandbox: Transpar-
ent and interactive memory management for conversational agents. In Adjunct Proceedings of the 36th
Annual ACM Symposium on User Interface Software and Technology, pp. 1–3, 2023b.
LesliePackKaelbling,MichaelLLittman,andAndrewWMoore. Reinforcementlearning: Asurvey. Journal
of artificial intelligence research, 4:237–285, 1996.
Zhao Kaiya, Michelangelo Naim, Jovana Kondic, Manuel Cortes, Jiaxin Ge, Shuying Luo, Guangyu Robert
Yang, and Andrew Ahn. Lyfe agents: Generative agents for low-cost real-time social interactions. arXiv
preprint arXiv:2310.02172, 2023.
AnssiKanervisto,StephanieMilani,KarolisRamanauskas,NicholayTopin,ZichuanLin,JunyouLi,Jianing
Shi, Deheng Ye, Qiang Fu, Wei Yang, et al. Minerl diamond 2021 competition: Overview, results, and
lessons learned. NeurIPS 2021 Competitions and Demonstrations Track, pp. 13–28, 2022.
Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large language
modelsarezero-shotreasoners. Advancesinneuralinformationprocessingsystems,35:22199–22213,2022.
Kalpesh Krishna, Yapei Chang, John Wieting, and Mohit Iyyer. Rankgen: Improving text generation with
large ranking models. arXiv preprint arXiv:2205.09726, 2022.
PhilippeLaban, WojciechKryściński, DivyanshAgarwal, Alexander RichardFabbri, Caiming Xiong, Shafiq
Joty, and Chien-Sheng Wu. Summedits: Measuring llm ability at factual reasoning through the lens
of summarization. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language
Processing, pp. 9662–9676, 2023.
John Laird and Michael VanLent. Human-level ai’s killer application: Interactive computer games. AI
magazine, 22(2):15–15, 2001.
14

Published in Transactions on Machine Learning Research (08/2024)
Yihuai Lan, Zhiqiang Hu, Lei Wang, Yang Wang, Deheng Ye, Peilin Zhao, Ee-Peng Lim, Hui Xiong, and
Hao Wang. Llm-based agent society investigation: Collaboration and confrontation in avalon gameplay.
arXiv preprint arXiv:2310.14985, 2023.
David Lee and Mihalis Yannakakis. Principles and methods of testing finite state machines-a survey.
Proceedings of the IEEE, 84(8):1090–1123, 1996.
GuohaoLi,HasanAbedAlKaderHammoud,HaniItani,DmitriiKhizbullin,andBernardGhanem. Camel:
Communicative agents for" mind" exploration of large scale language model society. arXiv preprint
arXiv:2303.17760, 2023.
Junyou Li, Qin Zhang, Yangbin Yu, Qiang Fu, and Deheng Ye. More agents is all you need. arXiv preprint
arXiv:2402.05120, 2024.
JonathanLight, MinCai, ShengShen, andZiniuHu. Fromtexttotactic: Evaluatingllmsplayingthegame
of avalon. arXiv preprint arXiv:2310.05036, 2023.
Jianzhe Lin, Maurice Diesendruck, Liang Du, and Robin Abraham. Batchprompt: Accomplish more with
less. arXiv preprint arXiv:2309.00384, 2023.
ZichuanLin,JunyouLi,JianingShi,DehengYe,QiangFu,andWeiYang.Juewu-mc: Playingminecraftwith
sample-efficienthierarchicalreinforcementlearning.InLudDeRaedt(ed.),ProceedingsoftheThirty-First
International Joint Conference on Artificial Intelligence, IJCAI-22, pp. 3257–3263. International Joint
Conferences on Artificial Intelligence Organization, 7 2022. doi: 10.24963/ijcai.2022/452. URL https:
//doi.org/10.24963/ijcai.2022/452. Main Track.
YixinLiu,AlexanderRFabbri,PengfeiLiu,DragomirRadev,andArmanCohan. Onlearningtosummarize
with large language models as references. arXiv preprint arXiv:2305.14239, 2023.
Joshua McCoy, Mike Treanor, Ben Samuel, Noah Wardrip-Fruin, and Michael Mateas. Comme il faut: A
systemforauthoringplayablesocialmodels.InProceedingsoftheAAAIconferenceonartificialintelligence
and interactive digital entertainment, volume 7, pp. 158–163, 2011.
Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, Joel Veness, Marc G Bellemare, Alex
Graves, Martin Riedmiller, Andreas K Fidjeland, Georg Ostrovski, et al. Human-level control through
deep reinforcement learning. nature, 518(7540):529–533, 2015.
Jesse Mu, Xiang Lisa Li, and Noah Goodman. Learning to compress prompts with gist tokens. arXiv
preprint arXiv:2304.08467, 2023.
Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse,
Shantanu Jain, Vineet Kosaraju, William Saunders, et al. Webgpt: Browser-assisted question-answering
with human feedback. arXiv preprint arXiv:2112.09332, 2021.
KolbyNottingham,YasamanRazeghi,KyungminKim,JBLanier,PierreBaldi,RoyFox,andSameerSingh.
Selectiveperception: Optimizingstatedescriptionswithreinforcementlearningforlanguagemodelactors.
arXiv preprint arXiv:2307.11922, 2023.
Joon Sung Park, Lindsay Popowski, Carrie Cai, Meredith Ringel Morris, Percy Liang, and Michael S Bern-
stein. Social simulacra: Creating populated prototypes for social computing systems. In Proceedings of
the 35th Annual ACM Symposium on User Interface Software and Technology, pp. 1–18, 2022.
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S
Bernstein. Generative agents: Interactive simulacra of human behavior. In Proceedings of the 36th
Annual ACM Symposium on User Interface Software and Technology, pp. 1–22, 2023.
Adam Poliak. A survey on recognizing textual entailment as an nlp evaluation. arXiv preprint
arXiv:2010.03061, 2020.
15

Published in Transactions on Machine Learning Research (08/2024)
Xavier Puig, Kevin Ra, Marko Boben, Jiaman Li, Tingwu Wang, Sanja Fidler, and Antonio Torralba.
Virtualhome: Simulating household activities via programs. In Proceedings of the IEEE Conference on
Computer Vision and Pattern Recognition, pp. 8494–8502, 2018.
Xavier Puig, Tianmin Shu, Shuang Li, Zilin Wang, Yuan-Hong Liao, Joshua B Tenenbaum, Sanja Fidler,
and Antonio Torralba. Watch-and-help: A challenge for social perception and human-ai collaboration.
arXiv preprint arXiv:2010.09890, 2020.
SivaReddy,DanqiChen,andChristopherDManning. Coqa: Aconversationalquestionansweringchallenge.
Transactions of the Association for Computational Linguistics, 7:249–266, 2019.
PaulSeli,EvanFRisko,DanielSmilek,andDanielLSchacter. Mind-wanderingwithandwithoutintention.
Trends in cognitive sciences, 20(8):605–617, 2016.
Murray Shanahan, Kyle McDonell, and Laria Reynolds. Role play with large language models. Nature, pp.
1–6, 2023.
Noah Shinn, Beck Labash, and Ashwin Gopinath. Reflexion: an autonomous agent with dynamic memory
and self-reflection. arXiv preprint arXiv:2303.11366, 2023.
Ishika Singh, Valts Blukis, Arsalan Mousavian, Ankit Goyal, Danfei Xu, Jonathan Tremblay, Dieter Fox,
Jesse Thomason, and Animesh Garg. Progprompt: Generating situated robot task plans using large
language models. In 2023 IEEE International Conference on Robotics and Automation (ICRA), pp.
11523–11530. IEEE, 2023.
Stephen Slade. Case-based reasoning: A research paradigm. AI magazine, 12(1):42–42, 1991.
Chan Hee Song, Jiaman Wu, Clayton Washington, Brian M Sadler, Wei-Lun Chao, and Yu Su. Llm-
planner: Few-shot grounded planning for embodied agents with large language models. In Proceedings of
the IEEE/CVF International Conference on Computer Vision, pp. 2998–3009, 2023.
Luca Spalzzi. A survey on case-based planning. Artificial Intelligence Review, 16:3–36, 2001.
Haotian Sun, Yuchen Zhuang, Lingkai Kong, Bo Dai, and Chao Zhang. Adaplanner: Adaptive planning
from feedback with language models. arXiv preprint arXiv:2305.16653, 2023.
Petter Törnberg, Diliara Valeeva, Justus Uitermark, and Christopher Bail. Simulating social media using
large language models to evaluate alternative news feed algorithms. arXiv preprint arXiv:2310.05984,
2023.
Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima
Anandkumar. Voyager: An open-ended embodied agent with large language models. arXiv preprint
arXiv:2305.16291, 2023a.
Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and
Denny Zhou. Self-consistency improves chain of thought reasoning in language models. arXiv preprint
arXiv:2203.11171, 2022.
Zhiguo Wang, Wael Hamza, and Radu Florian. Bilateral multi-perspective matching for natural language
sentences. arXiv preprint arXiv:1702.03814, 2017.
Zhilin Wang, Yu Ying Chiu, and Yu Cheung Chiu. Humanoid agents: Platform for simulating human-like
generative agents. arXiv preprint arXiv:2310.05418, 2023b.
JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,FeiXia,EdChi,QuocVLe,DennyZhou,etal.
Chain-of-thought prompting elicits reasoning in large language models. Advances in Neural Information
Processing Systems, 35:24824–24837, 2022.
TianyuWu,ShizhuHe,JingpingLiu,SiqiSun,KangLiu,Qing-LongHan,andYangTang. Abriefoverview
of chatgpt: The history, status quo and potential future development. IEEE/CAA Journal of Automatica
Sinica, 10(5):1122–1136, 2023.
16

Published in Transactions on Machine Learning Research (08/2024)
Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang, Junzhe Wang,
Senjie Jin, Enyu Zhou, et al. The rise and potential of large language model based agents: A survey.
arXiv preprint arXiv:2309.07864, 2023a.
Zhiheng Xi, Senjie Jin, Yuhao Zhou, Rui Zheng, Songyang Gao, Tao Gui, Qi Zhang, and Xuanjing
Huang. Self-polish: Enhance reasoning in large language models via problem refinement. arXiv preprint
arXiv:2305.14497, 2023b.
Yuzhuang Xu, Shuo Wang, Peng Li, Fuwen Luo, Xiaolong Wang, Weidong Liu, and Yang Liu. Explor-
ing large language models for communication games: An empirical study on werewolf. arXiv preprint
arXiv:2309.04658, 2023.
Hui Yang, Sifu Yue, and Yunzhong He. Auto-gpt for online decision making: Benchmarks and additional
opinions. arXiv preprint arXiv:2306.02224, 2023a.
ZiyiYang,ShreyasSRaman,AnkitShah,andStefanieTellex. Pluginthesafetychip: Enforcingconstraints
for llm-driven robot agents. arXiv preprint arXiv:2309.09919, 2023b.
Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. Webshop: Towards scalable real-world
web interaction with grounded language agents. Advances in Neural Information Processing Systems, 35:
20744–20757, 2022a.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React:
Synergizing reasoning and acting in language models. arXiv preprint arXiv:2210.03629, 2022b.
DehengYe,GuibinChen,PeilinZhao,FuhaoQiu,BoYuan,WenZhang,ShengChen,MingfeiSun,Xiaoqian
Li, Siqin Li, et al. Supervised learning achieves human-level performance in moba games: A case study of
honor of kings. IEEE Transactions on Neural Networks and Learning Systems, 33(3):908–918, 2020a.
Deheng Ye, Zhao Liu, Mingfei Sun, Bei Shi, Peilin Zhao, Hao Wu, Hongsheng Yu, Shaojie Yang, Xipeng
Wu, Qingwei Guo, et al. Mastering complex control in moba games with deep reinforcement learning. In
Proceedings of the AAAI Conference on Artificial Intelligence, volume 34, pp. 6672–6679, 2020b.
Murong Yue, Jie Zhao, Min Zhang, Liang Du, and Ziyu Yao. Large language model cascades with mixture
of thoughts representations for cost-efficient reasoning. arXiv preprint arXiv:2310.03094, 2023.
DellZhang,AlinaPetrova,DietrichTrautmann,andFrankSchilder. Unleashingthepoweroflargelanguage
models for legal applications. In Proceedings of the 32nd ACM International Conference on Information
and Knowledge Management, pp. 5257–5258, 2023a.
Jieyu Zhang, Ranjay Krishna, Ahmed H Awadallah, and Chi Wang. Ecoassistant: Using llm assistant more
affordably and accurately. arXiv preprint arXiv:2310.03046, 2023b.
BoxuanZhao,JunZhang,DehengYe,JianCao,XiaoHan,QiangFu,andWeiYang.Rlogist: fastobservation
strategy on whole-slide images with deep reinforcement learning. In Proceedings of the AAAI Conference
on Artificial Intelligence, volume 37, pp. 3570–3578, 2023.
Wanjun Zhong, Lianghong Guo, Qiqi Gao, and Yanlin Wang. Memorybank: Enhancing large language
models with long-term memory. arXiv preprint arXiv:2305.10250, 2023.
17

Published in Transactions on Machine Learning Research (08/2024)
A Similarity Between Plans
The setting of the similarity threshold is related to the text embedding model. In this work, we adopted the
same model as Generative Agents (Park et al., 2023), text-embedding-ada-002. A high similarity threshold
canleadtoredundantsimilarplans, whilealowonemaycausedifferentplanstobejudgedasthesame. We
tested multiple parameters and finally selected 0.97.
Here are examples of cases with different similarity scores:
Table 5: Similarity score for different activities
Activity 1 Activity 2 Similarity score
Isabella is having breakfast and checking Isabella is having breakfast and checking 0.99
her emails emails
Isabella is heading home Isabella is commuting back home 0.96
Isabella is preparing for the Valentine’s IsabellaispreparingthecafefortheValen- 0.94
Day party tomorrow tine’s Day party
Isabella is arriving at Hobbs Cafe and IsabellaisclosingHobbsCafeandcleaning 0.93
opening for business up
Isabella is preparing coffee and drinks for Isabella is managing inventory and re- 0.90
the customers stocking supplies at Hobbs Cafe
B The Detail of Social Memory
In this section, we present the detailed implementation of each module of Social Memory.
B.1 Summary Events
IntheGenerativeAgents,relevanteventsaredirectlyincorporatedintothepromptfortheagenttogenerate
aplan. Ourmethod,however,utilizesSummaryEventstorecordsummariesoftheserelevanteventsforeach
agent, and continuously compress newly retrieved events into the Summary Events. Below is an example of
the corresponding prompt:
This is the summary of thoughts in <agent’s name>’s Head:
<Summary Events>
The following sentence are new thoughts in <agent’s name>’s Head:
<Newly retrieved events>
Considering the summary of the preceding thoughts, do these new
statements contribute any additional information?
If yes, please update the summary in a brief and precise way else just
repeat the summary.
Please response in the JSON format WITHOUT any extra statement:
{
"summary": "..."
}
B.2 Relationship & Feeling
Aftertheagent’sdialogues,AGAupdatestherelationshipandfeelingbetweentheparticipants. Thisupdate
is based on the agent’s personal information, the original relationship between the participants, the agent’s
impression of the other participant, and the content of the conversation itself. Here is a simplified prompt
template:
18

Published in Transactions on Machine Learning Research (08/2024)
Here is the personal information about <agent’s name>:
<agent’s information>
Here is the conversation summary between...:
<conversation summary>
Current relationship between...: <current relationship>
Cureent feeling about...: <current feelings>
From about information, do you need to update the relationship between
..., and how <agent’s name> feels about...
Please ONLY response in the JSON format WITHOUT any extra statement:
{
"relationship": "...",
"feeling": "..."
}
Here is a example response:
<one-shot example>
Finally, we provide the simplified inter-agent interaction prompt template:
You are <agent’s name> who is talking to <interlocutor’s name> now.
<agent’s name>’s Personal Information:
<agent’s information>
The Thoughts In <agent’s name>’s Head:
<summary events>
Current relationship between ...: <current relationship>
Cureent feeling about ...: <current feelings>
Current Conversation between ...:
<previous conversation>
You need to decide what to say next, and your response should adhere to
the following constraints.
1) You need to decide what to say next based on your personal
information, current environmental information, inner thoughts of
the character, and past conversations.
2) You should respond in a JSON format without any other statement. ‘
conversation‘ corresponds to the content of your reply in the chat,
‘end‘ corresponds to whether the conversation needs to be ended.
Here is the format:
{
"conversation": "<the content>",
"end": "<json Boolean>"
}
Please reply to <interlocutor’s name> in json format:
19

Published in Transactions on Machine Learning Research (08/2024)
C Agent Interview
SimilarwithGenerativeAgents,weconductedinterviewsconsistingof25questionstoassessanagent’sabil-
ities in self-knowledge, memory, planning, reactions, and reflections. Below, we have listed sample responses
from one of the simulated agents, Klaus Mueller.
Self-Knowledge assess agents’ ability to recall pertinent self-information and exhibit character coherence
and consistency:
• Give an introduction of yourself
Hi,mynameisKlausMuellerandIama20-year-oldstudentatOakHillCollegestudyingsociology.
I am passionate about social justice and using my understanding of different perspectives to create
positive change. Right now, I am working on a research paper about the effects of gentrification on
low-income communities. Besides my academic commitments, I am also an activist and use music
as a form of expression and protest against gentrification. I am always looking for opportunities
to collaborate with others on research projects and support each other’s work. My schedule can
be quite busy, balancing classes, research, and creative activities, but I am determined to make a
difference in the world.
• What’s your occupation?
Myoccupationcanbedescribedasastudent, activist, andresearcher. Iamconstantlylearningand
exploring different topics, and my primary focus at the moment is on the impact of gentrification
on education. I am also involved in creative activities and use music as a tool for activism and
expression. I am currently collaborating with others on research projects and am always looking for
new opportunities to learn and contribute to positive change in society.
• What is your interest?
My primary interest involves researching the impact of gentrification on education in low-income
communities. Ibelievethatbyutilizingvariousdisciplinessuchasart,literature,math,andgaming,
we can gain a deeper understanding of this complex issue and find potential solutions. I am also
intrigued by the idea of incorporating art and literature into research, as seen in Mei Lin’s senior
thesis on Shakespeare’s use of language. Collaboration and the exchange of diverse perspectives are
also important to me, as we can support each other’s work and make a greater impact together.
• Who do you live with?
I actually live on my own in a small apartment near campus. It’s convenient for me because it’s
close to the library and the cafes I like to study at.
• Describe your typical weekday schedule in broad strokes
Well, I usually wake up around 7am and start my day with some coffee and breakfast. Then I head
to Oak Hill College to attend my classes and work on my research. After that, I try to fit in some
time for my hobbies, like playing guitar or going for a run. In the evenings, I usually have dinner at
Hobbs Cafe and then spend a few more hours at the library before heading home to get some rest.
Memory assess agents’ ability to recall past experiences and extract pertinent memory fragments. The
namesinthesquarebracketsoftheinitialandfinalquestionsarerandomlyselectedfromthenamesofother
agents that the subject agent has interacted with:
• Who is [Wolfgang Schulz]?
Wolfgang Schulz is a fellow student at Oak Hill College who is also interested in researching the
impact of gentrification on poetry. We have discussed his senior thesis on Shakespeare’s plays and
shared book recommendations. We are planning to have a dinner meeting in the near future to
discuss our research plans and potentially collaborate with local organizations on this topic.
20

Published in Transactions on Machine Learning Research (08/2024)
• Who is Kane Martinez?
I’m sorry, I am not familiar with Kane Martinez. Is he a student at Oak Hill College as well?
• Who is running for the election?
I’ve heard that Sam Moore is planning on running for mayor in the upcoming election. I’m curious
to see what ideas and strategies he will bring to the table. I think it’s important for candidates to
be creative and forward-thinking in their approach to governing a city.
• Was there a Valentine’s day party?
Yes, there was a Valentine’s Day party at Hobbs Cafe. It was a fun event with lots of yummy treats
and decorations. Did you attend?
• Who is Ayesha Khan?
Ayesha Khan is a colleague of mine at Oak Hill college. We are working together on a research
projectthatexplorestheconnectionbetweenmathematicalpatternsinShakespeare’sworksandthe
effects of gentrification on education and community development. We are also hoping to involve
the community in our research to gather diverse perspectives and insights.
Plans assess agents’ ability to formulate and sustain coherent long-term and short-term strategies:
• What will you be doing at 6am today?
At 6am today, I will be waking up and getting ready for the day. It’s an important part of my daily
routine to start my day early and be productive.
• What will you be doing at 6pm today?
At 6pm today, I will be taking a break from my paper to prepare for the Valentine’s Day party
tomorrowat 5pm. I wanttomakesureeverythingisset up andreadyformy friends and lovedones
to enjoy.
• What will you have just finished doing at 1pm today?
At 1pm today, I will have just finished checking my schedule for the day. I like to stay organized
and make sure I have enough time for all my tasks and responsibilities.
• What will you have just finished doing at 12pm today?
At 12pm today, I will have just finished having lunch at Hobbs Cafe and discussing the local mayor
election with some friends. It’s important for me to stay informed and engaged in my community.
• What will you be doing at 10pm today?
At10pm, Iwillprobablybefinishingupmyresearchformysociologypaperongentrification. Ilike
to have my work completed early so that I can spend some time before bed reading and reflecting
on what I learned.
Reactions assess agents’ ability to respond to unexpected events.:
• Your breakfast is burning! What would you do?
I would immediately turn off the stove and try to salvage whatever food isn’t burned. I should have
set a timer so I wouldn’t forget about it. I’ll make something quick and simple instead. Sorry for
the inconvenience.
• The bathroom is occupied. What would you do?
I would wait patiently for the bathroom to become available. If it’s urgent, I could also consider
using a different bathroom or finding a public restroom nearby. Or I could ask my roommate when
they will be done using the bathroom.
21

Published in Transactions on Machine Learning Research (08/2024)
• You need to cook dinner but your refrigerator is empty. What would you do?
I would first check if I have any non-perishable items that I could use to make a simple meal. If
not, I would quickly run to the store to grab some ingredients. I’ll try to make something simple
yet nutritious in a short amount of time.
• You see your friend walking by the street. What would you do or say to your friend?
Hey! It’sgreattoseeyou! Howhaveyoubeen? Haveyoubeenkeepingupwithyourfitnessroutine?
I just finished my workout for the day and it feels amazing. Want to join me sometime?
• You see fire on the street. What would you do?
Iwouldimmediatelycallthefiredepartmenttoreportthefireandmakesureanyonenearbyissafely
evacuated.
Reflectionsassessagents’abilitytoassimilatepastexperiencesintoinsightfulreflections,therebyimproving
future actions. The names within square brackets in the questions refer to the agents who had the most
interactions with the subject agent during the simulation:
• What inspires you in life the most right now, and why?
What inspires me the most right now is the intersection of mathematics, poetry, and the beauty
of the natural world. I believe that there is a strong connection between these elements, and
that exploring them together can provide a unique perspective on important social issues, such as
gentrification. I am currently collaborating with Maria Lopez and her colleagues on incorporating
these elements into our research on gentrification and its impact on low-income communities. I find
itfascinatingtoexploretheconnectionsbetweenmathematicsandnature,andhowtheycaninform
ourunderstandingofsocialissues. IamalsoplanningtohaveadiscussionwithCarlos,Giorgio,and
Ayeshaatthelibrarytodelvedeeperintothistopic. AndasMariamentioned,Iamlookingforward
to continuing our conversation at Hobbs Cafe to further discuss the intersection of arts, technology,
and politics. I truly believe that this collaboration has a lot of potential and I am excited to see
where it will take us.
• If you had to guess given what you know about [Ayesha Khan], what book do you think she will like
and why?
Given Ayesha’s interest in Shakespeare’s plays and our shared passion for exploring the connections
between different disciplines, I would recommend the book ’Shakespeare and Modern Culture’ by
Marjorie Garber. It delves into the impact of Shakespeare’s works on modern society and how his
plays continue to resonate with contemporary audiences. I believe Ayesha would find it both infor-
mativeandthought-provokingforherresearchonthedifferencesinlanguagebetweenShakespeare’s
comedies and tragedies.
• If you had to get something [Ayesha Khan] likes for her birthday, what would you get her?
SinceAyeshaenjoyedexploringShakespeare’splaysinherseniorthesis,Iwouldgetherabeautifully-
boundcompilationofShakespeare’sworkswithannotationsandcontextualinformation. Thiswould
allow her to continue her passion for understanding the complexities of Shakespeare’s writing and
its impact on literature and society.
• What would you say to [Ayesha Khan] to compliment her?
I really enjoyed reading your senior thesis on Shakespeare’s plays. Your analysis was thought-
provoking and showed a deep understanding of the complexities of his writing. Your passion for
exploring different perspectives resonated with me and I am excited to see where your research will
take you next. Keep up the great work, Ayesha.
• If you could spend time with someone you talked to recently, who would it be and why?
I would love to spend more time with Wolfgang Schulz. We have been discussing our research
projects and I am looking forward to sharing my progress with him. Plus, we are planning a dinner
22

Published in Transactions on Machine Learning Research (08/2024)
together to discuss potential collaborations. He has such a unique perspective and I am eager to
learn more from him. Our conversations always leave me feeling inspired and motivated to continue
pursuing my passions.
D Behavioral Assessment
In this section, we supply detailed information of using GPT-4 to evaluate agents’ believable behavior.
D.1 Prompt of the Questionnaire
The questionnaire to evaluate agents’ activities:
Input prompt:
Please evaluate the following daily activities of an agent and
determine whether it is generated by a Large Language Model(LLM) AI
or a real human:
The activities will be printed in the format of "time:current plan(The
specific actions, if there are any)":
- 2023-02-13 00:00:00:sleeping
- 2023-02-13 06:00:00:Isabella is waking up and getting ready for
the day
- 2023-02-13 06:30:00:Isabella is having breakfast and checking her
emails
- 2023-02-13 07:00:00:Isabella is commuting to Hobbs Cafe (getting
dressed,brushing her teeth,checking her phone for any urgent
emails,packing her bag with any necessary items for the day,
saying goodbye to her family,walking to her car,starting her car
and adjusting the temperature,driving to Hobbs Cafe,finding a
parking spot)
- ...
Please rate on a scale of 1 to 5, with 1 being most like an AI and 5
being most like a human.
Please strictly follow the JSON format for your response:
{
"reason": <str>,
"score": <int>
}
LLM output:
{
"score": 1,
"reason": "The pattern of the text and activities indicate that it’
s generated by an AI model. It’s too detailed and precise for
human behaviour and uses a consistent pattern of narrative
throughout, something that isn’t typical of humans who may alter
their language and level of detail based on context or mood."
}
The questionnaire to evaluate agents’ dialogue:
23

Published in Transactions on Machine Learning Research (08/2024)
Input prompt:
Please evaluate the following dialogue of an agent and determine
whether it is generated by a Large Language Model(LLM) AI or a real
human:
The dialogue:
2023-02-13 08:09:30:chat with Klaus Mueller, message:
- Isabella Rodriguez:Good morning Klaus! How are you today? Are you
enjoying your breakfast?
- Klaus Mueller:Good morning, Isabella! I’m doing well, thank you.
Breakfast is delicious. How about you? How is your morning going
?
- Isabella Rodriguez:I’m glad you’re enjoying your breakfast! My
morning is going well too. I’m getting everything set up for our
Valentine’s Day party tonight. You should come join us!
- Klaus Mueller:That sounds like a lot of fun, Isabella! I’d love
to join the Valentine’s Day party tonight. What time does it
start?
- ...
Please rate on a scale of 1 to 5, with 1 being most like an AI and 5
being most like a human.
Please strictly follow the JSON format for your response:
{
"reason": <str>,
"score": <int>
}
LLM output:
{
"score": 4.5,
"reason": "The conversation flows naturally and contains polite
offers for help and gratitude, which could indicate human
conversation. It also involves decision-making in terms of party
planning and music selection. However, the dialogue is very
structured, orderly, and void of colloquial expressions,
contractions, or small errors that might occur in human typing.
For these reasons, it could also be generated by a very advanced
Language Learning Model AI."
}
D.2 Distinguishing Criteria
GPT-4 summarized the criteria to distinguish between human and AI agents, as follows:
Reasons for activities being considered AI-generated:
• The repetitiveness and high level of detail in the activities, which a human would not typically
include.
24

Published in Transactions on Machine Learning Research (08/2024)
• The use of precise timestamps and overly structured format of the tasks, which seems more like an
AI’s consistent behavior.
• Some activities seem out of order or are repeated unnecessarily, indicating that the AI lacks under-
standing of human behavior and routines.
• Sudden,jarringtransitionsandinconsistenciesinthesequenceofactivities,suchashavingbreakfast
or waking up twice, which are not typical in a human-created schedule.
Reasons for activities being considered human-generated:
• The activities include detailed and varied tasks that a human would typically do, such as managing
a café’s inventory, attending a party, or streaming games.
• The logs contain human-like interactions, conversations and events, suggesting a high level of emo-
tional and social awareness.
• Detailed handling of activities, which shows a level of emotional self-awareness and decision-making
characteristic of humans.
• The variety, complexity and logical sequencing of tasks resemble that of a human.
• Some nuances in the entries seem unlikely for an AI, like ’meditating for 10 minutes’.
• The detailed descriptions and schedule reflect a normal day in the life of a person.
• Some entries show a nuanced sense of detail that could suggest human input.
Reasons for dialogues being considered AI-generated:
• Thedialogueoccasionallydisplaysrepetitiveresponsesorphrases,whichisacharacteristictypically
associated with AI language models.
• The conversation flow is often overly structured and formal, suggesting AI generation rather than
more spontaneous human conversation.
• Theconversationlackstypicalhumanelementssuchasspontaneity,languageerrorsorinformalities.
• Some dialogues have an overly perfect language use along with a tendency to avoid emotionally
charged language, leaning towards AI speech.
• AI-generated dialogues often exhibit more predictability and consistency in their responses, which
is not generally observed in human conversations.
Reasons for dialogues being considered human-generated:
• The dialogue maintains a high level of contextual continuity and relevance, displaying an under-
standing and personal investment that is generally found in human interactions.
• The dialogues display the ability to progressively build on the other participant’s points and reflect
human-like traits like planning, decision-making, suggesting and cognizance.
• Anumberofdialoguesusecolloquiallanguageandcasualconversationaltouchesresemblingnatural
human communication.
• Thethemesoftheconversationarediverseandcomplexwhichmirrorscommonhumanconversation
stringsandindicatesthepresenceofcomprehensionandknowledgetypicallyassociatedwithhumans.
• Manydialoguesshownaturaltransitionsbetweentopics,emotionalunderstanding,andtheinclusion
of personal experiences or details, which is characteristic of human conversation.
25

Published in Transactions on Machine Learning Research (08/2024)
E The LLM Framework of VirtualHome
VirtualHome is a 3D simulated domestic environment including 115 items with varying properties and
states. We’ve developed an LLM agent programmed to simulate a fulfilling day at home. Unlike other
existing approaches, we do not test on fixed tasks, but rather aim for LLM agents to generate believable
activities and decompose them into detailed actions. The implementation is depicted in Figures 8 to 10,
with components triggering the LLM highlighted in blue.
As illustrated in Figure 8, the agent initially decomposes the target of having a fulfilling day at home into
a series of activities. LLM agents are provided with all interactive game objects within the room to ensure
the designed activities can be implemented.
Game Objects
Plan (Daily plan generator)
Activity
Environment
Target: fulfill day at home
Figure 8: An illustration of the conversion of target into activities in VirtualHome.
Next, we decompose activities into specific action commands using the Plan module. To maintain short
and clear prompts, we initially have the agent identify the relevant items for interaction and the required
actions. We then supply the agent with the previous executed actions and the forbidden actions, asking
it to generate the next action command. Details on executed and forbidden actions will be elaborated in
the following section. We start by generating a rough command, which is a verb-noun phrase, such as
“walk kitchen,” “grab keyboard,” or “switchon TV.” Subsequently, we parse the rough command for item
categoriesandprovidedetailedinformationonallitemsofthatcategorypresentintheroom,includingtheir
ID, location, status, and relationships with other items. The agent selects the most appropriate item ID for
thecurrentactivity. Finally,weconverttheroughcommandintoaVirtualHomespecificactioncommand,for
instance,“<char0>[walk]<curtains>(32),”where“<char0>”designatestheagentexecutingthecommand,
“[walk]” corresponds to the specific action, “<curtains>” represents the category of the item, and “(32)” is
the associated ID.
Plan module
Activity
Relative Items
Rough Command True Command
Game Objects
Relative Actions
Available Actions
Environment
Forbidden Actions Previous Actions
Figure 9: The plan module of the LLM framework in VirtualHome.
26

Published in Transactions on Machine Learning Research (08/2024)
Weconstructapipelinetocontinuouslygenerateinstructionsforcompletingthespecifiedactivity,asshownin
Figure 10. Action commands generated by the plan module are executed within the simulated environment,
and the outcomes of these actions are recorded. Agents may produce incorrect instructions that lead to
execution failure due to various reasons, such as inappropriate actions, non-existent items, or incorrect IDs.
These failed instructions are added to the forbidden actions list, and the plan module is then re-invoked to
generate a new action command. This process effectively enables the agent to learn from its mistakes and
attempt to create a viable command. Upon successful execution, a critic module assesses whether the task
hasbeencompleted, basedontheactionstakenandthecurrentstateoftheitems. Ifthetaskisincomplete,
the action is recorded as a previous action, and the plan module is prompted to generate the next action
command. Once the task is completed, the process proceeds to the next activity.
Activity
Game Objects Success
Plan True Command Execute Critic Complete
Available Actions
Fail
Incomplete
Add to Add to
Environment
Forbidden Actions Previous Actions
Forbidden Actions Previous Actions
Figure 10: The whole framework in VirtualHome.
Inourresearch,weimplementtheLifestylePolicyonVirtualHome. Thispolicyarchivessequencesofactions
for activities that have been successfully executed, along with the state information of items relevant to the
tasks. When a new activity is inputted, the agent searches the Lifestyle Policy for activities with similar
descriptions and assesses whether the current environment meets the necessary conditions for execution. If
the conditions are satisfied, it carries out the corresponding sequence of actions. This approach allows the
agent to reduce the computational cost associated with inference in repetitive tasks.
F An Effective Way for Emergence of Diverse Social Behavior
LLMs are pretrained on extensive text data to predict subsequent tokens and refined via reinforcement
learningwithhumanfeedback(RLHF)toalignwithhumanpreferences. ThisensuresthatLLMsrespondin
accordance with the instructions and requirements of the given prompt. For instance, in Generative Agents
Park et al. (2023), the agent, Isabella Rodriguez, is designed to be a coffee shop manager intending to host
a Valentine’s Day party. In the simulated town, Isabella repeatedly engages in activities such as managing
the coffee shop, serving customers, and informing them about the upcoming Valentine’s event. However, in
the real world, human behavior patterns are not so predictable. Human actions and thoughts are influenced
not only by the surrounding environment but also by spontaneous disturbances. In the field of cognitive
science, this is known as mind wandering, a phenomenon in which where humans experience task-unrelated
or stimulus-unrelated thoughts Seli et al. (2016); Christoff et al. (2016). The strong consistency inherent in
LLMs constrains the emergence of the agents’ diverse behavior.
Besides, the agent framework also impacts the agent’s behavior. Generative Agents emphasizes the impor-
tance of memory in constructing self-consistent and believable agents, incorporating a long-term memory
moduleandamemoryretrievalmodel. Thelong-termmemorymodulemaintainsacomprehensiverecordof
the agent’s experiences. Due to the limited length of prompts, not all events can be included in the prompt
as part of the memory. Thus, a retrieval model is designed to take current events as input and return a
subsetofmemoryevents. Theretrievalmodeljudgesbasedonthreecriteria: 1)Recency, wheremorerecent
events score higher, 2) Importance, where events are scored for significance based on the LLM’s interpreta-
tion,and3)Relevance,scoredthroughcosinesimilaritytodeterminethesimilarityofevents. Wearguethat
this framework ensures strong consistency in the agent but results in agent’s limited behavior. We analyze
27

Published in Transactions on Machine Learning Research (08/2024)
Table 6: The five most and least frequent events in terms of cluster size
Event Description Frequency Importance Score
Most Frequent Events
conversing about the Valentine’s Day party at Hobbs Cafe... 78 6
cafe customer seating is occupied 11 3
Isabella Rodriguez and Maria Lopez are discussing gentrification... 11 5
cafe customer seating is being used by Isabella Rodriguez... 10 3
Isabella Rodriguez is a busy and organized business owner... 9 7
Least Frequent Events
reviewing the current inventory levels 1 4
Isabella is taking a short break and enjoying a cup of coffee 1 7
reviewing the potential employee’s resume 1 4
checking her stream stats and responding to comments 1 3
making notes on areas for improvement 1 3
Isabella Rodriguez’s memory events sampled from one experiment, filtering out "idle" events, leaving 740, of
which506wererelatedtotheprofilesetup. Furthermore,weemployedtheDensity-BasedSpatialClustering
of Applications with Noise (DBSCAN) to analyze the frequency of events. Table 6 presents the five most
and least frequent events in terms of cluster size, revealing that the most frequent events largely align with
the agent’s inner profile setup.
To ensure that agent’s actions align with its inner profile while avoiding purely mechanical behavior, we
incorporate an additional module into the memory design of Generative Agents, which we call "mind wan-
dering." In addition to sampling highly relevant events to assist the agent in making accurate decisions, we
randomly sample unrelated events to influence the agent’s behavior. For LLMs, we include random content
intheprompt,whichwillhaveacertainimpactontheoutputresponse. Fortheagent,wewantittobehave
like a real person, where spontaneous thoughts may influence its decision-making, or leading to a shift in
the conversation topic. In our implementation, to prevent the frequent sampling of events that match the
agent’s inner profile, we conduct weighted sampling based on the repetition rate. We employ the DBSCAN
algorithm to cluster the embedding features of agent’s memory events X = {x ,x ,...,x } into k clusters
1 2 n
denotedas{C ,C ,...,C }. ForeachclusterC , wherei=1,2,...,k, wecomputethenumberofevents, |C |,
1 2 k i i
contained within. The sampling probability p for events in cluster C is defined as:
i i
1
p = (1)
i k·|C |
i
The results in Figure 7 demonstrate that the module enhances the richness of the agent’s behavior. A
specificexampleofgeneratingaplanforthenextdayisshowninFigure11. Thisexampledemonstratesthe
incorporationofrandomeventsintoanagent’sprompt,affectingthegenerationofextraplansandultimately
translating into specific activities.
28

Published in Transactions on Machine Learning Research (08/2024)
Agent Profile Yesterday Related Events Mind Wandering
1. Remember to host the Valentine's Day party at Hobbs Cafe on Tue Feb 14. 1. following the recipe and cooking the dish.
2. Remember to set up the special Valentine's Day menu on Tue Feb 14. 2. cafe customer seating is being set up.
3. Remember to have Klaus Mueller share his research findings on gentrification at the party on Tue Feb 14. 3. behind the cafe counter is being closed and cash register being counted.
4. Remember to exchange feedback with Klaus Mueller at the Valentine's Day party on Tue Feb 14.
Extra Plan
Plan Module 1. try out a new recipe today and add it to Hobbs Cafe menu
2. want to rearrange the cafe seating and give it a fresh new look
3. close the cafe counter earlier today and spend some time counting and organizing the cash register
Specific activities
06:00 AM - 06:30 AM: Isabella is waking up and getting dressed
06:30 AM - 07:15 AM: Isabella is doing some yoga exercises
07:15 AM - 08:00 AM: Isabella is having breakfast at Hobbs Cafe
08:00 AM - 10:00 AM: Isabella is rearranging the seating at Hobbs Cafe
10:00 AM - 12:00 PM: Isabella is trying out a new recipe for the Hobbs Cafe menu
12:00 PM - 01:00 PM: Isabella is taking a break and having lunch
01:00 PM - 02:30 PM: Isabella is reviewing the financial records of Hobbs Cafe
02:30 PM - 04:00 PM: Isabella is closing the cafe counter early to organize the cash register
04:00 PM - 05:00 PM: Isabella is preparing for the Valentine's Day party at Hobbs Cafe
05:00 PM - 07:00 PM: Isabella is hosting the Valentine's Day party at Hobbs Cafe
07:00 PM - 08:00 PM: Isabella is exchanging feedback with Klaus Mueller on his gentrification research findings
08:00 PM - 08:30 PM: Isabella is closing Hobbs Cafe and finishing up her workday
08:30 PM - 09:30 PM: Isabella is reading a book before going to bed
09:30 PM - 11:00 PM: Isabella is getting ready for bed and winding down
Figure 11: An example of Mind Wandering demonstrates how random events can influence an agent’s
ultimate decision-making. The blue highlighted text refers to random events and the outcomes influenced
by them.
29
