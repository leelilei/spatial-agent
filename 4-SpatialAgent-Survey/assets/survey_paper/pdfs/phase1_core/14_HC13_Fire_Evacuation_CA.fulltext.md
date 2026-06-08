Title: Large-language-model-driven agents for fire evacuation simulation in a cellular automata environment

Source PDF: D:\0-AI相关研究\1-spatialagent\spatial-agent\assets\survey_paper\pdfs\phase1_core\14_HC13_Fire_Evacuation_CA.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-04-27T13:19:40+00:00
- page_count: 13
- status: ok
- text_char_count: 70097

Metadata:
- author: Pei Dang
- doi: 10.1016/j.ssci.2025.106935
- keywords: Large language model, Fire evacuation, Multi agent, Cellular automata
- subject: Safety Science, 191 (2025) 106935. doi:10.1016/j.ssci.2025.106935

Outline:
- Large-language-model-driven agents for fire evacuation simulation in a cellular automata environment (page 1)
  - 1 Introduction (page 1)
  - 2 Background (page 2)
    - 2.1 Agent-based fire evacuation model (page 2)
    - 2.2 Multi-agent evacuation systems (page 2)
  - 3 Method (page 2)
    - 3.1 Agent memory and cognitive constraints (page 2)
    - 3.2 Characterization of evacuation environments and autonomous actions (page 4)
      - 3.2.1 Cell-semantic hybrid modeling for evacuation environments (page 4)
      - 3.2.2 LLM-agent action framework (page 5)
    - 3.3 Multi-agent interaction behavior (page 6)
  - 4 Experiment and result (page 6)
    - 4.1 Experiment design (page 6)
      - 4.1.1 Construction of a three-dimensional experimental scenario (page 6)
      - 4.1.2 Simulation of flames and smoke (page 7)
      - 4.1.3 Evacuees and initial paths (page 7)
      - 4.1.4 Experimental and control group setup (page 7)
    - 4.2 Results (page 7)
      - 4.2.1 Evacuation duration and paths (page 7)
      - 4.2.2 Evacuation decisions (page 7)
  - 5 Discussion (page 9)
    - 5.1 Evacuation efficiency (page 9)
    - 5.2 Evacuation behaviors (page 10)
    - 5.3 Reasoning-based evacuation decision (page 11)
  - 6 Conclusion and future work (page 11)
  - CRediT authorship contribution statement (page 12)
  - Declaration of competing interest (page 12)
  - Acknowledgements (page 12)
  - Data availability (page 12)
  - References (page 12)

Markdown Content:

Safety Science 191 (2025) 106935
Contents lists available at ScienceDirect
Safety Science
journal homepage: www.elsevier.com/locate/safety
Large-language-model-driven agents for fire evacuation simulation in a
cellular automata environment
Pei Danga, Jun Zhua,*, Weilian Lia, Yakun Xiea, Heng Zhangc,d
aFaculty of Geosiences and Engineering, Southwest Jiaotong University, Chengdu 611756, China
cChina Railway Design Corporation, Tianjin 300308, China
dNational Engineering Research Center for Digital Construction and Evaluation Technology of Urban Rail Transit, Tianjin 300308, China
A R T I C L E I N F O A B S T R A C T
Keywords: This study presents a multi-agent fire evacuation model driven by large language models (LLMs), aiming to
Large language model simulate human-like decision-making and behaviors during fire emergencies. The proposed model endows agents
Fire evacuation with personalized memory, cognition, and decision-making capabilities through LLMs, while characterizing the
Multi agent
evacuation environment using a combination of spatial semantics and cellular automata. This approach enables
Cellular automata
agents to perceive, decide, and move within a unified spatiotemporal framework. The model is tested using
various LLMs with different scales, including ChatGPT 4.0, ERNIE-Bot 4.0, Llama-2-70B-Chat, and ChatGLM2-
6B-32K, in a simulated shopping mall fire evacuation scenario constructed from LiDAR scans and 3D recon-
struction. Experimental results demonstrate that the LLM-driven agents exhibit exploratory and adaptive be-
haviors consistent with real-world scenarios, with larger-scale LLMs generating more consistent and efficient
evacuation strategies. The study also reveals the impact of agent background settings and communication be-
haviors on evacuation outcomes. This research contributes to the advancement of intelligent agent-based
modeling for emergency evacuation simulations and provides insights into the potential of LLMs in enhancing
the realism and effectiveness of such models. Future work should focus on increasing scenario complexity, model
interpretability, and controllability to better serve real-world evacuation management and decision-making.
1. Introduction while Colombo and Rosini (2005) analyzed high-density crowd dy-
namics with shock wave theory. However, these models struggle to
With the increase in population and the growing complexity of capture individual behaviors and micro-interactions due to their neglect
buildings, fire evacuation simulation has become particularly important. of individual heterogeneity, such as decision-making and local in-
Utilizing mathematical and computational tools, these models are teractions (Li et al., 2018). Microscopic models simulate individual
capable of simulating the evacuation behavior of individuals during a attributes—such as movement speed, target location, and decision-
fire, detailing the movement of people, building structures, and the making logic—along with their interactions, including environmental
spread of fire. Through quantitative analysis, fire evacuation simulation responses and behaviors like avoidance and following, to achieve
can assist decision-makers in optimizing evacuation routes, allocating bottom-up emergence of group behavior. Typical approaches include
emergency resources reasonably, and providing a basis for the formu- the Social Force Model and Agent-Based Models (Helbing & Moln´ar,
lation of emergency plans. These models play a crucial role in disaster 1995; Pan et al., 2007). However, these models require significant
prevention, mitigation, and enhancing public safety. computational resources in large-scale scenarios (Dang et al., 2021). The
Currently, fire evacuation models can be categorized into three hybrid model integrates the strengths of both macro and micro levels,
types: macroscopic models, microscopic models, and hybrid models striving to strike a balance between the two, and is suitable for complex
(Ronchi et al., 2019; Chen et al., 2021; Kaur and Kaur, 2022). Macro- evacuation scenarios involving multi-scale interactions (Tissera et al.,
scopic models simulate crowd movement using hydrodynamic equations 2012; Hassannayebi et al., 2022). For instance, Xiong et al. (2022)
or continuum theory, focusing on overall behavior. For example, Hughes combined the continuum model with the cellular automaton model,
(2002) modeled pedestrian flow akin to the Navier-Stokes equations, which not only reflects the overall movement trends of crowds but also
* Corresponding author.
E-mail address: zhujun@swjtu.edu.cn(J. Zhu).
https://doi.org/10.1016/j.ssci.2025.106935
Received 12 October 2024; Received in revised form 1 June 2025; Accepted 21 June 2025
Available online 7 July 2025
0925-7535/© 2025 Published by Elsevier Ltd.

P. Dang et al. S a f e t y S c i e n c e 191 (2025) 106935
captures the diverse behaviors of individuals. However, such models communicate and interact with other Agents. These elements make
must also overcome the inherent limitations of each approach. Agents’ behavior and decision-making in fire evacuation more human-
With the development of artificial intelligence technology, compu- like, aiming to simulate humans. Research on Agents spans diverse
tational power and efficiency have significantly improved, making it areas such as crowd behavior simulation (Helbing et al., 2000; Lovreglio
easier for researchers to conduct studies on microscopic algorithms. An et al., 2016), evacuation environment modeling (Pelechano & Badler,
Agent is a type of microscopic model that simulates human attributes 2006; Chen et al., 2006), social interactions (Moussaïd et al., 2010), real-
and behavior, making decisions based on the environment (Shi et al., time simulation (Zheng et al., 2009), and virtual reality (Ronchi et al.,
2009). Agent-based models simulate human behavior in real-world en- 2016; Dang et al., 2021). These studies significantly contribute to Agent
vironments by defining attributes, behaviors, and mechanisms (Gilbert construction, environmental complexity, method integration, and sce-
and Terna, 2000; Pan et al, 2007). Researchers hope to achieve swarm nario diversity. However, limitations exist as Agents’ behaviors are
intelligence by endowing Agents with more elements, making the Agent- predefined, and simulating all human behaviors is unattainable. Despite
based model exhibit behavior similar to humans (Li et al., 2018). Despite progress with deep learning (Chen & Xue, 2015; Zhao et al., 2020; Hou
the success of Agent-based models, there are still limitations, such as the et al., 2022; Zhu et al., 2023), a comprehensive method to simulate
complexity of the system due to considering too many elements, and the human behavior is lacking. Systems that fully simulate human behavior
difficulty in quantifying and simulating human emotions, psychology, or thought are termed Artificial General Intelligence (AGI), defined as AI
and cultural factors (LEE & Malkawi, 2013). systems with human-like intelligence (Minsky, 1961; Turing, 2009; Legg
In recent years, LLMs based on the Transformer architecture have and Hutter, 2007). Recent emergent capabilities of LLMs show signifi-
demonstrated groundbreaking progress in cognitive tasks. Models like cant progress towards AGI, exhibiting capabilities that approach or
ChatGPT and Claude3.5, trained on massive text corpora, have not only surpass human abilities in some tasks (Wu et al., 2023), offering a
acquired factual memory capabilities but also exhibited decision- promising method for Agent-based fire evacuation simulation.
making levels comparable to humans in reasoning tasks (Aidan Gilson
et al., 2023; Zhu et al., 2024a). Current research has begun exploring the 2.2. Multi-agent evacuation systems
potential of LLMs in fire evacuation decision support, such as optimizing
dynamic path planning (Dang et al., 2024; Durmus et al., 2024; Luo MAS consist of multiple intelligent agents capable of acting inde-
et al., 2025) and analyzing social media behavioral data (Wu et al., pendently and cooperating to achieve objectives (Tampuu et al., 2015).
2025). However, existing studies primarily focus on technical adapta- In MAS, each agent possesses a certain degree of autonomy, enabling
tions at the task execution level and have yet to systematically construct self-initiated decisions and actions. Key features of MAS include au-
an LLM-based human cognition-behavior fire evacuation simulation tonomy, local perspectives, decentralization, and the capacity for both
framework, lacking dynamic simulations of individual risk perception collaboration and competition. Within fire evacuation simulations, the
and behavioral decision-making. Meanwhile, LLMs have already characteristics of MAS can be further defined as follows: each agent
demonstrated human-like thought patterns in other tasks (Yoo and Lee, represents an independent evacuee controlling their own state and
2023; Webb et al., 2023), providing a theoretical foundation for building behavior; each agent only accesses local information around them or
fire evacuation agent models. Nevertheless, translating this potential obtains information through communication with other agents;
into practical applications still faces challenges: how to enable LLMs to decision-making is decentralized among agents without a single control
perceive fire evacuation scenarios through language descriptions and point; agents may collaborate and compete during evacuation (Sharma
how to simulate interactions between individuals and between in- et al., 2018).
dividuals and the environment. The application and study of MAS in evacuation scenarios are
In response to these issues, we have designed an Agent-based fire becoming increasingly significant, especially in simulating and man-
evacuation model built upon LLMs, aiming to create credible intelligent aging crowd evacuations during emergencies. Research includes inte-
agents that simulate individuals with varying attributes during a fire grating MAS with the Internet of Things to recommend the most efficient
evacuation. These agents possess independent physiological attributes, evacuation routes (Neto et al., 2019); expanding MAS parameters to
memory, and decision-making capabilities, and can communicate with optimize evacuation processes (Zhang & Shen, 2019); incorporating
other agents to collaboratively complete fire evacuation tasks. robots into evacuation processes and assessing their impact on evacua-
tion with MAS (Uchiya et al., 2019); and combining MAS with fuzzy
2. Background logic to enhance the realism and effectiveness of simulated individual
evacuations (Sahin et al., 2019). These studies aim to improve the re-
2.1. Agent-based fire evacuation model alism of evacuations using MAS or to extend MAS to accommodate more
evacuation scenarios. Despite significant progress, these approaches are
Agent-based fire evacuation models are computational methods that mostly tailored for specific evacuation scenarios and require additional
utilize agent technology to simulate and analyze the evacuation process parameters to control evacuation processes for more realistic individual
of people in fire scenarios. In these algorithms, each evacuee is consid- behaviors, making it challenging for MAS to balance between parameter
ered an intelligent agent with autonomous decision-making capabilities, (or rule) specificity and universality. Adopting reasoning methods can
making decisions based on their perception of the environment, in- effectively reduce the number of parameters and rules, and LLMs offer
teractions with other agents, and self-awareness. Multi-Agent Systems potential solutions to this issue.
(MAS) allow for a bottom-up approach to evacuation, where the col-
lective evacuation outcome is derived from simulating individual be- 3. Method
haviors, a capability beyond the reach of macroscopic evacuation
algorithms. Agent models are computation-intensive algorithms that 3.1. Agent memory and cognitive constraints
were challenging to implement on traditional computing systems, but
recent advancements in GPU computing chips and parallel computing Memory serves as the foundation for humanoid agents to simulate
technologies have made it possible to develop more complex Agent human behavior and decision-making, supporting the accumulation of
models. experience and behavioral evolution (Zhu et al., 2024b), and providing
Agent models typically require three elements: first, an Agent is an data support for learning adaptability (Dang et al., 2023). In multi-agent
autonomous entity with its own needs, reactivity, proactivity, and social fire evacuation scenarios, agent interactions rely on memory construc-
behaviors (Jennings & Wooldridge, 1998). Second, they must interact tion. However, while LLMs can utilize pre-trained knowledge to process
with the environment, sensing and altering it. Third, they should general information, they struggle to simulate individual specificity (e.
2

P. Dang et al. S a f e t y S c i e n c e 191 (2025) 106935
g., age differences). To address this, two strategies are needed: 1) prompt (continued)
constraints (e.g., “simulate the decision-making of an 8-year-old child”) Perceive Environment
to limit the model’s output range; and 2) task fine-tuning, optimizing the Decision =Query LLM (Perception +History)
model through training with specific data. Due to resource efficiency, Update History
Update Agent Intention Based On Decision
prompt constraints are more practical.
END FOR
The conversational mechanism of LLMs limits the context of user END IF
input. Despite expanding context length, research indicates that overly FOR EACH Agent DO
long contexts can cause LLMs to overlook details, leading to Cata- Act Based On Intention
strophic Forgetting (Zhai et al., 2023). To model Agents with different END FOR
Update Environment State
characteristics, we divide an Agent’s memory into short-term and long-
Increment time
term memory. Short-term memory, akin to human working memory, END WHILE
consists of real-time environmental information (building layout, fire
location, etc.), personal status (current location and direction of move-
Using memory to simulate human cognition and behavior is an im-
ment of the Agent, etc.), and social dynamics information (behavior of
plicit method. For instance, an LLM can infer that “I am an 8-year-old
surrounding crowd, contact with other Agents, etc.), submitted to the
child” may not independently choose a reasonable exit through im-
LLM in the form of prompts. Considering these inputs continuously feed
plicit reasoning. However, to ensure Agents perform specific actions, we
into the LLM during fire evacuation, past information remains relevant
have incorporated explicit cognitive constraints into them. These con-
to current decisions, necessitating its storage in a time-series format and
straints are formed by texts such as “You remember there is an emer-
submission as prompts to the LLM. Short-term memory primarily pro-
gency exit next to the elevator” and are present in each round of
cesses evacuation environment information, while long-term memory
shapes the Agent’s personality traits, such as individual physiological prompts.
attributes, familiar Froutes in evacuation settings, specific events, and It’s noteworthy that as evacuation time increases, a substantial
preferences. Not all this information is submitted as prompts in every amount of process information is injected into the Prompt, which not
dialogue round with the LLM but is queried actively or loaded into only exceeds the context limitations of LLMs but also makes it chal-
prompts under specific conditions. lenging for LLMs to reason based on a vast amount of text. In fact,
To implement this mechanism, we employ OpenAI’s text- humans adopt strategies of filtering and summarizing when dealing with
embedding-3-small model for text embedding to manage agent long- a large volume of information, allowing more focus on current events. In
term memory storage and retrieval. The workflow proceeds as follows: fire evacuations, evacuation instructions, fire information, and exit in-
Long-term memories are first segmented into fixed-length 512-token formation are the most critical, while the reasons behind each decision
text fragments through a sliding window approach, with consecutive during the evacuation process are secondary. Therefore, we use LLMs to
fragments maintaining a 128-token overlap to preserve contextual compress the historical memory of Agents, ensuring that the prompts
continuity. Each fragment is then encoded into a 1536-dimensional remain concise while retaining key evacuation information, as shown in
vector representation using text-embedding-3-small, subsequently Fig. 2.
stored in the database. Leveraging the model’s proven semantic repre- To optimize context management in prompt engineering, this study
sentation capabilities in high-dimensional spaces, query statements proposes a hierarchical information organization approach that struc-
undergo identical encoding followed by nearest-neighbor search via tures original prompts into three distinct layers: contextual information,
cosine similarity measurement, with a confidence threshold of 0.75. To action information, and instruction information. The action information
address the inherent semantic sparsity yet content relevance among layer incorporates critical data elements including fire dynamics, evac-
segmented sentences, we organize long-term memory into multi-vector uation decision-making, and environmental perception. To mitigate the
memory chunks. When any constituent vector within a chunk demon- performance degradation of LLMs caused by extended context lengths, a
strates sufficient semantic affinity with input sentences, the entire selective compression strategy is implemented, prioritizing retention of
memory chunk is retrieved as contextual prompts for LLMs, as illus- core information such as positional trajectories, environmental state
trated in Fig. 1. changes, decision rationale, and chronological fire progression patterns.
The pseudocode for this process is shown in Algorithm 1. This structured information architecture not only effectively reduces the
risk of memory loss in LLMs during long-context processing but also
Algorithm 1. (Embedding and retrieval of long-term memory)
prevents agent behavioral loops through preserved trajectory data.
Initialize Simulation (Grid, Agents, DecisionInterval Δ t) Continuous monitoring of fire development dynamics further enhances
time =0 decision-making capabilities by providing agents with comprehensive
WHILE simulation_running DO situational awareness, thereby improving the rationality and effective-
IF time MOD Δ t ==0 THEN ness of evacuation strategies.
FOR EACH Agent DO
Furthermore, this study employs a systematic prompt engineering
(continued on next column)
approach in the interaction process based on LLMs. To ensure the
Fig. 1. Design of agent’s long-term and short-term memory.
3

P. Dang et al. S a f e t y S c i e n c e 191 (2025) 106935
Fig. 2. The compression process of prompts.
effectiveness and parsability of the model’s outputs, we have imple-
mented the following core strategies in the design of prompts: 1) Clearly
defining the task objectives and expected output results, guiding the
model to focus on key issues through structured instructions; 2) Strictly
standardizing the output format to JSON data structure, establishing a
standardized response template to enhance the accuracy of computer
program parsing; 3) Introducing the Few-shot learning mechanism,
embedding complete examples in each task prompt to guide the model
to follow the preset reasoning path and output specifications through
demonstrative samples(Schulhoff et al., 2024).
3.2. Characterization of evacuation environments and autonomous
actions
3.2.1. Cell-semantic hybrid modeling for evacuation environments
Agents’ autonomous actions depend on their memory and perception
Fig. 3. Cell semantics and multiplicity of semantics.
of the environment. The method in 3.1 provides Agents with human-like
memory; however, LLMs cannot directly perceive fire evacuation envi-
summarized in three stages: vague perception, preliminary cognition,
ronments, necessitating a representation of the evacuation environment
and full cognition (Man and Vision,1982; Song and Zhao, 2025). In the
to the LLM. Cellular automata, as a mathematical model discrete in both
vague perception stage, humans can only vaguely perceive the existence
time and space, offer precise spatial positioning and layout representa-
and rough shape of an object; in the preliminary cognition stage, they
tion, generating a more accurate descriptive text of the environment.
can recognize basic features of the object, such as color and shape. In the
Furthermore, Agents’ actions during evacuation require a spatiotem-
full cognition stage, humans can clearly understand the object-related
poral framework consistent with the environment, making cellular
information, including texture, expressed information, etc. Similarly,
automata an effective method for environment characterization and
in evacuation scenarios, the distance between an object and an Agent is a
constructing an action framework for Agents.
key factor affecting the Agent’s acquisition of object information. In our
In our study, we describe evacuation environments using a spatial-
research, this process is simplified into Perceptual Threshold Distance
semantic-cellular approach. Fire evacuation scenarios include multiple
and Full Perception Distance. At the Perceptual Threshold Distance, we
environmental objects (such as walls, tables, chairs, etc.), each occu-
input basic shape information about the object to the Agent and use
pying certain spaces. Thus, an environmental object should encompass
terms like “seems” and “looks like” to indicate what it might be. At the
both semantic information and spatial information represented by
Full Perception Distance, we provide the Agent with all information
cellular automata. When characterizing environmental objects using
about the object, including its shape, color, semantics, contained text,
cellular automata and semantics, two considerations are necessary: the
etc. Cellular automata employ a two-dimensional grid representation;
multiplicity of semantics, as cellular automata are a two-dimensional
however, in actual evacuation environments, the height of objects also
structure, but evacuation environments are three-dimensional, inevi-
affects Agents’ perception of the environment. Therefore, we assign
tably leading to a cell having multiple spatial semantics, as shown in
height information to each cell and calculate the occlusion relationships
Fig. 3.
between different cells.
Visibility relationships in evacuation scenarios require consideration
Considering that Agents need to make movement decisions after
of the occlusion relationships, field of view, and inference thresholds
perceiving the environment, we divide the Agent’s field of view into
between objects (cells). Human visual cognition of an object can be
4

P. Dang et al. S a f e t y S c i e n c e 191 (2025) 106935
multiple directions and provide the LLM with prompts corresponding to movement position considers Moore or von Neumann neighborhoods.
those areas. In the decision-making phase, the Agent will decide the We utilize the cellular automaton’s environmental representation to
direction and position to move based on the descriptions of objects seen generate descriptive texts for 8 (or 4) directions, which are then sub-
in different directions, as shown in Fig. 4. mitted to the LLM for next-step action decisions. These textual de-
To calculate the visible cells in a certain direction for an Agent, it’s scriptions are updated after each step. To enable the agent to
necessary to compute the cells within a certain angle and their occlusion comprehend the entire evacuation process, we record each step of its
relationships. We employed three steps: linear interpolation, stepwise decision-making as new prompts submitted to the LLM for reference.
detection, and occlusion detection. Assume the Agent’s cell coordinates Before each agent movement operation, the system integrates two
are A(x,y), and the line-of-sight cell coordinates are B(m,n). The in- critical components into the prompt: (1) the structured textual repre-
crements in the x and y directions are calculated based on Formula 1. sentation of environmental information as described in Section 3.2.1,
and (2) the compressed historical movement data from Section 3.1. This
dx
xincrement =
steps
contextual integration allows the agent to understand its historical de-
# (1) cisions and current status, thereby ensuring consistency in decision-
yincrement =
st
d
e
y
ps
mak
If
i n
e
g
a c
b
h
e h
m
a
o
v
v
io
em
r.
ent of multi-agents (moving to adjacent cells) requires
a perception-decision process, this would generate an excessive number
where dx =m (cid:0) x and dy =n (cid:0) y represent the difference in distance
of LLM dialogues during evacuation simulations, resulting in prohibitive
between the endpoint and the starting point along the x-axis and y-axis, economic and temporal costs. We therefore adopt fixed time steps (t =
respectively. The number of steps is calculated based on the maximum
0.333 s in this study) to replace grid-by-grid movement. Within each
distance difference to ensure continuity of points along the path. The
time step, each agent completes displacement corresponding to its
coordinates of each intermediate point P(i) on the path are then calcu-
movement speed and is assigned to the cell it occupies. The selection of
lated step by step according to the increment formula, as shown in
time step t involves balancing multiple factors: excessively large t values
Formula 2.
reduce the real-time responsiveness of environmental updates and agent
Px (i)=x+i*xincrement#
(2)
i
h
n
e
t
a
e
d
ra
a
c
n
ti
d
o
L
n
L
s,
M
w
d
h
i
i
a
l
l
e
o g
o
u
v
e
e r
f
l
r
y
e q
s
u
m
e
a
n
l
c
l
y
t
.
v
T
a
h
l
e
u e
sp
s
e
i
c
n
i
c
fi
r
c
e a
v
s
a
e
l u
c
e
o
o
m
f
p
t
u
=
ta
0
ti
.3
on
3
a
3
l
s
o
u
v
s
e
e
r
d
-
Py (i)=y+i*yincrement
here was chosen as it approximates the time required for an agent at
typical walking speed (~1.5 m/s) to cross one grid cell (approx. 0.5 m),
Here, i iterates from 0 to steps, representing each step along the straight-
thereby linking the decision update rate to the spatial resolution of the
line path. Finally, each point P(i) on the path is checked to see if it exists
environment. By updating agent states in cellular automata at fixed time
in the set of impassable cells, blockedCells, as shown in Formula 3.
(cid:0) ) intervals, we effectively reduce LLM dialogue requirements while
blocked= Px (i),Py (i) ∈blockedCells# (3) simulating agents’ capacity to formulate new movement strategies
based on environmental changes. This approach preserves the discrete
If any point P(i) is blocked, the line of sight is considered obstructed; nature of cellular automata while maintaining the continuity of indi-
otherwise, the line of sight is unobstructed, as illustrated in Fig. 5. vidual mobility. The pseudocode for this process is shown in Fig. 6.
Furthermore, we added a unified spatial reference for Agents, Furthermore, in traditional cellular automata, objects with spatial
generating direction predicates about other cells based on their current semantics often correspond to a single cell, causing multiple evacuating
position. For example: “You have previously visited [Room 503′s door] individuals to move towards the same cell. This not only exacerbates cell
located to your east, and currently, you can see [a red door] in your competition but also makes the individuals’ movement paths unrealistic.
north direction.” This helps the Agent understand past orientations and Therefore, in our study, an object containing spatial semantics is
the direction of the next move. expressed through multiple cells, any of which can serve as a destination
for the Agent’s movement. To address cell preemption conflicts caused
3.2.2. LLM-agent action framework by simultaneous agent arrivals at target cells (with identical timestamps
The agent’s perception of the environment depends on the cellular within precision), the proposed model employs a randomized allocation
automaton’s representation of that environment, while the agent’s ac- mechanism for conflict resolution: Random numbers are generated to
tions are also executed within the cellular automaton framework. This determine priority, where the selected agent gains exclusive access to
unified framework ensures that the agent’s perception and actions share the target cell while the other agent is dynamically redirected to the
the same spatiotemporal context. Traditionally, an agent’s next nearest available adjacent cell.
Fig. 4. Environment perception based on cellular automata.
5

P. Dang et al. S a f e t y S c i e n c e 191 (2025) 106935
Fig. 5. Calculation of cell occlusion relationship.
Fig. 6. Pseudocode for agent’s action.
3.3. Multi-agent interaction behavior containing agent ID, timestamp, and fire scenario descriptions prepared
for transmission. In this study, this module primarily facilitates fire-
In multi-agent systems for fire evacuation simulations, dynamic in- related information exchange between agents, simulating behavioral
teractions among artificial intelligence agents (Agents) constitute a responses under conditions where agents lack direct visual perception of
critical component for simulating realistic behaviors. These interactions flames and smoke. While these descriptions provide a basis for more
primarily involve spatial positioning, the dynamics of competition and detailed content analysis in the future, the focus of this study is on the
cooperation, and social network structures. These elements collectively occurrence of communication and its impact on the basic transmission of
influence the decision-making processes of agents and significantly fire information.
impact the overall effectiveness of evacuation simulations.
To simulate such interactions, we designed a communication module 4. Experiment and result
for each agent. This module enables agents to record and exchange
critical information at each simulation step, primarily consisting of 4.1. Experiment design
environmental perception data, which is subsequently used for effective
communication with neighboring agents. During each simulation step, 4.1.1. Construction of a three-dimensional experimental scenario
an agent may choose to communicate with nearby agents (within 3.6 m). This study utilized a LiDAR scanner (LiGrip H120) to scan a real
The communication content comprises summarized descriptions of fire scene and constructed a virtual fire evacuation scenario based on point
scenarios retrieved from the agent’s short-term memory, while cloud data and three-dimensional reconstruction results. We selected the
excluding long-term memories, decision-making processes, historical first floor of a shopping mall as the experimental area, covering
movement paths, and other sensitive data. Received response informa- approximately 16,545 square meters. The point cloud data obtained
tion is integrated into the agent’s short-term memory for future decision- from LiDAR scanning were processed using ContextCapture v10.20 for
making. three-dimensional reconstruction, and a cellular automaton of 502*206
To implement this process, we introduced a decision-making mech- cells was constructed based on the reconstruction results. Given the total
anism in the agent’s logic. At each simulation step, agents can choose to scanned area of approximately 16,545 square meters, each cell in this
move toward their target direction, initiate communication with sur- 502x206 grid represents a physical area of roughly 0.4 m x 0.4 m. This
rounding agents, or accept incoming communication requests. Agents defined spatial scale is used consistently throughout the simulation for
receiving communication requests may opt to respond, though doing so translating real-world parameters, such as agent perception distances
requires maintaining a stationary position during that simulation step. and movement speeds, into the cellular automata framework. Finally,
All inter-agent communications follow a standardized JSON format spatial semantics were manually added to the cells based on the
6

P. Dang et al. S a f e t y S c i e n c e 191 (2025) 106935
panoramic video and point cloud data from the 3D laser scanning, System-Prompts, as shown in Table 2.
setting spatial semantic information for 62 objects in the evacuation
environment (such as exits, evacuation signs, etc.), as shown in Fig. 7. 4.1.4. Experimental and control group setup
Currently, many organizations and companies have developed both
4.1.2. Simulation of flames and smoke open-source and proprietary LLMs, which exhibit differences in text
In this study, we used PyroSim 2022 software to simulate the spread comprehension, generation abilities, and generalization capacities.
of flames and smoke under controlled conditions. PyroSim is a graphical Among the factors influencing the performance of LLMs, the number of
interface for the Fire Dynamics Simulator (FDS), capable of detailed model parameters is significant. Therefore, to verify whether our
simulation of flames, smoke, and heat transfer phenomena. The burning research method is universally applicable across different LLMs, we
object was set to fabric, with a heat release rate of 600 kW/m2 per unit selected LLMs of various scales for the experimental group, as shown in
area, and the burning area was set to 5 square meters. Two exits were Table 3.
kept open as ventilation ports, with an area of 3 m x 4 m and an air flow Although some organizations have not disclosed the parameter
rate of 0.5 m/s. Under these conditions, the simulation results of flames counts of their LLMs, based on evaluations and estimates by other re-
and smoke spread from PyroSim were imported into Unity 2021.3.11 for searchers, these models are believed to possess larger parameter counts
visualization and cell description, as shown in Fig. 8. and have thus been adopted in our study.
We categorized visibility into seven levels based on ISO 13571 (ISO, As a comparison, we developed an evacuation program in Unity as
2012), establishing corresponding prompt messages to describe the the control group, where Agents move only towards the nearest exit, and
Agent’s surrounding environment. This refined gradation system en- all Agents’ Response Time is set to 120 s. The movement of Agents in the
ables LLMs to generate differentiated decisions through variations in control group employs the A* algorithm, hence naming the control
descriptive vocabulary, as detailed in Table 1. Objects beyond visibility group as Control Group-A* (CG-A*).
thresholds were not included in environmental prompts, though explicit
notifications were provided in system messages indicating their 4.2. Results
obstruction by smoke. This study enables agents to perceive and respond
to complex environments by converting environmental parameters such 4.2.1. Evacuation duration and paths
as smoke into structured text inputs for the LLM. The method is also In the outcome experiment, we randomly selected a group from each
applicable to other environmental factors, providing an scalable inter- experimental group to present the final evacuation paths of the Agents,
face for building a general decision-making framework. as shown in Fig. 10.
We calculated the path length based on the number of cells each
4.1.3. Evacuees and initial paths Agent passed through in the experiment and summed up the movement
In the evacuation scenario, 10 Agents were set, among which 5 distances for all Agents in each group. After conducting the Shapiro-Wilk
Agents (numbered 1, 3, 5, 6, 9) moved along an initial path at the start of test and Levene’s test on the data from each experimental group, the
the experiment until they autonomously generated their first evacuation results indicated that the data from the four experimental groups
decision. The other Agents remained stationary, waiting to generate generally followed a normal distribution but did not satisfy the homo-
their first autonomous decision, as shown in Fig. 9. Considering Agents geneity of variance test. Therefore, we used the T-test to compare the
move towards semantic cells as their destination, the movement process differences between groups, the significance level is set at 0.05, as
is facilitated by Unity’s Navmesh component, with walking speeds set shown in Table 4.
between 1 m/s and 1.7 m/s, and running speeds between 2.2 m/s and Considering the significant differences in evacuation paths among
4.2 m/s. Agents begin to evacuate under any of the following conditions: Agents due to their diverse background settings in each group,
1. Flames and smoke are within the Agent’s perception rang.2. After comparing the same Agents across different groups yields more mean-
communicating with other Agents and obtaining information about the ingful insights. The results of the T-test comparing Agents across
fire; 3. Upon hearing the alarm, initiate evacuation procedures; the different groups are shown in Fig. 11.
alarm will sound 120 s after a fire breaks out. Moreover, the movement speeds of Agents were variable, affecting
Moreover, basic attribute information and context backgrounds were the overall evacuation duration for each group. We compiled the
added to each Agent. This information was submitted in the form of remaining number of evacuees during the evacuation process for each
group, as illustrated in Fig. 12.
The CG-A* group moved along the shortest path, thus taking the least
actual time. T-tests among the experimental groups revealed no signif-
icant difference between EG-1 and EG-2 (T = (cid:0) 0.306, p = 0.763) or
between EG-3 and EG-4 (T =(cid:0) 0.247, P =0.808). However, significant
differences were found between EG-1 and EG-2 when compared with
EG-3 and EG-4 (P < 0.05), mirroring the variations in evacuation
duration with differences in evacuation path lengths.
4.2.2. Evacuation decisions
During the evacuation process, various factors ultimately influence
the evacuation distance and time, all of which are expressed in LLM’s
responses in each round. Therefore, we analyzed LLM’s decisions in each
round to explore the factors specifically affecting the evacuation out-
comes. We collected statistics on the Agents’ changes in evacuation di-
rection, the number of interactions with other Agents, whether they
sought companions based on background information, and whether they
passed through dangerous areas (cells covered by smoke).
In the evacuation process, we adopted an Agent-centered spatial
orientation, describing the locations of different objects in terms of
cardinal directions. Changes in evacuation direction often imply more
Fig. 7. Construction of evacuation scenario and cell setup. evacuation time. Considering the different initial positions and
7

P. Dang et al. S a f e t y S c i e n c e 191 (2025) 106935
Fig. 8. Spread of smoke.
pass through dangerous areas. We counted the number of times Agent 1
Table 1
in different groups decided to seek its companion (Agent 8) under the
Visibility grading and prompt settings.
known fire occurrence and the number of times all Agents passed
No. Visibility Level Prompt through dangerous areas, as shown in Fig. 14.
Range (m)
In EG-1 and EG-2, Agent 1 decided to seek Agent 8 a total of 5 times
1 =0 Extremely Low The smoke is so dense that visibility is out of 10 tests in EG-1 and EG-2, 3 times in EG-3, and 2 times in EG-4. Of
Visibility completely obstructed, making it these, EG-1 had 4 successful searches for Agent 8, EG-2 had 5, EG-3 had
impossible to discern any objects or
1, and EG-4 had none. During the search, Agent 1 passed through
directions.
2 (0,0.5] Very Low The smoke is very heavy, only allowing dangerous areas, and other instances of passing through dangerous areas
Visibility the sight of objects that are very close, were caused by Agent 4 after starting the evacuation.
with no discernible details of anything Finally, we compiled the communication behaviors among Agents in
further away.
each group. Considering that not all Agents engaged in communication
3 (0.5,1.5] Low Visibility The density of the smoke is high,
significantly limiting visibility, but still with other Agents during the evacuation process, we counted the
permitting the identification of some communication occurrences for each Agent individually, as shown in
nearby objects and outlines.
4 (1.5,2.5] Moderate The density of the smoke is moderate,
Visibility with distant objects starting to blur, but
Table 2
nearby objects can still be seen
Setting of agent background information.
relatively clearly.
5 (2.5,5] Relatively High The smoke is relatively light, enabling No. Name Gender Age Role Social relations
Visibility the sight of more distant objects,
although the vision may still be slightly 1 Alex Male 35 Customer Preparing to go to the clothing
obstructed. store and meet his friend Mike.
6 (5,10] High Visibility While smoke is present, its impact on 2 Sarah Female 44 Food Working alone in the store.
visibility is minimal, hardly hindering store
the normal field of view. employee
7 >10 Extremely High The smoke is almost invisible or does 3 Emily Female 24 Customer Preparing to go to the toy store to
Visibility not affect visibility at all, allowing for a purchase toys.
…
clear view of objects at all distances.
background information of different Agents, we also compared the
Table 3
number of decision changes among the same Agents across different
Information on LLMs in the Experimental Group.
groups, as shown in Fig. 13.
The CG-A* group’s Agents changed their direction of movement the G (E r G o u ¼ p Model Name Organization P (B a i r l a li m on e ) ters O So p u e r n c - e
least during evacuation (M =1.6 ±1.20). In the experimental groups, Experiment
there was no significant difference between EG-1 (M =4.27 ±2.68) and Group)
EG-2 (M =4.43 ±2.74) (T =(cid:0) 0.114, p =0.912), nor between EG-3 and EG-1 ChatGPT 4.0 OpenAI >1750 No
EG-4 (T =(cid:0) 0.492, p = 0.628). For Agent 1, the number of direction EG-2 ERNIE-Bot Baidu >100 No
changes in EG-1 and EG-2 was higher than in EG-3 and EG-4, due to 4.0
Agent 1′s initial information including seeking friends in the mall. This EG-3 Llama-2-70B- Meta 70 Yes
Chat
process resulted in more direction changes in EG-1 and EG-2, while
EG-4 ChatGLM2- THUDM 6 Yes
similar decisions in EG-3 and EG-4 were fewer in number. 6B-32 K
Furthermore, if Agent 1 decided to seek companions, it needed to
Fig. 9. Initial positions and paths of agents.
8

P. Dang et al. S a f e t y S c i e n c e 191 (2025) 106935
Fig. 10. Evacuation paths in part of the experiment.
and 73.46 % (EG-4), while these three Agents contributed only 27.38 %
Table 4
(EG-1) and 16.47 % (EG-2) in other groups. There are differences in
Evacuation distance and time for each group.
communication frequency among the experimental groups and agents,
Group Evacuation Distance (cell) Evacuation Time (s) mainly used to transmit critical environmental information such as fire
EG-ChatGPT4 2829.3 ±224.58a 71.03 ±9.56a notifications. For example, in group EG-3, agent 2 significantly reduced
EG- ERNIE4 3080.4 ±182.27b 75.83 ±7.91a evacuation time after receiving a fire notification.
EG- Llama2 3811.1 ±168.61c 109.16 ±7.17b
EG- ChatGLM2 3745.6 ±114.46c 115.01 ±6.38c
CG-A* 1181.0 ±0.0d 142.28.0 ±0.0d 5. Discussion
5.1. Evacuation efficiency
Fig. 15.
The results showed no difference between EG-1 (M =8.4 ±1.837) For Agents, emphasis is placed on their exploration of and decision-
and EG-2 (M =8.5 ±2.068) (T =(cid:0) 0.114, p =0.910), nor between EG-3 making in the environment, whereas traditional Agent evacuation
(M =6.2 ±1.751) and EG-4 (M =4.9 ±1.523) (T =1.771, p =0.093). models stress the homogeneity and orderliness of individual behaviors.
In EG-1 and EG-2, Agents 1, 3, and 5 frequently decided to communicate Traditional Agent evacuation models, such as the Social Force Model
with other Agents, accounting for 58.33 % (EG-1) and 62.3 % (EG-2) of (Helbing et al., 2000) and Cellular Automata Model (Pelechano &
the total, whereas in other groups, they accounted for 23.43 % (EG-3) Badler, 2006), typically assume that all individuals follow the same
and 14.28 % (EG-4). Conversely, in EG-3 and EG-4, Agents 4, 7, and 8 behavioral rules, such as moving towards exits, avoiding obstacles, and
contributed the most communications, accounting for 65.62 % (EG-3) maintaining distance from others. Although this assumption of
Fig. 11. Comparison of agent evacuation distances.
9

P. Dang et al. S a f e t y S c i e n c e 191 (2025) 106935
strategies in response to real-time conditions, exhibiting enhanced
exploratory and adaptive behaviors. This exploratory behavior leads to
extended navigation time in experimental groups, ultimately reducing
evacuation efficiency. However, such exploration is commonly observed
in fire evacuations, particularly among evacuees unfamiliar with the
environment, who frequently modify their exploration patterns and
wayfinding strategies (Cao et al., 2019). The diverse evacuation paths
exhibited by different LLM-driven agents in this study (as shown in
Fig. 10) also intuitively corroborate this, aligning with the characteris-
tics of spontaneous wayfinding behaviors described in literature when
individuals face uncertainty.
Notably, larger-scale models demonstrate superior wayfinding effi-
ciency, with EG-1 and EG-2 significantly outperforming EG-3 and EG-4
across multiple metrics, while similarly scaled LLMs exhibit comparable
performance. Except for Agent 6 showing significant path variation
Fig. 12. Remaining number of evacuees. between EG-1 and EG-2, other agents maintained similar evacuation
path lengths. This discrepancy arises because Agent 6 followed its initial
route until blocked by building structures and triggered fire alarms,
failing to fully acquire fire outbreak information from other agents (cid:0) a
situation entirely driven by procedural randomness. Crucially, this
randomness differs fundamentally from real-world evacuation behavior
variability: it stems from textual output stochasticity in small-scale
LLMs, contrasting with decision-making randomness observed in
large-scale LLM evacuation simulations.
5.2. Evacuation behaviors
Differences in evacuation behaviors are a significant factor leading to
variations in evacuation outcomes. Except for the control group, which
only considered the shortest path, other groups exhibited complex and
variable behaviors during evacuation. Firstly, whether Agents were
informed of the fire outbreak by other Agents significantly impacted the
overall evacuation time. For example, in EG-3, Agent 2′s evacuation time
Fig. 13. Number of changes in agents’ evacuation decisions. without notification from other Agents was 158.19 ± 10.90 s, while
with notification, it dropped to 82.33 ±36.96 s. Experimental results
homogeneity helps improve the computational efficiency and control- indicate that notifying other Agents about the fire is a random behavior;
lability of the model, it also limits the diversity and adaptability of in- even under the same LLM parameters, Agent behaviors showed vari-
dividual behaviors. In real evacuation processes, individuals often make ability, but larger-scale models reduced this randomness. The coefficient
different decisions based on their own attributes, experiences, and of variation for communication among Agents in the experimental
environmental conditions, and it is this diversity that is key to enhancing groups was calculated as EG-1: 0.208, EG-2: 0.231, EG-3: 0.268, EG-4:
the realism and effectiveness of evacuation. 0.295.
Compared to agent models utilizing deep reinforcement learning Moreover, the background setting of Agents significantly affected
(Hou et al., 2022) or genetic algorithms (Zhai & Feng, 2022), LLM-based their evacuation behaviors. In the prompts, we did not strictly require
evacuation agent models demonstrate superior capabilities in capturing seeking Agent 7 for evacuation, but the decision to find Agent 7 was
the heterogeneity and dynamic nature of individual decision-making, made by Agent 1 in all experimental groups, resembling actual evacu-
while enabling more direct integration of human knowledge for ation scenarios (Dang et al., 2024). However, cases of giving up the
reasoning and decision-making. Through environmental perception and search occurred in EG-3 and EG-4, possibly due to three reasons: firstly,
comprehension, LLM-driven agents dynamically adjust evacuation increasing context in prompts could lead LLM to miss critical
Fig. 14. Times of searching for other agents (a) and Times of passing through smoke cell (b).
10

P. Dang et al. S a f e t y S c i e n c e 191 (2025) 106935
Fig. 15. Times of group communication (a) and Times of individual agent communication (b).
information due to difficulty in capturing focus. Secondly, abandoning environmental information, even large-scale LLMs may generate un-
previous decisions could lead Agents to give up searching for compan- certain judgments. Implicit reasoning capability directly influences
ions midway. Lastly, reaching Agent 7′s location required Agent 1 to pass model generalization performance, serving as a necessary but insuffi-
through dangerous areas, and in some tests, Agent 1 chose to find the cient condition for LLMs to simulate realistic human behaviors. All
nearest exit after weighing the options. Changes in decisions not only experimental LLMs autonomously developed fire notification behaviors
occurred while seeking companions but also in searching for exits, often (not explicitly required in prompts), with large-scale models (EG-1/EG-
when Agents continued exploration in a direction without finding the 2) demonstrating more proactive responses, particularly in actively
desired target. This behavior aligns closely with the classic ’affiliative approaching stationary agents for warnings. This behavior stems from
behavior’ phenomenon in evacuation behavior studies, where in- implicit reasoning that “stationary status may indicate undetected fire
dividuals in crisis situations tend to seek out and evacuate with relatives hazards.” However, such reasoning might be influenced by ethical biases
or friends rather than solely pursuing the quickest personal escape route, in training data, potentially causing over-reliance on idealized social
as discussed in studies such as Fischer et al. (1995). norms.
Frequent changes in decisions led to increased evacuation times. We Therefore, while larger-parameter models demonstrate superior
calculated the Pearson correlation coefficient between the number of performance in critical decision-making and behavioral simulation,
decision changes and evacuation distance: EG-1: 0.820, EG-2: 0.604; EG- their limitations in processing dynamic information and overcoming
3: 0.485, EG-4: 0.571. However, changes in decisions did not necessarily training biases remain significant concerns. These factors could sub-
imply more efficient exploration, as some tests found Agents wandering stantially impact model effectiveness in practical evacuation scenarios
between multiple objectives. We assessed the effectiveness of decision (Fischer et al., 1995; Efferson et al., 2024).
changes in each group using the ratio of evacuation distance to the The human-like characteristics demonstrated by LLMs in implicit
number of decision changes, finding EG-1: 66.61 ±4.54, EG-2: 70.60 ± reasoning tasks stem from their ability to capture and learn from human
6.35, EG-3: 51.07 ± 2.47, EG-4: 43.49 ± 2.29. EG-2 performed best, knowledge and behavioral patterns in the training data. Nevertheless,
with each decision change covering approximately 70 cells, whereas EG- due to the potential introduction of specific ethical and moral biases by
4 had the most changes but the least effectiveness. Notably, in real different developers during the training process, the specific perfor-
evacuation scenarios, changes in decisions relate to environmental mance of each LLM may vary. Overall, the formation of LLMs’ human-
changes (Zheng et al., 2017), but in this study, evacuation decision like reasoning capabilities relies on the coverage of human knowledge
changes were linked to LLM’s memory and reasoning capabilities. in the training data and the guidance of developers’ value orientations,
which are also important premises for their application in agent
behavior simulation.
5.3. Reasoning-based evacuation decision
6. Conclusion and future work
The core characteristic of LLM-driven agent evacuation models lies
in their autonomous reasoning capabilities based on real-time infor- This study introduced a multi-Agent fire evacuation model based on
mation, rather than reliance on predefined rules. At the individual level, LLM, endowing Agents with personalized memory, cognition, and
agents exhibit behavioral diversity in evacuation scenarios (cid:0) even with decision-making capabilities through LLM. By characterizing the evac-
identical parameters, different agents display behavioral variations. uation environment through a combination of spatial semantics and
However, at the group level, behavioral patterns stabilize under the cellular automata, Agents can perceive, decide, and move within a
constraints of a unified perception–action framework, explaining the unified spatiotemporal framework. Experimental results demonstrated
approximate distribution patterns of communication frequencies across that this framework enables LLM-Agents to complete fire evacuation
experimental groups. tasks, exhibiting exploratory and adaptive behaviors consistent with real
Experimental findings reveal that individual decision variations scenarios. Additionally, LLMs of different scales exhibited variations in
under identical parameters originate from LLMs’ implicit reasoning the diversity and randomness of Agent behaviors, with larger-scale LLMs
capabilities, though these capabilities demonstrate significant limita- generating more consistent and efficient evacuation strategies.
tions: In explicit reasoning scenarios (e.g., “exit located west” prompts), This study has several limitations that indicate clear directions for
EG-3/EG-4 group agents still exhibit non-westerly movement choices future research. First, although the model incorporates heterogeneous
(with occurrence frequencies significantly higher than EG-1/EG-2 agent attributes, it emphasizes collective evacuation behaviors under
groups). This suggests smaller-scale LLMs may fail to accurately parse multi-factor coupling, with less focus on the independent impact of in-
critical information (Wei et al., 2022), leading to more invalid/erro- dividual variables (e.g., age, social role). Future work should prioritize
neous decisions. When confronted with ambiguous or incomplete
11

P. Dang et al. S a f e t y S c i e n c e 191 (2025) 106935
integrating more diverse agent populations—considering differences in Dang, P., Zhu, J., Li, W., Lai, J., 2024b. A large language model-based agent for
age, mobility, social responsibilities (e.g., staff, caregivers), and envi- wayfinding: simulation of spatial perception and memory. Cartogr. Geogr. Inf. Sci.
1–20. https://doi.org/10.1080/15230406.2024.2405596.
ronmental familiarity—to improve the ecological validity and capture Dang, P., Zhu, J., Pirasteh, S., Li, W., You, J., Xu, B., Liang, C., 2021. A chain navigation
nuanced evacuation dynamics in real-world public settings. Moreover, grid based on cellular automata for large-scale crowd evacuation in virtual reality.
the lack of quantitative validation against real-world data limits Int. J. Appl. Earth Obs. Geoinf. 103, 102507. https://doi.org/10.1016/j.
jag.2021.102507.
behavioral fidelity to qualitative assessments. Second, the small agent
Dang, P., Zhu, J., Qiao, X., Wu, J., Li, W., You, J., Fu, L., 2023. How does spatial
population (N =10) and limited simulation repetitions—constrained by cognitive style affect indoor fire evacuation wayfinding in mobile virtual reality?
the high computational cost of LLM-driven approaches—limit statistical Cartogr. Geogr. Inf. Sci. 50 (3), 272–288. https://doi.org/10.1080/
15230406.2023.2176928.
robustness and generalizability. Third, the model uses simplified evac-
Durmus, D., Giretti, A., Ashkenazi, O., Carbonari, A., Isaac, S., 2024. The role of large
uation triggers and does not explicitly differentiate cognitive and language models for decision support in fire safety planning. Proceedings Of The...
behavioral phases within pre-movement time (e.g., detection, recogni- ISARC 339–346. https://hdl.handle.net/11566/333102.
Efferson, C., Bernhard, H., Fischbacher, U., Fehr, E., 2024. Super-additive cooperation.
tion), which may affect the accuracy of delay modeling. Lastly, the
Nature 1–8. https://doi.org/10.1038/s41586-024-07077-w.
decision-making logic of LLM-based agents lacks interpretability; Fischer, H.W., Stine, G.F., Stoker, B.L., Trowbridge, M.L., Drain, E.M., 1995. Evacuation
developing tools for traceability and visualization is essential to enhance behaviour: why do some evacuate, while others do not? Acase study of the Ephrata,
Pennsylvania (USA) evacuation. Disaster Prevention and Management: an
transparency and trust. Addressing these issues will be key to advancing
International Journal 4 (4), 30–36.
LLM-based evacuation modeling toward reliable real-world applications Gilbert, N., Terna, P., 2000. How to build and use agent-based models in social science.
in urban resilience. Mind & Society 1, 57–72. https://doi.org/10.1007/BF02512229.
Data and codes availability statement: The data and codes that Gilson, A., Safranek, C., Huang, T., Socrates, V., Chi, L., Taylor, R., Chartash, D., 2023.
How does ChatGPT perform on the United States medical licensing examination? the
support the findings of this study are available in figshare.comwith the implications of large language models for medical education and knowledge
identifier https://figshare.com/s/333e166317fa3a6afd90. assessment. JMIR Med. Educ. 9. https://doi.org/10.2196/45312.
Helbing, D., Molnar, P., 1995. Social force model for pedestrian dynamics. Phys. Rev. E
51 (5), 4282. https://doi.org/10.1103/PhysRevE.51.4282.
CRediT authorship contribution statement Helbing, D., Farkas, I., Vicsek, T., 2000. Simulating dynamical features of escape panic.
Nature 407 (6803), 487–490. https://doi.org/10.1038/35035023.
Pei Dang: Methodology, Software, Writing – original draft. Jun Zhu: Hou, H., Wang, L., 2022. Measuring dynamics in evacuation behaviour with deep
learning. Entropy 24 (2), 198. https://doi.org/10.1080/13658816.2024.2306167
Data curation, Supervision. Weilian Li: Validation, Data curation. https://doi.org/10.48550/arXiv.2309.10313.
Yakun Xie: Resources, Software. Heng Zhang: Funding acquisition, Hughes, R.L., 2002. A continuum theory for the flow of pedestrians. Transp. Res. B
Validation. Methodol. 36 (6), 507–535. https://doi.org/10.1016/S0191-2615(01)00015-7.
International Organization for Standardization, 2012. ISO 13571:2012: Life-threatening
components of fire — guidelines for the estimation of time to compromised
tenability in fires. International Organization for Standardization, Geneva https://
Declaration of competing interest www.iso.org/standard/56172.html.
Jennings, N.R., Wooldridge, M., 1998. Applications of intelligent agents. Agent
The authors declare that they have no known competing financial technology: foundations, applications, and markets, pp.3-28. https://doi.org/
10.1007/978-3-662-03678-5_1.
interests or personal relationships that could have appeared to influence
Kaur, N., Kaur, H., 2022. A multi-agent based evacuation planning for disaster
the work reported in this paper. Jun Zhu reports financial support was management: a narrative review. Arch. Comput. Meth. Eng. 29 (6), 4085–4113.
provided by Southwest Jiaotong University. https://doi.org/10.1007/s11831-022-09729-4.
Lee, Y., Malkawi, A., 2013. Simulating human behavior: an agent-based modeling
approach. Building Simulation Conference Proceedings. https://doi.org/10.26868/
25222708.2013.2464.
Acknowledgements
Legg, S., Hutter, M., 2007. A collection of definitions of intelligence. Frontiers Artificial
Intelligence Appl. 157, 17. https://doi.org/10.48550/arXiv.0706.3639.
This research was funded by the National Natural Science Founda- Li, X., Zhou, J., Chen, F., Zhang, Z., 2018. Cluster risk of walking scenarios based on
macroscopic flow model and crowding force analysis. Sustainability 10 (2), 385.
tion of China [Grant Nos. 42271424, 42171397, 42201445], the Open
https://doi.org/10.3390/su10020385.
Project Fund of National Key Laboratory of Intelligent Parallel Tech- Lovreglio, R., Ronchi, E., Nilsson, D., 2016. An Evacuation Decision Model based on
nology [SHJJ2024013], the Open Project Fund of National Engineering perceived risk, social influence and behavioural uncertainty. Simul. Model. Pract.
Theory 66, 226–242. https://doi.org/10.1016/j.simpat.2016.03.006.
Research Center of Digital Construction and Evaluation Technology of
Luo, G., Weng, L., Li, Y., Sun, Y., Hong, Y., Wu, Y., Luo, R., Wang, L., Wang, C., Chen, L.,
Urban Rail Transit [No. 2024sys015], and the Natural Science Foun- 2025. FireExpert: fire event identification and assessment leveraging cross-domain
dation of Tianjin [No. 23JCQNJC01130]. knowledge and large language model. IEEE Trans. Mob. Comput. https://doi.org/
10.1109/TMC.2025.3528413.
Man, D., Vision, A., 1982. Vision: a computational investigation into the human
Data availability representation and processing of visual information. WH San Francisco: Freeman
and Company, San Francisco 1, 1. https://doi.org/10.7551/mitpress/
Data will be made available on request. 9780262514620.001.0001.
Minsky, M., 1961. Steps toward artificial intelligence. Proc. IRE 49 (1), 8–30. https://doi.
org/10.1109/JRPROC.1961.287775.
References Moussaïd, M., Perozo, N., Garnier, S., Helbing, D., Theraulaz, G., 2010. The walking
behaviour of pedestrian social groups and its impact on crowd dynamics. PLoS One 5
(4), e10047. https://doi.org/10.1371/journal.pone.0010047.
Cao, L., Lin, J., Li, N., 2019. A virtual reality based study of indoor fire evacuation after
Neto, J., Morais, A., Gonçalves, R., Coelho, A., 2019. A multi-agent system for
active or passive spatial exploration. Comput. Hum. Behav. 90, 37–45. https://doi.
recommending fire evacuation routes in buildings, based on context and IoT,
org/10.1016/j.chb.2018.08.041. 10.1007/978-3-030-24299-2_34. Springer, Cham, pp. 343–347.
Chen, J., Shi, T., Li, N., 2021. Pedestrian evacuation simulation in indoor emergency
Pan, X., Han, C.S., Dauber, K., Law, K.H., 2007. A multi-agent based framework for the
situations: Approaches, models and tools. Saf. Sci. 142, 105378. https://doi.org/ simulation of human and social behaviors during emergency evacuations. AI & Soc.
10.1016/j.ssci.2021.105378. 22, 113–132. https://doi.org/10.1007/s00146-007-0126-1.
Chen, X., Meaker, J.W., Zhan, F.B., 2006. Agent-based modeling and analysis of
hurricane evacuation procedures for the Florida Keys. Nat. Hazards 38, 321–338. Pelec b h u a il n d o in , g N . e , v B a a c d u l a e t r i , o n N . . I I . E , E 2 E 0 0 C 6 o . m M p o u d t. e l G in ra g p c h r . o A w p d p a l. n 2 d 6 t r ( a 6 i ) n , e 8 d 0 l – e 8 a 6 d . e h r t b tp e s h : a / v / i d o o r i . d o u rg ri / n g
https://doi.org/10.1007/s11069-005-0263-0.
10.1109/MCG.2006.133.
Chen, Y., Xue, Y., 2015, October. A deep learning approach to human activity
Ronchi, E., Gwynne, S.M., Rein, G., Intini, P., Wadhwani, R., 2019. An open multi-
recognition based on single accelerometer. In 2015 IEEE international conference on
physics framework for modelling wildland-urban interface fire evacuations. Saf. Sci.
systems, man, and cybernetics (pp. 1488-1492). IEEE. DOI: 10.1109/SMC.2015.263. 118, 868–880. https://doi.org/10.1016/j.ssci.2019.06.009.
Colombo, R.M., Rosini, M.D., 2005. Pedestrian flows and non-classical shocks. Math. Ronchi, E., Nilsson, D., Koji´c, S., Eriksson, J., Lovreglio, R., Modig, H., Walter, A.L., 2016.
Methods Appl. Sci. 28 (13), 1553–1567. https://doi.org/10.1002/mma.624.
A virtual reality experiment on flashing lights at emergency exit portals for road
Dang, P., Zhu, J., Cao, Y., Wu, J., Li, W., Hu, Y., You, J., Fu, L., 2024a. A method for tunnel evacuation. Fire Technol. 52, 623–647. https://doi.org/10.1007/s10694-
multi-person mobile virtual reality fire evacuation drills based on pose estimation:
015-0462-5.
consistency of vision and perception. Saf. Sci. 170, 106334. https://doi.org/
10.1016/j.ssci.2023.106334.
12

P. Dang et al. S a f e t y S c i e n c e 191 (2025) 106935
Sahin, C., Rokne, J., Alhajj, R., 2019. Human behavior modeling for simulating Bushfire Evacuations. In Australasian Database Conference (pp. 17-29). Springer,
evacuation of buildings during emergencies. Phys. A. https://doi.org/10.1016/J. Singapore. https://doi.org/10.1007/978-981-96-1242-0_2.
PHYSA.2019.121432. Wu, T., He, S., Liu, J., Sun, S., Liu, K., Han, Q.L., Tang, Y., 2023. A brief overview of
Schulhoff, S., Ilie, M., Balepur, N., Kahadze, K., Liu, A., Si, C., Li, Y., Gupta, A., Han, H., ChatGPT: the history, status quo and potential future development. IEEE/CAA J.
Schulhoff, S. and Dulepet, P.S., 2024. The Prompt Report: A Systematic Survey of Autom. Sin. 10 (5), 1122–1136. https://doi.org/10.1109/JAS.2023.123618.
Prompting Techniques. arXiv preprint arXiv:2406.06608. https://doi.org/10.48550/ Yoo, S.J., Lee, S., 2023. December. Large Language Models Show Human-Like Abstract
arXiv.2406.06608. Thinking Patterns: A Construal-Level Perspective. In Proceedings of the Annual
Sharma, S., Ogunlana, K., Scribner, D., Grynovicki, J., 2018. Modeling human behavior Meeting of the Cognitive Science Society (Vol. 46). https://escholarship.org/uc/
during emergency evacuation using intelligent agents: a multi-agent simulation item/3f28f61v.
approach. Inf. Syst. Front. 20, 741–757. https://doi.org/10.1007/s10796-017-9791- Zhai, L., Feng, S., 2022. A novel evacuation path planning method based on improved
x. genetic algorithm. J. Intell. Fuzzy Syst. 42 (3), 1813–1823. https://doi.org/10.3233/
Shi, J., Ren, A., Chen, C., 2009. Agent-based evacuation model of large public buildings JIFS-211214.
under fire conditions. Autom. Constr. 18 (3), 338–347. https://doi.org/10.1016/J. Zhai, Y., Tong, S., Li, X., Cai, M., Qu, Q., Lee, Y.J., Ma, Y., 2023. Investigating the
AUTCON.2008.09.009. catastrophic forgetting in multimodal large language models. arXiv preprint arXiv:
Song, Y., Zhao, L., 2025. Modeling and simulation of risk-information processing in 2309.10313.
decision-making during pedestrian seismic evacuation. J. Build. Perform. Simul. Zhang, J., Shen, W., 2019. Research on personnel emergency evacuation model based on
1–20. https://doi.org/10.1080/19401493.2025.2454258. multi-agent. Destech Transactions on Computer Science and Engineering. https://
Tampuu, A., Matiisen, T., Kodelja, D., Kuzovkin, I., Korjus, K., Aru, J., Aru, J., doi.org/10.12783/dtcse/cisnrc2019/33341.
Vicente, R., 2015. Multiagent cooperation and competition with deep reinforcement Zhao, X., Lovreglio, R., Nilsson, D., 2020. Modelling and interpreting pre-evacuation
learning. PLoS One 12. https://doi.org/10.1371/journal.pone.0172395. decision-making using machine learning. Autom. Constr. 113, 103140. https://doi.
Tissera, P.C., Printista, A.M., Luque, E., 2012. A hybrid simulation model to test org/10.1016/j.autcon.2020.103140.
behaviour designs in an emergency evacuation. Procedia Comput. Sci. 9, 266–275. Zheng, X., Zhong, T., Liu, M., 2009. Modeling crowd evacuation of a building based on
https://doi.org/10.1016/j.procs.2012.04.028. seven methodological approaches. Build. Environ. 44 (3), 437–445. https://doi.org/
Turing, A.M., 2009. Computing machinery and intelligence. In Parsing the turing test, 10.1016/j.buildenv.2008.04.002.
10.1093/oso/9780198250791.003.0017. Springer, Dordrecht, pp. 23–65. Zhu, J., Dang, P., Cao, Y., Lai, J., Guo, Y., Wang, P., Li, W., 2024a. A flood knowledge-
Uchiya, T., Sugie, R., Takumi, I., 2019. October. Evaluation of evacuation guidance by constrained large language model interactable with GIS: enhancing public risk
robots using multi-agent simulation. In: In 2019 IEEE 8th Global Conference on perception of floods. Int. J. Geogr. Inf. Sci. 1–23. https://doi.org/10.1080/
Consumer Electronics (GCCE), IEEE, pp. 1034–1035. https://doi.org/10.1109/ 13658816.2024.2306167.
GCCE46687.2019.9015493. Zhu, J., Dang, P., Zhang, J., Cao, Y., Wu, J., Li, W., Hu, Y., You, J., 2024b. The impact of
Webb, T., Holyoak, K.J., Lu, H., 2023. Emergent analogical reasoning in large language spatial scale on layout learning and individual evacuation behavior in indoor fires:
models. Nat. Hum. Behav. 7 (9), 1526–1541. https://doi.org/10.1038/s41562-023- single-scale learning perspectives. Int. J. Geogr. Inf. Sci. 38 (1), 77–99. https://doi.
01659-w. org/10.1080/13658816.2023.2271956.
Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., Le, Q.V., Zhou, D., 2022. Zhu, R., Becerik-Gerber, B., Lin, J., Li, N., 2023. Behavioral, data-driven, agent-based
Chain-of-thought prompting elicits reasoning in large language models. Adv. Neural evacuation simulation for building safety design using machine learning and discrete
Inf. Proces. Syst. 35, 24824–24837. choice models. Adv. Eng. Inf. 55, 101827. https://doi.org/10.1016/j.
Wu, J., Zhou, X., Kuligowski, E. and Zhang, Y., 2025. Queries Optimised LLM- aei.2022.101827.
Empowered Active Learning for Social Media Analysis of Human Behaviour in
13
