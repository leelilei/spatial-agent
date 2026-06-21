---
title: "Introduction"
source_pdf: "02_citysim_agents\\05_ChatSUMO_Mao2024.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-06-21T17:32:12+00:00
page_count: 10
status: ok
text_char_count: 43869
quality_flags: []
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\02_citysim_agents\05_ChatSUMO_Mao2024.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-06-21T17:32:12+00:00
- Page count: 10
- Status: ok
- Text chars: 43869
- Quality flags: none

## Metadata

- Title: Introduction
- Author: unknown
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

—Large Language Models (LLMs), capable of han- Despite its effectiveness, creating traffic simulation scedling multi-modal input and outputs such as text, voice, images, narios is a time-consuming process that requires specialized and video, are transforming the way we process information. traffic-related knowledge [7]. Most mainstream simulation Beyond just generating textual responses to prompts, they can software demands that users define networks, vehicles, routes, integrate with different software platforms to offer comprehensive solutions across diverse applications. In this paper, we and other parameters, which poses a significant barrier to present ChatSUMO, a LLM-based agent that integrates language entry for beginners who lack professional expertise or even for 4202 gu pprreosceensstiCnghastkSiUllsMtOo ,gaenLeLraMte-baabssetdraacgtenatndtharetainl-twegorraldtessimlanuglautaiogne scenarios in the widely-used traffic simulator - Simulation o Urban MObility (SUMO). Our methodology begins by leveraging the LLM for user input which converts to relevant keywords needed to run python scripts. These scripts are designed to convert specified regions into coordinates, fetch data from Open StreetMap, transform it into a road network, and subsequently run SUMO simulations with the designated traffic conditions The outputs of the simulations are then interpreted by the LLM resulting in informative comparisons and summaries. Users can continue the interaction and generate a variety of customized scenarios without prior traffic simulation expertise. For simula tion generation, we created a real-world simulation for the city of Albany with an accuracy of 96%. ChatSUMO also realizes the customizing of edge edit, traffic light optimization, and vehicle edit by users effectively.

## Outline

- Introduction (page 1)
- Literature Review (page 2)
- Methodology (page 3)
  - Overview (page 3)
  - GPT-reasoning (page 3)
- Experimental Results (page 5)
  - Setup (page 5)
  - Simulation Generation (page 5)
  - Edge Modification (page 5)
  - Traffic Light Optimization (page 6)
  - Vehicle Edits (page 7)
  - Discussion and Potential Application (page 8)
- Conclusion and Future Work (page 9)
- References (page 9)

## Markdown Content

IEEE JOURNAL 1
ChatSUMO: Large Language Model for
Automating Traffic Scenario Generation in
Simulation of Urban MObility
Shuyang Li, Talha Azfar, and Ruimin Ke, Member, IEEE
Abstract—Large Language Models (LLMs), capable of han- Despite its effectiveness, creating traffic simulation scedling multi-modal input and outputs such as text, voice, images, narios is a time-consuming process that requires specialized
and video, are transforming the way we process information.
traffic-related knowledge [7]. Most mainstream simulation
Beyond just generating textual responses to prompts, they can
software demands that users define networks, vehicles, routes,
integrate with different software platforms to offer comprehensive solutions across diverse applications. In this paper, we and other parameters, which poses a significant barrier to
present ChatSUMO, a LLM-based agent that integrates language entry for beginners who lack professional expertise or even for
4202
gu

pprreosceensstiCnghastkSiUllsMtOo ,gaenLeLraMte-baabssetdraacgtenatndtharetainl-twegorraldtessimlanuglautaiogne
scenarios in the widely-used traffic simulator - Simulation o
Urban MObility (SUMO). Our methodology begins by leveraging
the LLM for user input which converts to relevant keywords
needed to run python scripts. These scripts are designed to
convert specified regions into coordinates, fetch data from Open
StreetMap, transform it into a road network, and subsequently
run SUMO simulations with the designated traffic conditions
The outputs of the simulations are then interpreted by the LLM
resulting in informative comparisons and summaries. Users can
continue the interaction and generate a variety of customized
scenarios without prior traffic simulation expertise. For simula
tion generation, we created a real-world simulation for the city
of Albany with an accuracy of 96%. ChatSUMO also realizes the
customizing of edge edit, traffic light optimization, and vehicle
edit by users effectively.
Index Terms—Traffic simulation, Large Language Model, Sim
ulation scenario generation, Simulation automation, SUMO
I. INTRODUCTION
T HE increasing complexity of modern transportation systems, with diverse vehicle types and traffic patterns, poses
significant challenges for traffic management and forecasting [1], [2]. This complexity not only escalates transportation
costs but also contributes to environmental pollution. The
need for improved traffic planning and operation has led to a
surge in studies focused on optimizing transportation systems
e.g., the strategic reconstruction of road infrastructure [3], [4]
Traffic simulation has emerged as a powerful tool for modeling
current traffic scenarios, predicting future conditions, and mitigating negative impacts, all while reducing the costs associated
with real-world traffic planning implementations [5]. Among
these tools, SUMO (Simulation of Urban MObility) stands
out as a versatile, open-source platform for traffic simulation
used widely for urban mobility research, operations, and
planning [6].
S. Li was with the Department of Civil and Environmental Engineering
University of Michigan, Ann Arbor, MI, 48109.
Talha Azfar and Ruimin Ke (e-mail: ker@rpi.edu) are with the Departmen
of Civil and Environmental Engineering, Rensselaer Polytechnic Institute
Troy, NY, 12180.
Manuscript received xxx, 2024; revised xxx.
uA
92
]CH.sc[
1v04090.9042:viXra

entry for beginners who lack professional expertise or even for
experts but without the experience in the certain software [8],
[9]. These users often seek quick access to modeling results
without the need for extensive setup and configuration.
The advent of Large Language Models (LLMs), trained
on vast datasets, offers a promising solution by facilitating a
more intuitive human-machine interaction. LLMs can interpret
a wide range of inputs, including text, images, and videos,
and generate corresponding outputs [10]. SUMO, a popular
open-source traffic simulation software, requires users to either
code networks from scratch or convert them from other
platforms [11]. Additionally, users must manually define traffic
flows or run Python scripts with specific parameters, adding
o the software’s learning curve [12].
To address these challenges, we present ChatSUMO, a
cutting-edge LLM-based assistant designed to streamline
he use of SUMO simulations. Powered by the Llama 3.1
model [13], [14], ChatSUMO enables users to generate and
modify traffic simulation scenarios through simple textual
nputs. This framework transforms user descriptions into executable SUMO simulations using Python scripts, effectively
owering the barrier for those without specialized knowledge.
ChatSUMO operates by leveraging a multi-module architecure to facilitate user interaction and simulation generation.
The system begins with an Input Module, which processes user
nputs and converts them into relevant keywords. These keywords are then used by the Simulation Generation Module to
create either abstract or real-world traffic scenarios in SUMO.
Users can customize these scenarios using the Customization
Module, which supports a range of modifications, including
edge and lane edits, traffic light optimization, and vehicle route
adjustments. The Analysis Module interprets the simulation
outputs, providing detailed reports on traffic density, travel
ime, emissions, and more. The contributions are summarized
as follows:
• We propose a novel LLM-based agent capable of transforming textual descriptions into SUMO simulation scenarios. This allows users to bypass the need for extensive
traffic simulation knowledge.
• ChatSUMO streamlines the process of generating and
modifying simulations, making it accessible to users of

IEEE JOURNAL
all expertise levels.
• By leveraging advanced language processing capabilities
ChatSUMO provides an intuitive interface for traffic
simulation, offering real-time insights and dynamic adjustments.
The rest of the paper is structured as follows: we first review
related literature on traffic simulation and the application
of LLMs in this domain. We then detail the methodology
behind ChatSUMO’s design and functionality, followed by
an experimental evaluation of its performance in generating
and modifying traffic simulations. Finally, we discuss potentia
applications and conclude with future work directions aimed
at enhancing the system’s capabilities.
II. LITERATURE REVIEW
LLM research is focused on enhancing natural language
processing objectives including text classification, language
inference, and semantic understanding. While they face challenges in reasoning, ethics, and conflict resolution, they have
proven to be excellent tools for summarization, contextua
comprehension, and question answering [10]. Modern LLMs
have undergone training on vast quantities of data and their
behavior has been fine tuned by human feedback, such tha
the most competitive models are very good at following
instructions and remaining focused towards specified tasks
[15]. LLMs show promise in the enhancement of education
where precise answers or subject matter experts may not be
easily accessible [16].
In the transportation field some LLM related work has
emerged recently, focusing primarily on safety. TrafficSafetyGPT [17] finetuned Llama on a custom dataset curated from
NSTHA Model Minimum Uniform Crash Criteria guidelines
FHWA Highway Safety Manual, and ChatGPT generated data
The model learned domain specific concepts allowing it to
accurately answer challenging transportation safety questions
with concise answers. ChatScene [18] was developed to generate safety-critical scenarios for autonomous vehicles as tex
descriptions which are then broken down into sub-descriptions
that can be used to instantiate the scenario in CARLA. A
database of scene components and descriptions was created
that enabled ChatScene to assemble scene scripts from LLM
output. AccidentGPT [19] combines scene perception and
trajectory prediction using computer vision on camera views
from multiple vehicles and roadside units for environmenta
understanding and collision avoidance. GPT4 based reasoning
module is then used to provide proactive cues for human
drivers and traffic management authorities. It also stores key
moments and uses it for later analysis to improve future
autonomous driving decisions. Traffic Performance GPT (TPGPT) proposes an intelligent chatbot designed to aid in transportation analytics. The TP-GPT utilizes LLMs to generate
accurate SQL queries and interpret traffic data, leveraging a
real-time database of traffic information [20].
Language models have been used in combination with computer vision for scene understanding for autonomous driving
in a variety of techniques [21]. ADAPT (Action-aware Driving
cAPtion Transformer) [22] provides an innovative end-to-end

2
ransformer-based approach for generating action narration and
reasoning in self-driving vehicles. ADAPT employs multiask joint training to bridge the gap between driving action
captioning and control signal prediction. ChatGPT was used
as a co-pilot for assisted driving in [23] by converting vehicle
elemetry, road state, human intention, and descriptions of the
available controllers into a combined prompt. The response
from the LLM determines the course of action most appropriate for those conditions. The system can switch between
aggressive and gentle controllers, and handle lane changes and
overtaking. The DiLu framework [24] incorporates GPT based
reasoning and reflection modules to perform decision making
for an autonomous vehicle and has the ability to learn continuously. The system is able to use LLM common sense chain of
hought reasoning from prompts tailored to the scenario which
generates the final decision. Meanwhile the decision sequences
stored to memory can be reflected upon by the LLM to find
mistakes and correct them. Similarly, LanguageMPC [25] used
an LLM for high level autonomous driving decision making,
converting text descriptions to mathematical representations
o be used by the model predictive controller. It was able
o handle multi-vehicle coordinated control by generating a
convoy level decision that each vehicle interprets according to
ts internal state. BEVGPT is a generative pre-trained model
hat integrates driving scenario prediction, decision-making,
and motion planning into a minimalist autonomous driving
framework using only bird’s-eye-view images, outperforming
previous methods in key metrics and pioneering long-term
BEV image generation for autonomous driving [26].
Microscopic traffic simulations such as VISSIM, SUMO,
and MATSim are the basis of planning and optimization
studies for traffic networks [27] and a few recent works have
ncorporated LLMs with microsimulation tools. PromptGAT
[28] leverages LLM inference to understand how weather conditions, traffic states, and road types influence traffic dynamics,
which is used to inform policy in reinforcement learning for
raffic signal control. This additional information about realworld conditions helps to reduce the simulation to reality gap.
In a similar vein, language assisted traffic light control in
[23] employ LLM to understand the traffic observations and
recommended action from reinforcement learning, which then
generates a justification for the action using chain of thought
reasoning. Anomalous traffic conditions like blockages, and
he presence of emergency vehicles are some of the factors the
LLM takes into consideration before selecting the appropriate
action. In [29], natural language queries are translated into
differentiable loss functions for specified vehicle trajectories
n order to facilitate scenario based traffic simulations. These
scenarios include car following and collision trajectories for a
few vehicles and compare them to ground truth from nuScenes
dataset. There have also been advances in using LLM for
microscopic traffic behavior modeling, such as in [30], Chen
et al. proposes a LLM-based method for car following behavior modeling; however, they do not necessarily include
microscopic traffic simulations.

IEEE JOURNAL
Fig. 1: ChatS
III. METHODOLOGY
A. Overview
The overview of ChatSUMO, as Figure 1, presents a
structure of the proposed system. The framework is designed
to assist traffic simulation generation. ChatSUMO integrates
advanced chat model capabilities into the SUMO platform
to enhance the efficiency and accuracy of traffic simulation
and management. This integration leverages the power of the
GPT model to simulate, modify, and analyze traffic scenarios
providing real-time insights and dynamic adjustments. Our
methodology begins by leveraging the LLM for user inpu
which converts to relevant keywords needed to run python
scripts. These scripts are designed to create an abstract network
or convert specified regions into coordinates, fetch data from
OpenStreetMap, transform it into a road network, and subsequently run in SUMO simulation with the designated traffic
conditions. We use Llama 3 8B, an open-source model, to
parse the inputs and provide a summary of the output. The user
can then request another simulation with some modifications
which create a different traffic condition. The LLM retains
context for continued interaction. The core component of this
methodology is the gpt-reasoning module, which is responsible for three critical modules: Input Module, Simulation
Generation Module, Simulation Customization Module, and
Simulation Analysis Module.
B. GPT-reasoning
The GPT-reasoning framework serves as the core elemen
of ChatSUMO’s functionality. The process of our reasoning
module is illustrated in Figure 1, encompassing input, simulation generation, modification, analysis modules. We will now
elaborate on the design of these modules, emphasizing their

3
O Framework
positive impact on increasing the human-machine interaction
efficiency. In this work, we consistently use Llama 3.1 to
decode the user input. In the reasoning module, it would first
analyze the user’s input which contains requirements (type
of network, city for simulation, traffic volume) to generate
he user’s ideal simulation scenario. After running the initial
simulation, the LLM would analysis the output, producing
a report for the simulation. Then ChatSUMO asks the user
what modification they want to utilize for optimization, and
he modification module will comprehend the user’s needs
and modify the simulation scenario based on the specific
commands. Finally, the LLM in analysis module analyzes the
results of each simulation and the user can choose to compare
he output from each step of modification, which includes
nformation like traffic density, average travel time, emissions
and fuel consumption.
Input Module. Input Module is header which deals with
all the input information from users. In order to reduce the
difficulty of creating traffic simulation scenarios, we have
simplified the user input as much as possible, so that the
user can create the desired simulation scenarios without enering traffic-professional descriptions using natural language.
Based on the Meta llama3.1 model, we create SUMOInput as
he traffic scenario identification model for analyzing users
nput. In this model, we customize it with specified some
prompts as “You are taking input and generate keywords for
a transportation simulation. Analyze the user input and give
a python dictionary with these keywords ...”. To generate the
nitial simulation scenario, an example of user input can be:
“Generate a simulation in city Albany with a radius of 3miles,
and the volume of traffic should be medium.” After parsed by
ChatSUMO, the natural language input would be transformed

IEEE JOURNAL
Fig. 2: Simul
into a python dictionary. These python dictionaries usually
conclude three parts: the input of decision, the input of types
the input of specific requirement. Regarding the decision
input, it requires users to make a yes or no decision for
the question. For the input of types, SUMOInput is expected
obtain the type of the decision question (type of network, kind
of modification). Specific requirement inputs are inputs tha
contains users detailed information about the simulation or
modification (number of grids, which street to be removed). As
the example above, the dictionary transformed from user inpu
would be “{city: Albany, radius: 3 miles, traffic condition
medium}”.
Generation Module. To generate the initial scenario of
the Simulation, we build the simulation scenarios in SUMO
by inputting the desired simulation scenarios from the user
Currently we can generate two types of simulation networks
including abstract scenarios (e.g., spider, grid networks) and
real-world networks. For real-world networks, users can enter
the name of the city, size of radius and the condition of traffic
(e.g., light, medium, heavy). After the user inputs a simulation
scenario, the input would be analyzed and understood by
Llama, and then it would be extracted to keywords as python
dictionary. These keywords won’t be directly transmitted to
python, as ChatSUMO will analyze the user input and provides
feedback on whether the input is sufficient to construct the
simulation scenario.
After the simulation generate module gets sufficient information, these keywords would be processed by python
script which executes commands for generating simulation. To
download the OSM (OpenStreetMap) of the required region
of city, ChatSUMO would execute “osmGet.py” to obtain
the osm map in predefined region. Then it would execute
“netconvert” commands which would convert the OSM map
to network file in SUMO. After converting, it would utilize
“randomTrips.py” and generates random trips with converted
network and required traffic volume. Finally, it would create
the configuration file which can be executed by SUMO.
Customization Module. Based on the generated simulation, ChatSUMO supports the customization of simulation

4
n Generation
from the user’s text descriptions by utilizing multiple cusomizing modules. After users enter their modification, the
nput module would analyze and match the keywords with
some predefined customizing API. Through these apis, users
can remove edges, optimize traffic light, and add vehicles to
he simulation. Here are the details of implementing these
APIs.
Edge and Lane Edit: Users can make modifications to
he roads in simulation by simply telling ChatSUMO which
anes to remove, e.g., ”I want to remove Madison Avenue”
or ”I’d like to remove the first lane in Madison Avenue”,
hus validating some of the user’s conjectures about traffic.
To realize this function, ChatSUMO would first check whether
he modified road is in the generated simulation, if so, the edit
module obtains the modification type for the road. Then the
module would extract the name of road as ”Madison Avenue”,
and generate the terminal command for SUMO tool netconvert
hrough python script to modify the network. As user only
nput the general name of the removed street, multiple edges
might be found, then ChatSUMO would ask for the user’s
decision which edge to be removed.
Traffic Light Offset: Traffic light offsets are useful dealing
with multiple traffic lights to increase the crossing efficiency
of traffic flow. Users can enter commands like ”I want to set
offsets to all the traffic light in the simulation” to set all the
raffic light in the simulation with offsets. With the traffic light
offsets, intersections are capable of green wave control. To
mplement this function, once ChatSUMO receives the key
word “traffic light offset”, it will generate terminal command
o call tlsCoordinator.py python script to modify the trafficight offsets to coordinate them for the current traffic demand,
and generate a tlsOffstes.add.xml which can be loaded into
SUMO.
Traffic Light Adaptation: Users can enter command like ”I
want to set offsets to all the traffic light in the simulation”
o optimize the traffic-light cycle in the simulation with
raffic light adaptation api. To implement this function, once
ChatSUMO receives the command, it will call tlsCycleAdaptaion.py python script generate an additional newTLS.add.xml

IEEE JOURNAL
file to sumo configuration, which modifies the signal cycle
length and the duration of green phases according to Websters
formula to best accommodate a given traffic demand.
Vehicle Generate: The vehicle generate API is used to
generate a vehicle with a given depart and arrival edge-pair
After the user entered the origin and destination, ChatSUMO
would first whether these roads are contained in the network
or it would tell the user ”Entered Roads are not in the curren
network”. To generate route for the vehicle, the module would
call getOptimalPath to finds the optimal (shortest or fastest)
path from depart edge to arrival edge by using Dijkstra’s
algorithm. Then, a vehicle with the assigned route would be
add into the cityname.rou.xml file, which would be loaded into
SUMO simulation later.
Vehicle Type Edit: In the initial traffic simulation settings
both gas vehicles and electric vehicles are generated, and the
proportion of them is 0.5 and 0.5. To change the proportion of
vehicle types, users can utilize the vehicle type edit module
To implement the customization, ChatSUMO creates a vehicle
type dictionary which stores the detail information for each
vehicle type. After the user entered the modified proportion
ChatSUMO would utilize RandomTrips.py to generate the new
route file, including the customized vehicle proportion.
Analysis Module. For analysis module, it will process data
from the output xml file generated by simulation, and interpre
them into analysis report, which involves density analysis
travel time analysis, emission analysis. Based on the outpu
of simulation, ChatSUMO would identify the top 10 congested roads, average travel time, the emission of pollutants
including CO , CO, PMx, and the fuel consumption. Every
2
time customization ends, the output of simulation would be
stored into a database. Each time the user makes customization
to the simulation, ChatSUMO would run another round of
simulation. When the simulation finished, ChatSUMO asks
the user if they want to make a comparison with any previous
simulation, giving a more intuitive summary of how effective
the optimization works.
IV. EXPERIMENTAL RESULTS
ChatSUMO with interactive web interface has been developed using Streamlit framework in Python. An example for
simulation generation between user and Llama3.1 is visualized in Figure 5. Furthermore, experiment study has been
conducted leveraging the interface to evaluate the performance
of ChatSUMO.
A. Setup
In the experiment section, we will conduct tests and experiments on the proposed ChatSUMO agent to demonstrate
its effectiveness on simulation generation and modification
For testing based on LLM, we utilized Meta’ s Llama3.1
for parsing text input by users. In the experimental part, we
will evaluate its performance in two different construction
of network, the abstract network and real-world network
As for the metrics, we focus on the average traffic density
average travel time (TT), CO emission and fuel consumption
2
(Fuel Cons) as evaluation. As the distribution of vehicles in

5
different level of roads varies a lot, to obtain the average traffic
density, we summarize the top 10 congested roads’ density and
calculated the mean of summation.
B. Simulation Generation
As the foundation of whole process, the accuracy of
simulation generation plays an extremely important role in
ChatSUMO. To evaluate the accuracy and effectiveness of
simulation generation, we generate two types of networks.
For the real-world network, we create a simulation of the
city of Albany, New York with the radius of 1 miles around
downtown. In order to make these two simulations relatively of
he same size and same density of streets, we generate a spiderike network with 20 arms, 10 circles and the distance between
circles is 150 meters. The setup for traffic condition for both
simulations is “medium”, which is 2000 vehicles per hour. To
meet these requirements, the user input is “I want to see a traffic simulation in Albany. There should be medium traffic and it
should show me streets in a 1 mile radius.”. The generated realworld simulation is shown in Figure 3. To validate the accuracy
of real-world network, we calculate the number of edges in the
network created by ChatSUMO and the network downloaded
by OSM. The number of the former is 30570 and the that of the
atter is 29325, indicating that the difference is 4.2%, which
shows a great performance of generation module. To create
such a simulation, it takes about one minute to complete the
simulation, from entering user input, to generating the final
summary. At the same time, we made a comparison with
he time needed to build such a simulation manually which
akes about 15 minutes. Considering the proficiency required
for SUMO, beginners in traffic simulation may need to spend
more time creating a complete traffic simulation, showing the
mportant contribution of ChatSUMO in time efficiency.
To evaluate how well the system handles different scales of
simulations, we conduct another experiment on recording the
processing time for simulation generation in different scales,
from small-scale intersections to city-wide traffic networks. In
his experiment, we set the scale of network as three levels (0.5
mile, 1 mile, 3 miles) to simulate different traffic condition in
city Albany. The experiment result is shown in Table I. It
can be observed that for small-scale intersections, the traffic
simulation can be generated by ChatSUMO in 10 seconds,
regardless the traffic condition. Regarding a normal scale,
which is 1 mile, traffic simulation can be created in 30 seconds.
However, the processing time of simulation increase significantly for a city-wide traffic simulation, considering the large
scale network and large number of vehicles. In conclusion, the
processing time for simulation generation depends on both the
scale of simulation and the traffic condition, as well as the cpu
performance of the conducted machine.
C. Edge Modification
Blocking some the of main streets has a significant impact
n urban traffic, which would change the constriction of traffic
flow. To assess the performance of edge editing, we implement
he edit prompt in real-world network. In this experiment,
we remove three levels of edges in simulation of Albany,

IEEE JOURNAL
Fig. 3: Edge Cust
TABLE I: Simulation Generation Experiment
Traffic condition Range (mile) Processing Time (s)
0.1 8.64
Medium 1 19.68
3 99.37
0.1 9.49
Heavy 1 23.38
3 174.3
which are Washington Avenue, Lark Street and Orange Street
to evaluate the impact of the edge removing function. A
the same time, we utilize the customization in two differen
traffic conditions, with a volume of 2000 and 3000 vehicles
per hour, to evaluate the modification impact differently. The
visualization of modification is shown in Figure 3, which
shows that our text commands successfully modified three type
of streets in the simulated network.
The results of this experiment are shown in Table II. For the
medium traffic, the removal of streets increases the average
density of main streets, e.g. removing Washington Avenue
lead to a increase of 3.32% on density. At the same time
modification of streets changes the average travel time slightly
Removal of streets also boosts the CO emission and fuel con2
sumption. However, as the level of removed streets descends
the impact on different metrics gets smaller. For Heavy traffic
interestingly, the modification of streets, decreases the average
density of main streets. The possible cause of this result is
that in heavy traffic conditions, the density of main streets is
already at a high level, and deleting an edge may lead traffic
flow to another direction, decreasing the transit pressure for

6
zation Experiment
main streets. Unsurprisingly, the removal of roads also leads
o a longer travel time in heavy traffic condition. Compared
o average density and travel time, CO emission changed
2
significantly when vehicles increase from 2000 to 3000, with
an increase about 53.1%. In correlation with CO emissions,
2
more vehicles lead to obviously higher fuel consumption. In
summary, removing lanes of different density levels affects
raffic, but the lower the original density of the removed lanes,
he smaller the impact on traffic.
D. Traffic Light Optimization
To optimize urban traffic signals, we have integrated two
signal optimization modules in ChatSUMO: one for setting
signal offsets and another for adjusting the duration of the
green light phase, which are designed for both multiple and
single traffic light optimization. Traffic light offsets is a
powerful tools when dealing with multiple traffic light coordination in urban traffic, creating green wave for the crossing
raffic flow and increasing the efficiency of transportation.
To evaluate the impact of traffic light offsets on the two
different network, in this experiment, we equip the simulations
separately with traffic light offset with the command: “I want
o set traffic light offsets for the simulation”. To optimize
ndividual traffic signals, the traffic light adaptation module
n ChatSUMO can be utilized as shown in Figure 4. The
raffic signal program shown in the figure is implemented at
he intersection of Madison Avenue and South Pearl Street. As
we can see from the figure, after user input the prompt, the
Llama3.1 process the text information and generate command
creating the newTLS.add.xml file to modify the signal phases
n SUMO simulation.
To verify the effectiveness of traffic light offsets and adapation, we compare traffic flow density, travel times, CO
2

IEEE JOURNAL
TABLE I
Traffic condition Blocked Road Density
Initial Network 19
Washington Avenue 20
Medium
Lark Street 20
Orange Street 20
Initial Network 22
Washington Avenue 21
Heavy
Lark Street 21
Orange Street 21
Fig. 4: Traffic
emission and fuel consumption (Fuel Cons) of the whole
simulation. The experiment results are shown in Table III
We conducted tests and validations by utilizing the traffic
light offset first and adapting traffic signals based on differen
traffic condition (medium and heavy traffic condition). In
medium traffic condition, it is evident that traffic light offsets
significantly decrease the average density of top 10 roads by
11.64%, and they also reduce the average travel time by around
10 seconds. After utilizing traffic signal adaptation, however
the average density is even higher than the initial condition. On
the contrast, the average travel time is reduced by surprisingly
40 seconds, which is 15.68% shorter than the initial one
The probable explanation for the result is that the signa
adaptation is designed to optimize a single intersection withou
considering the coordination of intersections. At the same
time, CO emission is decreased by 0.2t and fuel consumption
2
is decreased by 0.06t.

7
Edge Edit
km) TT(s) CO2 Emission(t) Fuel Cons(t)
287.62 1.60 0.51
291.44 1.63 0.52
289.29 1.61 0.51
286.77 1.60 0.51
293.06 2.44 0.78
302.69 2.52 0.80
297.22 2.47 0.79
294.25 2.45 0.78
ght Adaptation
E. Vehicle Edits
To compare the effectiveness of vehicle type customization,
we prompt the proportion of electric vehicles from 0.3 to 0.5,
aiming to observe the difference of pollutant emission and fuel
consumption. Using the text input “I want to set the proportion
of electric vehicles as 0.5.”, we customize the vehicle type
proportion. The output of both simulations are shown in
Figure 5. In these figures, we show the interactions with the
ChatSUMO interface, and the output generated by Llama3.1
s also shown in three figures, which is very intuitive for users
o see the summary of simulations. After implementing the
vehicle type customization, the analysis module compares two
simulations, and also generates a brief summary about general
raffic, traffic density, pollutant emission and fuel consumption.
It is obvious that the emission of CO and fuel consumption
2
has fallen by a very large amount with the increase of electric
vehicles. However, the traffic density does not vary a lot due
o the vehicle dynamic parameters are quite similar for both
vehicle types.

IEEE JOURNAL
TABLE III: Traffic Ligh
Traffic condition Modification Densi
Initial 1
Medium Traffic light offset 1
Traffic light adaptation 1
Initial 2
Heavy
Traffic light offset 2
Traffic light adaptation 2
Fig. 5: Vehicle Type Proportion
To evaluate the effectiveness of vehicle type editing and
CO and electricity trends with change of vehicle proportion
2
by ChatSUMO and traffic light adaptation, we conducted an
experiment with five different proportion of gasoline vehicle
(0, 0.25, 0.5, 0.75, 1). All five simulation runs were automatically generated by ChatSUMO. The result of the experimen
is shown in Figure 6. It can be seen from the figure that CO
2
emission increases and electricity descents with the rises of
gasoline vehicles’ proportion. However, after utilizing the traffic light adaptation, although the emission of CO decreases
2
compared to the previous one, the electricity consumption is
not affected according to the curve in the figure. We assume
that the causing is the electricity consumption model is no
sensitive to speed as travel distance.
F. Discussion and Potential Application
Through the experiments above, we have tested the ability
of ChatSUMO in multiple fundamental functions, and the

8
ptimization performance
h/km) TT(s) CO2Emission(t) Fuel Cons(t)
0 287.62 1.60 0.51
8 275.04 1.53 0.49
3 242.53 1.39 0.44
1 293.06 2.44 0.78
7 315.23 2.60 0.83
5 246.20 2.12 0.68
t with the ChatSUMO Interface.
results of these experiments shows that ChatSUMO plays an
active role not only in simulation generation but also in human
and machine interaction. When conducting these experiences,
hanks to ChatSUMO’s excellent human-computer interaction
experience, even though we made dozens of modifications to
he simulation, the experiment itself did not take too long.
Additionally, due to the involvement of the LLM, the results
of each simulation were very intuitive, saving us a lot of
unnecessary effort in our experiments.
The ease of use and excellent interactive experience of
ChatSUMO provide it with great potential for application. For
nstance, ChatSUMO can be easily deployed as an online application, similar to ChatGPT, giving an approach for internet
users to generate their own traffic simulation without mastering
he conventional tools by SUMO. Users, especially beginning
users can make preliminary testing on ChatSUMO by easily
setting the simulation scenario by text massage, and then
customize the scenario through some short words. Integration

IEEE JOURNAL
Fig. 6: Emission trend with different vehicle proport
with real-world traffic, users can build the simulation with realtime traffic data through database API, and also simulate traffic
incident like climate change or real-world road construction
With customized simulation and predefined metrics, users can
do brainstorming for planning and estimating climate impacts
as well.
V. CONCLUSION AND FUTURE WORK
In this paper, we have presented a comprehensive approach
to generating SUMO simulations based on LLM. Our system
designed with the aim of democratizing access to traffic
simulation tools, includes four key modules: user input, simulation generation, simulation modification, and output analysis
These modules work in concert to simplify the process of
creating and refining traffic simulations, making it accessible
to users with little to no prior experience in traffic modeling
The user input module ensures that users can easily specify
their requirements and parameters without needing to understand the complexities of traffic simulation syntax. Through
this integrated approach, we have demonstrated that complex
traffic simulations can be generated, modified, and analyzed
with minimal user intervention and expertise. The Llama3.1based system not only reduces the barrier to entry for traffic
simulation but also enhances the overall user experience by
providing a seamless and intuitive interface. Future work wil
focus on further enhancing the system’s capabilities, including
the incorporation of more advanced simulation features and
improved user support tools, to continue expanding the accessibility and utility of traffic simulation technologies. To the
best of our knowledge, we are the first to implement a largelanguage model with SUMO, integrating human understanding
into simulation generation and modification. For the future
work, we aim to generate more compre

9
and traffic light adaptation supported by ChatSUMO
REFERENCES
[1] Z. Cui, K. Henrickson, R. Ke, and Y. Wang, “Traffic graph convolutional
recurrent neural network: A deep learning framework for networkscale traffic learning and forecasting,” IEEE Transactions on Intelligent
Transportation Systems, vol. 21, no. 11, pp. 4883–4894, 2019.
[2] R. Ke, Y. Zhuang, Z. Pu, and Y. Wang, “A smart, efficient, and
reliable parking surveillance system with edge artificial intelligence on
iot devices,” IEEE Transactions on Intelligent Transportation Systems,
vol. 22, no. 8, pp. 4962–4974, 2020.
[3] Y. Wang, Z. Cui, and R. Ke, Machine learning for transportation
research and applications. Elsevier, 2023.
[4] S. Dorokhin, A. Artemov, D. Likhachev, A. Novikov, and E. Starkov,
“Traffic simulation: an analytical review,” IOP Conference Series: Materials Science and Engineering, vol. 918, no. 1, p. 012058, sep 2020.
[5] S. Kim and W. Suh, “Modeling traffic congestion using simulation
software,” in 2014 International Conference on Information Science &
Applications (ICISA), 2014, pp. 1–3.
[6] D. Krajzewicz, G. Hertkorn, C. Ro¨ssel, and P. Wagner, “Sumo (simulation of urban mobility)-an open-source traffic simulation,” in Proceedings of the 4th middle East Symposium on Simulation and Modelling
(MESM20002), 2002, pp. 183–187.
[7] T. Azfar, J. Weidner, A. Raheem, R. Ke, and R. L. Cheu, “Efficient
procedure of building university campus models for digital twin simulation,” IEEE Journal of Radio Frequency Identification, vol. 6, pp.
769–773, 2022.
[8] P. M. Ejercito, K. G. E. Nebrija, R. P. Feria, and L. L. Lara-Figueroa,
“Traffic simulation software review,” in 2017 8th International Conference on Information, Intelligence, Systems & Applications (IISA). IEEE,
2017, pp. 1–4.
[9] J. Nguyen, S. T. Powers, N. Urquhart, T. Farrenkopf, and M. Guckert,
“An overview of agent-based traffic simulators,” Transportation research
interdisciplinary perspectives, vol. 12, p. 100486, 2021.
10] Y. Chang, X. Wang, J. Wang, Y. Wu, L. Yang, K. Zhu, H. Chen, X. Yi,
C. Wang, Y. Wang et al., “A survey on evaluation of large language
models,” ACM Transactions on Intelligent Systems and Technology,
vol. 15, no. 3, pp. 1–45, 2024.
11] P. A. Lopez, M. Behrisch, L. Bieker-Walz, J. Erdmann, Y.-P. Flo¨ttero¨d,
R. Hilbrich, L. Lu¨cken, J. Rummel, P. Wagner, and E. Wiessner,
“Microscopic traffic simulation using sumo,” in 2018 21st International
Conference on Intelligent Transportation Systems (ITSC), 2018, pp.
2575–2582.
12] S. Wu, H. Fei, L. Qu, W. Ji, and T.-S. Chua, “Next-gpt: Any-to-any
multimodal llm,” 2024. [Online]. Available: https://arxiv.org/abs/2309.
05519

IEEE JOURNAL 10
[13] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux,
T. Lacroix, B. Rozie`re, N. Goyal, E. Hambro, F. Azhar et al.,
“Llama: Open and efficient foundation language models,” arXiv preprint
arXiv:2302.13971, 2023.
[14] L. team, “The llama 3 herd of models.” Meta, 2024. [Online]. Available:
https://ai.meta.com/research/publications/the-llama-3-herd-of-models/
[15] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin,
C. Zhang, S. Agarwal, K. Slama, A. Ray et al., “Training language
models to follow instructions with human feedback,” Advances in neural
information processing systems, vol. 35, pp. 27 730–27 744, 2022.
[16] E. Kasneci, K. Sessler, S. Ku¨chemann, M. Bannert, D. Dementieva,
F. Fischer, U. Gasser, G. Groh, S. Gu¨nnemann, E. Hu¨llermeier, S. Krusche, G. Kutyniok, T. Michaeli, C. Nerdel, J. Pfeffer, O. Poquet,
M. Sailer, A. Schmidt, T. Seidel, M. Stadler, J. Weller, J. Kuhn, and
G. Kasneci, “Chatgpt for good? on opportunities and challenges of large
language models for education,” Learning and Individual Differences,
vol. 103, p. 102274, 2023.
[17] O. Zheng, M. Abdel-Aty, D. Wang, C. Wang, and S. Ding, “Trafficsafetygpt: Tuning a pre-trained large language model to a domain-specific
expert in transportation safety,” arXiv preprint arXiv:2307.15311, 2023.
[18] J. Zhang, C. Xu, and B. Li, “Chatscene: Knowledge-enabled safetycritical scenario generation for autonomous vehicles,” in Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
2024, pp. 15 459–15 469.
[19] L. Wang, Y. Ren, H. Jiang, P. Cai, D. Fu, T. Wang, Z. Cui, H. Yu,
X. Wang, H. Zhou, H. Huang, and Y. Wang, “Accidentgpt: A v2x
environmental perception multi-modal large model for accident analysis
and prevention,” in 2024 IEEE Intelligent Vehicles Symposium (IV),
2024, pp. 472–477.
[20] B. Wang, M. M. Karim, C. Liu, Y. Wang et al., “Traffic performance gpt
(tp-gpt): Real-time data informed intelligent chatbot for transportation
surveillance and management,” arXiv preprint arXiv:2405.03076, 2024.
[21] X. Zhou, M. Liu, E. Yurtsever, B. L. Zagar, W. Zimmer, H. Cao, and
A. C. Knoll, “Vision language models in autonomous driving: A survey
and outlook,” IEEE Transactions on Intelligent Vehicles, pp. 1–20, 2024.
[22] B. Jin, X. Liu, Y. Zheng, P. Li, H. Zhao, T. Zhang, Y. Zheng, G. Zhou,
and J. Liu, “Adapt: Action-aware driving caption transformer,” in 2023
IEEE International Conference on Robotics and Automation (ICRA),
2023, pp. 7554–7561.
[23] S. Wang, Y. Zhu, Z. Li, Y. Wang, L. Li, and Z. He, “Chatgpt as your
vehicle co-pilot: An initial attempt,” IEEE Transactions on Intelligent
Vehicles, vol. 8, no. 12, pp. 4706–4721, 2023.
[24] L. Wen, D. Fu, X. Li, X. Cai, T. Ma, P. Cai, M. Dou, B. Shi, L. He, and
Y. Qiao, “Dilu: A knowledge-driven approach to autonomous driving
with large language models,” arXiv preprint arXiv:2309.16292, 2023.
[25] H. Sha, Y. Mu, Y. Jiang, L. Chen, C. Xu, P. Luo, S. E. Li, M. Tomizuka,
W. Zhan, and M. Ding, “Languagempc: Large language models as decision makers for autonomous driving,” arXiv preprint arXiv:2310.03026,
2023.
[26] P. Wang, M. Zhu, H. Lu, H. Zhong, X. Chen, S. Shen, X. Wang,
and Y. Wang, “Bevgpt: Generative pre-trained large model for autonomous driving prediction, decision-making, and planning,” arXiv
preprint arXiv:2310.10357, 2023.
[27] A. O. Diallo, G. Lozenguez, A. Doniec, and R. Mandiau, “Comparative
evaluation of road traffic simulators based on modeler’s specifications:
An application to intermodal mobility behaviors,” in 13th International
Conference on Agents and Artificial Intelligence. SCITEPRESSScience and Technology Publications, 2021, pp. 265–272.
[28] L. Da, M. Gao, H. Mei, and H. Wei, “Prompt to transfer: Sim-to-real
transfer for traffic signal control with prompt learning,” in Proceedings
of the AAAI Conference on Artificial Intelligence, vol. 38, no. 1, 2024,
pp. 82–90.
[29] Z. Zhong, D. Rempe, Y. Chen, B. Ivanovic, Y. Cao, D. Xu, M. Pavone,
and B. Ray, “Language-guided traffic simulation via scene-level
diffusion,” in Proceedings of The 7th Conference on Robot Learning,
ser. Proceedings of Machine Learning Research, J. Tan, M. Toussaint,
and K. Darvish, Eds., vol. 229. PMLR, 06–09 Nov 2023, pp. 144–177.
[Online]. Available: https://proceedings.mlr.press/v229/zhong23a.html
[30] X. Chen, M. Peng, P. Tiu, Y. Wu, J. Chen, M. Zhu, and X. Zheng,
“Genfollower: Enhancing car-following prediction with large language
models,” arXiv preprint arXiv:2407.05611, 2024.
