---
title: "Introduction"
source_pdf: "02_citysim_agents\\08_Urban_Generative_Intelligence_Li2023.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-06-21T17:32:25+00:00
page_count: 31
status: ok
text_char_count: 132536
quality_flags: []
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\02_citysim_agents\08_Urban_Generative_Intelligence_Li2023.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-06-21T17:32:25+00:00
- Page count: 31
- Status: ok
- Text chars: 132536
- Quality flags: none

## Metadata

- Title: Introduction
- Author: unknown
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

Urban environments, characterized by their complex, multi-layered networks encompassing physical, social, economic, and environmental dimensions, face significant challenges in the face of rapid urbanization. These challenges, ranging from traffic congestion and pollution to social inequality, call for advanced technological interventions. Recent developments in big data, artificial intelligence, urban computing, and digital twins have laid the groundwork for sophisticated city modeling and simulation. However, a gap persists between these technological capabilities and their practical implementation in addressing urban challenges in an systemic-intelligent way. This paper proposes Urban Generative Intelligence (UGI), a novel foundational platform integrating Large Language Models (LLMs) into urban systems to foster a new paradigm of urban intelligence. UGI leverages CityGPT, a foundation model trained on city-specific multi-source data, to create embodied agents for various urban tasks. These agents, operating within a textual urban environment emulated by city simulator and urban knowledge graph, interact through a natural language interface, offering an open platform for diverse intelligent and embodied agent development. This platform not only addresses specific urban issues but also simulates complex urban systems, providing a multidisciplinary approach to understand and manage urban complexity. This work signifies a transformative step in city science and urban intelligence, harnessing the power of LLMs to unravel and address the intricate dynamics of urban systems. The code repository with demonstrations will soon be released here https://github.com/tsinghua-fib-lab/UGI.

## Outline

- Introduction (page 1)
- Related Work (page 3)
  - Complex Urban System (page 3)
  - Urban Computing and Intelligence (page 3)
  - Digital Twin City (page 4)
  - Large Language Models and Agents (page 4)
  - Agent-based Modeling and Simulation (page 5)
  - Metaverse (page 5)
- Architecture (page 6)
- Open Digital Infrastructure (page 7)
  - Urban Modeling (page 7)
  - Data Streams (page 8)
    - Databases (page 8)
    - Knowledge Graphs (page 10)
  - City Simulator (page 10)
  - Open Interfaces (page 11)
    - Application Programming Interface (page 11)
    - Natural Language Interface (page 12)
- Foundation Model and Agent (page 12)
  - CityGPT: Large Language Model for Urban Generative Intelligence (page 12)
  - General Framework for Generative City Agents (page 15)
    - Simulation Agent: Generating Individual and Collective Behaviour (page 15)
    - Decision Making Agent: Task Solving and Personal Assistance (page 16)
- Evaluation (page 17)
- Enabled Urban Applications (page 19)
  - Transportation System (page 19)
  - Business Intelligence (page 19)
  - Urban Economy System (page 20)
  - Urban Society (page 20)
- Discussion (page 21)
  - Dive into Complicated Urban Issues (page 21)
  - Scale Up to Large City (page 21)
  - Openness of the Environment (page 22)
  - Developer Community (page 22)
- Conclusion (page 22)

## Markdown Content

URBAN GENERATIVE INTELLIGENCE (UGI): A FOUNDATIONAL
PLATFORM FOR AGENTS IN EMBODIED CITY ENVIRONMENT
A PREPRINT
Fengli Xu∗ Jun Zhang∗ Chen Gao∗ Jie Feng Yong Li
Tsinghua University, Beijing, China
{fenglixu, chgao96, liyong07}@tsinghua.edu.cn
December 20, 2023
ABSTRACT
Urban environments, characterized by their complex, multi-layered networks encompassing physical,
social, economic, and environmental dimensions, face significant challenges in the face of rapid
urbanization. These challenges, ranging from traffic congestion and pollution to social inequality,
call for advanced technological interventions. Recent developments in big data, artificial intelligence,
urban computing, and digital twins have laid the groundwork for sophisticated city modeling and
simulation. However, a gap persists between these technological capabilities and their practical
implementation in addressing urban challenges in an systemic-intelligent way. This paper proposes
Urban Generative Intelligence (UGI), a novel foundational platform integrating Large Language
Models (LLMs) into urban systems to foster a new paradigm of urban intelligence. UGI leverages
CityGPT, a foundation model trained on city-specific multi-source data, to create embodied agents
for various urban tasks. These agents, operating within a textual urban environment emulated by
city simulator and urban knowledge graph, interact through a natural language interface, offering
an open platform for diverse intelligent and embodied agent development. This platform not only
addresses specific urban issues but also simulates complex urban systems, providing a multidisciplinary approach to understand and manage urban complexity. This work signifies a transformative
step in city science and urban intelligence, harnessing the power of LLMs to unravel and address the
intricate dynamics of urban systems. The code repository with demonstrations will soon be released
here https://github.com/tsinghua-fib-lab/UGI.
1 Introduction
Urban are complex systems with dynamic and multi-layered networks encompassing physical elements (buildings,
roads, infrastructure), social structures (population distribution, organizations, culture), economic activities (industry,
services, commerce), and environmental factors (natural resources, ecosystems, climate change) [10, 15, 17]. This
intricate interplay creates uncertainty and dynamism, reflecting the complex interactions between human activities and
the urban environment [17]. Each individual, community, and organization within these systems is interconnected,
influencing the city’s overall characters and functionality [99]. The primary challenge in urban complex systems is
balancing economic growth, social welfare, and environmental sustainability amid rapid urbanization, and it faces
critical challenges including traffic congestion, environmental pollution, resource scarcity, and infrastructure strain, all
exacerbated by rapid urbanization [184]. Besides, social inequality and housing issues further impact residents’ quality
of life. The growing threats of climate change, such as extreme weather and rising sea levels, add to these challenges,
highlighting the urgent need for solutions. Addressing these prominent urban issues is essential to ensure sustainable,
equitable urban development and maintain the vitality of cities in a rapidly evolving global context [2].
In order to address above problems, the recent technological evolution began with big data, which provided rich and
variety urban information [178]. The complexity of this data necessitated the development of artificial intelligence (AI)
for effective description, prediction and management [186]. This synergy led to urban computing[184], which applies
∗The first three authors contribute to this work equally.
3202
ceD
91
]IA.sc[
1v31811.2132:viXra

Urban Gener
AI to big data for urban problem-solving. Building on thi
creating virtual models of cities using real-time data and
data collection (big data), to data analysis (AI), to applicat
modeling (digital twins and city simulations). Each stage
for tackling urban complexities. However, despite these ad
address the complexity of urban issues lies in the gap bet
This shortfall implies that while these technologies are in
intricate and systemic challenges cities face, necessitatin
achieve more intelligent system-wide urban solutions.
The advent of artificial general intelligence, particularl
intelligence presents a transformative opportunity in add
emergent intelligence capabilities, mimicking human c
human-like intelligence of LLMs can significantly contr
and context-aware insights. They can identify patterns, se
nuanced understanding of the complex social and econo
supports smart decision-making in urban planning and p
systems holds great promise for finding comprehensive
push the urban technology to the next stage of urban inte
In this paper, we propose Urban Generative Intelligence
evolution, and application of generative intelligence in urb
platform is built on top of an open digital infrastructure th
simulator engine [176]. This infrastructure is capable of
urban data and providing embodied feedback to intellig
virtual environments [41]. We design a standard languag
facilitating the easy plugin of language models and the d
foundation model for urban problems, we pre-train a LL
city-specific data, including general text corpus, including
and so on. Using CityGPT as a generative intelligence c
agents for various urban tasks, such as planning transpor
life and socioeconomic interactions [50]. Moreover, this
agents, fostering the emergence of diverse intelligent age
the realistic embodied feedback provided by digital infr
empowered agents are able to learn from the environmen
intelligence to deal with complicate urban tasks. Lever
platform can help solve urban issues, support a wide r
These components collectively form the Foundation Plat
generative intelligence in urban space.
The contributions of this paper can be summarized as the
• We are the first to propose an open digital infras
provides realistic feedback of urban experienc
knowledge graph and city simulator to provide
urban space.
• We design and implement a foundation model fo
from general foundation model to incorporate urb
fine-tuned to induce urban intelligence ability w
• We propose a general framework for generativ
CityGPT in various urban tasks. We also propos
physical mobility, economy activity, and social i
personal assistance of location recommendation
• We introduce an evaluation framework to valida
agents, quantifying urban generative intelligence
planing and decision making. It provides a stand

e Intelligence A PREPRINT
igital twins [11] and city simulations [176, 175] emerged,
nalysis. These technologies represent a progression from
(urban computing), and finally to advanced simulation and
lds upon the last, offering increasingly sophisticated tools
cements, the ability of these technologies to systematically
n technological capabilities and practical implementation.
uable tools, they cannot yet comprehend and address the
urther advancements in AI and computational models to
rge language models (LLMs), as a form of human-like
sing urban challenges [48, 151, 25]. LLMs demonstrate
itive process to analyze and reason vast datasets. The
e to the intelligence of urban systems by providing deep
ments, and trends within urban discourse, offering a more
dynamics at play in urban environments, which further
y formulation. Thus, the integration of LLMs into urban
tions to the multifaceted challenges in cities, which will
ence.
GI), a foundational platform that fosters the emergence,
pace and fuels the transition to smart future city. The UGI
consists of the UrbanKG knowledge graph [95] and a city
ulating realistic urban interactions based on multi-source
agents, setting it apart from existing sandboxes [112] or
terface to expose the access to this digital infrastructure,
lopment of generative and embodied agents. To create a
called CityGPT on general text corpus and high-quality
main-specific urban knowledge, task-solving process data
, we propose a general framework of creating embodied
on system, assisting policy-making, and simulating urban
eral framework can be easily adapted to build customized
upporting various aspects of urban intelligence. Through
ucture and the interactions with other agents, the LLMevelop their own understanding, and further evolve their
ng the CityGPT and various embodied agents, the UGI
e of urban applications, and explore new urban forms.
m of UGI, facilitating the emergence and advancement of
lowing aspects.
cture for embodied urban environment simulation, which
ia a natural language interface. It leverages UrbanKG
tual feedback that can enable generative intelligence in
y problems, called CityGPT. It is continuously pre-trained
knowledge extracted from text corpus, and then supervised
domain-specific data.
ty agents, which releases the generative intelligence of
veral successful design cases for: a) simulation agents of
action in city; b) decision making agents that can serve as
d schedule planning.
he performance of foundation model and generative city
the levels of mastering knowledge, simple reasoning, and
and reference for the development of urban intelligence.

Urban Gener
2 Related Work
2.1 Complex Urban System
Cities have long been viewed as a complex system of inte
attentions are devoted to review the universal patterns of v
morphology shape [9]. Specifically, previous works find c
common practice in urban planing, but is a symbolic fea
devoted to reveal the scaling laws in urban space [18]. Th
innovation and crimes, and sub-linear growth of infrastru
theoretical framework to explain these scaling laws from
in the increased interaction frequency in the compact u
research attention is drawn to the complex challenges face
inequality, especially as the detailed data of social fabric
understanding the complex and concerning phenomena
gaps [22], and prevalence of slums [23].
Motivated by these empirical studies, extensive previous
urban system from a bottom up perspective. For examp
model to reproduce fractal urban morphology as the pro
percolation model on spatial lattice to explain urban mor
growth and fractal urban morphology can naturally emerg
of complex urban challenges, agent-based model has been
in urban space [127]. Researchers have also developed bo
socioeconomic inequality as the provision of universal ba
However, previous studies mainly use agents guided by
provides unique opportunity to design generative agents
been proved feasible in simulating virtue village [112] a
and bias encoded in large language model, these gene
social phenomena. For example, recent studies show l
bias in transmission chain [1], and can reproduce the ty
conformity [190]. However, these agents are all simulate
are sophisticated enough to interact with complex urban
expose language model-driven agents to the rich inform
simulators.
2.2 Urban Computing and Intelligence
As a core concept of urban intelligence, urban computi
energy consumption, and air pollution with the help of c
focused on the spatial-temporal data analytics and mana
planing [187, 166], transportation [167, 97, 147] and en
and fusion technics in different fields, these works ach
application of deep learning methods, urban computing a
the urban space, e.g., traffic prediction [142, 61, 86] and
transportation, epidemic modeling and environment. ST
into the crowd flow prediction problem to better model the
to utilize the power of recurrent neural network and atten
mobility. ASTGCN [61] applies graph neural network to
between road segments.
While these data analytics and prediction methods of ur
from different aspects, they are limited for tackling man
decision making ability. Thus, recent works further exte
behavior simulation [47, 168, 170] and decision making [1
behaviors and is applied in the epidemic modeling. Fur
to simulate the human activities with Maslow’s need. In
enable the intelligent traffic light control. Zheng et. al. [1
generate spatial plans for urban communities with the he

e Intelligence A PREPRINT
nected humans, things and space [10]. Extensive research
us statistics in complex urban system, such as city size and
exhibit typical fractal morphology [12], contradicting the
of complex system. Besides, a large body of literature is
find universal patterns of super-linear growth of economy,
e investment as city size increases. Previous works build
interaction mechanisms of urban agents [16], which root
n space of large cities [128]. In recent years, increasing
y modern cities, ranging from climate change to economic
ncreasingly available [164]. Researchers are dedicated to
experienced segregation [108], widening socioeconomic
rks aim to design agent-based model to explain complex
esearchers propose to use diffusion limited aggregation
s of physical particles [13]. A later study uses correlated
logy [101]. Recent study finds the scaling laws of urban
om agent-based model of human mobility [156]. In terms
eraged to reproduce and explain the ubiquitous segregation
m up model to explain the emergence of varying levels of
urban service change [22].
ple rules. The recent advance of large language models
much more sophisticated intelligence. Such agents have
ompany [66]. By leveraging the human like intelligence
ve agents have the potential to explain more complex
e language model-driven agents exhibit similar content
al social processes like wisdom of crowd [3] and social
simple and virtual environment. It is still unclear if they
ironment. Hence, it is an important research direction to
n collected from urban systems or generated by realistic
184] is to solve the urban issues like traffic congestion,
puter science algorithms. In the early years, the research
ent [90, 185, 189, 188, 167] and its application on urban
nment [118, 37]. With careful designed data processing
d pretty good results. In the recent five years, with the
ved significant process on various prediction problems in
bility prediction [177, 46, 162] which are widely used in
Net [177] first introduces the convolution neural network
tial correlation between regions. DeepMove [46] proposes
n mechanism to capture the periodic pattern of individual
raffic network to capture the spatial-temporal correlations
computing helped us better understand the urban space
al-life issues which require counterfactual inference and
he concept of urban intelligence into the new fields like
149, 186]. MoveSim [47] simulates the human movement
, SAND [170] develops a knowledge-driven framework
ilight [150] first utilizes deep reinforcement learning to
propose an artificial intelligence urban-planning model to
f graph neural network and deep reinforcement learning.

Urban Gener
However, despite the above advancements, these methods
and fail to solve the complex urban system issues in pract
human-like cognitive abilities provide us new opportun
urban intelligence will enable the more real-world applica
prediction and decision making in the urban space from a
2.3 Digital Twin City
Digital Twin City (DTC) refers to the emulation of a city
and optimization of urban systems through the use of datacity research, finding applications in urban planning, traffic
Recent years have witnessed substantial progress in vari
development pace of DTC. On one hand, advancements in
of data from multiple sources, including aerospace satelli
terminals [28], smart wearable devices [126], industrial an
devices [119]. A recent focus has been on crowd-sensin
crowd, exhibiting distinctive characteristics [30, 60], foc
large-scale crowds to establish reliable and semantic-ric
On the other hand, the analysis and optimization of urb
complex spatio-temporal data of DTC present challeng
AI [53] has significantly improved data processing effici
or knowledge graphs [19, 165] can yield more informed
comprehension of domain intricacies. Deep reinforceme
data through trial-and-error learning with agents [169] for
navigation [92].
It is important to acknowledge that the digital twin city tec
and problems. Firstly, there is a strong need to enhance th
credibility and realism. Secondly, the processing and co
updates and evolution, and how to process complex inst
more accessible to policymakers and urban planners, is cr
proposed LLM-empowered fundamental city platform aim
of urban problem solving.
2.4 Large Language Models and Agents
Large language models [182] such as ChatGPT [110], L
advances of artificial intelligence, which learns from the
generating language texts. Since language is the most bas
like language ability endows large language models with
Therefore, large language models are considered a promi
To achieve urban generative intelligence, it is required t
for urban scenarios. It is worth mentioning that there a
models. Deng et al. [36] proposed to fine-tune Llama-7B
research papers in the geoscience field. The fine-tuned
concepts, and support the basic QA tasks. Similar soluti
corpus include GeoLM [91] and GeoLLM [103]. Zhang
the user query in traffic-related tools. GeoGPT [181] to
language model a bridge in connecting the practitioners w
in only understanding some city-related concepts, without
scenarios, i.e., urban generative intelligence, limiting the
construct the foundational model, simulation environmen
Despite the astonishing performance in various tasks of na
be used as an agent [145, 154], which can act and behave
purposes. That is, the agent can be a digital twin in variou
other humans in social networks in Metaverse applicatio
language ability to more dimensions of models, from env
the environment can be represented as textual descriptions

e Intelligence A PREPRINT
ally simplify the assumptions of specific real-life problems
Recently, the rapid development of LLMs with incredible
to solve these issues. The integration of LLMs into the
methods and frameworks for pattern discovery, dynamics
stematic view.
digital environment, enabling real-time sensing, analysis,
en models [191]. DTC stands as a significant trend in smart
nagement, environmental protection and disaster response.
information technologies, significantly accelerating the
nsor devices have facilitated the collection of vast amounts
[161], aircraft and drones [106], smartphones and mobile
ousehold monitoring equipment [76], and wireless sensing
methods that leverage distributed smart devices within a
ng on integrating and analyzing digital footprints left by
epresentations of group behavior across spatial domains.
data heavily rely on machine learning algorithms. The
for forecasting and decision-making, and the advent of
y. Advancements like differentiable decision trees [131]
contextually sound outcomes through utilizing inherent
earning provides a direct path to model spatio-temporal
an decision-making tasks including traffic signal [102] or
logy to solve urban problems still faces several challenges
pability to process the multi-source urban data to improve
utation of large-scale data pose challenges for real-time
ions and provide human-friendly outputs, making DTC
l for scenario testing and decision-making processes. Our
o solve these problems to upgrades DTC into the practice
MA [139], Alphca [136], and GLM [172], are the recent
ge corpus, with emergent abilities in understanding and
ol for humans interacting with the world [62], the humanh-level capacity, including reasoning and decision-making.
g approach for artificial general intelligence [26].
ndow the existing large language with essential abilities
ome recent attempts to build city-related large language
th Geoscience Academic Knowledge Graph and relevant
del obtained the ability to understand these professional
with fine-tuned large language models with geo-related
al. [179] utilize the large language model to help process
advantage of the ability in tool usage, considering large
GIS software. Despite these efforts, they are still limiting
y considering what abilities a real human has in the urban
works’ application. In this paper, we pay attention to the
nd embodied agents for the urban context.
l language processing, the large language models can also
e a real human, serving as a virtual agent for personalized
enarios, such as representing a real human to interact with
[84]. One of the most critical challenges is to extend the
nment perception and action execution. On the one hand,
2], which can be naturally perceived by the large language

Urban Generative Intelligence A PREPRINT
models; on the other hand, recent advances build the multi-modal ability by the alignment among different modals [67],
including textual, visual, etc. As for action execution, it is widely acknowledged that the agent can leverage various
tools well, which extend the action space to language into real-world actions, supporting various interactions between
the large language model agent and the environment. That is, it endows the large language models with the ability of
embodied perception, reasoning, and action, which is also known as embodied agent [143, 40, 107, 174]. Specifically,
these works approach the embodied tasks in the real-world environment, such as navigating and controlling robots, and
take advantage of the reasoning and decision-making abilities of large language models. Moreover, to ensure the agents
can take embodied actions, these works connect the textual output with a tool or another action-execution module.
However, these works only consider simple environments such as a room or virtual game environment. In addition,
the tasks are relatively simple. Unlike these works, in this paper, we present a far more complex problem in building
fundamentally embodied agents in the city environment, and the agents can have almost all kinds of embodied behaviors
of real humankind.
2.5 Agent-based Modeling and Simulation
Agent-based modeling and simulation is an important and powerful approach to modeling complex systems, such as the
city system, understanding, analyzing, explaining, and even predicting the dynamics of the systems [14]. Generally
speaking, simulation can be divided into macrosimulation and microsimulation. Macrosimulation refers to simulating
the system from an aggregate or high level, which focuses on the trends and behaviors within a system or a population
without focusing on the individual-level characteristics. Specifically, macrosimulation may deploy several equations
to describe how the critical variables in the system affect each other. However, it is quite challenging to formulate
the equations since real-world systems are always very complex, which motivates the microsimulation, which is also
known as agent-based simulation. On the other hand, microsimulation focuses on individual entities within a system.
In general, agent-based simulation aims to model the behavior of individual components or agents to understand their
interactions and how they collectively contribute to the overall system. For example, the famous Cellular Automata [153]
is comprised of discrete cells, each following a set of rules based on their neighboring cells. The simulations based on
setting rules for each individual can often showcase emergent behaviors, where complex patterns arise from simple
interactions between individual components. Since it is general, agent-based simulation is extensively used in various
fields, such as biology [5], ecology [104], sociology [100], etc., to model systems where individual entities influence
collective behavior.
The early attempts at agent-based simulation [24, 138] used some simple rules or formulas to guide how each individual
behaved when faced with environmental change, which is easy to implement but makes it hard to capture complex
individual behaviors accurately. After that, with the development of neural networks, for those individual decision
factors that the simple rules cannot well capture, the neural networks are leveraged [44, 52]. Furthermore, recent works
tend to deploy reinforcement learning-based agents [183], for which each individual’s goal in the simulation is to
maximize the reward.
However, these agents are limited since they are not autonomous and require human-defined goals or rules, which
motivates the large language model-driven agents. In this paper, we present the UGI system, one of the main goals of
which is to deploy large language model-based agents to simulate the complex dynamics of the city and further support
various applications such as decision-making, etc. The large language model agents are the up-to-date solution for
agent-based modeling and simulation for the complex city system.
2.6 Metaverse
The Metaverse epitomizes a collective virtual shared space, formed from the fusion of physical and digital realities,
typically accessed through immersive technologies such as virtual reality (VR) [84] and augmented reality (AR) [109].
This digital universe offers an array of interactive experiences, social interactions, and economic activities, presenting
various research questions and avenues for advancement. At its philosophical core, the Metaverse is entwined with
the reality-virtuality continuum [31]. On the reality aspect, it draws inspiration from the concept of the digital twin,
meticulously replicating the physical world within the virtual sphere. This comprehensive replication captures physical
objects, interactions, and dynamics, integrating reality into the digital landscape [45]. Conversely, the virtuality facet
of the Metaverse revolves around generating entities within the digital realm [20]. These virtual creations, born from
human imagination and innovation, surpass physical limitations and showcase human ingenuity in the virtual domain.
Recent strides in Artificial Intelligence Generated Content (AIGC) notably advance this field [98, 116].
Therefore, it comes as no surprise that research in this field is currently focused on two primary directions, one
of which involves progress related to devices closely associated with the physical world. In contemporary times,
5

Urban Gener
Figure 1: Architecture of the foundation
Metaverse applications vary based on execution devices,
and headsets [56, 105, 6]. These devices play a pivotal rol
have delved into innovative solutions aiming to prevent in
eye-tracking technologies [122], synchronize visual-moto
These efforts aim to create more accessible and intuitiv
advancements in Artificial Intelligence (AI) have revo
models [123] and applications like Midjourney, demons
creators within the Metaverse can now generate diverse t
prompts. Similarly, generative works in film [43], aud
ultimately providing users with experiences derived from
to architectural designs [68], landscape design [7], and ur
metaverse city.
Looking ahead, the Metaverse is poised for rapid evoluti
and creating an equitably accessible City Metaverse. F
between diverse virtual environments, integration of AI fo
systems [34], and exploration of blockchain [80] for de
platform aims to build the future city metaverse with emb
3 Architecture
Here, we present the overall architecture of our proposed
The key idea is to assemble the powerful city simulator, u
as an open digital infrastructure. More importantly, the i
enables the easy plugin of large language models and ge
conveniently access the computation power and factual

e Intelligence A PREPRINT
atform for urban generative intelligence.
h as tabletops, projectors, hand-held touchscreen devices,
creating seamless, immersive experiences. Recent studies
mation overload [38], alleviate cognitive load [77], explore
sponses [79], or leverage natural finger positioning [158].
ntry points into the physical world. In the virtual realm,
onized artistic creation. With the success of diffusion
ing high-quality, real-life image generation capabilities,
s, contents, and styles of artworks through simple textual
[72], or poetry [93] have produced impressive content,
ity but elevated beyond it. This revolution extends further
planning [186], offering exciting possibilities to create a
and expansion, particularly in encompassing entire cities
re developments may involve enhanced interoperability
ersonalized experiences, advancements in haptic feedback
tralized virtual economies. Our proposed foundational
ed agent to achieve urban generative intelligence.
an Generative Intelligence (UGI) platform (see Figure 1).
n knowledge graphs (Urban KG) and various data streams
astructure will provide a standard language interface that
tive agents. It allows the generative intelligent models to
wledge in digital infrastructure, test strategies in various

Urban Gener
simulated scenarios and learn to evolve based on the feed
facilitate various downstream urban applications. The ke
follows:
Open Digital Infrastructure: This component aims to
resources and computational tools designed for urban pro
systems to collect massive spatial-temporal data of emp
(e.g. points-of-interest and areas-of-interest), infrastruc
human behaviour (e.g. individual movements and colle
These rich datasets are fed into a powerful city simulator
between human, thing and space in an efficient and exten
module can simulate various hypothetical scenarios efficie
Besides, UrbanKG module [95] fuses various data stream
like “border by” and semantic relation like “category of”
and basic operations and algorithms of factual knowledg
models.
Language Interface: We design a standardized language
ture. City simulator, Urban KG and diverse data sources
algorithms to configure city simulator, retrieve factual kn
Such obstacles limit their application in downstream task
In our architecture, we design a user-friendly language
infrastructure. It uses predefined natural language proto
conveniently leverage the computation power of city sim
standardized language interface reduces the barrier of d
digital infrastructure, which hopefully will foster the pro
Generative Intelligence: On top of the language interface
problems, CityGPT. Specifically, CityGPT is a pre-trained
the language interface. It effectively leverages the reasoni
greatly reinforced for specialized local urban problems.
design a series of generative agents in the dimensions of u
not only are capable of high quality decision making in
simulations. Such agents combined with CityGPT will
important urban problems, such as urban planning, clima
4 Open Digital Infrastructure
One question that must be answered on the road to buildi
digital environment. With a real urban digital environm
interaction behaviors in this environment. Therefore, the
systems, and even assess the level of urban intelligence. T
requirements of agents, we start with urban modeling in
multiple sources in Section 4.2, implement a computatio
and economic simulations in Section 4.3, and finally prov
language interface for agents and human users in Section
shown in Figure 2.
4.1 Urban Modeling
From the perspective of urban spatial structure, cities can b
connecting each area. These areas include commercial la
residential land such as neighborhoods, and public servic
these areas as areas-of-interest (AOIs).
From the perspective of urban functions, cities are repres
cater to the dietary needs of the public, hotels provide te
help people with vehicle problems.

e Intelligence A PREPRINT
k. Consequently, these empowered generative models will
omponents of the presented architecture are elaborated as
vide a backbone system that integrates the data science
ms. Specifically, it accesses various data streams in urban
al urban activities, covering the aspects of spatial layout
e distribution (e.g. road network and subway network),
e mobility flows) and urban dynamics (e.g. traffic jams).
rage [176], which can simulate the complex interactions
e manner. On top of the empirical observational data, this
y, providing diverse environment to host intelligent agents.
nd extracts factual knowledge, such as the spatial relation
rban KG provides the functions of construction, storage,
which can facilitate easy access in generative intelligence
erface to fully release the power of open digital infrastrucd to be difficult to access. They often require customized
ledge from Urban KG and integrate various data sources.
nd make their power inaccessible to advanced AI models.
erface to fully unleash the potential of the open digital
to allow large language models and generative agents to
ator and access factual knowledge from Urban KG. The
oping language model-driven agents on top of the open
ation of generative urban agents.
propose to train a foundation model customized for urban
ge language model that encodes local urban knowledge via
apability and common sense in large language model, and
powered by this powerful city foundation model, we will
mobility, economy, community and society. These agents
ious scenarios, but also can enable realistic agent-based
ase the power of generative intelligence to solve various
daptation, inequality reduction, etc.
urban generative intelligence is how to create a real urban
, agents can use LLMs’ capabilities to perform realistic
an address specific urban issues, simulate complex urban
uild open digital infrastructure that satisfy the interaction
ction 4.1, build data streams of real urban data based on
engine (i.e. city simulator) that supports mobility, social,
open application programming interface (API) and natural
The whole framework of the open digital infrastructure is
onsidered to be made up of many areas and a road network
uch as shopping centers, industrial land such as factories,
nd such as parks and sport fields. In the work, we define
d as a collection of points-of-interest (POIs). Restaurants
rary accommodation for travelers, and auto repair stores

Urban Generative Intelligence A PREPRINT
Multi-Mode Mobility
Simulation
CPU/GPU Acceleration
Clock
Social Economy
Simulation Simulation Infrastructure
Network
Simulation
nepO
ytiC
smaertS
ataD
secafretnI
rotalumiS
Natural Language Interface
Python API
Protobuf + gRPC API Data Streams API
Databases UrbanKG
Spatial Urban Infrastructure
Human
Structure Functions Networks
Street View Satellite Imagery Economy
Figure 2: The framework of the open digital infrastructure.
To model the external and internal characteristics of the city at the same time, our urban modeling takes into account
both the urban spatial structure and urban functions, including the urban road network, AOIs, and POIs. In more detail,
the urban road network contains two types of elements, roads and junctions.
After modeling the spatial structure and function of the city, we then consider the most critical element that makes up
the city, human. Under such modeling, human activity in the city is in terms of spatial structure moving between the
urban road network and AOIs, while in the functional sense it is expressed as visiting different POIs at different times.
Human social behavior is then viewed as peer-to-peer and peer-to-cluster messaging. Relationships in pairs or groups
can be predefined through social networks (i.e. online socialization) or obtained based on spatial proximity (i.e. offline
socialization).
To model the necessities that people need to live in cities, we also need to model infrastructure networks and economic
systems. Infrastructure networks, including power grids, water supply networks, communication networks, etc., are
modeled as a topology with AOIs as vertices, and edges represent infrastructure conduits like electrical wiring, water
pipes, etc. Modeling of economic systems includes companies, individuals, governments, banks. Between these entities,
we model the basic economic behaviors of consumption, wages, taxes, and interest.
Through the above modeling, we are able to obtain a comprehensive description of people’s lives in the city, including
people’s mobility, people’s socialization, people’s economic behavior, etc. This will guide us in refining the construction
of real data streams and the implementation of the city simulator.
4.2 Data Streams
4.2.1 Databases
To model cities realistically, it is important to continuously collect real-world data and enrich the attributes of urban
elements based on the data and the data preprocessing processes. To achieve this, we build a pipeline that incorporates
multiple data sources such as open source crowd-sourced data, research results [58, 137], and Internet application
8

Urban Gener
services to profile a city. After preprocessing is complete
used as input to the city simulator or available for call by
For the urban spatial structure, i.e., the urban road network
topology and AOI polygon boundaries from OpenStreetM
meet the needs of the city simulator, we perform a series
vertex-edge topology, we first aggregate redundant vertic
junction and an edge corresponds to a real-world road. Fo
to them based on the road class provided by OpenStreetM
topology and the geometry of the edges, distinguishing b
junction morphology, we establish the road to road conn
phases. Finally, we can obtain an urban road network wit
• Road: ID, road’s geometry, number of lanes an
• Junction: ID, list of road IDs connected to the j
and the turn types, and signal phases.
For the AOI data, we use only the polygon boundary da
AOIs, land use [58] and population data [137] are matc
the population size attribute to the AOI. Besides, we also
locations of the connection points between the AOI and th
between the AOI and the urban road network. Thus, we c
• AOI: ID, boundary geometry, land use type, pop
For POI data representing urban functions, we use Ur
correlation knowledge and data fusion of urban domain
containing it based on its latitude and longitude coordinate
to the spatial structure of the city through spatial subordi
(e.g. go for leisure) and actions (e.g. drive to the park)
following attributes:
• POI: ID, coordinate, name, category, and belon
It is very hard to get direct access to the activities of all p
training on sampled human travel records (e.g., check-in
169, 171] can help us generate and restore the full amoun
real pattern. The generated human activity contains the f
• Person: ID, home position, list of trips.
A trip is characterized by a tuple (P , P , t , mode), whe
s e s
trip, t represents the starting time of the trip, and mod
s
walking, driving, or biking.
For the infrastructure network, we use heuristics for const
the resource demand based on the regional population an
the edges based on the aggregation of the resource deman
with a hierarchical structure and use it for infrastructure
the following attributes:
• Vertex: ID, coordinate, level and belonging AO
• Edge: vertex pair, line geometry and level.
For different infrastructure networks, specific fields are
inputs.
The city’s economic performance data are better publicize
such as enterprise information disclosure platforms, recru
information of enterprises in the city as well as the main
different areas. This data is eventually matched to the AO
2https://www.openstreetmap.org/

e Intelligence A PREPRINT
e city modeling data is stored in multiple databases to be
agent via the API.
d AOIs, we first obtain the original urban road vertex-edge
2. To improve the quality of the OpenStreetMap data to
processes on the raw geometric data. For the urban road
and edges so that each vertex corresponds to a real-world
e edges, we assign the number of lanes and the speed limit
Then, we identify the junction morphology based on the
een ramps, crossroads, T-intersections, etc. Based on the
vity at the junction and assign their turn types and signal
e following elements and attributes:
eed limit.
ion, connectivity between roads with the number of lanes
provided by OpenStreetMap. To enrich the attributes of
to AOI polygons and used to add the type attribute and
atch the AOI polygons with close roads to get the spatial
eighboring roads, and establish the topological association
obtain AOIs with the following attributes:
tion, and road connection points.
KG’s data sources to benefit from the spatio-temporal
ovided by UrbanKG. We match the POI data to the AOI
n this way, elements describing urban functions are linked
on, which helps to understand and control the intentions
human activities in cities. We can obtain POIs with the
g AOI ID.
le in the city. However, through data analysis and model
uences, GPS tracks, etc.), deep learning models [124, 125,
human mobility behavior in the city that conforms to the
wing attributes:
P and P denote the starting and ending positions of the
s e
dicates the mobility mode used during the trip, such as
ion. The methods consider each AOI as a vertex, calculate
nd use type, and then obtain the higher-level vertices and
Finally, we can obtain an infrastructure network topology
work simulation. In general, infrastructure networks have
.
o added to match the corresponding simulation program
By crawling the public information from internet platforms
ent platforms and real estate agency platforms, we get the
ustries, wage levels, consumption levels and rent levels in
y adding the following fields to the AOI:

Urban Gener
• Enterprises: name, category, registered capital,
• Consumption: per capita consumption of differ
• Rent: average rent.
In order to add more real city information and build a
additional data source. These images include satellite ima
tiles and the data source is from Mapbox 3. Street view da
where the images are located are spaced at intervals of 10
4.2.2 Knowledge Graphs
At the urban functional level, the complex relationships
However, it is difficult to process and mine the correlatio
solely on the attributes of POIs.
In the field of data mining, knowledge graphs [146, 6
knowledge, which can help users quickly retrieve othe
idea, UrbanKG [96] is proposed to build the relationsh
variety of relations for urban entities. Of these, the relatio
and locateAt, belongTo. The relations regarding urba
competitive, coCheckin, similarFunc, provideSer
Besides, for multi-modal data, UrbanKG establishes two r
relational categories designed by expert knowledge and
understanding of urban spatial structure and urban functio
4.3 City Simulator
The open digital infrastructure computational engine is c
Firstly, the city simulator [175, 176] can efficiently sim
large-scale cities. In detail, it simulate the movement o
multiple mobility modes (e.g. driving, walking, etc.), a
like obtaining its current road or querying specific AOIs’
the simulator is described as a list of trips. Therefore, the
Overall, city simulators provide agents with sense and c
interface to obtain the current road, query the AOI and PO
to the AOI where a restaurant type POI is located.
As the most important part of open digital infrastructure, t
of generative agents and provide excellent computing effi
end, the city simulator has implemented numerous softwa
the following features:
• Multiple Modes Simulation: The city simulator
driving, walking, biking and public transportatio
through space in cities. In order to realistically s
IDM car-following model [140] and MOBIL lan
model to simulate walking.
• Clock Synchronization: During the simulation
keep the simulation time synchronized. In orde
introduced in the Mirage framework [176] is em
is opened as a necessary link for agent access.
• Computing Acceleration: Through reasonable
an efficient indexing subsystem [175], the city
times compared to wall clock time for nearly o
quickly explore, learn and evolve.
3https://docs.mapbox.com/api/maps/raster-tiles
4https://map.baidu.com/

e Intelligence A PREPRINT
mber of employees and average wage.
POI categories.
ltimodal data base, we finally introduced images as an
and street view data. Satellite image data is organized in
s obtained from Baidu Maps 4, and the spatial coordinates
meters from each other.
ween POIs further constitute the uniqueness of the city.
etween POIs and aggregate and distill massive data based
re a means of effectively organizing massive data and
tities that are related to a given entity. Inspired by the
network of entities within the city. UrbanKG builds a
on the urban spatial structure include borderBy, nearBy
nctions include brandOf, cate1Of, cate2Of, cate3Of,
ce, etc.
onships satelliteImageOf and streetViewOf. These
data-driven fact set provided by UrbanKG enhance the
nd also provide more effective information input to agents.
d the city simulator.
ate the interactions between human and urban space in
gents in the urban space between roads and AOIs using
provide agents with the ability to sense the environment
d POIs’ information by IDs. The agent’s mobility task in
ent’s behavior can be controlled by modifying its trip list.
rol. For example, the agent can use the city simulator’s
nformation on the road, and then control the agent to walk
ity simulator need to be able to host the access of a variety
ncy to ensure the speed of city-level simulations. To this
esign and optimization for urban simulation, and achieves
ports the simulation of multiple mobility modes, including
his comprehensively models how people commonly move
ulate human mobility behavior, we adopt the widely used
anging model [75] to simulate driving, and the PCS [173]
e city simulator and the accessed agents must be able to
achieve this goal, the clock synchronization mechanism
ded in the city simulator, and the communication interface
ign of control flow and data flow, and the introduction of
ulator achieves computing acceleration of more than 10
million agents at the urban scale. This can help the agent

Urban Generative Intelligence A PREPRINT
• Various Data Retrieval Interfaces: The city simulator models the spatial structure of the city. Therefore, it
also provides a rich data retrieval interfaces about the spatial structure and the agents running in the spatial
structure. These retrieval interfaces include retrieval of urban spatial topological structures (e.g. which roads
the specified AOI is connected to) and runtime status (e.g. how many people are in the specified AOI now).
These retrieval interfaces provide two access forms: pull and push. The specific details will be introduced in
Section 4.4.1.
• Unified Control Interface: In order to simplify the control of the agent, the control interface of the agent
is unified into modifying the agent’s trip list. By modifying the trip list, the caller can control the agent’s
attributes such as stay time, departure time, destination, and mobility mode.
On top of the mobility simulation, we also add the ability to social message propagation and financial flow mechanism
based on the extended friendliness of the city simulator. The social message propagation mechanism allows a person to
send a message to a specific list of people or broadcast it to the surrounding crowd, which enables online and offline
socialization, respectively. Financial flows are triggered primarily based on a person’s visit to a POI. Depending on
the POI category, the city simulator models consumption, income and taxes. The simulation of interest is triggered
periodically. Through these features, the city simulator can realistically model the life activities of agents in urban
space, orderly access a large number of generative agents, and provide rich sense capabilities and a simple and unified
control method. This provides an environment for exploration, learning and evaluation for agents. Agents can use
the city simulator to enhance their understanding of the city, and even deduce the future evolution of the city and find
optimal decisions.
Using the distributed architecture described in Mirage [176], the simulation of the infrastructure networks is implemented
as multiple independent extensions in the city simulator. We support to integrate PYPOWER5 as grid simulation,
WNTR [78] and SWMM [55] as water supply and drainage simulation, and the digital twin system for mobile
networks [57] as communication simulation.
4.4 Open Interfaces
4.4.1 Application Programming Interface
As the open digital infrastructure in UGI, its capabilities need to be exported through open interfaces. For experienced
developers, we provide two layers of application programming interface (API). The first layer is based on Protobuf 6
and gRPC7. We use Protobuf to standardize data structures including roads, junctions, AOIs, and POIs. gRPC is used to
implement communication between the caller and the city simulator to achieve clock synchronization, data retrieval,
and control. Actually, the gRPC implementation we use is Connect 8, which is a simple, reliable and interoperable
library to provide both browser (i.e. JSON format message on HTTP) and gRPC-compatible APIs. For users who do
not want to see the underlying communication implementation, we provide a higher-level Python API. Through the
Python API, users can interact with the open infrastructure in the form of Python function calls and receive responses in
Python’s basic data format (e.g. dict and list), which is more familiar to researchers.
For the original data from the data streams, encapsulation of database access is provided in the Python API. Relation
queries and reasoning to UrbanKG are also included in it.
Through these APIs, users can not only access the original data provided by the data streams, but also can sense the
environment and control agents in the city simulator. The main sense APIs are as follows:
• GetAoi: get the runtime status of the specific AOI.
– Input: AOI ID.
– Output: list of people IDs, number of recent entries and departures.
• GetRoad: get the runtime status of the specific road.
– Input: road ID.
– Output: list of vehicle IDs and pedestrian IDs, average speed and congestion level.
• GetPerson: get the runtime status of the specific person.
– Input: person ID.
5https://github.com/rwl/PYPOWER/
6https://protobuf.dev/programming-guides/proto3/
7https://grpc.io/
8https://connectrpc.com/
11

Urban Gener
– Output: coordinate, speed, direction, trip c
The unique control API is as follows:
• SetTrips: modify a person’s trip list to change th
– Input: person ID and new list of trips.
– Output: None.
In particular, in order to avoid excessive processing pre
mechanism for the retrieval of runtime environmental inf
certain element through the API. When the element cha
trigger the corresponding processing logic. The list of tr
limited to, the following scenarios:
• Someone enters the specific AOI.
• Someone leaves the specific AOI.
• Someone enters the specific road.
• Someone leaves the specific road.
• The specific person starts a trip.
• The specific person finishes a trip.
For example, the client can monitor the entry of a person
client will receive the information about the person who e
person.
4.4.2 Natural Language Interface
For users without programming skills, we also provide a n
further encapsulation of the API. Users can use some stan
such as data retrieval and agent control like ALFWorld [1
For instance, in the natural language interface, the inform
• Request: Get AOI with ID 500000000.
• Response: The AOI with ID 500000000 has an
use type is commercial land, contains 51 POIs,
The control of the agent is expressed in the following for
• Request: Set agent with ID 1000 to drive to AO
11:00.
• Response: OK.
5 Foundation Model and Agent
5.1 CityGPT: Large Language Model for Urban Ge
As the fundamental component of platform, the large
city agents with general and specific skills in the urban
large language model determines the upper limit of wh
model [159, 139, 8], which are build for general purpose.
chat and text generation, they perform inefficiently even
in many cases due to the lack of domain-specific backg
enhance the general large language model to meet the re
whole enhancement procedure is presented in the Figure 3
model to obtain the CityGPT. Firstly, we aim to incorpora
language model. Then, based on the output of the first step
the related skills of it for urban intelligence.

e Intelligence A PREPRINT
ently in progress.
erson’s moving target, departure time, and mobility mode.
re caused by polling, the city simulator provides a push
mation. The client can specify to monitor the changes of a
s, the city simulator will push a message to the client to
ers that support the push mechanism includes, but is not
o the specified AOI. When someone enters the AOI, the
s the AOI, so that it can control the future behavior of the
ral language interface. The natural language interface is a
dized natural language instructions to complete functions
.
on to retrieve AOI is expressed in the following form:
a of 26059 square meters, a population of 1219, the land
is connected to roads 10, 11 and 23.
00000001 at 09:20, and then walk to AOI 500000010 at
ative Intelligence
guage model plays the critical role of empowering the
nerative intelligence. In other words, the ability of the
system. There exists many open source large language
ile these models perform well on common tasks like daily
l to support the generative city agent in the urban space
nd knowledge [144] and related skills. Thus, we need to
ements of city agents modelling in the urban space. The
We introduce two steps to refine the general large language
g the multi-source urban knowledge into the general large
e design sufficient methods and training datasets to induce

Urban Generative Intelligence A PREPRINT
Figure 3: Training procedure of CityGPT.
Figure 4: Training data of CityGPT.
Stage 1: incorporating the urban knowledge. As claimed in open source models [159, 139, 8], most of the training
corpus are from the public web text like common crawl project and only limited common data processing methods
are applied due to the high-cost of handling the large volume various data. However, domain specific data like urban
knowledge data are usually not open and specific data processing method is fundamentally necessary for utilizing
them. Thus, incorporating the carefully processed urban knowledge into the general large language model becomes
an essential step. There are several methods for incorporating knowledge into the large language model, including
retrieval based methods [85], fine-tuning based methods [49], and continue pre-training methods [74]. The retrieval
based methods rely on the effective retrieval mechanisms and only limited knowledge can be utilized for each single
use. While fine-tuning methods can introduce more knowledge than the first one, their capacity are still limited and may
amplify the hallucination of large language model when requiring model to output things which not learned during its
pre-training. Thus, we apply continue pre-training methods to incorporating urban knowledge into the general large
language model.
As shown in the left part in the Figure 4, we collect general text corpus (e.g., domain-specific research papers, highquality codes and online web text) and domain-specific data (e.g., urban knowledge graph [95], geographic data, human
behavior data [46]) to conduct the continue pre-training process. We follow the data cleaning rules in open source
LLMs [159, 8] to process the general text corpus data. As for the domain-specific data, we process them case by
13

Urban Gener
Figure 5: A general framework for em
case. For knowledge graph data, we apply the universal
into model. Given a pair of tuple from urban knowledge
Different from the original paper, we combine the tuple
For geographic data, we directly use the widely-used geoj
as a single training instance. For human behavior data, w
source and regard each behavior session as a single traini
as the base model and utilize deepspeed [120] to contin
GPUs for about one week. Other general large language
experimental example. The continue pre-trained model is
Stage 2: inducing the urban intelligence ability. After t
various urban knowledge. While we can directly extra
method, it requires few-shot demonstrations during the us
learn to response based on the injected factual urban kno
output formats, e.g., JSON. Thus, we need the alignme
ability of model. Follow the common practice of large la
and DPO [117] to achieve this goal. The dataset used in
Figure 4. Specifically, we build a domain-specific align
datasets [83, 155], domain-specific chat datasets and ta
urban space) chat dataset. The open source general purpo
fluently. Similar to the self-instruct framework [148, 39
question-answer pair with ChatGPT on the domain specifi
urban tasks with the assistance of ChatGPT and external to
are directly added in the continue pre-training stage, we a
solving the specific tasks. Details about the task-solvin
sections. After supervised fine-tuning CityGPT on above
human preferences. We use trl [141] with packing strateg
After the above two-stage training procedure, we obtain t
for urban generative intelligence. In the following section
instructions to complete different tasks.

e Intelligence A PREPRINT
died generative agents in urban space.
wledge-text prediction task [135] to integrate knowledge
aph, we use ChatGPT to generate a related text sentence.
the related text as a training instance in the pre-training.
[27] format in the GIS community to organize each object
ignment their elements with the aforementioned two data
nstance. We choose the open source Baichuan2-7B [159]
re-train the model on a single machine with eight A100
del can also be selected and we take Baichuan2-7B as an
led as CityGPT-base model.
continue pre-training procedure, the based model acquires
nformation from the base model via in-context learning
hich are not easy to construct. Besides, we want CityGPT
dge and follow the instruction from agents with standard
rocedure [111] to induce the these general and specific
age model [159, 139, 8], we apply supervised fine-tuning
supervised fine-tuning stage is shown in the right part of
nt dataset with three kinds of data: general purpose chat
solving (e.g., schedule planning, and navigation task in
chat datasets aim to teach model how to chat with people
we build the domain-specific chat dataset by generating
ext corpus. Task-solving dataset is built by solving classic
It is noted that while urban knowledge data like UrbanKG
use the UrbanKG as an external knowledge source when
ocess of different urban tasks can refer to the following
sets, we use UltraFeedback [35] with DPO to align it with
o accelerate the training procedure.
CityGPT, an urban knowledge enhanced foundation model
with sufficient prompts as inputs, CityGPT will follow the

Urban Gener
5.2 General Framework for Generative City Agents
Here, we present a general framework for embodied gen
leverages generative foundation model as intelligence co
simulator and UrbanKG knowledge graph. Following e
generative agents to harness the realistic embodied fee
intelligence in simulated urban environment. The propo
for most generative city agents, and provide enough flexi
the autonomous agents under this framework have the M
The memory component stores the history of past behaiv
specific profile to leverage the role play capability of lang
the agents with high-level language description. Besides
senses the simulated urban environment; act module that
communicate module to exchange information with other
generative intelligence core, which can comprehensively
generate appropriate behaviours. To better illustrate our fr
focusing on two major categories of urban problems, i.e.,
making.
5.2.1 Simulation Agent: Generating Individual and
Complex urban phenomena are driven by the spatiotemp
and social domains. Understanding the underlying micro
role in modeling and managing urban systems, necessita
autonomous agents. Here, we present three design exampl
which are customized for the simulation of the basic u
respectively.
Physical mobility: This agent aims to simulate individua
the objective of creating trajectories that mirror real-life
behavior, we also want to reproduce the statistical distr
of these agents, such as reproducing the daily number o
models often use simplified rules to guide agent’s mobi
semantic in urban mobility, such as the function of a spe
The generative intelligence in city foundation model offers
and has deep knowledge of the local environment. These
norms and human behaviour patterns, contributing to mo
language models, particularly through their prompt-base
behavior simulation.
We propose a generative agent that involves the memory
framework, combined with reasoning core driven by Cit
historical mobility patterns, and persona module holds
agent will generate mobility behaviour step by step base
demographic profiles. Besides, it will also jointly conside
environment, such as current time and road traffic. Af
locations in simulator via act module. We also design an
each agent based on its profile, such as the work schedule
core is prompted to avoid violation with these anchor poin
of realistic, personalized and coherent urban mobility beh
physical domains, reflecting the interactions between urb
Economy activity: For the economy, agent-based model
and predicting the dynamics of economic systems [44]. S
unemployment rate, etc., Traditional methods, such as e
scenarios. For example, for one of the most famous econ
(DGSE) [63], sometimes there is no feasible solution f
construct multiple heterogeneous agents to describe each
behaviors the agents can have. The major objective of th
the emerging phenomenon from the perspective of macr

e Intelligence A PREPRINT
ive agents in urban space (see Figure 5). This framework
and it is built upon the open digital infrastructure of city
odied cognition hypothesis [152], this framework allows
ck provided by the digital infrastructure and evolve its
framework aims to extract a unified conceptual abstract
ty for customization in various applications. Specifically,
al States components of memory, persona and preference.
and interactions, persona component assign the agents a
e model, and preference component allows personalizing
e Interaction components include: perceive module that
isters behaviours or status changes in city simulator; and
nts. Finally, these agents use city foundation model as its
del the internal Mental States and external Interactions to
work, we provide several concrete agent designs as below,
ulating urban phenomena and informing complex decision
lective Behaviour
agglomeration of micro activities in physical, economic
echanisms and the emergence process plays an important
the simulation of complex urban phenomena with micro
f embodied agents under the proposed general framework,
n activities in physical, economic and social domains,
ctivities and movements within urban environments, with
terns. In addition to generate logical individual mobility
ion of collective movements by simulating a population
mmuters between two locations. Traditional simulation
behaviour, but they lack depth in understanding the rich
place and characteristics of diverse demographic profile.
romising alternative. It excels in common sense reasoning
ures equip simulation agents with accurate prior of social
plausible simulation outcomes. Besides, the flexibility of
echanism, enables more logical and realistic reasoning in
rsona, perceive and act modules in the proposed general
PT. The memory module serves as the knowledge base of
ographic profiles of the simulated agents. The designed
its historic movements and the preference inferred from
e contextual information perceived from simulated urban
generating a mobility behaviour, it will register its new
chor detection mechanism that will generate a routine for
rving as the anchor points of its daily life. The reasoning
uring generation. Such agent designs allow the simulation
urs, which are the most essential micro urban activities in
dwellers and the access of various urban resources.
and simulation is a promising solution for understanding
fically, when predicting economic indicators such as GDP,
ometrics [132], cannot handle some complex real-world
etrics methods, Dynamic Stochastic General Equilibrium
he equilibrium. That is, the agent-based simulation can
r in the ecosystem and then define what kind of economic
gent-based simulation in the economy is to observe both
onomics and behavioral economics, which can regarded

Urban Generative Intelligence A PREPRINT
Labor Income Tax Government
Redistribution
Bank
Consumption
dnameD ylppuS
Memory
Market Dynamics
Income Inflation
Savings Interest Rate
Consumption Interest Rate
Inflation
Tax, Redistribution
noitcelfeR
Prompt
Decision
Prompt
ledoM
egaugnaL
egraL
ylppuS dnameD
LLM Agent Macroeconomics
2
1
3
4
1
Figure 6: The illustration of LLM-driven agents for economic simulation [88].
as an environment to support theory validation and decision-making. To construct the economic agents, our previous
work [88] follows the well-acknowledged simulation mechanism illustrated in Figure 6.
Specifically, there are four components: labor, consumption, financial markets, and government taxation, covering
the primary components of existing macroeconomic simulations. Specifically, the agent is deployed to simulate the
two most critical decisions the real human will make in real life: going to work (earning money) and consumption
(spending money). The government agents decide the tax policy, and the bank agents adjust interest rates based on
market inflation or deflation. From the macroscopic perspective, the system can observe the dynamics of overall labor
and consumption markets.
Social interaction: Human social behaviors can also be simulated with large language model-empowered agents.
Specifically, the social agents require human-like abilities in social behaviors, i.e., interacting with other individuals in
the city system. For social activities, there are both online and offline social networks, i.e., the communication can
occur in both online social networks or just via chatting in a room. The social agent simulation mainly focuses on how
information propagates on the social network and its further impact on the individuals. That is, the LLM-driven agent
can first shape their social awareness, i.e., distinguishing the friends and other individuals and distinguishing different
social-tie strengths. The agents can further make their own daily schedule autonomously in the city environment, which
further leads to social activities, yielding interaction between different agents, including chatting, cooperation, or even
conflicts. Last, the online social network, which is not restricted by the physical space, also provides the environment
for social activities. The agents can post new content or propagate content of the other users. Despite the behavior
itself, the internal characteristics, including the emotion and attitude of the agent, are also contained in the memory and
mechanism of the large language model-based social agents. Overall speaking, the simulation can be evaluated from
both individual-level and population-level perspectives. Regarding individual-level simulation, the aim is to generate
social behaviors, attitudes, and emotions by leveraging user characteristics and the informational context within social
networks. In the social simulation system S3 [51] built based on the UGI system, the social agents can accurately
simulate the propagation process of information, attitude, and emotion on two representative events about nuclear
energy and gender discrimination. To summarize, the UGI system provides a good platform to support understanding
and simulate social behaviors, including the emerged social phenomenon.
5.2.2 Decision Making Agent: Task Solving and Personal Assistance
We present the design cases of decision-making agents in the following two scenarios.
Location recommendation: Location recommendation is one kind of new infrastructure in the area of information
overload. That is, there are too many points of interest (locations) in the city environment, and the individual living
there finds it hard to determine where to visit to meet the demands. Furthermore, each individual may have his/her
own preferences and interests, which motivates the construction of personalized assistants based on large language
model-empowered agents. In our system, we design an LLM-driven agent for location recommendation based on the
LLM’s strong ability to understand both user preferences and decision-making. First, the agent can extract critical
information from the profile, attributes, and other basic information for a given user. In other words, the LLM agent can
be a personal assistant with essential information about the user. Second, the agent is good at planning and scheduling
based on the city environment’s feedback. Specifically, it is always challenging for a human to directly query or search
for locations for visitation since the searching or filtering process will be faced with abundant data and information.
To address it, the agent can organize the output of the traditional search and recommendation engines well and even
adjust the engine if the results cannot meet the requirements. Last, the agent can communicate well with the user,
16

Urban Gener
Figure 7: Systematic evaluation fram
understand the user’s new and instant feedback, and prov
the users’ historical behaviors, personal demands, or spat
agents have three major abilities, including 1) understand
profiles and interests based on historical data and then adj
demands given the real-world city environment.
Schedule planning: Effective schedule planning is crucia
often relying on shortest path algorithms [42], provide t
They fail to account for user-specific preferences and ca
potentially leading to suboptimal scheduling and confli
model-driven agent to help users make high quality dec
CityGPT capabilities, integrating common-sense knowle
planning solutions. Its natural language interface ensures a
enhancing the user experience.
The proposed agent comprises several key components
the comprehension and reasoning skills of its generati
respect the fixed commitments specified by users while ac
module continuously integrates new information, facilitat
and communicate, the agent evaluates the feasibility of
schedule with the user preference inferred from persona m
approach represents a significant advancement in persona
understanding and reasoning for more tailored and efficie
represents the basic decision making capability in urban d
that continuously learns user preference and evolves with
6 Evaluation
Here, we introduce a systematic evaluation framework
empowered agents for urban generative intelligence. As
three levels,
• Level 1: evaluating the urban knowledge of City
• Level 2: evaluating the simple reasoning abili
answering
• Level 3: evaluating the planning and decision ma
in urban space
Level 1: Automated domain-specific question answer e
CityGPT really learn and understand the domain-knowled

e Intelligence A PREPRINT
ork for urban generative intelligence.
extual explanations for recommendation results based on
emporal context. In UGI, the large language model-based
the mixed and complex user intents, 2) detecting the user
ng recommendations, and 3) identifying the improper user
efficient daily activity management. Traditional methods,
-saving solutions but lack personalization and flexibility.
dynamically adapt to evolving or abstract requirements,
To overcome these limitations, we design a foundation
ns for nuanced schedule planning. This agent leverages
e to contextualize tasks and offering logical, user-centric
mless, intuitive human-computer interaction, significantly
pon receiving user’s schedule input, the agent will use
ntelligence core to formulate optimal schedule. It will
mmodating preferences and time constraints. The memory
dynamic adjustments. Through its interfaces for perceive
s, considering travel time and proximity. It finalizes the
ule, ensuring logical coherence and user satisfaction. This
d schedule planning, harnessing foundation model’s deep
aily organization. The design of schedule planning agent
y life, which can also serve as a useful personal assistance
ban environment.
alidate the performance of foundation model and LLM
wn in Figure 7, the whole evaluation framework contains
T by automated domain-specific question answering
f CityGPT via human labeled domain-specific question
g ability of generative city agents by solving specific tasks
uation. Evaluation in Level 1 aims to validate whether the
injected in the training. To do this, we first extract related

Urban Generative Intelligence A PREPRINT
Figure 8: Human labeled domain-specific question answer example on commonsense knowledge. The left is the answer
from ChatGPT, the right is the answer from CityGPT.
domain-specific question answer pairs from various general evaluation datasets including Gaokao [180], CEval [69] and
CMMLU [87] as the first part of evaluation. Besides, we also construct domain-specific question answer pairs based
on the pre-training corpus with the help of ChatGPT. Specifically, we first random sample instance from the training
corpus. Then, with carefully designed prompts, we require ChatGPT to generate question and answer pairs based on the
input context. Finally, we design another prompt to require ChatGPT validate the quality of generated QA and filter the
low quality ones. In this way, we can collect questions span diverse topics in the city including transportation, civil
engineering, environment, geography and so on. To enable the automated evaluation, all the question answer pairs are
formatted as the multiple-choice questions and we use accuracy as the metric.
Level 2: Human labeled domain-specific question answer evaluation. We build Level 2 evaluation to validate the
reasoning ability of CityGPT in the simple scenarios of city. Different from the Level 1 evaluation, we hope the Level
2 evaluation can take a step further by answering the questions which can not be directly extracted from the training
corpus. Thus, we recruit volunteers with various backgrounds to write new expert problems related to urban intelligence
and corresponding answers. To guarantee the coverage of problems on urban space, we predefine a question taxonomy
of various domain to lead the topic selection of volunteers. One example of question on common knowledge is shown
in Figure 8 and another example on route planning is presented in Figure 9. We can find that due to the lack of domain
knowledge on urban space, advanced LLMs like ChatGPT cannot solve these simple urban problems. At the same time,
CityGPT with domain-knowledge enhancement solve them easily.
Level 3: Problem solving of various urban tasks. Finally, we introduce several complicated real-life urban task
as Level 3 evaluation to validate the capability of generative city agents on long term planning and decision making.
We use next location prediction, PoI navigation without map, daily schedule planning, and society simulation as four
representative tasks. To complete these tasks, beyond the basic ability evaluated before, agents have to master several
high-level skills like spatial-temporal reasoning, multi-step goal decomposition, external tool using and so on. During
the evaluation, agent is only allowed to access the API and dataset provided by City Simulator. The agents empowered
by different foundation models should follow the same structure in the specific task. In each task, we provide hundreds
of samples for agents to complete and the overall success rate on these samples are calculated as the final metric of it. It
is noted that the definition of success rate various depending on the task. For simulation based tasks, we define the task
is successfully completed when its results meet the general law in the field and various pre-defined metrics.
18

Urban Gener
Figure 9: Human labeled domain-specific question answ
ChatGPT, the right is the answer from CityGPT.
7 Enabled Urban Applications
In this Section, we take several typical examples to discus
with complicated urban tasks and issues from four impor
society.
7.1 Transportation System
Travel surveys have long been a cornerstone in transpor
behaviors and patterns. These surveys inform urban plan
aiding in the creation of more efficient and user-centric tr
household travel surveys and on-board transit surveys, co
time-consuming to conduct, involving face-to-face interv
Additionally, the data collected may not adequately c
nature [121]. Recent advancements in technology hav
mobility [59]. Researchers leverage the increasingly ava
mobility [133], and design rule-based generator of urban m
to overcome the limitations of traditional surveys, offerin
However, the classic rule-based mobility generator mode
to simulate individual movements between several freq
lack a in-depth understanding of mobility intent and use
not realistic. Foundation model-driven generative agents
language model possesses not only robust comprehensi
quality reasoning based on contextual information. In thi
behaviour, which can generate realistic and intention-aw
important opportunity for high-quality and efficient alter
7.2 Business Intelligence
Business site selection plays a key role in the interdiscip
development. Traditional site selection methods, often re
intensive and time expensive [21, 81, 114]. In contrast, re
employing machine learning models fed with diverse ur
models, however, often lack comprehensive feature repres
advancements have introduced knowledge graphs in busi
structure for enhanced knowledge representation without

e Intelligence A PREPRINT
example on route planning. The left is the answer from
ow our proposed UGI foundation platform enables to deal
urban systems of transportation, business, economy, and
on research, providing indispensable insights into travel
g, infrastructure development, and transportation policy,
port systems. However, traditional travel surveys, such as
with significant challenges. They are often expensive and
s, manual data collection, and extensive processing [134].
re rapid shifts in travel behavior due to its infrequent
d to the exploration of data science research in human
le mobility data to identify the universal rules in human
ility behaviour [71]. This shift is significant as it promises
al-time data collection and analysis capabilities.
uch as TimeGeo [71], leverages simplified statistics rules
t locations like home, work, and other. However, they
rofiles, and hence the travel behaviour they generate are
ng about important opportunities. The reasoning core of
capabilities for commonsense, but also could make high
per, we describe a generative agent for physical mobility
travel behaviour. Such generative model will provide an
ve for travel survey.
ry areas of urban planning, economic growth, and social
t on expert consultants and manual surveys, are resourcerch interests have shifted towards a data-driven paradigm,
data to evaluate potential sites [73, 89, 94, 157]. These
ation and logical reasoning in their analysis [163]. Recent
s site selection, integrating multifaceted data into a graph
mplex feature engineering [70, 96]. Despite their potential,

Urban Gener
knowledge graphs face challenges in assimilating varie
ensuring interpretability in decision-making.
Foundation models have emerged as a promising tool, ca
knowledge, advanced language generation abilities, and ef
site selection offers capabilities like comprehensive info
foundation models often struggle with accurately recalling
propose to address these gaps with an integrated intellige
of knowledge graphs with the reasoning and common-sens
enhanced for urban problems in CityGPT. Utilizing algori
to deliver precise site selection results with enhanced d
efficiency and breadth. Therefore, we can leverage city
graph and various empirical data to transform business si
7.3 Urban Economy System
Agent-based modeling and simulation are of great import
other approaches. Early empirical statistical models, such
of Hendry [64], delved into data-driven analyses of macro
among pivotal variables. Kydland and Prescott [82] craf
outcomes. Later, the advent of Dynamic Stochastic Gener
dynamics of diverse economic variables like output, infl
the inherent uncertainty and randomness within econom
models operate under the assumption of a perfect world, w
economy. That is, the large language model-based econom
deploy various relevant applications.
Macroeconomic behavior. This simulation offers an idea
behaviors. By leveraging the interplay of diverse agents
market dynamics, and the ripple effects of economic decis
economic trends and devising resilient strategies in respo
Macroeconomic activities. Through this simulation fram
can be explored comprehensively. From trade dynamics an
behaviors, the model provides a simulated environment t
Policy making. This simulation serves as an invaluable to
policy interventions in a controlled environment. By simu
economic indicators, policymakers can fine-tune strategie
before implementation. This proactive approach to policy
to sustainable economic growth.
In essence, our system’s large language model-based e
framework for investigating, understanding, and shaping
7.4 Urban Society
Understanding our society is the core of social sciences,
on social experiments. Due to the high cost of real-wo
approach. There are two key perspectives in social simul
among individuals, and 2) the status evolving of the po
and practitioners gain the ability to forecast the future p
populations. Moreover, these simulations provide exper
their effects observed. The applications supported by our
Understanding individual behaviors in society. The sim
deep dive into individual behaviors within social contexts
can forecast and comprehend how individual actions are d
Predicting population-level dynamics. Beyond individ
population dynamics. It offers insights into how collectiv
aiding in anticipating societal shifts and trends.

e Intelligence A PREPRINT
rban data, refining knowledge for different factors, and
le of automating text-related tasks with extensive domain
nt data processing [151, 26]. Their application in business
ation retrieval and real-time decision support. However,
ts in knowledge-based content generation [160]. Here, we
te selection model. It combines the structured knowledge
owess of language foundation model, which is particularly
s of reasoning on knowledge graph, this model is designed
sion-making quality, clear interpretations and improved
ndation model to unleash the power in urban knowledge
election.
e for the research of the economy due to the limitations of
he Phelps Model [113] highlighted in the pioneering works
nomic phenomena. These models unraveled relationships
a computational model geared toward predicting policy
quilibrium (DSGE) models [33] aimed to encapsulate the
on, consumption, and investment, while accommodating
rocesses. However, as pointed out by Farmer [44], these
ch motivates agent-based modeling and simulation for the
simulation based on our system can be an environment to
atform to scrutinize and emulate complex macroeconomic
institutions, the model can elucidate emergent behaviors,
s. Understanding these behaviors is crucial for forecasting
to varying scenarios.
work, the intricate landscape of macroeconomic activities
nvestment patterns to consumption trends and labor market
amine and evaluate diverse economic activities.
or policymakers to test and assess the efficacy of different
ng policy scenarios and their potential impacts on various
aluate trade-offs, and anticipate unintended consequences
king helps in devising robust, adaptive policies conducive
nomic simulation platform offers a versatile and robust
croeconomic behavior, activities, and policy outcomes.
which the proposal and validation of theory highly relies
social experiments, the simulation is a very promising
n, as outlined by Gilbert [54]: 1) the dynamic interaction
ation. By simulating social activities, both researchers
ression of individual behaviors and the overall status of
ntal arenas where interventions can be implemented and
tem and agents can be summarized as follows.
tion system, along with the LLM-driven agents, enables a
y emulating these behaviors, researchers and practitioners
n by internal mechanisms and external contexts or factors.
behaviors, the system facilitates the prediction of broader
ehaviors, trends, and group interactions evolve over time,

Urban Gener
Experimenting with interventions and policy evalua
testing interventions in simulated social environments.
impact of various interventions, policies, or changes wit
potential real-world outcomes. Thus, policymakers can d
By testing proposed policies virtually, they can assess the
deployment.
Emergency and risk management. In the real-world sce
the challenge of risk prevention. By exploring different po
can prepare strategies to mitigate risks and adapt to chan
LLM-driven agents in simulated society.
8 Discussion
We discuss the open challenges and important future rese
the following aspects.
8.1 Dive into Complicated Urban Issues
Urban environments are dynamic and multifaceted, which
stemming from their intricate networks encompassing
mentioned in the Introduction, the rapid urbanization ex
pollution, resource scarcity, and infrastructure strain, along
crises. Addressing these issues is crucial for sustainable,
cities in a global context.
To navigate these complexities, our proposed foudation
emergent and sophisticated urban solutions. By levera
environment for interaction beyond traditional sandboxes
agents, UGI enables deep, context-aware insights, offering
allows for the emergence of intelligent solutions, which
cognitive capabilities similar to human intelligence, whil
While UGI holds promise in tackling urban complexities
the gap between advanced technological capabilities an
hurdle. This includes adapting UGI to rapidly evolving
pressing need to develop advanced embodied agent for a m
integrating the diverse social, economic, and environment
to the escalating challenges of rapid urbanization and clim
development. Addressing these problems is critical for th
a truly transformative tool for urban problem-solving.
8.2 Scale Up to Large City
Recent advancements in LLMs have opened new frontie
LLM agents, when personalized with diverse roles such as
complex tasks like software development, making signifi
processes [115]. The scalability of these simulations, intro
across various domains [193], which are particularly of s
However, simulating societies of large-scale LLM agen
faces substantial computational challenges. Research eff
operational efficiencies of these models [129, 4]. Techni
and quantization have been proposed [192]. Specificall
crucial technique, enhancing efficiency by simulating mu
in inference time and cost [32]. Moreover, the MetaGPT
presents a promising approach for efficient multi-agent
pool and subscription mechanism offer significant reduc
simulating expansive urban societies with LLM agents r
these simulations. Successfully simulating large-scale ur

e Intelligence A PREPRINT
n. The simulation serves as an experimental ground for
earchers and practitioners can implement and study the
these controlled settings, providing crucial insights into
op and evaluate policies in a simulated societal landscape.
otential effects and fine-tune strategies before real-world
o, emergency-related data is always sparse, which leads to
ial outcomes based on varying parameters, the government
g circumstances, supported by the simulation system and
directions of urban generative intelligence platform from
increasingly confronted with a myriad of complex issues
sical, social, economic, and environmental factors. As
rbates challenges like traffic congestion, environmental
e socio-economic issues like social inequality and housing
itable urban development and maintaining the vitality of
form of Urban Generative Intelligence (UGI) can foster
g the multi-source urban data and creating a real urban
virtual simulations, with the LLM-empowered embodied
anced understandings of urban dynamics. Morevoer, UGI
able to address complex urban issues through advanced
th the power of computational intelligence.
veral challenges necessitate further exploration. Bridging
actical, real-world urban applications remains a crucial
an dynamics and policy landscapes. Moreover, there is a
nuanced, systematic understanding of urban complexities,
spects of urban life. Additionally, adapting these solutions
change is vital for ensuring sustainable and resilient urban
ccessful implementation and evolution of UGI, making it
n simulating complex urban systems. Studies reveal that
cutives, engineers, and designers, can synergistically solve
t strides in designing, coding, testing, and documentation
ing more varied personas, has been shown to be beneficial
lating large urban systems.
flecting the complex constraints in urban environments,
are geared towards optimizing the memory footprint and
s like model compression through knowledge distillation
n urban simulations, batch prompting has emerged as a
le agents concurrently, showing up to a 5x improvement
mework, initially applied in virtual software companies,
aboration in urban simulations [66]. Its shared message
s in resource consumption. Despite these advancements,
ains a formidable challenge, limiting the full potential of
environments with LLM agents could not only enhance

Urban Generative Intelligence A PREPRINT
performance in specific tasks but also mimic emergent properties of human societies, offering insights into complex
urban dynamics [29]. Thus, achieving full-process acceleration in LLM agent simulations remains a critical, yet
unresolved, task in urban science.
8.3 Openness of the Environment
As a foundational platform that integrates advanced technologies such as big data, simulation, and LLMs, UGI’s
capabilities are not limited to providing realistic urban environments. With UGI’s open capabilities, users can transform
their environments at will based on real cities, or even create a new city. Specifically, users can adjust AOI, POI and other
data to change the urban spatial structure, land use type, so as to change the spatial distribution of urban functions. Based
on the new urban spatial structure and functional distribution, users can use existing algorithms [124, 125, 169, 171] to
generate urban human activities under new conditions. Users are also allowed to create human activities using their
own algorithms or data sources. Besides, the city’s road network, infrastructure networks, and even the image data,
are all open and allow users to make any modifications on the copy that belongs to them. Through the openness of
the environment, we hope that UGI will not only be used to build LLM-based agents in the city, but also that it will
be able to provide a full range of intelligence for the planning, design, and governance of future cities, and promote
multidisciplinary paradigm innovation in the urban field.
8.4 Developer Community
As a topic that integrates the latest achievements in big data, urban simulation, LLMs and other fields, the development
of UGI requires the collaboration of researchers and developers in multiple fields. This requires the establishment of a
multi-disciplinary collaborative UGI developer community. In the community, researchers in the field of big data can
share their data sets, data processing methods, and data generation methods to provide high-quality data streams for
UGI. People interested in urban simulation can add new functions to the open infrastructure, improve its computing
performance, and design more reasonable interfaces. Large language model researchers can provide insights for the
training of CityGPT. Researchers in urban-related fields, such as urban planning, traffic management, economics, etc.,
can build their own agents that solve domain-specific problems through programming or natural language interface. The
community will be a highly interdisciplinary community that will inspire many interesting ideas and research questions,
help solve urban problems, and achieve smart and sustainable urban development.
9 Conclusion
In conclusion, Urban Generative Intelligence (UGI) marks a significant advancement in the field of city science
and urban computing, bridging the gap between cutting-edge technological capabilities and practical urban system
applications. By innovatively integrating Large Language Models (LLMs) with urban data and digital twins, UGI
provides a nuanced, dynamic platform for the development and deployment of embodied agents with human-level
intelligence. These agents, empowered by CityGPT, are adept at addressing diverse urban challenges, offering insights
and solutions across social, economic, and environmental dimensions. This foundational platform not only propels
forward the field of urban science but also sets new paradigm of generative intelligence in urban space. UGI’s
comprehensive approach to modeling complex urban systems heralds a new era of intelligent, sustainable, and resilient
urban development, paving the way for future cities that are more adaptive and responsive to the evolving needs of their
inhabitants.
References
[1] Alberto Acerbi and Joseph M Stubbersfield. Large language models show human-like content biases in
transmission chain experiments. Proceedings of the National Academy of Sciences, 120(44):e2313790120, 2023.
[2] Michele Acuto, Susan Parnell, and Karen C Seto. Building a global urban science. Nature Sustainability,
1(1):2–4, 2018.
[3] Gati V Aher, Rosa I Arriaga, and Adam Tauman Kalai. Using large language models to simulate multiple
humans and replicate human subject studies. In International Conference on Machine Learning, pages 337–371.
PMLR, 2023.
[4] Reza Yazdani Aminabadi, Samyam Rajbhandari, Ammar Ahmad Awan, Cheng Li, Du Li, Elton Zheng, Olatunji
Ruwase, Shaden Smith, Minjia Zhang, Jeff Rasley, et al. Deepspeed-inference: enabling efficient inference of
transformer models at unprecedented scale. In SC22: International Conference for High Performance Computing,
Networking, Storage and Analysis, pages 1–15. IEEE, 2022.
22

Urban Generative Intelligence A PREPRINT
[5] Gary An, Qi Mi, Joyeeta Dutta-Moscato, and Yoram Vodovotz. Agent-based models in translational systems
biology. Wiley Interdisciplinary Reviews: Systems Biology and Medicine, 1(2):159–171, 2009.
[6] Apple. Apple vision, 2022.
[7] Peter Ardhianto, Yonathan Purbo Santosa, Christian Moniaga, Maya Putri Utami, Christine Dewi, Henoch Juli
Christanto, Abbott Po Shun Chen, et al. Generative deep learning for visual animation in landscapes design.
Scientific Programming, 2023, 2023.
[8] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei
Huang, et al. Qwen technical report. arXiv preprint arXiv:2309.16609, 2023.
[9] Michael Batty. The size, scale, and shape of cities. science, 319(5864):769–771, 2008.
[10] Michael Batty. The new science of cities. MIT press, 2013.
[11] Michael Batty. Digital twins, 2018.
[12] Michael Batty and Paul A Longley. Fractal cities: a geometry of form and function. Academic press, 1994.
[13] Mike Batty, Paul Longley, and Stewart Fotheringham. Urban growth and form: scaling, fractal geometry, and
diffusion-limited aggregation. Environment and planning A, 21(11):1447–1472, 1989.
[14] Jean Baudrillard. Simulacra and simulation. University of Michigan press, 1994.
[15] Alan R Berkowitz, Charles H Nilon, and Karen S Hollweg. Understanding urban ecosystems: a new frontier for
science and education. Springer Science & Business Media, 2003.
[16] Luís MA Bettencourt. The origins of scaling in cities. science, 340(6139):1438–1441, 2013.
[17] Luís MA Bettencourt. Introduction to urban science: evidence and theory of cities as complex systems. 2021.
[18] Luís MA Bettencourt, José Lobo, Dirk Helbing, Christian Kühnert, and Geoffrey B West. Growth, innovation,
scaling, and the pace of life in cities. Proceedings of the national academy of sciences, 104(17):7301–7306,
2007.
[19] Wendong Bi, Xueqi Cheng, Bingbing Xu, Xiaoqian Sun, Li Xu, and Huawei Shen. Bridged-gnn: Knowledge
bridge learning for effective knowledge transfer. arXiv preprint arXiv:2308.09499, 2023.
[20] Timothy Binkley. The vitality of digital creation. The journal of aesthetics and art criticism, 55(2):107–116,
1997.
[21] Michael J Breheny. Practical methods of retail location analysis: a review. Store choice, store location and
market analysis, pages 39–86, 1988.
[22] Christa Brelsford, José Lobo, Joe Hand, and Luís MA Bettencourt. Heterogeneity and scale of sustainable
development in cities. Proceedings of the National Academy of Sciences, 114(34):8963–8968, 2017.
[23] Christa Brelsford, Taylor Martin, Joe Hand, and Luís MA Bettencourt. Toward cities without slums: Topology
and the spatial evolution of neighborhoods. Science advances, 4(8):eaar4644, 2018.
[24] William A Brock and Cars H Hommes. Heterogeneous beliefs and routes to chaos in a simple asset pricing
model. Journal of Economic dynamics and Control, 22(8-9):1235–1274, 1998.
[25] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners.
Advances in neural information processing systems, 33:1877–1901, 2020.
[26] Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter Lee,
Yin Tat Lee, Yuanzhi Li, Scott Lundberg, et al. Sparks of artificial general intelligence: Early experiments with
gpt-4. arXiv preprint arXiv:2303.12712, 2023.
[27] Howard Butler, Martin Daly, Allan Doyle, Sean Gillies, Stefan Hagen, and Tim Schaub. The geojson format.
Technical report, 2016.
[28] Francesco Calabrese, Laura Ferrari, and Vincent D Blondel. Urban sensing using mobile phone network data: a
survey of research. Acm computing surveys (csur), 47(2):1–20, 2014.
[29] G Caldarelli, E Arcaute, M Barthelemy, M Batty, C Gershenson, D Helbing, S Mancuso, Y Moreno, JJ Ramasco,
C Rozenblat, et al. The role of complexity for digital twins of cities. Nature Computational Science, pages 1–8,
2023.
[30] Andrea Capponi, Claudio Fiandrino, Burak Kantarci, Luca Foschini, Dzmitry Kliazovich, and Pascal Bouvry.
A survey on mobile crowdsensing systems: Challenges, solutions, and opportunities. IEEE communications
surveys & tutorials, 21(3):2419–2465, 2019.
23

Urban Generative Intelligence A PREPRINT
[31] Melvin Chen. The philosophy of the metaverse. Ethics and Information Technology, 25(3):41, 2023.
[32] Zhoujun Cheng, Jungo Kasai, and Tao Yu. Batch prompting: Efficient inference with large language model apis.
arXiv preprint arXiv:2301.08721, 2023.
[33] Lawrence J Christiano, Martin Eichenbaum, and Charles L Evans. Nominal rigidities and the dynamic effects of
a shock to monetary policy. Journal of political Economy, 113(1):1–45, 2005.
[34] Dixuan Cui and Christos Mousas. Evaluating the sense of embodiment through out-of-body experience and
tactile feedback. In Proceedings of the 18th ACM SIGGRAPH International Conference on Virtual-Reality
Continuum and its Applications in Industry, pages 1–7, 2022.
[35] Ganqu Cui, Lifan Yuan, Ning Ding, Guanming Yao, Wei Zhu, Yuan Ni, Guotong Xie, Zhiyuan Liu, and Maosong
Sun. Ultrafeedback: Boosting language models with high-quality feedback. arXiv preprint arXiv:2310.01377,
2023.
[36] Cheng Deng, Tianhang Zhang, Zhongmou He, Qiyuan Chen, Yuanyuan Shi, Le Zhou, Luoyi Fu, Weinan
Zhang, Xinbing Wang, Chenghu Zhou, et al. Learning a foundation language model for geoscience knowledge
understanding and utilization. arXiv preprint arXiv:2306.05064, 2023.
[37] Srinivas Devarakonda, Parveen Sevusu, Hongzhang Liu, Ruilin Liu, Liviu Iftode, and Badri Nath. Real-time
air quality monitoring through mobile sensing in metropolitan areas. In Proceedings of the 2nd ACM SIGKDD
international workshop on urban computing, pages 1–8, 2013.
[38] Ersin Dincelli and Alper Yayla. Immersive virtual reality in the age of the metaverse: A hybrid-narrative review
based on the technology affordance perspective. The Journal of Strategic Information Systems, 31(2):101717,
2022.
[39] Ning Ding, Yulin Chen, Bokai Xu, Yujia Qin, Zhi Zheng, Shengding Hu, Zhiyuan Liu, Maosong Sun, and Bowen
Zhou. Enhancing chat language models by scaling high-quality instructional conversations. arXiv preprint
arXiv:2305.14233, 2023.
[40] Danny Driess, Fei Xia, Mehdi SM Sajjadi, Corey Lynch, Aakanksha Chowdhery, Brian Ichter, Ayzaan Wahid,
Jonathan Tompson, Quan Vuong, Tianhe Yu, et al. Palm-e: An embodied multimodal language model. arXiv
preprint arXiv:2303.03378, 2023.
[41] Sean C Duncan. Minecraft, beyond construction and survival. 2011.
[42] David Eppstein. Finding the k shortest paths. SIAM Journal on computing, 28(2):652–673, 1998.
[43] Patrick Esser, Johnathan Chiu, Parmida Atighehchian, Jonathan Granskog, and Anastasis Germanidis. Structure
and content-guided video synthesis with diffusion models. In Proceedings of the IEEE/CVF International
Conference on Computer Vision, pages 7346–7356, 2023.
[44] J Doyne Farmer and Duncan Foley. The economy needs agent-based modelling. Nature, 460(7256):685–686,
2009.
[45] Tao Fei, Zhang Chenyuan, Qi Qinglin, and Zhang He. Digital twin maturity model. Computer Integrated
Manufacturing Systems, 28(5):1–20, 2022.
[46] Jie Feng, Yong Li, Chao Zhang, Funing Sun, Fanchao Meng, Ang Guo, and Depeng Jin. Deepmove: Predicting
human mobility with attentional recurrent networks. In Proceedings of the 2018 world wide web conference,
pages 1459–1468, 2018.
[47] Jie Feng, Zeyu Yang, Fengli Xu, Haisu Yu, Mudan Wang, and Yong Li. Learning to simulate human mobility.
In Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining,
pages 3426–3433, 2020.
[48] Ragnar Fjelland. Why general artificial intelligence will not be realized. Humanities and Social Sciences
Communications, 7(1):1–9, 2020.
[49] Peng Fu, Yiming Zhang, Haobo Wang, Weikang Qiu, and Junbo Zhao. Revisiting the knowledge injection
frameworks. arXiv preprint arXiv:2311.01150, 2023.
[50] Chen Gao, Xiaochong Lan, Nian Li, Jingtao Ding, Yuan Yuan, Zhilun Zhou, Fengli Xu, and Yong Li. Large
language models empowered agent-based modeling and simulation: A survey and prospective. arXiv preprint,
2023.
[51] Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao, Jinghua Piao, Huandong Wang, Depeng Jin, and Yong
Li. S3: Social-network simulation system with large language model-empowered agents. arXiv preprint
arXiv:2307.14984, 2023.
[52] John Geanakoplos. The leverage cycle. NBER macroeconomics annual, 24(1):1–66, 2010.
24

Urban Gener
[53] Amir Ghaderi, Borhan M Sanandaji, and Faezeh G
forecasting. arXiv preprint arXiv:1707.08110, 201
[54] Nigel Gilbert and Klaus Troitzsch. Simulation for
[55] Jorge Gironás, Larry A Roesner, Lewis A Rossm
storm water management model(swmm). Environ
[56] Eg Su Goh, Mohd Shahrizal Sunar, and Ajune W
mobile augmented reality interface: A review. IEE
[57] Jiahui Gong, Qiaohong Yu, Tong Li, Haoqiang Liu
digital twin system for mobile networks with gen
Conference on Mobile Systems, Applications and S
[58] Peng Gong, Bin Chen, Xuecao Li, Han Liu, Jie Wa
Feng, et al. Mapping essential urban land use cat
Science Bulletin, 65(3):182–187, 2020.
[59] Marta C Gonzalez, Cesar A Hidalgo, and Albertpatterns. nature, 453(7196):779–782, 2008.
[60] Bin Guo, Yan Liu, Sicong Liu, Zhiwen Yu, and X
fusion of human, machine, and iot. IEEE Internet
[61] Shengnan Guo, Youfang Lin, Ning Feng, Chao
graph convolutional networks for traffic flow fore
intelligence, volume 33, pages 922–929, 2019.
[62] Marc D Hauser, Noam Chomsky, and W Tecumse
how did it evolve? science, 298(5598):1569–1579
[63] Fumio Hayashi. Econometrics. Princeton Univers
[64] David F Hendry and Jean-Francois Richard. On th
Journal of Econometrics, 20(1):3–33, 1982.
[65] Aidan Hogan, Eva Blomqvist, Michael Cochez, Cl
Kirrane, José Emilio Labra Gayo, Roberto Navi
Computing Surveys (Csur), 54(4):1–37, 2021.
[66] Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng
Lin, Liyang Zhou, Chenyu Ran, et al. Metagpt: M
arXiv preprint arXiv:2308.00352, 2023.
[67] Hanyao Huang, Ou Zheng, Dongdong Wang, Jia
Renjie Yang, Qian Zheng, et al. Chatgpt for shapi
language model. International Journal of Oral Sc
[68] Weixin Huang and Hao Zheng. Architectural draw
Proceedings of the 38th annual conference of the a
City, Mexico, pages 18–20, 2018.
[69] Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei Z
Lv, Yikai Zhang, Jiayi Lei, et al. C-eval: A multimodels. arXiv preprint arXiv:2305.08322, 2023.
[70] Shaoxiong Ji, Shirui Pan, Erik Cambria, Pekka M
Representation, acquisition, and applications. IE
33(2):494–514, 2021.
[71] Shan Jiang, Yingxiang Yang, Siddharth Gupta, Da
The timegeo modeling framework for urban mo
Academy of Sciences, 113(37):E5370–E5378, 201
[72] Cong Jin, Fengjuan Wu, Jing Wang, Yang Liu, Z
framework for concerts in metaverse. EURASIP J
2022.
[73] Dmytro Karamshuk, Anastasios Noulas, Salvato
spotting: mining online location-based services fo
ACM SIGKDD international conference on Knowl

e Intelligence A PREPRINT
deri. Deep forecast: Deep learning-based spatio-temporal
social scientist. McGraw-Hill Education (UK), 2005.
and Jennifer Davis. A new applications manual for the
tal Modelling & Software, 25(6):813–814, 2010.
Ismail. 3d object manipulation techniques in handheld
Access, 7:40581–40601, 2019.
n Zhang, Hangyu Fan, Depeng Jin, and Yong Li. Scalable
tive ai. In Proceedings of the 21st Annual International
ices, pages 610–611, 2023.
Yuqi Bai, Jingming Chen, Xi Chen, Lei Fang, Shuailong
ries in china (euluc-china): Preliminary results for 2018.
zlo Barabasi. Understanding individual human mobility
she Zhou. Crowdhmt: Crowd intelligence with the deep
hings Journal, 9(24):24822–24842, 2022.
g, and Huaiyu Wan. Attention based spatial-temporal
ing. In Proceedings of the AAAI conference on artificial
itch. The faculty of language: what is it, who has it, and
02.
Press, 2011.
ormulation of empirical models in dynamic econometrics.
ia d’Amato, Gerard De Melo, Claudio Gutierrez, Sabrina
Sebastian Neumaier, et al. Knowledge graphs. ACM
ng, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan
a programming for multi-agent collaborative framework.
in, Zijin Wang, Shengxuan Ding, Heng Yin, Chuan Xu,
he future of dentistry: the potential of multi-modal large
e, 15(1):29, 2023.
recognition and generation through machine learning. In
ciation for computer aided design in architecture, Mexico
g, Jinghan Zhang, Tangjun Su, Junteng Liu, Chuancheng
l multi-discipline chinese evaluation suite for foundation
tinen, and S Yu Philip. A survey on knowledge graphs:
transactions on neural networks and learning systems,
le Veneziano, Shounak Athavale, and Marta C González.
y without travel surveys. Proceedings of the National
an Guan, and Zhe Han. Metamgc: a music generation
nal on Audio, Speech, and Music Processing, 2022(1):31,
Scellato, Vincenzo Nicosia, and Cecilia Mascolo. Geoptimal retail store placement. In Proceedings of the 19th
e discovery and data mining, pages 793–801, 2013.

Urban Generative Intelligence A PREPRINT
[74] Zixuan Ke, Yijia Shao, Haowei Lin, Tatsuya Konishi, Gyuhak Kim, and Bing Liu. Continual pre-training of
language models. In The Eleventh International Conference on Learning Representations, 2022.
[75] Arne Kesting, Martin Treiber, and Dirk Helbing. General lane-changing model mobil for car-following models.
Transportation Research Record, 1999(1):86–94, 2007.
[76] Hakpyeong Kim, Heeju Choi, Hyuna Kang, Jongbaek An, Seungkeun Yeom, and Taehoon Hong. A systematic
review of the smart energy conservation system: From smart homes to sustainable smart cities. Renewable and
sustainable energy reviews, 140:110755, 2021.
[77] Jonghyun Kim, Youngmo Jeong, Michael Stengel, Kaan Aksit, Rachel A Albert, Ben Boudaoud, Trey Greer,
Joohwan Kim, Ward Lopes, Zander Majercik, et al. Foveated ar: dynamically-foveated augmented reality display.
ACM Trans. Graph., 38(4):99–1, 2019.
[78] Katherine A Klise, Regan Murray, and Terra Haxton. An overview of the water network tool for resilience (wntr).
2018.
[79] Ryota Kondo, Maki Sugimoto, Kouta Minamizawa, Takayuki Hoshi, Masahiko Inami, and Michiteru Kitazaki.
Illusory body ownership of an invisible body interpolated between virtual hands and feet via visual-motor
synchronicity. Scientific reports, 8(1):7541, 2018.
[80] Logan Kugler. Non-fungible tokens and the future of art. Commun. ACM, 64(9):19–20, aug 2021.
[81] Vipin Kumar and Kiran Karande. The effect of retail store environment on retailer performance. Journal of
business research, 49(2):167–181, 2000.
[82] Finn E Kydland and Edward C Prescott. Time to build and aggregate fluctuations. Econometrica: Journal of the
Econometric Society, pages 1345–1370, 1982.
[83] Ariel N. Lee, Cole J. Hunter, and Nataniel Ruiz. Platypus: Quick, cheap, and powerful refinement of llms. 2023.
[84] Lik-Hang Lee, Tristan Braud, Pengyuan Zhou, Lin Wang, Dianlei Xu, Zijun Lin, Abhishek Kumar, Carlos
Bermejo, and Pan Hui. All one needs to know about metaverse: A complete survey on technological singularity,
virtual ecosystem, and research agenda. arXiv preprint arXiv:2110.05352, 2021.
[85] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich
Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al. Retrieval-augmented generation for knowledgeintensive nlp tasks. Advances in Neural Information Processing Systems, 33:9459–9474, 2020.
[86] Fuxian Li, Jie Feng, Huan Yan, Guangyin Jin, Fan Yang, Funing Sun, Depeng Jin, and Yong Li. Dynamic
graph convolutional recurrent network for traffic prediction: Benchmark and solution. ACM Transactions on
Knowledge Discovery from Data, 17(1):1–21, 2023.
[87] Haonan Li, Yixuan Zhang, Fajri Koto, Yifei Yang, Hai Zhao, Yeyun Gong, Nan Duan, and Timothy Baldwin.
Cmmlu: Measuring massive multitask language understanding in chinese. arXiv preprint arXiv:2306.09212,
2023.
[88] Nian Li, Chen Gao, Yong Li, and Qingmin Liao. Large language model-empowered agents for simulating
macroeconomic activities. arXiv preprint arXiv:2310.10436, 2023.
[89] Nuo Li, Bin Guo, Yan Liu, Yao Jing, Yi Ouyang, and Zhiwen Yu. Commercial site recommendation based
on neural collaborative filtering. In Proceedings of the 2018 ACM International Joint Conference and 2018
International Symposium on Pervasive and Ubiquitous Computing and Wearable Computers, pages 138–141,
2018.
[90] Quannan Li, Yu Zheng, Xing Xie, Yukun Chen, Wenyu Liu, and Wei-Ying Ma. Mining user similarity based
on location history. In Proceedings of the 16th ACM SIGSPATIAL international conference on Advances in
geographic information systems, pages 1–10, 2008.
[91] Zekun Li, Wenxuan Zhou, Yao-Yi Chiang, and Muhao Chen. Geolm: Empowering language models for
geospatially grounded language understanding. arXiv preprint arXiv:2310.14478, 2023.
[92] Lucia Liu, Daniel Dugas, Gianluca Cesari, Roland Siegwart, and Renaud Dubé. Robot navigation in crowded
environments using deep reinforcement learning. In 2020 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), pages 5671–5677. IEEE, 2020.
[93] Qing Liu, Cheng Chang, Hao Shen, Shasha Cheng, Xiaoyu Li, and Ran Zheng. Research on artificial intelligence
generated audio. In Sixth International Conference on Computer Information Science and Application Technology
(CISAT 2023), volume 12800, pages 1206–1212. SPIE, 2023.
[94] Yan Liu, Bin Guo, Nuo Li, Jing Zhang, Jingmin Chen, Daqing Zhang, Yinxiao Liu, Zhiwen Yu, Sizhe Zhang,
and Lina Yao. Deepstore: An interaction-aware wide&deep model for store site recommendation with attentional
spatial embeddings. IEEE Internet of Things Journal, 6(4):7319–7333, 2019.
26

Urban Generative Intelligence A PREPRINT
[95] Yu Liu, Jingtao Ding, Yanjie Fu, and Yong Li. Urbankg: An urban knowledge graph system. ACM Transactions
on Intelligent Systems and Technology, 14(4):1–25, 2023.
[96] Yu Liu, Jingtao Ding, and Yong Li. Knowledge-driven site selection via urban knowledge graph. arXiv preprint
arXiv:2111.00787, 2021.
[97] Yin Lou, Chengyang Zhang, Yu Zheng, Xing Xie, Wei Wang, and Yan Huang. Map-matching for low-samplingrate gps trajectories. In Proceedings of the 17th ACM SIGSPATIAL international conference on advances in
geographic information systems, pages 352–361, 2009.
[98] Zhihan Lv. Generative artificial intelligence in the metaverse era. Cognitive Robotics, 2023.
[99] Larry Lyon and Robyn Driskell. The community in urban society. Waveland Press, 2011.
[100] Michael W Macy and Robert Willer. From factors to actors: Computational sociology and agent-based modeling.
Annual review of sociology, 28(1):143–166, 2002.
[101] Hernán A Makse, Shlomo Havlin, and H Eugene Stanley. Modelling urban growth patterns. Nature,
377(6550):608–612, 1995.
[102] Patrick Mannion, Jim Duggan, and Enda Howley. An experimental review of reinforcement learning algorithms
for adaptive traffic signal control. Autonomic road transport support systems, pages 47–66, 2016.
[103] Rohin Manvi, Samar Khanna, Gengchen Mai, Marshall Burke, David Lobell, and Stefano Ermon. Geollm:
Extracting geospatial knowledge from large language models. arXiv preprint arXiv:2310.06213, 2023.
[104] Adam J McLane, Christina Semeniuk, Gregory J McDermid, and Danielle J Marceau. The role of agent-based
models in wildlife ecology and management. Ecological modelling, 222(8):1544–1556, 2011.
[105] Meta. Meta quest, 2022.
[106] Norzailawati Mohd Noor, Alias Abdullah, and Mazlan Hashim. Remote sensing uav/drones and its applications
for urban areas: A review. In IOP conference series: Earth and environmental science, volume 169, page 012003.
IOP Publishing, 2018.
[107] Yao Mu, Qinglong Zhang, Mengkang Hu, Wenhai Wang, Mingyu Ding, Jun Jin, Bin Wang, Jifeng Dai, Yu Qiao,
and Ping Luo. Embodiedgpt: Vision-language pre-training via embodied chain of thought. arXiv preprint
arXiv:2305.15021, 2023.
[108] Hamed Nilforoshan, Wenli Looi, Emma Pierson, Blanca Villanueva, Nic Fishman, Yiling Chen, John Sholar,
Beth Redbird, David Grusky, and Jure Leskovec. Human mobility networks reveal increased segregation in large
cities. Nature, pages 1–7, 2023.
[109] Huansheng Ning, Hang Wang, Yujia Lin, Wenxi Wang, Sahraoui Dhelim, Fadi Farha, Jianguo Ding, and
Mahmoud Daneshmand. A survey on the metaverse: The state-of-the-art, technologies, applications, and
challenges. IEEE Internet of Things Journal, 2023.
[110] OpenAI. Introducing chatgpt. https://openai.com/blog/chatgpt, 2022. (Accessed on 01/10/2023).
[111] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human
feedback. Advances in Neural Information Processing Systems, 35:27730–27744, 2022.
[112] Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S Bernstein.
Generative agents: Interactive simulacra of human behavior. In Proceedings of the 36th Annual ACM Symposium
on User Interface Software and Technology, pages 1–22, 2023.
[113] Edmund S Phelps. Phillips curves, expectations of inflation and optimal unemployment over time. Economica,
pages 254–281, 1967.
[114] Nicholas A Phelps and Andrew M Wood. The business of location: site selection consultants and the mobilisation
of knowledge in the location decision. Journal of Economic Geography, 18(5):1023–1044, 2018.
[115] Chen Qian, Xin Cong, Cheng Yang, Weize Chen, Yusheng Su, Juyuan Xu, Zhiyuan Liu, and Maosong Sun.
Communicative agents for software development. arXiv preprint arXiv:2307.07924, 2023.
[116] Hua Xuan Qin and Pan Hui. Empowering the metaverse with generative ai: Survey and future directions. In 2023
IEEE 43rd International Conference on Distributed Computing Systems Workshops (ICDCSW), pages 85–90.
IEEE, 2023.
[117] Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D Manning, and Chelsea Finn. Direct
preference optimization: Your language model is secretly a reward model. arXiv preprint arXiv:2305.18290,
2023.
27

Urban Generative Intelligence A PREPRINT
[118] Rajib Kumar Rana, Chun Tung Chou, Salil S Kanhere, Nirupama Bulusu, and Wen Hu. Ear-phone: an end-to-end
participatory urban noise mapping system. In Proceedings of the 9th ACM/IEEE international conference on
information processing in sensor networks, pages 105–116, 2010.
[119] Bushra Rashid and Mubashir Husain Rehmani. Applications of wireless sensor networks for urban areas: A
survey. Journal of network and computer applications, 60:192–219, 2016.
[120] Jeff Rasley, Samyam Rajbhandari, Olatunji Ruwase, and Yuxiong He. Deepspeed: System optimizations enable
training deep learning models with over 100 billion parameters. In Proceedings of the 26th ACM SIGKDD
International Conference on Knowledge Discovery & Data Mining, pages 3505–3506, 2020.
[121] Anthony J Richardson, Elizabeth S Ampt, and Arnim H Meyburg. Survey methods for transport planning.
Eucalyptus Press Melbourne, 1995.
[122] Florent Robert. Analysing and understanding embodied interactions in virtual reality systems. In Proceedings of
the 2023 ACM International Conference on Interactive Media Experiences, pages 386–389, 2023.
[123] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image
synthesis with latent diffusion models. In Proceedings of the IEEE/CVF conference on computer vision and
pattern recognition, pages 10684–10695, 2022.
[124] Can Rong, Jingtao Ding, and Yong Li. An interdisciplinary survey on origin-destination flows modeling: Theory
and techniques. arXiv preprint arXiv:2306.10048, 2023.
[125] Can Rong, Jingtao Ding, Zhicheng Liu, and Yong Li. Complexity-aware large scale origin-destination network
generation via diffusion model. arXiv preprint arXiv:2306.04873, 2023.
[126] Francesco Salamone, Massimiliano Masullo, and Sergio Sibilio. Wearable devices for environmental monitoring
in the built environment: a systematic review. Sensors, 21(14):4727, 2021.
[127] Thomas C Schelling. Micromotives and macrobehavior. WW Norton & Company, 2006.
[128] Markus Schläpfer, Luís MA Bettencourt, Sébastian Grauwin, Mathias Raschke, Rob Claxton, Zbigniew Smoreda,
Geoffrey B West, and Carlo Ratti. The scaling of human interactions with city size. Journal of the Royal Society
Interface, 11(98):20130789, 2014.
[129] Ying Sheng, Lianmin Zheng, Binhang Yuan, Zhuohan Li, Max Ryabinin, Daniel Y Fu, Zhiqiang Xie, Beidi
Chen, Clark Barrett, Joseph E Gonzalez, et al. High-throughput generative inference of large language models
with a single gpu. arXiv preprint arXiv:2303.06865, 2023.
[130] Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté, Yonatan Bisk, Adam Trischler, and Matthew Hausknecht.
ALFWorld: Aligning Text and Embodied Environments for Interactive Learning. In Proceedings of the International Conference on Learning Representations (ICLR), 2021.
[131] Andrew Silva, Matthew Gombolay, Taylor Killian, Ivan Jimenez, and Sung-Hyun Son. Optimization methods
for interpretable differentiable decision trees applied to reinforcement learning. In International conference on
artificial intelligence and statistics, pages 1855–1865. PMLR, 2020.
[132] Frank Smets and Raf Wouters. An estimated dynamic stochastic general equilibrium model of the euro area.
Journal of the European economic association, 1(5):1123–1175, 2003.
[133] Chaoming Song, Tal Koren, Pu Wang, and Albert-László Barabási. Modelling the scaling properties of human
mobility. Nature physics, 6(10):818–823, 2010.
[134] Peter Stopher. Collecting, managing, and assessing data using sample surveys. Cambridge University Press,
2012.
[135] Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen, Yanbin
Zhao, Yuxiang Lu, et al. Ernie 3.0: Large-scale knowledge enhanced pre-training for language understanding
and generation. arXiv preprint arXiv:2107.02137, 2021.
[136] Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy Liang, and
Tatsunori B. Hashimoto. Stanford alpaca: An instruction-following llama model. https://github.com/
tatsu-lab/stanford_alpaca, 2023.
[137] Andrew J Tatem. Worldpop, open data for spatial demography. Scientific data, 4(1):1–4, 2017.
[138] Leigh Tesfatsion and Kenneth L Judd. Handbook of computational economics: agent-based computational
economics. Elsevier, 2006.
[139] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov,
Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models.
arXiv preprint arXiv:2307.09288, 2023.
28

Urban Generative Intelligence A PREPRINT
[140] Martin Treiber, Ansgar Hennecke, and Dirk Helbing. Congested traffic states in empirical observations and
microscopic simulations. Physical review E, 62(2):1805, 2000.
[141] Leandro von Werra, Younes Belkada, Lewis Tunstall, Edward Beeching, Tristan Thrush, Nathan Lambert, and
Shengyi Huang. Trl: Transformer reinforcement learning. https://github.com/huggingface/trl, 2020.
[142] Dong Wang, Junbo Zhang, Wei Cao, Jian Li, and Yu Zheng. When will you arrive? estimating travel time based
on deep neural networks. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 32, 2018.
[143] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anandkumar. Voyager: An open-ended embodied agent with large language models. arXiv preprint arXiv:2305.16291,
2023.
[144] Jindong Wang, Xixu Hu, Wenxin Hou, Hao Chen, Runkai Zheng, Yidong Wang, Linyi Yang, Haojun Huang,
Wei Ye, Xiubo Geng, et al. On the robustness of chatgpt: An adversarial and out-of-distribution perspective.
arXiv preprint arXiv:2302.12095, 2023.
[145] Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang,
Xu Chen, Yankai Lin, et al. A survey on large language model based autonomous agents. arXiv preprint
arXiv:2308.11432, 2023.
[146] Quan Wang, Zhendong Mao, Bin Wang, and Li Guo. Knowledge graph embedding: A survey of approaches and
applications. IEEE Transactions on Knowledge and Data Engineering, 29(12):2724–2743, 2017.
[147] Yilun Wang, Yu Zheng, and Yexiang Xue. Travel time estimation of a path using sparse trajectories. In
Proceedings of the 20th ACM SIGKDD international conference on Knowledge discovery and data mining, pages
25–34, 2014.
[148] Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A Smith, Daniel Khashabi, and Hannaneh Hajishirzi. Self-instruct: Aligning language model with self generated instructions. arXiv preprint arXiv:2212.10560,
2022.
[149] Hua Wei, Nan Xu, Huichu Zhang, Guanjie Zheng, Xinshi Zang, Chacha Chen, Weinan Zhang, Yanmin Zhu, Kai
Xu, and Zhenhui Li. Colight: Learning network-level cooperation for traffic signal control. In Proceedings of the
28th ACM International Conference on Information and Knowledge Management, pages 1913–1922, 2019.
[150] Hua Wei, Guanjie Zheng, Huaxiu Yao, and Zhenhui Li. Intellilight: A reinforcement learning approach for
intelligent traffic light control. In Proceedings of the 24th ACM SIGKDD International Conference on Knowledge
Discovery & Data Mining, pages 2496–2505, 2018.
[151] Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten
Bosma, Denny Zhou, Donald Metzler, et al. Emergent abilities of large language models. arXiv preprint
arXiv:2206.07682, 2022.
[152] Margaret Wilson. Six views of embodied cognition. Psychonomic bulletin & review, 9:625–636, 2002.
[153] Stephen Wolfram. Statistical mechanics of cellular automata. Reviews of modern physics, 55(3):601, 1983.
[154] Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang, Junzhe Wang, Senjie
Jin, Enyu Zhou, et al. The rise and potential of large language model based agents: A survey. arXiv preprint
arXiv:2309.07864, 2023.
[155] Can Xu, Qingfeng Sun, Kai Zheng, Xiubo Geng, Pu Zhao, Jiazhan Feng, Chongyang Tao, and Daxin Jiang.
Wizardlm: Empowering large language models to follow complex instructions. arXiv preprint arXiv:2304.12244,
2023.
[156] Fengli Xu, Yong Li, Depeng Jin, Jianhua Lu, and Chaoming Song. Emergence of urban growth patterns from
human mobility behavior. Nature Computational Science, 1(12):791–800, 2021.
[157] Mengwen Xu, Tianyi Wang, Zhengwei Wu, Jingbo Zhou, Jian Li, and Haishan Wu. Demand driven store site
selection via multiple spatial-temporal data. In Proceedings of the 24th acm sigspatial international conference
on advances in geographic information systems, pages 1–10, 2016.
[158] Takahiro Yamada, Toshimitsu Tanaka, and Yuji Sagawa. One-handed character input method without screen
cover for smart glasses that does not require visual confirmation of fingertip position. In International Conference
on Human-Computer Interaction, pages 603–614. Springer, 2023.
[159] Aiyuan Yang, Bin Xiao, Bingning Wang, Borong Zhang, Chao Yin, Chenxu Lv, Da Pan, Dian Wang, Dong Yan,
Fan Yang, et al. Baichuan 2: Open large-scale language models. arXiv preprint arXiv:2309.10305, 2023.
[160] Linyao Yang, Hongyang Chen, Zhao Li, Xiao Ding, and Xindong Wu. Chatgpt is not enough: Enhancing large
language models with knowledge graphs for fact-aware language modeling. arXiv preprint arXiv:2306.11489,
2023.
29

Urban Generative Intelligence A PREPRINT
[161] Xiaojun X Yang. Urban remote sensing: monitoring, synthesis and modeling in the urban environment. John
Wiley & Sons, 2021.
[162] Huaxiu Yao, Fei Wu, Jintao Ke, Xianfeng Tang, Yitian Jia, Siyu Lu, Pinghua Gong, Jieping Ye, and Zhenhui Li.
Deep multi-view spatial-temporal network for taxi demand prediction. In Proceedings of the AAAI conference on
artificial intelligence, volume 32, 2018.
[163] Jeremy YL Yap, Chiung Ching Ho, and Choo-Yee Ting. Analytic hierarchy process (ahp) for business site
selection. In AIP Conference Proceedings, volume 2016. AIP Publishing, 2018.
[164] Hyejin Youn, Luís MA Bettencourt, José Lobo, Deborah Strumsky, Horacio Samaniego, and Geoffrey B
West. Scaling and universality in urban economic diversification. Journal of The Royal Society Interface,
13(114):20150937, 2016.
[165] Biao Yuan, Zengde Deng, Na Geng, Yujie Chen, and Haoyuan Hu. Practice summary: Cainiao optimizes the
fulfillment routes of parcels. INFORMS Journal on Applied Analytics, 2023.
[166] Jing Yuan, Yu Zheng, and Xing Xie. Discovering regions of different functions in a city using human mobility
and pois. In Proceedings of the 18th ACM SIGKDD international conference on Knowledge discovery and data
mining, pages 186–194, 2012.
[167] Jing Yuan, Yu Zheng, Chengyang Zhang, Wenlei Xie, Xing Xie, Guangzhong Sun, and Yan Huang. T-drive:
driving directions based on taxi trajectories. In Proceedings of the 18th SIGSPATIAL International conference on
advances in geographic information systems, pages 99–108, 2010.
[168] Yuan Yuan, Jingtao Ding, Huandong Wang, Depeng Jin, and Yong Li. Activity trajectory generation via modeling
spatiotemporal dynamics. In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and
Data Mining, pages 4752–4762, 2022.
[169] Yuan Yuan, Jingtao Ding, Huandong Wang, Depeng Jin, and Yong Li. Activity trajectory generation via modeling
spatiotemporal dynamics. In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and
Data Mining, pages 4752–4762, 2022.
[170] Yuan Yuan, Huandong Wang, Jingtao Ding, Depeng Jin, and Yong Li. Learning to simulate daily activities via
modeling dynamic human needs. arXiv preprint arXiv:2302.10897, 2023.
[171] Yuan Yuan, Huandong Wang, Jingtao Ding, Depeng Jin, and Yong Li. Learning to simulate daily activities via
modeling dynamic human needs. In Proceedings of the ACM Web Conference 2023, WWW ’23, page 906–916,
New York, NY, USA, 2023. Association for Computing Machinery.
[172] Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang, Hanyu Lai, Ming Ding, Zhuoyi Yang, Yifan Xu, Wendi
Zheng, Xiao Xia, et al. Glm-130b: An open bilingual pre-trained model. In The Eleventh International
Conference on Learning Representations, 2023.
[173] Guozhen Zhang, Zihan Yu, Depeng Jin, and Yong Li. Physics-infused machine learning for crowd simulation. In
Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, pages 2439–2449,
2022.
[174] Hongxin Zhang, Weihua Du, Jiaming Shan, Qinhong Zhou, Yilun Du, Joshua B Tenenbaum, Tianmin Shu, and
Chuang Gan. Building cooperative embodied agents modularly with large language models. arXiv preprint
arXiv:2307.02485, 2023.
[175] Jun Zhang, Wenxuan Ao, Depeng Jin, Li Liu, and Yong Li. A city-level high-performance spatio-temporal
mobility simulation system. 2023.
[176] Jun Zhang, Depeng Jin, and Yong Li. Mirage: an efficient and extensible city simulation framework (systems
paper). In Proceedings of the 30th International Conference on Advances in Geographic Information Systems,
pages 1–4, 2022.
[177] Junbo Zhang, Yu Zheng, and Dekang Qi. Deep spatio-temporal residual networks for citywide crowd flows
prediction. In Proceedings of the AAAI conference on artificial intelligence, volume 31, 2017.
[178] Mingyang Zhang, Haohao Fu, Yong Li, and Sheng Chen. Understanding urban dynamics from massive mobile
traffic data. IEEE Transactions on Big Data, 5(2):266–278, 2017.
[179] Siyao Zhang, Daocheng Fu, Zhao Zhang, Bin Yu, and Pinlong Cai. Trafficgpt: Viewing, processing and
interacting with traffic foundation models. arXiv preprint arXiv:2309.06719, 2023.
[180] Xiaotian Zhang, Chunyang Li, Yi Zong, Zhengyu Ying, Liang He, and Xipeng Qiu. Evaluating the performance
of large language models on gaokao benchmark. arXiv preprint arXiv:2305.12474, 2023.
[181] Yifan Zhang, Cheng Wei, Shangyou Wu, Zhengting He, and Wenhao Yu. Geogpt: Understanding and processing
geospatial tasks through an autonomous gpt. arXiv preprint arXiv:2307.07930, 2023.
30

Urban Gener
[182] Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang
Junjie Zhang, Zican Dong, et al. A survey of large
[183] Stephan Zheng, Alexander Trott, Sunil Srinivasa
Taxation policy design via two-level deep multiage
2022.
[184] Yu Zheng, Licia Capra, Ouri Wolfson, and Hai
applications. ACM Transactions on Intelligent Sys
[185] Yu Zheng, Quannan Li, Yukun Chen, Xing Xie, a
In Proceedings of the 10th international conferenc
[186] Yu Zheng, Yuming Lin, Liang Zhao, Tinghai W
communities via deep reinforcement learning. Na
[187] Yu Zheng, Yanchi Liu, Jing Yuan, and Xing Xie.
international conference on Ubiquitous computing
[188] Yu Zheng, Xing Xie, Wei-Ying Ma, et al. Geolife: A
and trajectory. IEEE Data Eng. Bull., 33(2):32–39
[189] Yu Zheng, Lizhu Zhang, Xing Xie, and Wei-Ying
gps trajectories. In Proceedings of the 18th interna
[190] Xuhui Zhou, Hao Zhu, Leena Mathur, Ruohong
Yonatan Bisk, Daniel Fried, Graham Neubig, et
language agents. arXiv preprint arXiv:2310.11667
[191] Yu Zhou and Chuncheng Liu. The logic and innova
Development Studies, 25(10):60–67, 2018.
[192] Xunyu Zhu, Jian Li, Yong Liu, Can Ma, and Weipi
models. arXiv preprint arXiv:2308.07633, 2023.
[193] Mingchen Zhuge, Haozhe Liu, Francesco Faccio
Abdullah Hamdi, Hasan Abed Al Kader Hammoud
language-based societies of mind. arXiv preprint a

e Intelligence A PREPRINT
aolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang,
guage models. arXiv preprint arXiv:2303.18223, 2023.
avid C Parkes, and Richard Socher. The ai economist:
einforcement learning. Science advances, 8(18):eabk2607,
ng. Urban computing: concepts, methodologies, and
s and Technology (TIST), 5(3):1–55, 2014.
Wei-Ying Ma. Understanding mobility based on gps data.
n Ubiquitous computing, pages 312–321, 2008.
Depeng Jin, and Yong Li. Spatial planning of urban
Computational Science, pages 1–15, 2023.
an computing with taxicabs. In Proceedings of the 13th
ges 89–98, 2011.
llaborative social networking service among user, location
10.
. Mining interesting locations and travel sequences from
nal conference on World wide web, pages 791–800, 2009.
ng, Haofei Yu, Zhengyang Qi, Louis-Philippe Morency,
Sotopia: Interactive evaluation for social intelligence in
023.
of building digital twin city in xiong’an new area. Urban
Wang. A survey on model compression for large language
ylan R Ashley, Róbert Csordás, Anand Gopalakrishnan,
ncent Herrmann, Kazuki Irie, et al. Mindstorms in natural
v:2305.17066, 2023.
