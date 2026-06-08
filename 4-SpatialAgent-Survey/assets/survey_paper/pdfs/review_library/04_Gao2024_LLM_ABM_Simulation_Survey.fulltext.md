Title: Large language models empowered agent-based modeling and simulation: a survey and perspectives

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/review_library/04_Gao2024_LLM_ABM_Simulation_Survey.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:58:16+00:00
- page_count: 24
- status: ok
- text_char_count: 158282

Metadata:
- author: Chen Gao
- doi: 10.1057/s41599-024-03611-3
- keywords: unknown
- subject: Humanities and Social Sciences Communications, doi:10.1057/s41599-024-03611-3

Outline:
- Large language models empowered agent-based modeling and simulation: a survey and perspectives (page 1)
  - Introduction (page 1)
    - Discussions on PRISMA (page 2)
  - Background (page 2)
    - Agent-based simulation (page 2)
      - Basic concepts of agent-based simulation (page 2)
        - D1 (page 2)
        - D2 (page 2)
        - D3 (page 3)
      - Agent capability (page 3)
        - D4 (page 3)
        - D5 (page 3)
        - D6 (page 3)
        - D7 (page 3)
      - Applications of agent-based modeling and simulation (page 3)
        - D8 (page 3)
        - D9 (page 3)
        - D10 (page 3)
        - D11 (page 3)
      - Methodologies of agent-based modeling and simulation (page 4)
      - Limitations (page 4)
        - D12 (page 4)
        - D13 (page 4)
        - D14 (page 4)
    - Large language models and LLM-empowered agents (page 4)
  - Critical abilities of LLM for agent-based modeling and simulation (page 5)
    - Perception (page 5)
    - Reasoning and decision making (page 5)
    - Adaptive learning and evolution (page 6)
    - Heterogeneity and personalizing (page 6)
      - An example of a better understanding (page 6)
  - Challenges and approaches of LLM agent-based modeling and simulation (page 7)
    - Environment construction and interface (page 7)
      - Environment: define the world and rules (page 7)
      - Interface (page 7)
    - Human alignment and personalization (page 7)
      - Human alignment (page 7)
        - D15 (page 7)
        - D16 (page 8)
      - Personalization (page 8)
        - D17 (page 8)
        - D18 (page 8)
    - How to simulate actions (page 8)
      - Planning (page 8)
      - Memory (page 8)
      - Reflection (page 9)
    - Evaluation of LLM agents (page 9)
      - Realness validation with real human data (page 9)
      - Provide explanations for simulated behaviors (page 9)
      - Ethics evaluation (page 9)
  - Recent advances in LLM agent-based modeling and simulation (page 10)
    - Social domain I: social sciences (page 10)
      - Simulation of social network dynamics (page 10)
      - Simulation of cooperation (page 13)
      - Simulation of individual social behavior (page 13)
    - Social domain II: economic system (page 14)
      - Individual economic behavior simulation (page 14)
      - Interactive economic behavior simulation (page 15)
      - Economic system-level simulation (page 15)
    - Physical domain (page 16)
      - LLM agents for simulating mobility behaviors (page 16)
      - LLM agent-based modeling and simulation for transportation (page 16)
      - LLM agent-based modeling and simulation for wireless network (page 16)
    - Cyber domain (page 16)
    - Hybrid domain (page 17)
  - Open problems and future directions (page 17)
    - Efficiency of scaling up (page 17)
    - Benchmark (page 17)
    - Open platform (page 18)
    - Robustness of LLM-driven agent-based simulation (page 18)
    - Ethical risks in LLM agents (page 19)
  - Conclusion (page 19)
  - Data availability (page 19)
  - References (page 19)
  - References (page 19)
  - Acknowledgements (page 23)
  - Author contributions (page 23)
  - Competing interests (page 23)
  - Additional information (page 23)

Markdown Content:

REVIEW ARTICLE
https://doi.org/10.1057/s41599-024-03611-3 OPEN
Large language models empowered agent-based
modeling and simulation: a survey and perspectives
Chen Gao1, Xiaochong Lan1,2, Nian Li1,2, Yuan Yuan1,2, Jingtao Ding1,2,
✉
Zhilun Zhou1,2, Fengli Xu1,2 & Yong Li 1,2
Agent-basedmodelingandsimulationhaveevolvedasapowerfultoolformodelingcomplex
systems, offering insights into emergent behaviors and interactions among diverse agents.
Recently, integrating large language models into agent-based modeling and simulation
presents a promising avenue for enhancing simulation capabilities. This paper surveys the
landscape of utilizing large language models in agent-based modeling and simulation,
discussing their challenges and promising future directions. In this survey, since this is
an interdisciplinary field, we first introduce the background of agent-based modeling and
simulationandlargelanguagemodel-empoweredagents.Wethendiscussthemotivationfor
applying large language models to agent-based simulation and systematically analyze the
challenges in environment perception, human alignment, action generation, and evaluation.
Mostimportantly,weprovideacomprehensiveoverviewoftherecentworksoflargelanguage
model-empowered agent-basedmodelingandsimulationinmultiplescenarios,whichcanbe
dividedintofourdomains:cyber,physical,social,andhybrid,coveringsimulationofbothreal-
world and virtual environments, and how these works address the above challenges. Finally,
since this area is new and quickly evolving, we discuss the open problems and promising
futuredirections.Wesummarizetherepresentativepapersalongwiththeircoderepositories
in https://github.com/tsinghua-fib-lab/LLM-Agent-Based-Modeling-and-Simulation.
ISntroduction
imulation,asacomputationaltool,encompassestheemulationofreal-worldprocessesor
systems by employing mathematical formulas, algorithms, or computer-generated repre-
sentations to imitate their behaviors or characteristics. Agent-based modeling and simu-
lation focuses on modeling complex systems by simulating individual agents and their
interactions within an environment (Macal and North, 2005). It operates by assigning specific
behaviors,attributes,anddecision-makingcapabilitiestotheseagents,enablingtheexamination
of emergent phenomena resulting from agents’ interactions and environment dynamics. The
significance of simulation spans various domains, serving as a valuable tool for understanding,
analyzing, and predicting intricate phenomena that might be impractical or impossible to
observe directly in real life. It facilitates experimentation, hypothesis testing, and scenario
analysis, offering insights into systems’ behaviors under diverse conditions and aiding in
1BNRist,TsinghuaUniversity,Beijing,China.2DepartmentofElectronicEngineering,TsinghuaUniversity,Beijing,China. ✉ email:liyong07@tsinghua.edu.cn
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3 1
;,:)(0987654321

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
decision-making processes across fields like economics, biology, works. (1) Eligibility criteria, Information sources, and Search
sociology,andecology.Thecapacitytoacquireanduselanguage strategy. For the eligibility criteria, we delineate the scope of the
is a key aspect that distinguishes humans from other beings review,including(1)theusageofLLMagentsand(2)thestudied
(Hauseretal.,2002).Theadventoflargelanguagemodels(LLMs) problem of agent-based modeling and simulation. Information
represents a recent milestone in machine learning, showcasing sources for our paper are diverse, encompassing peer-reviewed
immense capabilities in natural language processing tasks and journals,conferenceproceedings,preprintarchives,andreputable
textualgeneration(Zhaoetal.,2023).Leveragingtheirformidable databases like IEEE Xplore, ACM Digital Library, Elsevier,
abilities, LLMs have shown promise in enhancing agent-based ClarivateWebofScience,arXivpreprint,SSRNpreprint,etc.The
simulations by enabling more nuanced and realistic representa- search strategy we used incorporates a combination of keyword
tions of agents’ decision-making processes, communication, and searches and controlled vocabulary terms related to LLMs,
adaptationwithinsimulatedenvironments.IntegratingLLMsinto ABMS, and their intersection, of which the keywords include
agent-based modeling and simulation holds the potential to “large language models,” “agent-based simulation,” “intelligent
enrich the fidelity and complexity of simulations, potentially agents,” “AI-driven simulation,” etc. We also use the citation
yieldingdeeperinsightsintosystem-levelbehaviorsandemergent trackingfunctionofGoogleScholartoidentifycited/citingpapers
phenomenaforthefollowingreasons:First,LLMagentscantake for those seminal works, ensuring a thorough and relevant lit-
actions even if there are no explicit instructions (Team, 2022; eraturereview.Webelievethisstructuredapproachwillfacilitate
Yoheinakajima, 2023). Second, LLM agents can respond like a a comprehensive understanding of the current landscape and
real human with adaptive planning (Schick et al., 2024; Wang emerging trends using LLM agents for ABMS. (2) Selection pro-
etal.,2024b;Xietal.,2023).Lastly,LLMagentscaninteractwith cess, Data collection process, and Data items. After deploying the
otheragents(orevenrealhumans)(Parketal.,2023).Thus,LLM search strategy on the various information sources, we select the
agentshaveachieved successina lotof areas(Boiko etal.,2023; proper papers presented in this review. The filtering process
Branetal.,2023;Gaoetal.,2023;Jinxinetal.,2023;Kovačetal., mainly focuses on two specific problems: (1) double-checking
2023; Li et al., 2023c, 2023e; Lin et al., 2023; Park et al., whether the paper belongs to agent-based modeling simulation
2023,2022).Fromthisperspective,itisclearthatLLMagentscan and uses LLM agents and (2) what kind of sub-category this
serve as a new paradigm for simulation with human-level paper belongs to. For the first problem, we found some papers
intelligence. thatuseanLLMagentasanassistantordecision-makinghelper,
As a result of the massive potential of LLM agents, there has which is close to agent-based modeling and simulation but,
recentlybeenaboominresearcheffortsinthisarea.However,as indeed, not the same. We filter out these papers (20+) and
yet,thereisnosurveythatsystematicallysummarizestherelevant reserve the remaining ones. For the second problem, we cate-
works, discusses the unresolved issues, and provides a glimpse gorize the papers based on two-dimension criteria: the domain
intoimportantresearchdirections.Inthissurvey,weanalyzewhy and the environment.
large language models are essential in the fundamental problem
of simulation, especially for agent-based simulation. After dis-
cussing how to design agents in this new paradigm, we carefully Background
and extensively discuss and introduce the existing works in var- In this section, we will first introduce the background of agent-
ious areas, most of which have been published recently. The based modeling and simulation, and large language models-
contribution of this survey can be summarized as follows. empowered agents.
● We takethefirststeptoreview theexisting worksoflarge
languagemodel-basedagentmodelingandsimulation.We
Agent-based simulation
systematicallyanalyzewhylargelanguagemodelscanserve
Basicconceptsofagent-basedsimulation.Agent-basedsimulation
as an advanced solution for agent-based modeling and
simulationcomparedwithexistingapproaches.Specifically, captures the intricate dynamics inherent in complex systems by
we first extensively explain the requirements of the agent c a o n n d c N en o t r r t a h ti , n 2 g 00 o 5 n ). in T d h iv es id e u a a g l e e n n ts tit a ie re s r h e e f t e e r r r o e g d en to eo a u s s a , g w e i n th ts s ( p M ec a i c fi a c l
capability for agent-based modeling and simulation from
characteristics and states, and adaptively behave according to
four aspects: autonomy, social ability, reactivity, and pro-
context and environment, making decisions and taking actions
activeness. Then, we analyze how large language models
(Elsenbroich et al., 2014). The environment, whether static or
address these challenges, including perception, reasoning evolving, introduces conditions, instigates competition, defines
and decision-making, adaptivity, and heterogeneity. boundaries,andoccasionallysuppliesresourcesinfluencingagent
● We divide the agent-based modeling and simulation into
behaviors (Cipi and Cico, 2011). The interaction includes inter-
fourdomains,physical,cyber,social,andhybrid,whichcan
actionswithboththeenvironmentandotheragents,andthegoal
coverthemainstreamsimulationscenariosandtasks,after is to mirror the behaviors in reality based on predefined or
which we present the relevant works, providing a detailed
adaptiverules(ElliottandKiel,2002;MacalandNorth,2005).To
discussion about how to design the simulation environ-
summarize, the basic components of agent-based simulation
ment and how to build simulation agents driven by large
include:
language models.
● In addition to the existing works in this new area, we
Agents: Agents are the fundamental entities in an agent-based
discuss four important research directions, including
simulation.Theyrepresentindividuals,entities,orelementsinthe
improving the simulation of scaling up, open simulation
system being modeled. Each agent has its own set of attributes,
platform, robustness, ethical risks, etc., which we believe
behaviors, and decision-making processes.
will inspire future research.
Environment: The environment is the space in which agents
operateandinteract.Itincludesthephysicalspace,aswellasany
Discussions on PRISMA. Following Preferred Reporting Items external factors, e.g., weather conditions, economic changes,
for Systematic Reviews and Meta-Analyses (PRISMA), we pro- political shifts, and natural disasters, that influence agent beha-
vide more details of how we collect and organize the related vior. Agents may be constrained or influenced by the
2 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
environment, and their interactions can have effects on the exploration of diverse scenarios and the study of emergent phe-
environment itself. nomenainacontrolledsimulationenvironment.Therefore,itoffers
researchersandpractitionersaversatiletoolforunderstandingand
Interaction: Agents interact with each other and their environ- predictingthebehaviorofcomplexsystemsacrossvariousdomains.
mentthroughpredefinedmechanisms.Interactionscanbedirect Based on the four categories of the target systems, current
(agent-to-agent) or indirect (agent-to-environment or environ- works of agent-based simulation can be divided into four
ment-to-agent). domains.
With the above components, agent-based modeling and
simulation provide a bottom-up perspective to study the Physicaldomain:Thiscategoryreferstothenaturalsysteminthe
macro-level phenomenons and dynamics from the individual physical environment (An, 2012). Typical applications include
interactions. ecology and biology (Pereira et al., 2004; Zhang and DeAngelis,
2020),suchasmodelingecologicalsystems(Heckbertetal.,2010;
Agentcapability.Toachieverealisticsimulationinawiderangeof Lippeetal.,2019),speciesinteractions(McLaneetal.(2011),and
applicationdomains,agentsshouldhavethefollowingcapabilities the impact of environmental changes (Beltran et al., 2017; Per-
in terms of perception, decision, and action (Wooldridge and toldi and Topping, 2004). Many simulation problems in urban
Jennings, 1995). environments also belong to the physical domain (An, 2012),
such as transportation, human mobility, etc. Specifically, for
Autonomy: Agents should be able to operate without the direct urban planning (Gaube and Remesch, 2013), agent-based mod-
intervention of humans or others, which is important in real- eling and simulation can aid in simulating urban growth
world applications such as microscopic traffic flow simulation (Arsanjani et al., 2013; Barros, 2004), traffic patterns (de Souza
(Lopez et al., 2018) and pedestrian movement simulation (Batty, etal.,2019;Mastioetal.,2018),andtheimpactofurbanpolicies
2001). (Ma et al.,2013;Maggi and Vallino,2016;Widener et al.,2013).
Another application is engineering and manufacturing (Barbosa
Socialability:Agentsshouldbeabletointeractwithotheragents and Leitão, 2011; Rolón and Martínez, 2012), in which agent-
(and possibly humans) to complete the assigned goals. When based molding and simulation can be applied to model supply
studying social phenomena, group behavior, or social structures, chain dynamics (Schieritz and Grobler, 2003), production pro-
the sociability of agents is key. This includes simulating the for- cesses (Parv et al., 2019), and the interactions of entities within
mation of social networks, the dynamics of opinions, the spread manufacturing systems.
of culture, and more. The social interactions between agents can
be either cooperative or competitive, which are critical when Social domain: The social domain mainly covers the social
simulating economic activities such as market behavior, con- behavior simulation, which can be further divided into (1) social
sumer decisions, etc. interaction that focuses on social networks, community interac-
tions, or organizational behavior (Macy and Willer, 2002; Wall,
Reactivity: Agents should be able to perceive their environment 2016)and(2)economicsystemthatsimulateseconomicsystems,
and respond quickly to changes in the environment. This cap- market dynamics, or financial interactions (Samanidou et al.,
ability is especially important in systems that need to simulate 2007). Specifically, for social sciences (Conte and Paolucci, 2014;
real-time responses, such as traffic control systems and auto- Gilbert,2007b;GilbertandTerna,2000;Ternaetal.,1998),agent-
matedproductionlines,andindisasterresponsescenarioswhere based modeling and simulation are widely used to model social
agents need to be able to respond to environmental changes phenomena such as crowd behavior (Kountouriotis et al., 2014;
immediatelytoeffectivelyconductearlywarningandevacuation. Luoetal.,2008),opiniondynamics(Banischetal.,2012;Lietal.,
More importantly, agents should be able to learn from previous 2020), and social network interactions (El-Sayed et al., 2012;
experienceandadaptivelyimprovetheirresponses,similartothe Gilbert,2004a;Madeyetal.,2003).Theagent-basedmodelingcan
idea of reinforcement learning (Lin, 1992). simulate the emergence of societal patterns and trends (Helbing,
2012).Asfortheresearchofeconomics(HamillandGilbert,2015;
Pro-activeness: Agents should be able to exhibit goal-directed LeombruniandRichiardi,2005; VanDinther,2008),agent-based
behavior by taking the initiative instead of just responding to modelsareemployedtostudyeconomicsystems(Deguchi,2011),
their environment. For example, agents need to proactively pro- market dynamics (Rouchier, 2017; Wang et al., 2018), and the
vide help, advice, and information in applications such as intel- behaviorofindividualeconomicagents(MuellerandPyka,2016).
ligent assistants and actively explore their environment, plan
paths,andperformtasksinfieldssuchasautonomousrobotsand
Cyberdomain:Besidesthephysicalworldandhumansociety,our
self-driving cars. daily life has been further extended into cyberspace. Therefore,
It is worth mentioning that, like humans, agents cannot make agent-based simulation has also been applied in wide areas like
perfectly rational choices due to limitations of knowledge and web-based behaviors (Guyot and Honiden, 2006) and cyber-
computational capacity (Simon, 1997). Instead, they can make security applications (Alluhaybi et al., 2019).
suboptimalyetacceptabledecisionsbasedonimperfectinformation.
This capability is particularly critical in achieving human-like Hybriddomain:Thiscategoryincludeshybridsystemscombining
simulations in the economic market (Arthur, 1991) and manage- components covering the physical world, social life, and cyber-
mentorganizations(Puranametal.,2015).Forexample,considering space. For example, an urban environment is a socio-physical
agents’ bounded rationality when simulating consumer behavior, environment that integrates social behavior with physical infra-
market transactions, and business decisions can more accurately structure. Moreover, it is also multi-layered after taking online
reflect real economic activities. In addition, in simulating decision- social networks into account. That is, these applications involve
making, teamwork, and leadership within organizations, bounded more than one domain of physical, social, or cyber domains.
rationalityhelpsrevealbehavioraldynamics inrealworksettings. Therefore,agent-basedsimulationswithinanurbanenvironment,
suchasurbanplanning(Chen,2012)andepidemiccontrol(Silva
Applications of agent-based modeling and simulation. The flex- etal.,2020),arefarmorecomplexandchallengingthanthosein
ibility of agent-based modeling and simulation allows for the unitary environments. Moreover, for healthcare (Barnes et al.,
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3 3

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
2013;Cabreraetal.,2011),agent-basedmodelingandsimulation Simple agent architecture is not enough to cope with
canbeusedtomodelthespreadofinfectiousdiseases(Perezand complex tasks: Although “reactive architectures” are able to
Dragicevic,2009),healthcaresystems(Silvermanetal.,2015),and adapttodifferentenvironmentalconditions,theymaybelimited
the effectiveness of interventions (Beheshti et al., 2017), which in handling complex tasks or situations that require long-term
help in understanding and planning for public health scenarios. planning. To achieve human-like simulation in real-world com-
plex problems, current agent architecture requires redesigns that
Methodologies of agent-based modeling and simulation. The solvechallengesinprocessingspeed,resourceefficiency,andtask
development of modeling technologies utilized in agent-based complexity. Specifically, agents should be capable of complex
simulation has also gone through the early stage of knowledge- planning and reasoning processes, like using internal models to
driven approaches and the recent stage of data-driven approa- predicttheconsequencesofdifferentcoursesofactionandchoose
ches. Specifically, the former includes various approaches based the best one, and able to develop and execute complex strategies
onpredefinedrulesorsymbolicequations,andthelatterincludes to achieve long-term goals.
stochastic models and machine learning models.
It is difficult to develop a general agent that can support
● Predefined rules: This approach involves defining explicit
simulationsacrossenvironments:Differentenvironmentsvaryin
rulesthatgovernagentbehaviors.Theserulesaretypically
dimensions like complexity, dynamics, and uncertainty. Due to
basedonlogicalorconditionalstatementsthatdictatehow thisdiversity,aspecificagentthatiseffectiveinoneenvironment
agentsreacttospecificsituationsorinputs.Themostwell-
(like a financial market simulation) might be completely inef-
known example is the cellular automata (Wolfram, 1984)
fective in another (like a social campaign simulation). In real-
thatleveragessimple,localrulestosimulatecomplexglobal
world applications where the target environment is often hybrid
phenomenathatexistnotonlyinthenaturalworldbutalso with significant dynamics and uncertainty, developing specific
in complex urban systems. agents case by case is highly inefficient and costly.
● Symbolic equations: Compared with predefined rules,
symbolic equations are used to represent relationships or
Existing methods cannot support integrative simulation in real-
behaviors in a more formal, mathematical manner. These
worldproblems:Aversatileagent-basedsimulationmodelshould
can include algebraic equations, differential equations, or
beabletodescribehowsystemsoperateunderknownconditions,
other mathematical formulations. A typical example is the
explain why certain patterns emerge, predict future states based
social force model widely used in pedestrian movement
on existing observations, and explore the outcomes of hypothe-
simulation (Helbing and Molnar, 1995). It assumes that
tical scenarios. However, existing methods cannot support the
pedestrian movements are driven by a Newton-like law
above tasks simultaneously: rule-based methods are useful in
decidedbyanattractiveforcedrivenbythedestinationand
descriptive problems, while symbolic or stochastic methods can
arepulsiveforcefromneighboringpedestriansorobstacles.
provideexplanationsregardingunderlyingmechanismsthatdrive
● Stochasticmodeling:Thisapproachintroducesrandomness thesystem.Comparatively,machinelearningmodelsarebetterat
andprobabilityintoagentdecision-making,whichisuseful
predictive problems by learning hidden patterns from data but
for capturing the uncertainty and variability inherent in
with less interpretability. Therefore, there remain challenges in
many real-world systems (Feng et al., 2012). For example,
developing methods that simultaneously capture the accuracy of
to account for the impact of randomness originating from
behavioralmodeling,interpretabilityofmechanisms,adaptability,
human decision-making, we can leverage discrete choice
and reliability under environmental changes.
models for simulating pedestrian walking behaviors
(Antonini et al., 2006).
● Machine learning models: Machine learning models allow
Large language models and LLM-empowered agents. Large
agentstolearnfromdataorthroughinteractionwiththeir
language models (LLMs), such as ChatGPT (OpenAI, 2022),
environment.Supervisedlearningapproachesaregenerally
Gemini(DeepMind,2023),LLaMA(Touvronetal.,2023),Alpaca
used for estimating parameters of agent-based models,
(Taori et al., 2023), and GLM (Zeng et al., 2023), are the latest
whilereinforcementlearningapproachesarewidelyusedin
paradigm oflanguagemodels,whichevolvefromearlystatistical
the simulation period, enhancing the adaptation capability
language models (Bellegarda, 2004) to neural language models
ofagentswithindynamicenvironments(Kavaketal.,2018;
(Melis et al., 2017), then to pre-trained language models (Brown
Kim et al., 2021; Platas-López et al., 2023). et al., 2020), and finally to large language models (Zhao et al.,
2023c). With billions of parameters and extensive pre-training
Limitations. Early works on agent-based simulation are keen to corpus,LLMshaveshownastonishingabilitiesnotonlyinnatural
design “deliberative architectures” that relyon explicit, often com- language processing tasks (Li et al., 2023a; Zhang et al., 2024c)
plex, internal models to make decisions, emphasizing the impor- suchastextgeneration,summarization,translation,etc.,butalso
tance of planning, reasoning, and decision-making processes in complex reasoning and planning tasks, such as solving math-
(WooldridgeandJennings,1995).However,optimizingtheinternal ematicalproblems(Aroraetal.,2023),etc.Pre-trainingonlarge-
world model and planning-reasoning module based on symbolical scale corpora lays the foundation ability for zero-shot general-
AIapproachesaregenerallyintractableinpractice.Thisleadstothe ization. Moreover, pre-trained models can be further fine-tuned
prevalence of “reactive architectures” in agent-based simulations, for specific tasks, adapting to particular application scenarios
which instead rely primarily on direct sense-action loops rather (Jiang et al., 2023). In addition, the advances of large language
than complex internal models of the world or deep reasoning models in the past year, such as ChatGPT and GPT-4 have
processes to make decisions. The subsequent development of AI, achieved human-like reasoning ability, a milestone that is now
especiallydeeplearningtechnology,doesnotfundamentallychange being considered to be the seed of artificial general intelligence
this paradigm of agent-based simulation due to the poor inter- (AGI). Specifically, the capacity to acquire and use language is a
pretability and generalization capability. However, facing the need key aspect of how we humans distinguish ourselves from other
for realistic simulation of real-world processes or systems, current beings(Tomasello,2010).Languageisoneofthemostimportant
approaches still have several limitations, as described below. mechanisms we have to interact with the environment, and
4 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
Fig.1Illustrationofhowlargelanguagemodelagentsmeettherequirementsofagent-basedmodelingandsimulation.
language provides the basis for high-level abilities (Hauser et al., detail in the section “Critical abilities of LLM for agent-based
2002). modeling and simulation”. Then, in the section “hallenges and
Thus, it is promising to construct large language model- approaches of LLM agent-based modeling and simulation”, we
empowered agents (Wang et al., 2024b; Xi et al., 2023) due to will elaborate on the recent advances of large language model
their human-like intelligence in perceiving the environment and agent-based modeling and simulation to further answer the
making decisions. In the following, we have a short summary of question of how large language model agents meet the
the motivations to apply large language models to agent-based requirements(whatkindofchallengesandhowtoaddressthem).
modeling and simulation.
First, the LLM agent is able to adaptively react and perform
Critical abilities of LLM for agent-based modeling and
tasks based on the environment without predefined explicit
simulation
instructions (Team, 2022; Yoheinakajima, 2023). In addition,
Asmentionedabove,agent-basedmodelingandsimulationserve
duringthesimulationprocess,theLLMagentcanevenformnew
as a basic approach for simulation in many areas (Elsenbroich
ideas,solutions,goals,etc.(FranceschelliandMusolesi,2023).For
et al., 2014; Macal and North, 2005), but it still suffers from
example, AutoGPT Team (2022) can automatically schedule
several key challenges. Large language model-empowered agents
plans when given a set of available tools and the final task goal,
not only meet the requirements for agent-based simulation but
exemplifying the significant potential of LLMs in constructing
also address the limitations relying on their strong abilities in
autonomousagents.Meanwhile,BabyAGI(Yoheinakajima,2023)
perception, reasoning, decision-making, and self-evolution, illu-
created an LLM-driven script running an infinite loop, which
strated in Figs. 1, 2.
continuously maintains a task list, in which each task is
completed the task by ChatGPT API (OpenAI, 2022) based on
the task context. Second, the LLM agent has enough intelligence Perception. The core of agent-based modeling and simulation is
that it can respond like a human and even actively take actions tomodelhowanindividualagentinteractswithanenvironment
with self-oriented planning and scheduling (Wang et al., 2024b; (Macal and North, 2005), which requires the agent to accurately
Xi et al., 2023). Actually, the input of the environment is not sensevarioustypesofinformationfromsaidenvironment.Asfor
limited to text; rather, recent multi-modal fusion models can be the large language model-empowered agents, the ability of lan-
fedothertypesofinformation,suchasimageoraudio(Zhuetal., guage enables agents to comprehend and respond to diverse
2024). The action space of the LLM agent is neither limited to environments directly or indirectly. On the one hand, the basic
text,forwhichthetool-usageabilityallowstheagenttotakemore ability to understand and generate text enables agents to engage
actions(Schicketal.,2024).Third,theLLMagenthastheability in complex dialogs, negotiate, and exchange information, and
to interact and communicate with humans or other AI agents support direct interaction. On the other hand, the interface
(Park et al., 2023). In the simulation, especially agent-based between the agent and environment can be operated via texts
simulation,theagent’scommunicationability elevatesindividual (Team,2024),whichleadstoindirectinteraction.Ofcourse,such
simulationtothecommunitylevel(GilbertandTroitzsch,2005). abilityalsosupportsthecommunicationbetweendifferentagents,
An LLM-driven agent can generate text, which can be received besides the agent-environment perspective.
andunderstoodbyanotheragent,inturnprovidingthebasisfor It is worth mentioning that the ability to interact with the
interpretable communication among agents or between humans environmentandotheragentsisnotadequatetoachievehuman-
and agents (Park et al., 2023). Fourth, the simulation at the
likesimulations.Tobemorespecific,itisalsorequiredthatlarge
community level requires heterogeneity of agents, and the LLM language model-based agents “put themselves in real humans’
agentscan meet these requirementsfor playingdifferent rolesin shoes”, thereby allowingthe agent to imagine thatit isindeed in
society (Qian et al., 2024). An artificial society constructed by the environment. That is, LLM agents should be able to
LLM agents can further reveal the emergence of swarm comprehend, perceive, and respond to diverse needs, emotions,
intelligence with collective agent behaviors (Gao et al., 2023;
andattitudeswithindifferentcontexts,fromthe“first-viewsight”
Parketal.,2023),similartowisdom-of-crowdsinhumansociety (Shanahan et al., 2023). This capability enables models to better
(Surowiecki, 2005). understand the information from the environment or other
Asmentionedabove,thesimulationsystemhaswidelyutilized agents and generate more real responses.
the paradigm of agent-based modeling, which requires agents
with high-level abilities. This well motivates the use of large Reasoning and decision making. One critical challenge in tra-
language model-empowered agents in simulation scenarios. In ditional agent-based simulation is that rule-based or even neural
the following, we will discuss the critical abilities of a large network-based agents is not intelligent enough (Cipi and Cico,
language model for agent-based modeling and simulation in 2011). That is, the agent is not able to make correct or optimal
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3 5

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
Fig.2Illustrationofhowlargelanguagemodel-empoweredagentsworkbasedonfouraspectsofcriticalabilities(figureeditedfromS3Gaoetal.,2023):
perception,heterogeneityandpersonalizing,reasoninganddecision-making,adaptivelearning,andevolution.
decisions,suchaschoosingacrowdedroadinthetransportation Heterogeneity andpersonalizing.Asthesayinggoes,oneman’s
simulationorsendinganincorrectmessageinthesocialnetwork meatisanotherman’spoison.Heterogeneityofagentsiscriticalfor
simulation. This can be explained by the fact that traditional agent-based simulation, with the complex society (Brown and
neural network-based artificial intelligence is still not as intelli- Robinson,2006)oreconomicsystem(Bohlmannetal.,2010)with
gentasarealhuman(Hernández-Oralloetal.,2016;Hoshenand heterogeneous individuals. Specifically, in agent-based modeling
Werman,2017;Liuetal.,2019;MańdziukandŻychowski,2019). andsimulations,theheterogeneityofagentsinvolvesrepresenting
In contrast, large language model-empowered agents exhibit diverse characteristics, behaviors, and decision-making processes
heightened reasoning capabilities, enabling them to make more among individuals. Agent-based simulation stands out for its
informed decisions and choose suitable actions within the capacitytoaccommodatevariedrulesorparameterscomparedto
simulation. Despite making suitable decisions, another critical traditional simulation methods, discussed as follows.
advantageoflargelanguagemodel-empoweredagentstosupport The first one is the extremely high complexity of parameter
better agent-based modeling and simulation is autonomy (Fu settings of the existing methods (Elliott and Kiel, 2002; Macal and
et al., 2024). With only limited guidance, regulations, and goals, North,2005).Inthesemodels,thevastarrayofvariablesinfluencing
agents equipped with large language models can autonomously an agent’s behavior-from personal traits to environmental factors-
take actions, make plans for the given goal, or even achieve new makes selecting and calibrating these parameters daunting. This
goals without the need for explicit programming or predefined complexity often leads to oversimplification, compromising the
rules(Parketal.,2023).Thatis,autonomyenablesLLMagentsto simulation’s accuracy in portraying true heterogeneity (Macal and
dynamically adjust their actions and strategies based on real North,2005).Moreover,acquiringaccurateandcomprehensivedata
circumstances, contributing to the realism of the simulation. to inform parameter selection is another challenge. That is, real-
world data capturing diverse individual behaviors across various
contexts might be limited or challenging to collect. Furthermore,
Adaptive learning and evolution. Foragent-basedmodelingand validatingthechosenparametersagainstreal-worldobservationsto
simulation, the system always has uncertainty and controllability ensuretheirreliabilityaddsanotherlayerofcomplexity.Second,the
(MacalandNorth,2005).Inotherwords,theenvironmentandthe rule or the model cannot cover all dimensions of heterogeneity, as
agent’sstatemaybecompletelydifferentcomparedwiththeinitial real-world individuals are very complex (Macal and North, 2005).
stageofthesimulation.AstheoldstoryofRipVanWinkletells,a Usingrulestodriveagentbehaviorsonlycapturescertainaspectsof
man falls asleep in the mountains and awakens to find that the heterogeneity but could lack the depth to encapsulate the full
worldaroundhimhasdrasticallychangedduringhisslumber.That spectrum of diverse behaviors, preferences, and decision-making
is,theenvironmentiscontinuouslychanginginalong-termsocial processes. Furthermore, as the model capacity, trying to cover all
network simulation (Gao et al., 2023); the agent should be able to dimensions of heterogeneity within a single model is too idealistic.
adapt to the new environment, formulating decision policies that Thus, balancing model simplicity and accurate modeling agents
may deviate significantly from their original strategies. Obviously, becomes a critical challenge in agent-based modeling and simula-
adaptive learning and evolution are challenging for traditional tion, resulting in oversimplification or neglect of certain aspects of
approaches, but luckily, this can be addressed by large language agentheterogeneity.
model-basedagents(Luetal.,2023).Specifically,withtheabilityto Different fromthe traditional methods, theLLM-based agents
continually learn from new data and adapt to changing contexts, support (1) capturing complex internal characteristics with
LLM agents can evolve behaviors and decision-making strategies internal human-like cognitive complexity and (2) specialized
overtime.Agentscanassimilatenewinformation,analyzeemerging and customized characteristics with prompting, in-context
patternsindata,andmodifytheirresponsesoractionsaccordingly learning, or fine-tuning.
based on in-context learning (Dong et al., 2022), mirroring the
dynamicnatureofreal-worldentities.Thisadaptabilitycontributes Anexampleofabetterunderstanding.Forabetterunderstanding
to the simulation’s realism by simulating the learning curve and oftheaboveabilitiesoflargelanguagemodelagents,weselectthe
evolution ofagents’ behaviors in response tovarying stimuli. paradigmofarepresentativepaper,S3inthesocialdomain,asa
6 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
templateandaddmoresupplementarydescriptionstoconstructa ● Inputandoutputoftheenvironment.Mostexistingworks
representative diagram. We have done some editing on the ori- usetextsasthemajorinterface,naturallyduetotheability
ginal figure, and the improved figure illustrates a representative tounderstandandgeneratetextsoflargelanguagemodels.
agent workflow that reveals four critical abilities: perception, Even if the environment is a sandbox with rich models,
heterogeneityandpersonalizing,reasoninganddecision-making, such as Smallville sandbox world (Park et al., 2023) in
adaptivelearning,andevolution.Theoverallstructureisalsovery which the environment is still represented with texts,
similar to Generative Agent (Park et al., 2023). relying on which the agent can perceive the context. In
addition, the basic rules or domain-specific knowledge,
suchasthegamerule,isalsosummarizedwithtexts,which
Challenges and approaches of LLM agent-based modeling are received by the large language model agents with
and simulation prompt engineering. Due to the limitation of texts, the
The core of agent-based modeling and simulation is how the existing works construct various tools to interact with
agent reacts to the environment and how agents interact with complexenvironmentsordata,butrecallingorusingthese
each other, in which agents should behave close to real-world tools is still based on texts. For example, in Zhu et al.
individuals withhumanknowledgeand rules, as realas possible. (2023c), the large language model’s action is a phrase,
Therefore, when constructing large language model-empowered which can be a parameter of the tool function to interact
agents for simulation, there are four major challenges, including with the simulation environment.
perceivingtheenvironment,aligningwithhumanknowledgeand ● Communication between agents. First, the direct commu-
rules, choosing suitable actions, and evaluating the simulation. nication between agents is also focusing on the texts. For
We will discuss the solutions from a high-level perspective, and example, in agent-based simulation for social science, the
how the existing works address them will be elaborated on in textual information exchange represents the communica-
detail in the next section. tionbetweenhumansintherealworld.Second,theagents
canindirectlyinteractwithothersthroughpredefinedrules;
for example, in economic simulation, the agents can work
Environment construction and interface. For agent-based in the same factory, and the rule in the economic system
simulation with large language models, the first step is to con- makes them interact indirectly.
struct the environment, virtual or real, and then design how the
In summary, the environment construction, along with
agentinteractswiththeenvironmentandotheragents.Thus,we
defining how agents interact with the environment, is the first
need to propose proper methods for an environment that LLM
step of deploying large language model agents for agent-based
can perceive and interact with.
modelingandsimulation.Thankstothemulti-modalabilityand
Environment: define the world and rules. The external environ- usage of tools, the interface is not limited to pure texts,
supporting more diverse and more realistic environments, with
ment in agent-based simulation varies for different domains. In
more complicated cross-agent interactions.
general, the environment built by existing works can be divided
into two categories: virtual and real.
● The virtual environment includes simulation applications Human alignment and personalization. Although LLMs have
withpredefinedrulesinprototype-levelsimulation,suchas
already demonstrated remarkable human-like characteristics in
a virtual social system, game, etc. For example, Qian et al. many aspects, agents based on LLMs still lack the necessary
(2024) designed a virtual software company with multiple domain knowledge in specific areas, leading to irrational deci-
agents for different roles, such as CEO, managers, sions. Therefore, aligning LLM agents with human knowledge
programmers, etc. Wang et al. (2023b) constructed an and values, especially those of domain experts, is an essential
environment of a virtual recommender system in which challengetoachievemorerealisticdomainsimulations.However,
agentscanbrowsetherecommendedcontentsandprovide the heterogeneity of agents, as a fundamental characteristic of
feedback. The sandbox environment is one kind of virtual ABM, is both an advantage and a challenge for traditional
environmentwheretheprinciplesandideasconceptualized models. While, LLMs possess a powerful capability to simulate
inavirtualenvironmentcanbetestedandadaptedtoreal- heterogeneous agents, ensuring controllable heterogeneity.
world applications. For example, Generative Agent Park However, enabling LLMs to play different roles to meet perso-
et al. (2023) builds a Smallville sandbox world in which nalized simulation requirements is a significant challenge. Next,
large language model-empowered agents plan their days, wewillexplainthemethodsandtechnologiestoaddressthesetwo
share news, form relationships, and coordinate group challenges from two perspectives: prompt engineering and tun-
activities. ing, and introduce the existing related work in these areas.
● Therealenvironmentincludesourrealworld.Forexample,
Lietal.(2024b)deploylargelanguagemodel-basedagents Human alignment
to simulate economic activities, in which agents can Prompt engineering: When simulating specific agents, we can
represent both consumers and workers. WebAgent Gur provide task instructions, background knowledge, generation
etal.(2024)simulatearealhumanbrowsingandaccessing patterns, and task examples specific to certain domains or sce-
online content of real websites. UGI (Xu et al., 2023a) narios, thereby aligning LLMs’ output with human knowledge
proposed to build agents for the real-world urban and values when deployed. For example, providing detailed
environment, and the agents are expected to generate descriptionsofgamerulesandexamplesfortheagentallowsitto
various human behaviors in the city, including navigation, considervariousfactorsitcaresabout,likehumanswhenmaking
social, economic, etc. decisions, such as self-interests, fairness, etc. (Akata et al.,2023).
Inaddition,constructingmodulessuchasreflectionandmemory
canimprove agents’planningand reasoningcapabilities,thereby
Interface. The interface actually has two aspects, how the agent
giving them stronger gaming capabilities and creating a possible
interacts with the environment and how agents communicate
path towards human-intelligent gaming (Guo et al., 2023).
with each other.
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3 7

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
Tuning: Tuning requires constructing a training dataset for spe- How to simulate actions. This section aims to delve into how
cific domains, scenarios, or hiring domain experts. Based on the LLM agents are designed to exhibit complex behaviors that are
dataset or expert feedback, fine-tuning the LLM can also reflective of real-world cognitive processes. This involves under-
empower the agents with more domain-specific knowledge, standing and implementing the mechanisms by which these
producing outputs more in line with human knowledge and artificialagentscanretainand utilize pastexperiences (memory)
values. For example, Singhal et al. (2023) propose to achieve (Gao et al., 2023; Park et al., 2023; Zhu et al., 2023c), introspect
knowledge alignment in clinical medicine. The proposed Multi- and adjust their behavior based on their outcomes (reflection)
MedQAbenchmarkcombinessixexistingmedicalquestion-and- (Park et al., 2023; Shinn et al., 2023), and execute a sequence of
answer datasets covering professional medicine, research, and interconnected tasks that mimic human workflows (planning)
consumer inquiries. Additionally, Med-PaLM (Singhal et al., (Wei et al., 2022).
2023), an LLM for the medical field, is trained based on a
foundational model PaLM (Chowdhery et al., 2023). In terms of Planning. Here, we introduce the methodology by which LLM
implementation, the authors incorporate examples of medical agents approach complex tasks through decomposition. Initially,
question-and-answer and modify model prompts through the an LLM assesses the task to understand its main objectives and
guidanceofprofessionalclinicians(involvingfiveclinicaldoctors) context. It then breaks down the task into smaller, manageable
forfine-tuning.Thisguidesthemodeltogeneratetextconsistent subtasks, each contributing towards the overall goal. This seg-
with clinical requirements. With this domain-specific LLM, we mentation leverages the LLM’s training corpus to recognize pat-
can simulate agents (e.g., medical assistants) in real-world med- terns and apply relevant knowledge efficiently (Park et al., 2023;
ical environments. In addition to collecting large-scale datasets Sun et al., 2024); Wang et al., 2024a; Zhu et al., 2023c).
with domain knowledge, other research (Dubois et al., 2024) Each subtask is executed sequentially, with the LLM agent
directly uses LLMs to generate “human feedback”, specifically applying its knowledge base to ensure logical progression and
pair-wise feedback for instructions, for LLM fine-tuning. Results coherence. This approach not only simplifies complex tasks but
show that the generated feedback enables LLM to achieve high also enhances the LLM’s accuracy and adaptability. By tackling
humanalignment45×cheaperthanhiringcrowdworkerstogive tasks incrementally, the LLM agent can adapt its strategies and
feedback in experiments. ensure that each step is contextually relevant and logically
structured. For example, GITM (Zhu et al., 2023c) showcase an
Personalization LLM agent that decomposes the overarching goal of “Mining
Prompt engineering: The basic idea is to adapt to personalized Diamond”intoaseriesofsub-goals,constructingasub-goaltree.
needs by providing LLM agents with individual preferences, This model uses its text-based knowledge and memory to
expected output patterns, background knowledge, etc., thereby navigate in a virtual environment, making strategic decisions at
making the output closer to the specific needs or preferences of eachtreenodetoachievethemainobjective.VoyagerWangetal.
individuals when deployed. For example, in the well-known (2024a)employanautomaticcurriculumtoaidtheLLMagentin
LLM-basedsocialactivitysimulation,AITown(Parketal.,2023), understanding the sequence of actions required to reach a goal.
personalized interaction behaviors of agents in different scenar- Byreasoningwiththeavailableresources,theLLMagentcanplan
ios, at different times, and with different other agents can be an efficient course of action, like upgrading tools for better
achieved by introducing professions, behavioral preferences, and efficacy and demonstrating adaptive problem-solving skills.
interpersonal relationships in the prompts. In economic simula- AdaPlanner (Sun et al., 2024) introduces an LLM that refines
tion, specifically the simulation of canonical games, the agent’s itsactionplanbasedonfeedback,whichhasanin-planrefinerfor
preferences can be specified in the prompt, such as cooperative, aligning actions with predictions and an out-of-plan refiner to
selfish,altruistic,etc.,sothattheagentwillhavedifferentlevelsof adjustwhenpredictionsdonotmatchoutcomes,showcasingthe
cooperative tendencies during the game playing (Phelps and model’s ability to adapt and revise its plan dynamically in
Russell, 2023). response to changing scenarios.
Insummary,advancementsrepresentsignificantstridesintask
Tuning: Tuning for personalization requires selectively con- decomposition and strategic planning. They highlight the
structing datasets or fine-tuning multiple models based on feed- capability of LLMs to not only break down complex tasks into
backfromdifferentusers,witheachmodelcorrespondingtoone manageable sub-goals but also to dynamically adapt their
or a type of personalized needs. This can also be achieved by strategies and refine plans based on ongoing feedback and
using specific combinations to provide relevant, personalized changing scenarios, thereby enhancing decision-making and
requirements. Some research attempts to efficiently align LLMs problem-solving efficiency in various contexts.
with various preferences tailored to different users’ distinct pre-
ferences (Jang et al., 2023). Specifically, user preferences are Memory. Human behavior is largely influenced by past experi-
decomposed into standards across multiple aspects, with perso- ences and insights, which are stored in memory. If LLM agents
nalized optimization based on RLHF targeted towards different aim to mimic this aspect of human behavior, they also need to
aspects. In practical applications, the strategy of LLM response referencepastexperiencesandinsightswhenacting.However,the
generation is based on linearly weighting strategies according to volume of this information is often immense, frequently
user preferences. When simulating agents with individual pre- exceeding the context window length of LLMs. Therefore, it’s
ferences (e.g., users in recommender systems), this approach necessary to design a memory system that functions as an
achieves a more accurate match for different preferences and is external database for LLM agents. This system should have
also easily generalizable to scenarios with a broader range of appropriate mechanismsfor organizing,updating,and retrieving
preferences. information, enabling LLM agents to reference these memories
Insummary,humanalignmentandpersonalizationensurethe for future actions.
large language model-empowered agents cannot only simulate Generative Agents Park et al. (2023) showcase an LLM agent
real human behaviors but also play a given role, making it that develops a generative memory system, integrating sensory
possibletosimulatetheheterogeneityofreal-worldsystems.The perceptionswithacontinuousstreamofexperiences.Thissystem
typical techniques in this component mainly involve prompt notonlystoresinformationbutactivelyengagesinplanningand
engineering and tuning. reflection, adapting its behavior based on past outcomes. Chen
8 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
et al. (2023c) illustrate an LLM agent’s strategic prowess in In summary, in the realm of simulating actions, LLMs stand
auction scenarios, where it adapts its bidding strategy by outfortheirabilitytointegrateplanning,memory,andreflection.
synthesizing new information with existing memories to max- They employ a cyclical approach where planning dictates the
imize profits or meet specific objectives. course of action, memory provides a knowledge base derived
GITM(Zhuetal.,2023c)andVoyager(Wangetal.,2024a)are from past experiences, and reflection adjusts strategies based on
seen curating a skill library, updating its capabilities through feedback. This dynamic interplay allows LLMs to not only
practiceandfeedback.Thisapproachreflectsanunderstandingof executeactionswithinvariedsimulationsbutalsotocontinuously
task requirements and environmental challenges, where the learn and adapt. By simulating these cognitive processes, LLMs
LLM’s memory serves as a dynamic repository of actions and demonstrate an advanced capacity for autonomous decision-
strategies. The distinction between explicit and implicit memory making,whichisincreasinglyindistinguishablefromhuman-like
comes into play in simulations that require the LLM to navigate behavior in complexity and adaptability.
complex tasks, such as resource management and goal-oriented In summary, how the large language model agents generate
action planning in open-world environments. Here, the LLM’s actions are inspired by the mechanism of humans, including
memory functions extend beyond simple recall, enabling the planning, memory, and reflection, with similar and simplified
agent to perform with a sense of history and progression. designs. These designs are independent of the specific large
Lastly, the role of memory in social interactions is explored language models but also significantly influence the simulation
through simulations in S3 (Gao et al., 2023) that mimic the performance.
intricaciesofhumanbehavior.LLMstrackandadapttochanging
social cues and demographic shifts, employing memory not just
as a record of past interactions but as a tool for future social Evaluation of LLM agents
navigation and decision-making. Li et al. (2024b) demonstrate Realness validation with real human data. The basic evaluation
howamemorymoduleinLLMscanbecrucialforunderstanding protocol for LLM-based agents is to compare the simulation’s
and adapting to dynamic social environments. They show that output with existing real-world data. The evaluation can be
LLMs, equipped with a memory of past social interactions and conductedattwolevels:micro-levelandmacro-level.Specifically,
trends, can more effectively predict and respond to future micro-level evaluation refers to evaluating the ability to simulate
economic changes, enhancing their decision-making in complex the individual agent’s behavior or actions as realistically as pos-
social landscapes. sible. For example, in S3 (Gao et al., 2023), the authors test the
Collectively, these studies contribute to our understanding of performance of the LLM agents in predicting the individual
LLMs as agents capable of sophisticated memory management, agent’s next state, given the current state and the environment
crucial for their function in dynamic and unpredictable context. On the other hand, since the agent-based simulation
environments. They highlight the remarkable potential of LLMs always pays more attention to the emerged phenomenon of the
to transcend traditional data storage, moving towards a more population,macro-levelevaluationisofgreatsignificance,which
integrated and intelligent use of memory in artificial cognition. aims to evaluate whether the simulated process has the same
pattern, regularity, etc., as the real-world data. In S3 (Gao et al.,
Reflection. The section explores how LLM agents incorporate 2023),oneofthemaingoalsistoaccuratelypredictthedynamics
feedback mechanisms to enhance their memory systems, ofinformation,opinion,andattitudebasedonthecollectedreal-
improving decision-making and learning processes. This reflec- world social media data. In economics simulation by Li et al.
tionencompassesbothshort-termandlong-termmemoryfacets, (2024b),thesimulated economicsystem isevaluated on whether
enabling LLMs to adapt their behaviors and strategies those most representative macroeconomic regularities, such as
dynamically. Okun’s law (Plosser and Schwert, 1979), etc. Furthermore, the
An exemplary implementation of this reflective cycle is generated behaviors’ rationality can also be evaluated, such as
Reflexion (Shinn et al., 2023). In this work, the LLM leverages logical consistency, adherence to established common sense, or
anintegratedevaluatortointernallyassesstheefficacyofactions following the given rule in the simulation environment. In
based on the rewards received. It also utilizes a prompt-based addition,wecanassessthesimulatedagent’sperformanceagainst
approach to self-reflection, allowing the agent to internally established benchmarks or standardized tasks relevant to its
simulateandcritiqueitsperformance.Thisdualfeedbacksystem domain. For example, whether the agent can reach human-level
enablestheagenttorefineitsmemoryandbehaviorinanuanced evaluation scores in a web-browsing or game environment
andcontinuouslearningprocess.Themodelcapturesshort-term (Chang et al., 2024).
memory as trajectories of actions and observations, while long-
term memory encompasses accumulated experiences. The inter- Provide explanations for simulated behaviors. One of the main
action between these memory types and the reflective loop advantages of the large language model-based agent against the
ensures that the agent’s memory is not only a repository of past traditionalrule-basedorneuralnetwork-basedagentisitsstrong
events but also a dynamic foundation for future improvement ability to engage in interactive conversation and textual reason-
andlearning.ThissystemexemplifieshowLLMscanevolvefrom ing.Therefore,toevaluatewhethertheagenthasunderstoodthe
static knowledge bases to dynamic entities capable of self- simulation rules well, accurately perceived the environment,
improvement through iterative reflection and adaptation. In S3 madeachoicerationally,etc.,wecandirectlyobtainexplanations
(Gaoetal.,2023),theLLMs’abilitytoreflectisintricatelytiedto from the large language model-based agent. We can evaluate
their simulation of human social interactions, where they whether the agent-based simulation is good by analyzing the
continuously adjust their understanding and responses based on explanationsandcomparingthemwiththehumandataorawell-
evolvingsocialdynamicsandcues.Thisreflectivecapacityenables established theory or model. For example, in economic simula-
them to navigate complex social environments with greater tion(Lietal.,2024b),theauthorsquerythelargelanguagemodel
finesse.In theworkofLi etal.(2024b), reflectionisleveraged to agentaboutthereasonforeconomicdecision-making,whichwell
refine the LLMs’ approach to socio-economic predictions. By explains the simulated actions and behaviors.
reflectingonpastinteractionsandtrends,thesemodelscanadapt
theirpredictivealgorithms,leadingtomoreaccurateresponsesto Ethics evaluation. Besides the simulation accuracy or explain-
future social and economic shifts. ability of the large language model-empowered agent-based
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3 9

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
simulation, the ethics issue is also of great importance. The first solving, etc., offering insights into both individual and collective
oneisbiasandfairness,anditisessentialtoassessthesimulation social behaviors, as illustrated in Fig. 5.
for biases in language, culture, gender, race, or other sensitive
attributes to evaluate whether the generated content perpetuates Simulation of social network dynamics. The part discusses whe-
or mitigates societal biases. Another concern is harmful output therLLMAgents,duetotheirhuman-likebehavior,canbeused
detection since the output of the generative artificial intelligence torecreateandvalidateestablishedsociallawsandpatterns.This
is hard to control compared with traditional approaches. Thus, involvesananalysisofhowcloselytheseagentscanmimichuman
the practitioners of the large language model agent-based simu- behavior and whether their actions can be quantified to validate
lation should scrutinize the simulation’s output for potentially or challenge existing theories in social science.
harmful or inappropriate content, including hate speech, mis- S3(Gaoetal.,2023)utilizesLLM-empoweredagentstosimulate
information, or offensive material. individual and collective behaviors within the social network.This
In summary, the evaluation of the large language model for system effectively replicates human behaviors, including emotion,
agent-based modeling and simulation mainly involves accuracy, attitude, and interaction behaviors. It leverages real-world social
explainability, and ethics. For accuracy, the evaluation can be network data to initialize the simulation environment, where
conductedatboththeindividuallevelandpopulationlevel,based information influences users’ emotions and subsequent behaviors.
on collected real ground-truth data; for explainability, the agent Thestudyparticularlyfocusesonscenariosofgenderdiscrimination
should be able to provide reliable reasons for their generated andnuclearenergy,demonstratingtheabilityofLLMstosimulate
actions; for the ethics evaluation, the agent-based modeling and complex social dynamics. The results underscore LLM’s ability to
simulationsystembuiltwithlargelanguagemodelagentsmaybe capture real-world social phenomena. Specifically, for the
facedwithbiggerconcernscomparedwithtraditionalagent-based individual-level evaluation, the authors mainly focus on the
modelingmethods,sinceLLM-empoweredagentsaremuchmore prediction problem, i.e., whether the LLM agent can predict the
intelligent. nextlabel(emotion,attitude,interaction).Forexample,whetherthe
LLM agent can accurately predict whether the user will have a
positiveattitudetowardonespecificevent.Forthepopulation-level
Recent advances in LLM agent-based modeling and
evaluation,theauthorstestwhetherthesimulatedresultswithlarge
simulation
language model agents have the same trends as the ground-truth
In the following, we elaborate on the recent advances in using
data,includingthepropagationspeed/range,attitudedynamic,etc.
large language models for agent-based modeling and simulation
Williams et al. (2023) study whether LLM agents can accurately
in social, physical, cyber, and hybrid domains. The typical
applicationsinthefirstthreedomainsareillustratedinFig.3,and reproducethetrend ofepidemicspread.Theresultsshowthatthe
LLM agent-based simulation system can replicate complex
the details are shown in Table 1. We also illustrate the ratio of
phenomenaobservedintherealworld,suchasmulti-peakpatterns.
different domains and what to simulate in Fig. 4. From the per- Xu et al. (2023b) examine LLMs’ capabilities in simulating
spective of technical design, the statistics are as follows: about
individual and collective behaviors in a rule-based Werewolf
50% of the papers have considered planning when generating
actions,50%ofthepapershaveusedthereflectionstrategy,80% Gameenvironment.ItrevealsthatLLMscaneffectivelyengagein
strategic social interactions, generating behaviors such as trust
have conducted real-world evaluation, and about 40% have
and confrontation, thus offering insights into their potential for
considered ethical evaluation. Note that almost all the papers social simulations. Acerbi and Stubbersfield (2023) demonstrate
have designed a memory mechanism.
that the information transmitted by large language models
mirrors the biases inherent in human social communication.
Social domain I: social sciences. This section discusses the Specifically, LLM exhibits preferences for stereotype-consistent,
application of LLM agent-based modeling and simulation in negative, socially oriented, and threat-related content, reflecting
social sciences. Specifically, the existing works examine and biasesinitstrainingdata.TheobservationunderscoresthatLLMs
exploreLLMagents’effectivenessinreplicatinghumanbehaviors arenotneutralagents;instead,theyechoandpotentiallyamplify
andinteractionsandtheirroleinvalidatingsocialtheories.They existinghumanbiases,shapingtheinformationtheygenerateand
focus on how LLM agents can serve as tools for understanding transmit.Zhangetal.(2023c)studiedtheimpactofcollaboration
complex social dynamics, enhancing collaborative problem- strategies on the performance of LLM agents. Specifically, three
Fig.3IllustrationofLLMagent-basedmodelingandsimulationindifferentdomains.
10 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
Table1Alist of representativeworksof agent-based modeling andsimulation with largelanguagemodels.
Domain Environment Advance Whattosimulate
Social Virtual Schwitzgebeletal.(2024) Conversationandinteraction
Social Virtual Xuetal.(2023b) Werewolfgame
Social Virtual AcerbiandStubbersfield(2023) InformationPropagation
Social Virtual Zhangetal.(2023c) CollaborationMechanism
Social Virtual SuzukiandArita(2024) Cooperationanddefection
Social Virtual deZarzàetal.(2023) Socialinteraction
Social Real Mukobietal.(2023) Welfarediplomacygame
Social Real S3(Gaoetal.,2023) Onlinesocialnetwork
Social Virtual SimReddit(Parketal.,2022) Onlineforum
Social Real Caietal.(2024) SocialMediaLangauge
Social Real PapachristouandYuan(2024) SocialNetworkDynamics
Social Real COLA(Lanetal.,2024) Cooperativetasksolving
Social Virtual MAD(Liangetal.,2023) Cooperativetasksolving
Social Virtual CHATDEV(Qianetal.,2024) Cooperativetasksolving
Social Virtual MetaGPT(Hongetal.,2024) Cooperativetasksolving
Social Virtual ChatEval(Chanetal.,2024) Cooperativetasksolving
Social Virtual CAMEL(Lietal.,2023d) Cooperativetasksolving
Social Virtual AgentVerse(Chenetal.,2024) Cooperativetasksolving
Social Virtual SPP(Wangetal.,2023d) Cooperativetasksolving
Social Virtual CoELA(Zhangetal.,2024b) Cooperativetasksolving
Social Real AgentHospital(Lietal.,2024a) Cooperativetasksolving
Social Virtual HumanoidAgents(Wangetal.,2023c) Individualsocialbehavior
Social Real SocioDojo(ChengandChin,2024) Individualsocialbehavior
Social Virtual Liuetal.(2024a) Individualsocialbehavior
Social Virtual Argyleetal.(2023) Individualsocialbehavior
Social Virtual Hämäläinenetal.(2023) Individualsocialbehavior
Social Virtual Singhetal.(2023) Individualsocialbehavior
Social Virtual BinzandSchulz(2023) Individualsocialbehavior
Social Virtual Elyosephetal.(2023) Individualsocialbehavior
Social Virtual Lietal.(2022) Individualsocialbehavior
Social Virtual XieandZou(2024) Individualsocialbehavior
Social Virtual Yoonetal.(2024) Individualsocialbehavior
Social Virtual Horton(2023) Economicsystem:individualbehavior
Social Virtual Chenetal.(2023e) Economicsystem:individualbehavior
Social Virtual Geerlingetal.(2023) Economicsystem:individualbehavior
Social Real Xieetal.(2023) Economicsystem:marketbehavior
Social Real Faria-eCastroandLeibovici(2023) Economicsystem:marketbehavior
Social Real Bybee(2023) Economicsystem:marketbehavior
Social Virtual PhelpsandRussell(2023) Economicsystem:gametheory
Social Virtual Akataetal.(2023) Economicsystem:gametheory
Social Virtual Guoetal.(2023) Economicsystem:gametheory
Social Virtual Zhaoetal.(2023b) Economicsystem:consumptionmarket
Social Virtual Hanetal.(2023) Economicsystem:consumptionmarket
Social Virtual Zhaoetal.Nascimentoetal.(2023) Economicsystem:consumptionmarket
Social Virtual Chenetal.(2023c) Economicsystem:auctionmarket
Physical Real Shahetal.(2023a) Navigationbehavior
Physical Real NLMap(Chenetal.,2023b) Navigationbehavior
Physical Real Zouetal.(2023) Wirelessnetworkusers
Physical Real Cuietal.(2024) Vehicledrivers
Physical Virtual GITM(Zhuetal.,2023c) Tool-usagesimulationinsandboxgame
Cyber Real WebAgent(Guretal.,2024) HumanbehaviorsinWeb
Cyber Real Mind2Web(Dengetal.,2024) HumanbehaviorsinWeb
Cyber Real Zhouetal.(2024a) HumanbehaviorsinWeb
Cyber Real Parketal.(2023) HumanbehaviorsinWeb
Cyber Virtual RecAgent(Wangetal.,2023b) Interactionwithrecommendersystem
Cyber Virtual Agent4Rec(Zhangetal.,2024a) Interactionwithrecommendersystem
Hybrid Virtual Williamsetal.(2023) Epidemicspreading
Hybrid Virtual Generativeagents(Parketal.,2023) Sandboxsociallife
Hybrid Real WarAgent(Huaetal.,2023) Warsimulation
Hybrid Real Lietal.(2024b) Economicsystem:macroeconomics
Hybrid Real UGI(Xuetal.,2023a) Humanbehaviorsinreal-worldcity
agents with distinct personalities (easy-going or overconfident) those relying solely on memory reflection. That is, it highlights
formed four different societies, employing eight collaboration LLM agents’ capability to exhibit human-like social phenomena
strategies over three rounds to solve mathematical problems. It ofconformityandtheWisdomofCrowdseffect,wherecollective
means that strategies initiating a debate show better results than intelligence tends tosurpass individual capabilities.Kimand Lee
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3 11

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
Fig.4Illustrationoftheratioofdifferentdomainsandsimulationobjectivesoftherecentworksoflargelanguagemodelagent-basedmodelingand
simulation.
Trends,Messagepropagation Cooperativetasksolving Individualsocialbehavior
Reflection
Long/short-term Planning
Long/short-term Memory
Profile Personality
Fig.5TaxonomyofLLM-basedmodelingandsimulationinsocialsciences.Therepresentativeworksinclude(Gaoetal.,2023),ChatDev(Qianetal.,
2024),andHumanoidagents(Wangetal.,2023c).
(2023) assessed the boundaries and effectiveness of LLMs in variations in social network structures, among other factors.
modeling personal actions and societal dynamics, shedding light Park et al. (2022) investigated LLM agents’ capacity to simulate
ontheirapplicabilityforbelievablesocialsimulations.Suzukiand online behaviors within forums. It demonstrates how LLMs can
Arita (2024) and de Zarzà et al. (2023) constructed simulation predict user interactions and responses by generating scenarios
systems with multiple agents, employing LLM as a generator of based on specific forum rules and descriptions. This simulation
social strategy variations to simulate changes in cooperation/ assistsinrefiningforumregulations,highlightingthepotentialof
selfish strategies among agents in social cooperation and LLMs in understanding and shaping digital social environments.
12 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
Cai et al. (2024) employed a multi-agent simulation framework focusingontooldevelopment.ItinvolvesroleslikeTaskDetailing
using to study language evolution in regulated social media. It Assistant,Commander,andExecutor.Specifically,TaskDetailing
featuresLLM-drivensupervisoryandparticipantagents,simulat- Assistant specifies tasks in detail, Commander provides step-by-
ing communication under strict regulations. The framework step instructions based on these specifics, and Executor carries
evaluates scenarios from abstract to real-world, demonstrating out these instructions. Li et al. (2024a) introduced Agent
LLMs’ ability to adapt language strategies, improving evasion of Hospital, a simulation of the entire process of treating illness
supervision and information accuracy. Papachristou and Yuan using LLM agents, and proposed the MedAgent-Zero method,
(2024) examined the behavior of LLM agents in forming social demonstrating improved treatment performance and real-world
networks, comparing their dynamics to human social behaviors. applicability.
The study highlights key principles such as preferential attach- Theaboveeffortsinvolvedesigningspecifictypesofagents,their
ment, triadic closure, homophily, community structure, and the roles, and the collaboration framework for certain tasks. The
small-world phenomenon, revealing that LLMs’ network forma- limitationliesintheirlackofversatility,asthedesignoftheagents
tion decisions are influenced more by triadic closure and is not flexible or adaptable. To address it, some work focuses on
homophily than preferential attachment. adaptivelyperformingtaskswithautomatedgeneratedLLMagents
and cooperation framework. AgentVerse (Chen et al., 2024)
Simulationofcooperation.Someotherworkspayattentiontothe simulated human group problem-solving focusing on adaptively
humancollaboration replicatedby LLM agents. Specifically,they generatingLLMagentsfordiversetasks.Itinvolvesfourstages:(1)
focus on how these agents, assigned distinct roles and functions, Expert Recruitment, where agent composition is determined and
can mimic the cooperative behaviors observed in real human adjusted; (2) Collaborative Decision-Making, where agents plan
societies.Themechanismsand cooperativeframeworks designed problem-solving strategies; (3) Action Execution, where agents
for these agents can enable them to work together efficiently implementthesestrategies;(4)Evaluation,assessingprogress,and
toward achieving goals. guiding improvements. That is, it can effectively enhance agents’
COLA (Lan et al., 2024) proposed to organize LLM agents to capabilities across various tasks, from coding to embodied AI,
discuss and finally decide the stance on social media text, with demonstrating their versatility in collaborative problem-solving.
threerole-playedagents: analyzer,debater,and summarizer. The Wangetal.(2023d)introducesoloperformanceprompting(SPP)
analyzersdissecttextsfromlinguistic,domain-specific,andsocial to emulate human-like cognitive synergy, which transforms a
media perspectives; the debaters propose logical links between singleLLMintoamulti-personaagent,enhancingproblem-solving
text features and stances; finally, the summarizer considers all intasksrequiringcomplexreasoninganddomainknowledge.For
these discussions and determines the text’s stance. The frame- tasks like trivia creative writing and logic grid puzzles, SPP
work achieves SOTA performance on stance detection tasks. significantly outperforms standard methods, showcasing its
MAD(Liangetal.,2023)proposedtouseLLM agentstoengage effectiveness in collaborative problem-solving. CoELA (Zhang
in reasoning-intensive question answering through structured etal.,2024b)integratesLLMs’criticalcapabilities,includingnatural
debates.LLMsadopttherolesofopposingdebaters,eacharguing language processing, reasoning, and communication, into a novel
for a different perspective on the solution’s correctness. MAD cognitive-inspired modular framework. The authors evaluate
enforces a “tit for tat” debate dynamic, wherein each agent must CoELA in various embodied environments like C-WAH and
argue against the other’s viewpoint, leading to a more TDW-MAT, demonstrating its proficiency in perceiving, reason-
comprehensive exploration of potential solutions. A judge agent ing, communicating, and planning. The results show that CoELA
then evaluates these arguments to arrive at a final conclusion. surpasses traditional planning methods and exhibits effective
This work fosters divergent thinking and deep contemplation, cooperationandcommunicationbehaviors.
addressing the degeneration-of-thought issue common in self- In conclusion, simulating collaborative behaviors among LLM
reflection methods. CHATDEV (Qian et al., 2024) is a virtual agents in various frameworks has shown their potential in
softwaredevelopmentcompanywhereLLMAgentscollaborateto emulatinghumancooperativebehaviorstotackleawiderangeof
develop computer software, with different roles for agents problem-solving tasks.
includingCEO,CTO,designers,andprogrammers.Thecoopera-
tion process encompasses designing, coding, testing, and Simulation of individual social behavior. In the simulation of
documenting, with agents engaging in role-specific tasks like social dynamics and cooperative problem-solving, LLM agents
brainstorming,codedevelopment,GUIdesigning,anddocumen- show a strong ability to replicate human behavior. However,
tation. MetaGPT (Hong et al., 2024) also introduced a novel achieving a closer approximation to real human responses from
framework for collaborative software development with LLM the individual perspective is also of great significance. In this
agents,simulatingasoftwarecompany.Therolestheagentsplay, section, we discuss how the recent works approach the problem
including Product Manager, Architect, Project Manager, Engi- howtobettersimulatetheindividualhumanbehaviorinasocial
neer, and QA Engineer, that follows the standardized operating context with LLM agents, enhancing their decision-making pro-
procedures.Eachrolecontributessequentially,fromrequirement cesses, interaction patterns, and emotional responses.
analysis and system design to task distribution, coding, and Humanoid agents (Wang et al., 2023c) propose a novel
quality assurance, showcasing LLMs’ potential in efficiently approachtoenhancingtherealismofLLMagentsimulations.By
mimicking human cooperative behaviors and workflows in incorporatingelementsofhumancognitiveprocessing(System1
complex software development. ChatEval (Chan et al., 2024) (Daniel, 2017)), such as basic needs, emotions, and relational
present a multi-agent framework for text quality evaluation, closeness, Humanoid Agents are designed to behave more like
employing LLMs as diverse role-playing agents, in which key humans. For each agent, the authors maintain an internal state
roles include the public, critics, journalists, philosophers, and (stored in files) including human needs and emotions. The
scientists, each contributing unique perspectives. The agents human needs and emotions are generated by agents with role-
engage in sequential debates, with access to all communication playing prompts, and are updated according to the context and
history. Finally, a judge gives a final decision. It results in more environment changes. These dynamic elements allow agents to
accurate and human-aligned evaluations compared to single- adapt their activities and interactions based on their internal
agent methods. CAMEL (Li et al., 2023d) introduces a states, thereby bridging the gap between simulated and real
cooperative role-playing framework with communicative agents, human behavior. The platform also facilitates immersive
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3 13

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
Fig.6TaxonomyofLLM-basedmodelingandsimulationineconomicsystems.
visualization and analysis of these behaviors, advancing the field Social domain II: economic system. This section discusses
of social simulation and cooperative problem-solving. This another important field in the social domain, the economic sys-
approach demonstrates a significant leap in individual agent tem. Currently, LLM-driven economic simulations can be cate-
design, moving closer to replicating the complexities of human gorizedintothreetypesbasedonthenumberofagentsinvolved:
decision-makingandinteractionpatterns.SocioDojo(Chengand individual behavior, interactive behavior, and economic system-
Chin, 2024) is a lifelong learning environment using real-world level simulations. For individual behavior simulations, the pri-
datafortrainingagentsinsocietalanalysisanddecision-making. mary goal of related research is to simulate the human-like eco-
It introduces an innovative Analyst–Assistant–Actuator frame- nomic decision-making capabilities of LLMs (Bauer et al., 2023;
work and Hypothesis-Proof prompting, resulting in notable Chen et al., 2023e; Geerling et al., 2023; Horton, 2023) or their
improvements in the time series forecasting task. Liu et al. understanding of economic phenomena (Bybee, 2023; Faria-e
(2024a) present a novel approach to optimizing LLM agents by Castro and Leibovici, 2023; Xie et al., 2023). This provides an
refining agents’ decision-making processes, interaction patterns, empirical foundation for the latter two types of economic simu-
and emotional responses through a three-stage alignment lations and is currently a more extensively researched area. In
learning framework, Stable Alignment. This framework, which interactive behavior simulations, the focus is mainly on game
efficiently teaches social alignment to LLMs, is based on theory,exploringwidelyfocusedbehaviorsofLLMsduringgame-
simulated social interactions, detailed feedback, and progressive playing, such as cooperative and reasoning behaviors (Akata
refinement of responses by autonomous social agents. Xie and et al., 2023; Guo S et al., 2024; Guo et al., 2023; Phelps and
Zou(2024)developedahuman-likeplanningframeworkforLLM Russell, 2023). For system-level simulations, the research pri-
agents, focusing on the multi-phase travel planning problem. By marily targetsmarket simulations, such as consumption markets
simulatinghumanplanningpatterns,theframeworkenablesLLM or auction markets, and investigates the rationality oroptimality
agents to generate coherent outlines, integrate information of LLMs’ economic behaviors within these markets (Weiss M
collection, and provide essential details. et al., 2024; Chen et al., 2023c; Li et al., 2024b; Zhao et al.,
Moreover, some studies use LLM agents to simulate human 2023b). The illustration is shown in Fig. 6.
responsesinsocialscienceresearch.Argyleetal.(2023)useLLM
agents as proxies for specific human populations to generate Individual economic behavior simulation. Considering the
responses in social science research. The authors show that, human-like characteristics of LLMs,manyresearchersattempted
conditioned on socio-demographic profiles, LLM agents can to replace humans in behavioral economics experiments with
generate outputs similar to human counterparts. Hämäläinen LLMs to observe the rational and irrational factors in their eco-
etal.(2023)constructLLMagentstosimulaterealparticipantsto nomic decision-making. Horton (2023) replicated classic beha-
fill in open-ended questionnaires and analyze the similarity vioral economics experiments using LLMs, including unilateral
between the response and real data. The results show that dictatorgames,fairnessconstraints(Kahnemanetal.,1986),and
syntheticresponsesgeneratedbylargelanguagemodelscannotbe status quo bias (Samuelson and Zeckhauser, 1988), confirming
easily distinguished from human data. Yoon et al. (2024) the human-like nature of LLMs in aspects such as altruism,
introduced a protocol to use LLM agents to simulate human fairness preferences, and status quo bias (Horton, 2023).
behavior in conversational recommender systems. By assessing Although the experiment was conducted simply by asking GPT
baseline simulators, the study identifies deviations between questions and analyzing responses, this represents a preliminary
language models and human behavior, providing insights on attempt to explore the use of LLMs for simulating human eco-
improving model accuracy through better model selection and nomic behavior. Chen et al. (2023e) have employed standard
prompting strategies. In short, these works indicate that LLM frameworks,revealedpreferencetheory,tosimulatetherationality
agents can be useful in social science experiments to simulate in the economic decisions of GPTs. Results show that GPT per-
human responses with much lower costs. formslargelyrationallyinrisk,time,social,andfoodpreferences
Some researchers have also studied LLM agents’ ability to domains in terms of budgetary decisions. Additionally, Geerling
simulate human behavior in social psychological experiments. et al. (2023) have utilized the Test of Understanding in College
Specifically, these works (Binz and Schulz, 2023; Singh et al., EconomicstosimulateLLMs’comprehensionofmicroeconomics
2023) use psychological tests to simulate the human response to and macroeconomics, with results indicating that LLMs outper-
test the cognitive ability, emotional intelligence (Elyoseph et al., form most students who have taken economics courses.
2023), and psychological well-being (Li et al., 2022) of LLMs, Another research line to test the economic capabilities of LLMs
demonstratingthatLLMagentshavehuman-likeintelligencetoa involvesaccuratelyunderstandingcertainsocio-economicphenom-
certain degree. ena,specificallybyusingexternaltextinformation(suchasnews)to
14 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
predict future economic changes. Xie et al. (2023) used LLM to also a few studies attempting to construct strong game-playing
predict stock market movements with historical stock data and agents. Guo et al. (2023) go beyond simple measurement and
related tweets based on the perception of investor sentiment. enhance LLMs’ gaming abilities through prompt engineering.
However,thepredictiveperformanceofLLMsisworsethanthatof This work, specifically in an incomplete information game
state-of-the-art methods, and in some cases, it is even inferior to (namely Leduc Hold’em), has created agents with higher-order
traditional linear regression. Faria-e Castro and Leibovici (2023) theory of mind that can significantly outperform traditional
utilized LLMs for quarterly inflation forecasts, achieving accuracy algorithm-basedopponentswithouttherequirementfortraining.
comparable to, if not surpassing, the results of the Survey of MetaFundamentalAIResearchDiplomacyTeam(FAIR)†etal.,
Professional Forecasters (SPF). Bybee (2023) tested LLMs on their 2022) proposed the first AI agent Cicero combining a language
predictions of finance and macroeconomics after reading specific model and reinforcement learning to play the Diplomacy game.
sectionsofTheWallStreetJournal,withresultsequivalenttothose Aftercompetingwithrealhumansinonlinegamesanonymously,
of SPF. These results suggest that LLMs possess a basic under- results show that Cicero can outperform 90% of players. Even
standingofeconomicandfinancialmarketsbutstilllacksufficient without employing LLMs, it has been demonstrated that earlier
and precise perception for accurate prediction, requiring more language models can approach or even surpass human capabil-
domain-specific data for additional fine-tuning. itiesintherealmofstrategicgaming.Moreover,Maoetal.(2023)
developedasimulationframeworknamedAlympics,consistingof
Interactive economic behavior simulation. These simulations a sandbox playground and several agent players. The sandbox
mainly focus on game theory, where there are only two or a few playground serves as the environment that stores and executes
agents as opponents. Observing and analyzing the interactive game settings, and agent players interact with the environment.
behavior and capabilities of LLMs in various classic games is a The framework enables controlled, scalable, and reproducible
current research hotspot. Guo (2023) studied the behavior of simulation of game theory experiments.
large language model agents in the ultimatum game and pris- Theresultsfromthesesimplesimulationenvironmentsfurther
oner’s dilemma game and found that the agents exhibit some validate the perception, reasoning, and planning capabilities of
similar patterns as humans, such as the positive correlation LLMs.Inordertomaximizetheirgoals,LLMsconsidertheirown
between offered amounts and acceptance rates in the ultimatum benefits and opponents’ strategies when making economic
game. Phelps and Russell (2023) found that incorporating indi- decisions. It is worth noting that these goals can be customized
vidual preferences into prompts can influence the level of coop- through prompts, such as maximizing returns or maximizing
eration of LLMs. Specifically, they construct LLM agents with fairness.
different personalities like competitive, altruistic, self-interested,
etc., via prompts. Then, they let the agents play the repeated Economicsystem-levelsimulation.Inaneconomicsystem,agents
prisoner’s dilemma game with bots with fixed strategies (e.g. often interact with each other, trade goods, and form a market.
always cooperate, always defect, or tit-for-tat) and analyze the These agents may not be limited to individuals but can also
agents’ cooperation rate. They find that competitive and self- represententitiessuchascompaniesandbanks,asthesearealso
interested LLM agents show a lower cooperation rate, while important components of the market. Zhao et al. (2023b),
altruisticagentsdemonstrateahighercooperationrate,indicating through simple consumption market simulations, uncovered
the feasibility of constructing agents with different preferences competitive behaviors of LLM agents in managing restaurants,
through natural language. However, LLM agents also have lim- which are aligned with well-known sociological and economic
itations in some capabilities, such as the inability to reasonably theories. Specifically, the dish prices tend to be consistent with
respond to opponents’ actions, which may lead to higher coop- each other in the two simulated restaurants. Matthew effect also
erationpreferenceswithbetrayingopponents.Theunderstanding emergesduringthesimulation,i.e.,onerestaurantbecomesmore
of LLM social behaviors is very important for subsequent devel- popularandpopularwhileanotherhasfewconsumers.Moreover,
opments in artificial intelligence and its impact on human social restaurantsimitatecompetitors’behaviors,andatthesametime,
behavior. Other research (Guo S et al., 2024) measured LLMs’ they try to make differentiation to attract more consumers.
rationality and strategic reasoning ability using the second-price Similarly, Han et al. (2023) studied the collusion between firms’
auction and the Beauty Contest game. In such games, fully price strategies. They simulated the product pricing process of
rationalplayersareassumedtochoosethemostbeneficialchoice twofirmsinamarketenvironment(i.e.,Bertrandduopolygame)
from their point of view, which results in the Nash equilibrium. based on LLM. The results show that in the absence of com-
Therefore, the authors define the deviation of LLMs’ behavior munication, prices tend to approach the Bertrand equilibrium
from Nash equilibrium as the rationality degree. Moreover, they price. However, with communication, collusion between the
measurethestrategicreasoningabilityofLLMsbytheratioofthe companies tends to bring prices closer to the monopoly price.
actualpayofftotheoptimalpayoff.ExperimentsshowthatLLMs Nascimento et al. (2023) simulated a simple online book mar-
generallydemonstraterationalitytosomedegreewhiletheyoften ketplace and observed interesting phenomena such as price
cannot reach the Nash equilibrium. Among them, GPT-4 shows negotiation between sellers and buyers. Another work (Weiss M
better strategic reasoning ability and can converge to Nash et al., 2024) attempts to have LLMs act as intermediaries in
equilibrium faster than other LLMs like GPT-3.5 and text- information trading markets to address the issue of information
davinci.Theauthorsclaimtoprovideabenchmarkfortestingthe asymmetrybetweenbuyersandsellers.Specifically,whenaseller
economic capabilities of the LLM research community. Akata presents information and quotes a price as the response to the
et al. (2023) discovered through experiments in multiple game queryfromabuyer,anLLMagent,actingasanintermediary,can
scenariosthatLLMsareskilledingamesvaluingtheirself-interest decide whether to purchase and, if choosing not to, forget the
but not as adept at coordinating with others. Specifically, in the information seen, thus protecting the seller’s interests. In
prisoner’sdilemma,GPT-4willcooperatewellwithacooperative experiments,theinformationtoexchangeisactuallythe‘passage’
opponent but will always choose to defect after the opponent from documents on the topic of LLMs from ArXiv. The results
defectsonce.IntheBattleoftheSexes,GPT-4cannotcoordinate show thatLLMcannotonlymake rationalpurchasing decisions
well with the opponent’s choices to obtain maximum payoff. in this information market but also ensure the rationality of the
In addition to the observations on the cooperative behavior overall market dynamics; for example, a higher budget can
and reasoning abilities of LLM agents during gaming, there are improve the quality of purchased answers (response to queries).
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3 15

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
Chen et al. (2023c) have developed LLM agents with planning and exchange knowledge to solve a complex task together. Spe-
capabilities in constructed virtual auction markets to achieve cifically,intentsfromhumansormachinesareprovidedtoagents
higherprofitsgivenlimitedbudgets.ExperimentsshowthatLLM throughwirelessterminals,andthetasksaredividedandplanned
has the crucial abilities to participate in the auction, including collaboratively among multiple agents by leveraging the knowl-
managing budgets, considering long-term returns, etc, even edge of different LLMs and device capabilities. On each device,
through only simple prompts. the agent observes the environment and actors to execute deci-
sions. On-device LLMs can extract semantic information from
various data types and store it for future task planning. To deal
Physical domain. For the physical domain, the applications for withaspecifictask,theagentcanretrieverelevantinformationor
LLM agent-based modeling and simulation include mobility createlower-leveltasksandsendthemtootheragentstoachieve
behaviors, transportation, wireless networks, etc. thegoal.Theauthorsdemonstratetheabilityoftheframeworkby
anexampleofawirelessenergy-savingtask,wherefourusersaim
LLM agents for simulating mobility behaviors. Understanding to reduce the network energy consumption while keeping the
real-world space and time is crucial to harness LLMs for agent- transmission rate. In the experiment, the agents gradually
based modeling and simulation in human mobility behaviors. decreasetheirownpowerlevelbasedonpreviousactionsofother
Researchers have delved into this issue through various investi- users and manage to achieve the target after a few iterations,
gations(GurneeandTegmark,2024;Manvietal.,2024).Gurnee which shows the potential of LLM agent-based modeling and
and Tegmark (2024) focus on probing LLMs to extract repre- simulation in solving wireless network problems.
sentations of real-world locations and temporal events, and the
resultsdemonstratethatthesemodelsbuildspatialandtemporal
representationsintheneurallayers.Manvietal.(2024)delveinto Cyberdomain.Agent-basedmodelingandsimulationcyberspace
the geospatial knowledge embedded in LLMs. By fine-tuning mainly involves various human behaviors such as information
LLMs on map-based prompts, substantial geospatial knowledge access, website visitation, network attack/defense, etc., in
within LLMs is illustrated and shows improvements in tasks cyberspace.
related to population density, asset wealth, and education. These WebAgent (Gur et al., 2024) is introduced as an LLM-driven
investigations contribute valuable insights into the nuanced agentcapableoflearningfromitsexperiencestosimulatehuman
understanding of real-world space and time by LLMs, laying the behaviorsonrealwebsitesbasedonnaturallanguageinstructions.
groundwork for their application in agent-based simulations. Itstrategizesbybreakingdowninstructionsintomanageablesub-
Based on their fundamental abilities, LLMs have showcased parts,condenseslengthyHTMLdocumentsintorelevantsections
remarkablecapabilitiesinsimulationforthephysicaldomain.For for the task at hand, and interacts with websites using Python
simulating the human-like navigation behaviors in the physical programsderivedfromthisinformation.Mind2Web(Dengetal.,
environment, LM-Nav (Shah et al., 2023) combines large 2024) further used large language models (LLMs) to construct
language models with image-language alignment algorithms. these generalist web agents. While the sheer size of raw HTML
Following it, LLM-Planner (Song et al., 2023) harnesses large from real websites poses a challenge for LLMs, Mind2Web
language models to achieve few-shot planning for embodied demonstrates that pre-filtering this data with a smaller language
agents.Movingintothedomainofreal-worldplanningwithlarge model substantially enhances the effectiveness and efficiency of
language models, Chen et al. (2023b) introduce NLMap, which the LLMs in generating human-like web browsing behaviors.
creates an open-vocabulary and queryable scene representation, Zhou et al. (2024a) further addressed the discrepancy between
allowing language models to gather and integrate contextual current language-guided autonomous agents, often tested in
informationforcontext-conditionedplanning.Additionally,Shah simplified synthetic environments and the complexity of real-
etal.(2023b)studytrainingageneralgoal-conditionedmodelto world scenarios. The authors build a highly realistic and
simulate human-like vision-based navigation, demonstrating the reproducible environment specifically tailored for language-
broad generalization capabilities of LLMs in complex physical guided agents simulating human behaviors on the web. Park
environments. etal.(2023)simulateonlinedecision-makingscenarios,exploring
the challenges individuals face when lacking domain expertise
LLMagent-basedmodelingandsimulationfortransportation.The while searching for and making decisions using online informa-
possibility of using LLM agents for other applications in the tion.Wangetal.(2023b)proposedtobuildlargelanguagemodels
physical domain, like transportation, has also been explored. Jin to interact with recommender systems by selecting from
etal.(2023)designanLLMagenttosimulatethedrivingbehavior recommendation results and providing positive or negative
ofhumandrivers.Specifically,theagentinteractswithasimulator feedback. It serves as the testing protocol for evaluating the
named CARLA, where it receives information about the state of recommender system’s performance: whether it can satisfy the
thecarandenvironmentfromthesimulatoranddecideswhatto agents’ preferences well.
do next, such as stop, speed up, change lanes, and so on, which In RecAgent (Wang et al., 2023b), the researchers explore the
willbefedbacktothesimulator.Duringthedecisionprocess,the potential of LLMs in simulating user behaviors within online
agent will consider its recent behaviors using a memory module environments,particularlyrecommendersystems.Bycreatingan
and also take into account safety criteria as well as guidelines LLM-based autonomous agent framework, the study investigates
learned from human expert drivers. Experiments show that the how these agents can simulate complex human interactions and
agent designcan significantly reduce collision rate and make the decisionsinavirtualenvironment.Thisapproachenablesanovel
agent’sbehaviormorehuman-like.Moreover,theagentmanages method for studying user behavior, offering insights into how
to perform complex driving tasks such as overtaking. users might react to different scenarios in digital platforms, thus
advancing our understanding of user dynamics in virtual spaces.
LLMagent-basedmodelingandsimulationforwirelessnetwork.In Zhang et al. (2024a) proposed to build generative agents for the
addition, some researchers focus on deploying LLM agents to recommender system in which the authors design LLM-
simulate device users in the city infrastructure, such as the empowered generative agents equipped with user profile,
wireless network. Zou et al. (2023) propose a framework where memory, and actions modules specifically tailored for the
multipleon-deviceLLMagentscaninteractwiththeenvironment recommendersystem.Theproposedagentscanemulatethefilter
16 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
bubble effect and discover the underlying causal relationships in navigation, etc., showing promising abilities in simulating city
recommendation tasks. activities based on embodied agents.
Open problems and future directions
Hybriddomain.Insomestudies,simulationsareconductedthat Efficiency of scaling up. Many studies of LLM agents find it
simultaneouslyconsidermorethanonedomain,suchasphysical
advantageous to simultaneously simulate multiple personas and
and social, and we refer to these simulations as being within a
exploit the synergy effect by allowing them to communicate and
hybrid domain. vote for the final output (Yao et al., 2024). For example,
As a pioneering work, Generative Agents (Park et al., 2023) researchers find LLM-based software development can be sig-
offers a compelling insight into the generation of believable nificantly improved by simulating a virtual software company
individualandsocialbehaviors.Theresearchfocusesonacentral withdiversesocialidentities,includingchiefofficers,professional
question:howcangenerativeagentsreliablyproducehuman-like
programmers,testengineers,andartdesigners(Qianetal.,2024).
individual actions and social dynamics? It delves into an agent
Thisvirtualcompanyiscapableofstreamliningthedevelopment
architecture that integrates memory (for storing past experi-
ences), reflection (to make rational present decisions), and o te f st c i o n m g, p a le n x d so d f o t c w u a m re en so ti l n u g ti . o M ns o i r n eo t v h e e r, st r a e g s e e s ar o c f h d er e s sig g n en in e g r , al c l o y d fi in n g d ,
planning (for future actions). This architecture is critically
e ev ff a e l c u t a iv te e d nes t s hr o o f ug th h e c m ro e w m d o - r s y o , u r r e c fl e e d cti a o s n se , s a sm nd en p ts la , nn af i fi n r g m m in o g du t l h e e s s d c i a v l e i r n s g e u p p er t s h o e na n s um ar b e er be o n f e s fi im cia u l la i t n ed v a a g ri e o n u t s s a ta n s d ks de ( p Z l h o u y g in e g e m t o a r l. e ,
2023).
in generating rational behaviors. Notably, this approach led to
complex social scenarios, such as Valentine’s Day parties and However,simulatingsocietiesoflarge-scaleLLMagentsisvery
mayoral elections, underscoring the agents’ proficiency in computationally expensive. Extensive research efforts are dedi-
catedtooptimizingthememoryfootprint(Shengetal.,2023)and
simulatingnuancedhumaninteractionsandsocietalevents.This
operation subroutines (Aminabadi et al., 2022) of language
research offers a substantial contribution to social simulations,
models. Researchers also develop several effective model
demonstrating the advanced potential of LLM agents in
compression techniques (Zhu et al., 2023d), such as knowledge
replicating the depth and complexity of human social behaviors.
distillation and quantization. In the context of LLM agent
Williams et al. (2023) conducted an epidemic simulation
simulation, batch prompting (Cheng et al., 2023b) is a highly
within a hybrid domain. In this simulation, social relationships
influenced individuals’ perception of the epidemic, while relevanttechniquethatiscapableofsimulatingmultipleagentsin
individuals’ physical movements within spatial contexts affected b ef a fi tc c h ie e n s c . y Ex i p m er p im ro e v n em ts e s n h t ow in bat i c n h fe p re r n om ce pt t i o n k g e c n an a a n c d hie t v im eu e p c to os 5 ts × .
their susceptibility to infection. Welfare Diplomacy (Mukobi Besides, MetaGPT is proposed to improve the efficiency of
et al., 2023) sets a benchmark, a nation-to-nation war/welfare
multi-agent collaboration in virtual software companies Hong
equilibrium tabletop game designed to evaluate the collaborative
et al. (2024). They leverage a shared message pool and subscribe
capabilities of large language models.
mechanism to reduce the time and token cost of generating one
Hua et al. (2023) proposed to use LLM agents to represent
line of code. Despite the previous efforts of accelerating LLM
countries and simulate their decisions and consequences, based
on which the historical international conflicts, including World a ch ge a n ll t e s n , gi s n im g u ta la sk ti , n w g h l i a c r h ge s - ig sc n a i l fi e ca L n L tl M y hi a n g d e e n r t s s L r L e M ma a in ge s nt a si h m ig u h la ly -
War I, World War II, and the Warring States Period in Ancient
tion from reaching its full potential. Simulating large societies of
China are selected for evaluation. In the LLM agent-based war
LLM agentsnotonlycaneffectively improvetheperformancein
simulations, the emergent interactions among countries help
downstream tasks but also has the potential to mimic the
explain why the wars occur.
emergence properties of human societies and, hence, reveal the
Lietal.(2024b)simulateahybridmacroeconomicsystemand
underlyingmechanisms(Caldarellietal.,2023).Therefore,itisan
expand the scale of simulation environments from tens to
hundreds. Specifically, they simulate LLM-empowered agents’ important open problem to achieve full-process acceleration of
LLM agent simulations.
work and consumption behaviors in a macroeconomic market.
The proposed perception, memory, and action modules endow
the agents with real-world heterogeneity, the ability to grasp Benchmark. Benchmarks have significantly advanced the devel-
market dynamics, and decision-making considering multiple opment of AI in the past decade. Landmark benchmarks like
economic factors, respectively. Experimental results show the ImageNet (Russakovsky et al., 2015), GLUE (Wang et al., 2019),
emergence of more reasonable and stable macroeconomic and the benchmarks in graph learning (Dwivedi et al., 2023; Hu
indicators (price inflation, unemployment rate, GDP, and GDP etal.,2020)havebeenpivotaltotherapidinnovationinthefields
growth rate) and regularities (Phillips curve and Okun’s law) of computer vision, natural language processing, and graph
compared with traditional rule-based ABM (Gatti et al., 2011; neural networks.
Lengnick, 2013) and RL-based approaches (Zheng et al., 2022). Recently,therehasbeenasurgeinbenchmarksthatassessthe
Especially,onlythesimulationbasedonLLMagentscanproduce capabilities of LLM-driven agents, highlighting the growing
the correct Phillips curve, i.e., negative relationship between the interest in this emerging area. For example, researchers
unemployment rate and inflation. This advantage is owned by Valmeekam et al. (2022) developed benchmarks to evaluate
LLM’s accurate perception of market dynamics, such as the LLM’s capability in planning and reasoning about change,
deflation of labor markets. focusing on symbolic models and structured inputs compatible
Urban generative intelligence (UGI) (Xu et al., 2023a) is a with such representations. Meanwhile, AgentBench develops a
platform that constructs a real-world urban environment multi-dimensional benchmark with eight distinct environments
provided by digital twins, which provide various interfaces for to assess the capabilities of LLM-driven agents in various multi-
embodied agents to generate many behaviors, supported by a turn open-ended generation settings (Liu et al., 2024b).
foundation model named CityGPT, which is trained on city- MLAgentBench, on the other hand, designs a suite of ML tasks
specificmulti-sourcedata.Inthisplatform,multiplecategoriesof for benchmarking LLM-driven AI research agents, including
LLM-based agents can simulate human-like behaviors, including taskslikeimageclassificationandsentimentclassification(Huang
social interactions, economic activities, mobility, street et al., 2023). Researchers also propose to evaluate LLM-driven
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3 17

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
agentswithembodiedtasks,usingthemashigh-levelplannersin proposed as a general and customizable agent framework
robotics setups or in textual environments, focusing on the designed for real-world applications, which supports model
interaction between planning and action, like ALFWorld training on multiple open-source LLMs and offers diversified
(Shridhar et al., 2021) and ComplexWorld (Basavatia et al., and comprehensive APIs. On top of the textual embodied
2023). On top of textual environments, online reinforcement environment ALFWorld, researchers developed BUTLER frame-
learning approaches are developed to align LLM agents with work (Shridhar et al., 2021) that can operate across text and
human preferences and evaluate their performance (Carta et al., embodiedenvironmentswiththreemaincomponents,i.e.,brain,
2023). vision,andbody.ThisarrangementallowsBUTLERtoeffectively
However, the previous benchmarks mainly focus on the bridge the gap between abstract language understanding and
decision and planning capability of LLM-driven agents, the practical, embodied task execution in simulated virtual environ-
assessment of LLM-driven agent simulation is still inadequate. ments. However, these previous works mainly focus on task-
On the one hand, there still exist challenges in evaluating the solving LLM agents, while the open platforms for LLM-driven
performanceofagentsimulations.Previousworksoftenexamine ABS are still lacking. Such a gap can be largely attributed to the
the statistics feature of simulated behavior (Feng et al., 2020), challenges of integrating LLM-driven agents with the complex
suchasthespatialandtemporaldistribution.Recentstudiesalso environment of simulation. Urban generative intelligence (UGI)
recruit human evaluators to gather feedback on the believability (Xu et al., 2023a) is a recently proposed open platform that
of the simulation (Park et al., 2023). However, developing integrates embodied agents with the digital twins of cities,
benchmarks for quantitative and qualitative evaluation of LLM- offering the opportunity to evaluate urban problems with large-
driven agent-based simulation remains a largely open problem scale urban agent simulations and solve them with multi-
and a promising future research direction. On the other hand, disciplinary approaches. Despite this early attempt at urban
LLM-driven simulation might serve as a realistic environment system simulation, the development of an open platform for
thatprovideshigh-qualityfeedbacktotrainotherAImodels.For LLM-drivenABSisanemergingareathatcallsformoreresearch
example, previous studies explore the simulations of social attention.
segregation (Sert et al., 2020), competing firms (Osoba et al.,
2020),competitivegames(Parketal.,2019),andcoordinationof
different stakeholders (Bone and Dragićević, 2010). Such Robustness of LLM-driven agent-based simulation. The
simulations can serve as a benchmark to train and evaluate the robustness problems of LLM agent simulation can be classified
reinforcement learning models. A recent study by Wu et al. into two main scenarios, adversarial attack and out-of-
(2023)proposesaPETframeworktoleverageLLM-drivenagents distribution generalization, which fundamentally stem from the
as a supervisor of low-level trainable models, which simplifies robustnessissuesoftheunderlyinglanguagemodels(Wangetal.,
challenging control tasks by translating task descriptions into 2023a).Thecurrentmethodologiestoaddressout-of-distribution
high-level sub-tasks and then tracking the accomplishment of generalization problems primarily resort to classic machine
these sub-tasks. Additionally, more research efforts should be learning techniques (Shen et al., 2021), such as unsupervised
dedicated to the benchmarks of AI for social good (Cowls et al., representation learning, supervised model learning, and optimi-
2021). zation methods. As for adversarial attacks, various defense tech-
niques have been proposed in recent studies. For example,
researchers propose to certify LLM safety with an erase-and-
Open platform. Building open platforms for LLM-driven agents checkfilterthatdetectsadversarialprompts(Kumaretal.,2023).
will play a pivotal role in this emerging research area that could Besides moving target defense, Chen et al. (2023a) aim to select
substantiallyreducethebarriersofLLM-drivenABSandfostera safe answers from the responses generated by different LLMs to
vibrant community, echoing the calls for open-source software enhancetheLLMsystem’srobustnessagainstjailbreakingattacks.
(Weber,2004)and open science NationalAcademies of Sciences Moreover, extensive benchmarks of adversarial prompts are for-
et al. (2018). The recent advance of LLMs has led to the public mulated to evaluate LLM (Zhu et al., 2023b).
release of several powerful pre-trained language models. For AsfortheLLMagents,theyoftenhavetool-usecapability(Qin
example, Bidirectional Encoder Representations from Transfor- et al., 2023) and engage in human interactive scenarios, such as
mers (BERT) has been publicly released and gained huge influ- theconflictsimulationactorthathelpsuserslearnconflictresolve
ence in the past few years (Devlin et al., 2019). GPT2, a through rehearsal (Shaikh et al., 2024), which makes the
predecessor to the current ChatGPT family, was released by robustness of LLM agents have far-reaching consequences.
OpenAI with limited model sizes for open-source use (Radford Furthermore,inthecontextofmulti-agentsimulation,adversarial
et al., 2019). Additionally, Meta AI recently released a collection attacks might propagate among agents (Tian et al., 2023). More
ofopenfoundationandfine-tunedchatmodelsnamedLLaMa 2 importantly,recentworksshowthesimulationsofmultipleLLM
(Touvron et al., 2023), which range in scale from 7 billion to 70 agents show human-like collective behaviors (Aher et al., 2023;
billion parameters. These open-source LLMs demonstrate pow- Zhou et al., 2024b), such as social conformity and homophily,
erful capabilities in various natural language tasks, which can be which could be exploited by adversaries as weaknesses in the
furtheradaptedforspecificdownstreamtaskswithefficient fine- societiesof LLMagents.ImprovingtherobustnessofLLMagent
tuningmethodssuchasLow-RankAdaptation(LoRA)(Huetal., simulation atboth theindividual and collective levels isan open
2021). problem.
TherecentproliferationofLLM-drivenagentshasalsoresulted ThestabilityofLLMagentscanalsoberegardedasonekindof
in several open-source platforms. Voyager is an example open- robustness.EveniftheLLMagentsarefedthesameprompts,the
source framework of embodied LLM-driven agents, capable of agent may generate odd responses due to the limitation of large
continuously acquiring diverse skills and making novel discov- language models, especially for smaller LLMs. This leads to a
eries in Minecraft without human intervention (Xi et al., 2023). concern about the reproducibility of large language model-
Researchers also develop open-source frameworks for real-world empowered agent-based modeling and simulation. Three poten-
task-solving agents, such as XAgent Team (2024) that are tial solutions exist based on the requirements of agent-based
designed as a general-purpose framework of automatic task- modelingandsimulationandthecharacteristicsoflargelanguage
solving. Moreover, ModelScope-Agent (Li et al., 2023b) is models.Thefirstsolutionistodevelopspecializedlargelanguage
18 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
models tailored for simulation, improving environment consis- reshaped the paradigm of agent-based modeling and simulation,
tency. The second solution may be a combination of large and providing a new perspective for constructing intelligent human-
smallerLLMs,reachinganacceptabletrade-offbetweencostand like agents rather than those driven by simple rules or limited-
robustness.Thethirdpromisingfuturedirectioncouldbeabetter intelligenceneuralmodels.Inthispaper,wetakethefirststepto
agent mechanism, with more powerful reflection, memory, etc. provide a survey of the agent-based modeling and simulation
with large language models. We systematically analyze why the
LLM agents are required for agent-based modeling and simula-
Ethical risks in LLM agents. The advances of LLM unleash the
tion and how to address the critical challenges. Afterward, we
unprecedented capability of human-like text generation and rea-
extensivelysummarizetheexistingworksinfourdomains:cyber,
soning,raisingconcernsaboutpotentialethicalrisksofmisuse,such
physical,social,andhybrid,carefullydescribinghowtodesignthe
as jailbreaking (Zhuo et al., 2023). For example, recent studies
simulation environment, how to construct the large language
highlight the risks of generating malicious network payloads that
model-empoweredagents,andwhattoobserveandachievebased
could jeopardize cyber security at scale (Charan et al., 2023), and
on agent-based simulation. Lastly, given the unresolved limita-
emphasize the concerns of accuracy, recency, coherence, and trans-
tions of existing works and this new and fast-growing area, we
parency of LLM agents inmedical practice (Thirunavukarasu etal.,
2023). To gauge LLM agents’ susceptibility to social bias and ste- discuss the open problems and point out the important research
reotype, researchers use semantic illusions and cognitive reflection directions, which we hope can inspire future research.
tests (Hagendorff et al., 2023), typically administered to human
subjects, to quantify LLM’s tendency to produce intuitive yet erro-
neousresponses.TheyfindearlymodelsfromtheGPTfamilyhave Data availability
All data generated or analyzed during this study are included in
an increasing tendency to generate intuitive errors as their size
this manuscript.
increases,whileChatGPT-3.5and4haveapatternshiftthatradically
eliminates these errors and achieves superhuman accuracy. They
speculate the pattern shift is driven by the employment of reinfor- Received: 19 December2023; Accepted: 12August 2024;
cement learning from human feedback, a sophisticated technique
only deployed in ChatGPT-3.5 and later models. These findings
highlighttheimportanceof embeddinghumanpreferencesintothe
language models, instead of solely relying on web corpus. In the References
context of LLM-driven agent simulations, researchers find when AcerbiA,StubbersfieldJM(2023)Largelanguagemodelsshowhuman-likecontent
certainpersonasareassignedtoChatGPTitwillgenerateoutputwith biases in transmission chain experiments. Proc Natl Acad Sci USA
120:e2313790120
6× toxicity, engaging in discriminatory stereotypes, harmful con-
AherGV,ArriagaRI,KalaiAT(2023)Usinglargelanguagemodelstosimulate
versation,andoffensivelanguage(Deshpandeetal.,2023).Besides,a
multiple humans and replicate human subject studies. In: International
recent work by Acerbi and Stubbersfield (2023) shows LLM agent ConferenceonMachineLearning(PMLR).pp337–371
exhibits human-like biases that prefer gender-stereotype-consistent, Akata Eetal.(2023)Playingrepeatedgameswithlargelanguagemodels.arXiv
negative, and biologically counter-intuitive content. More impor- preprintarXiv:2305.16867
tantly, such biases could be further amplified in the transmission AlluhaybiB,AlrahhalMS,AlzhraniA,ThayananthanV(2019)Asurvey:agent-
basedsoftwaretechnologyundertheeyesofcybersecurity,securitycontrols,
chaininmulti-agentsettings.Theexperimentalresultsfromprevious attacksandchallengesIntJAdvComputSciAppl10:211–230
studiesemphasizetheimportanceofethicalconsiderationsinLLM- Aminabadi RY et al. (2022) Deepspeed-inference: enabling efficient inference of
drivenagent-basedsimulations,especiallyagainstthebackdropofthe transformer models at unprecedented scale. In: SC22: international con-
rapidproliferationofLLMagentsinvariousdomains. ferenceforhighperformancecomputing,networking,storageandanalysis.
IEEE,pp1–15,https://ieeexplore.ieee.org/abstract/document/10046087
Extensive efforts have been made to mitigate the potential
AnL(2012)Modelinghumandecisionsincoupledhumanandnaturalsystems:
ethicalrisksofLLMagents.Aprimaryfocusistofundamentally reviewofagent-basedmodels.EcolModel229:25–36
align language models with human values (Yao et al., 2023a; Yi AntoniniG, Bierlaire M,Weber M(2006) Discrete choice modelsofpedestrian
et al., 2023). A recent survey classifies the alignment goals into walkingbehavior.TranspResPartB:Methodol40:667–687
threedistinctlevels,i.e.,humaninstructions,humanpreferences, Argyle LP et al. (2023) Out of one, many: using language models to simulate
humansamples.PoliticalAnal31:337–351
and human values. Besides, Moral Foundation theory is invoked
to benchmark mainstream language models’ alignment with the Arora D, Singh HG et al. (2023) Have LLMs advanced enough? A challenging
problemsolvingbenchmarkforlargelanguagemodels.The2023Conference
foundationalethicalvaluesofcare,fairness,loyalty,authority,and onEmpiricalMethodsinNaturalLanguageProcessing,https://openreview.
sanctity (Yi et al., 2023). Researchers also find LLM agents are net/forum?id=YHWXlESeS8
susceptible to flattened caricatures when specific personas are ArsanjaniJJ,HelbichM,deNoronhaVazE(2013)Spatiotemporalsimulationof
urbangrowthpatternsusingagent-basedmodeling:thecaseofTehran.Cities
assignedtothem(Chengetal.,2023a).TheCoMPosTframework
32:33–42
isproposedtoevaluatethemultidimensionalityofsimulatedLLM
Arthur WB (1991) Designing economic agents that act like human agents: a
agents and provide a measure for caricature in LLM agent behavioralapproachtoboundedrationality.AmEconRev81:353–359
simulations.TheyfindeventheagentsdrivenbythelatestGPT-4 BakhtinA,BrownN,DinanE,FarinaG,FlahertyC,FriedD,GoffA,GrayJ,HuH,
in the simulation of political and marginalized demographic
JacobAPMetaFundamentalAIResearchDiplomacyTeam(FAIR)†(2022)
Human-levelplayinthegameofdiplomacybycombininglanguagemodels
groups. Finally, to fundamentally address the potential ethical
withstrategicreasoningScience378:1067–1074
risks, many scholars advocate enhancing the interpretability of
BanischS,LimaR,AraújoT(2012)Agentbasedmodelsandopiniondynamicsas
LLMagents,questioningthefalsifiabilityofanymoralprinciples Markovchains.SocNetw34:549–561
learned by black box LLM agents (Vijayaraghavan and Badea, BarbosaJ,LeitãoP(2011)Simulationofmulti-agentmanufacturingsystemsusing
2024). Therefore, they propose to benchmark and continuously agent-based modelling platforms. In: Proceedings of the 2011 9th IEEE
improve LLM agents’ interpretability (Zhao et al., 2024). internationalconferenceonindustrialinformatics.IEEE,pp477–482
Barnes S, Golden B, Price S (2013) Applications of agent-based modeling and
simulationtohealthcareoperationsmanagement.In:PriceCC&Gendreau
Conclusion M (eds) Handbook of healthcare operations management: methods and
applications.Springer,pp.45–74.https://www.springer.com/series/6161
Agent-based modeling and simulation is one of the most
BarrosJX(2004)UrbangrowthinLatinAmericancities-exploringurbandynamics
important methods to model complex systems in various through agent-based simulation. University of London, University College
domains. The recent advances in large language models have London,UK
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3 19

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
BasavatiaS,RatnakarS,MurugesanK(2023)Complexworld:alargelanguagemodel- ChengZ,KasaiJ,YuT(2023b)Batchprompting:efficientinferencewithlargelanguage
based interactive fiction learning environment for text-based reinforcement modelAPIs.In:Proceedingsofthe2023ConferenceonEmpiricalMethodsin
learningagents.InternationalJointConferenceonArtificialIntelligence2023 NaturalLanguageProcessing.AssociationforComputationalLinguistics,Singa-
WorkshoponKnowledge-BasedCompositionalGeneralization pore,pp792–810,https://doi.org/10.18653/v1/2023.emnlp-industry.74
Batty M (2001) Agent-based pedestrian modeling. Environ plan B: Plan Des ChowdheryAetal.(2023)Palm:scalinglanguagemodelingwithpathways.JMach
28:321–326 LearnRes24:1–113
BauerK,LiebichL,HinzO,KosfeldM(2023)DecodingGPT’sHidden‘Ration- CipiE,CicoB(2011)Simulationofanagentbasedsystembehaviorinadynamic
ality’ofCooperation.SAFEWorkingPaperNo.401,https://doi.org/10.2139/ andunpredictedenvironment.Simulation1:172–176
ssrn.4576036 ConteR,PaolucciM(2014)Onagent-basedmodelingandcomputationalsocial
BeheshtiR,JalalpourM,GlassTA(2017)Comparingmethodsoftargetingobesity science.FrontPsychol5:668
interventionsinpopulations:anagent-basedsimulation.SSM-PopulHealth CowlsJ,TsamadosA,TaddeoM,FloridiL(2021)Adefinition,benchmarkand
3:211–218 databaseofAIforsocialgoodinitiatives.NatMachIntell3:111–115
Bellegarda JR (2004) Statistical language model adaptation: review and perspec- CuiC,MaY,CaoX,YeW,WangZ(2024)Driveasyouspeak:enablinghuman-
tives.SpeechCommun42:93–108 like interaction with large language models in autonomous vehicles. In:
BeltranRS,TestaJW,BurnsJM(2017)Anagent-basedbioenergetics modelfor ProceedingsoftheIEEE/CVFWinterConferenceonApplicationsofCom-
predictingimpactsofenvironmentalchangeonatopmarinepredator,the puterVision,pp902–909
Weddellseal.EcolModel351:36–50 deSouzaF,VerbasO,AuldJ(2019)Mesoscopictrafficflowmodelforagent-based
BinzM,SchulzE(2023)UsingcognitivepsychologytounderstandGPT-3.Proc simulation.ProcediaComputSci151:858–863
NatlAcadSciUSA120:e2218523120 deZarzàI,deCurtòJ,RoigG,ManzoniP,CalafateCT(2023)Emergentcoop-
BohlmannJD,CalantoneRJ,ZhaoM(2010)Theeffectsofmarketnetworkhet- erationandstrategyadaptationinmulti-agentsystems:anextendedcoevo-
erogeneity on innovation diffusion: an agent-based modeling approach. J lutionarytheorywithLLMs.Electronics12:2722
ProductInnovManag27:741–760 DeepMindG(2023)IntroducingGemini:ourlargestandmostcapableAImodel.
Boiko DA, MacKnight R, Gomes G (2023) Emergent autonomous scientific https://blog.google/technology/ai/google-gemini-ai.Accessed7Dec2023
research capabilities of large language models. arXiv preprint DeguchiH(2011)Economicsasanagent-based complexsystem:toward agent-
arXiv:2304.05332 basedsocialsystemssciences.SpringerScience&BusinessMedia
BoneC,DragićevićS(2010)Simulationandvalidationofareinforcementlearning DengXetal.(2024)Mind2web:towardsageneralistagentfortheweb.AdvNeural
agent-based model for multi-stakeholder forest management. Comput InfProcessSyst,36
EnvironUrbanSyst34:162–174 DeshpandeA,MurahariV,RajpurohitT,KalyanA,NarasimhanK(2023)Toxicityin
Bran AM, Cox S,WhiteAD, Schwaller P (2023)Chemcrow: augmenting large- chatgpt:analyzingpersona-assignedlanguagemodels.FindingsoftheAssociation
languagemodelswithchemistrytools.arXivpreprintarXiv:2304.05376 for Computational Linguistics: EMNLP 2023, Association for Computational
Brown T et al. (2020) Language models are few-shot learners. Adv Neural Inf Linguistics,pp1236–1270.https://doi.org/10.18653/v1/2023.findings-emnlp.88
ProcessSyst33:1877–1901 Devlin J, Chang M-W, Lee K, Toutanova K (2019) Bert: pre-training of deep
BrownDG,RobinsonDT(2006)Effectsofheterogeneityinresidentialpreferences bidirectional transformers for language understanding. In: Proceedings of
onanagent-basedmodelofurbansprawl.EcolSoc11 naacL-HLTVol1.pp2
BybeeL(2023) SurveyinggenerativeAI’seconomic expectations. arXivpreprint Dong Q et al. (2022) A survey for in-context learning. arXiv preprint
arXiv:2305.02823 arXiv:2301.00234(2022)
Cabrera E, Taboada M, Iglesias ML, Epelde F, Luque E (2011) Optimization of DuboisYetal.(2024)Alpacafarm:asimulationframeworkformethodsthatlearn
healthcare emergency departments by agent-based simulation. Procedia fromhumanfeedback.AdvNeuralInfProcessSyst,36
ComputSci4:1880–1889 DwivediVPetal.(2023)Benchmarkinggraphneuralnetworks.JMachLearnRes
CaiJetal.(2024)Languageevolutionforevadingsocialmediaregulationviallm- 24:1–48
basedmulti-agentsimulation.IEEEWCCI,https://arxiv.org/abs/2405.02858 ElliottE,KielLD(2002)Exploringcooperationandcompetitionusingagent-based
Caldarelli G et al. (2023) The role of complexity for digital twins of cities. Nat modeling.ProcNatlAcadSciUSA99:7193–7194
ComputSci3:374–381 El-SayedAM,ScarboroughP,SeemannL,GaleaS(2012)Socialnetworkanalysisand
CartaTetal.(2023)Groundinglargelanguagemodelsininteractiveenvironments agent-basedmodelinginsocialepidemiology.EpidemiolPerspectInnov9:1–9
with online reinforcement learning. International Conference on Machine ElsenbroichC,GilbertN,ElsenbroichC,GilbertN(2014)Agent-basedmodelling.
Learning.PMLR,pp3676–3713 ModellingNorms,pp65–84
ChanC-Metal.(2024)ChatEval:towardsbetterLLM-basedevaluatorsthrough Elyoseph Z, Hadar-Shoval D, Asraf K, Lvovsky M (2023) Chatgpt outperforms
multi-agent debate. The Twelfth International Conference on Learning humansinemotionalawarenessevaluations.FrontPsychol14:1199058
Representations.https://openreview.net/forum?id=FQepisCUWu Faria-eCastroM,LeiboviciF(2023)Artificialintelligenceandinflationforecasts.
ChangYetal.(2024)Asurveyonevaluationoflargelanguagemodels.ACMTrans TechnicalReport,https://research.stlouisfed.org/wp/more/2023-015
IntellSystTechnol15:1–45 FengL,LiB,PodobnikB,PreisT,StanleyHE(2012)Linkingagent-basedmodels
CharanP,ChunduriH,AnandPM,ShuklaSK(2023)Fromtexttomitretech- and stochastic models of financial markets. Proc Natl Acad Sci USA
niques:exploringthemalicioususeoflargelanguagemodelsforgenerating 109:8388–8393
cyberattackpayloads.arXivpreprintarXiv:2305.15336 FengJetal.(2020)Learningtosimulatehumanmobility.In:Proceedingsofthe
ChenL(2012)Agent-basedmodelinginurbanandarchitecturalresearch:abrief 26thACMSIGKDDinternationalconferenceonknowledgediscovery&data
literaturereview.FrontArchitRes1:166–177 mining.pp3426–3433
Chen B et al.(2023b)Open-vocabulary queryable scene representations for real Franceschelli G, Musolesi M (2023) On the creativity of large language models.
world planning. In 2023 IEEE International Conference on Robotics and arXivpreprintarXiv:2304.00008
Automation(ICRA).IEEE,pp11509–11522 FuDetal.(2024)Drivelikeahuman:rethinkingautonomousdrivingwithlarge
ChenB,PaliwalA,YanQ(2023a)Jailbreaker injail:movingtargetdefense for language models. In: Proceedings of the IEEE/CVF Winter Conference on
large language models. In: Proceedings of the 10th ACM Workshop on ApplicationsofComputerVision,pp910–919
MovingTargetDefense.pp29–32 Gao C et al. (2023) S3: social-network simulation system with large language
ChenJ,YuanS,YeR,MajumderBP,RichardsonK(2023c)Putyourmoneywhere model-empoweredagents.arXivpreprintarXiv:2307.14984
yourmouthis:evaluatingstrategicplanningandexecutionofLLMagentsin Gatti DD, Desiderio S,GaffeoE, CirilloP, GallegatiM (2011) Macroeconomics
anauctionarena.arXivpreprintarXiv:2310.05746 fromtheBottom-up,Vol1.SpringerScience&BusinessMedia
Chen W et al. (2024) Agentverse: Facilitating multi-agent collaboration and GaubeV,RemeschA(2013)Impactofurbanplanningonhousehold’sresidential
exploringemergentbehaviorsinagents.TheTwelfthInternationalConference decisions:anagent-basedsimulationmodelforVienna.EnvironModelSoftw
onLearningRepresentations.https://openreview.net/forum?id=EHg5GDnyq1 45:92–103
ChenY,LiuTX,ShanY,ZhongS(2023e)Theemergenceofeconomicrationality GeerlingW,MateerGD,WootenJ,DamodaranN(2023)Chatgpthasacedthetest
of GPT. In: Proceedings of the National Academy of Sciences. Vol 120. ofunderstandingincollegeeconomics:nowwhat?AmEcon.68.https://doi.
NationalAcadSciences,pe2316205120 org/10.1177/05694345231169654
ChengJ,ChinP(2024)SocioDojo:BuildingLifelongAnalyticalAgentswithReal- GilbertN(2004a)Agent-basedsocialsimulation:dealingwithcomplexity.Com-
world Text and Time Series. The Twelfth International Conference on plexSystNetwExcell9:1–14
LearningRepresentations.https://openreview.net/forum?id=s9z0HzWJJp Gilbert N, Terna P (2000) How to build and use agent-based models in social
Cheng M, Piccardi T, Yang D (2023a) Compost: characterizing and evaluating science.MindSoc1:57–72
caricatureinLLMsimulations.In:Proceedingsofthe2023Conferenceon GilbertN(2007b)Computationalsocialscience:agent-basedsocialsimulation.In:
Empirical Methods in Natural Language Processing. Association for Com- PhanD&AmblardF(eds)Agent-basedmodellingandsimulation.Bardwell,
putationalLinguistics,pp10853–10875 Oxford,pp115–134
20 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
Gilbert N, Troitzsch K (2005) Simulation for the social scientist. McGraw-Hill KimJ,LeeB(2023)AI-augmentedsurveys:leveraginglargelanguagemodelsfor
Education,UK opinion prediction in nationally representative surveys. arXiv preprint
Guo F (2023) GPT agents in game theory experiments. arXiv preprint arXiv:2305.09620
arXiv:2305.05516 Kountouriotis V, Thomopoulos SC, Papelis Y (2014) An agent-based crowd
Guo J et al. (2023) Suspicion-agent: Playing imperfect information games with behaviourmodelforrealtimecrowdbehavioursimulation.PatternRecognit
theoryofmindawareGPT-4.arXivpreprintarXiv:2309.17277 Lett44:30–38
GuoSetal.(2024)Largelanguagemodelsasrationalplayersincompetitive Kovač G, Portelas R, Dominey PF, Oudeyer P-Y (2023) The social AI school:
economicsgames.In:Proceedingsofthe12thinternationalconferenceon Insights from developmental psychology towards artificial socio-cultural
learning representations. https://openreview.net/forum?id= agents.arXivpreprintarXiv:2307.07871
NMPLBbjYFq Kumar A, Agarwal C, Srinivas S, Feizi S, Lakkaraju H (2023)
GurIetal.(2024)Areal-worldwebagentwithplanning,longcontextunder- Certifying llm safety against adversarial prompting. arXiv preprint
standing, and program synthesis. The Twelfth International Conference arXiv:2309.02705
on Learning Representations. https://openreview.net/forum?id= LanX,GaoC,JinD,LiY(2024)Stancedetectionwithcollaborativerole-infused
9JQtrumvg8 llm-basedagents.In:ProceedingsoftheinternationalAAAIconferenceon
GurneeW,TegmarkM(2024)Languagemodelsrepresent space andtime.The webandsocialmedia,AAAI,Vol18.pp891–903
Twelfth International Conference on Learning Representations. https:// LengnickM(2013)Agent-basedmacroeconomics:abaselinemodel.JEconBehav
openreview.net/forum?id=jE8xbmvFin Organ86:102–120
GuyotP,HonidenS(2006)Agent-basedparticipatorysimulations:mergingmulti- LeombruniR,RichiardiM(2005)Whyareeconomistsscepticalaboutagent-based
agentsystemsandrole-playinggames.JArtifSocSocSimul9 simulations?PhysicaA355:103–109
HagendorffT,FabiS,KosinskiM(2023)Human-likeintuitivebehaviorandrea- Li K, Liang H, Kou G, Dong Y (2020) Opinion dynamics model based on the
soningbiasesemergedinlargelanguagemodelsbutdisappearedinChatGPT. cognitivedissonance:Anagent-basedsimulation.InfFusion56:1–14
NatComputSci,3:833–838 LiBetal.(2023a)Seed-bench:benchmarkingmultimodalLLMswithgenerative
HämäläinenP,TavastM,KunnariA(2023)Evaluatinglargelanguagemodelsin comprehension.arXivpreprintarXiv:2307.16125
generatingsyntheticHCIresearchdata:acasestudy.In:Proceedingsofthe Li C et al. (2023b) Modelscope-agent: building your customizable agent
2023CHIConferenceonHumanFactorsinComputingSystems.ACM,pp system with open-source large language models. In: Proceedings
1–19 of the 2023 Conference on Empirical Methods in Natural Language
HamillL,GilbertN(2015)Agent-basedmodellingineconomics.JohnWiley&Sons Processing: System Demonstrations. Association for Computational
Han X, Wu Z, Xiao C (2023) “Guinea pig trials” utilizing GPT: a novel smart Linguistics,Singapore,pp566–578https://aclanthology.org/2023.emnlp-
agent-basedmodelingapproachforstudyingfirmcompetitionandcollusion. demo.51
arXivpreprintarXiv:2308.10974 LiCetal.(2023c)Quantifyingtheimpactoflargelanguagemodelsoncollective
HauserMD,ChomskyN,FitchWT(2002)Thefacultyoflanguage:whatisit,who opiniondynamics.arXivpreprintarXiv:2308.03313
hasit,andhowdiditevolve?science298:1569–1579 Li G, Hammoud HAAK, Itani H, Khizbullin D, Ghanem B (2023d) Camel:
HeckbertS,BaynesT,ReesonA(2010)Agent-basedmodelinginecologicaleco- Communicative agents for “mind” exploration of large language model
nomics.AnnNYAcadSciUSA1185:39–53 society.AdvNeuralInfProcessSyst36:51991–52008
HelbingD,MolnarP(1995)Socialforcemodelforpedestriandynamics.PhysRev LiJetal.(2024a)Agenthospital:asimulacrumofhospitalwithevolvablemedical
E51:4282 agents.arXivpreprintarXiv:2405.02957
Helbing D (2012) Social self-organization: agent-based simulations and experi- Li N, Gao C, Li M, Li Y, Liao Q (2024b) Econagent: large language model-
mentstostudyemergentsocialbehavior.Springer empoweredagentsforsimulatingmacroeconomicactivities.In:ACL
Hernández-OralloJ,Martínez-PlumedF,SchmidU,SiebersM,DoweDL(2016) LiS,YangJ,ZhaoK(2023e)Areyouinamasquerade?exploringthebehaviorand
Computermodelssolvingintelligencetestproblems:progressandimplica- impactoflargelanguagemodeldrivensocialbotsinonlinesocialnetworks.
tions.ArtifIntell230:74–107 arXivpreprintarXiv:2307.10337
HongSetal.(2024)MetaGPT:metaprogrammingformulti-agentcollaborative LiX,LiY,LiuL,BingL,JotyS(2022)IsGPT-3apsychopath?evaluatinglarge
framework.TheTwelfthInternationalConferenceonLearningRepresenta- language models from a psychological perspective. arXiv preprint
tions.https://openreview.net/forum?id=VtmBAGCN7o arXiv:2212.10529
HortonJJ(2023)Largelanguagemodelsassimulatedeconomicagents:whatcan Liang T et al. (2023) Encouraging divergent thinking in large language models
welearnfromhomosilicus?TechnicalReport,NationalBureauofEconomic throughmulti-agentdebate.arXivpreprintarXiv:2305.19118
Research Lin L-J (1992) Self-improving reactive agents based on reinforcement learning,
Hoshen D, Werman M (2017) IQ of neural networks. arXiv preprint planningandteaching.MachLearn8:293–321
arXiv:1710.01692 LinJetal.(2023)Agentsims:anopen-sourcesandboxforlargelanguagemodel
Hu W et al. (2020) Open graph benchmark: datasets for machine learning on evaluation.arXivpreprintarXiv:2308.04026
graphs.AdvNeuralInfProcessSyst33:22118–22133 LippeM et al. (2019) Using agent-based modelling to simulate social-ecological
HuEJetal.(2022)Lora:low-rankadaptationoflargelanguagemodels.Interna- systemsacrossscales.GeoInformatica23:269–298
tional Conference on Learning Representations. https://openreview.net/ LiuRetal.(2024a)Trainingsociallyalignedlanguagemodelsinsimulatedhuman
forum?id=nZeVKeeFYf9 society.TheTwelfthInternationalConferenceonLearningRepresentations.
Hua W et al. (2023) War and peace (waragent): Large language https://openreview.net/forum?id=NddKiWtdUm
model-based multi-agent simulation of world wars. arXiv preprint LiuXetal.(2024b)Agentbench:evaluatingLLMsasagents.TheTwelfthInter-
arXiv:2311.17227 national Conference on Learning Representations. https://openreview.net/
HuangQ,VoraJ,LiangP,LeskovecJ(2023)Benchmarkinglargelanguagemodels forum?id=zAdUB0aCTQ
asAIresearchagents.arXivpreprintarXiv:2310.03302 LiuYetal.(2019)HowwelldomachinesperformonIQtests:acomparisonstudy
JangJetal.(2023)Personalizedsoups:personalizedlargelanguagemodelalign- onalarge-scaledataset.In:IJCAI.pp6110–6116
mentviapost-hocparametermerging.arXivpreprintarXiv:2310.11564 LopezPAetal.(2018)Microscopictrafficsimulationusingsumo.In:201821st
Jiang LYetal.(2023)Healthsystem-scalelanguagemodelsareall-purpose pre- internationalconferenceonintelligenttransportationsystems(ITSC).IEEE,
dictionengines.Nature619:357–362 pp2575–2582
Jin Y et al. (2023) Surrealdriver: designing generative driver agent simulation Lu J et al. (2023) Self: language-driven self-evolution for large language model.
frameworkinurbancontextsbasedonlargelanguagemodel.arXivpreprint arXivpreprintarXiv:2310.00533
arXiv:2309.13193 LuoLetal.(2008)Agent-basedhumanbehaviormodelingforcrowdsimulation.
JinxinSetal.(2023)CGMI:configurablegeneralmulti-agentinteractionframe- ComputAnimatVirtualWorlds19:271–281
work.arXivpreprintarXiv:2308.12503 Ma Y, Zhenjiang S, Kawakami M (2013) Agent-based simulation of residential
Kahneman D (2017) Thinking, fast and slow[J]. Farrar, Straus and Giroux, promotingpolicyeffectsondowntownrevitalization.JArtifSocSocSimul
2011 16:2
Kahneman D, Knetsch JL, Thaler R (1986) Fairness as a constraint on profit Macal CM, North MJ (2005) Tutorial on agent-based modeling and
seeking:entitlementsinthemarket.AmEconRev76.4:728–741 simulation.In:ProceedingsoftheWinterSimulationConference.IEEE,
Kavak H, Padilla JJ, Lynch CJ, Diallo SY (2018) Big data, agents, and machine 14pp
learning: towards a data-driven agent-based modeling approach. In: Pro- MacyMW,WillerR(2002)Fromfactorstoactors:computationalsociologyand
ceedingsoftheannualsimulationsymposium.pp1–12 agent-basedmodeling.AnnuRevSociol28:143–166
KimD,YunT-S,MoonI-C,BaeJW(2021)Automaticcalibrationofdynamicand MadeyG,GaoY,FreehV,TynanR,HoffmanC(2003)Agent-basedmodelingand
heterogeneous parameters in agent-based models. Autonomous Agents simulationofcollaborativesocialnetworks.In:ProceedingsAmericasCon-
Multi-AgentSyst35:46 ferenceonInformationSystems(AMCIS)pp1836–1842
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3 21

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
Maggi E, Vallino E (2016) Understanding urban mobility and the impact of RouchierJ(2017)Agent-basedsimulationasausefultoolforthestudyofmarkets.
public policies: the role of the agent-based models. Res Transp Econ In:Simulatingsocialcomplexity:ahandbook.pp671–704
55:50–59 RussakovskyOetal(2015)Imagenetlargescalevisualrecognitionchallenge.IntJ
MańdziukJ,ŻychowskiA(2019)Deepiq:ahuman-inspiredAIsystemforsolving ComputVis115:211–252
IQ test problems. In: 2019 International Joint Conference on Neural Net- Samanidou E, Zschischang E, Stauffer D, Lux T (2007) Agent-based models of
works(IJCNN).IEEE,pp1–8 financialmarkets.RepProgPhys70:409
ManviRetal.(2024)Geollm:extractinggeospatialknowledgefromlargelanguage Samuelson W, Zeckhauser R (1988) Status quo bias in decision making. J Risk
models.TheTwelfthInternationalConferenceonLearningRepresentations. Uncertain1:7–59
https://openreview.net/forum?id=TqL2xBwXP3 SchickTetal.(2024)Toolformer:languagemodelscanteachthemselvestouse
MaoSetal.(2023)Alympics:languageagentsmeetgametheory.arXivpreprint tools.AdvNeuralInfProcessSyst36:68539–68551
arXiv:2311.03220 Schieritz N, Grobler A (2003) Emergent structures in supply chains-a study
Mastio M, Zargayouna M, Scemama G, Rana O (2018) Distributed agent-based integratingagent-basedandsystemdynamicsmodeling.In:Proceedingsof
trafficsimulations.IEEEIntellTranspSystMag10:145–156 the 36th Annual Hawaii International Conference on System Sciences.
McLaneAJ,Semeniuk C,McDermidGJ,Marceau DJ(2011)Theroleofagent- IEEE,9
based models in wildlife ecology and management. Ecol Model SchwitzgebelE,SchwitzgebelD,StrasserA(2024)Creatingalargelanguagemodel
222:1544–1556 ofaphilosopher.MindLang39:237–259
MelisG,DyerC,BlunsomP(2017)Onthestateoftheartofevaluationinneural SertE,Bar-YamY,MoralesAJ(2020)Segregationdynamicswithreinforcement
languagemodels.arXivpreprintarXiv:1707.05589 learningandagentbasedmodeling.SciRep10:11771
Mueller M, Pyka A (2016) Economic behaviour and agent-based modelling. In: ShahD,OsińskiB,LevineSetal.(2023a)Lm-nav:roboticnavigationwithlarge
Frantz R, Chen S-H, Dopfer K, Heukelom F, Mousavi S, (eds) Routledge pre-trainedmodelsoflanguage,vision,andaction.In:Conferenceonrobot
handbookofbehavioraleconomics.Routledge,pp405–415 learning.PMLR,pp492–504
MukobiGetal.(2023)Welfarediplomacy:benchmarkinglanguagemodelcoop- ShahD,SridharA,BhorkarA,HiroseN,LevineS(2023b)Gnm:ageneralnavi-
eration.arXivpreprintarXiv:2310.08901 gationmodeltodriveanyrobot.In:2023IEEEInternationalConferenceon
Nascimento N, Alencar P, Cowan D (2023) Self-adaptive large language model RoboticsandAutomation(ICRA).IEEE,pp7226–7233
(LLM)-based multiagent systems. 2023 IEEE International Conference on ShaikhO,ChaiV,GelfandMJ,YangD,BernsteinMS(2024)Rehearsal:simulating
AutonomicComputingandSelf-OrganizingSystemsCompanion(ACSOS- conflicttoteachconflictresolution.In:ProceedingsoftheCHIConference
C),IEEE,pp104–109 onHumanFactorsinComputingSystems.pp1–20
NationalAcademiesofSciencesEMedicineetal.(2018)Opensciencebydesign: Shanahan M, McDonell K, Reynolds L (2023) Role play with large language
realizingavisionfor21stcenturyresearch models.Nature623:493–498
OpenAI(2022)IntroducingChatGPT.https://openai.com/blog/chatgpt.Accessed Shen Z et al. (2021) Towards out-of-distribution generalization: a survey. arXiv
1Dec2023 preprintarXiv:2108.13624
Osoba OA, Vardavas R, Grana J, Zutshi R, Jaycocks A (2020) Policy-focused Sheng Y et al. (2023) High-throughput generative inference of large language
agent-based modeling using RL behavioral models. arXiv preprint models with a single gpu. International Conference on Machine Learning,
arXiv:2006.05048 PMLR,pp31094–31116
PapachristouM,YuanY(2024)Networkformationanddynamicsamongmulti- ShinnN,CassanoF,GopinathA,NarasimhanKR,YaoS(2023)Reflexion:language
LLMs.arXivpreprintarXiv:2402.10659 agents with verbal reinforcement learning. In: 37th conference on Neural
Park YJ, Cho YS, Kim SB (2019) Multi-agent reinforcement learning with InformationProcessingSystems.https://doi.org/10.48550/arXiv.2303.11366
approximate model learning for competitive games. PLoS ONE ShridharMetal.(2021)Alfworld:aligningtextandembodiedenvironmentsfor
14:e0222215 interactivelearning.InternationalConferenceonLearningRepresentations.
Park J, Min B, Ma X, Kim J (2023) Choicemates: supporting unfamiliar online https://openreview.net/forum?id=0IOX0YcCdTn
decision-makingwithmulti-agentconversationalinteractions.arXivpreprint SilvaPCetal.(2020)Covid-abs:anagent-basedmodelofCOVID-19epidemicto
arXiv:2310.01331 simulate health and economic effects of social distancing interventions.
Park JS et al. (2022) Social simulacra: Creating populated prototypes for social ChaosSolitonsFractals139:110088
computingsystems.In:Proceedingsofthe35thannualACMsymposiumon SilvermanBG,HanrahanN,BharathyG,GordonK,JohnsonD(2015)Asystems
userinterfacesoftwareandtechnology.ACM,pp1–18 approach to healthcare: agent-based modeling, community mental health,
ParkJSetal.(2023)Generativeagents:interactivesimulacraofhumanbehavior. andpopulationwell-being.ArtifIntellMed63:61–71
In: Proceedings of the 36th annual ACM symposium on user interface SimonHA(1997)Modelsofboundedrationality:empiricallygroundedeconomic
softwareandtechnology.ACM,pp1–22 reason,Vol3.MITPress
ParvL,DeakyB,NasuleaMD,OanceaG(2019)Agent-basedsimulationofvalue Singh M et al. (2023) Mind meets machine: unravelling GPT-4’s cognitive psy-
flowinanindustrialproductionprocess.Processes7:82 chology.BenchCouncilTransBenchmarks,StandEval3:100139
PereiraA,DuarteP,ReisLP(2004)Agent-basedsimulationofecologicalmodels. SinghalKetal.(2023)Largelanguagemodelsencodeclinicalknowledge.Nature
In:Proceedings5thWorkshoponAgent-BasedSimulation 620:172–180
PerezL,DragicevicS(2009)Anagent-basedapproachformodelingdynamicsof Song CH et al. (2023) LLM-planner: few-shot grounded planning forembodied
contagiousdiseasespread.IntJHealthGeogr8:1–17 agentswithlargelanguagemodels.In:ProceedingsoftheIEEE/CVFinter-
PertoldiC,Topping C(2004)Impact assessment predictedbymeans ofgenetic nationalconferenceoncomputervision.pp2998–3009
agent-basedmodeling.CritRevToxicol34:487–498 SunH,ZhuangY,KongL,DaiB,ZhangC(2024)Adaplanner:adaptiveplanningfrom
Phelps S, Russell YI (2023) Investigating emergent goal-like behaviour in large feedbackwithlanguagemodels.AdvNeuralInfProcessSyst36:58202–58245
language models using experimental economics. arXiv preprint SurowieckiJ(2005)Thewisdomofcrowds.Anchor
arXiv:2305.07970 Suzuki R, Arita T (2024) An evolutionary model of personality traits related to
Platas-López A, Guerra-Hernández A, Quiroz-Castellanos M, Cruz-Ramirez N cooperativebehaviorusingalargelanguagemodel.SciRep14:5989
(2023) A survey on agent-based modelling assisted by machine learning. TaoriRetal.(2023)Stanfordalpaca:aninstruction-followingllamamodel.https://
ExpertSyste13325.https://doi.org/10.1111/exsy.13325 github.com/tatsu-lab/stanford_alpaca
PlosserCI,SchwertGW(1979)PotentialGNP:itsmeasurementandsignificance:a Team A (2022) Autogpt: the heart of the open-source agent ecosystem. https://
dissentingopinion.In:Carnegie-Rochesterconferenceseriesonpublicpolicy, github.com/Significant-Gravitas/AutoGPT.Accessed1Oct2023
Elsevier,Vol10,pp179–186 TeamX(2024)Xagent:anautonomousagentforcomplextasksolving|XAgent
Puranam P, Stieglitz N, Osman M, Pillutla MM (2015) Modelling bounded (xagent.net)
rationality in organizations: progress and prospects. Acad Manag Ann Terna P et al.(1998)Simulation tools for social scientists: building agent based
9:337–392 modelswithswarm.JArtifSocSocSimul1:1–12
QianCetal.(2024)Communicativeagentsforsoftwaredevelopment.In:Proceedings Thirunavukarasu AJ et al. (2023) Large language models in medicine. Nat Med
ofthe62ndAnnualMeetingoftheAssociationforComputationalLinguistics 29:1930–1940
(Vol 1: Long Papers) Association for Computational Linguistics, Bangkok, TianY,YangX,ZhangJ,DongY,SuH(2023)Evilgeniuses:delvingintothesafety
Thailand,pp15174–15186.https://aclanthology.org/2024.acl-long.810 ofLLM-basedagents.arXivpreprintarXiv:2311.11855
Qin Y et al. (2023) Tool learning with foundation models. arXiv preprint TomaselloM(2010)Originsofhumancommunication.MITPress
arXiv:2304.08354 TouvronHetal.(2023)Llama:openandefficient foundationlanguagemodels.
Radford A et al. (2019) Language models are unsupervised multitask learners. arXivpreprintarXiv:2302.13971
OpenAIBlog1:9 Valmeekam K, Olmo A, Sreedharan S, Kambhampati S (2022) Large language
Rolón M, Martínez E (2012) Agent-based modeling and simulation of an auto- modelsstillcan’tplan(abenchmarkforLLMsonplanningandreasoning
nomicmanufacturingexecutionsystem.ComputInd63:53–78 aboutchange).arXivpreprintarXiv:2206.10498
22 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
Van Dinther C (2008) Agent-based simulation for research in economics. In: ZhangHetal.(2024b)Buildingcooperativeembodiedagentsmodularlywithlarge
Handbookoninformationtechnologyinfinance.Springer,pp421–442 language models. The Twelfth International Conference on Learning
VijayaraghavanA,BadeaC(2024)Minimumlevelsofinterpretabilityforartificial Representations.https://openreview.net/forum?id=EnXJfQqy0K
moralagents.AIandEthics,Springer,pp1–17 Zhang J, Xu X, Deng S (2023c) Exploring collaboration mechanisms for LLM
WallF(2016)Agent-basedmodelinginmanagerialscience:anillustrativesurvey agents:asocialpsychologyview.arXivpreprintarXiv:2310.02124
andstudy.RevManagSci10:135–193 ZhangTetal.(2024c) Benchmarking large languagemodelsfornewssummar-
Wang A et al. (2019) Glue: a multi-task benchmark and analysis platform for ization.TransAssocComputLinguist12:39–57
natural language understanding. 7th International Conference on Learning ZhaoHetal.(2024)Explainabilityforlargelanguagemodels:asurvey.ACMTrans
Representations,ICLR2019 intellSystTechnol15:1–38
WangGetal.(2024a)Voyager:anopen-endedembodied agentwithlarge lan- ZhaoQetal.(2023b)Competeai:understandingthecompetitionbehaviorsinlarge
guagemodels.TransactionsonMachineLearningResearch,pp2835–8856 languagemodel-basedagents.arXivpreprintarXiv:2310.17512
https://openreview.net/forum?id=ehfRiF0R3a Zhao WX et al. (2023c) A survey of large language models. arXiv preprint
WangJetal.(2023a)OntherobustnessofChatGPT:anadversarialandout-of- arXiv:2303.18223
distributionperspective.arXivpreprintarXiv:2302.12095 Zheng S, Trott A, Srinivasa S, Parkes DC, Socher R (2022) The AI economist:
WangLetal.(2023b)Recagent:anovelsimulationparadigmforrecommender Taxationpolicydesignviatwo-leveldeepmultiagentreinforcementlearning.
systems.arXivpreprintarXiv:2306.02552 SciAdv8:eabk2607
WangLetal.(2024b)Asurveyonlargelanguagemodelbasedautonomousagents. Zhou S et al. (2024a) WebArena: A realistic Web Environment for Building
FrontComputSci18:186345 Autonomous Agents. The Twelfth International Conference on Learning
Wang L, Ahn K, Kim C, Ha C (2018) Agent-based models in financial market Representations.https://openreview.net/forum?id=oKn9c6ytLx
studies.JPhysConfSer1039,012022 Zhou X et al. (2024b) Sotopia: interactive evaluation for social intelligence in
WangZ,ChiuYY,ChiuYC(2023c)Humanoidagents:platformforsimulating languageagents.TheTwelfthInternationalConferenceonLearningRepre-
human-like generative agents. Proceedings of the 2023 Conference on sentations.https://openreview.net/forum?id=mM7VurbA4r
EmpiricalMethodsinNaturalLanguageProcessing:SystemDemonstrations, ZhuD,ChenJ,ShenX,LiX,ElhoseinyM(2024)Minigpt-4:enhancingvision-
pp167–176 languageunderstandingwithadvancedlargelanguagemodels.TheTwelfth
WangZetal.(2023d)Unleashingcognitivesynergyinlargelanguagemodels:A International Conference on Learning Representations. https://openreview.
task-solving agent through multi-persona self-collaboration. arXiv preprint net/forum?id=1tZbq88f27
arXiv:2307.05300 Zhu K et al. (2023b) Promptbench: towards evaluating the robustness of large
WeberS(2004)Thesuccessofopensource.HarvardUniversityPress languagemodelsonadversarialprompts.arXivpreprintarXiv:2306.04528
WeiJetal.(2022)Chain-of-thoughtpromptingelicitsreasoninginlargelanguage Zhu Xetal.(2023c) Ghostintheminecraft: generallycapableagents foropen-
models.AdvNeuralInfProcessSyst35:24824–24837 world environments via large language models with text-based knowledge
WeissMetal.(2024)Rethinkingthebuyer’sinspectionparadoxininformationmarkets andmemory.arXivpreprintarXiv:2305.17144
with languageagents. In: Proceedings ofthe 12th international conferenceon ZhuX,LiJ,LiuY,MaC,WangW(2023d)Asurveyonmodelcompressionfor
learningrepresentations.https://openreview.net/forum?id=6werMQy1uz largelanguagemodels.arXivpreprintarXiv:2308.07633
WidenerMJ,MetcalfSS,Bar-YamY(2013)Agent-basedmodelingofpoliciesto ZhugeMet al.(2023) Mindstorms innatural language-based societies ofmind.
improve urban food access for low-income populations. Appl Geogr arXivpreprintarXiv:2305.17066
40:1–10 Zhuo TY, Huang Y, Chen C, Xing Z (2023) Exploring ai ethics of ChatGPT: a
WilliamsR,HosseinichimehN,MajumdarA,GhaffarzadeganN(2023)Epidemic diagnosticanalysis.arXivpreprintarXiv:2301.12867
modelingwithgenerativeagents.arXivpreprintarXiv:2307.04986 Zou H, Zhao Q, Bariah L, Bennis M, Debbah M (2023) Wireless multi-agent
WolframS(1984)Cellularautomataasmodelsofcomplexity.Nature311:419–424 generative AI: from connected intelligence to collective intelligence. arXiv
WooldridgeM,JenningsNR(1995)Intelligentagents:theoryandpractice.Knowl preprintarXiv:2307.02757)
EngRev10:115–152
WuYetal.(2023)Plan,eliminate,andtrack–languagemodelsaregoodteachers
Acknowledgements
forembodiedagents.arXivpreprintarXiv:2305.02412
XiZetal.(2023)Theriseandpotentialoflargelanguagemodelbasedagents:A ThisworkissupportedbytheNationalNaturalScienceFoundationofChinaunder
survey.arXivpreprintarXiv:2309.07864 62272262andU23B2030.
XieC,ZouD(2024)Ahuman-likereasoningframeworkformulti-phasesplanning
taskwithlargelanguagemodels.arXivpreprintarXiv:2405.18208 Author contributions
XieQ,HanW,LaiY,PengM,HuangJ(2023)TheWallStreetNeophyte:azero-
C.Gaocontributedtothestructureofthissurveypaper,searchingandorganizingall
shotanalysisofchatgptovermultimodalstockmovementpredictionchal-
relevantrelatedpapers,aswellasallthecontentthroughoutthewholepaper.X.Lan
lenges.arXivpreprintarXiv:2304.05351
partlycontributedtothecontentrelevanttothesocialdomain;N.LiandZ.Zhoupartly
XuF,ZhangJ,GaoC,FengJ,LiY(2023a)Urbangenerativeintelligence(UGI):
contributedtothecontentrelevanttotheeconomicdomain;Y.YuanandJ.Dingpartly
a foundational platform for embodied agent and future city.
contributedtothecontentrelevanttoagent-basedmodelingandthephysicaldomain.F.
arXiv:2312.11813
Xupartlycontributedtothesectiononperspectivesofthisresearchdirection.Y.Li
XuYetal.(2023b)Exploringlargelanguagemodelsforcommunicationgames:an
contributedtothewholestructure,motivation,andtaxonomy.Allauthorscontributedto
empiricalstudyonwerewolf.arXivpreprintarXiv:2309.04658
thewritingofthismanuscript.
YaoSetal.(2024)Treeofthoughts:deliberateproblemsolvingwithlargelanguage
models.AdvNeuralInfProcessSyst36:11809–11822
YaoJ,YiX,WangX,WangJ,XieX(2023a)Frominstructionstointrinsichuman Competing interests
values—a survey of alignment goals for big models. arXiv preprint Theauthorsdeclarenocompetinginterests.
arXiv:2308.12014
YiX,YaoJ,WangX,XieX(2023)Unpackingtheethicalvaluealignmentinbig Ethical approval
models.arXivpreprintarXiv:2310.17551
Thisarticledoesnotcontainanystudieswithhumanparticipantsperformedbyanyof
Yoheinakajima(2023)Babyagi.https://github.com/yoheinakajima/babyagi.Acces-
theauthors.
sed1Oct2023
Yoon S-E, He Z, Echterhoff JM, McAuley J (2024) Evaluating large language
modelsasgenerativeusersimulatorsforconversationalrecommendation.In: Informed consent
Proceedings of the 2024 conference of the north american chapter of the Thisarticledoesnotcontainanystudieswithhumanparticipantsperformedbyanyof
associationforcomputationallinguistics:humanlanguagetechnologies(Vol theauthors.
1:LongPapers),AssociationforComputationalLinguistics,pp1490–1504.
https://doi.org/10.18653/v1/2024.naacl-long.83
Additional information
Zeng A et al. (2023) Glm-130b: an open bilingual pre-trained model. In: Pro-
ceedingsofthe11thinternationalconferenceonlearningrepresentations CorrespondenceandrequestsformaterialsshouldbeaddressedtoYongLi.
ZhangB,DeAngelisDL(2020)Anoverviewofagent-basedmodelsinplantbiology
andecology.AnnBot126:539–557 Reprintsandpermissioninformationisavailableathttp://www.nature.com/reprints
ZhangAetal.(2024a)Ongenerativeagentsinrecommendation.In:Proceedingsof
the47thinternationalACMSIGIRconferenceonresearchanddevelopment
Publisher’snoteSpringerNatureremainsneutralwithregardtojurisdictionalclaimsin
inInformationRetrieval,pp1807–1817 publishedmapsandinstitutionalaffiliations.
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3 23

REVIEW ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-024-03611-3
Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreative
Commonslicence,andindicateifchangesweremade.Theimagesorotherthirdparty
materialinthisarticleareincludedinthearticle’sCreativeCommonslicence,unless
indicatedotherwiseinacreditlinetothematerial.Ifmaterialisnotincludedinthe
article’sCreativeCommonslicenceandyourintendeduseisnotpermittedbystatutory
regulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfrom
thecopyrightholder.Toviewacopyofthislicence,visithttp://creativecommons.org/
licenses/by/4.0/.
©TheAuthor(s)2024
24 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2024) 11:1259 |https://doi.org/10.1057/s41599-024-03611-3
