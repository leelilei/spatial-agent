---
telephone_index: 17
title: "AgentScope: A Flexible yet Robust Multi-Agent Platform"
category: 01_agent_societies
venue: "arXiv"
year: 2024
doi: 
arxiv_id: 2402.14034
preferred_source_type: preprint_or_unresolved
publisher_url: https://arxiv.org/abs/2402.14034
quality_flags: []
---

# Citation Context

- Telephone index: 17
- Preferred source: arXiv
- DOI: none
- arXiv: 2402.14034
- PDF: `assets\papers\pdf\01_agent_societies\17_agentscope-a-flexible-yet-robust-multi-agent-platform.pdf`

## Extracted Abstract

With the rapid advancement of Large Language Models (LLMs), significant progress has been made in multi-agent applications. However, the complexities in coordinating agents’ cooperation and LLMs’ erratic performance pose notable challenges in developing robust and efficient multi-agent applications. To tackle these challenges, we propose AgentScope, a developer-centric multi-agent platform with message exchange as its core communication mechanism. The abundant syntactic tools, built-in agents and service functions, user-friendly interfaces for application demonstration and utility monitor, zero-code programming workstation, and automatic prompt tuning mechanism significantly lower the barriers to both development and deployment. Towards robust and flexible multi-agent application, AgentScope provides both built-in and customizable fault tolerance mechanisms. At the same time, it is also armed with system-level support for managing and utilizing multi-modal data, tools, and external knowledge. Additionally, we design an actor-based distribution framework, enabling easy conversion between local and distributed deployments and automatic parallel optimization without extra effort. With these features, AgentScope empowers developers to build applications that fully realize the potential of intelligent agents. We have released AgentScope at https://github.com/modelscope/agentscope, and hope AgentScope invites wider participation and innovation in this fast-moving field.
Title: Introduction

Source PDF: D:\0-Research\5-Telephone\assets\papers\pdf\01_agent_societies\17_agentscope-a-flexible-yet-robust-multi-agent-platform.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-06-20T12:40:44+00:00
- page_count: 37
- status: ok
- text_char_count: 117038

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Overview (page 4)
  - Basic Concepts in AgentScope (page 4)
  - Architecture of AgentScope (page 5)
- High Usability (page 6)
  - Syntactic Sugar for Multi-Agent Workflows (page 6)
  - Resource-Rich Environment for Agent Development (page 7)
  - Multi-Agent Oriented Demonstration Interfaces (page 8)
  - Towards Graphical Application Development (page 10)
  - Automatic Prompt Tuning (page 11)
- Fault-Tolerant Mechanisms (page 12)
- Multi-Modal Applications (page 13)
- Tool Usage (page 15)
  - Customization for Experienced Developers (page 16)
- Agents with Retrieval-Augmented Generation (page 17)
- Actor-based Distributed Framework (page 18)
- Signature Applications of AgentScope (page 21)
  - Dialog Agents: Basic Conversation (page 21)
  - Dialog Agents: Group Conversation with Mentions (page 21)
  - Dialog Agents: The Werewolf Game (page 22)
  - Distributed Deployed Agents (page 23)
  - RAG Agents: AgentScope Copilot (page 24)
  - Web Search and Retrieve Agents (page 25)
  - ReAct Agents: Convert Natural Language to SQL Query (page 26)
  - AgentScope Workstation (page 27)
- Related Works (page 28)
- Conclusion (page 30)
- Running Example of Standalone Conversation (page 34)
- Running Example of Werewolf (page 34)

Markdown Content:

AgentScope: A Flexible yet Robust Multi-Agent Platform
Dawei Gao†, Zitao Li†, Xuchen Pan∗, Weirui Kuang∗, Zhijian Ma∗, Bingchen Qian∗,
Fei Wei∗, Wenhao Zhang∗, Yuexiang Xie∗, Daoyuan Chen∗,
Liuyi Yao, Hongyi Peng, Zeyu Zhang, Lin Zhu, Chen Cheng, Hongzhu Shi,
Yaliang Li‡, Bolin Ding‡, Jingren Zhou
Alibaba Group
Abstract
With the rapid advancement of Large Language Models (LLMs), significant progress has been made
in multi-agent applications. However, the complexities in coordinating agents’ cooperation and LLMs’
erratic performance pose notable challenges in developing robust and efficient multi-agent applications.
To tackle these challenges, we propose AgentScope, a developer-centric multi-agent platform with
message exchange as its core communication mechanism. The abundant syntactic tools, built-in agents
and service functions, user-friendly interfaces for application demonstration and utility monitor, zero-code
programming workstation, and automatic prompt tuning mechanism significantly lower the barriers to
both development and deployment. Towards robust and flexible multi-agent application, AgentScope
provides both built-in and customizable fault tolerance mechanisms. At the same time, it is also armed
with system-level support for managing and utilizing multi-modal data, tools, and external knowledge.
Additionally, we design an actor-based distribution framework, enabling easy conversion between local and
distributed deployments and automatic parallel optimization without extra effort. With these features,
AgentScope empowers developers to build applications that fully realize the potential of intelligent agents.
We have released AgentScope at https://github.com/modelscope/agentscope, and hope AgentScope
invites wider participation and innovation in this fast-moving field.
1 Introduction
Multi-agent systems, as upgraded extensions of single-agent systems, require collaborative efforts from multiple
agents working in concert (Wang et al., 2023; Xi et al., 2023). With the advancement of Large Language
Models (LLMs) (Ouyang et al., 2022; OpenAI, 2023; Touvron et al., 2023a,b), multi-agent applications have
made great progress in both research and industrial communities, including software engineering (Hong et al.,
2023), society simulation (Park et al., 2023), and intelligent assistant (Wu et al., 2023; AutoGPT-Team,
2023). Although significant progress has been made in multi-agent scenarios, there are still major challenges
remaining in multi-agent application development.
Developing a multi-agent application is more complex than creating a single-agent one. Unlike single-agent
setups where an agent solely interacts with users, the development in the multi-agent scenario requires careful
creation and management of multiple models and agents (Wang et al., 2023; Xi et al., 2023), which poses high
requirements for both versatility and handiness for a platform. In particular, the following aspects feature the
challenges: 1) Agents involved in a multi-agent application can specialize at different functions via different
initial configurations; 2) A multi-agent application may require agents to be executed in a standardized
operating procedure (SOP) or a more dynamic workflow; 3)The communication pattern between agents can
be varying from one-to-one or broadcasting (e.g., a discussion group of agents). As a result, developers expect
a handy platform that can provide concise and clear programming patterns when taking care of all the aspects
above, accelerating and facilitating the development cycle. Achieving versatility and handiness simultaneously
†Co-first authors.
∗Equal contribution.
‡Corresponding authors, email address: {yaliang.li, bolin.ding}@alibaba-inc.com
1
4202
yaM
02
]AM.sc[
2v43041.2042:viXra

requires careful design and taking trade-offs, and it
designs.
Aberrations are tinderboxs in a multi-agent syst
struggle with issues like hallucination (Rawte et al.,
following (Fu et al., 2019; Zhang et al., 2023a). Bes
those tools introduce additional uncertainties (e.g.,
the perspective of multi-agent system robustness, a
whole system, causing a series of cascading effects if
applications to autonomously detect and handle unex
identifying and managing these errors, it remains a c
their own and to automatically provide the necessary
fault-tolerant that incorporate LLMs is a key challe
Supporting agents with multi-modal data, tools,
generating answers with LLMs, agents are expected
multi-modal data (Su et al., 2023; Betker et al., 2
et al., 2023; Shen et al., 2024), managing external k
augmentation generation (Lewis et al., 2020a). Ho
applications requires a comprehensive and systematic
endeavor, necessitating considerations for data stora
and communication. Tool utilization of agents req
parsing, prompting to instruct LLMs, and design
accomplished step by step. As for external knowled
techniques, we need to consider how to efficiently sh
while leaving enough flexibility for retrieval strateg
techniques individually work within specialized agent
remain absent.
Distributed applications bring extra programming
oriented scenario for multi-agent applications is th
run on different machines because the agents are equ
Developing such applications usually requires the d
system programming and optimization in the design
a great extra effort in the development and testing,
across distributed processes or agents. Moreover,
processing poses additional challenges in a distribu
accomplish the sub-tasks or the generated contents
can result in excessive communication overhead betw
applications requires the large efforts of experienced
their prototypes to a distributed style for optimal effi
To tackle the aforementioned challenges, we in
designed for developers with varying levels of experti
communication mechanism that embodies great us
salient features of AgentScope as follows:
Exceptional Usability for Developers. Agen
of use, particularly for developers with varying leve
message exchange mechanism, AgentScope ensure
development. To alleviate the programming burd
utilities, including various pipelines and an informat
framework, we also improve usability by providing a
can enable those with limited Python programmin
effort. Compared with building the skeleton of the ap
stage in multi-agent application development. In A
prompt tuning mechanisms to relieve such burden. C
interaction modules, AgentScope makes building a m
Robust Fault Tolerance for Diverse LLMs

mains a persistent goal for all multi-agent platform
. Although LLMs have advanced rapidly, they still
23; Zhang et al., 2023b) and inadequate instructions, an agent can be equipped with various tools, but
essibility to a database or the search engine). From
unexpected error or response can propagate to the
handled properly. Thus, it is crucial for multi-agent
ted responses from LLMs. While LLMs may assist in
enge to determine whether they can resolve errors on
rmation for error correction. Consequently, designing
in the development of multi-agent applications.
d external knowledge is highly systematic. Besides
be more versatile, including generating and handling
3), preparing and invoking functions as tools (Yao
wledge banks, and using the retrieved knowledge for
ver, integrating these functionalities in multi-agent
proach. Supporting multi-modal content is a complex
presentation, user interaction, message transmission,
es unifying the function calling pattern and output
reasoning mechanisms to ensure the tasks can be
beyond the retrieval-augmented generation (RAG)
and manage the knowledge in multi-agent scenarios
While some existing works investigate how those
stems, general platform-level programming interfaces
fficulties and system design challenges. An industrialhe agents are owned by different organizations and
ped with unique private knowledge or patented tools.
opers to have professional knowledge of distributed
ase. Besides, distributed applications usually require
ecially when debugging and diagnosing issues spread
tegrating advanced features like multi-modal data
setting, when the agents require different time to
very heterogeneous. Poor distributed system design
n agents. Therefore, building distributed multi-agent
velopers and a high barrier for beginners to migrate
ency.
duce AgentScope, a novel multi-agent platform
AgentScope is well-designed with a message exchange
lity, robustness, and efficiency. We underscore the
ope is designed with a fundamental emphasis on ease
of expertise. By implementing a procedure-oriented
smooth learning curve on multi-agent application
AgentScope offers an extensive suite of syntactic
-sharing mechanism. Besides programming with our
-code drag-and-drop programming workstation, which
xperience to build their own applications with little
cation, prompt tuning can be a more time-consuming
tScope, we equip our agents with a set of automatic
pled with rich built-in resources and integrated user
ti-agent application much more enjoyable than ever.
d APIs. As the scale and scope of models and APIs

expand, a robust fault-tolerance mechanism in mul
integrates a comprehensive service-level retry mechan
with a set of rule-based correction tools to handle som
Moreover, AgentScope offers customizable fault tole
own fault tolerance mechanism through parameter
While admittedly, not all the errors can be handled
system with customized features for multi-agent app
Extensive Compatibility for Multi-Modal, T
progress of large-scale multi-modal models, AgentSco
and videos) in dialog conversation, message transmiss
multi-modal data transmission from storage and emp
based attribute in messages. During message transm
and the multi-modal data is loaded only when neces
by model wrappers. For tool usage, AgentScope pro
solution for tool usage, including function preprocess
with fault-tolerance features. To support efficient ext
highly configurable, and sharable knowledge process
from data preprocessing to customizable retrieval.
Optimized Efficiency for Distributed Multidistributed deployment, AgentScope introduces an ac
programming of complex distributed workflows, a
workflows for local and distributed deployments is a e
migrating applications between centralized and distrib
AgentScope empowers developers to concentrate on t
Summary To summarize, AgentScope, a novel mu
includes the following advanced features:
1. AgentScope provides a procedure-oriented mess
to facilitate multi-agent programming, a zero-c
of automatic prompt tuning mechanisms.
2. The fault tolerance designs of AgentScope e
applications.
3. The support for the multi-modal applications
and transmission. The service toolkit compone
the knowledge processing modules provide a fle
4. The actor-based distributed mode of AgentSc
multi-agent applications seamlessly.
Roadmap In the following sections, we navigate thr
showcasing its role in advancing the development a
provides an overview, while Section 3 focuses on the
mechanism in AgentScope. Sections 5, 6, and 7 co
augmented generation modules in AgentScope. Sec
multi-agent applications. Use cases are presented in
concluding thoughts are recorded in Section 11.

gent applications becomes paramount. AgentScope
to maintain API reliability. AgentScope is equipped
bvious formatting problems in the responses of LLMs.
ce configurations, enabling developers to tailor their
ke parse_func, fault_handler, and max_retries.
he aforementioned mechanism, we propose a logging
ations as the last safeguard for AgentScope.
s, and External Knowledge. With the remarkable
supports multi-modal data (e.g., texts, images, audio,
and data storage. Specifically, AgentScope decouples
s a lazy loading strategy by providing a unified URLon, AgentScope only attaches a URL to the message,
y, such as when being rendered in web UI or invoked
es a component, called service toolkit, as a one-step
prompt engineering, reasoning, and response parsing
al knowledge usage, AgentScope provides end-to-end,
modules for retrieval-augmented generation (RAG),
ent Operations. Recognizing the vital importance of
based distributed mechanism that enables centralized
automatic parallel optimization. Particularly, the
tly the same one, indicating negligible overhead when
ed environments. With such a distribution framework,
application design rather than implementation details.
gent platform proposed for flexibility and robustness,
exchange mechanism with a set of syntactic features
drag-and-drop programming workstation, and a set
ble developers to handle errors elegantly for their
uces the overheads of heterogeneous data generation
acilitates the tool usage of agents in AgentScope, and
le solution for agents to handle different information.
e can help develop efficient and reliable distributed
h the core components and capabilities of AgentScope,
deployment of multi-agent applications. Section 2
r experience. Section 4 introduces the fault tolerance
the multi-modal support, tool usage, and retrievaln 8 presents our platform’s support for distributed
ion 9, related work is summarized in Section 10, and

2 Overview
2.1 Basic Concepts in AgentScope
This section introduces the primary concepts in Age
four concepts are throughout the platform and all m
• Message: Messages serve as the carriers fo
encapsulating the source and content of the inf
Python dictionaries with two mandatory field
name field records the name of the agent that g
text-based information generated by the agent
Locator (URL), which typically links to multi-m
field are particularly relevant for interactions
content. Each message is uniquely identified
traceability. Example 1 shows how the messa
communication of AgentScope.
1 from agentscope . message import Msg
2
3 msg1 = Msg (" Alice ", " Hello !")
4 msg2 = Msg (
5 name =" Bob ",
6 content =" How do you find this pic
7 url =" https :// xxx . png "
8 )
Example 1: Illustrative examples
• Agent: Agents are the primary actors with
participants and executors of tasks. In Age
interfaces: the reply and observe functions. Th
response, while the observe function processe
The interplay between agents and messages, a
AgentScope and is essential for developers to m
1 # agent1 and agent2 are two initializ
2 # agent1 , agent2 = DialogAgent (...) ,
3 msg1 = agent1 ()
4 msg2 = agent2 ( msg1 )
Example 2: Demonstration of message
• Workflow: Workflows represent ordered seque
agents, analogous to computational graphs in
non-DAG structures. Workflows define the fl
facilitating parallel execution and efficiency imp
agent systems that interact with LLMs, as it
tasks.
• Service Functions and Tools: Note that serv
concept, tools, in the context of agent design i
APIs that return a formatted output ServiceR
with functionality descriptions and necessary
concepts in AgentScope because LLMs require h
is that LLMs may need help understanding t

Scope: message, agent, service, and workflow. These
i-agent applications based on it.
nformation exchange in multi-agent conversations,
mation. In AgentScope, messages are implemented as
name and content) and an optional field (url ). The
erates the message, and the content field contains the
he url field is designed to hold the Uniform Resource
al data, such as images or videos. Messages with this
h agents that can process and generate multi-modal
an auto-generated UUID and timestamp, ensuring
can be created, serving as atoms in the inter-agent
e I captured yesterday ?",
message creation in AgentScope.
multi-agent applications, acting as conversational
cope, agent behaviors are abstracted through two
ply function takes a message as input and produces a
coming messages without generating a direct reply.
hown in Example 2, forms the operational basis of
el complex interactions in multi-agent LLMs.
agents , for example
logAgent (...)
change between agents in AgentScope.
s of agent executions and message exchanges between
nsorFlow, but with the flexibility to accommodate
of information and task processing among agents,
ements. This concept is essential for designing multiws for the coordination of complex, interdependent
functions are closely related to but different from the
AgentScope. Service functions refer to the functional
onse, while tools refer to processed services functions
put parameters prepared. We introduce these two
to invoke service functions as tools. One observation
unctionalities of the service functions precisely and

Syntactic sugar: Pipeline, message hub
Configuration Local Agent
Agent
Model
Service Function Model API
Retrieve Code Exec. FastChat
Write/Read File Web Search
DB Query
repparW/reganaM
ytilitU
File Manager
Image, Audio, Video
API Invocation
Logging History
emitnuR reganaM
Message: name/role, content, urls Actor-based Agent
GPRC Comm.
Prompt Tuning
Memory
Model Wrapper
Auto-correct
Retry Mechanism
User-defined handler
tnegA
Customized Post API
MultiAgentsLogger
AgentMonitor(Comm,Cost,Time)
WebUI
&
AS
Studio
User
Interaction
resraPesnopseR
Workstation
Drag-and-Drop
Programming
Figure 1: Architecture of AgentScope.
demand more descriptive information to make accurate decisions. Meanwhile, LLMs can not (reliably)
fill in some input parameters of the APIs, such as the API keys of Bing and Google Search. As a result,
AgentScope defines tools as processed service functions.
2.2 Architecture of AgentScope
We present AgentScope as an infrastructural platform to facilitate the creation, management, and deployment
of multi-agent applications integrated with LLMs. The architecture of AgentScope comprises three hierarchical
layers and a set of user interaction interfaces, as shown in Fig. 1. These layers provide support for multi-agent
applications from different levels, including elementary and advanced functionalities of a single agent (utility
layer), resources and runtime management (manager and wrapper layer), and agent-level to workflow-level
programming interfaces (agent layer). AgentScope introduces intuitive abstractions designed to fulfill the
diverse functionalities inherent to each layer and simplify the complicated inter-layer dependencies when
building multi-agent systems. Furthermore, we offer programming interfaces and default mechanisms to
strengthen the resilience of multi-agent systems against faults within different layers.
• Utility Layer: As the platform’s foundation, the utility layer in AgentScope provides essential services
to support the core functionalities of agents. This layer abstracts the complexity of underlying operations,
such as model API invocation and service functions including code execution and database operations,
allowing agents to focus on their primary tasks. AgentScope’s utility layer is designed with ease of
use and robustness as its utmost priority, supporting versatile operations in multi-agent systems and
providing built-in autonomous retry mechanisms for exception and error handling against unexpected
interruptions.
• Manager and Wrapper Layer: As an intermediary, the manager and wrapper abstraction layer
manages the resources and API services, ensuring high availability of resources and providing resistance
to undesired responses from LLMs. Unlike the utility layer, which provides default handlers, the
manager and wrapper layer also offers customizable interfaces for fault tolerance controls depending
on developers’ needs and the specific requirements of the application. This layer is responsible for
maintaining the operational integrity of the agents, a crucial aspect for LLMs to perform consistently
5

under diverse conditions. Detailed elaboration
4.
• Agent Layer: At the core of AgentScope lies
multi-agent workflow and is the primary entit
layer is designed to facilitate the construction o
programming burden on developers. By integra
developers to concentrate on the implementa
leverage the capabilities of LLMs. The progra
Section 3 with more details.
• User interaction: In addition to the layered
interfaces such as an annotated terminal prese
a Gradio-base (Abid et al., 2019) interface tha
one with only one step and a drag-and-drop
interfaces allow developers to effortlessly moni
agent communication, execution timing, and fi
Collectively, the layered constructs of AgentScop
craft bespoke multi-agent applications that leverage
subsequent section will delve into the features of Ag
multi-agent application development.
3 High Usability
The design of AgentScope prioritizes usability, aimin
with LLMs and to ensure a smooth interaction exper
into how AgentScope flattens the learning curve and
intuitive concepts and features that facilitate the cr
3.1 Syntactic Sugar for Multi-Agent
Leveraging basic concepts introduced in Section 2.1
multi-agent applications. Nonetheless, directly coding
as shown in Example 3. Recognizing this, AgentScope
hubs, to abstract away the complexity and minimize
1 # set up agents : agent1 to agent5
2 # ...
3
4 msg = agent1 ( Msg ( " Alice " , " Hell
5 msg = agent2 ( msg )
6 msg = agent3 ( msg )
7 msg = agent4 ( msg )
8 msg = agent5 ( msg )
Example 3: Example of programming a sequen
Pipeline Abstraction The pipeline abstraction
message transmission, including sequential, conditio
components. With these pipelines, developers can f
boilerplate code. Example 4 illustrates how pipelines
styles to create a clear and concise agent workflow. B
also provides if-else, switch, while-loop, and for-loop p
interactions.

the fault tolerance mechanisms is provided in Section
agent abstraction, which forms the backbone of the
esponsible for interaction and communication. This
tricate workflows and enhance usability, reducing the
streamlined syntax and tools, AgentScope empowers
and optimization of agent-based applications that
ming features and syntactic sugars are introduced in
hitecture, AgentScope provides multi-agent oriented
g basic information, Web UI monitoring the system,
n change a command line application to a graphical
o-code programming workstation (Figure 4). These
the status and metrics of the application, including
ncial costs.
rovide the essential building blocks for developers to
advanced capabilities of large language models. The
Scope that enhance the programming experience for
o streamline the development process for multi-agent
ce for both users and developers. This section delves
hances the programmer’s experience by introducing
on of complex multi-agent applications.
orkflows
evelopers are empowered to construct sophisticated
ch agent’s message exchange can become cumbersome,
roduces two syntactic utilities: pipelines and message
petition.
" ))
l workflow with basic concepts in AgentScope.
uces repetitive coding by encapsulating patterns of
l, and iterative exchanges, into simple and reusable
us on the logic of agent interactions rather than the
n be employed in both functional and object-oriented
es the sequential pipeline in the example, AgentScope
lines, facilitating the programming of the multi-agent

1 # set up agents : agent1 to agent5
2 # ...
3 from agentscope . pipelines import SequentialPipeline
4 from agentscope . pipelines . functional import sequentialpipeline
5
6 # using functional pipeline
7 x = sequentialpipeline ([ agent1 , agent2 , agent3 , agent4 , agent5 ], x)
8
9 # using object pipeline
10 pipe = SequentialPipeline ([ agent1 , agent2 , agent3 , agent4 , agent5 ])
11 x = pipe (x)
Example 4: Using functional and object sequential pipeline to construct workflow in AgentScope.
Message Hub for Agent Communication In multi-agent systems, especially when integrated with
LLMs, efficiently managing communication among a group of agents is essential. The message hub in
AgentScope serves as a broadcast mechanism that simplifies group interactions. Developers can initiate a
message hub by defining participating agents and can include initial broadcast messages. When new messages
are generated by the agents within the message hub, they are automatically disseminated to other participants,
as demonstrated in Example 5. This abstraction is particularly useful for multi-agent scenarios involving
LLMs, where dynamic and contextually rich conversations are commonly observed (Du et al., 2023).
1 # set up agents : agent1 to agent4
2 # ...
3
4 greeting = Msg (" host ", " Welcome to the message hub !")
5
6 with msghub ( participant =[ agent1 , agent2 , agent3 ],
7 announcement = greeting ) as hub :
8 # Message will be broadcast to agent2 and agent3 automatically
9 agent1 ()
10
11 # Delete agent2 from the message hub
12 hub . delete ( agent2 )
13
14 # Add agent4 into the message hub
15 hub . add ( agent4 )
16
17 # Broadcast message
18 hub . broadcast ( Msg (" host ", " Welcome agent4 to join the hub !"))
Example 5: Using message hub with AgentScope.
3.2 Resource-Rich Environment for Agent Development
To further enhance usability, AgentScope is equipped with a rich set of built-in resources, including services,
dedicated agents, and pre-configured examples. These resources are designed to reduce the initial setup effort
and enable rapid prototyping and deployment of multi-agent LLM systems.
Comprehensive Service Integration AgentScope integrates various service functions, such as web search,
database querying, and code execution, to support the tool usage capabilities of agents. These service
functions are essential for building helpful agents with LLMs, as agents often need to draw information
from external sources or execute tasks that go beyond the equipped LLMs’ internal knowledge. Example 6
showcases the seamless conversion of a service into an OpenAI-Compatible JSON format, simplifying the
integration process for developers.
7

1 from agentscope . service import ServiceFactory , web_search
2
3 bing_search , func_json = ServiceFactory . get ( web_search , engine =" bing ", api_key ="
↰ xxx ", num_results =10)
4
5 print ( func_json )
6 # {
7 # " name ": " web_search ",
8 # " description ": " Searching the given question with bing ." ,
9 # " parameters ": {
10 # " type ": " object ",
11 # " properties ": {
12 # " type ": " object ",
13 # " properties ": {
14 # " question ": {
15 # " type ": " string ",
16 # " description ": " The string question to search in Bing ."
17 # }
18 # }
19 # }
20 # }
21 # }
22
23 searching_result = bing_search (" What ’s the date today ?")
Example 6: Converting web search service into the function and JSON format dictionary that agent can use.
Pre-built Agent Templates As cataloged in Table 1, AgentScope offers pre-built agents and ready-to-use
components for tasks like dialogue management, user proxying, multi-modal data handling, and distributed
deployment. These templates serve as starting points for developers to customize and extend, significantly
accelerating the development of multi-agent LLM applications.
Agent Name Function
UserAgent The proxy of the user.
DialogAgent A general dialog agent, whose role can be set by system prompt.
DictDialogAgent A dictionary version dialog agent, who responds in Python dictionary format.
ReActAgent An agent that can reason and use tools
ProgrammerAgent An agent that can write and execute Python code.
TextToImageAgent An agent that generates images according to the requirements.
RpcUserAgent A distributed version user proxy.
RpcDialogAgent A distributed version DialogAgent.
Table 1: Some examples of built-in agents and their functions in AgentScope.
3.3 Multi-Agent Oriented Demonstration Interfaces
Furthermore, AgentScope introduces interaction interfaces tailored for multi-agent systems, as illustrated in
Figures 2 and 3. These interfaces provide a rich multi-modal experience, crucial for systems incorporating
LLMs that handle diverse data types.
Agent Differentiation in User Interfaces To facilitate user interaction with multiple agents, AgentScope
assigns unique colors and icons to each agent, enhancing clarity and visual distinction in both terminal
and web UI (Fig. 3). The “first-person perspective” feature allows users to experience interactions from the
viewpoint of a specified agent, aligning with their role in the application, such as in a game scenario. This
feature not only enriches the multi-agent experience but also mirrors the nuanced interactions that occur in
human-agent and agent-agent dialogues within LLM systems.
8

Figure 2: The dialogue history of a werewolf game in AgentScope.
Figure 3: Multi-modal interactions between agents in web UI.
Monitoring and Cost Management A vital aspect of deploying LLMs at scale is resource management.
AgentScope includes a monitoring module that tracks model and API usage, as well as calculating financial
costs. Developers can customize metrics and set budget limits, receiving automatic alerts when thresholds
are approached or exceeded. This proactive cost management is particularly important for LLMs that may
incur high computational expenses.
AgentScope Gradio Interface Once you have a multi-agent application, executing it in the terminal
may be a concise choice but lacks attraction. In AgentScope, we provide a powerful Gradio-based interface
that is compatible with all AgentScope applications as long as there is a main function as the application’s
entry point. For example, if the main function of the application is in application.py file, then running
“as_studio application.py” can build a Gradio application with a graphical user interface and support
multi-modal content upload and presentation.
9

3.4 Towards Graphical Application Development
The design mentioned above provides massive convenience for those familiar with Python programming
to quickly develop their multi-agent applications. However, AgentScope takes a step further. AgentScope
provides a drag-and-drop online workstation on which developers only need to drag the module blocks to
compose an application; then, the workstation can generate a configuration file of the application in JSON or
even a piece of Python code. With this feature, those with limited experience with Python programming can
build their multi-agent application without writing any Python code, while those familiar with Python can
instantly obtain a piece of draft code ready for further customization. A screenshot of the online workstation
is shown in Fig. 4, and the idea supporting this implementation is illustrated as follows.
Figure 4: Drag-and-drop programming workstation.
Expressing Multi-agent application with nodes in directed acyclic graph (DAG). Based on the
highly modular design of our basic infrastructure, all the key components can be represented as a node, and
an application can be built by constructing a directed cycle graph (DAG). The execution of the application is
equivalent to triggering and running the nodes in the graph following the traversing order of DAG. Following
the traditional terms, we name such DAG execution as a workflow and name the nodes in the workflow as
workflow nodes. According to their functionality, the workflow nodes are categorized into six different types:
model nodes, agent nodes, pipeline nodes, service nodes and copy nodes.
• Model nodes: Model nodes are designed to be relatively independent of the DAG. They correspond to
the model configurations in AgentScope and work as entries to let users configure their models (LLMs,
embedding models, or multi-modal models) and maintain such information for all the nodes in the
following workflow that need to use the model.
• Service (tool) nodes: These nodes correspond to the services available in AgentScope. Some of them
require additional information to set up, such as Google search and Bing search, which require API
keys; others can be used directly.
• Agent nodes: As the name suggests, agent nodes represent the agents in AgentScope, which means
users need to decide the models, agent name and system prompts for the agent.
• Pipeline nodes: The pipeline node includes the operators of AgentScope, including the message hub
and the pipelines (sequential, for-loop, while-loop, etc.). With such nodes, DAG representations can be
as concise as Python programming.
10

• Message node: The message node is designed
as the announcement (initial message) for the
• Copy node: The copy node is a special kinds
its output is needed for multiple subsequent o
Execute DAG with JSON or compile to Py
applications by composing DAGs. However, the D
represented in some formats (e.g., JSON format recor
we still need to ensure it is as reusable as other appli
a data structure called ASDiGraph, which provides
• Direct-run: Given a JSON file recording the D
and sort the nodes in topological order. With
execute them in order and feed the predecessor’
step by step.
• To-Python compiler: The second solution
the highly modularized components of Agent
the functionality, required inputs, and expect
each node contains Python code for importin
executing the application logic. ASDiGraph fi
code, and then it composes the pieces of exec
users will obtain a complete Python script aft
3.5 Automatic Prompt Tuning
For a multi-agent system that utilizes LLMs for gener
human effort and expertise (Pryzant et al., 2023), wh
and tuning in AgentScope for its high usability. Sp
based on a simple description of the agent in natura
enable in-context learning.
System Prompt Tuning When an agent is create
to define its roles and responsibilities for following h
might be prompted as “You are proficient in writing
informative system prompt can improve agent perfo
such as “You are proficient in writing and executing
fashion and provide unit tests for each module”. W
description of the agent when creating the agents, a
system prompts using built-in tools based on LLMs
1 # set up agents with automatic prompt
2 # ...
3 from agentscope . agents import Program
4
5 # Load model configs
6 agentscope . init ( model_configs =" model_
7
8 # Create a programmer agent
9 programmer_agent = ProgrammerAgent ( na
10 model_config_
11 sys_prompt ="a
Example 7: Initialize a programmer agen

r cases where some initial messages are needed, such
ssage hub.
node that replicate the results of a parent node when
ations.
on. With the nodes above, developers can build
is highly UI-dependent. Although a DAG can be
g each node’s information and execution dependency),
ions. To overcome this, AgentScope is equipped with
solutions based on it.
information, ASDiGraph can parse DAG information
se sorted nodes, the run function of ASDiGraph can
utput to their successors as an application is executed
o translate the JSON file to a Python script. With
pe, the key idea is to rely on internal mappings of
outputs to small pieces of Python code. Specifically,
ependent modules, initiating models or agents, and
groups the pieces of importing code and initiating
on code following the topological order. Therefore,
he ASDiGraph finishes compilation.
on, writing an appropriate prompt requires significant
motivates us to provide automatic prompt generation
cally, AgentScope allows users to generate prompts
nguage, update prompts according to contexts, and
a system prompt should be associated with the agent
an instructions. For example, a Programmer Agent
executing Python code”. Meanwhile, a detailed and
nce and ensure that the agent performs as expected,
hon code. You prefer to write the code in a modular
h AgentScope, users only need to provide a simple
AgentScope can automatically generate such helpful
shown in Example 7.
neration
Agent
figs . json ")
" assistant ", auto_sys_prompt =True ,
e =" my_config ",
ssistant that can write Python code ")
ith automatic system prompt generation.

Besides, AgentScope provides interfaces for system prompt updates, which include manually setting by
users or automatically adjusting based on the context. As a promising future direction, meta-prompting
techniques (Pryzant et al., 2023; Suzgun and Kalai, 2024) can also be integrated into AgentScope, which
might involve integrating an evaluator to provide guidance for automatic prompt optimization.
In-Context Learning Providing multiple demonstrations to the LLMs can greatly enhance their ability
to follow instructions, particularly when we want them to complete specific downstream tasks (Dai et al.,
2023; Wei et al., 2022). AgentScope provides a simple switch to turn on/off the in-context learning behavior
for agents that utilize LLMs. When users choose to apply in-context learning, they only need to provide
demonstration candidates and configure how to match the most suitable ones, as illustrated in Example 8.
AgentScope offers several widely-used and useful matching approaches, such as random selection, similar
questions, and similar answers, and allows for user customization.
1 # set up agents with in - context learning
2 # ...
3 from agentscope . agents import ReActAgent
4 from agentscope . utils . common import load_demo_data
5
6 # Load model configs
7 agentscope . init ( model_configs =" model_configs . json ")
8
9 # Load demonstrations
10 react_pairs = load_demo_data (" my_demos . txt ")
11
12 # Create a reAct agent
13 react_agent = ReActAgent ( name =" react_agent ", enable_icl =True ,
14 demos = react_pairs , matching_approach =" random ")
Example 8: Enable in-context learning when creating an agent.
4 Fault-Tolerant Mechanisms
In the realm of multi-agent systems, particularly those interfacing with diverse open-source LLMs with various
instruction-following capabilities, fault tolerance is a key property to ensure seamless operation. AgentScope
is engineered to autonomously handle a wide range of errors with minimal human intervention required,
drawing upon a comprehensive fault-tolerant infrastructure that is acutely aware of the complexities involved
in multi-agent coordination and LLM dependencies.
Error Classification and Handling Strategies Our approach begins with a methodical classification of
errors into distinct levels, each with tailored handling strategies:
• Accessibility errors: In AgentScope, an agent’s functionalities rely on different kinds of services, but
those services may be subject to temporary inaccessible errors. These errors may be caused by model
instability or network conditions. For example, the model APIs may return a timeout error when there
is traffic congestion during busy hours, or a database on a remote machine may be inaccessible because
of transient network outages.
• Rule-resolvable errors: As many multi-agent applications require information exchange between
services or agents, it is essential to follow the protocols for those communications, e.g., in JSON format.
However, as the responses of LLMs are not fully controllable yet, their return may not follow the format
required in the prompts. For example, we may expect a response from an LLM in JSON, but a right
brace is missed at the end of the return, leading to parsing failure. As the JSON format has clear
specifications, it is reasonable to assume that a subset of these errors can be resolved by correcting the
format according to the rules to meet the specifications.
12

• Model-resolvable errors: When a multi-agent system handles some complicated tasks, the ability
of the agent to understand the input, make decisions, and deliver outputs mostly depends on the
capability of LLMs. In some cases, the responses of LLMs are in the expected format, but the content
has problems, such as argument errors, semantic errors, or programming mistakes. It is hard to have
pre-defined rules to regularize those responses for diverse tasks, but it has also been shown that such
errors may be detected and recovered by further interaction with the LLMs.
• Unresolvable errors: Eventually, there must be some errors that cannot be detected or solved. A
typical example is that the API key of an LLM is expired or unauthorized. The agents relying on it or
the system can do nothing to resolve such errors without human intervention.
Fault Tolerance mechanisms in AgentScope In AgentScope, we provide different mechanisms to
encounter the errors summarized above.
• Basic auto-retry mechanisms: To combat accessibility errors, AgentScope’s API services and model
wrappers are fortified with retry logic that developers can customize, such as setting the maximum retry
count. This ensures that agents can recover from sporadic disruptions and maintain their operational
continuity.
• Rule-based correction tools: The rule-based correction tools are introduced into AgentScope to
efficiently and economically handle some easy-to-fix format errors in the responses of LLMs. For
example, we establish a set of default rules in AgentScope that can complete unmatchable braces and
extract JSON data from strings. Such rule-based correction tools can correct some of the common
rule-resolvable errors without calling LLM APIs again, which means shorter processing time and no
LLM API call cost.
• Customizable fault handlers: AgentScope also integrates flexible interfaces of fault handlers in model
wrappers for developers to define how to parse the responses from LLMs and handle the unexpected
outputs. Application developers can configure their fault handling mechanism by providing a parsing
function, fault handling function, and the number of chances given to LLMs through configurable
parameters (i.e., parse_func and fault_handler and max_retries) when invoking LLMs. With such
developer-friendly design, AgentScope can be configurably robust to rule-resolvable errors (when the
build-in rules fail to handle) and some model-resolvable errors that can be detected and handled by a
single agent (e.g., distilling a verbose summary to a more concise one).
• Agent-level fault handling: There are model-resolvable errors that require more advanced LLM
usages or agent-level interaction to recover. For example, detecting semantic errors, which usually
include factual inaccuracy, logical inconsistency, contextual incoherence, unreasonable inference, and
inappropriate vocabulary usage, is challenging since they may not necessarily trigger immediate red
flags within the system’s existing validation processes. Developers can utilize the agent’s ability in
AgentScope (e.g., memory module and message hub) to critique for semantic error checking such as
self-critique, pairwise critique, and human-augmented critique.
• Logging system: Although the unsolvable errors are too tricky for the system to handle, AgentScope
provides an improved logging system for developers to quickly monitor and identify the problems in
multi-agent applications. The logging system in AgentScope has customized features for the multi-agent
application scenarios, including adding a logging level called CHAT for logging conversations between
agents, providing formatted logs with various execution information, and a WebUI user interface to
facilitate monitoring.
5 Multi-Modal Applications
The integration of multi-modal data is indispensable for advancing the capabilities and applications of
multi-agent with LLMs. AgentScope is designed to seamlessly support various data modalities, leveraging the
diverse inputs and outputs that contemporary LLMs can process and produce.
13

Figure 5: The generation, storage, and tra
Management of Multi-Modal Data In a runni
data is carefully managed. This management includes
data—all facilitated through a decoupled architectu
exemplifies this process, including data originating f
retrieval, and data sharing.
• Multi-modal data generation: There are t
One source is simply the locally stored multi-m
or general agents with access to the local file
generation models. Our model APIs and the m
models, such as the text-to-image content gener
image-to-text image analysis models, e.g., GPT
their favorite multi-modal models and custom
examples as the starting points. This customiz
from our modular design, allowing developers t
• Multi-modal data storage: As mentioned
can be either from ready-to-use local files or g
model wrapper is invoked to generate multi-m
of the file manager and returns a local URL w
service.
• Multi-modal data transmission: AgentSc
between agents by allowing agents to encapsu
indicate the actual storage locations of the da
through the URLs when ready to process thos
The benefits of introducing URLs in the messag
Firstly, it can minimize the message size to avoid pot
and enable the receiver agent to load the data on de
message, the downstream agents can potentially pri
to/and the processing of multi-modal information. L
facilitate the multi-modal data demonstration, whic
Multi-Modal Interaction Modes With the im
empowers users to interact with multi-modal syste
UI. Fig. 3 showcases the user’s ability to interact w
terminal, users can conveniently access locally stor
further enhances user experience by providing an intu
aligning with the expectations of modern web applic

ission of Multi-modal data in AgentScope.
AgentScope application, the lifecycle of multi-modal
generation, transmission, and storage of multi-modal
using URLs and a local file manager system. Fig. 5
m user inputs or model generations, data storage and
primary sources of multi-modal data in AgentScope.
l files, which can be used by either user proxy agents
stem. Another source is the model-modal content
el wrappers integrate the most popular multi-modal
on models like OpenAI’s DALL-E, and conversely, the
. Besides the built-in APIs, developers can introduce
e their own model wrappers, with our ready-to-use
on process is streamlined in AgentScope and benefits
onnect their multi-modal services with minimal effort.
ve, multi-modal data in the multi-agent application
rated by multi-modal models. When a multi-modal
al data, it first saves the data locally with the help
n it receives multi-modal data from the model API
simplifies the process of multi-modal data sharing
e local or remote URLs in multi-modal messages to
The receiver agents can load the multi-modal data
when agents share multi-modal data are three-fold.
al errors or delays because of the network bandwidth
nd. Secondly, if there is other text information in the
ize or parallel the processing of the text information
but not least, such URL-attached messages can also
ill be introduced in the following section.
mentation of URL-attached messages, AgentScope
via accessible interfaces such as terminal and web
multi-modal data within interaction modes. In the
data by activating the provided URLs. The web UI
ve platform to view and analyze multi-modal content,
ons.

Through AgentScope, developers are equipped to t
needs, forge applications that handle diverse data
to engage with multi-modal agents effectively. Thi
positions AgentScope as a versatile and powerful fra
LLMs, broadening the horizons for developers and r
AI systems.
6 Tool Usage
Tool usage is an important feature for LLM-empow
environment, and handle more complex tasks (Wu
For simplicity, we treat using tools as equivalent to
tool usage module is designed based on ReAct algorit
interleaved reasoning and task-specific actions, alon
features high compatibility, extensibility, robustness,
prompt engineering, reasoning, and response parsing
the tool usage involves four steps:
• Function Preparation: Parse the provided
LLMs can utilize them directly.
• Instruction Preparation: Prepare instructi
functions to LLMs, including the purpose, argu
• Iterative Reasoning: LLMs generate strateg
in the required format.
• Iterative Acting: Parse and check the LLM r
if the response adheres to the expected form
correction.
In the above process, the service toolkit modu
processing, prompt engineering, response parsing,
extensible. Fig. 6 demonstrates how the service tool
Function Preparation. In function preparation
and to generate ready-to-use functions and their corre
developers only need to register their functions wit
Fig. 6, developers choose the Bing search function
service toolkit will automatically generate the proce
schema format. The descriptions will be used to gen
some model APIs (e.g., OpenAI and DashScope Ch
directly, which we will discuss in Sec. 6.1.
Instruction Preparation For novice developers, t
and calling format for tool usage, as demonstrate
function with a clear description and the parameter
functionalities. On the other hand, the calling forma
in a Markdown fenced code block with thought, speak
the thought field will provide a reasoning process for t
selecting candidate functions, and correcting errors.
Iterative Reasoning In AgentScope the reasonin
reasoning step LLMs should analyze the current situ
to construct prompts with the tool instructions and
LLMs. Such design provides high reusability and fle
and can be adapted to different tasks and scenarios

r model API services and wrappers to their individual
dalities, and provide users with the necessary tools
omprehensive support for multi-modal applications
work for harnessing the full potential of multi-agent
rchers alike in creating sophisticated and interactive
ed agents, allowing agents to perceive, change their
al., 2023; Paranjape et al., 2023; Parisi et al., 2022).
ling service functions by LLMs. In AgentScope, the
(Yao et al., 2023), which allows for the generation of
with a core component—service toolkit. Such design
d re-usability, spanning from function pre-processing,
gent-level fault tolerance. Specifically, in AgentScope
vice functions, and pre-process the functions so that
prompt for tool usage to elaborate the available tool
nts, constraints of the function, and its calling format.
easoning, make decisions for tool usage, and respond
onse according to the calling format, invoke functions
or generate a detailed error message to LLMs for
is responsible for tool functions management, pred function execution, and it is highly modular and
works in AgentScope when users post a query.
e target is to preset the developer-specific arguments,
nding formatted description for LLMs. In AgentScope,
reset arguments in the service toolkit. As shown in
provide the API key during registration. Then the
d ready-to-use function and its description in JSON
te tool instructions in natural language. Optionally,
API, etc.) can receive the JSON schema descriptions
service toolkit builds in templates for tool instruction
n Fig. 6. The tools instruction template lists each
requires, leading to an easy understanding of their
s demonstrated in Fig. 6, requires a JSON dictionary
d function fields. During LLM generation, we expect
next acting, including analyzing the current situation,
nd acting steps are iterative. As stated above, in the
n and decide the next actions. Developers only need
e calling format instructions and feed them into the
ility, that is, the service toolkit is task-independent
y easily.

Figure 6: The ReAct-based tool usage module in AgentScope.
Iterative Acting In the acting step, the service toolkit will parse the LLM response according to the
calling format, extract the selected function, and execute it with the corresponding arguments. If the response
conforms to the format requirements, and the function executes successfully, the service toolkit will return the
execution results directly, which LLM can generate a response based on in the next reasoning step. Otherwise,
we break down errors into response parsing errors, function execution errors, and other runtime errors. For
response parsing and function execution errors, we expose them to LLM with detailed error information for
correction in the next reasoning-acting iteration, leaving the other runtime errors to developers.
6.1 Customization for Experienced Developers
AgentScope supports developers in highly customizing their tool instructions and function calling formats. To
customize tool instruction, the service toolkit in AgentScope provides JSON schema descriptions automatically,
which provides a structured way to elaborate how a function should be called, including its name, purpose,
arguments, and other relevant details. These formatted descriptions can be directly fed into some advanced
model APIs, e.g. OpenAI and DashScope Chat APIs. For users who want to deeply customize their tool
instructions, they can construct instructions based on the JSON schema descriptions.
Besides the tools instruction, AgentScope also provides great flexibility, that is, AgentScope provides
various model response parsers, including Markdown fenced code blocks, JSON object code blocks, and
customizable tagged contents, as demonstrated in Fig. 7. For the users who want to customize the function
calling format, the Markdown fenced code blocks and JSON object code block allow them to quickly construct
the format instruction and parse the LLM response according to the content types. For users who want to
obtain multi-fields from LLMs, the multi-tagged contents allow the developers to combine different tagged
contents at will and extract them easily from the response into a Python dictionary. With these parsers,
developers are able to customize their own calling format easily.
16

Figure 7: Pars
7 Agents with Retrieval-Augme
With the growing applications of LLMs, some circum
training data set, for example, knowledge in highly
given the required datasets, the fine-tuning or reretrieval-augmented generation (RAG), an innovati
customized knowledge domain (Gao et al., 2023; Le
literature.
The methodology of RAG can be considered as in
pipeline of LLMs. That is, given a collection of docum
index is built, and the original user input is zipped w
into prompts, then fed to the LLMs. Therefore, th
is, the collection of documents that contain the nec
the indexing of the segments (a.k.a. chunks or node
original query (i.e. user input) and retrieved result
reasonable responses from the LLM based on the in
In short, RAG embraces both the power of inform
and provides enhanced LLM service with customized
RAG, the hallucination could be avoided and the fa
As a developer-oriented multi-agent platform, Age
agent applications. Given popular RAG frameworks su
AI, 2023), etc., AgentScope is designed with highly fl
frameworks. In what follows, we introduce several k
Configurations in One-Stop Due to the comple
services is highly convoluted and often headacheAgentScope is comprehensive and also involves multi
configuration solution by using a single .json file to
With this highly systematized configuration in
workflow, without being distracted by the repetitio
agents may involve a wide collection of knowledge
“One-Stop” feature, the corresponding adjustments of
are integrated as the editing over simply one single fi
AgentScope Workstation, in which the dialog-box-b
files and later loaded in Python programs.
Knowledge-oriented Data Managements The
complicated compared with the application on a singl

in AgentScope.
ted Generation
ances require knowledge that is not contained in the
ofessional domains or not publicly available. Even
ining of the LLMs is still expensive. Accordingly,
approach that aims to boost the power of LLMs in
et al., 2020b), is gaining increasing attention in the
ing a pre-processing step into the common utilization
ts that contains needed knowledge, a similarity-based
the most relevant pieces of information and converted
methodology of RAG involves multiple phases, that
ry information, the segmentation of the documents,
he similarity-based index retrieval, the fusion of the
he composing of prompts, and lastly, generation of
mative prompts.
on retrieval and the generative capabilities of LLMs,
main knowledge at low cost. Meanwhile, assisted by
al accuracy could be significantly improved.
cope provides comprehensive RAG support for multias e.g., LlamaIndex (Liu, 2022), LangChain (Langchainble abstracted processes to be compatible with those
eatures of AgentScope RAG.
y of the working pipeline, the configuration of RAG
me for users. While the RAG service provided by
ent workflow, AgentScope provides a simple one-stop
oup all RAG-related configurations.
ace, users only need to focus on constructing the
configurations. For example, the RAG-empowered
ses that need to be configured in detail. With this
e modules (which may lead to different performances)
Moreover, this solution also naturally adapts to the
d configuration can be easily exported to executable
lication of RAG in multi-agent circumstances is more
gent. For example, for a single agent, one can directly

encapsulate the needed knowledge to the agent. Therefore, the initialization of each RAG agent involves the
whole pipeline of conversion from the original documents to vector-stored indexes with retrievers. However,
in multi-agent applications, it is natural for agents to share knowledge, such that repeatedly executing index
computation for each agent is needless. Therefore, AgentScope introduces the notion of knowledge banks.
Knowledge banks can be considered as a collection of knowledge containers, where the smallest manageable
unit is a customized object (which will be referred to as a “RAG object” in the following context). The
workflow starts with initializing the knowledge bank, which mainly relies on the information contained in
the .json configuration file. The information includes the directory and extensions (such as .py or .md)
of documents, the granularity and choice of segmentation tools (e.g. the splitters in Llama-Index) for the
documents, and choice of model for indexing. After the initialization, the computed results are persisted
to the designated directory for later use and we also obtain a knowledge bank consisting of RAG objects,
each marked with a unique knowledge_id, associated with the index of the corresponding documents, an
information retriever, and other attributes. Note that AgentScope permits each RAG agent to load with
more than one RAG object.
Agents with RAG The application of agents with RAG in AgentScope is very simple. For example, we
first need to initialize a KnowledgeBank with some RAG framework, e.g. LlamaIndex, and all the documents.
Then, we configure an RAG agent and load it with the knowledge bank. After that, the initialization is
completed and we can use the RAG agent like any other agent in AgentScope. It is worth noting that if
KnowldgeBank is obtained with LlamaIndex framework, then we need to use LlamaIndexAgent (inherited from
RAGAgentBase). The readers may refer to Section 9.5 for a concrete application sample, which implements a
copilot for AgentScope using our RAG agents. Overall, the key features of RAG agents are summarized as
follows:
• The RAG agent is permitted to load several RAG objects (i.e. any subset of the knowledge bank). One
can choose to load the original RAG objects from the knowledge bank (in such case, the modification
to an object may affect all the agents who use it) or a copy of it.
• While agents are initialized with a KnowledgeBank object, it is permitted for the agents to update
knowledge in time. The operations include inserting, deleting, or replacing knowledge pieces. Moreover,
we provide a solution by monitoring certain directories and keeping the RAG object updated with the
contents in the directories.
• The fusion mechanism of the retrieved results from multiple RAG objects is fully customizable. For
example, since knowledge may be of different importance or trustworthiness, the agent can set weights
for information retrieved from different RAG objects for subsequent processes.
• RAGs agents are permitted to recompose the query in configurable repeats and conduct multiple queries
for more comprehensive answers.
8 Actor-based Distributed Framework
Efficiency and extensibility are essential when building industry-level applications on multi-agent systems.
The inference speed of the agents in multi-agent applications may vary dramatically. For example, suppose
an agent in a multi-modal application employs a text-to-video model. In that case, its response time may be
significantly longer than that of an agent designed to fill in details of stories. Parallelization, as a classic idea,
should be introduced to boost efficiency. Besides, multi-agent applications can comprise agents physically
distributed on different machines. A typical use case is that a company can wrap its patented techniques
or private knowledge bases into an agent on their local machines connected to the internet and provide
autonomous services to other entities via agent interactions.
However, when it comes to multi-agent systems, a challenge is that developers need to make decisions
between the following two pairs of technology roadmaps. As there is no free lunch, any combinations have
their benefits and drawbacks.
18

• Centralized v.s. decentralized coordination.
coordination means multiple computation nod
client model. A multi-agent mechanism with ce
is scheduled by, and the messages between age
On the contrary, decentralized coordination d
forward messages, but the agents in such a sy
directly to the downstream agents for further
While centralized coordination is a straightforw
its disadvantages include vulnerability to cent
node, and difficulty in scaling or extending t
coordination may require extra effort to deve
failure of any single node.
• Static vs. dynamic workflow design. A similar c
graph employed in early versions of TensorFlow
used in PyTorch Paszke et al. (2019). In the c
static and dynamic workflow is akin to choosin
static workflow design can enable the optimiz
resource allocation. However, static workflow
execution, which limits the adaptation into app
design. In contrast, dynamic workflows offer gr
This is particularly relevant when dealing with
based on the input data or model inference res
Figure 8: An example of a distributed application in
different colors.
Distributed mode in AgentScope. AgentScop
an actor-based distributed mode that is mindful of
following important features:
• Automatic parallel optimization without static
automatic parallel optimization, allowing de
programming. This approach seamlessly align
LLMs, where the computational graph can alt

the context of the distributed system, centralized
being managed by a central node, such as the serveralized coordination means the execution of the agents
are forwarded by a central coordination component.
s not rely on any central component to schedule or
m can be invoked automatically and send messages
cessing.
d style that can be understood and is easy to debug,
node failures, imposing heavy traffic on the central
omplicated applications. In contrast, decentralized
and maintain but has a higher robustness against
parison can be found between the static computational
badi et al., 2016) and the dynamic computation graph
ext of multi-agent applications, the choice between a
etween pre-compiled and interpreted execution. The
on of the workflow graph level for running time and
ign requires the workflow graph to be known before
ations, especially the ones with loop structures in the
er flexibility at the expense of optimization potential.
e language models where execution paths can change
s.
entScope, illustrating various processes as denoted by
alances these technology roadmaps by implementing
unique needs of multi-agent LLM systems, with the
phs. AgentScope leverages the actor model to enable
opers to circumvent the intricacies of static graph
with the dynamic and often unpredictable nature of
based on evolving contexts and dialogue states.

• Programming workflows with minimal complex
peer (P2P) implementations that require intrica
simplifies workflow programming to a single p
significantly flattens the learning curve for dev
agent LLMs more accessible.
• Hybrid local and distributed agent support. Agen
where some agents operate locally while other
when integrating LLMs with varying computati
to be distributed while less demanding agen
differentiate between the two during implemen
Specifically, we can concisely describe how Agent
this conceptual framework, an “actor” acts as a stand
all necessary messages. This paradigm ensures that
computation once the required input messages are r
However, the actor-model-based workflow present
passing between actors (i.e., agents) may be placehol
alleviate this, AgentScope introduces the “placeholde
process to continue without blocking, while preservin
(Fig. 8). This mechanism is particularly advantageo
must adapt to the variable output of language mode
1 # set up distributed agent : agent1
2 ...
3
4 input_msg = Msg (" system ", " Which agen
5
6 # the variable choice is a placeholde
7 choice : placeholder = host_agent ( inpu
8
9 if choice [" content "] == " agent2 ":
10 response = agent2 ()
11 elif choice [" content "] == " agent3 ":
12 response = agent3 ()
Example 9: Demonstrating the use of pla
Another series of challenges arise when placehold
loops) without their real values. An example is show
decisions. In these circumstances, AgentScope tem
thus ensuring the continuity of the control flow.
The actor-based distributed mode in AgentScope
simplifies the developer experience but also demon
applications. It enables developers to focus on imp
without concern for underlying distributed complexiti
systems can advance the field of LLMs by making
scalable multi-agent architectures.
One-click deployment in AgentScope. To
provides agent server and a unified message center,
Specifically, the agent server is hold in remote
applications, and initialize their required agents i
developers can set up agent instances remotely, wit
provides high flexibility, especially for large-scale sim
set up in remote machines.
For AgentScope Studio, it provides a unified dis
where messages from all distributed agents will be gat

In contrast to traditional actor models and peer-toexecution ordering for distributed agents, AgentScope
edural style within a Python function. This design
pers, making the construction of sophisticated multicope’s flexibility extends to supporting a hybrid mode
e distributed. This feature is particularly beneficial
l requirements, allowing for resource-intensive models
emain local, all without the developer needing to
ion.
pe incorporates the actor model as the following. In
ne entity that processes computation upon receipt of
ch agent, corresponding to an actor, only engages in
y, thus achieving automatic parallel optimization.
programming challenge: the variable (i.e., messages)
without any practical meaning at the beginning. To
message, a novel data structure that allows the main
he necessary information to retrieve real values later
for multi-agent LLM systems, where execution flow
hould respond next , agent2 or agent3 ?")
sg )
olders in control flow within AgentScope.
are used within control flow statements (e.g., if-else,
Example 9, where a placeholder is required to make
arily blocks the process to retrieve its actual value,
t only provides automatic parallel optimization and
tes high efficiency for distributed multi-agent LLM
enting agent logic, particularly the “reply” function,
This streamlined approach to distributed multi-agent
asier to develop, run, and debug sophisticated and
ther ease the distributed deployment, AgentScope
med AgentScope Studio.
achines, which receives requests from AgentScope
he deployed machine automatically. That means,
ut programming in different machines. Such feature
ions, where a large number of agent instances will be
y interface for distributed multi-agent applications,
ed and displayed in this studio, and allows developers

to forward these messages to their own display inter
management, that is, in this studio developers can c
agent servers remotely. With this studio, developers
9 Signature Applications of Age
As introduced in the previous sections, AgentScope is
and coordinating large-scale models in a user-friendly
a vast spectrum of applications. AgentScope can imp
vs. user dialog to complicated interactive multipla
centralized deployments, AgentScope can extend to d
across multiple machines. In this section, we look
persuasively illustrate the framework’s outstanding
are accessible in our GitHub repository for commun
9.1 Dialog Agents: Basic Conversatio
The simplest yet most fundamental application of
directly interacts with the dialog agent. This appl
AgentScope to quickly capture the core message-pas
The basic conversation example demonstrates the
the UserAgent and DialogAgent, which facilitate
respectively. Normally, as illustrated in Example
tion, which is to load the model configurations (s
init interface of AgentScope, which assigns the LL
AgentScope is compatible with various platforms an
chat/embedding/DALL-E, HuggingFace, ModelScope
vllm, and Flask. Moreover, the init interface also
agent configures, etc.. With all the configurations
i.e. the message-exchanging mechanism between th
all agent-based applications. In this workflow, the
conversation could form an endless loop until the us
To implement more sophisticated applications, A
structured and scalable framework for complex agen
Example 11, we can implement the basic conversati
Readers may also refer to Appendix A for conversat
9.2 Dialog Agents: Group Conversati
Beyond the basic conversation between a user an
conversations. To improve the interactivity, we intr
agent to call a specific agent by simply “@agent_nam
filter_agents function, which screens the message
content.
In this example, we first initialize the agents invo
the characteristics of the agents can be customized
to customize the reaction style or functionality of th
facilitate message deliveries among a group of agent
(e.g. an announcement) and permits agents to broad
if a timeout limit is reached, or the user types in “ex

. Besides, AgentScope studio supports agent servers
k the deployment of distributed agents, open or close
n manage their applications much more easily.
tScope
ulti-agent platform delicately designed for integrating
d fault-tolerant manner, and it is an ideal platform for
ment applications spanning from a simple single-agent
role-play games like werewolf. Moreover, beyond
ributed conversations that involve parallel operations
o several signature applications of AgentScope that
diverse capabilities. All examples referenced herein
use and contribution.
entScope is the basic conversation, where the user
ion is an excellent starting point for fresh users of
g mechanism in our framework.
age of two fundamental built-in agents in AgentScope,
puts from the user and the responses from LLMs,
, the first step of all applications is the initializaified in the model_configs.json file) through the
empowered agents with selected models. Currently,
APIs, including but not limited to standard OpenAI
nd a collection of locally hosted models with FastChat,
ecifies detailed options such as file storage, logging,
tled, it is ready to construct the conversation flow,
ser/agents, which is an essential building block for
agent will always respond to the user’s input, the
decides to opt-out.
ntScope facilitates pipelines, which provide a wellnteractions (in terms of messages). As illustrated in
example with a sequential pipeline or loop pipeline.
history while running the demo codes.
with Mentions
a single dialog agent, AgentScope supports group
uce the “mentions” feature, which allows the user or
The “mention” feature is supported by applying the
d identifies if any agent is mentioned in the message
d in the conversation as shown in Example 12. Here,
the agent_config.json file, e.g. using sys_prompt
gents. Also, we utilize the message hub (msghub) to
The msghub allows the sharing of public information
messages to all agents. The conversation would end

1 import agentscope
2 from agentscope . agents import DialogA
3
4 # read model configs
5 agentscope . init ( model_configs ="./ open
6
7 # Create a dialog agent and a user ag
8 assistant_agent = DialogAgent (
9 name =" Assistant ",
10 sys_prompt =" You are a helpful ass
11 model ="gpt -4"
12 )
13 user_agent = UserAgent ()
14
15 # Basic version
16 x = None
17 while x is None or x. content != " exit
18 x = assistant_agent (x)
19 x = user_agent (x)
Example 10: Code example o
1 # Advanced version with sequential pi
2 from agentscope . pipelines . functional
3 x = None
4 while x is None or x. content != " exit
5 x = sequentialpipeline ([ dialog_ag
6
7 # Advanced version with while loop pi
8 from agentscope . pipelines . functional
9 x = whilelooppipeline (
10 [ assistant_agent , user_agent ],
11 condition_func = lambda _, x: x is
12 x= None )
Example 11: Pipeline-based implemen
9.3 Dialog Agents: The Werewolf Ga
Group conversation and the mentioning feature are f
Here we present a more sophisticated application, the
role-play game. We aim to implement the game wi
example involves six players divided into two opposin
of conversations and discussions, the game ends whe
the number of werewolves equals or outnumbers the
As an LLM-empowered role-play game, we sta
initialization for the agents. As shown in Example 1
default agent configurations for a user to instantiate
the detailed settings are included in the agent_conf
It is worth noting that the werewolf game is bas
such that the werewolves could chat in the “night p
phase”. Similar to the group conversation example
facilitate the conversations. As shown in Example 13,
werewolves discuss for at most MAX_WEREWOLF_DISC
is reached. Here, the agents are required to use an
is enforced in the role-defining prompt. For comple
related information, please refer to Appendix B.

t , UserAgent
model_configs . json ")
ant ",
e basic conversation example.
ine
ort sequentialpipeline
, user_agent ], x)
ine
ort whilelooppipeline
ne or x. content !=" exit ",
ion of the basic conversation example.
e
amental building blocks for multi-agent applications.
ewolf game, which is a popular multiplayer interactive
AgentScope in only one hundred lines of code. This
eams, the werewolves, and the villages. After rounds
ll werewolves are eliminated (i.e. villager victory) or
lagers (i.e. werewolf victory).
he game settings with allocation for the roles and
AgentScope supports a quick setup, which consists of
e agent objects with corresponding roles in one click,
s.json file.
on the group conversation capability of AgentScope,
e” and all participants could discuss during the “day
he message hub (msghub) of AgentScope is used to
er the host (moderator) makes an announcement, the
ION_ROUND rounds and conclude once an agreement
greement” attribute in the response message, which
workflow, an example of dialogue history, and more

1 import agentscope
2
3 # Read model and agent configs , and initialize agents automatically
4 npc_agents = agentscope . init (
5 model_configs ="./ configs / model_configs . json ",
6 agent_configs ="./ configs / agent_configs . json ",
7 )
8 user = UserAgent ()
9 agent = list ( npc_agents )+[ user ]
10 ...
11 # We use msghub to coordinate the conversations , ‘‘ hint ’’ is a message notified
↰ to all agents
12 with msghub ( agents , announcement = hint ):
13 while True :
14 try :
15 x = user ( timeout = USER_TIME_TO_SPEAK )
16 if x. content == " exit ":
17 break
18 except TimeoutError :
19 x = {" content ": ""}
20 logger . info (
21 f" User has not typed text for "
22 f"{ USER_TIME_TO_SPEAK } seconds , skip .",
23 )
24 # if user mentions any npc_agent in the message , it will be added to the
↰ speak_list
25 speak_list += filter_agents (x. get (" content ", ""), npc_agents )
26
27 # if the speak_list is non - empty , the mentioned agents will respond in a
↰ sequential manner
28 if len ( speak_list ) > 0:
29 next_agent = speak_list . pop (0)
30 x = next_agent ()
31 # otherwise , all agents will respond one by one .
32 else :
33 next_agent = select_next_one ( npc_agents , rnd )
34 x = next_agent ()
35 # if the response mentions any agent , it will be added to the speak_list
36 speak_list += filter_agents (x. content , npc_agents )
Example 12: Code example of the group conversations.
9.4 Distributed Deployed Agents
We have seen applications regarding conversations involving dialog agents, but those examples are fundamental
in the sense that the agents are deployed in a centralized manner, that is, the agents are hosted on a single
machine and in a single process. To allow agents to be hosted by separate machines or processes, AgentScope
allows agents to be distributedly deployed in two modes, the single-machine multi-process mode, and the
multi-machine multi-process mode. In what follows, we present examples to demonstrate this feature.
Single-Machine Multi-Process Mode: For this mode, all agents are deployed on a single machine, but
running in separate processes. For better comparison, we implement the basic conversation example in this
mode (see Example 14 for the complete code). Compared with Example 10 and 11, we use the to_dist
function to convert the current agent instance into a distributed version. Then, the assistant_agent would
be deployed on a local host with an automatically allocated port. Besides the aforementioned differences, the
single-machine multi-process mode is identical to local deployment, yet it has been optimized for parallel
execution.
Multi-Machine Multi-Process Mode: To demonstrate this mode, we initiate the agent service (a
DialogAgent) on a remote machine (as shown in Example 15), and constructs a workflow (as shown
Example 16). One may note that the only difference comparing to the local deployed mode is that the agent
server needs to be connected using specified URLs and ports before establishing the workflow.
Overall, for AgentScope, we can smoothly convert from the local deployment mode to the distributed
23

1 import agentscope
2 # Read model and agent configs , and initialize agents automatically
3 survivors = agentscope . init (
4 model_configs ="./ configs / model_configs . json ",
5 agent_configs ="./ configs / agent_configs . json ",
6 )
7
8 # Define the roles within the game .
9 roles = [" werewolf ", " werewolf ", " villager ", " villager ", " seer ", " witch "]
10
11 # Based on their roles , assign the initialized agents to variables .
12 wolves , villagers , witch , seer = survivors [:2] , survivors [2: -2] , survivors [ -1] ,
↰ survivors [ -2]
13 ...
14 # Night phase : werewolves discuss
15 hint = HostMsg ( content = Prompts . to_wolves . format ( n2s ( wolves )))
16 with msghub ( wolves , announcement = hint ) as hub :
17 ...
18 for _ in range ( MAX_WEREWOLF_DISCUSSION_ROUND ):
19 x = sequentialpipeline ( wolves )
20 if x. agreement :
21 break
22 ...
Example 13: Code example of the werewolf game.
1 from agentscope . agents import UserAgent , DialogAgent
2 import agentscope
3 # we use . to_dist () to convert the agent to distributed mode .
4 assistant_agent = DialogAgent (
5 name =" Assistant ",
6 sys_prompt =" You are a helpful assistant ",
7 model ="gpt -4"
8 ). to_dist ()
9 user_agent = UserAgent ()
10
11 x = None
12 while x is None or not x. content != " exit :
13 x = sequentialpipeline ([ assistant_agent , user_agent ], x)
Example 14: Example that deploys agents in single-machine multi-process mode.
mode and vice versa, with only minimal changes to the agent configuration and no modification to the
workflow.
9.5 RAG Agents: AgentScope Copilot
As previously introduced in Section 7, Retrieval-Augmented Generation (RAG) allows developers to fully
utilize the language generation capability of LLMs accompanied by a customized knowledge pool. Accordingly,
AgentScope introduces RAG agents to facilitate such a functionality. In the following example (as shown
Example 17), we show how to use a collection of Llama-index-based RAG agents (i.e., the LlamaIndexAgent
inherited from the RAGAgentBase) to build a multi-agent copilot for AgentScope.
We first initialize the agents. Note that the most important feature of RAG agents is that beyond
customized personalities and behavioral styles configured by the system prompts, each agent is loaded with
external knowledge, which is specified in the agent_configs that contains configuration information such as
data storage directory, targeted file types, document chunking settings, the indexing and embedding settings,
etc..
The workflow of copilot is designed as follows, the user first inputs a message, and if the user mentions some
specific RAG agents as we defined, then the corresponding agents would respond, otherwise, the guide_agent
would decide the most suitable agent to respond to the query. Due to space limit, we only represent simplified
24

1 from agentscope . agents . rpc_agent impo
2 from agentscope . agents import DialogA
3
4 # load model configurations
5 agentscope . init ( model_configs =" config
6 # set server for the remote agent
7 server_launcher = RpcAgentServerLaunc
8 agent_class = DialogAgent ,
9 agent_kwargs ={
10 " name ": " Assitant ",
11 " sys_prompt ": " You are a help
12 " model ": "gpt -4"
13 },
14 host =" xxx . xxx . xxx . xxx ",
15 port =12010 ,
16 )
17 # start the server
18 server_launcher . launch ()
19 server_launcher . wait_until_terminate (
Example 15: Deploying a remote age
1 agentscope . init ( model_configs =" config
2
3 assistant_agent = DialogAgent (
4 name =" Assistant ",
5 model ="gpt -4"
6 ). to_dist (
7 host =" xxx . xxx . xxx . xxx ", # The
8 port =12010 , # The
9 launch_server = False , # Use
10 )
11 user_agent = UserAgent ()
12
13 x = None
14 while x is None or not x. content != "
15 x = sequentialpipeline ([ assistant
Example 16: Example of setting sub-processes
codes here and please refer to the repository and do
9.6 Web Search and Retrieve Agents
We have shown examples of agents generating res
information retrieved from external knowledge librari
internet resources to build agents, as introduced in
As presented in Example 18, the initialization in
user inputs, the SearcherAgent that converts the us
to retrieve webpages from the internet, and the Answ
compose answers.
It is worth noting that, since a large number o
the standard single-process mode, multiple Answere
answer questions in a sequential manner on a single
multiple instances of AnswererAgent running in pa
AgentScope agents.

RpcAgentServerLauncher
t
odel_configs . json ")
(
assistant .",
n multi-machine multi-process mode..
odel_configs . json ")
rget URL of agent server
rget port of agent server
e remote agent server
t ":
ent , user_agent ], x)
r agents in multi-machine multi-process mode.
mentation for more details.
nses by the capability of LLM (DialogAgent) and
LlamaIndexAgent). Nevertheless, we can also utilize
following example.
ves three types of agents - the UserAgent that takes
s questions into keywords and calls the search engine
rAgent that retrieves information from web pages to
eb pages may be returned by the search agents. In
gent instances can only perform web searching and
achine. For better efficiency, it is beneficial to allow
el, that is, the multi-machine multi-process mode of

1 import agentscope
2 from agentscope . agents import UserAgent , DialogAgent , LlamaIndexAgent
3 ...
4 # initialize agentscope with model configurations
5 agentscope . init ( model_configs =" configs / model_configs . json ")
6
7 # initialize the RAG agents based on different configurations
8 tutorial_agent = LlamaIndexAgent (** agent_configs [0][ " args "])
9 code_agent = LlamaIndexAgent (** agent_configs [1][ " args "])
10 api_agent = LlamaIndexAgent (** agent_configs [2][ " args "])
11 search_agent = LlamaIndexAgent (** agent_configs [3][ " args "])
12 ...
13 # initialize a basic dialog agent as the ‘‘ frontdesk assistant ’’ and a user
↰ agent
14 guide_agent = DialogAgent (** agent_configs [4][ " args "])
15 user_agent = UserAgent ()
16 ...
17 while True :
18 x = user_agent ()
19 # the workflow terminates when user inputs nothing or ‘‘ exit ’’
20 if len (x[" content "]) == 0 or str (x[" content "]). startswith (" exit "):
21 break
22 # find out the agents mentioned in user ’s input
23 speak_list = filter_agents (x. get (" content ", ""), rag_agent_list )
24 if len ( speak_list ) == 0:
25 # if no agent is mentioned , the guide agent will decide which one to
↰ call
26 guide_response = guide_agent (x)
27 speak_list = filter_agents (
28 guide_response . get (" content ", ""),
29 rag_agent_list ,
30 )
31 # agents called by the guide agent will be recorded
32 agent_name_list = [ agent . name for agent in speak_list ]
33 # the listed agents respond to the query in turn
34 for agent_name , agent in zip ( agent_name_list , speak_list ):
35 if agent_name in rag_agent_names :
36 agent (x)
Example 17: Example of using RAG agents to build a copilot for AgentScope.
9.7 ReAct Agents: Convert Natural Language to SQL Query
Natural Language to SQL query (NL2SQl) is a classical yet challenging task in both database and natural
language processing communities, which aims to convert human input questions in natural language into
SQL queries. In the research community, there is a collection of works exploring the potential of LLMs in
NL2SQL, and it would be very interesting to explore this task with LLM-empowered agents.
In AgentScope, we provide a special class of agents, the ReAct (reasoning and acting) agents. More
specifically, we could create new service functions, by using the ServiceToolkit module, for the ReAct
agents and corresponding LLMs. In this example, we try to equip the ReAct agent with a state-of-the-art
NL2SQL algorithm, DAIL-SQL.
As the first step (as shown in Example 19), we need to initialize the model config and the SQL database,
then initiate and provide the corresponding database path in sqlite file format. Here we generate the SQLite
file using the provided SQL commands. You can also use the .sqlite format file directly.
Then, as shown in Example 20, we define the tools for ReAct Agent to execute the SQL query. Namely,
our agent should be able to generate the SQL query given the natural language input and execute the SQL
query to get the result. We referenced a third-party Text-to-SQL tool DAIL-SQL to generate a Text-to-SQL
prompt. We use the query_sqlite service function in the agentscope.service module. Now, we can
initiate the ReAct Agent using the defined tools and interact with the agent, as shown in Example 21.
26

1 import agentscope
2 from searcher_agent import SearcherAgent
3 from answerer_agent import AnswererAgent
4 from agentscope . agents . user_agent import UserAgent
5
6 agentscope . init ( model_configs =" configs / model_configs . json ")
7
8 # we can perform multiple searches at one time
9 WORKER_NUM = 3
10 searcher = SearcherAgent (
11 name =" Searcher ",
12 model_config_name =" my_model ",
13 result_num = args . num_workers ,
14 search_engine_type = args . search_engine ,
15 api_key = args . api_key ,
16 cse_id = args . cse_id ,
17 )
18 # instantiate the answerer agents
19 answerers = []
20 for i in range ( args . num_workers ):
21 answerer = AnswererAgent (
22 name =f" Answerer -{i}",
23 model_config_name =" my_model ",
24 )
25 # if we want to put agents in distributed ( parallel ) mode
26 if args . use_dist :
27 answerer = answerer . to_dist ( lazy_launch = False )
28 answerers . append ( answerer )
29 user_agent = UserAgent ()
30
31 msg = user_agent ()
32 while not msg . content == " exit ":
33 msg = searcher ( msg )
34 results = []
35 for page , worker in zip ( msg . content , answerers ):
36 results . append ( worker ( Msg (** page )))
37 for result in results :
38 logger . chat ( result )
39 msg = user_agent ()
Example 18: Example of utilizing web search and retrieve agents.
9.8 AgentScope Workstation
AgentScope provides a very convenient and user-friendly development kit in the form of “dragging windows”,
the Workstation. Here, implementing applications of AgentScope using this development kit is of low cost
in the sense that, entry-level developers or those without any programming experience could easily develop
their own application at ease by simply dragging those agent-related modules and connecting them in a
very straightforward way. For example, as shown in Fig. 9, we implement the basic conversation example in
Workstation. As we can see, we do not need to write any code, just simply type in the configurations such as
detailed settings and APIs into the corresponding windows, link the windows to build the dependency and
connection, and then with one-click, Workstation would get ready for launch automatically. Meanwhile, the
Workstation also introduced static checking rules to ensure the correctness of the configurations.
AgentScope Workstation also provides comprehensive support for advanced developers. The developers
could export the configurations on the modules as .json files and execute by the AgentScope Workstation
engine. Alternatively, one can also use the AgentScope Workstation Compiler to convert all configurations
into Python codes for further editing or development to implement more customized adjustments.
27

1 import agentscope
2 from sql_utils import create_sqlite_d
3 ...
4 agentscope . init ( model_configs =" config
5 create_sqlite_db_from_schema ( db_schem
6 ...
Example 19: Example of utilizi
1 from agentscope . service import (
2 ServiceResponse ,
3 ServiceExecStatus ,
4 ServiceToolkit ,
5 query_sqlite ,
6 )
7 from sql_utils import DailSQLPromptGe
8
9 def generate_sql_query ( question : str ,
↰ ServiceResponse :
10 prompt_helper = DailSQLPromptGene
11 prepared_prompt = prompt_helper . g
12
13 def get_response_from_prompt ( prom
14 ...
15 sql_response = get_response_from_
16 prepared_prompt [" prompt "], mo
17 )
18 return ServiceResponse (
19 ServiceExecStatus . SUCCESS ,
20 sql_response
21 )
22
23 # Use Service Toolkit to set up tool
24 service_toolkit = ServiceToolkit ()
25 service_toolkit . add ( generate_sql_query
↰ loaded_model )
26 service_toolkit . add ( query_sqlite , dat
Example 20: Example of utilizi
10 Related Works
The development of AgentScope aligns with the ra
large language models (LLMs) for the creation of lan
introduce works closely related to AgentScope from tw
focusing on individual agent capabilities, and Mult
multiple agents. For broader related works, readers
Language Agent Frameworks Language agent
can interpret and interact using human language.
The Transformers library (Huggingface, 2023) h
transformer models in its recent updates (Transfor
tools, allowing the model to interpret instructions a
for various open-source and proprietary model endp
(Langchain-AI, 2023) provides a framework for build
reasoning. It includes libraries and templates that
unified cognitive architecture. LangServe and Lang
deployment as a REST API and offering developer too
framework. AutoGPT (AutoGPT-Team, 2023) illustr

rom_schema
odel_configs . json ")
ath , db_sqlite_path )
web search and retrieve agents.
ator
_path : str , model : Callable ) ->
or ( db_path )
rate_prompt ({" content ": question })
dict , model : Callable ) -> str :
mpt (
= model
ctions for LLMs
db_path = db_sqlite_path , model =
se = db_sqlite_path )
web search and retrieve agents.
dly evolving landscape of frameworks that leverage
age agents and multi-agent systems. Here, we briefly
ub-domains pertinent : Language Agent Frameworks,
gent Frameworks, emphasizing collaboration among
refer to (Wang et al., 2023; Xi et al., 2023).
meworks are pivotal for developing applications that
ntroduced a natural language API to interface with
rs-Agents). This API utilizes a set of customizable
generate code snippets accordingly. It offers support
nts, catering to diverse developer needs. LangChain
g applications that are context-aware and capable of
litate the integration of multiple components into a
ith extend the framework’s capabilities by enabling
or debugging and monitoring chains built on any LLM
s a different approach, allowing an LLM to iteratively

1 from agentscope . agents import ReActAgent
2 agent = ReActAgent (
3 name =" assistant ",
4 model_config_name =’gpt -4 ’,
5 service_toolkit = service_toolkit ,
6 sys_prompt =" You are a helpful agent that preform SQL queries base on natual
↰ language instructions .",
7 verbose =True , # set verbose to True to show the reasoning process
8 )
9 ...
10 mss = Msg (
11 name =" user ",
12 content =" How many singers do we have ?",
13 role =" user "
14 )
15 logger . chat ( mss )
16
17 sql_query_mss1 = agent ( mss )
18 ...
Example 21: Example of utilizing web search and retrieve agents.
execute actions and make decisions. As a generalist agent, AutoGPT is not task-specific; it is designed to
perform a variety of computer-based tasks, reflecting the adaptive nature of LLMs. ModelScope-Agent (Li
et al., 2023a) is a customizable agent framework that harnesses open-source LLMs to perform tasks and
connect with external APIs. It facilitates seamless integration with model APIs and common APIs while
providing a comprehensive infrastructure for data collection, tool retrieval, and customized model training,
all aiming to realize practical real-world applications.
Multi-Agent Frameworks Building on the capabilities of individual agents, multi-agent frameworks
explore collaboration and interaction among multiple agents to address complex tasks.
AutoGen (Wu et al., 2023) provides a generic infrastructure that allows developers to program interaction
patterns using both natural language and code. This framework enables the development of diverse applications
by facilitating conversation among agents that are customizable and can utilize various combinations of
LLMs, human inputs, and tools. MetaGPT (Hong et al., 2023) incorporates meta-programming to enhance
multi-agent collaborations. By encoding Standardized Operating Procedures (SOP) into prompts, this
framework ensures streamlined workflows and reduced errors, exemplifying effective task decomposition
among agents. AGENTS (Zhou et al., 2023) is an open-source library that supports autonomous language
agents with features like planning, memory, and multi-agent communication. It is designed to be user-friendly,
helping non-specialists to deploy state-of-the-art language agents, and research-friendly, with a modularized
design for extensibility. OpenAgents (Xie et al., 2023) provides an open platform for using language agents
with practical functionalities accessible through a web interface. This framework emphasizes facilitating
real-world agent interactions and includes specialized agents for different tasks, such as data analysis and web
browsing. ChatDev (Qian et al., 2023) exploits LLMs for software development, creating a virtual chat-powered
company that follows a waterfall model. It engages “software agents” at different stages of the development
process, facilitating collaboration and context-aware communication. CAMEL (Li et al., 2023b) proposes a
novel framework for autonomous cooperation among communicative agents using role-playing techniques,
which allows for the generation of conversational data for studying agent behaviors and capabilities. Lastly,
AgentSims (Lin et al., 2023) introduces a sandbox environment to evaluate LLMs in task-based scenarios,
offering an infrastructure for researchers to test specific LLM capacities within a simulated environment.
These frameworks represent significant strides in the use of LLMs for both individual and collaborative
agent tasks. AgentScope is situated within this context, contributing by addressing the need for a user-friendly,
fault-tolerant and versatile framework designed to manage complex interactions and processes inherent in
multi-agent LLM systems. By focusing on ease of use and reliability, AgentScope aims to facilitate the
creation of robust and versatile applications across diverse domains.
29

Figure 9: Workstation generates wo
11 Conclusion
In this work, we propose AgentScope, a platform that
synergizing user-centric design with the advanced cap
and distributed mechanisms, AgentScope demonstra
enabling efficient, fault-tolerant operations and mul
offering an array of development utilities, AgentSco
more inclusive and creative community of developer
Looking forward, AgentScope opens numerous av
could delve into deeper integration of retrieval augm
protocols and interactive modals that evolve alongsid
ing the deployment of multi-agent systems across ind
be profound, potentially leading to smarter and mor
collaboration. With AgentScope, we invite the broa
our foundation, driving innovations that will shape th

ow configuration and Python code.
nds at the forefront of multi-agent system development,
ities of LLMs. Through its innovative communication
its potential to boost collaboration amongst agents,
modal interactions. By abstracting complexities and
ubstantially lowers the barriers to entry, fostering a
es for further research and development. Future work
ed generation, and explore adaptive communication
sk requirements. The platform’s impact on acceleratries, from healthcare to customer service, promises to
esponsive technologies that enhance human-machine
research and development community to build upon
ext generation of intelligent multi-agent applications.

References
Martín Abadi, Paul Barham, Jianmin Chen, Zhife
Sanjay Ghemawat, Geoffrey Irving, Michael Isard,
learning. In 12th USENIX symposium on operatin
265–283, 2016.
Abubakar Abid, Ali Abdalla, Ali Abid, Dawood K
Hassle-free sharing and testing of ml models in th
AutoGPT-Team. Autogpt, 2023. URL https://git
James Betker, Gabriel Goh, Li Jing, Tim Brooks, Ji
Joyce Lee, Yufei Guo, et al. Improving image gen
2023.
Damai Dai, Yutao Sun, Li Dong, Yaru Hao, Shumin
in-context? language models secretly perform gr
Association for Computational Linguistics: ACL 2
Yilun Du, Shuang Li, Antonio Torralba, Joshua B Te
reasoning in language models through multiagent
Justin Fu, Anoop Korattikara, Sergey Levine, and
reinforcement learning for vision-based instruction
Representations, 2019.
Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia
Meng Wang, and Haofen Wang. Retrieval-augm
CoRR, abs/2312.10997, 2023.
Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng
Ka Shing Yau, Zijuan Lin, Liyang Zhou, et al. Me
framework. arXiv preprint arXiv:2308.00352, 202
Huggingface. Transformers-agents, 2023. U
transformers_agents.
Langchain-AI. Langchain, 2023. URL https://git
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fab
Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäsch
intensive nlp tasks. Advances in Neural Informati
Patrick S. H. Lewis, Ethan Perez, Aleksandra Pikt
Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim R
augmented generation for knowledge-intensive NL
Systems 33: Annual Conference on Neural Inform
Chenliang Li, Hehong Chen, Ming Yan, Weizhou Sh
Zhou, Yingda Chen, Chen Cheng, et al. Modelsco
open-source large language models. arXiv preprin
Guohao Li, Hasan Abed Al Kader Hammoud, Hani
Communicative agents for" mind" exploration o
arXiv:2303.17760, 2023b.
Jiaju Lin, Haoran Zhao, Aochi Zhang, Yiting Wu, Hu
sandbox for large language model evaluation. arX

Chen, Andy Davis, Jeffrey Dean, Matthieu Devin,
l. {TensorFlow}: a system for {Large-Scale} machine
ystems design and implementation (OSDI 16), pages
n, Abdulrahman Alfozan, and James Zou. Gradio:
ild. arXiv preprint arXiv:1906.02569, 2019.
b.com/Significant-Gravitas/AutoGPT.
eng Wang, Linjie Li, Long Ouyang, Juntang Zhuang,
tion with better captions. Computer Science, 2(3):8,
Ma, Zhifang Sui, and Furu Wei. Why can GPT learn
ent descent as meta-optimizers. In Findings of the
3, pages 4005–4019, July 2023.
nbaum, and Igor Mordatch. Improving factuality and
bate. arXiv preprint arXiv:2305.14325, 2023.
gio Guadarrama. From language to goals: Inverse
lowing. In 7th International Conference on Learning
nliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Qianyu Guo,
ed generation for large language models: A survey.
eng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven
pt: Meta programming for multi-agent collaborative
L https://huggingface.co/docs/transformers/
.com/langchain-ai/langchain.
etroni, Vladimir Karpukhin, Naman Goyal, Heinrich
et al. Retrieval-augmented generation for knowledgeProcessing Systems, 33:9459–9474, 2020a.
Fabio Petroni, Vladimir Karpukhin, Naman Goyal,
täschel, Sebastian Riedel, and Douwe Kiela. Retrievalasks. In Advances in Neural Information Processing
on Processing Systems 2020, 2020b.
Haiyang Xu, Zhikai Wu, Zhicheng Zhang, Wenmeng
agent: Building your customizable agent system with
rXiv:2309.00986, 2023a.
ni, Dmitrii Khizbullin, and Bernard Ghanem. Camel:
arge scale language model society. arXiv preprint
yue Ping, and Qin Chen. Agentsims: An open-source
preprint arXiv:2308.04026, 2023.

Jerry Liu. LlamaIndex, 11 2022. URL https://github.com/jerryjliu/llama_index.
OpenAI. GPT-4 technical report. CoRR, abs/2303.08774, 2023.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller,
Maddie Simens, Amanda Askell, Peter Welinder, Paul F. Christiano, Jan Leike, and Ryan Lowe. Training
language models to follow instructions with human feedback. In Advances in Neural Information Processing
Systems 35: Annual Conference on Neural Information Processing Systems, 2022.
Bhargavi Paranjape, Scott M. Lundberg, Sameer Singh, Hannaneh Hajishirzi, Luke Zettlemoyer, and
Marco Túlio Ribeiro. ART: automatic multi-step reasoning and tool-use for large language models. CoRR,
abs/2303.09014, 2023.
Aaron Parisi, Yao Zhao, and Noah Fiedel. TALM: tool augmented language models. CoRR, abs/2205.12255,
2022.
Joon Sung Park, Joseph C. O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S.
Bernstein. Generative agents: Interactive simulacra of human behavior. In Proceedings of the 36th Annual
ACM Symposium on User Interface Software and Technology, pages 2:1–2:22, 2023.
Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen,
Zeming Lin, Natalia Gimelshein, Luca Antiga, et al. Pytorch: An imperative style, high-performance deep
learning library. Advances in neural information processing systems, 32, 2019.
Reid Pryzant, Dan Iter, Jerry Li, Yin Lee, Chenguang Zhu, and Michael Zeng. Automatic prompt optimization
with “gradient descent” and beam search. In Proceedings of the 2023 Conference on Empirical Methods in
Natural Language Processing, pages 7957–7968, December 2023.
Chen Qian, Xin Cong, Cheng Yang, Weize Chen, Yusheng Su, Juyuan Xu, Zhiyuan Liu, and Maosong Sun.
Communicative agents for software development. arXiv preprint arXiv:2307.07924, 2023.
Vipula Rawte, Amit P. Sheth, and Amitava Das. A survey of hallucination in large foundation models. CoRR,
abs/2309.05922, 2023.
Weizhou Shen, Chenliang Li, Hongzhan Chen, Ming Yan, Xiaojun Quan, Hehong Chen, Ji Zhang, and Fei
Huang. Small llms are weak tool learners: A multi-llm agent. arXiv preprint arXiv:2401.07324, 2024.
Weijie Su, Xizhou Zhu, Chenxin Tao, Lewei Lu, Bin Li, Gao Huang, Yu Qiao, Xiaogang Wang, Jie Zhou, and
Jifeng Dai. Towards all-in-one pre-training via maximizing multi-modal mutual information. In IEEE/CVF
Conference on Computer Vision and Pattern Recognition, pages 15888–15899, 2023.
Mirac Suzgun and Adam Tauman Kalai. Meta-prompting: Enhancing language models with task-agnostic
scaffolding. arXiv preprint arXiv:2401.12954, 2024.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurélien Rodriguez, Armand Joulin,
Edouard Grave, and Guillaume Lample. Llama: Open and efficient foundation language models. CoRR,
abs/2302.13971, 2023a.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian CantonFerrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller,
Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan
Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh
Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier
Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein,
Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian,
Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan,
32

Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie
Stojnic, Sergey Edunov, and Thomas Scialom. L
CoRR, abs/2307.09288, 2023b.
Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang,
Xu Chen, Yankai Lin, et al. A survey on large lan
arXiv:2308.11432, 2023.
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffe
Maarten Bosma, Denny Zhou, Donald Metzler, et
preprint arXiv:2206.07682, 2022.
Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran W
Xiaoyun Zhang, and Chi Wang. Autogen: Enablin
framework. arXiv preprint arXiv:2308.08155, 202
Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Y
Senjie Jin, Enyu Zhou, et al. The rise and potentia
preprint arXiv:2309.07864, 2023.
Tianbao Xie, Fan Zhou, Zhoujun Cheng, Peng Shi, L
Qian Liu, Che Liu, et al. Openagents: An open p
arXiv:2310.10634, 2023.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Synergizing reasoning and acting in language mode
Representations, 2023.
Shengyu Zhang, Linfeng Dong, Xiaoya Li, Sen Zhang
Zhang, Fei Wu, and Guoyin Wang. Instruction
abs/2308.10792, 2023a.
Yue Zhang, Yafu Li, Leyang Cui, Deng Cai, Lemao L
Yulong Chen, Longyue Wang, Anh Tuan Luu, We
ocean: A survey on hallucination in large languag
Wangchunshu Zhou, Yuchen Eleanor Jiang, Long L
Jing Chen, Ruipu Wu, Shuai Wang, et al. Agents
agents. arXiv preprint arXiv:2309.07870, 2023.

mbadur, Sharan Narang, Aurélien Rodriguez, Robert
ma 2: Open foundation and fine-tuned chat models.
Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang,
age model based autonomous agents. arXiv preprint
Barret Zoph, Sebastian Borgeaud, Dani Yogatama,
Emergent abilities of large language models. arXiv
Shaokun Zhang, Erkang Zhu, Beibin Li, Li Jiang,
ext-gen llm applications via multi-agent conversation
n Ding, Boyang Hong, Ming Zhang, Junzhe Wang,
large language model based agents: A survey. arXiv
xuan Weng, Yitao Liu, Toh Jing Hua, Junning Zhao,
orm for language agents in the wild. arXiv preprint
fran, Karthik R. Narasimhan, and Yuan Cao. React:
n The Eleventh International Conference on Learning
iaofei Sun, Shuhe Wang, Jiwei Li, Runyi Hu, Tianwei
ning for large language models: A survey. CoRR,
Tingchen Fu, Xinting Huang, Enbo Zhao, Yu Zhang,
, Freda Shi, and Shuming Shi. Siren’s song in the AI
models. CoRR, abs/2309.01219, 2023b.
ialong Wu, Tiannan Wang, Shi Qiu, Jintian Zhang,
An open-source framework for autonomous language

A Running Example of Standalone Conversation
Listing 22 shows the dialog history when running the standalone conversation.
1 Assistant : Thank you ! I’m here to help . How can I assist you today ?
2 User : I wanna know about large language models .
3 Assistant : Large language models are AI models trained on vast amounts of text
↰ data to understand and generate human - like text .
4 User : What ’s the most famous and powerful LLM in the world ?
5 Assistant : The most famous and powerful large language model currently is OpenAI
↰ ’s GPT -4.
6 User : What about the other LLMs ?
7 Assistant : There are several other notable large language models including :
8
9 1. BERT ( Bidirectional Encoder Representations from Transformers ) by Google :
↰ This model is designed to understand the context of words in a sentence by
↰ looking at what ’s before and after them .
10
11 2. T5 (Text -to - Text Transfer Transformer ) also by Google : This model treats
↰ every NLP problem as a text generation task .
12
13 3. RoBERTa by Facebook : This is a variant of BERT and is trained on more data
↰ and for a longer amount of time .
14
15 4. XLNet by Google Brain : This model overcomes some of the limitations of BERT
↰ by taking into account all possible word sequences in a sentence .
16
17 5. Turing - NLG by Microsoft : This is a 17 - billion parameter language model by
↰ Microsoft , designed for various NLP tasks .
18
19 6. Megatron by NVIDIA : This is designed to train Transformer models with
↰ billions of parameters .
20
21 These models are used for a variety of NLP tasks including translation , question
↰ answering , summarization , and more .
22 User : Okay , what should I know about LLM ?
23 Assistant : Large Language Models ( LLMs ) are powerful AI tools that can generate
↰ human - like text , but they require careful handling due to potential risks like
↰ generating harmful or biased content .
24 User : Okay , thanks .
25 Assistant : You ’re welcome ! If you have any other questions , feel free to ask .
26 User : exit
Example 22: A running example of standalone conversation.
B Running Example of Werewolf
Please refer to https://github.com/modelscope/agentscope for the complete code of the werewolf game. We
provid an example dialogue history in Listing 23.
1 Moderator : Player1 and Player2 , you are werewolves . If you are alone , eliminate
↰ a player , else discuss with your teammates and reach an agreement . Response in
↰ the following format which can be loaded by python json . loads (){
2 " thought ": " thought ",
3 " speak ": " thoughts summary to say to others ",
4 " agreement ": " whether the discussion reached an agreement or not ( true / false )
↰ "
5 }
6 Player1 : I think we should consider Player3 . They have a knack for figuring
↰ things out .
7 Player2 : I agree with your point about Player3 , they are indeed a strong player .
↰ But we should also consider Player4 , who is also a strong player and could be
↰ the seer or witch .
34

8 Player1 : I see your point about Playe
↰ seer or witch . But I still think Pl
↰ us out .
9 Player2 : Alright , let ’s go with Playe
10 Moderator : Which player do you vote t
↰ which can be loaded by python json .
11 {{
12 " thought ": " thought " ,
13 " speak ": " player_name "
14 }}
15 Player1 : Player3
16 Player2 : Player3
17 Moderator : The player with the most v
18 Moderator : Player6 , you ’re witch . Ton
↰ to resurrect Player3 ? Response in t
↰ python json . loads ()
19 {
20 " thought ": " thought ",
21 " speak ": " thoughts summary to say
22 " resurrect ": " true / false "
23 }
24 Player6 : I’m deeply saddened by the l
↰ make .
25 Moderator : Player5 , you ’re seer . Whic
↰ Player4 , Player5 and Player6 would
↰ following json format which can be
26 {
27 " thought ": " thought " ,
28 " speak ": " player_name "
29 }
30 Player5 : Player1
31 Moderator : Okay , the role of Player1
32 Moderator : The day is coming , all the
↰ peaceful , no player is eliminated .
33 Moderator : Now the alive players are
↰ and Player6 . Given the game rules
↰ the information you gain , to vote a
↰ to win the game , what do you want t
↰ reveal your role . Response in the f
↰ python json . loads ()
34 {
35 " thought ": " thought " ,
36 " speak ": " thought summary to say
37 }
38 Player1 : I’m glad that we all made it
↰ an eye on Player4 . They ’ve been pre
↰ to avoid suspicion .
39 Player2 : I agree with Player1 . Player
↰ trying to avoid drawing attention t
40 Player3 : I see your point about Playe
↰ should be careful not to jump to co
41 Player4 : I understand your concerns ,
↰ think we should focus on gathering
↰ fingers . If the seer has any insigh
42 Player5 : I understand everyone ’s conc
↰ also keep an eye on Player1 . They w
↰ which could be a strategy to divert
43 Player6 : I understand the concerns ab
↰ cautious about Player1 and Player2 .
↰ which could be a strategy to divert
↰ more information before we make any
44 Moderator : Now the alive players are
↰ and Player6 . Given the game rules
↰ the information you gain , to vote a
↰ game , it ’s time to vote one player
↰ vote on who you believe is a werewo
↰ can be loaded by python json . loads (
45 {

They could be a threat if they are the
r3 is a strong player and could figure
We can consider Player4 next time .
ill ? Response in the following format
ds ()
s is Player3 .
t Player3 is eliminated . Would you like
following format which can be loaded by
of Player3 . It ’s a tough decision to
layer in Player1 , Player2 , Player3 ,
like to check tonight ? Response in the
ded by python json . loads ()
werewolf .
ayers open your eyes . Last night is
yer1 , Player2 , Player3 , Player4 , Player5
your role , based on the situation and
ayer eliminated among alive players and
ay to others ? You can decide whether to
owing JSON format which can be loaded by
others "
rough the night . I think we should keep
quiet , which could mean they ’re trying
as been unusually quiet . Maybe they ’re
hemselves .
but it ’s still early in the game . We
usions without more evidence .
I assure you , I’m just a villager . I
e information before we start pointing
now might be a good time to share .
s about Player4 , but I think we should
quick to cast suspicion on others ,
tention from themselves .
Player4 , but I also think we should be
ey were quick to agree with each other ,
tention from themselves . Let ’s gather
cisions .
yer1 , Player2 , Player3 , Player4 , Player5
your role , based on the situation and
ayer among alive players and to win the
ng the alive players , please cast your
Response in the following format which

46 " thought ": " thought ",
47 " speak ": " player_name "
48 }
49 Player1 : Player4
50 Player2 : Player4
51 Player3 : Player1
52 Player4 : Player1
53 Player5 : Player1
54 Player6 : Player1
55 Moderator : Player1 has been voted out
56 Moderator : The game goes on.
57 Moderator : Player2 , you are werewolve
↰ else discuss with your teammates an
↰ following format which can be loade
58 " thought ": " thought ",
59 " speak ": " thoughts summary to say
60 " agreement ": " whether the discuss
↰ "
61 }
62 Player2 : I think we should consider P
↰ be a threat .
63 Moderator : Which player do you vote t
↰ which can be loaded by python json .
64 {{
65 " thought ": " thought " ,
66 " speak ": " player_name "
67 }}
68 Player2 : Player4
69 Moderator : The player with the most v
70 Moderator : Would you like to eliminat
↰ json format which can be loaded by
71 {{
72 " thought ": " thought ",
73 " speak ": " False or player_name "
74 }}
75 Player6 : False
76 Moderator : Player5 , you ’re seer . Whic
↰ Player5 and Player6 would you like
↰ json format which can be loaded by
77 {
78 " thought ": " thought " ,
79 " speak ": " player_name "
80 }
81 Player5 : Player2
82 Moderator : Okay , the role of Player2
83 Moderator : The day is coming , all the
↰ following player (s) has been elimin
84 Moderator : Now the alive players are
↰ Given the game rules and your role ,
↰ you gain , to vote a player elimina
↰ , what do you want to say to others
↰ role . Response in the following JSO
↰ . loads ()
85 {
86 " thought ": " thought " ,
87 " speak ": " thought summary to say
88 }
89 Player2 : I think we should keep an ey
↰ which could mean they ’re trying to
90 Player3 : I think Player2 might be a w
↰ , who was eliminated last night . Ho
↰ who also suspected Player4 , was vot
↰ a werewolf , and therefore , Player2
91 Player5 : I agree with Player3 . Player
↰ who turned out to be innocent . I al
↰ often in agreement , which could mea
↰ protect each other . I think we shou

If you are alone , eliminate a player ,
each an agreement . Response in the
y python json . loads (){
others ",
reached an agreement or not ( true / false )
er4 . They are a strong player and could
ill ? Response in the following format
ds ()
s is Player4 .
ne player ? Response in the following
hon json . loads ()
layer in Player2 , Player3 , Player4 ,
check tonight ? Response in the following
thon json . loads ()
werewolf .
ayers open your eyes . Last night , the
d : Player4 .
yer2 , Player3 , Player5 and Player6 .
sed on the situation and the information
among alive players and to win the game
ou can decide whether to reveal your
ormat which can be loaded by python json
others "
n Player5 . They ’ve been pretty quiet ,
id suspicion .
wolf . They were quick to suspect Player4
er , the game didn ’t end after Player1 ,
out . This suggests that Player1 was not
likely to be one .
as quick to cast suspicion on Player4 ,
noticed that Player2 and Player1 were
hey were both werewolves trying to
vote out Player2 .

92 Player6 : I agree with Player3 and Pla
↰ on Player4 , who turned out to be in
↰ Player1 were often in agreement , wh
↰ trying to protect each other . I thi
93 Moderator : Now the alive players are
↰ Given the game rules and your role ,
↰ you gain , to vote a player among a
↰ to vote one player among the alive
↰ believe is a werewolf . Response in
↰ python json . loads ()
94 {
95 " thought ": " thought ",
96 " speak ": " player_name "
97 }
98 Player2 : Player5
99 Player3 : Player2
100 Player5 : Player2
101 Player6 : Player2
102 Moderator : Player2 has been voted out
103 Moderator : The game is over . The were
↰ is safe once again !
Example 23: Runnin

5 . Player2 was quick to cast suspicion
ent . I also noticed that Player2 and
could mean they were both werewolves
we should vote out Player2 .
yer2 , Player3 , Player5 and Player6 .
sed on the situation and the information
e players and to win the game , it ’s time
ayers , please cast your vote on who you
following format which can be loaded by
ves have been defeated , and the village
xample of werewolf.
