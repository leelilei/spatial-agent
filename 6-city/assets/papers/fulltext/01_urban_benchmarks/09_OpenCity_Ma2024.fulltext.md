---
title: "Introduction"
source_pdf: "01_urban_benchmarks\\09_OpenCity_Ma2024.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-06-21T17:31:40+00:00
page_count: 15
status: ok
text_char_count: 48868
quality_flags: []
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\01_urban_benchmarks\09_OpenCity_Ma2024.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-06-21T17:31:40+00:00
- Page count: 15
- Status: ok
- Text chars: 48868
- Quality flags: none

## Metadata

- Title: Introduction
- Author: unknown
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

Agent-based models (ABMs) have long been employed to explore how individual behaviors aggregate into complex societal phenomena in urban space. Unlike black-box predictive models, ABMs excel at explaining the micro-macro linkages that drive such emergent behaviors. The recent rise of Large Language Models (LLMs) has led to the development of LLM agents capable of simulating urban activities with unprecedented realism. However, the extreme high computational cost of LLMs presents significant challenges for scaling up the simulations of LLM agents. To address this problem, we propose OpenCity, a scalable simulation platform optimized for both system and prompt efficiencies. Specifically, we propose a LLM request scheduler to reduce communication overhead by parallelizing requests through IO multiplexing. Besides, we deisgn a “group-and-distill” prompt optimization strategy minimizes redundancy by clustering agents with similar static attributes. Through experiments on six global cities, OpenCity achieves a 600-fold acceleration in simulation time per agent, a 70% reduction in LLM requests, and a 50% reduction in token usage. These improvements enable the simulation of 10,000 agents’ daily activities in 1 hour on commodity hardware. Besides, the substantial speedup of OpenCity allows us to establish a urban simulation benchmark for LLM agents for the first time, comparing simulated urban activities with real-world data in 6 major cities around the globe. We believe our OpenCity platform provides a critical infrastructure to harness the power of LLMs for interdisciplinary studies in urban space, fostering the collective efforts of broader research communities. Code repo is available at https://anonymous.4open.science/r/Anonymous-OpenCity-42BD.

## Outline

- Introduction (page 1)
- Related Works (page 3)
  - LLM Agents (page 3)
  - LLM Deployment Optimization (page 3)
- Preliminaries (page 3)
  - LLM Agents for Urban Activities (page 3)
  - Time Cost Analysis (page 4)
- OpenCity Platform (page 4)
  - LLM Request Scheduler (page 4)
  - Group-and-Distill Meta-Prompt Optimizer (page 5)
  - Web Portal (page 6)
- Benchmark (page 7)
  - Dataset and Setup (page 7)
  - Acceleration Performance (page 7)
  - Reproducing Urban Dynamics (page 8)
- Case Study: Experienced Urban Segregation (page 9)
- Conclusion (page 10)
- Urban Mobility Dataset (page 13)
- Urban dynamic metrics (page 13)
- Image supplements (page 14)

## Markdown Content

OPENCITY: A SCALABLE PLATFORM TO SIMULATE URBAN
ACTIVITIES WITH MASSIVE LLM AGENTS
Yuwei Yan∗1, Qingbin Zeng∗2, Zhiheng Zheng3, Jingzhe Yuan2, Jie Feng2, Jun Zhang2, Fengli Xu† 2, and Yong Li† 2
1Information Hub, The Hong Kong University of Science and Technology (GuangZhou)
2Department of Electronic Engineering, Tsinghua University
3Shenzhen International Graduate School, Tsinghua University
October 30, 2024
ABSTRACT
Agent-based models (ABMs) have long been employed to explore how individual behaviors aggregate
into complex societal phenomena in urban space. Unlike black-box predictive models, ABMs excel
at explaining the micro-macro linkages that drive such emergent behaviors. The recent rise of Large
Language Models (LLMs) has led to the development of LLM agents capable of simulating urban activities with unprecedented realism. However, the extreme high computational cost of LLMs presents
significant challenges for scaling up the simulations of LLM agents. To address this problem, we
propose OpenCity, a scalable simulation platform optimized for both system and prompt efficiencies.
Specifically, we propose a LLM request scheduler to reduce communication overhead by parallelizing
requests through IO multiplexing. Besides, we deisgn a “group-and-distill” prompt optimization strategy minimizes redundancy by clustering agents with similar static attributes. Through experiments
on six global cities, OpenCity achieves a 600-fold acceleration in simulation time per agent, a 70%
reduction in LLM requests, and a 50% reduction in token usage. These improvements enable the simulation of 10,000 agents’ daily activities in 1 hour on commodity hardware. Besides, the substantial
speedup of OpenCity allows us to establish a urban simulation benchmark for LLM agents for the first
time, comparing simulated urban activities with real-world data in 6 major cities around the globe. We
believe our OpenCity platform provides a critical infrastructure to harness the power of LLMs for interdisciplinary studies in urban space, fostering the collective efforts of broader research communities.
Code repo is available at https://anonymous.4open.science/r/Anonymous-OpenCity-42BD.
1 Introduction
Agent-based models (ABMs) were first introduced to urban studies in the seminal work of Thomas Schelling about
50 years ago [1], which ingeniously explained how segregation can emerge as the aggregation of individual choices.
Compared to black-box predictive models, ABMs offer the unique advantage of explaining the underlying mechanisms
behind aggregated phenomena [2], i.e., revealing the connections between “micro-motives” and “macro-behaviours.”
As a result, ABMs play an important role in many research areas [3], including computational social sciences, urban
planning and public health. The recent advance of Large Language Models (LLMs) have driven the rise of LLM
agents [4, 5], which leverage LLM’s remarkable capabilities of commonsense reasoning and role-playing to simulate
human behaviours. Unlike previous rule-based agents, these emerging LLM agents generate far more realistic human
behaviours [4, 6], and can also explain their inner motives via prompting techniques like chain-of-thoughts [7].
Therefore, LLM agents hold great potential to harness the power of language models in transforming urban studies.
*Equal Contribution.
†Corresponding authors.
Preprint. Under review.
4202
tcO
11
]AM.sc[
1v68212.0142:viXra

Despite this promising outlook, LLM agents also face sev
In the pioneering work of Park et al. [4] only 15 LLM a
reason is the prohibitive simulation time, which can be br
slow due to their enormous model sizes; on the other han
which introduces significant time delay due to network tra
worse, the prompt design of urban LLM agents often inv
perceived environment [4, 8]. This important feature prev
small sample of the population [9], as LLM agents need t
essential for simulating a vibrant and diverse urban popu
In this paper, we present OpenCity, a scalable platform tha
to enable efficient LLM agent simulation in urban environ
leverages the scalable I/O event notification mechanism
network transmission delay. This design is based on ou
generated output account for only a small portion of tota
for LLM responses and the repeatedly establishing TCP
scheduler uses the scalable I/O event notification mech
I/O portal and TCP connections while waiting for resp
interdependencies of LLM requests and local computatio
locations, ensuring local computation tasks are optimall
optimizations enable large-scale LLM agent simulation
optimization, OpenCity introduces a novel “group-and-di
LLMs. The key idea is to identify the clusters of LLM ag
gender and income level, and use shared context in batch
“group-and-distill” strategy leverages the in-context learn
workflow that automatically discovers clusters of LLM ag
Agents within the same clusters are grouped into a batch p
prefix for grouped agents. Finally, OpenCity also features
configuration and result visualization. This design mini
LLM agents, ensuring our OpenCity platform can benefi
We evaluate the efficiency and faithfulness of OpenCity i
using the widely adopted Generative Agent workflow
635x acceleration in simulations with 10,000 LLM agen
reduced by 73.7% and 45.5%, respectively. OpenCity als
reducing from 36.25 to 0.06 seconds as the simulation siz
simulations allow for more efficient LLM request schedul
maintains high faithfulness of the simulated behaviour. Sp
of our method are comparable to the standard prompting
straightforward reusing strategy [9]. Besides, the top-1 hi
GPT-4o.
The substantial simulation acceleration allows us to ben
activities for the first time. We use classic evaluation me
matrix [14], and segregation index [15] to assess LLM ag
that characterize urban residents’ activities at both individ
Our experiments show that LLM agents perform comp
EPR [16]. Moreover, LLM agents enable counterfactual
without residential segregation [17]. They also allow re
behaviors, offering valuable insights for urban policy-ma
We believe our OpenCity platform can serve as a critical
plinary studies in urban space. It not only provides high
hardware, but also offers a user-friendly web portal that a
access this technology. It will facilitate a broader resear
evaluate, analyze and inform their projects.

A PREPRINT - OCTOBER 30, 2024
challenges of scaling up due to the high computation time.
ts were employed to simulate a small village. One main
n down into two parts: on one hand, LLMs are inherently
powerful commercial LLMs are only accessible via APIs,
ission, further slowing down simulation. To make matters
e dynamic elements, such as the changing memories and
s the straightforward reuse of simulated behaviors from a
aintain independent memories and experiences, which are
on.
roduces both system-level and prompt-level optimizations
nts. Specifically, we design an LLM request scheduler that
operating system (e.g., epoll in Linux [10]) to minimize
y observation that sending LLM requests and receiving
ommunication time, while the rest are wasted on waiting
nections [11]. To address this problem, the LLM request
sm to parallelize LLM requests by reusing the network
es. Besides, LLM request scheduler also analyzes the
sks, e.g., updating agent’s memory and retrieving nearby
stributed across multiple CPU cores. These system-level
run on commodity hardware. As for the prompt-level
” prompt strategy to minimize the input token required by
s that share semantically similar static elements, e.g., age,
mpting [12] to reduce token redundancy. Specifically, our
capabilities of LLMs to implement a prototype learning
s with semantically similar static elements for simulation.
pt, and we design a “prompt distillation” to extract shared
easy-to-use web portal that facilitates code-less simulation
es the program requirement for running simulation with
earchers from all background.
mulating the urban activities of 6 cities around the world
Our experiments show OpenCity achieves an average
Besides, the number of requests and consumed tokens are
ows strong scalability, with the simulation time per agent
creases from 1 to 10,000 agents, demonstrating that larger
and prompt distillation. More importantly, OpenCity also
fically, the Jensen–Shannon divergence and top-1 hit rates
hnique of batch prompting [12], and substantially surpass
e can reaches up to 96% when using powerful LLMs like
mark LLM agents’ ability to replicate large-scale urban
res such as the radius of gyration [13], origin-destination
’ simulations. These are the most widely adopted metrics
and group levels, and across physical and social domains.
bly to, or better than, traditional rule-based agents like
yses, such as evaluating experienced segregation in cities
rchers to interrogate LLM agents’ motives behind their
g.
astructure to unleash the power of LLMs in the interdiscieedup that allows large simulation to run on commodity
s researchers with minimum programming background to
ommunity and other stakeholders to use LLM agents to

A PREPRINT - OCTOBER 30, 2024
2 Related Works
2.1 LLM Agents
With the widespread use of large language models (LLMs) in various applications, the limitations of LLMs, e.g.,
unstable reasoning abilities, limited memory capacity, and lack of specialized expertise, have been exposed to the public.
As one of the potential solution, LLM agents are proposed to overcome these limitations and promote the practical
application of LLMs. AutoGPT [18] as one of the most popular LLM autonomous agent explore the potential of applying
LLM to enable the autonomous planning and task-solving. After that, LLM agents [19, 20] have made significant
progress in two directions: task-oriented agents and simulation agents. Following the first direction, researchers aim to
improve LLM agent’s ability to solve complex tasks. For example, lots of programming agents, such as ChatDev [21],
SWEAgent [22], and MetaGPT [23], are designed to solve the complex programming tasks. As for the second direction,
generative agents [4] have demonstrated the potential of large models in simulating human behavior, which has been
further validated in subsequent research. S3 [24] explores the potential of using LLM agents to simulate the social
network. CoPB [6] defines a agentic workflow to simulate the mobility behaviors. RecAgent [25] simulate the user
behavior in the recommendation system. While these works demonstrate the potential of LLM agents, the large scale
efficient simulation of generative agents becomes the critical bottleneck of further applications.
2.2 LLM Deployment Optimization
To support the efficient inference of LLMs and LLM agents, enormous works and systems [26] are designed to optimize
the inference efficiency of LLMs and further accelerate their practical applications. For example, Flash-attention [27] is
an IO-aware exact attention algorithm which uses tiling to reduce the number of memory reads/writes within GPU.
AWQ [28] is an activation-aware weight quantization to compress and accelerate the LLM inference. vLLM [29]
proposes pagedAttention mechanism to enable highly efficient KV cache scheduler during the inference and becomes
the most population open source LLM inference engine. SGLang [30] provides a flexible frontend language to enable
the efficient autonomous optimization of LLM inference. Synergy-of-thought [31] proposes to exploit the synergy
between larger and smaller language models for efficient reasoning. While these systems are designed to process the
general LLM inference, specific characteristics of generative agents especially urban generative agents are ignored
which can be employed to further accelerate the inference and simulation. In this paper, we explore the potential of this
direction and design the OpenCity platform.
3 Preliminaries
3.1 LLM Agents for Urban Activities
We focus on using LLM agents to reproduce urban dynamics characterized primarily by physical mobility. Consider
an urban environment E containing N LLM agents. The state of agent i at simulation time t, denoted as S (t) =
i
{s , m (t)}, consists of both static properties s and dynamic properties m (t). Static properties, like the agent’s
i i i i
demographics, remain constant throughout the simulation, while dynamic properties, such as memory and perceived
environment information, change frequently and are hard to predict. We can represent the state update of agent i using
a function f :
m (t + 1) = f (s , E, m (t); S (t + 1) = {s , m (t + 1)} (1)
i i i i i i
Here, m (t + 1) is the updated memory of agent i at time t + 1, and the function f models how the agent updates
i
its state by perceiving the urban environment E, reflecting on its memory m (t), and interacting with the LLM. The
i
individual trajectory of agent i, denoted as T , describes the trajectory of the agent over time in the urban environment E.
i
If the location of agent i at time t is represented by L (t), which depends on its state S (t), then the individual trace can
i i
be expressed as T = {L (0), L (1), L (2), ..., L (t )}, where t is the the total simulation time. Along with individual
i i i i i s s
(cid:80) (cid:80)
mobility, we also examine the aggregated mobility features A = Φ( ϕ( S (t))), such as Original-Destination
i t i
(OD) matrix and income segregation index, which reflects the urban dynamics involving states of all agents.
To simulate LLM agents in the urban space, we set the initial state for the agents and environment {S (0)|i ∈ N } and
i
then apply the Equation 1 for each agent at every simulation step. When the number of agents increases, challenges
arise mainly because of the LLM request process. LLMs are inherently slow due to their parameter size, and when using
commercial LLMs accessed via APIs, response times can be further delayed, especially with poor network conditions.
Some have proposed reusing the LLM response for agents can improve the efficiency [9], but it requires that the agents
have the completely same state or have limit kinds of state that can be easily predicted. What’s more, simply reusing
the response would eliminate the independence of agents and reduce the faithfulness of the simulation results. Urban
3

agent i has dynamic memory m (t) that evolves during t
i
memory m (t ) but also on the current environment. Sin
i h
LLM, predicting an agent’s future state or finding an agen
Therefore, to simulate the large-scale and reliable LLM a
insufficient.
3.2 Time Cost Analysis
In light of the prevailing dominance of remote LLM serv
agents simulation, a decomposition of the time required
in Fig.1(b). The first phase is the initialization and rec
connection and destruction time between the simulation s
transmission and waiting time. For a single LLM request
in comparison to the third, and the core time consumptio
The simulation of large-scale agents necessitates the issua
the presence of waiting periods, impairs the overall effi
are not fully utilized. Consequently, the effective sched
utilization of system resources, which in turn improves the
required for LLM inference is directly proportional to th
important to reduce the number of tokens consumed per
From this vantage point, the present work puts forth an
method, which can markedly enhance the efficiency of la
4 OpenCity Platform
We devise a scalable platform OpenCity to accelerate t
prompt-level. The OpenCity platform aims to substantially
high simulation fidelity. Besides, OpenCity also provide
researchers from diverse background. The key designs ar
4.1 LLM Request Scheduler
As shown in Fig.1(a), for a LLM agent, the dependency
LLM request to be initiated after the previous one is com
of a fixed network environment and request content. In c
dependency between their LLM requests. In order to ach
have implemented an IO multiplexing scheme (based on e
system. This allows the operating system to manage IO
data transmission in the simulation system. Consequentl
required for the first and second phases (Time saving#1 i
Furthermore, the considerable number of LLM calls nec
service provider, resulting in a considerable overhead in th
given that the content of LLM requests is inherently link
same connection for multiple agents, thereby reducing th
of reusable connections is maintained within the system
content is populated into an available connection, thus av
additionally reduces the mean time consumption of LLM
For those agents with CPU tasks during the computation p
CPU resources by the computation load will inevitably res
agents. To mitigate the adverse effects of this issue on th
as "local IO", offload it to available cores for computatio
result to the designated agent upon completion of the com
of asynchronous LLM requests (Time saving#3 in Fig.1(
The proposed LLM request scheduler is designed to redu
during the simulation runtime. Based on the supporting a
the efficiency of large-scale LLM agents.

A PREPRINT - OCTOBER 30, 2024
imulation. This memory m (t) depends not only on past
i
decision-making and memory updates rely heavily on the
ith an identical state to reuse an LLM response is difficult.
ts for urban dynamics, a simple response reuse strategy is
invocations in the current operational landscape of LLM
a single LLM request can be undertaken, as illustrated
on time for the LLM request, the second is the TCP/IP
m and the LLM service provider, and the third is the data
e overhead of the first and second phases is relatively low
derived from the data transmission and waiting.
of a considerable number of LLM requests, which, given
ncy of the simulator. Furthermore, the system resources
g of LLM requests is essential for enhancing the overall
erall efficiency of the simulation. Furthermore, as the time
umber of tokens contained in an LLM request, it is also
nt while compressing the number of requests.
acious LLM request scheduler and a prompt distillation
scale LLM agents simulation.
imulation of urban LLM agents from both system- and
duce the simulation time per LLM agent while maintaining
user-friendly web interface to facilitate the easy access of
troduced as follows.
ween its LLM requests—that is, the necessity for the next
ed—results in a constant waiting time under the condition
rast, for a system comprising multiple agents, there is no
e asynchronous processing of multiple LLM requests, we
in Linux) which eliminates waiting time in the simulation
iting, thereby achieving the desired "zero-awareness" of
he average time for a LLM request is reduced to the time
g.1(c)).
tates the frequent establishment of connections with the
tablishment and destruction of each connection. However,
to the corresponding agent, it is possible to leverage the
erall performance overhead. To address this issue, a pool
on initiation of an LLM request by an agent, the request
ng the establishment of a new connection. This approach
uests (Time saving#2 in Fig.1(c)).
ess, it is important to note that the continued occupation of
n a delay in the sending of LLM requests from subsequent
ystem’s overall performance, we categorize the CPU task
hrough a multi-core parallel scheme, and then return the
tation. This approach further ensures the stable operation
he waiting time for a significant number of LLM requests
liary scheme, it has the potential to significantly enhance

Figure 1: The functionality of th
4.2 Group-and-Distill Meta-Prompt Optimizer
A further crucial method for enhancing the efficiency of th
by agents and the quantity of tokens consumed by said ag
of a single LLM request across multiple agents. Howev
fine-grained urban LLM agent simulations, each agent po
scheme compromises the independence of agents, which i
through large-scale LLM agents. Furthermore, for agents
the result of a single LLM request, as shown in Fig.2(a).
To address this issue, we propose the Group-and-Distill
group information in lieu of the static attributes of the ag
at runtime and realizes prompt by sharing group inform
dynamic properties. The optimizer is comprised of two d
distill meta-prompt.
The inputs and outputs of IPL are defined as follow:
IP L({s },
i
in which, {s } is the collection of agent’s static properties;
i
T is the threshold for decision making; G is the collect
agents.
Input the static properties of a set of agents, IPL first g
the corresponding description information. Subsequen
static properties of the agent to LLM, which analyzes
on the group description and provides the quantization
the result is greater than T , IPL assigns the agent to the
describes the characteristics of the group. In comparison t
a fixed parameter space, IPL exhibits enhanced general
semantic-level knowledge in the prototyping process.
efficiently summarize the static attribute characteristics o
The distill meta-prompts obtained through a systematic e
employed to generate the prompts (details can be found
proposed a raw prompt design diagram, which divides the
section, and the input section. The generation process, wh
summarization, context extraction, information sharing, an

A PREPRINT - OCTOBER 30, 2024
oposed LLM Request Scheduler.
mulation is to reduce the number of LLM requests issued
. A conventional approach is to reuse the generated result
this approach presents two significant drawbacks: 1. In
sses its own dynamic properties. Consequently, the reuse
tithetical to the objective of conducting urban simulations
h dynamic properties, it is inherently impossible to share
a-Prompt Optimizer (depicted in Fig.2), which employs
This approach aggregates requests from multiple agents
on and context information while preserving the agent’s
nct components. In-context prototype learning (IPL) and
T ) → G, D (2)
controls the number of agents in initial prototype learning;
of agent groups; D is the descriptions for each group of
ps the first M agents, providing both group results and
IPL classifies the remaining agents by transmitting the
likelihood of the agent belonging to each group based
ult. By comparing the quantization result with T , when
ecified group. Otherwise, it constructs a new group and
nventional prototype learning methods that operate within
ion capabilities and a particular aptitude for leveraging
prototype information obtained by IPL is employed to
e set of agents within the specified group.
mination of the original prompts and the CoT approach is
Fig.A1). To facilitate the generation procedure, we have
ompt into three sections: the function section, the variable
is initiated with a given raw prompt, comprises four steps:
ewriting of the raw prompt into the distill meta-prompt. In

Figure 2: Overview of Group-a
the operational phase, the requests from the agents in a gr
effect of reducing the number of LLM requests and the c
The proposed prompt optimizer enables further enhancem
while maintaining agent dynamic properties.
4.3 Web Portal
A web portal has been designed for the utilisation of Op
system. This enables users to rapidly configure simula
facilitating the storage of simulation data and urban infr
concept underlying the design of this portal is user-friendl
of urban research. We have developed a rapid, code-free
thereby facilitating the seamless engagement of experts f
User-friendliness: In order to enhance the usability of
with the incorporation of the LLM agent blueprint const
function module in order to construct complex logic for L
function is based on the established LLM agent developm
and incorporates several fundamental modules oriented t
sensing. The blueprint offers an efficient and agile devel
the rapid iteration of simulation methods and theories.
Basic workflow: The primary process of urban LLM age
phases: citizen profile configuration, deployment and si
citizen profile is facilitated by the provision of a conso
administer the simulation tasks they have created on the p
user is able to bind the execution logic designed in the bl

A PREPRINT - OCTOBER 30, 2024
Distill Meta-Prompt Optimizer.
are aggregated into a single Distill request, which has the
umption of tokens.
of simulation efficiency and reduction of simulation cost
ity, encompassing the frontend, backend, and simulation
conditions and visualise simulation results, as well as
ucture information within a database. The fundamental
s, particularly given the inherently interdisciplinary nature
nfiguration approach tailored to the needs of researchers,
diverse fields with our simulation platform.
OpenCity platform, the Web Portal has been augmented
ion function. Users are able to drag and drop each basic
M agents. In order to meet a variety of needs, the blueprint
frameworks, such as Langchain [32] and AutoGPT [33],
rds urban simulation, including environmental and traffic
ent solution for interdisciplinary researchers, facilitating
mulation on this web portal is comprised of three distinct
ation, and results presentation. The configuration of the
ub, which enables users to efficiently and transparently
orm, along with the agents within those simulations. The
int to different agents and to configure their profiles with

great rapidity via the web interface. This may entail selec
manually. Once the configuration process is complete, us
single click, leveraging the backend system and simulati
enables users to observe the real-time outcomes of ongo
Finally, after the simulation has concluded, users can acce
format, such as Origin-Destination (OD) maps. An exem
Figure A2.
5 Benchmark
5.1 Dataset and Setup
Dataset We collect urban mobility data in 6 major cities
Paris, and Sydney. The data sources vary. Beijing’s data
network platform. New York and San Francisco source f
other three cities are from Foursquare which consist of th
we have done some preprocess method, such as trajectory
be seen in Appendix A.
Architecture of LLM Agent The main agent used in Ope
agent [4]. Generative agents use a framework that involve
creates a daily plan to ensure the trajectory is reasonable.
current perceptions and memory. After taking action, the
Once the memory stream reaches a threshold, the agent r
well in the OpenCity platform.
We also have rule-based agent for comparison, such as th
This work make agent choose to explore a new locatio
some parameters to compute the probability. In this pape
exploration-return trade-off parameter γ = 0.21, waiting
5.2 Acceleration Performance
This section presents an evaluation of the performance o
Agent (Tested on Huawei ECS Cloud Server - Intel(R) X
256 GB RAM). The performance of the platform was eva
presented in Table.1, where the following variables are de
Rr denotes the LLM request number reduction rate, and
The results demonstrate that OpenCity exhibits substant
0.058s per LLM agent and an average speedup of 635.3x
scheme is capable of markedly reducing the number of LL
of 73.7% and 45.5%, respectively.
To assess the scalability of OpenCity, we conducted a se
under varying orders of magnitude of agents. The results
represents the simulation time without optimization. The
scalable, with a notable enhancement in acceleration effe
This is due to the fact that as the number of agents increas
increases. This, in turn, allows the advantages of the LL
better utilisation of system resources.
Furthermore, faithfulness experiments are conducted to de
preserve the distinctive personality traits of the agents. T
which requires the combination of agent properties to se
between the performance of four distinct methods, includ
ing [12], archetype prompting [9], and the proposed meth
selection was performed 100 times for each agent with the
by counting the distribution of selections (JSD) as well
where Inherent denotes the bias present in LLM itself (ra

A PREPRINT - OCTOBER 30, 2024
a city, selecting an existing profile, or filling out a profile
can deploy and initiate simulations on the platform with a
ystem. The web portal also offers a monitor page, which
simulations and assess the performance of their agents.
he portal to view macroscopic statistical results in a visual
r of the proposed web portal in operation can be found in
ound world: Beijing, New York, San Francisco, London,
mes from a related work [6], which collected from social
Safegraph for aggregated population flow data. And the
sands of check-ins data. To make better use of these data,
er, home extraction and profile sampling. More details can
y platform to simulate the urban dynamic is the generative
rception, planning, and reflection. A generative agent first
en the agent arrives at a POI, it makes decisions based on
nt records the action and the POI into its memory stream.
cts. The results show that the generative agent to function
mous Explore and Preferential-Return (EPR) model [16].
return to the visited location. Decisions are related to
e set the parameters as follows: exploration rate ρ = 0.6,
e distribution parameters τ = 17, β = 0.8.
e OpenCity platform in conjunction with the Generative
(R) Platinum 8378C CPU @ 2.80GHz with 64 cores and
ted in six major cities with 10,000 agents. The results are
d: Speedup denotes the improvements in simulation time,
denotes the token number reduction rate.
acceleration in all test cities, with an average runtime of
simulation time. Furthermore, the proposed acceleration
equests and token consumption, with an average reduction
s of simulations to evaluate its acceleration performance
his analysis are presented in Fig.3, in which the baseline
lts demonstrate that OpenCity’s acceleration capability is
when the number of agents is increased from 10 to 10,000.
he number of groups obtained based on IPL also gradually
equest scheduler to be fully realised, thereby ensuring a
nstrate that the Group-and-Distill optimizer can effectively
testbed for this evaluation is location choice generation,
the next location to visit. A comparison was conducted
raw prompting (without any modification), batch promptOne hundred agents were randomly selected and location
me context. The effectiveness of the method was evaluated
the top-1 hit rate (T 1). The results are shown in Table.2,
rompt method).

Cities Time Speedup Rr T r
Beijing 0.07s 521.7 73.2% 38.7%
New York 0.06s 624.7 67.3% 37.6%
San Francisco 0.07s 588.6 80.3% 51.3%
London 0.04s 792.5 74.6% 49.9%
Paris 0.06s 640.0 76.3% 48.6%
Sydney 0.05s 644.0 70.7% 46.6%
Average 0.058s 635.3 73.7% 45.5%
Table 1: Acceleration experiment results
Inherent Batch pr
Model and Cities
JSD T 1 JSD
BJ 0.04 ± 0.02 90% 0.11 ± 0.
NY 0.02 ± 0.01 92% 0.07 ± 0.
SF 0.03 ± 0.02 88% 0.09 ± 0.
4o-mini
Lo 0.06 ± 0.04 89% 0.12 ± 0.
Pa 0.05 ± 0.02 86% 0.17 ± 0.
Sy 0.04 ± 0.03 85% 0.08 ± 0.
NY 0.003 ± 0.002 98% 0.012 ± 0.
GPT-4o
Pa 0.004 ± 0.002 99% 0.021 ± 0.
Table 2: Faithfuln
As evidenced by the results, our method demonstrates
to that observed in the batch prompting method, while
However, the archetype prompting method performs poor
of the reuse-based method to accommodate the dynami
discrepancies observed in the raw prompting method w
assessment was conducted on two cities, New York and Pa
method is capable of approximating the execution of the ra
results indicate that there are notable discrepancies betwe
and the capacity to process lengthy textual content. The c
In general, OpenCity is capable of markedly enhancing th
concurrently preserving the distinctive characteristics o
populations exceeding 10,000 to be maintained at the hou
5.3 Reproducing Urban Dynamics
The significant increase in simulation efficiency enables u
urban dynamics for the first time. We use comprehensive
from individual- to group level, and also from physical d
the radius of gyration [13] for each user. At the group l
social domain, we focus on the income segregation index
the MSE for these three metrics, which are denoted as R
Appendix B.
In this section, we analyze the performance of the Gener
We test both agents in 6 major cities using 1,000 agents. T
the Generative Agent and EPR Agent successfully reprod
LLM Agent performs as well as or better than the classica
semantic understanding ability in urban simulations.

A PREPRINT - OCTOBER 30, 2024
Figure 3: Scalability experiments
pting Archetype prompting Ours
T 1 JSD T 1 JSD T 1
76% 0.89 ± 0.04 8% 0.13 ± 0.02 74%
81% 0.84 ± 0.11 13% 0.06 ± 0.04 86%
77% 0.91 ± 0.03 11% 0.10 ± 0.03 85%
79% 0.86 ± 0.06 9% 0.12 ± 0.04 78%
69% 0.94 ± 0.03 4% 0.14 ± 0.04 71%
75% 0.88 ± 0.05 5% 0.07 ± 0.04 75%
94% 0.89 ± 0.09 10% 0.009 ± 0.004 97%
93% 0.91 ± 0.04 7% 0.010 ± 0.006 96%
experiment results
capacity to maintain a comparable level of consistency
ibiting a reduction in volatility and token consumption.
n this evaluation, which further demonstrates the inability
operties of agents. Furthermore, given the considerable
evaluated using the GPT-4o-mini model, an additional
utilising the GPT-4o model. The findings indicate that our
rompting method to a significant degree. Additionally, the
ifferent models in terms of environmental comprehension
istency of LLM outcomes merits further examination.
ficiency of large-scale urban LLM agent simulations while
e agents themselves. This enables the cost of simulating
level.
benchmark LLM agent’s ability to reproduce large-scale
rics in three-levels to evaluate the simulation performance,
in to social domain. At the individual level, we calculate
, we use the original-destination matrix [14]. As for the
]. To evaluation the simulation performance, we compute
, OD and S . More details can be referred to
E MSE MSE
e Agent and EPR Agent in reproducing urban dynamics.
results are shown in Table 3. The results indicate that both
urban dynamics with low MSE values. Additionally, the
e-based EPR Agent, highlighting the advantage of LLM’s

A PREPRINT - OCTOBER 30, 2024
GenerativeAgent EPR
Cities
R OD S R OD S
MSE MSE MSE MSE MSE MSE
Beijing 19.5 3.88e-4 0.0312 29.8 4.26e-4 0.0630
New York - 5.95e-4 0.3521 - 3.70e-4 0.2319
San Francisco - 23.6e-4 0.1535 - 14.0e-4 0.0352
Paris 2.48 7.58e-4 0.1255 4.04 6.25e-4 0.1240
London 6.24 5.22e-4 0.1258 25.7 7.41e-4 0.1501
Sydney 15.1 4.71e-4 0.1118 54.2 7.63e-4 0.1265
Table 3: Urban dynamics reproduction results
6 Case Study: Experienced Urban Segregation
With the ability to simulate large-scale urban LLM agents, we can conduct counterfactual experiments to explore
outcomes under different policies and design optimal strategies for the future. Conventional rule-based models do
not support this capability, as they are designed to simulate real-world scenarios. Experienced urban segregation is a
widely discussed issue with significant impacts on social dynamics and the economy. It arises from both demographic
differences in residential neighborhoods and the mobility patterns of urban residents [15].
This section provides a case study: a counterfactual simulation is conducted in New York and San Francisco, to observe
how the simulation results change in different configurations, and try to summarize the results with the LLM agents
themselves.
Specifically, we construct the counterfactual scenario by evenly distributing LLM agents with different income levels
across the city, that means we almost eliminate the residential segregation. The results of the income segregation
statistics with CBGs as the statistical granularity are shown in Fig.4, where ‘Original’ samples the segregation results
from the real census data, and ‘Even’ is the result after uniform distribution of agents with different incomes.
Figure 4: The distribution of income segregation index for counterfactual experiment.
From the results, it can be seen that the segregation of the two cities changed significantly after the different income
groups were evenly distributed in the cities. In New York City, the mean segregation index decreases from 0.845 to
0.172, and in San Francisco, the mean segregation index decreases from 0.665 to 0.232. As a result, we believe that
differences between regions are the main cause of segregation as opposed to segregation by choice of action. To extend,
we can know that with policies that promote more even income distribution among neighborhoods, urban segregation
and social inequality can be improved.
Furthermore, we use natural language to communicate with those involved agents to gain deeper insights about urban
segregation. One detailed case is shown in Fig.5. When we ask an agent about its daily journey, it can accurately
provide the time and locations it visited. This is because the agent caches runtime information and uses the LLM’s
ability to understand semantic details. When asked about the people it met, the agent lists everyone it encountered
at different locations and provides their information. This is due to vectorized storage of the agent’s simulation
results and the LLM’s ability to retrieve that information. Collecting and observing fine-grained statistical information
through conversations with agents and even through LLM improves both the interpretability of the simulation and our
understanding of the simulation goals.
9

Figure 5: A detail case of interpreting
7 Conclusion
In this work, we introduced OpenCity, a scalable platform
challenges inherent to the deployment of large-scale LLM
LLM request scheduler and a novel "group-and-distill" p
increase in the efficiency of agent simulations, with a s
The OpenCity platform was evaluated through experime
the platform’s capability to simulate the daily activities o
benchmark for generative agent performance in urban con
with real-world data highlights its potential for real-wor
planners and researchers to explore and understand comp

A PREPRINT - OCTOBER 30, 2024
ulation results through communication.
esigned to address the computational and communication
sed urban agents in city simulations. By incorporating an
mpt optimization strategy, we achieved a notable 600-fold
antial reduction in both LLM requests and token usage.
conducted on six global cities. The results demonstrated
0,000 agents at an hourly level, while also establishing a
ts. The platform’s ability to compare simulated behaviors
rban-scale applications, offering a robust tool for urban
societal phenomena.

References
[1] Thomas C Schelling. Micromotives and macrobeha
[2] Fengli Xu, Yong Li, Depeng Jin, Jianhua Lu, and
human mobility behavior. Nature Computational Sc
[3] Lin Chen, Fengli Xu, Zhenyu Han, Kun Tang, Pan
distribution can simultaneously elevate social utili
2022.
[4] Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, M
Generative agents: Interactive simulacra of human
on user interface software and technology, pages 1–
[5] Fengli Xu, Jun Zhang, Chen Gao, Jie Feng, and Yo
platform for agents in embodied city environment.
[6] Chenyang Shao, Fengli Xu, Bingbing Fan, Jingta
imitation: Generating human mobility from context
arXiv:2402.09836, 2024.
[7] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maar
Chain-of-thought prompting elicits reasoning in large
systems, 35:24824–24837, 2022.
[8] Qingbin Zeng, Qinglong Yang, Shunan Dong, He
reflect, and plan: Designing llm agent for goal-di
arXiv:2408.04168, 2024.
[9] Ayush Chopra, Shashank Kumar, Nurullah Giray-Ku
of agency in agent-based models. arXiv preprint ar
[10] Francesc Bruguera i Moriscot. Benchmarking inpu
[11] Larry L Peterson and Bruce S Davie. Computer net
[12] Zhoujun Cheng, Jungo Kasai, and Tao Yu. Batch pr
arXiv preprint arXiv:2301.08721, 2023.
[13] Marta C Gonzalez, Cesar A Hidalgo, and Albert-L
patterns. nature, 453(7196):779–782, 2008.
[14] Shan Jiang, Yingxiang Yang, Siddharth Gupta, Danie
timegeo modeling framework for urban mobility wi
Sciences, 113(37):E5370–E5378, 2016.
[15] Esteban Moro, Dan Calacci, Xiaowen Dong, and Ale
income segregation in large us cities. Nature comm
[16] Chaoming Song, Tal Koren, Pu Wang, and Albertmobility. Nature physics, 6(10):818–823, 2010.
[17] Douglas S Massey and Nancy A Denton. The dimen
1988.
[18] Significant Gravitas. Autogpt. https://github.
2024-09-01.
[19] Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, H
Yankai Lin, et al. A survey on large language mode
18(6):186345, 2024.
[20] Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yi
Jin, Enyu Zhou, et al. The rise and potential of lar
arXiv:2309.07864, 2023.
[21] Chen Qian, Xin Cong, Cheng Yang, Weize Chen,
Communicative agents for software development. a
[22] John Yang, Carlos E Jimenez, Alexander Wettig, Ki
Swe-agent: Agent-computer interfaces enable autom
2024.

A PREPRINT - OCTOBER 30, 2024
r. WW Norton & Company, 2006.
oming Song. Emergence of urban growth patterns from
ce, 1(12):791–800, 2021.
, James Evans, and Yong Li. Strategic covid-19 vaccine
nd equity. Nature Human Behaviour, 6(11):1503–1514,
dith Ringel Morris, Percy Liang, and Michael S Bernstein.
avior. In Proceedings of the 36th annual acm symposium
2023.
Li. Urban generative intelligence (ugi): A foundational
iv preprint arXiv:2312.11813, 2023.
Ding, Yuan Yuan, Meng Wang, and Yong Li. Beyond
are reasoning with large language models. arXiv preprint
Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al.
guage models. Advances in neural information processing
g Du, Liang Zheng, Fengli Xu, and Yong Li. Perceive,
ed city navigation without instructions. arXiv preprint
Ramesh Raskar, and Arnau Quera-Bofarull. On the limits
2409.10568, 2024.
tput multiplexing facilities of the linux kernel. 2019.
ks: a systems approach. Morgan Kaufmann, 2007.
pting: Efficient inference with large language model apis.
lo Barabasi. Understanding individual human mobility
Veneziano, Shounak Athavale, and Marta C González. The
t travel surveys. Proceedings of the National Academy of
entland. Mobility patterns are associated with experienced
ations, 12(1):4633, 2021.
zló Barabási. Modelling the scaling properties of human
s of residential segregation. Social forces, 67(2):281–315,
m/Significant-Gravitas/AutoGPT, 2023. Accessed:
Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen,
ased autonomous agents. Frontiers of Computer Science,
Ding, Boyang Hong, Ming Zhang, Junzhe Wang, Senjie
anguage model based agents: A survey. arXiv preprint
sheng Su, Juyuan Xu, Zhiyuan Liu, and Maosong Sun.
v preprint arXiv:2307.07924, 6, 2023.
Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir Press.
d software engineering. arXiv preprint arXiv:2405.15793,

[23] Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng C
Yau, Zijuan Lin, Liyang Zhou, et al. Metagpt: Meta
preprint arXiv:2308.00352, 2023.
[24] Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao
Social-network simulation system with large languag
2023.
[25] Lei Wang, Jingsen Zhang, Xu Chen, Yankai Lin, Ru
novel simulation paradigm for recommender system
[26] Xupeng Miao, Gabriele Oliaro, Zhihao Zhang, Xi
wards efficient generative large language model se
arXiv:2312.15234, 2023.
[27] Tri Dao, Dan Fu, Stefano Ermon, Atri Rudra, and
exact attention with io-awareness. Advances in Neu
[28] Ji Lin, Jiaming Tang, Haotian Tang, Shang Yang, W
Dang, Chuang Gan, and Song Han. Awq: Activatio
and acceleration. Proceedings of Machine Learning
[29] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying S
Zhang, and Ion Stoica. Efficient memory managem
Proceedings of the 29th Symposium on Operating S
[30] Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie, Je
Kozyrakis, Ion Stoica, Joseph E Gonzalez, et al. E
arXiv preprint arXiv:2312.07104, 2023.
[31] Yu Shang, Yu Li, Fengli Xu, and Yong Li. Defint: A
hybrid large language models. arXiv preprint arXiv
[32] Keivalya Pandya and Mehfuza Holia. Automating cu
gpt chatbot for organizations. arXiv preprint arXiv:
[33] Hui Yang, Sifu Yue, and Yunzhong He. Auto-gpt for
arXiv preprint arXiv:2306.02224, 2023.

A PREPRINT - OCTOBER 30, 2024
g, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing
gramming for multi-agent collaborative framework. arXiv
ghua Piao, Huandong Wang, Depeng Jin, and Yong Li. S3:
odel-empowered agents. arXiv preprint arXiv:2307.14984,
a Song, Wayne Xin Zhao, and Ji-Rong Wen. Recagent: A
arXiv preprint arXiv:2306.02552, 2023.
o Cheng, Hongyi Jin, Tianqi Chen, and Zhihao Jia. Tog: A survey from algorithms to systems. arXiv preprint
istopher Ré. Flashattention: Fast and memory-efficient
Information Processing Systems, 35:16344–16359, 2022.
Ming Chen, Wei-Chen Wang, Guangxuan Xiao, Xingyu
ware weight quantization for on-device llm compression
d Systems, 6:87–100, 2024.
ng, Lianmin Zheng, Cody Hao Yu, Joseph Gonzalez, Hao
for large language model serving with pagedattention. In
ms Principles, pages 611–626, 2023.
Huang, Chuyue Sun, Cody Hao Yu, Shiyi Cao, Christos
ently programming large language models using sglang.
ault-interventionist framework for efficient reasoning with
02.02563, 2024.
mer service using langchain: Building custom open-source
0.05421, 2023.
ine decision making: Benchmarks and additional opinions.

A Urban Mobility Dataset
As shown in Table A1, we collect urban mobility data o
Beijing, the data is from a related work [6], which gath
mobility trajectories. Additionally, users’ profiles, suc
age, are collected through digital surveys. In New York
provides aggregated population flow among Points of Inte
cities—London, Paris and Sydney—use data are from Fo
data of users and the corresponding venue position.
To make better use of the datasets, we apply several prep
time sequence, and divide the trajectory into units of one
a day, as they do not fully capture users’ mobility patterns
location of the useres the home. Since only the Tencent
users of each city based on local census data for the other
in urban mobility simulations.
Source City Users
[6] Beijing 100000
New york Aggregated
Safegraph San Francisco Aggregated
London 9409
Foursquare Paris 5809
Sydney 1720
Table A1: Basic info
B Urban dynamic metrics
We use comprehensive metrics in three-levels to evaluate
level, and also from physical domain to social domain. Th
patterns and their implications, and can also help us ev
generated trajectory.
At the individual level, we calculate radius of gyration r
g
their movements. The radius of gyration is defined as fol
(cid:118)
(cid:117)
(cid:117) 1
rα = (cid:116)
g N α
where ⃗rα represents the i = 1, 2, ..., N positions record
i
mass of the trajectory. The radius of gyration provides a
the accuracy of our simulation data against real-world da
Error(MSE) of the radius of gyration.
To analyze movement patterns and other aggregated featu
cities with Safegraph data, we use existing Census Block
into evenly spaced grids, with each grid cell representing
At the group level, we count the inflow and outflow of a
(OD) matrix [14], and normalize it. To compare real data
OD matrix, denoted as OD . A smaller OD v
MSE MSE
meaning the movement characteristics of the simulated d
At the social domain, we calculate the income segregation
place α is defined as S = 5 (cid:80) |τ − 1 |, where τ is
α 8 q qα 5 qα
α. The S ranges from 0 to 1. A high S indicates that th
α α
suggesting a high level of income segregation. We denote

A PREPRINT - OCTOBER 30, 2024
major cities around the world. The data sources vary. In
d through a social network platform and tracking users’
income level, gender, occupation, education level and
d San Francisco, the data comes from Safegraph, which
(POIs) and Census Block Groups(CBGs). The other three
quare. Foursquare data consist of thousands of check-ins
ssing methods. We firstly arrange the trajectory points in
Then we filter out trajectories with fewer than 4 points in
r home extraction, we identify the most frequently visited
aset includes user profiles, we make profile sampling for
datasets. In the end, our dataset is optimized for easy use
Trajectory Points Duration
297363263 Oct. 2019 - Dec. 2019
760493
316732 May 2023 - July 2023
173268
85679 Apr. 2012 - Sept. 2013
54170
tion about the dataset
e simulation performance, from individual-level to group
metrics allows us to gain a full understanding of mobility
ate the performance of the simulation by analysing the
] for each user, which is a measure of the spatial extent of
s:
(⃗rα − ⃗rα )2 (3)
i cm
by user α, and rα = 1/N α (cid:80)Nα (⃗rα) is the center of
cm i=1 i
ndication of the size of a user’s activity range. To assess
or a specific user, we calculate R , the Mean Squared
MSE
we define block areas as spatial units within the city. For
oup (CBG) areas. For other cities, we divide the map area
lock area.
ts between block areas, calculate the Origin-Destination
h simulation data, we calculate the MSE of the normalized
e indicates greater similarity between the OD matrices,
closely match the real data.
dex [15] for each block area. The income segregation of a
he proportion of visitors in each income quintile for place
lace α is predominantly visited by a single income group,
as the MSE between the real data and simulation data.
SE

A PREPRINT - OCTOBER 30, 2024
C Image supplements
Figure A1: Distill meta-prompt generation through CoT inference.
14

A PREPRINT - OCTOBER 30, 2024
(a) Agent Construction
(b) Profile Configuration
(c) Simulation Visualization (d) Result Visualization
Figure A2: Overview of OpenCity web portal.
15
