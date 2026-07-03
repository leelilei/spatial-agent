---
title: "Simulating Multi-Stakeholder Decision-Making with Generative Agents in Urban Planning"
source_pdf: "09_surveys\\02_Multi_Stakeholder_Urban_Planning_Gao2025.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-07-03T12:08:32+00:00
page_count: 9
status: ok
text_char_count: 28658
quality_flags: []
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\09_surveys\02_Multi_Stakeholder_Urban_Planning_Gao2025.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-07-03T12:08:32+00:00
- Page count: 9
- Status: ok
- Text chars: 28658
- Quality flags: none

## Metadata

- Title: Simulating Multi-Stakeholder Decision-Making with Generative Agents in Urban Planning
- Author: Jin Gao; Hanyong Xu; Luc Dao
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

Reaching consensus in urban planning is a complex process often hindered by prolonged negotiations, trade-offs, power dynamics, and competing stakeholder interests, resulting in inefficiencies and inequities. Advances in large language models (LLMs), with their increasing capabilities in knowledge transfer, reasoning, and planning, have enabled the development of multi-generative agent systems, offering a promising approach to simulating discussions and interactions among diverse stakeholders on contentious topics. However, applying such systems also carries significant societal and ethical risks, including misrepresentation, privacy concerns, and biases stemming from opinion convergence among agents, hallucinations caused by insufficient or biased prompts, and the inherent limitations of the foundation models. To evaluate the influences of such factors, we incorporate varying levels of real-world survey data and demographic detail, to test agents performance on two decision-making value frameworks, altruism-driven and interest-driven, on a real-world urban rezoning challenge. This approach evaluates the influence of demographic factors such as race, gender, and age on collective decisions in the design of multi-generative agent systems. Our experimental results reveal that integrating demographic and life-value data enhances the diversity and stability of agent outputs. In addition, communication among the generated agents improves the quality of collective reasoning. These findings provide a predictive framework for decision-makers to anticipate stakeholder reactions, including concerns, objections, and support. By enabling the iterative refinement of proposals before public release, the simulated approach fosters more equitable, and cost-effective decisions in urban planning.

## Outline

- Related Works (page 2)
  - Multi-Generative Agent System Applied in Decision-Making (page 2)
  - Real-World Data Augmented Agent-Based Simulations (page 2)
  - Evaluation and Mitigation of Multi-Agent Emergent Bias (page 2)
- Methodology (page 3)
  - Kendall Square Redevelopment Proposal (page 3)
  - Framework and Agent Design (page 3)
  - Simulation Experiments (page 3)
- Findings (page 4)
  - Impact of Communication (page 4)
  - Impact of Opinion and Demographic Information (page 6)
  - Pros and Cons (page 7)
  - Ethical Risks and Recommendations (page 7)
  - Future works (page 8)
- Conclusion (page 8)

## Markdown Content

SIMULATING MULTI-STAKEHOLDER DECISION-MAKING WITH
GENERATIVE AGENTS IN URBAN PLANNING
Jin Gao Hanyong Xu
Massachusetts Institute of Technology Massachusetts Institute of Technology
Cambridge, MA 02139 Cambridge, MA 02139
gaojin@mit.edu hanyongx@mit.edu
Luc Dao
Massachusetts Institute of Technology
Cambridge, MA 02139
daoluc@mit.edu
ABSTRACT
Reaching consensus in urban planning is a complex process often hindered by prolonged negotiations, trade-offs, power dynamics, and competing stakeholder interests, resulting in inefficiencies
and inequities. Advances in large language models (LLMs), with their increasing capabilities in
knowledge transfer, reasoning, and planning, have enabled the development of multi-generative
agent systems, offering a promising approach to simulating discussions and interactions among diverse stakeholders on contentious topics. However, applying such systems also carries significant
societal and ethical risks, including misrepresentation, privacy concerns, and biases stemming from
opinion convergence among agents, hallucinations caused by insufficient or biased prompts, and the
inherent limitations of the foundation models. To evaluate the influences of such factors, we incorporate varying levels of real-world survey data and demographic detail, to test agents performance
on two decision-making value frameworks, altruism-driven and interest-driven, on a real-world urban rezoning challenge. This approach evaluates the influence of demographic factors such as race,
gender, and age on collective decisions in the design of multi-generative agent systems. Our experimental results reveal that integrating demographic and life-value data enhances the diversity and
stability of agent outputs. In addition, communication among the generated agents improves the
quality of collective reasoning. These findings provide a predictive framework for decision-makers
to anticipate stakeholder reactions, including concerns, objections, and support. By enabling the iterative refinement of proposals before public release, the simulated approach fosters more equitable,
and cost-effective decisions in urban planning.
Keywords: transdisciplinary engineering, multi-agent system, decision-making, large language model, urban planning
Introduction
A large language model (LLM) is a type of machine learning model that generates human-like text by learning from
vast amounts of data. Recently, LLMs have shown strong capabilities in transferring knowledge, generalizing across
contexts, and performing reasoning and planning tasks. One exciting development is their integration into multigenerative agent systems, which combine distinct personas, tools, data, and memory to enable rich interactions among
agents. By assigning different roles, expertise, or personality traits to each agent, these systems can simulate complex
collaborations and communications.
Multi-generative agent systems are well-suited for modeling complex social and public decision-making processes.
Cities, in particular, provide an ideal testing ground: urban policy discussions often involve multiple levels of gov6202
naJ
9
]AM.sc[
2v41311.2042:viXra

Simulating Multi-Stakeholder Decision-Ma
ernment and diverse stakeholders, with processes such
procedures aim to ensure that different interests are cons
foreseen complications. In our study area in the US, for e
committee of senior officials, but only after extensive pub
Designing such agent-based simulations for real-world d
erations. First, if the data used to train or inform these age
those biasesamplifying inequalities rather than promotin
individuals, using their personal opinions to generate res
agents view depends on the data it sees and the limited co
may fail to capture the full diversity of stakeholder persp
This research evaluates how incorporating stakeholder p
teristicsaffects the quality and fairness of simulated conv
communication, agent life values, and demographic va
attributes be included when designing such multi-gene
of urban planning. In our case study, agents representin
velopment plan for a rapidly growing neighborhood, usin
1 Related Works
1.1 Multi-Generative Agent System Applied in Deci
Building upon the foundation of traditional agent-base
behaviors, current research extends these systems by in
of LLMs. This advancement enables more realistic si
influential works is Generative Agents by Park et al.[1],
planning, and reflection capabilities can autonomously
structure these emergent behaviors, researchers have inc
agent systems. For example, Ren et al.[2]developed a mu
while Dai et al.[3]examined how environmental conditi
thus fostering social norms and reducing conflicts within
is enhancing decision-making quality through cross-disc
shown by Costabile et al.[4], who demonstrated perform
Additionally, integrating numerical strategic planning w
For instance, Cicero[5]claimed to achieve human-level p
1.2 Real-World Data Augmented Agent-Based Simu
Purely generative agent-based models lack grounding in
overcome this, researchers explored integrating real-wor
enhance simulation realism and representativeness. For i
uals by conditioning LLM agents on extensive personal
in reproducing the individuals’ survey responses, compa
time. Chopra et al.[7]and Hou et al. [8]modeled generati
sus data, demonstrating how demographic factors influen
real-world data. Notably, Chopras work demonstrated t
agents by sampling "LLM archetypes"representative gro
for nuanced behaviors without the need for individual LL
1.3 Evaluation and Mitigation of Multi-Agent Emer
Studies revealed multi-generative agent systems can dev
real-world data samples statistic bias, polarization effects
One common strategy to evaluate the agents biased outp
mated sentiment analysis to track the tone of each agent
emotional tone volatility might correlate with opinion ch
analysis, Bai et al.[13]uses both human scoring and wo
range of educational scenarios.

g with Generative Agents in Urban Planning
proposals, hearings, lobbying, and voting. While these
red, they can also lead to protracted negotiations and unmple, the final decision is made by a vote from a planning
hearings and discussion among stakeholders.
ion-making carries important societal and ethical considcontains biases, the system may unintentionally reinforce
air outcomes. Second, when agents are modeled on real
ses raises questions about consent and privacy. Third, an
t window of the underlying LLM; as a result, simulations
ves in a community.
pectivesparticularly life values and demographic characations. Specifically, we ask: How do different modes of
les influence collective decisions? Should demographic
ve agent systems? We test these questions in the context
rious demographic groups collaborate to propose a redeal survey data to ground their preferences and priorities.
-Making
odeling, which relies on rule-based or stochastic agent
porating the reasoning, action, and memory capabilities
ations of collective decision-making. One of the early
ich demonstrates how agents endowed with observation,
e decisions within small-scale communities. To further
orated social structures and mechanism design into multiagent framework to study the emergence of social norms,
can lead agents to spontaneously form social contracts,
erative multi-agent systems. Another promising direction
nary interactions among different expert agent groups, as
e exceeding that of human crowds in fact-checking tasks.
anguage-based reasoning has also shown great promise.
rmance in playing the strategic game Diplomacy.
ons
ual human data, limiting their real-world applicability; to
emographic and behavioral data into generative agents to
nce, Park et al.[6]simulated over a thousand real individerviews. This approach achieved a high (85%) accuracy
e to the consistency of participants’ own responses over
agents assigned demographic attributes derived from cenhealth-related social behaviors and decisions grounded in
otential for very large-scale simulation with millions of
of agents with similar behavior patternsthereby allowing
for each agent.
t Bias
p emergent biases due to inherent bias on training data,
social conventions[10]or interactions between agents[11].
s sentiment analysis. Elizabeth et al.[12]performed autoterances throughout a group discussion, to evaluate how
es. Another approach is word frequency and lexical bias
requency statistics to detect stereotypes and biases in a

Simulating Multi-Stakeholder Decision-Making with Generative Agents in Urban Planning
2 Methodology
2.1 Kendall Square Redevelopment Proposal
We chose Kendall Square, located in the heart of Cambridge, Massachusetts, USA, as our case study site. Over the
past few decades, this area has undergone dramatic development, becoming a hub for startups and high-tech industries.
However, the rapid growth has also raised concerns about inclusiveness and affordability, with criticism centered on the
displacement caused by gentrification. In 2017, the relocation of the John A. Volpe National Transportation Systems
Center left a 14-acre parcel of land available for urban redevelopment [14]. This decision raised a key challenge: how
to balance economic growth with social responsibility in a rapidly evolving urban landscape. To address this, we
propose two contrasting visions for the use of the site and ask the agents to discuss how much they agree or disagree
with the proposals:
Altruism-driven: Develop low-income housing to address homelessness and the rising living costs.
Interest-driven: Develop a shopping mall to create jobs and stimulate the local economy.
2.2 Framework and Agent Design
We developed our experiments on AutoGen framework [15],
which is flexible in defining agent roles, interaction and customizations including prompts, human-in-the-loop and tool usage.
To simulate government-led community negotiations, we
refactor the framework to facilitate a series of group chat simulations with the structure shown by Figure 1. We developed
eight generative agents representing eight different stakeholders. Each agent connects to ChatGPT-4 Turbo APIs, starting
with a prompt to describe a stakeholder. The prompt consists
of four components:
• Role: a high-level description of the stakeholder
• Demographics: demographic variables such as age,
gender, race, ethnicity, etc.
• Daily Life/Value: detailed description of the stakeholders daily life or personal opinion based on the
survey or interview Figure 1: Agent Communication Setup
• Task and Format: ensure the agents participate in
the discussion based on their own description within
the ChatGPT API context window limit.
The Government is an admin agent, coordinating the group chat by proposing a topic, prompting the next agent
and sharing information. Each generative agent takes turns to opine about the topic. When an agent speaks, the
Government collects the message and broadcasts it to all other generative agents so that all the agents receive and
process each others opinions. If users have inputs, the government also represents the user-agent to convey human
controllers messages to the shared discussion context, to enable human-in-the-loop interactions.
The agent prompt is developed based on actual interviews conducted on site. The interviews include questions about
the interviewees work, life, and their opinions about the Kendall Square Initiative, which is an urban development
project in Main Street to revitalize the area and make it a new entrance into the city. Due to the context window limit
of ChatGPT API, we summarize the interviews into the Role, Demographic, and Daily Life of the agents.
2.3 Simulation Experiments
To facilitate the discussion among the agents, we set the simulation run as the following steps:
1. The generative agents are initialized with the profile prompt.
2. The Government starts the discussion by providing the problem context, the proposals as well as pros and
cons of each proposal.
3

Simulating Multi-Stakeholder Decision-Making with Generative Agents in Urban Planning
Figure 2: Agent Discussion and Evaluation Procedure
3. The Government requests all agents to provide their opinions.
4. When an agent speaks to the Government, the message is broadcast to all other agents to ensure all agents are
aware of each other’s opinions.
5. Once all agents have spoken, the Government requests all agents to vote from 0 (disagree) to 10 (agree) for
each proposal.
We keep the temperature parameter, which decides the randomness and creativity of responses, as 1 (default value,
medium creativity). The agents may generate different results each run. We repeat the run 3 times and record all
results for analysis purposes. To assess how the communication, survey data, and demographic variables impact the
agents decisions, we adjust the prompts with 6 different setups as per Table 1. For example, we compare the results of
setup 2 to setup 1 to assess the impact of Life/Value on the agent response and decisions without communication.
Table 1: Four different setups to assess prompt elements.
Feature Setup 1 Setup 2 Setup 3 Setup 4 Setup 5 Setup 6
Communication × × × ✓ ✓ ✓
Role ✓ ✓ ✓ ✓ ✓ ✓
Demographic × × ✓ × × ✓
Life/Value × ✓ ✓ × ✓ ✓
3 Findings
3.1 Impact of Communication
As explained in the previous section, we compared the single agent planning decisions with the multi-agent decisions
to confirm the effectiveness of communication in the multi-agent decision-making system. Below is an example of
the planning decisions and excerpts of the reasoning in both scenarios of the agent University Student. We have also
highlighted the main idea or ideas that are worth comparing with bold font. Single-Agent Result: My inclination is
towards the construction of low-income housing. Despite safety concerns, this option supports economic diversity,
vital for a healthy, balanced community. Affordable housing addresses the pressing local need and enhances my
environment by potentially reducing the number of people experiencing homelessness, thus potentially increasing
safety in the long run. The strain on public services is a valid concern, but it offers an opportunity for the community
to rally together to improve and scale these services to meet demand. [...]
Multi-Agent Result: From my perspective, transforming the government building into low-income housing emboldens
the ethos of social responsibility and diversity that I value as part of the student community. Beyond the personal satisfaction of living within a diverse neighborhood, low-income housing could enrich the local talent pool, potentially
offering unique collaboration opportunities for community-focused research or student-led initiatives with direct societal impact. The concerns over safety and the financial strain on public services are not to be dismissed lightly.
4

Simulating Multi-Stakeholder Decision-Ma
Figure 3: Keyword Frequency of Age
However, integrating a diverse socioeconomic demogra
ter innovative approaches to urban living and governan
socio-technical systems. On the contrary, while the shop
revenue, it is less aligned with my academic environment
To interpret each stakeholders reasoning, we analyzed
aSafety, Affordability, Commercial, Financial, Commun
truistic (blue: Affordability and Equity), Neutral (gray:
nancial and Commercial). Specifically, for each stakeho
keyword frequency per turn by averaging the total key
illustrated by the series of radar charts in Figure 3.
Figure 3 reveals how stakeholders reasoning shifted bet
agent had received a broadcast of all stakeholders origina
more aligned and focused in Round 2, likely reflecting a
also observe that altruistic keywords remain prominent
ing a consistent emphasis on social equity based on th
and neutral keywords generally show a slight decrease i
moved toward shared community or balanced value due
comprehensive considerations between financial interest
Figures 4 and 5 demonstrate the error point plot of the de
in terms of the score given by each agent with and withou
each agent, and the vertical axis represents the score they
agents participate in the setups of experiments described
without opinions and demographic information, 2) witho
and demographic information. Each vertical bar represe
with the midpoint being the mean score and the higher
scores. The three vertical bars for each agent in each pla
respectively. The results suggest that without communic
with relatively low variance. However, when multi-age
proposals widens for many agents, with increased polariz

g with Generative Agents in Urban Planning
Outputs Influenced by Communication
can stimulate broader community engagement and fos-
- a relevant context for a university student researching
g mall might provide Local Business convenience and tax
pirations. [...]
frequency of predefined keywords related to six criteriand Equitygrouped into three color-coded categories: Alommunity and Safety), and Interest-Driven (orange: Fir role and experimental setup, we calculated the average
d occurrences across three repetitions. The results are
n Round 1 and Round 2. Round 2 took place after each
pinions from Round 1. Overall, agents responses became
nvergence of perspectives due to shared information. We
oles like the Planner and Low-Income Advocacy, reflectgents predefined values. Meanwhile, the interest-driven
equency in Round 2, implying that the agents reasoning
he additional inputs with altruist agents, reflecting more
social responsibilities.
on to vote for low-income housing versus shopping mall
ulti-agent communication. The horizontal axis represents
ed for each planning scenario after their discussions. All
ection 2, each tested with and without communication: 1)
emographic information, and 3) including both opinions
he decision outcome from one experiment by one agent,
d lower bounds reflecting the standard deviation of the
ng scenario represent the results of the three experiments,
n, most agents exhibit a clear and consistent preference,
communication is introduced, the gap between the two
n and greater variance in how each agent rates the options.

Simulating Multi-Stakeholder Decision-Ma
Figure 4: Agent Ratings acros
Figure 5: Agent Ratings acr
3.2 Impact of Opinion and Demographic Informatio
As shown in Figure 4, in general, most agents tend to pro
ratings for the shopping mall project. However, consider
distinctive choice patterns. The Employee, Low-Incom
diverging ratings for the two projects. In contrast, the
University Student, and Property Developer tend to giv
that of the shopping mall project. These findings conf
Income Advocacy would rate higher to the low-income
Development would rate higher to the shopping mall pro
the agents personas we extracted.
Adding life values and demographic information helped
versity Student and Local Business, either changed their
project when these factors were included in their profi
demand for low-income housing to be heard by multipl
ratings for the shopping mall project. Furthermore, addi
the agents’ ratings more consistent with reduced standard
As shown in further keyword analysis in Figure 6, across
consistent. Adding demographic and opinion data makes
reflected in the more clustered radar shapes. For instance,
of safety and affordability related keywords beyond affo
while slightly reducing the focus on financial and afford
graphic and opinion data allows the agents in the simulati

g with Generative Agents in Urban Planning
etups without Communication
Setups with Communication
high ratings for the low-income housing project and low
variances exist across different agents. Persona provides
Advocate, Resident, and Urban Planner tend to provide
of the agents, including the Local Business, Manager,
he ratings for the low-income housing project closer to
m with our belief since we would assume that the Lowusing project from their perspectives, while the Property
for profitability. This could be attributed to the focus of
ape the agents opinions. All agents, except for the Unicisions or gave higher ratings to the low-income housing
This suggests that the agents’ discussions allowed the
akeholders. In contrast, there was no clear trend in the
ife values and demographic information generally made
viation.
erent setups, the agents value orientations remain largely
tain agents value considerations more comprehensive, as
Low-Income Advocacy agent shows increased frequency
bility. The planner agent adds more emphasis on equity
ty concerns. This reflects how the introduction of demoo act more like real-world stakeholder representatives and

Simulating Multi-Stakeholder Decision-Ma
Figure 6: Keyword Frequency of A
are better equipped to consider the diverse positions and
process.
3.3 Pros and Cons
One advantage of using simulation as a decision-making
ing feedback from real stakeholders can be time-consum
testing of various planning proposals in hypothetical sc
real-life processes that often rely on centralized voting
works, ensuring that marginalized populations are repres
several drawbacks need to be considered. Unlike real-li
compromise, the generative agents tend to be receptive
perspectives, which strengthened the echo-chamber effec
moral compass, likely influenced by the underlying LLM
social justice values. Finally, the process of extracting an
real-world data, which can inadvertently introduce resear
3.4 Ethical Risks and Recommendations
Several ethical concerns arise in the design of this system
diverse views of all stakeholders, some groups might be m
of the entire community. Biases in the underlying data ca
existing social inequalities. While including demograph
responses, it further heightens privacy risks associated w
To address these potential ethical risks, several strategies a
the inclusion of diverse populations. It is also important t
processing pipeline, including LLM model selection, int
development, to identify and mitigate potential biases.
minimize biases and ensure transparency.

g with Generative Agents in Urban Planning
nt Outputs Based on Experiments.
spectives of all stakeholders during the decision-making
iliary tool is its efficiency and cost-effectiveness. Gatherand expensive, the simulated approach enables iterative
rios. Additionally, it promotes inclusive voices: unlike
is system enables decentralized decision-making frameed and their perspectives considered. On the other hand,
akeholders who may have deeply held beliefs and resist
others opinions, despite prompts emphasizing their own
nd convergence on ideas. Additionally, the agents built-in
odels’ moral gatekeeper, can lead to an overemphasis on
esigning agent personas requires manual interpretation of
r biases into the simulation.
irst, if the agent design does not adequately represent the
epresented, leading to decisions that fail to meet the needs
so be amplified by the algorithms, potentially reinforcing
etails can improve the comprehensiveness of the agents’
ensitive demographic information.
needed. Establishing clear guidelines is essential to ensure
arefully design and evaluate the entire data collection and
ewee recruitment, persona and agent design, and prompt
ditionally, involving external third audit parties can help

Simulating Multi-Stakeholder Decision-Ma
3.5 Future works
Due to computational resource constraints, we were lim
similar experiments with a broader range of stakeholder
would yield richer insights. Incorporating knowledge fro
as game theory, could also enhance the systems explanato
and discussion frameworks, including hierarchical powe
opinions.
4 Conclusion
This study explored the use of a multi-generative agent d
ing diverse stakeholders. We found that multi-agent comm
porting richer, more innovative, and inclusive reasoning.
the diversity and stability of agent outputs. These finding
ticipate stakeholder reactions using a simulation-based a
urban planning decisions.
Acknowledgement
We thank Professors Manish Raghavan and Ashia Wilso
Professor Kairos Shen and Mr. John Attanucci (MIT DU
stages of this work.
References
[1] Joon Sung Park, Joseph C. OBrien, Carrie J. Cai,
stein. Generative agents: Interactive simulacra of
doi:10.48550/arXiv.2304.03442.
[2] Shun Ren, Zhi Cui, Rui Song, Zhi Wang, and Shiwe
Principles and architecture. arXiv preprint arXiv:24
[3] Guangyu Dai, Wen Zhang, Junjie Li, Shuo Yang, C
Sra. Artificial leviathan: Exploring social evolution
theory. arXiv preprint arXiv:2406.14373, 2024. do
[4] Luigi Costabile, Gianluca M. Orlando, Vincenz
tential of generative agents in crowdsourced f
doi:10.48550/arXiv.2504.19940.
[5] Anton Bakhtin, Noam Brown, Emily Dinan, Gabr
Gray, Hengyuan Hu, Aaron P. Jacob, et al. Humanmodels with strategic reasoning. Science, 378(6624
[6] Joon Sung Park, Catherine Q. Zou, Aaron Shaw, Be
Willer, Percy Liang, and Michael S. Bernstein. G
arXiv:2411.10109, 2024. doi:10.48550/arXiv.2411
[7] Abhishek Chopra, Shubham Kumar, Nazli Giray-Ku
of agency in agent-based models. arXiv preprint ar
[8] Andrew B. Hou, Haoyi Du, Yixuan Wang, Junjie Z
Gardner, and Tian He. Can a society of generative a
icy? a case study on vaccine hesitancy. arXiv prepri
[9] Jiarui Piao, Zhaoyang Lu, Chao Gao, Feiyang Xu
Emergence of human-like polarization among larg
2025. doi:10.48550/arXiv.2501.05171.
[10] A. F. Ashery, Luca Maria Aiello, and Andrea Baro
llm populations. Science Advances, 11(20):eadu936
[11] Rakesh Ranjan, Shubham Gupta, and S. N. Singh.
equitable multi-agent systems. arXiv preprint arXiv

g with Generative Agents in Urban Planning
to a small set of agents in this experiment. Conducting
d agents representing diverse demographic backgrounds
egotiation studies and decision-making frameworks, such
power. Finally, exploring alternative prompting strategies
ynamics, may help generate more stable and passionate
ion-making system in an urban planning scenario involvication enhances the quality of the agents arguments, supgrating demographic and life-value data further improves
rovide a predictive framework for decision-makers to anoach, thereby fostering more equitable and cost-effective
MIT EECS) for their guidance and feedback, as well as
, and all interview participants for their input in the early
edith Ringel Morris, Percy Liang, and Michael S. Bernman behavior. arXiv preprint arXiv:2304.03442, 2023.
. Emergence of social norms in generative agent societies:
08251, 2024. doi:10.48550/arXiv.2403.08251.
ment O. Lbe, Shriram Rao, Antonio Caetano, and Misha
llm agents through the lens of hobbesian social contract
.48550/arXiv.2406.14373.
. Gatta, and Vincenzo Moscato. Assessing the pochecking. arXiv preprint arXiv:2504.19940, 2025.
Farina, Caitlin Flaherty, Daniel Fried, Alex Goff, John
el play in the game of diplomacy by combining language
067–1074, 2022. doi:10.1126/science.ade9097.
min M. Hill, Carrie J. Cai, Meredith Ringel Morris, Robb
ative agent simulations of 1,000 people. arXiv preprint
09.
Ramesh Raskar, and Arnau Quera-Bofarull. On the limits
2409.10568, 2024. doi:10.48550/arXiv.2409.10568.
ng, Zhen Wang, Paul P. Liang, Daniel Khashabi, Lauren
ts simulate human behavior and inform public health polrXiv:2503.09639, 2025. doi:10.48550/arXiv.2503.09639.
Hu, Francisco P. Santos, Yunzhi Li, and James Evans.
nguage model agents. arXiv preprint arXiv:2501.05171,
elli. Emergent social conventions and collective bias in
2025. doi:10.1126/sciadv.adu9368.
rness in agentic ai: A unified framework for ethical and
02.07254, 2025. doi:10.48550/arXiv.2502.07254.

Simulating Multi-Stakeholder Decision-Making with Generative Agents in Urban Planning
[12] Elizabeth Ondula, David Orner, Nicholas Mumero, and Chiara Rusti. Sentimental agents: Exploring deliberation,
cognitive biases, and decision-making in llm-based multi-agent systems. In Proceedings of the Fourth Workshop
on Knowledge-Infused Learning, Vienna, 2024. URL https://openreview.net/forum?id=izfJXk4wGz.
[13] Yuxuan Bai, Jing Zhao, Jing Shi, Zihan Xie, Xiaoyan Wu, and Lei He. Fairmonitor: A dual-framework
for detecting stereotypes and biases in large language models. arXiv preprint arXiv:2405.03098, 2024.
doi:10.48550/arXiv.2405.03098.
[14] Massachusetts Institute of Technology. Mit volpe final development plan, volume 1. Technical Report PB-368,
City of Cambridge Planning Board, 2021. URL https://www.cambridgema.gov/-/media/Files/CDD/
ZoningDevel/SpecialPermits/sp368/sp368_appnarrative_20210603.pdf.
[15] Qingyun Wu, Gagan Bansal, Jing Zhang, Yao Wu, Beibin Li, Erheng Zhu, Linxi Jiang, Xinyu Zhang, Shuo
Zhang, Jiahui Liu, et al. Autogen: Enabling next-gen llm applications via multi-agent conversation. arXiv
preprint arXiv:2308.08155, 2023. doi:10.48550/arXiv.2308.08155.
9
