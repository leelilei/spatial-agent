# HC14 - When agents learn to think: Large language model-enhanced agent-based modeling for crowd evacuation in disaster scenarios

## Stable Widened-Core Snapshot

- core_layer: `anchor_core`
- admission_status: `stable_anchor`
- corpus_tier: `Core`
- system_family: `Crowd Evacuation Disaster`
- paper_refs: `CrowdEvacuation2026`
- year: `2026`
- agent_count: `100+`
- environment_side_representation: `graph_based`
- agent_accessible_representation: `L3`
- behavioral_scale: `mixed`
- behavior_type: `mobility; cooperation; other`
- evidence_status: `observed_effect`
- spatial_behavior_coupling: `explicit`
- evaluation_method: `mixed`
- space_syntax_construct: `none`
- source_basis: `local_pdf_pdf2text_fulltext_review`
- artifact_class: `local_pdf`

## Representation Gap Note

The simulation uses a GIS-derived road network with road-width and speed attributes, but the agent-facing interface remains text prompts about hazard conditions, road status, memories, and nearby communications rather than direct geometry.

## Original Artifact Pointer

- local_artifact_path: `assets/survey_paper/pdfs/phase1_core/15_HC14_Crowd_Evacuation_Disaster.pdf`

## Source Content

Title: When agents learn to think: Large language model-enhanced agent-based modeling for crowd evacuation in disaster scenarios

Source PDF: D:\0-AI相关研究\1-spatialagent\spatial-agent\assets\survey_paper\pdfs\phase1_core\15_HC14_Crowd_Evacuation_Disaster.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-04-27T13:19:45+00:00
- page_count: 17
- status: ok
- text_char_count: 77213

Metadata:
- author: Sen Yang
- doi: 10.1016/j.ress.2025.112056
- keywords: Large language models, Agent-based modeling, Crowd evacuation, Disaster response, Resilience
- subject: Reliability Engineering and System Safety, 269 (2026) 112056. doi:10.1016/j.ress.2025.112056

Outline:
- When agents learn to think: Large language model-enhanced agent-based modeling for crowd evacuation in disaster scenarios (page 1)
  - 1 Introduction (page 1)
  - 2 Methodology (page 2)
    - 2.1 Prompt generation (page 3)
      - 2.1.1 System prompt (page 4)
      - 2.1.2 User prompt (page 5)
    - 2.2 Parallelized and batched LLM inference (page 6)
    - 2.3 Evacuation simulation environment (page 7)
  - 3 Case study (page 8)
    - 3.1 Simulation results (page 9)
    - 3.2 Emergent behaviors of agents (page 9)
    - 3.3 Conventional ABM comparison (page 11)
    - 3.4 Validation with reports (page 12)
    - 3.5 Sensitivity analysis and simulation cost (page 14)
  - 4 Conclusion (page 15)
  - CRediT authorship contribution statement (page 16)
  - Declaration of competing interest (page 16)
  - Acknowledgements (page 16)
  - Supplementary materials (page 16)
  - Data availability (page 16)
  - References (page 16)

Markdown Content:

Reliability Engineering and System Safety 269 (2026) 112056
Contents lists available at ScienceDirect
Reliability Engineering and System Safety
journal homepage: www.elsevier.com/locate/ress
When agents learn to think: Large language model-enhanced agent-based
modeling for crowd evacuation in disaster scenarios
Sen Yanga,b , Luis Ceferinob, Yi Zhangc,d,* , Chen Gua , Tong Guoc,d, Gen Kondob
aDepartment of Civil Engineering, Tsinghua University, Beijing 100084, China
bDepartment of Civil and Environmental Engineering, University of California, Berkeley, CA 94720, USA
cSchool of Civil Engineering, Southeast University, Nanjing 210096, China
dAdvanced Ocean Institute of Southeast University, Nantong 226000, China
A R T I C L E I N F O A B S T R A C T
Keywords: Reliable and realistic modeling of crowd evacuation is critical for improving the safety and resilience of complex
Large language models transportation and infrastructure systems under disaster emergencies. Traditional agent-based modeling has
Agent-based modeling been widely used to simulate individual behaviors and interactions during evacuations, but often struggles to
Crowd evacuation
represent interpersonal communication, context-aware reasoning, and adaptive decision-making under rapidly
Disaster response
evolving conditions. To address these limitations, this study introduces a dynamic evacuation simulation
Resilience
framework that integrates large language models as decision-making cores for individual agents. Each agent
maintains personality traits, environmental observations, and decision histories, while the large language model
enables context-sensitive reasoning and information exchange between agents and their surroundings. To sup-
port large-scale, computationally efficient simulations, we implement batch prompting and parallel processing
strategies that reduce runtime overhead. Both pedestrian and vehicle evacuations are represented to capture
multimodal evacuation dynamics. Using a real-world disaster evacuation case study, we demonstrate that
incorporating large language models significantly enhances the realism, adaptability, and reliability of evacu-
ation simulations. The framework reduces reliance on manually defined behavioral rules, supports probabilistic
safety and reliability assessment, and provides a scalable platform for stress-testing evacuation strategies under
diverse hazard scenarios. This research bridges the gap between human-centered behavioral modeling and en-
gineering decision-support, offering a novel tool for disaster preparedness and resilience planning.
1. Introduction Earthquake to investigate residents’ evacuation decisions. Some studies
have conducted small-scale evacuation drills with volunteers [7,8],
Widespread natural disasters have underscored the persistent chal- using questionnaires, GPS trackers, or VR devices [9] to collect behav-
lenges associated with community vulnerability and disaster prepared- ioral data such as route choices and evacuation speeds, which are then
ness [1–3]. Among various emergency response measures, crowd used to fit functions for simulation purposes. However, these methods
evacuation plays a critical role. Effective management of crowd move- are often costly, yield limited data, and fail to capture the dynamic and
ment can drastically reduce casualties and help maintain social stability detailed movement patterns seen in real disaster scenarios.
[4]. To support post-disaster decision-making and crowd management, In recent years, agent-based modeling (ABM) has become a widely
it is essential to analyze and reproduce sociological phenomena under- adopted tool to simulate large-scale evacuations during events such as
lying human decision-making and escape behaviors during emergencies. earthquakes [10] and tsunamis [11], and to estimate potential casualties
However, due to the nature of such events, organizing real-world [12]. ABM simulates both detailed individual behaviors and emergent
large-scale evacuation experiments is highly impractical. Several collective phenomena by defining micro-level decision rules and
studies have attempted to collect empirical evacuation data through mechanisms [13]. A typical ABM evacuation framework consists of
post-disaster surveys and small-scale drills. For instance, Murakami modules for agent attributes, decision-making logic, traffic simulation,
et al. [5,6] conducted a survey after the 2011 Great East Japan and disaster modeling, all of which interact to recreate realistic
* Corresponding author.
E-mail addresses: yangsen_1998@163.com(S. Yang), ceferino@berkeley.edu(L. Ceferino), zhang_yi@seu.edu.cn(Y. Zhang).
https://doi.org/10.1016/j.ress.2025.112056
Received 22 September 2025; Received in revised form 4 November 2025; Accepted 29 November 2025
Available online 1 December 2025
0951-8320/© 2025 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
evacuation processes [14]. The disaster modeling component provides reasoning and decision-making. The simulation reveals complex social
agents with information about disaster intensity and forecasts, while phenomena such as information diffusion, relationship building, and
simultaneously influencing traffic conditions. Based on the received group collaboration [64]. Wang et al. [36] utilized LLMs to extract
disaster information and their individual characteristics, agents make personalized and self-consistent daily activity patterns from historical
decisions such as evacuation timing, shelter selection, and route choice. data, guiding agents to generate realistic urban behavior sequences
The traffic module then simulates their movements accordingly, thereby driven by inferred motives and contextual needs. Wu et al. [31] applied
reconstructing the evacuation process. this approach to simulate indoor earthquake evacuation, showing that
In multi-agent systems, maintaining reliable communication and LLM-enhanced ABM effectively models disaster scenarios, with agent
coordination under dynamic environments is essential for collective personality and interactions significantly influencing the simulation
performance [15,16]. Various studies have demonstrated the effective- outcomes. Lu et al. [37] incorporated LLM for interactive risk analysis,
ness of ABM in modeling disaster scenarios [17,18]. Yang et al. [19] enabling intelligent evacuation safety assessments and providing opti-
developed a city-scale flood evacuation model using ABM to explore mization guidance.
cascading effects of flooding on human behavior, emphasizing the role The aforementioned studies demonstrate that the generalization
of risk education and emergency planning. Zhang et al. [20] modeled capabilities of LLMs enable agents to better adapt to complex and dy-
resident responses to flash flood warnings by incorporating modules for namic environments, thereby enhancing the realism and practical value
alerts, social behavior, and flood dynamics, finding that early warnings of simulation systems. Integrating LLMs into ABM thus offers a more
are not always effective, especially when trust is low and leadership is intelligent and efficient decision-support framework for applications
absent. In addition, simulation-based analysis was conducted to eval- such as disaster response and evacuation planning. However, only a
uate the effects of different warning frequencies and lead times, aiming limited number of studies have so far explored the use of LLMs in post-
to determine the optimal number of flash flood warnings [21]. Harris disaster evacuation modeling. Existing efforts typically simplify indoor
et al. [22] proposed a comprehensive ABM framework for hurricane spaces into grid-based representations and focus on relatively simple,
evacuation, capturing complex interactions from disaster formation to small-scale scenarios. Therefore, the integration of LLMs and ABM for
forecasting and evacuation. Wang et al. [23] applied ABM to simulate simulating large-scale regional evacuations under complex and realistic
near-field tsunami evacuation in Seaside, Oregon, analyzing how factors conditions represents a valuable and underexplored area of research.
like decision delay, transportation mode, and vertical evacuation To address these limitations, this study proposes a novel large-scale
structures affect casualty rates. Nguyen et al. [24] considered evacuation modeling framework that integrates LLMs into ABM. By
post-earthquake road blockages in ABM evacuation modeling, showing leveraging the language understanding, reasoning, and memory capa-
that debris-induced obstacles significantly hinder access to shelters and bilities of LLMs, the framework enables agents to make context-aware
increase evacuation difficulty [8]. The choice of transportation mode decisions, communicate with others, and adapt to dynamic disaster
also plays a major role in evacuation effectiveness. Takabatake et al. environments in a more human-like manner. The model captures both
[25] developed an ABM that simultaneously models pedestrian and pedestrian and vehicular evacuations, incorporates diverse individual
vehicle evacuation during tsunamis. Stochastic disaster generation characteristics and environmental factors, and supports scalable simu-
methods have also been integrated into ABM frameworks for lation through parallelized inference. A real-world case study is pre-
scenario-based risk assessment and emergency planning [26]. Further- sented to validate the framework and demonstrate its potential for
more, the reinforcement learning algorithm was integrated with ABM to supporting high-fidelity disaster evacuation analysis and decision-
enable adaptive evacuation path optimization at the individual level making. The remainder of this study is organized as follows. Section 2
[27]. Comparisons with post-disaster casualty data, shelter occupancy, describes the proposed LLM-enhanced ABM framework in detail,
and traffic congestion statistics have provided validation for the accu- including the prompt generation module, the inference acceleration
racy and practicality of ABM simulations [25,28,29]. Compared to module for interacting with the LLM server, and the evacuation simu-
simplified evacuation models, ABM offers detailed simulation of indi- lation module. Section 3presents a real-world disaster case study and
vidual behavior, making it particularly suitable when high-resolution evaluates the performance of the proposed method. Finally, Section 4
modeling is needed for planning resources or rescue operations [30]. concludes the paper and summarizes its key contributions.
Despite these advances, current ABM-based evacuation studies
generally overlook social interactions (e.g., group cohesion, leadership, 2. Methodology
or communication) among evacuees and changes in behavior due to
emotional states or evolving environmental conditions [25]. Addition- The central idea of this study is to replace predefined decision-
ally, ABM faces challenges in simulating behaviors that require natural making rules in conventional ABM with LLMs, as illustrated in Fig. 1.
language communication and common-sense reasoning, and struggles to In traditional ABMs, agents make decisions, such as when to evacuate,
handle individual heterogeneity and behavioral adaptability [31]. To which shelter to choose, and what route to take, based on fixed heu-
overcome these limitations, recent research has begun integrating large ristics. For example, agents may be programmed to select the nearest
language models (LLMs) to enhance agent decision-making and better shelter and follow the shortest path. While such rules partially reflect
reflect human evacuation behavior in real-world scenarios [32]. LLMs real-world behavior, they lack flexibility in capturing the adaptability of
offer advanced capabilities in natural language understanding, individuals and the dynamic interactions among agents, leading to less
reasoning, and learning, enabling a more accurate modeling of agent realistic simulations. To address this limitation, this study leverages
behavior with reduced reliance on predefined rules. In this sense, LLMs LLMs to generate decisions based on prompts that describe each agent’s
serve as a bridge that translates behavioral complexity into interpretable personality traits, surrounding environment, and memory of past ac-
and operational forms, thereby enhancing the theoretical and practical tions. By harnessing the natural language understanding and reasoning
foundation of behavior-driven simulations [33]. LLMs have recently capabilities of LLMs, agents are enabled to make context-aware de-
demonstrated significant potential in enabling autonomous agents with cisions, interact with others, and respond to evolving disaster conditions
context-aware reasoning, multimodal input understanding, and in a more human-like and adaptive manner.
high-level task planning [34]. Park et al. [35] implemented this concept The framework consists of three main modules, as illustrated in
by creating a virtual town in which each resident’s daily activities are Fig. 2, including prompt generation, LLM inference handling, and
driven by LLM-enhanced agents. These agents possess memory, reflec- evacuation simulation. Each agent is assigned a unique set of personal
tion, planning, and adaptive behavior capabilities. They perceive their attributes, such as age, gender, vehicle ownership, family structure, and
environment, receive communications from others, and store their de- current location. In addition to these static traits, agents continuously
cisions, which are later retrieved and used as context for future perceive dynamic environmental information, including the current
2

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
Fig. 1. Schematic illustration of the core concept: replacing the predefined logic of conventional ABMs with the autonomous decision-making capabilities of LLMs.
Fig. 2. The proposed framework for LLM-enhanced ABM, which comprises three main modules: prompt generation, LLM request, and the moving system.
time, hazard conditions, nearby communications, and road status. returned by the LLM and simulates the corresponding actions of each
Agents also maintain a memory system that stores past decisions and agent. The movement system in the simulation module accounts for both
relevant contextual information. These factors can effect the evacuation pedestrian and vehicular evacuation, and the road network is con-
decisions of each agent [38]. At each simulation timestep, the agents structed using GIS data to ensure spatial realism. This process is iterated
that need to make decisions will generate prompts based on their current at fixed time intervals until the simulation concludes. The following
state, which are then sent to the LLM to obtain decision outputs. These subsections describe each module in further detail.
decisions may include evacuation timing, route selection, and coordi-
nation with others. Given the large number of agents, often in the 2.1. Prompt generation
thousands, sequentially requesting decisions from the LLM would incur
significant latency. To address this, the framework integrates batch Individuals in different situations tend to make distinct decisions
prompting [39] and parallel inference mechanisms to improve effi- depending on the available options. In the proposed framework, agents
ciency. The evacuation simulation module interprets the decisions generate tailored prompts based on their current stage in the evacuation
3

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
process. Drawing on insights from post-disaster surveys [5,6], six is the input provided by the end-user, typically in the form of a question,
representative stages that capture key decision-making points in a instruction, or statement that elicits a response from the LLM. The as-
tsunami evacuation scenario is defined, as illustrated in Fig. 3. The sistant prompt, which is the model-generated reply from a previous turn,
process begins with agents potentially located outdoors when the is mainly used in multi-turn dialogues. In this study, assistant prompts
earthquake strikes. At this stage, their decision options may include are not utilized, as each interaction is designed as a single-turn dialogue.
remaining outside to observe the situation, returning home, or initiating This simplifies implementation and reduces the computational overhead
immediate evacuation. Each decision leads the agent to a different of maintaining multi-turn conversational states. Moreover, relevant
subsequent stage. For instance, an agent who chooses to evacuate memory information is already embedded in the prompt, eliminating
immediately will transition to the evacuation planning stage (Stage 3 in the need for dialogue history tracking. The remainder of this section
Fig. 3). For agents who are initially at home, available decisions include introduces the design of system prompts and user prompts tailored for
staying indoors to observe, evacuating immediately, or taking time to each evacuation stage.
collect essential items before evacuating. Agents who choose to prepare
before leaving move to Stage 4, where they remain stationary until the 2.1.1. System prompt
elapsed time exceeds a preparation duration drawn from a predefined The system prompt is constructed as a static template that offers
distribution. This design accounts for uncertainty in individual readiness general guidance for the LLM’s behavior. It begins with a task definition
times. Agents in Stage 3, having committed to evacuation, must decide that outlines the core requirements for generating realistic and context-
on both their destination and mode of transportation. Additionally, they aware decisions. The LLM is instructed to act as if it were personally
may determine whether to assist others in evacuating together. Once a experiencing the disaster scenario, and to make decisions accordingly. It
destination is selected, they transition to the movement stage (Stage 5). is also asked to assess its emotional state and generate information for
Agents may either follow their original plans or revise them by taking potential communication with others, such as asking questions,
alternative routes or formulating new evacuation strategies. Upon responding to others, or sharing situational updates. Although the task
reaching a shelter, agents enter the final stage, where further decisions definitions vary slightly across different agent stages, the overall struc-
may still occur, such as transferring to a different shelter if needed. ture remains consistent. The task description for agents in Stage 1 is
There are three types of prompts used when interacting with a LLM provided below for illustration, while the prompts for other stages are
through an Application Programming Interface (API): system prompts, included in the Appendix A as supplementary information.
user prompts, and assistant prompts [40]. The system prompt estab- To facilitate efficient interpretation of the output, a structured
lishes the context, tone, and boundaries for the LLM’s responses. It format is required. Therefore, the system prompt also includes explicit
serves as a guiding framework that consistently shapes the model’s output instructions and an example to guide the LLM’s responses. For
behavior and response style throughout the interaction. The user prompt agents in Stage 1, the LLM is required to select a next action, provide a
Fig. 3. Illustration of different stages for agents. Six stages are considered: outside, at home, making an evacuation plan, preparing for evacuation, moving,
and arriving.
4

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
self-assessed emotional score, and generate content for potential prompts to accommodate their specific decision-making needs. The user
communication with others. Output specifications for other agent stages prompt is designed as a dynamic template, with placeholders that are
follow a similar structure and are provided in the Appendix as supple- updated based on the agent’s state at each time step. To illustrate the
mentary material. It is important to note that all potential decision op- general structure, the user prompt for Stage 1 is presented below:
tions and supporting descriptions are predefined in the system prompt. The user prompt comprises three main components: personality,
The emotional score is included to account for the intensity of emotions surroundings, and relevant memories. The personality section includes
during decision-making. Previous studies have shown that panic can agent-specific attributes such as ID, age, gender, current location,
significantly influence evacuation behavior [41]. However, these effects vehicle ownership, and family details, enabling the model to account for
were often modeled using empirical equations, which may lack realism individual heterogeneity. Family information specifies whether the
to some extent. By contrast, this framework enables agents to express agent has a spouse or children, and whether they are currently present.
emotions directly, potentially capturing more subtle and realistic The surroundings component captures the agent’s immediate environ-
behavioral patterns. ment, including the current time, perceived disaster information, crowd
behavior, emotional atmosphere, and nearby conversations. Specif-
2.1.2. User prompt ically, tsunami information indicate whether the agent has received a
Agents at different stages are provided with slightly different user warning. Crowd movement is represented by the local moving ratio,
5

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
while crowd emotion reflects the level of panic observed. These factors highly time-consuming, especially considering that the simulation in-
are included because both the behavior and emotional state of sur- volves multiple decision rounds. This sequential process leads to a sig-
rounding individuals can significantly influence decision-making. In this nificant computational bottleneck. To address this challenge and enable
study, agents are assumed to perceive crowd movement and emotion efficient simulation at scale, this study incorporates two key techniques:
within a 25-meter radius. To emulate interpersonal communication batch prompting and parallel requests, which together substantially
during evacuation, conversations from nearby agents (within an reduce response time and improve computational feasibility.
assumed 5-meter radius) are also included in the prompt [42]. This Batch prompting allows the LLM to generate responses for multiple
simulates real-world information exchange and allows agents to make agents in a single inference run, thereby significantly reducing inference
more context-aware decisions. Each LLM call is treated as a standalone time [39]. As illustrated in Fig. 4, standard prompting involves one
request without access to prior conversational history. However, to system prompt and one user prompt, with the user prompt corre-
enable agents to make informed and consistent decisions, it is essential sponding to a single agent, resulting in one response per inference. In
that they retain awareness of their past actions. To emulate human-like contrast, batch prompting combines the user prompts of multiple agents
memory, each prompt includes a concise summary of the agent’s deci- into a single input, while still using one system prompt. The system
sion history. This approach preserves behavioral continuity while prompt is designed to guide the LLM in simulating multiple individuals
minimizing redundant information and computational overhead. In and generating distinct responses for each one. Agent IDs are included to
addition, it can include pre-disaster tsunami risk awareness to better help the LLM associate each input context with the correct output,
reflect individual preparedness and simulate more realistic evacuation ensuring alignment between prompts and responses across the batch.
behavior. An illustrative example of a user prompt generated during the Although batch prompting can significantly reduce inference time,
simulation is shown below: LLMs have input length limitations, making it infeasible to include all
The overall structure of user prompts remains consistent across agents in a single batch. Moreover, including too many agents in one
different stages, with slight modifications tailored to specific decision- prompt can confuse the model and degrade output quality. Previous
making needs. For instance, in Stage 3 (i.e., when the agent is making studies have shown a notable performance drop when the batch size
an evacuation plan), the list of available tsunami evacuation options is exceeds six [39]. Therefore, this study adopts a batch size of six agents,
included in the prompt. For agents in the moving stage, real-time road which strikes a practical balance between efficiency and response
conditions are incorporated to reflect dynamic changes in the environ- quality.
ment. In the case of agents who have arrived at vertical shelters, the Even with batch prompting, N/6 requests are still required for N
prompt additionally includes information about their arrival status and agents, which remains time-consuming if processed sequentially. To
the current occupancy of the shelter. Prompt templates for all stages are address this, parallel requests are integrated into the framework (see
provided in the Appendix B. Fig. 5). Specifically, all agents are first grouped into multiple batches,
and then all batch prompts are sent simultaneously to the LLM server.
2.2. Parallelized and batched LLM inference This parallel approach reduces the overall waiting time to a single round
of interaction with the server. Since the cloud-based LLM infrastructure
In large-scale evacuation simulations, thousands of agents must can handle large volumes of concurrent requests, this method avoids the
make decisions at each time step, resulting in a corresponding number of cumulative delays inherent in sequential querying. LLM stochasticity
requests to the LLM server. A conventional sequential approach, where can influence evacuation outcomes depending on the parameter set-
each agent requests a response only after the previous one completes, is tings. In this study, the temperature parameter is set to 0.3, following the
6

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
Fig. 4. Illustration of batch prompting used to accelerate LLM inference by combining multiple agent prompts into a single request.
Fig. 5. Illustration of parallel request handling for LLM inference, enabling simultaneous processing of multiple agent queries.
general recommendation that lower values are preferable for deter- must be assigned to each road segment. Traditionally, road length is
ministic and reasoning-oriented tasks. used as the cost metric, which is appropriate for pedestrian evacuees,
since they are less capable of covering long distances within the limited
2.3. Evacuation simulation environment time before tsunami impact. Previous study also suggested that this
assumption is suitable for estimating on-foot evacuation behavior [44].
Once the decisions are obtained from the LLM, the simulation envi- In contrast, vehicle-based evacuees are more likely to consider both road
ronment interprets them and prompts agents to act accordingly. As length and width, as wider roads tend to allow faster movement [25].
previously described, agents who choose to gather essential supplies and Therefore, for vehicular evacuation, the cost is defined as the estimated
make necessary preparations before evacuating must spend a certain travel time, calculated as the ratio of road segment length to its speed
amount of time in preparation. To account for the uncertainty in this limit.
duration, a Gamma distribution is employed to assign preparation times. Although the fastest path is initially assigned as each agent’s evac-
This distribution is parameterized using maximum likelihood estimation uation plan, agents are allowed to deviate from this path during
based on empirical survey data [43], as defined by the following movement in response to dynamic factors such as road congestion. If an
equation: agent opts for a detour, a new fastest path, passing through the selected
detour segment, is recalculated using the same fastest path procedure
f(x)=
Γ(α
1 )θαxα(cid:0)1e (cid:0)x θ, (1) described previously. This dynamic re-routing capability enables agents
to adapt to changing conditions in real time, reflecting more realistic
evacuation behavior. Such flexibility underscores the advantages of the
where θ and α are the parameters of the Gamma distribution, estimated
LLM-enhanced ABM over conventional rule-based models, which typi-
as θ =6.494, and α =1.659. Before the elapsed time is larger than the
cally lack the ability to adapt to evolving environmental contexts.
assigned preparation time, agents will stay in place. Agents remain in
During movement, the walking speed of pedestrian evacuees is
place until the elapsed time exceeds their assigned preparation duration.
determined based on the study by Takabatake et al. [25], as illustrated in
Once this condition is met, they transition to the stage of evacuation
Fig. 6. Specifically, pedestrian speed is modeled as a function of the
planning. evacuee’s age and the crowd density on the road. Crowd density is
In the planning stage, agents must determine their evacuation des-
dynamically calculated for each agent at every time step by counting the
tinations. Once the destination is selected by the LLM, the initial route is
number of evacuees within a 2-meter radius. To account for the influ-
generated using a fastest path algorithm. This approach is reasonable, as
ence of vehicles on pedestrian movement, one vehicle is equivalently
evacuees typically prefer the fastest route to safety when lacking
counted as ten evacuees in the density calculation, while each individual
detailed road condition information. To compute the fastest path, a cost
7

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
car is also considered. Based on the speed computed by the IDM, the
presence of surrounding pedestrians imposes an additional hindrance.
This is modeled using a one-tailed normal distribution [29,44], where
the vehicle’s speed decreases from the IDM-derived value to half when
approximately 15 pedestrians are present, and approaches zero as
pedestrian density increases further. It is worth noting that more so-
phisticated models for pedestrian and vehicle movement can be readily
integrated into this framework. However, since the primary focus of this
study is to explore the integration of LLMs with ABM, the development
of advanced movement models falls outside the scope of this work.
Moreover, agents may evacuate with family members or assist others
by forming groups. Within each group, a single agent is designated as the
decision-maker (i.e., the leader), while the remaining members follow
their lead. This approach reduces the complexity and computational
burden in large-scale simulations [42,46]. For pedestrian groups, the
Fig. 6. Relationship between agent moving speed and crowd density, with movement speed is determined by the slowest member, accounting for
different curves representing agents of different age groups. the need to assist older adults or infants. Regarding casualty estimation,
an agent is considered a casualty if the simulated tsunami amplitude at
is counted as one [25]. This adjustment reflects the greater spatial their current location exceeds 1 m [44]. The simulation framework is
impact that vehicles have on pedestrian flow during evacuation. For implemented in Python, with LLM requests made via the OpenAI API to
groups of agents evacuating together, the movement speed is deter- access the DeepSeek-V3 API [47]. The framework is model-agnostic and
mined by the slowest member within the group. To account for the in- can be adapted to various LLMs, such as GPT, by simply modifying the
fluence of infants, who are typically carried by their parents, on group API configuration settings. In this study, DeepSeek was selected due to
movement, infants are assigned slower speeds in the model. As a result, its cost-effectiveness and strong reasoning capabilities.
groups that include older adults or infants will exhibit reduced move-
ment speeds, reflecting realistic constraints on evacuation mobility in 3. Case study
such scenarios.
For evacuees traveling by car, this study adopts the Intelligent Driver In this study, Arahama Village in Japan is selected as the case study
Model (IDM) [45] to determine vehicle speed. The IDM effectively area. As a coastal community, Arahama experienced severe devastation
captures the dynamic changes in vehicle speed caused by interactions during the 2011 Great East Japan Earthquake and Tsunami. The tsunami
with the preceding vehicle, using a compact set of parameters. This struck approximately one hour after the earthquake, reaching a
model has been previously employed in evacuation simulations and has maximum wave height of 10 m It inundated up to 5 km inland, about ten
demonstrated satisfactory performance [25,43]. In the IDM, the speed of times farther than the expected extent of a typical tsunami. Following
each vehicle is updated at every time step using the following equations: the 2011 tsunami, a comparison between the number of residents re-
[ ( ) ( ) ] ported by the Sendai City Bureau and the pre-disaster population indi-
dv(t) v 4 s∗(v,Δv) 2
=a 1(cid:0) (cid:0) , (2) cated a discrepancy of 283 individuals, which is considered the upper
dt v0 s
bound of estimated casualties. In addition, local media sources reported
[ ( )] that between 200 and 300 victims were found in the area, aligning with
s ∗(v,Δv)=s0 +max 0, vT+ v √ Δ ̅ v ̅̅̅̅ , (3) the official estimates [29]. The village has limited high-rise reinforced
2 ab
concrete structures. Notably, the only official tsunami evacuation fa-
cility in the area is the four-story Arahama Elementary School, which
where a represents the maximum vehicle acceleration, b denotes the
features an accessible rooftop [28]. The building withstood both the
comfortable braking deceleration, T is the minimum desired time gap to
earthquake and tsunami, providing shelter for approximately 520
the vehicle in front, s0 is a minimum desired net distance to the lead
evacuees.
vehicle, s is the actual gap to the preceding vehicle, v0 is the desired
In Arahama village, eyewitness accounts and rescue team reports
speed under free-flow traffic conditions, v is current speed of the vehicle,
and Δv is the relative speed difference with respect to the lead vehicle. indicated that many evacuees gathered at Arahama Elementary School,
the designated vertical evacuation shelter. The rest of the population
Here, a, b, T, and s0 are constant values, adopted from the study by
evacuated by car using two main roads. Exit 1 followed the Prefectural
Treiber et al. [45].
Road, and Exit 2 served as an alternative route leading inland. In this
In this study, the desired free-flow speed v0 is determined based on
study, both pedestrians and vehicles are allowed to evacuate to the
both road width and the designated speed limit. Specifically, if the road
vertical shelter. However, only vehicles can choose to evacuate via
width exceeds 4.5 m, it is deemed sufficiently wide for vehicles to pass
inland exits [29]. The road network is reconstructed using pre-disaster
each other without deceleration, and the full speed limit is applied.
Conversely, if the road width is <4.5 m, indicating a narrow roadway satellite imagery, and roads are assigned speed limits based on their
width. Roads wider than 4.5 m are considered suitable for two-way
where vehicles must slow down to pass safely, the desired speed is set to
traffic without slowing down and are given a speed limit of 30 km/h.
half the original speed limit to reflect this constraint. Besides, when a
Narrower roads required vehicles to reduce speed, so their speed limit is
vehicle approaches within 10 m of an intersection, its desired speed is
set to half. The spatial layout is illustrated in Fig. 7.
fixed at 10 km/h [25]. It is adopted based on the premise that traffic
This study covers 84 % of the residential area in Arahama, resulting
signals are non-functional during the disaster scenario. Under such
in an estimated population of approximately 2271 residents [29]. Due to
conditions, it is assumed that most drivers would reduce their speed
the lack of precise data on evacuees at the time of the earthquake, the
significantly when approaching intersections, irrespective of road
age distribution from the study by Takabatake et al. [30] is adopted. The
width. Furthermore, in the presence of congestion near intersections,
population is assumed to have an equal gender distribution. Car
vehicles are unlikely to accelerate due to the increased risk of collisions
ownership is based on demographic data from the study by Yagi and
with surrounding traffic.
Manage [48]. Additionally, the marriage rate for residents aged 18 and
To account for the influence of nearby pedestrians on vehicle
above is set at 0.72, following data from the Statistics Bureau of Japan
movement, the number of pedestrians within a 5-meter radius of each
[49]. Children under the age of five are randomly assigned to a married
8

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
Fig. 7. Spatial layout of the study area. Two types of road speed limits are considered based on road width. The evacuation destinations include one vertical shelter
and two exits designated for residents evacuating by car.
couple. 3.1. Simulation results
To capture agent heterogeneity, tsunami risk awareness is incorpo-
rated into each agent’s initial memory. This addition aims to better The simulation snapshots at 10-minute intervals are presented in
represent individual preparedness and simulate more realistic evacua- Fig. 8. Immediately after the earthquake, only a small portion of resi-
tion behavior. Murakami et al. [5] conducted a questionnaire survey on dents begin to evacuate, while the majority remain in place without
tsunami warnings and evacuation behavior following the 2011 Great making an immediate decision. Ten minutes later, a noticeable increase
East Japan Earthquake and Tsunami in the same prefecture as the pre- in evacuation activity is observed. For residents near the coastline,
sent study area. The results showed that while the majority of re- evacuation toward inland areas requires crossing a bridge, resulting in
spondents (53.7 %) believed a tsunami would occur, they expected it to significant traffic congestion near this bottleneck. Some agents, how-
cause only minor damage. Some residents were unaware of the tsunami ever, choose to detour via the northern bridge to avoid the jam. Since
threat or believed it would not affect their area. Only a small portion pedestrian evacuees can only evacuate to the designated vertical shelter,
(12.7 %) perceived an imminent and severe danger. Regarding the and vehicle evacuees may also choose Exit 1 or the vertical shelter,
initial locations of residents at the time of the earthquake, the survey heavy traffic is observed along the Prefectural Road. Although most
found that approximately 58 % were at home, while the remainder were residents eventually begin to move or reach the shelter, a substantial
presumed to be outdoors. The spatial position of each agent is generated number still remain in place even 30 min after the earthquake. By 15:36,
randomly, as it is difficult to determine the exact positions of all resi- the majority of moving agents are pedestrians, as vehicle evacuees have
dents, and this issue falls outside the scope of the present study. already reached safety due to their higher travel speeds. In the end,
As for the disaster information, a massive earthquake with a agents who failed to evacuate or delayed evacuation remain on the move
magnitude of 9.0 struck Japan at 14:46 on March 11, 2011. A tsunami when the tsunami arrives and are ultimately considered casualties.
warning was issued three minutes after the earthquake. In the study The distribution of agent departure times is illustrated in Fig. 9. The
area, the initial tsunami height was estimated at 6 m Twenty-eight mi- results indicate that 95 % of individuals begin evacuation within 48 min
nutes later, a second bulletin revised the estimate to over 10 m This after the earthquake. The latest departure time observed is 63 min after
study utilizes numerically simulated tsunami data from Mas et al. [29], the earthquake, and the agent survives due to the short distance to a
which has been validated in previous research. The entire simulation nearby safe location. Given that the tsunami arrives approximately one
spans 70 min. Agents make decisions at fixed time intervals, meaning hour after the earthquake, this time window is generally sufficient for
the LLM is queried periodically. This decision interval must strike a reaching safety. Therefore, failure to evacuate or delayed departure
balance between computational efficiency and the temporal granularity emerges as the primary causes of fatalities. Additionally, some agents
needed to realistically simulate agent behavior. A very short interval who evacuate relatively early still perish, primarily due to slow move-
increases computational cost and is unrealistic, as people in real sce- ment, long travel distances, or changes in their intended shelter during
narios do not change decisions so frequently. Conversely, a long interval evacuation. These results are consistent with the findings of Goto et al.
reduces the responsiveness of agents and also fails to reflect realistic [6], who reported that most victims of the 2011 Great East Japan
human behavior. Based on experimental trials, a decision interval of two Earthquake and Tsunami were either at home or en route to evacuation
to four minutes is found to be appropriate for this framework. Therefore, sites at the time of inundation.
a three-minute interval is adopted in the case study to balance perfor-
mance and efficiency. Additionally, reconnaissance surveys revealed 3.2. Emergent behaviors of agents
that not all residents successfully received the tsunami warning or alerts
due to the complex and noisy post-earthquake environment [6]. A typical decision-making and evacuation process is illustrated in
Therefore, this study assumes that approximately 19 % of residents did Fig. 10, which shows the prompt inputs to the LLM and the corre-
not hear the tsunami warning [5]. sponding decisions generated at each time step. This example represents
9

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
Fig. 8. Snapshots of the simulation taken every 10 min. Different colors represent agents at various evacuation stages.
10

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
Fig. 9. Departure time of agents. Delayed departure emerges as the primary cause of fatalities.
a 23-year-old female agent accompanied by her child. At the moment of 3.3. Conventional ABM comparison
the earthquake, the agent is outdoors and initially decides to stay and
observe, believing that a tsunami would not occur. A few minutes later, To compare the proposed method with a conventional ABM, a
she receives a tsunami warning estimating a wave height of six meters. baseline simulation using a typical ABM framework was conducted for
Simultaneously, she overhears nearby individuals expressing panic and the same scenario. Specifically, agents’ evacuation departure times were
warning of the incoming tsunami, prompting her to evacuate immedi- sampled from a Gamma distribution. For destination selection, each
ately. While formulating her evacuation plan, she encounteres an elderly agent was assigned the nearest shelter, and route planning was based on
man calling for help and decided to assist him by evacuating together via the shortest path. These configurations represent common practices in
car toward Exit 2. During the journey, she encounters severe congestion traditional ABM approaches for disaster evacuation modeling [23,29,
along the originally planned route and opts for a detour to reach safety 43]. Additionally, agents in the conventional ABM were assumed to act
more quickly. Eventually, she successfully arrives at a safe location independently, without the ability to communicate, assist others, or
along with her child and the elderly man she assisted. This example il- revise their initial plans. For example, agents would continue along their
lustrates how the LLM-enhanced ABM can simulate agents’ dynamic pre-defined routes even in the presence of traffic congestion and would
decision-making and interpersonal communication, enabling more not switch shelters once arriving at a designated safe location. All other
realistic evacuation behaviors. However, this is an aspect that conven- settings, such as the initial population distribution, demographic attri-
tional rule-based ABMs often struggle to capture. butes, car ownership rates, and road network, were kept identical to
In addition to the dynamic evolution of agents’ decisions, the those in the LLM-enhanced ABM to ensure a fair comparison.
simulation also captures how information disseminates through social The road usage patterns generated by the LLM-enhanced ABM and
interactions. As previously noted, a small portion of agents do not the conventional ABM are shown in Fig. 12. Road usage is measured by
receive the official tsunami warning due to unexpected disruptions. the frequency with which each road segment is traversed by agents. For
However, some of these agents obtain the warning through conversa- car evacuees, roads near the vertical shelter, Exit 1, and Exit 2 are all
tions with neighbors or nearby individuals, which subsequently shapes heavily utilized in the LLM-enhanced ABM (Fig. 12a). In contrast, under
their evacuation decisions. Fig. 11presents several dialogue examples the conventional ABM (Fig. 12b), most agents choose the vertical shelter
illustrating this process. In Fig. 11a, a 73-year-old male, who is at home as their destination, leading to severe traffic congestion in its vicinity.
with his spouse and does not receive any official alert, overhears a Exit 1 is largely avoided, and only a small portion of agents select Exit 2.
neighbor mention a tsunami warning predicting wave heights exceeding This is because the vertical shelter, being centrally located within the
ten meters, urging people to evacuate. He then decides to gather village, is the closest option for most residents. Exit 1, on the other hand,
essential items and leave. In Fig. 11b, a 14-year-old female also misses is located farther away and is less frequently selected. However, this
the official warning. She hears one neighbor say they received a warning evacuation behavior does not align with real-world tendencies, as resi-
but are uncertain about its severity, advising cautious preparation. dents with access to vehicles often prefer to evacuate inland to safer
Meanwhile, another neighbor expresses doubt, saying they received no locations, even if it involves longer travel distances, due to their higher
alert and suspect the situation is not serious. Confronted with mixed mobility. The LLM-enhanced ABM more accurately reproduces this
signals, the girl ultimately chooses to stay and observe. behavior, yielding more realistic outcomes. Moreover, the simulation
Through interactions with one another, generative agents in this reveals that the central bridge connecting the two areas of the village
framework are able to exchange information, form spontaneous assis- acts as a traffic bottleneck. Although there is an alternative bridge at the
tance relationships, and dynamically respond to evolving situations. north that also provides a route inland, agents in the conventional ABM
These social behaviors emerge organically during the simulation, driven do not utilize it. This is because the conventional ABM relies simply on
by the integration of LLMs, rather than being pre-defined or explicitly the shortest-path algorithm, and agents lack the capacity to adjust their
programmed. This capacity for emergent behavior is a key innovation routes in response to congestion. In contrast, while agents in the LLM-
and a central contribution of this study. enhanced ABM also begin with shortest-path planning, they possess
the ability to dynamically revise their decisions. As a result, some agents
reroute through the northern bridge to avoid congestion, improving
11

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
Fig. 10. Illustration of a typical agent’s evacuation process. Agents enhanced with LLMs demonstrate adaptive and rational decision-making.
overall traffic flow. This adaptive route selection contributes to the vehicles to become stuck. As a result, some agents are still on the road
observed differences in road usage between the two approaches and when the tsunami arrives and are killed. In contrast, the LLM-enhanced
highlights the advantage of the proposed LLM-enhanced ABM frame- ABM gives more realistic results. It shows that delayed departures or
work in modeling realistic evacuation scenarios. intentional decisions to stay are the main causes of death.
For evacuees on foot, there is only one available evacuation option,
resulting in relatively minor differences in road usage patterns between
3.4. Validation with reports
the two methods, as shown in Fig. 12c and d. Previous studies have also
found that pedestrians have limited travel capacity within a short time
To further validate the proposed LLM-enhanced ABM, real-world
and are less affected by traffic congestion [44]. Therefore, they tend to
data are used to assess the accuracy of the simulation outcomes and
evacuate using the shortest available paths to reach safety. The results
demonstrate the model’s reliability. To account for uncertainty, twenty
from the LLM-enhanced ABM align with these observations, indicating
independent simulation runs are conducted. The number of casualties
that the proposed method not only captures the diverse and adaptive
and evacuees at the vertical shelter are recorded and compared with
behaviors of car evacuees but also reproduces the rational and consistent
reported disaster data. According to local media reports, between 200
evacuation patterns of pedestrian evacuees.
and 300 victims were found in the study area [29]. Fig. 13presents the
In the conventional ABM, most victims die due to severe traffic
distribution of casualties in simulations. All simulation results fall within
congestion. Many agents choose the same destination and follow the
or near the reported range, with an average of approximately 227 ca-
same route. This leads to extreme bottlenecks in certain areas. Although
sualties. The 95 % confidence interval (CI) also lies within this range,
agents begin evacuating earlier than those in the LLM-enhanced ABM,
although a few runs slightly underestimate the number of casualties due
with the latest departure at around 45 min, traffic jams cause many
to inherent randomness. Nevertheless, the results confirm the model’s
12

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
Fig. 11. Example of information dissemination among agents. (a) A male agent decides to evacuate after receiving an evacuation message from a neighbor. (b) A
female agent decides to stay and observe after hearing conflicting messages from different neighbors.
Fig. 12. Route usage of evacuees as determined by different methods. The comparison shows that the LLM-enhanced ABM aligns more closely with
observed behavior.
13

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
Fig. 13. Distribution of simulated casualties across 20 runs. The blue dashed line indicates the sample mean, and the blue shaded area represents the 95 % con-
fidence interval based on the t-distribution. The red shaded region indicates the reported casualty range (200–300) for validation.
ability to generate reasonable casualty estimates. tool for post-disaster emergency response and decision-making.
In addition, approximately 520 evacuees were reported [29] to have
taken shelter in the vertical evacuation building after the earthquake.
3.5. Sensitivity analysis and simulation cost
Fig. 14shows the number of evacuees at the vertical shelter across all
simulation runs. The average number of evacuees is around 533, which
To test the sensitivity of decision-making across different LLMs,
closely matches the reported figure. The 95 % CI ranges from 516.9 to
identical prompts representing various scenarios were input into several
549.3, which includes the real value. While exact matches are unlikely
popular models, including DeepSeek, GPT, and Claude. The corre-
in stochastic simulations, the average estimates of both casualties and
sponding decisions are summarized in Table 1. In Scenario 1, a female
shelter occupancy indicate that the proposed model effectively captures
agent was outdoors and believed the tsunami would cause only minor
key aspects of human decision-making and evacuation outcomes.
damage. All models chose the same action, stay and observe, although
Furthermore, the heavy traffic simulated along the prefectural road
the content of their communications differed slightly. In Scenario 2, a
is also reported by survivors, as mentioned in news articles [50] and
female agent had just returned home. DeepSeek decided to evacuate
reflected in Figs. 8 and 12. The main causes of death identified in the
immediately, while GPT and Claude suggested preparing briefly before
simulation, such as delayed evacuation, are consistent with those re-
evacuating. Despite minor differences in timing, all models shared the
ported in real-world data. This alignment demonstrates that the pro-
same core decision: do not stay in place and begin evacuation prepa-
posed model performs well in reproducing realistic evacuation
rations. In Scenario 3, a male agent was evacuating by car with his
scenarios. It shows strong potential as a high-fidelity, reliable support
spouse. DeepSeek and Claude both decided to take a detour due to road
Fig. 14. Distribution of simulated number of people in vertical shelters across 20 runs. The blue dashed line denotes the sample mean, while the blue shaded region
shows the 95 % confidence interval derived from the t-distribution. The red vertical line corresponds to the reported value of 520.
14

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
Table 1 English word, a number, or a symbol is treated as one token. On average,
The decisions made by different LLMs. one English character corresponds to approximately 0.3 tokens,
Scenario Deepseek GPT Claude although this ratio may vary depending on the model’s tokenization
method. In this study, each simulation round generates approximately
Scenario 1: A 59- "Action next": "Action next": "Stay "Action next":
five million input tokens and one million output tokens. Using the
year-old "Stay and and observe, "Stay and
female. observe", "Feeling score": "2, observe", DeepSeek model, the computational cost per round is around three U.S.
currently "Feeling score": "Exchange "Feeling score": dollars, while the cost is significantly higher when using models such as
outdoors, have "2", information": "Did "2", GPT.
a car. Relevant "Exchange anyone feel that "Exchange
Although the LLM-enhanced ABM entails higher computational
memories: She information": "It strongly? It didn’t information":
thought was just a tremor. last long… you think "Did anyone else costs, the resulting improvements in behavioral realism, dynamic
tsunami would I’ve lived here there’s any chance feel that decision-making, and emergent communication justify the additional
come with my whole life, of a tsunami?" earthquake? I expense, particularly in applications requiring high-fidelity evacuation
little damage. and the water wonder if my modeling for life-critical scenarios. As LLM inference efficiency ad-
never comes far. husband felt it
vances and more optimized models become available, the associated
No need to run too. Do you think
off just yet." we should be computational burden is expected to decline. This trend enhances the
worried about feasibility of deploying the proposed LLM-enhanced ABM framework at
anything?" scale in real-world disaster response and emergency management
Scenario 2: A 42- "Action next": " "Action next": "Take "Action next":
systems.
year-old Evacuate time to prepare, "Take time to
female immediately", then evacuate, prepare, then
currently at "Feeling score": "Feeling score": "3, evacuate", 4. Conclusion
home, have a "4", "Exchange "Feeling score":
car. Relevant "Exchange information": " Are "3",
This study proposes a novel LLM-enhanced ABM framework for
memories: She information": " I you leaving too? "Exchange
simulating crowd evacuation during disaster emergencies. The core
had no idea of just saw the Maybe we should information": "I
tsunami. At water pull back head inland just in just drove back innovation lies in replacing the conventional rule-based decision-mak-
first, she way too far from case." home after the ing mechanisms in ABM with LLMs. In this framework, agents are
decided to the shore! That earthquake - the capable of autonomously generating prompts based on their personality
remain in means a tsunami roads are getting
traits, current environment, and memory of past actions. The prompts
place, is coming, right more congested.
assessing the now! Don’t wait, Should we be serve as inputs to LLMs, enabling agents to make context-aware de-
situation. get to high worried about cisions, interact with others, and dynamically respond to evolving
Then, she ground!" something more disaster scenarios in a more human-like and adaptive manner than
decided to than just
conventional method. To address the computational challenges posed by
return to your aftershocks?"
large-scale agent populations, the framework incorporates batch
residence from
outside by car. prompting and parallel LLM requests to significantly improve efficiency.
Scenario 3: A 31- "Action next": "Action next": " "Action next ": The simulation module interprets LLM-generated decisions and simu-
year-old male. "Take a detour to Continue driving "Take a detour to lates agent movements via both pedestrian and vehicular modes, using a
currently Road10", along Road 81", Road 10",
road network built from GIS data for spatial accuracy. This decision-
moving "Feeling score": "Feeling score": "Feeling score":
towards exit by "4", "3′’, "Exchange "3", action loop is executed at fixed intervals throughout the simulation.
car with "Exchange information": "The "Exchange A real-world case study on tsunami evacuation is conducted to
spouse. information": warning’s worse information": validate the proposed framework and highlight its advantages over
Relevant "The warning just now—over ten "The wave height conventional ABMs. The results demonstrate the model’s ability to
memories: He got worse—over meters. But Road just went up to
had no idea of ten meters. I’m 81′s still dry and over 10 m—we simulate dynamic decision-making and interpersonal communication
tsunami. He turning onto moving. Let’s stay need to move among agents, leading to emergent behaviors such as information
decided to Road 10 now. It’s on this route unless faster. I’m dissemination and cooperative evacuation. Notably, the primary cause
begin narrow but we see water ahead. switching to of fatalities in the simulation is consistent with post-disaster survey
evacuating moving. We have Keep checking the Road 10 to avoid findings, further supporting the model’s realism. Compared to tradi-
toward Exit 1 to get to higher road updates on this heavy traffic.
by car. ground." your phone, okay? " Everyone else is tional ABMs, the LLM-enhanced ABM generates more realistic evacua-
taking it too." tion patterns and road usage, offering deeper insights for emergency
response planning. Additionally, the simulated numbers of casualties
and evacuees closely match the reported data, underscoring the frame-
congestion, whereas GPT chose to continue along the planned route.
work’s reliability. All stochastic simulation results fall within or near the
Although variations exist among the models, their overall tendencies
reported data and the 95 % confidence interval also lies within reported
align and remain consistent with human reasoning. While the exact
range. The study also provides a analysis of the model’s computational
phrasing of exchanged information differs across LLMs, and even be-
cost in terms of time and billing, offering practical guidance for real-
tween repeated queries to the same model, the essential content and
world applications. Each simulation round consumes approximately
logical flow are similar. Overall, all tested LLMs produce reasonable,
five million input tokens and one million output tokens.
consistent, and reproducible results, highlighting the robustness and
While this work represents a significant step toward integrating
rationality of the proposed framework.
LLMs with ABM for high-fidelity disaster simulation, some limitations
The computation time for one simulation round is approximately
remain. The current movement module relies on simplified assumptions
three hours, with over one-third of that time spent processing LLM re-
for both pedestrian and vehicular dynamics, which allows us to focus on
quests. Nevertheless, the framework supports parallel execution,
the core contribution of this work: the integration of LLM-based deci-
allowing multiple simulations to be run concurrently. For example,
sion-making. Nevertheless, the framework is modular and can be readily
executing 20 simulations in parallel would require approximately the
extended to incorporate more advanced traffic simulation models to
same wall-clock time as a single run. As the number of agents and de-
better capture real-world movement and congestion patterns. Future
cision queries increases, the total computation time grows accordingly.
research should also explore scaling the framework to larger populations
In LLMs, tokens are the basic units used to represent natural language
and broader geographic areas, which will require further improvements
text and are also the units for billing. Typically, a Chinese word, an
in computational efficiency and code optimization. This study focused
15

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
on the 2011 Arahama tsunami case, where sufficient empirical and [6] Y. Goto, T. Mikami, I. Nakabayashi, Fact-finding about the evacuation from the
comparative data are available. Validation for other disaster types re- unexpectedly large tsunami of March 11, 2011 East Jpn., in: 2012.
[7] Chen C, Mostafizi A, Wang H, Cox D, Cramer L. Evacuation behaviors in tsunami
mains an important direction for future research to enhance the drills. Nat Hazards 2022;112:845–71. https://doi.org/10.1007/s11069-022-
framework’s general applicability. Moreover, the concept of LLM- 05208-y.
enhanced ABM can be transferred to other contexts, such as digital [8] Lu X, Yang Z, Cimellaro GP, Xu Z. Pedestrian evacuation simulation under the
scenario with earthquake-induced falling debris. Saf Sci 2019;114:61–71. https://
twins, by leveraging the LLMs’ ability to reason and communicate.
doi.org/10.1016/j.ssci.2018.12.028.
Overall, this study demonstrates the feasibility and potential of using [9] Z. Zhang, Q. Li, Q. Sun, L. Ceferino, Investigating the feasibility of using virtual
LLMs to enhance agent-based simulations for disaster evacuation, of- reality to study Human response to flood risk in 3D flood simulation, (2025).
https://doi.org/10.31224/4620.
fering a promising direction for developing intelligent, adaptive, and
[10] Mesta C, Ceferino L, Cremen G, Galasso C. Investigating post-earthquake hospital
high-fidelity tools to support emergency response and decision-making transportation for casualties through agent-based modeling. Earthq Spectra 2025:
in complex real-world scenarios. This research bridges the gap be- 87552930251328386. https://doi.org/10.1177/87552930251328386.
[11] Senanayake GPDP, Kieu M, Zou Y, Dirks K. Agent-based simulation for pedestrian
tween human-centered behavioral modeling and engineering decision-
evacuation: a systematic literature review. Int J Disaster Risk Reduct 2024;111:
support, offering a novel tool for disaster preparedness and resilience 104705. https://doi.org/10.1016/j.ijdrr.2024.104705.
planning. [12] Mas E, Koshimura S, Imamura F, Suppasri A, Muhari A, Adriano B. Recent
advances in agent-based tsunami evacuation simulations: case studies in Indonesia,
Thailand, Japan and Peru. Pure Appl Geophys 2015;172:3409–24. https://doi.org/
CRediT authorship contribution statement 10.1007/s00024-015-1105-y.
[13] Aghababaei M, Koliou M. Community resilience assessment via agent-based
Sen Yang: Writing – review & editing, Writing – original draft, modeling approach. Comput Aided Civ Eng 2022. https://doi.org/10.1111/
mice.12916. mice.12916.
Visualization, Validation, Investigation, Formal analysis, Data curation, [14] Du E, Wu F, Jiang H, Guo N, Tian Y, Zheng C. Development of an integrated socio-
Conceptualization. Luis Ceferino: Validation, Supervision, Methodol- hydrological modeling framework for assessing the impacts of shelter location
ogy, Investigation, Conceptualization. Yi Zhang: Writing – review & arrangement and human behaviors on flood evacuation processes. Hydrol Earth
Syst Sci 2023;27:1607–26. https://doi.org/10.5194/hess-27-1607-2023.
editing, Supervision, Software, Resources, Project administration,
[15] Raja G, Anbalagan S, Ganapathisubramaniyan A, Selvakumar MS, Bashir AK,
Investigation, Funding acquisition. Chen Gu: Supervision, Methodol- Mumtaz S. Efficient and secured swarm pattern multi-UAV communication. IEEE
ogy, Investigation, Funding acquisition. Tong Guo: Writing – review & Trans Veh Technol 2021;70:7050–8. https://doi.org/10.1109/TVT.2021.3082308.
[16] Liu J, Fan Y, Sun R, Liu L, Wu C, Mumtaz S. Blockchain-aided privacy-preserving
editing, Software, Resources, Funding acquisition. Gen Kondo: Writing
medical data sharing scheme for E-Healthcare system. IEEE Internet Things J 2023;
– review & editing, Conceptualization. 10:21377–88. https://doi.org/10.1109/JIOT.2023.3287636.
[17] Lu P, Li Y. Agent-based fire evacuation model using social learning theory and
intelligent optimization algorithms. Reliab Eng Syst Saf 2025;260:111000. https://
Declaration of competing interest
doi.org/10.1016/j.ress.2025.111000.
[18] Bahmani H, Ao Y, Yang D, Xu Q, Zhao J. Enhancing evacuation safety in urban
The authors declare that they have no known competing financial primary schools: an agent-based model integrating child development behaviour
and health dynamics. Reliab Eng Syst Saf 2026;265:111591. https://doi.org/
interests or personal relationships that could have appeared to influence
10.1016/j.ress.2025.111591.
the work reported in this paper. [19] Yang Y, Yin J, Wang D, Liu Y, Lu Y, Zhang W, Xu S. ABM-based emergency
evacuation modelling during urban pluvial floods: a “7.20” pluvial flood event
study in Zhengzhou, Henan Province. Sci China Earth Sci 2023;66:282–91. https://
Acknowledgements
doi.org/10.1007/s11430-022-1015-6.
[20] Zhang R, Liu D, Du E, Xiong L, Chen J, Chen H. An agent-based model to simulate
This work was supported by the National Key R&D Program of China human responses to flash flood warnings for improving evacuation performance.
J Hydrol 2024;628:130452. https://doi.org/10.1016/j.jhydrol.2023.130452.
[2023YFC3081300], Beijing Natural Science Foundation [L231010],
[21] Zhang R, Liu D, Xiong L, Chen J, Chen H, Yin J, Wang J. An agent-based modeling
National Natural Science Foundation of China [52478531, method to determine the number of flash flood warnings for improving the
52311540150] and the Research Fund for Advanced Ocean Institute of warning response levels. J Hydrol 2024;640:131709. https://doi.org/10.1016/j.
Southeast University, Nantong (Major Program). All sources of support jhydrol.2024.131709.
[22] Harris A, Roebber P, Morss R. An agent-based modeling framework for examining
are gratefully acknowledged. the dynamics of the hurricane-forecast-evacuation system. Int J Disaster Risk
Reduct 2022;67:102669. https://doi.org/10.1016/j.ijdrr.2021.102669.
Supplementary materials [23] Wang H, Mostafizi A, Cramer LA, Cox D, Park H. An agent-based model of a
multimodal near-field tsunami evacuation: decision-making and life safety. Transp
Res C Emerg Technol 2016;64:86–100. https://doi.org/10.1016/j.trc.2015.11.010.
Supplementary material associated with this article can be found, in [24] Nguyen D-T, Shen Z, Truong M-H, Sugihara K. Improvement of evacuation
the online version, at doi:10.1016/j.ress.2025.112056. modeling by considering road blockade in the case of an earthquake: a case study
of Daitoku School District. Kanazawa City Jpn Sustain 2021;13:2637. https://doi.
org/10.3390/su13052637.
Data availability [25] Takabatake T, Fujisawa K, Esteban M, Shibayama T. Simulated effectiveness of a
car evacuation from a tsunami. Int J Disaster Risk Reduct 2020;47:101532.
https://doi.org/10.1016/j.ijdrr.2020.101532.
Data will be made available on request.
[26] Muhammad A, De Risi R, De Luca F, Kongko W, Mori N, Yasuda T, Goda K.
Integrated tsunami risk framework considering agent-based evacuation modelling:
References the case of Saga, Kochi Prefecture, Japan. Int J Disaster Risk Reduct 2024;101:
104193. https://doi.org/10.1016/j.ijdrr.2023.104193.
[27] Takabatake T, Nagashima W, Hasegawa N. Reinforcement learning-based
[1] Yang S, Zhang Y, Lu X, Guo W, Miao H. Multi-agent deep reinforcement learning
optimization of tsunami evacuation paths: effectiveness and robustness in two
based decision support model for resilient community post-hazard recovery. Reliab
coastal areas in Japan. Reliab Eng Syst Saf 2026;266:111594. https://doi.org/
Eng Syst Saf 2024;242:109754. https://doi.org/10.1016/j.ress.2023.109754.
10.1016/j.ress.2025.111594.
[2] Yang S, Zhang Y, Luo M, Guo J, Guo W, Guo T, Ma J. Augmented neural ordinary
[28] Samanez EAM. Development of An Integrated Simulator for Tsunami Inundation
differential equations with physical information for structural seismic response
and Agent Based Evacuation. Tohoku University; 2012. Thesis.
prediction using limited data. Eng Struct 2025;332:120087. https://doi.org/
[29] Mas E, Suppasri A, Imamura F, Koshimura S. Agent-based simulation of the 2011
10.1016/j.engstruct.2025.120087.
Great East Japan Earthquake/Tsunami Evacuation: an integrated model of tsunami
[3] Yang S, Zhang Y, Guo T, Luo M, Guo J, Ma J. Rapid regional assessment of post- inundation and evacuation. J Nat Disaster Sci 2012;34:41–57. https://doi.org/
hazard structures and transportation infrastructure using aerial images. Comput
Aided Civ Eng 2025;40:3833–52. https://doi.org/10.1111/mice.70015. 10.2328/jnds.34.41.
[30] Takabatake T, Hasegawa N, Yamaguchi K, Esteban M. Comparative analysis of
[4] Han Z, Meng L, Mitani Y, Kawano K, Sugahara T, Taniguchi H, Honda H, Li Z.
Tsunami casualty estimation approaches: agent-based modeling versus simplified
Machine learning-based assessment of building evacuation vulnerability at the pre- approach in Japanese coastal cities. Int J Disaster Risk Sci 2024;15:719–37.
disaster stage. Sustain Cities Soc 2025;130:106571. https://doi.org/10.1016/j.
https://doi.org/10.1007/s13753-024-00586-2.
scs.2025.106571.
[31] Z. Wu, R. Peng, X. Han, S. Zheng, Y. Zhang, C. Xiao, Smart agent-based modeling:
[5] H. Murakami, K. Takimoto, A. Pomonis, Tsunami evacuation process and Human
on the use of large language models in computer simulations, (2023). https://doi.
loss distribution in the 2011 Great East Japan Earthquake - A case study of Natori
org/10.48550/arXiv.2311.06330.
City, Miyagi Prefect., in: 2012.
16

S. Yang et al. R e l i a b i l i t y E n g i n e e r i n g a n d S y s t e m S a f e t y 269 (2026) 112056
[32] Gao C, Lan X, Li N, Yuan Y, Ding J, Zhou Z, Xu F, Li Y. Large language models [40] OpenAI, OpenAI API platf. doc., (2025). https://platform.openai.com/docs
empowered agent-based modeling and simulation: a survey and perspectives. /overview.
Humanit Soc Sci Commun 2024;11:1259. https://doi.org/10.1057/s41599-024- [41] De Iuliis M, Battegazzorre E, Domaneschi M, Cimellaro GP, Bottino AG. Large scale
03611-3. simulation of pedestrian seismic evacuation including panic behavior. Sustain
[33] Falegnami A, Tomassi A, Corbelli G, Nucci FS, Romano E. A generative artificial- Cities Soc 2023;94:104527. https://doi.org/10.1016/j.scs.2023.104527.
intelligence-based workbench to test new methodologies in organisational health [42] Tomassi A, Falegnami A, Romano E. Talking resilience: embedded natural
and safety. Appl Sci 2024;14:11586. https://doi.org/10.3390/app142411586. language cyber-organizations by design. Systems 2025;13:247. https://doi.org/
[34] Zhang C, Chen J, Li J, Peng Y, Mao Z. Large language models for human–robot 10.3390/systems13040247.
interaction: a review. Biomim Intell Robot 2023;3:100131. https://doi.org/ [43] Chen C, Koll C, Wang H, Lindell MK. An interdisciplinary agent-based evacuation
10.1016/j.birob.2023.100131. model: integrating the natural environment, built environment, and social system
[35] Park JS, O’Brien J, Cai CJ, Morris MR, Liang P, Bernstein MS. Generative agents: for community preparedness and resilience. Nat Hazards Earth Syst Sci 2023;23:
interactive simulacra of human behavior. In: Proceedings of the 36th Annual ACM 733–49. https://doi.org/10.5194/nhess-23-733-2023.
Symposium on User Interface Software and Technology. San Francisco CA USA: [44] Makinoshima F, Imamura F, Abe Y. Behavior from Tsunami recorded in the
ACM; 2023. p. 1–22. https://doi.org/10.1145/3586183.3606763. multimedia sources at Kesennuma City in the 2011 Tohoku Tsunami and its
[36] J. Wang, R. Jiang, C. Yang, Z. Wu, M. Onizuka, R. Shibasaki, N. Koshizuka, C. Xiao, simulation by using the evacuation model with pedestrian—Car interaction. Coast.
Large language models as urban residents: an LLM agent framework for personal Eng. J. 2016;58. https://doi.org/10.1142/S0578563416400234. 1640023-1-
mobility generation, in: 2024: pp. 124547–74. https://doi.org/10.48550/arXiv.2 1640023–28.
402.14744. [45] Treiber M, Hennecke A, Helbing D. Congested traffic states in empirical
[37] Lu T, Zhang Y, Xie W, Huang X. Human-AI interactive framework for smart observations and microscopic simulations. Phys Rev E 2000;62:1805–24. https://
evacuation safety analysis in large infrastructures. Reliab Eng Syst Saf 2026;266: doi.org/10.1103/PhysRevE.62.1805.
111695. https://doi.org/10.1016/j.ress.2025.111695. [46] Tomassi A, Falegnami A, Romano E. Unveiling simplexity: a new paradigm for
[38] Jin Z, Wang Y, Li C, Yu C, Ye X, Mu J. Exploring heterogeneity in evacuation understanding complex adaptive systems and driving technological innovation.
decision of urban residents between utility and regret decision rules under a flood Innovation 2025;6:100954. https://doi.org/10.1016/j.xinn.2025.100954.
hazard. Sustain Cities Soc 2025;130:106562. https://doi.org/10.1016/j. [47] DeepSeek-AI. DeepSeek-V3 technical report. https://arxiv.org/abs/2412.19437;
scs.2025.106562. 2024.
[39] Cheng Z, Kasai J, Yu T. Batch prompting: efficient inference with large language [48] Yagi M, Managi S. Demographic determinants of car ownership in Japan. Transp
model APIs. In: Proceedings of the 2023 Conference on Empirical Methods in Policy 2016;50:37–53. https://doi.org/10.1016/j.tranpol.2016.05.011.
Natural Language Processing: Industry Track. Singapore: Association for [49] Statistic Bureau of Japan. Population census. https://www.stat.go.jp/english/
Computational Linguistics; 2023. p. 792–810. https://doi.org/10.18653/v1/2023. data/kokusei/2000/kihon1/00/04.html; 2001.
emnlp-industry.74. [50] Konno M. Midori Wokshop Wakabayashi-evacuating. https://www.miyagi-selp.
org/311sorekara/en/earthquake/44; 2025.
17
