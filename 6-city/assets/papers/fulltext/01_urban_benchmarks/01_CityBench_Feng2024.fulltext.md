---
title: "CityBench: Evaluating the Capabilities of Large Language Models for Urban Tasks"
source_pdf: "01_urban_benchmarks\\01_CityBench_Feng2024.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-06-21T17:31:06+00:00
page_count: 12
status: ok
text_char_count: 68866
quality_flags: []
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\01_urban_benchmarks\01_CityBench_Feng2024.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-06-21T17:31:06+00:00
- Page count: 12
- Status: ok
- Text chars: 68866
- Quality flags: none

## Metadata

- Title: CityBench: Evaluating the Capabilities of Large Language Models for Urban Tasks
- Author: Jie Feng; Jun Zhang; Tianhui Liu; Xin Zhang; Tianjian Ouyang; Junbo Yan; Yuwei Du; Siqi Guo; Yong Li
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

As large language models (LLMs) continue to advance and gain widespread use, establishing systematic and reliable evaluation methodologies for LLMs and vision-language models (VLMs) has become essential to ensure their real-world effectiveness and reliability. There have been some early explorations about the usability of LLMs for limited urban tasks, but a systematic and scalable evaluation benchmark is still lacking. The challenge in constructing a systematic evaluation benchmark for urban research lies in the diversity of urban data, the complexity of application scenarios and the highly dynamic nature of the urban environment. In this paper, we design CityBench, an interactive simulator based evaluation platform, as the first systematic benchmark for evaluating the capabilities of LLMs for diverse tasks in urban research. First, we build CityData to integrate the diverse urban data and CitySimu to simulate fine-grained urban dynamics. Based on CityData and CitySimu, we design 8 representative urban tasks in 2 categories of perception-understanding and decision-making as the CityBench. With extensive results from 30 well-known LLMs and VLMs in 13 cities around the world, we find that advanced LLMs and VLMs can achieve competitive performance in diverse urban tasks requiring commonsense and semantic understanding abilities, e.g., understanding the human dynamics and semantic inference of urban images. Meanwhile, they fail to solve the challenging urban tasks requiring professional knowledge and high-level numerical abilities, e.g., geospatial prediction and traffic control task. These findings provide critical insights for the effective utilization and further development of LLMs to advance urban-related tasks and research in the future. The associated data and code are publicly available at https://github.com/tsinghua-fib-lab/CityBench.

## Outline

- Abstract (page 1)
- 1 Introduction (page 1)
- 2 Methods (page 2)
  - 2.1 CityData (page 2)
  - 2.2 CitySimu (page 2)
  - 2.3 CityBench (page 4)
- 3 Benchmark and Experiments (page 6)
  - 3.1 Settings (page 6)
  - 3.2 Overall Performance on CityBench (page 6)
  - 3.3 Detailed Analysis between Models (page 8)
- 4 Related Work (page 8)
- 5 Conclusion (page 8)
- References (page 9)
- A Appendix (page 11)
  - A.1  Few-Shot Performance of LLMs in CityBench (page 11)
  - A.2 Details of Quality Control (page 11)
  - A.3 Additional Results of Geospatial Bias Analysis (page 11)
  - A.4 Error Analysis of VLMs (page 11)
  - A.5 Map building tool in CityData (page 11)
  - A.6 Discussion (page 11)

## Markdown Content

5202
yaM
13
]IA.
CityBench: Evaluating the Capabilities of Large Language Models
for Urban Tasks
Jie Feng* Jun Zhang* Tianhui Liu*
Department of Electronic Department of Electronic School of Electronic and Information
Engineering, BNRist, Engineering, BNRist, Engineering,
Tsinghua University Tsinghua University Beijing Jiaotong University
Beijing, China Beijing, China Beijing, China
fengjie@tsinghua.edu.cn zhangjun990222@gmail.com 21211125@bjtu.edu.cn
Xin Zhang† Tianjian Ouyang† Junbo Yan†
Shenzhen International Department of Electronic Department of Electronic
Graduate School, Engineering, BNRist, Engineering, BNRist,
Tsinghua University Tsinghua University Tsinghua University
Shenzhen, China Beijing, China Beijing, China
zhangxin4087@163.com oytj22@mails.tsinghua.edu.cn yanjb20@mails.tsinghua.edu.cn
Yuwei Du† Siqi Guo† Yong Li‡
Department of Electronic Department of Electronic Department of Electronic
Engineering, BNRist, Engineering, Engineering, BNRist,
Tsinghua University Tsinghua University Tsinghua University
Beijing, China Beijing, China Beijing, China
duyw23@mails.tsinghua.edu.cn guosq21@mails.tsinghua.edu.cn liyong07@tsinghua.edu.cn

.sc[
3v54931.6042:viXra
Abstract
As large language models (LLMs) continue to advance and gain
widespread use, establishing systematic and reliable evaluation
methodologies for LLMs and vision-language models (VLMs) has
become essential to ensure their real-world effectiveness and reliability. There have been some early explorations about the usability
of LLMs for limited urban tasks, but a systematic and scalable evaluation benchmark is still lacking. The challenge in constructing
a systematic evaluation benchmark for urban research lies in the
diversity of urban data, the complexity of application scenarios
and the highly dynamic nature of the urban environment. In this
paper, we design CityBench, an interactive simulator based evaluation platform, as the first systematic benchmark for evaluating the
capabilities of LLMs for diverse tasks in urban research. First, we
build CityData to integrate the diverse urban data and CitySimu
to simulate fine-grained urban dynamics. Based on CityData and
CitySimu, we design 8 representative urban tasks in 2 categories of
perception-understanding and decision-making as the CityBench.
With extensive results from 30 well-known LLMs and VLMs in 13
cities around the world, we find that advanced LLMs and VLMs
can achieve competitive performance in diverse urban tasks requiring commonsense and semantic understanding abilities, e.g.,
understanding the human dynamics and semantic inference of urban images. Meanwhile, they fail to solve the challenging urban
tasks requiring professional knowledge and high-level numerical
abilities, e.g., geospatial prediction and traffic control task. These
findings provide critical insights for the effective utilization and
further development of LLMs to advance urban-related tasks and
research in the future. The associated data and code are publicly
available at https://github.com/tsinghua-fib-lab/CityBench.

1 Introduction
Recent years, large language models (LLMs) with extensive commonsense and reasoning capabilities have achieved excellent results in various fields [1, 48], including programming [18], mathematics [58], visual intelligence [28] and commonsense reasoning [37, 46]. Furthermore, powerful LLMs enable many unimaginable research endeavors to become feasible, e.g., agent [53] and
embodied intelligence [42, 65]. These researchers postulate that
LLMs, by acquiring extensive world knowledge and commonsense,
hold the key to unlocking promising outcomes in these challenging
applications. Many works [1, 16] have demonstrated that LLMs can
be regarded as ‘world models’ of our life and they are skilled at
solving a wide variety of tasks across multiple fields, while other
works [54, 59, 63] indicate that LLMs lack an comprehensive understanding of the real physical world and fail to handle many real-life
problems. However, these research efforts have primarily focused
on the indoor environment [41], while neglecting the outdoor environment, specifically the broader urban environment [2, 67].
Various works have explored the potential of LLMs in modeling urban space and solving urban tasks. For example, researchers
evaluate the potential of LLMs on remote sensing understanding
tasks [24] and urban visual tasks [60]. Gurnee et al. [16] evaluate
whether LLMs acquire the spatial knowledge of the world, such as
cities and coordinates. Manvi et al. [35, 36] try to extract the geospatial knowledge in LLMs to conduct geospatial indicator prediction
tasks [33]. Besides, researchers also explore how to apply LLMs into
the realistic urban applications, e.g., traffic control [26], mobility
∗These authors contributed equally.
†These authors contributed equally.
‡Corresponding author, email: liyong07@tsinghua.edu.cn

Submission #15, KDD Datasets and Benchmarks, 2025
prediction [11, 56], behavior modeling [15], visual language navigation [43] and so on. However, on the one hand, these existing works
primarily focus on evaluating the static spatial knowledge of LLMs
without considering the environment dynamics and interactivity.
On the other hand, most of them only focus on one type of task
and one modality of data in the urban space, using small dataset
that are not scalable globally. Although there are some existing
simulators for urban space such as game simulators [19] and traffic
simulators [31], they cannot be directly applied to support the evaluation and significant amount of adaptation work is required. None
of them can support the systematic evaluation of LLMs’ capabilities
for diverse tasks in urban research, ranging from understanding
and reasoning to decision-making tasks.
In this paper, we propose CityBench, a comprehensive evaluation platform for assessing the capabilities of LLMs to solve the
diverse urban tasks. It covers multiple modalities, supports interactive simulations, and includes data from 13 cities around the
world. CityBench consists of three modules: a data module CityData for collecting and processing diverse urban data, a simulation
module CitySimu for simulating fine-grained urban dynamics, a
evaluation module CityBench for the final evaluation of LLMs and
VLMs. In CityData, we first collect three kinds of open urban data:
geospaital data from Open Street Map, urban visual data from the
Google map and ArcGIS, and human activity data from Foursquare
and other websites. Then, we build an efficient simulation engine
CitySimu to simulate fine-grained urban dynamics and develop
various interfaces for controlling the urban dynamics and sensing the urban environments. Furthermore, based on CitySimu, we
design a comprehensive benchmark to evaluate the capability of
LLMs and VLMs, covering core research problems from various
urban research fields. The benchmark comprises two levels of tasks:
perception&understanding tasks and decision-making tasks. In perception&understanding tasks, based on the integrated multi-source
data from CitySimu, we introduce street view and satellite image
understanding and urban space understanding tasks to evaluate the
urban geospatial knowledge of LLMs and VLMs. In decision-making
tasks, we apply LLMs and VLMs to interact with CitySimu to complete the urban exploration, visual navigation, mobility prediction
and traffic signal control task, which require the comprehensive
ability of them. In summary, our contribution are as follows,
• We develop CityData and CitySimu, an urban data collector and
processor designed to support diverse urban tasks and applications, as well as an efficient urban simulator for generating
find-grained urban dynamics. They provide ease-to-use APIs for
controlling urban dynamics and sensing urban environments.
• We propose CityBench, a comprehensive evaluation benchmark
for evaluating the capability of LLMs and VLMs for urban tasks,
which includes 4 geospatial understanding tasks and 4 interactive urban decision-making tasks in 13 cities around the world.
• Extensive experiments on CityBench with 30 well-known open
source and proprietary LLMs and VLMs demonstrate the effectiveness of CityBench as evaluation benchmark and also discuss the potential and limitation of applying LLMs and VLMs
in urban tasks, ranging from understanding and reasoning to
decision-making task.

Jie Feng et al.
2 Methods
As presented in Figure 1, CityBench is a simulator based evaluation
platform with three core components: CityData for collecting and
processing diverse urban data, CitySimu for simulating human
dynamics and providing an interactive simulation environment,
and CityBench for model evaluation on 8 representative urban tasks
with different modalities.
2.1 CityData
In the section, we introduce the multi-source urban dataset CityData collected to support multi-modal urban tasks. To present a
complete picture of the city’s geospatial structure, semantic features,
and human activities, CityData integrates the following globally
available data from multiple sources [30]. The python package for
data collection and access is open-source1.
Geospatial Data Geospatial data, represented by maps, is the
most fundamental data for describing the urban structure including
road networks, points of interest (POIs), areas of interest (AOIs), etc.
OpenStreetMap (OSM) 2 is most widely used open source map data.
However, the raw data provided by OSM cannot support the simulation of urban dynamics directly because the relationship between
different elements is incomplete such as the connection between
buildings and roads. Therefore, we provide a globally available
rule-based map building tool 3 within CityData that reconstructs
lanes, lane topology, and building-lane connections based on the
raw OSM data. The reconstructed map is used as the geospatial
base and simulation input in CitySimu.
Urban Visual Data Street view data and satellite images are
two types of globally available urban data that contains rich semantic information, which represents the visual of human. Therefore,
CityData also integrates the two types of data, the former obtained
via Google Maps API and Baidu Maps API, and the latter using the
Esri World Imagery as data source. In CityData, street view data is
accessed through spatial location and facing direction, and satellite
images are acquired through spatial ranges.
Human Activities Data We use the global Foursquare-checkin [61]
data and a synthetic global origin-destination data (OD data) 4 as
the proxy of human activities to enable the fine-grained human
movement simulation. The Foursquare-checkin dataset [61] is a
long-term user check-in dataset collected from Foursquare 5 in
approximately 400 cities worldwide. It has been widely used in the
community over the past ten years [5]. Origin-destination data is
generated by a diffusion model with population from Worldpop 6
and satellite image from Esri World Imagery as input. While all
the user information are anonymized, we follow the license from
Foursquare-checkin [61] to protect the public privacy.
2.2 CitySimu
Building on CityData, CitySimu simulates the urban dynamics and
provide diverse easy-to-use APIs for the interactive operation. As
shown in Figure 3, CitySimu contains the base environment APIs for
1https://github.com/tsinghua-fib-lab/pycitydata
2https://www.openstreetmap.org/
3https://github.com/tsinghua-fib-lab/mosstool
4https://github.com/tsinghua-fib-lab/generate-od-pubtools
5https://foursquare.com/
6https://www.worldpop.org/

CityBench: Evaluating the Capabilities of Large Language Models for Urban Tasks
Geospatial Data Urban Visual Data Human
Location Spatial Range
OpenStreetMap & Direction
mosstool
Public API
Map
Street View Satellite Image
Road, POI, AOI, e.t.c
CityData
…
Multi-source Urba
…
Diffusion M
OD Matr
Individual Mobility Simulation Urban Vi
Next Lane/POI
…
Planning
…
…
…
Position
CitySimu Nearby Road/POIs
LLM&VLM Deploy Perception and Understanding
Prompt Examples
.......
GeoSpatial
Prediction
- Local Deployment
- Cloud APIs Traffic
Signal
CityBench Control
Figure 1: The framework of CityBench, which consists of a dat
urban tasks with different modalities. The evaluation data in
obtaining the static information of environment, three simulation
APIs for human and vehicle behavior simulations, language APIs
to enable the interaction between CitySimu and LLMs.
Individual Mobility Simulation Based on the geospatial data,
the individual mobility simulation constructs a simulator that can
simulate an agent moving and exploring within the city. Agents
can obtain the POIs and roads around them through API provided
by CityData, and thus plan and decide the next lane or POI to travel
in to update their locations. For the mobility prediction task in the
city scale, the available actions are defined as the POIs around the
city. For the urban exploration task in the local street scale, the
available actions are defined as the nearby lanes.
Urban Visual Environment Simulation To further support
the study of urban visual intelligence [10], we follow [4, 38] to
construct a urban visual environment simulation with real street

Submission #15, KDD Datasets and Benchmarks, 2025
vity Data
ures Public Dataset
CityBench
Checkin
from citybench import Evaluator - 8 Tasks
- 20K+ Images
Eval = Evaluator(city, task, model, version) - 30K+ Questions
Eval.evaluate() - 13 Cities
Eval.show_benchmark() - 100+ VLMs/LLMs
Environment Simulation Microscopic Traffic Simulation
Direction Traffic Signals
Traffic
Dynamics
Decision Decision
Car
Following
Lane
Changing
Junction
Instruction + StreetView Image Queue Length
Planning and Decision-making Analysis and Benchmark
llector CityData, an activity simulator CitySimu and 8 diverse
e benchmark is collected from 13 cities around the world.
view images and map data. In the environment, agent can access
the panoramic images of its location via APIs and then select the
available actions to move along the road to arrive the destination. In
the outdoor visual-language instruction navigation task, given the
human-like instruction, agent can observe the panoramic images
of its location, extract key elements from them and then decide
one direction to go. This can be saw as an extension of individual
mobility simulation with visual input.
Traffic Simulation In the former two simulations, we only
simulate the individual actions without the interaction with others.
Here, we introduce microscopic traffic simulation to model the
interaction behaviors between vehicles and provide a traffic control
environment. The simulator takes the geospatial data reconstructed
from OSM within CityData and the travel demand described by
the synthetic global OD data as inputs. It simulates the vehicle

Submission #15, KDD Datasets and Benchmarks, 2025 Jie Feng et al.
Data Collection Data Processing Evaluation Generation Quality Control CityBench Tasks
Matching Template based Human Testing Understanding Decision-making
Q { A o x f : : x { T W } x x h in i } e c . h C r o i { t a r y d o A a i d s ? } { x is x } th . I e t b is o u in n d th a e r y n o o r f th D C Q i o u v r a e r l r e i s t c y i t t n y ess LLM G N La o e n d o d e Q m s A , a P r a k t s h , s, M Ur o b b a il n it E y x P p r l e o d r i a c t t i i o o n n
Refinement LLM Assisted LLM Testing Rewriting Districts, ....... Traffic Signal
Control
Q: From the A ... , Diversity
given the image Correctness Image
Map Human Activity s th eq e u in en st c r e u , c g t e io n n e . rate Quality Geolocalization Outdoor
Annotation A do : w F n i r t s h t e g r o o s a t d r , a a ig n h d t Deploy VLM G Pr e e o d s i p c a ti t o ia n l Vison-Language
then take a left at ... Navigation
Address: xx street Infrastructure
Buildings: 1 park Inference
Roads: highway
Urban Visual Data
Figure 2: The pipeline of building benchmark, including data collection stage, data integration stage, evaluation generation
stage and quality control stage.
CityData CitySimu CityBench
Base Environment API Interactive Objects Simulation API Supported Task Examples
Individual LLM API
Action: walk Mobilty Urban GeoSpatial
Satellite Image Human Simulation Exploration Prediction
Mobility Infrastructure
Visual Signal Urban Visual LLM API Prediction Inference
Environment
Human Simulation
Street Activity Traffic Signal Outdoor Image
View Navigation Geolocalization
Image Vehicles LLM API
Traffic Traffic Signal GeoQA
Map Data Action: drive Simulation Control
Figure 3: The simulation framework of CitySimu, including base environment APIs, interactive objects, simulation APIs and
language APIs. Besides, supported task examples also present the relation between simulation APIs and evaluation tasks.
behaviors through realistic driving simulation models including the data processing stage. We focus on introducing the evaluation
the intelligent driver model (IDM) [49] as the car-following model generation stage and quality control stage as follows.
and the randomized MOBIL model [14, 23] as the lane-change In the evaluation generation stage, we use template based methmodel to obtain the dynamics of all vehicles in the city at each ods and LLMs/VLMs based methods to generate the evaluation quessecond. The simulator also provides a series of sensing and control tions. For example, for the image geolocalization task, the groundth
APIs. Through the sensing APIs, LLMs can obtain data about urban location is already known when collecting, thus we directly design
dynamics such as junction queue length, vehicle speed, and road template based question to convert the image geolocalization task
average speed. Through the control APIs, LLMs can intervene in the into question answer pair. As for the outdoor navigation task, we
city’s operation, such as modifying traffic signal lights, modifying employ VLM to act as human annotation experts to annotate the
the speed limit of the road, etc. data to generate the navigation instruction with additional inputs.
In CityBench, instructions for urban exploration task and outdoor
2.3 CityBench navigation task are generated by LLM assisted methods. Instructions for other tasks are generated from template based methods.
Based on CityData and CitySimu, we design a multi-modal urban
Due to the hand-craft designs and potential issues of LLMs, we
evaluation benchmark CityBench to evaluate the capability of LLMs
apply a quality control stage to filter and rewrite the generated
and VLMs. In the following section, we first summarize the whole
questions to obtain a high quality evaluation questions. For quespipeline and then give introduction to each task.
tions generated from template based methods, we use LLM as data
quality expert to filter the low-quality data and use LLM as data
2.3.1 Pipeline. Figure 2 describe the procedure of building evalrewritter to rewrite the questions with diverse formats and expresuation benchmark. As introduced before, CityData works in the
sions. For questions generated from the LLMs/VLMs based methods,
data collection and data processing stage and CitySimu works in

CityBench: Evaluating the Capabilities of Large Language Models for Urban Tasks
(A N c o c d ) e
Paths (Acc) GeoQA
for city
Dis ( t A r c ic c t ) s
Boun (A da c r c y ) Othe ( r A s c c ) Acc p1- To F1
La ( n A d c m c) ark R S a u te ccess
U L n L
S N te
d
a p
M
v s ig
e
a L t a
r
io
&
n n g
s
ua
t
V g i
a
e s u D a O l e - u c t i d s o i V o o n r L
C
D i s M tan ce &
i t y B e n
I nf r R a e
c
c s al t l r u c
h
- t u V re I U n L f er e n n M ce d n e & d r A s i n c t c a u g r G a c y e P o r s e p d a i t c i t a R
G
i
-
l o
l
M n
i
e
z
S
o
a
E
l
t
o
io
ca
n
A r c 2 / c 2 @ 5
A
k 1
c
m k
c
m
nding
Mo bility Pre dictio n
D ecisi L
on
L M
L C
&
en o g n t h t r T Q o u l r e a u e f f i c T u t h
E
ro
x
u
o p
g
U n
h
l
p
r o b ra a t n i
S teps
S R u a c t c e ess
Figure 4: 8 tasks in CityBench with their metrics.
we use LLM/VLM as the agent with additional information to execute the task to verify the quality of generated instructions. If
the generated questions are filtered too much, we will return to
the evaluation generation stage to generate new questions again.
Finally, authors of this paper also participate in the quality control
stage to filter and rewrite the generated data to ensure the quality
of whole benchmark.
After the above stages, we produce the evaluation benchmark
with 8 urban tasks. Their relations are presented in Figure 4. Details
of each task are introduced as follows.
2.3.2 Perception and Understanding Task. The first task is the street
view image geolocalization task from the urban visual intelligence [10
Following are social indicator prediction and infrastructure inference tasks from remote sensing field. Finally, we adapt GeoQA [12,
34] task into urban environment.
Image Geolocalization Image geolocalization task is to predict
the precise location of image based on its context. Street view
image is regarded as the recording of urban appearance and play
an important role in understanding the urban environment and
dynamics [10]. Thus, we query VLMs with street view image and
require them to directly generate the location of image. A good
VLM should recognize the important objects from the street image
and mapping them into the potential locations. Following [17], we
define two subtasks for this task: city name inference and precise
latitude and longitude inference.
Geospatial Prediction Geospatial predictions are important for
understanding the global sustainable development especially for
developing countries, e.g., poverty estimation [20] and population
density estimation [47]. One of the most widely used solutions is
using satellite images with machine learning methods to predict
these socioeconomic indicators. In the benchmark, following setting from [36], we query VLMs with a satellite image as context

Submission #15, KDD Datasets and Benchmarks, 2025
to predict the population density of it. We use population from
Worldpop [47] as the groundtruth.
Infrastructure Inference Besides, we also introduce the infrastructure inference task which means to recognize the urban infrastructures from the satellite images. This task require the ability of
scene understand and object segmentation of urban environment.
The groundtruth of this task is extracted from the OSM by matching
predefined infrastructure key words within a fixed spatial range.
Given the satellite image and a list of all kinds of infrastructures,
VLM is required to generate the infrastructure names appeared in
the image. Here, we pay attention to the following infrastructures:
Airport, Harbor, Stadium, Bridge, Roundabout and Train Station.
GeoQA for City Elements Beyond understanding the urban
space from the visual perspective, we introduce geographic question answer(GeoQA) [34] to test whether LLMs comprehends the
fundamental elements [32] in a city from the concept view, such as
road and landmarks. For example, we directly ask LLM about the
relation between different roads in a city. Following [12, 32], we
classify the spatial elements into six groups and design problems for
each group. These six groups are node, path, landmark, boundary,
districts and others.
2.3.3 Planning and Decision Making Task. Different from the static
evaluation introduced in the last section, we design four interactive decision making tasks to evaluate the capabilities of LLMs in
dynamic and partial observed environments which are more challenging and realistic. With the interaction with the CitySimu and
dynamic human activities, LLMs need to understand the important
mechanisms and regularity in the urban environments to complete
the decision-making tasks.
Mobility Prediction As one of the fundamental task for understanding the human behaviors and urban dynamics, mobility
prediction task is to predict the next location of user in the next
time window with given the past mobility trajectory. Here we use
the the global Foursquare checkin data to support the mobility
prediction in the simulator. We follow [56] to conduct the mobility
prediction task via LLMs.
Outdoor Navigation Outdoor navigation task is widely used in
neurocognitive science [9] as the important benchmark for evaluating the spatial cognition of human and models. As one of the most
widely-used settings in outdoor navigation task, vision-language
navigation task [43, 62] requires the model to follow the humanannotated language instruction to arrive to the destination with the
nearby street view images as additional input. This task requires
the VLMs to acquire the ability of urban visual scene understanding,
language understanding and decision-making.
Urban Exploration Here, we define a text based street exploration task to evaluate the zero-shot navigation capability of LLMs
in a new city without visual input and instructions. Different from
the visual language navigation which require model to follow the
language instruction and understand the scene via street view image, our urban exploration task require model to explore the region
via the local information (e.g. accessed road names) provided by the
simulator during action and its intrinsic knowledge of the whole
urban space in the city.
Traffic Signal Control Traffic signal control task is one of
the widely studied realistic urban decision making task in recent

Submission #15, KDD Datasets and Benchmarks, 2025
Table 1: Detailed statistics of multi-source data for 13 global
cities utilized in CityBench.
Visual Data GeoSpatial Data Human Activity Data
Cities
Satellite StreetView OD flow
Roads PoI/AoIs Checkins
Image Image (>10)
Beijing 1764 7482 17043 276090 1905025 21015
Shanghai 5925 4170 33321 57731 845188 33129
Mumbai 638 6025 6296 60245 309147 31521
Tokyo 1120 5514 33174 1146094 969865 1044809
London 1710 4148 14418 83892 1401404 173268
Paris 238 6044 4443 21950 28362 85679
Moscow 1558 5761 9850 28289 979064 836313
NewYork 320 3934 5414 349348 71705 390934
SanFrancisco 345 4473 4171 73777 61367 100249
SaoPaulo 1332 5184 28714 1681735 311830 808754
Nairobi 336 5987 2972 264101 135332 25727
CapeTown 896 5175 5947 151711 525578 11591
Sydney 1935 5087 21390 141997 438763 54170
years [57]. It is challenging for existing methods due to the dynamic
traffics and the generalization issues. It is to generate the future
traffic signal schedule by considering the current traffic states and
the future traffics. Lai et al. [26] propose LLMLight to employ LLM
as decision-making agent for traffic signal control problem and
demonstrate the generalization of LLMs. Following this work, we
evaluate the potential of LLMs as agents for multiple-intersections
traffic signal control.
3 Benchmark and Experiments
3.1 Settings
Model Deployment To facilitate usage of CityBench, we have
implemented local deployment support for the majority of LLMs
and VLMs using VLMEvalKit [8] and vLLM [25]. Additionally, we
also support evaluation through the APIs of proprietary models, e.g.,
OpenAI and open-source models, e.g. DeepInfra 7 and Siliconflow 8.
Baselines We select well-known LLMs and VLMs as baselines.
For VLMs, we select LLaVa-NeXT [28], CogVLM-v2 [55], MiniCPMLLama3-V-2.5 [40], Qwen-VL-plus and GPT4o. For LLMs, we select LLama3-8B, LLama3-70B, Mistral-7B-v0.2 [21], Mixtral-8x22Bv0.1 [22], DeepSeekv2 [44], GPT3.5, and GPT4 [1]. We also select
representative baselines, including GeoCLIP [51] for street view image geolocalization, RSVA [52] for infrastructure inference, RemoteCLIP [27, 64] for population prediction, LSTPM [45] for mobility
prediction and MaxPressure [50] for traffic signal control task.
Evaluation Metrics We follow the common practice of each
task to define the metrics. Metrics and instances for each task are
presented in Figure 4 and Table 6 in appendix. For each task with
results from 13 cities, we report the mean value of them in Table 2
and Table 3. More detailed results like standard deviation value can
be found in the appendix.
3.2 Overall Performance on CityBench
3.2.1 CityBench are Challenging for LLMs and VLMs. The
performance of LLMs and VLMs on CityBench is summarized in
7https://deepinfra.com/
8https://siliconflow.cn/

Jie Feng et al.
Table 2: Performance of 16 widely-used VLMs on four urban
visual tasks in CityBench. Here, ‘City’ and ‘Loc.’ represent
the city name inference task and the geo-coordinates inference task for street view images, respectively; ‘Population’
refers to the geospatial prediction task; ‘Infra’ denotes the
infrastructure inference task; and ‘Navigation’ indicates the
outdoor visual-language navigation task. ‘Succ.’ stands for
the success rate metric, while ‘Dist.’ represents the distance
metric.
Tasks Perception&Understanding Decision-making
City Loc. Population Infra Navigation
Metrics Acc↑ Acc↑ RMSE↓ 𝑟2↑ Acc↑ Succ.↑ Dist.↓
Baselines
GeoCLIP 0.340 0.464 - - - - -
RSVA - - - - 0.655 - -
RemoteCLIP - - 1.966 0.368 - - -
VLMs
Qwen2VL-2B 0.630 0.407 2.478 0.008 0.657 0.020 679.333
InternVL2-2B 0.238 0.380 3.142 -0.841 0.738 0.247 236.088
InternVL2-4B 0.398 0.397 2.501 -0.144 0.735 0.260 272.445
Yi-VL-6B 0.000 0.105 5.471 -3.967 0.816 0.267 429.683
Qwen2VL-7B 0.688 0.522 2.637 -0.112 0.773 0.153 529.549
LLaVANeXT-8B 0.267 0.221 3.31 -0.764 0.796 0.207 361.647
MiniCPMV2.5-8B 0.262 0.223 3.57 -1.054 0.806 0.260 296.427
InternVL2-8B 0.522 0.728 2.806 -0.320 0.806 0.233 223.971
GLM-4v-9B 0.726 0.000 2.769 -0.516 0.857 0.247 444.793
CogVLM2-19B 0.559 0.326 2.75 -0.301 0.726 0.087 596.056
InternVL2-26B 0.429 0.003 2.683 -0.209 0.790 0.180 526.079
Yi-VL-34B 0.251 0.003 2.510 -0.052 0.790 0.253 384.005
LLaVANeXT-34B 0.501 0.408 2.61 -0.163 0.804 0.267 274.036
InternVL2-40B 0.574 0.555 2.514 -0.113 0.808 0.213 364.032
Qwen-VL-plus 0.793 0.645 3.14 -1.028 0.454 0.240 377.622
GPT4o 0.862 0.797 2.32 0.122 0.812 0.180 388.582
Table 3 for urban tasks without visual input and in Table 2 for urban
visual tasks. As we can observe, except for the street view image
geolocalization and infrastructure inference tasks, the performance
of LLMs on the remaining six tasks is suboptimal and remains far
from the ideal ceiling. For instance, the performance on GeoQA
task, which evaluates detailed knowledge about urban elements of
LLMs, is only 0.398, significantly lower than the best possible score
of 1.0. These results demonstrate that CityBench is a challenging
benchmark on urban tasks for LLMs.
3.2.2 LLMs and VLMs Struggle with Numerical Tasks. As
shown in Table 3 and Table 2, the performance of LLMs and VLMs
on numerical tasks, including population estimation and traffic
signal control, significantly lags behind existing baselines. In population estimation tasks, the best-performing LLM, GPT-4o, underperforms RemoteCLIP by 18% in terms of RMSE. Similarly, in traffic
signal control tasks, the top-performing VLM, InternVL2-40B, trails
behind the Max-Pressure method by 41.9% in queue length. Therefore, improving the performance of LLMs on numerical tasks is
crucial for their application in urban tasks. Although some studies
have explored potential solutions by adding task-specific heads to
LLMs, such designs may compromise the generalizability of the
model.

CityBench: Evaluating the Capabilities of Large Language Models for Urban Tasks
Table 3: Performance of LLMs and VLMs on four urban tasks
without visual input in CityBench. Here, ‘Top 1’ represents
the Top-1 Accuracy metric, ‘Succ.’ denotes the success rate
metric, ‘Q’ refers to the Queue Length metric, and ‘TP’ indicates the throughput metric. ‘Und.’ stands for the understanding task.
Tasks Und. Planning & Decision-making
GeoQA Mobility Exploration Traffic Signal
Metrics Acc↑ Top1↑ F1↑ Succ.↑ Steps↓ Q↓ TP↑
Baselines
LSTPM - 0.114 0.086 - - - -
Fixed-Time - - - - - 57.870 993.333
Max-Pressure - - - - - 36.898 1345.333
LLMs
Mistral-7B 0.229 0.090 0.087 0.730 5.382 64.120 853.333
Qwen2-7B 0.289 0.142 0.109 0.697 5.889 62.271 880.000
Intern2.5-7B 0.304 0.118 0.102 0.738 5.552 55.121 1047.667
LLama3-8B 0.297 0.130 0.094 0.747 5.304 57.738 1014.333
Gemma2-9B 0.339 0.131 0.120 0.716 5.679 74.475 651.333
Intern2.5-20B 0.315 0.116 0.098 0.679 6.243 61.229 958.667
Gemma2-27B 0.349 0.145 0.118 0.713 5.733 56.081 1009.333
Qwen2-72B 0.357 0.155 0.135 0.697 5.887 66.924 793.333
LLama3-70B 0.329 0.159 0.130 0.796 4.941 59.338 959.667
Mixtral-8x22B 0.321 0.155 0.136 0.745 5.339 65.682 821.333
DeepSeekV2 0.358 0.126 0.101 0.698 5.739 56.086 1020.333
VLMs
InternVL2-2B 0.296 0.000 0.000 0.672 6.015 55.725 1012.000
InternVL2-4B 0.304 0.130 0.102 0.674 6.091 74.499 647.667
InternVL2-8B 0.329 0.142 0.102 0.703 5.714 53.196 1069.667
InternVL2-26B 0.310 0.137 0.107 0.694 5.723 57.512 971.667
InternVL2-40B 0.351 0.159 0.121 0.675 6.041 52.459 1087.000
Qwen2VL-2B 0.293 0.103 0.075 0.643 6.315 56.097 1003.667
Qwen2VL-7B 0.286 0.144 0.102 0.660 6.155 55.885 995.333
MiniCPMV2.5-8B 0.308 0.124 0.092 0.708 5.643 56.066 1001.000
LLaVANeXT-8B 0.313 0.124 0.084 0.688 5.891 56.184 989.333
GLM-4v-9B 0.296 0.133 0.092 0.680 5.979 53.870 1058.000
CogVLM2-19B 0.282 0.026 0.029 0.710 5.905 55.229 1046.667
GPT3.5-Turbo 0.285 0.152 0.113 0.719 5.473 56.219 1022.000
GPT4-Turbo 0.398 0.147 0.125 0.757 5.184 55.761 1022.333
3.2.3 Performance Consistency between Various Urban Tasks
As the best-performing VLM in urban visual tasks, GPT-4o only
excels in the first two tasks, while other VLMs, such as GLM-4v-9B,
LLaVANeXT-34B, and InternVL2-8B, outperform it in the remaining two tasks. For urban tasks without visual input, LLama3-70B
achieves the best performance in mobility prediction and urban
exploration tasks, but it falls behind other high-performing LLMs
like GPT-4 Turbo and InternVL2-40B in the other two tasks. In other
words, due to the heterogeneity and complexity of urban tasks, no
LLM or VLM, including the powerful GPT-4 series, can consistently
perform well across all tasks. These results highlight the challenges
posed by CityBench and underscore the necessity of developing
domain-specific LLMs and VLMs tailored for urban tasks.
3.2.4 LLMs and VLMs Exhibit Geospatial Bias. To further investigate the difference between LLMs and VLMs, we report the
detailed results of mobility prediction task and image geolocalization tasks from 13 cities in Figure 5. Based on the above results, we

Submission #15, KDD Datasets and Benchmarks, 2025
    
    
    
    
    
    
 0 L V W U D O   %  / O D P D  
 0
  %  L [ W U D O   [ 
 /
 
 O D
 %  P D   
 '
  %  H H S 6 H H N  9
 *
   3 7      * 3 7  
 Q R L W F L G H U 3  \ W L O L E R 0 # \ F D U X F F $
Tokyo Captetown Shanghai
Paris Nairobi Sydney
London SanFran Newyork
Mumbai SaoPaulo Beijing
Moscow
1.0
0.8
0.6
0.4
0.2
0.0
Tokyo Paris London
Mu
mbai Mosco w CapeTo wn Nairob
S
i anFrancis
S
co
ao
Paulo Shanghai Sydney
Ne w
York Beijing
noitazilacoloeG
egamI
,mk52@ycaruccA
CogVLM2 LLaVA-NeXT-34B Qwen-VL-plus
LLaVA-NeXT-8B MiniCPM-V-2.5 GPT-4o
Figure 5: Detailed performance results of LLMs on two tasks:
(top) mobility prediction and (bottom) image geolocalization.
Both tasks are evaluated across multiple cities and multiple
models, demonstrating that significant performance variations across diverse urban contexts are consistently observed
even with different model architectures, highlighting the
pervasive nature of geospatial bias in these models.
have made several interesting discoveries. First, we find that the
performance of different LLMs varies a lot across different cities, no
LLM can always perform best in mobility prediction tasks. Second,
we find that the performance of VLMs on visual task like image
geolocalization task are significantly biased. Most VLMs perform
well in major international cities, but poorly in some lesser-known
cities (e.g., CapeTown and Nairobi). We provide preliminary evidence for this phenomenon by analyzing the number of publicly
accessible websites indexed on Google and Wikipedia. We find that
cities with fewer publicly available websites tend to pose greater
challenges for LLMs, while those with more extensive online presence are generally easier for the models to handle. For more details,
see section A.3 in the appendix. The variability in evaluation results demonstrate the necessity of establishing a global evaluation
benchmark, and also highlights the potential shortcomings and
areas for improvement of LLMs.

Submission #15, KDD Datasets and Benchmarks, 2025
3.3 Detailed Analysis between Models
3.3.1 Disparity between Proprietary and Open-source Models. Although the GPT-4 series performs well on most tasks, several
open-source models have achieved better results on multiple other
tasks, albeit not consistently by a single open-source model. In
other words, we do not observe a dominant advantage of proprietary models over open-source models on CityBench, which may be
attributed to the uniqueness and heterogeneity of urban tasks. The
reasons behind this phenomenon warrant further in-depth analysis in future research. While the performance of models within
the same series generally follows the scaling law with respect to
model size, most VLMs’ performance across tasks is not robust. For
instance, some VLMs exhibit near-zero performance, and larger
models within the same series do not always outperform smaller
ones. For example, InternVL2-26B performs worse than InternVL28B. Similar trends are observed in LLMs, where Intern2.5-20B does
not consistently outperform Intern2.5-7B.
3.3.2 Performance Correlation between VLMs and LLMs.
While most VLMs are continuously trained based on LLMs, we
investigate the impact of LLMs on VLM performance. First, we find
that the performance variability across different LLMs and VLMs
is primarily influenced by the capabilities of the LLM backbone.
For instance, in widely used VLMs for urban tasks, Intern2.5-7B
consistently outperforms Qwen2-7B and Mistral-7B across most
tasks, which can be attributed to Intern2.5-7B’s superior performance in general NLP tasks at the same parameter scale. Similarly, LLaVA-NeXT-8B demonstrates performance comparable to
MiniCPM-V2.5-8B, as both models share the same LLM backbone,
LLaMA3-8B. Second, as shown in Table 3, we observe that most
VLMs underperform compared to their LLM bases on urban tasks
without visual input. This demonstrates that while post-training of
LLM-based VLMs enhances visual capabilities, it inevitably leads
to performance degradation in original textual tasks. For example,
LLaVA-NeXT-8B lags behind LLaMA3-8B on all textual tasks, with
an average performance degradation of 4.10%, while MiniCPMv2.58B exhibits a smaller degradation of over 1.88%. Therefore, maintaining the general capabilities of LLMs during the training of VLMs
should be a key direction to ensure their effectiveness across a wide
range of tasks.
3.3.3 Typical Errors of LLMs and VLMs in CityBench. We
find that LLMs often display errors such as logic error, format error,
invalid action, refusal to answer, and hallucinations. The types of
errors are highly correlated with the characteristics of the LLMs.
For instance, certain models, such as MiniCPM2.5-8B, exhibit excessive alignment in handling geospatial-related content, leading
to a systematic refusal to respond to queries across various tasks,
as illustrated in the image localization task depicted in Figure 5. On
the other hand, smaller models like InternVL2-2B often struggle
to follow instructions, leading to format errors and invalid actions.
We present typical error cases in Figure 6. For example, Llama3-8B
exhibited a logical error in its judgment of time in the task mobility
prediction. For the urban exploration task, Qwen2-7B refused to
choose the option and instead demanded the user to use a navigation service to solve the problem. Intern2.5-7B directly stated that it
lacks expertise in this area and needs more information to answer

Jie Feng et al.
the question. Llama3-8B provided an invalid option in the traffic
signal task, rendering CitySimu unable to perform next action. We
notice that the most frequent error is Misformatted, and several
instances close to 0 in Table 3 are mostly caused by formatting
errors. Thus, one of the promising direction is to reduce these error
from LLMs to improve their practicality. More detailed analysis on
VLMs are presented in section A.4 of appendix.
4 Related Work
Evaluating LLMs for Urban Knowledge and Tasks. Researchers
from various urban related fields have conducted extensive evaluations of LLM in urban space from different aspects [7, 13]. Kuckreja
et al. [24] evaluate the performance of multi-modal LLMs on several
remote sensing related tasks. Yang et al. [62] propose V-IRL benchmark to evaluate the performance of multi-modal LLMs on street
view image related tasks including localization and recognition
tasks. Mai et al. [33] and Manvi et al. [36] use LLMs to predict social
indicators like population and education level. Gurnee et al. [16]
and Bhandari et al. [3] try to testify whether LLMs know the coordinates of geospatial entity. Mooney et al. [39] and Deng et al. [6] use
GIS exams to understand the geospatial skills of LLMs. Different
from these works, we first introduce the interactive simulator based
systematic evaluation system for LLMs and VLMs, which covers
various data modalities, diverse urban task types and differentiated
data from 13 cities around the world.
Interactive Decision-making and Urban Simulator. Beyond
the above static evaluation, researchers also evaluate the capacity
of LLMs in the interactive decision making tasks with customized
simulators, e.g., web agent [29] with web environment and embodied intelligence [63] with virtual home [41]. In the urban domain,
Schumann et al. [43] apply LLM to do the visual language navigation task in Touchdown [4] and Lai [26] apply LLMs as the traffic
light controller in CityFlow [66] to manage the road traffic. Besides,
Yang et al. [62] design V-IRL as the environment of street view
image related tasks and propose a global scale virtual intelligence
benchmark. These works only evaluate the potential of LLMs in
single urban decision-making task and most of their results rely
on small-scale datasets in limited regions. Different from them,
our work builds on an efficient urban simulator with global scale
and supports 4 representative urban decision-making tasks with
different modality in one benchmark, including urban exploration,
outdoor navigation, mobility prediction and traffic control task.
5 Conclusion
In this paper, we propose CityBench, a systematic evaluation benchmark for LLMs and VLMs in diverse urban tasks. With the data
support from CityData and simulation support from CitySimu, we
design 8 important urban tasks in 13 cities to constitute the CityBench for evaluating the capabilities of LLMs and VLMs. Extensive experiments present that LLMs and VLMs exhibit exceptional
performance in various urban tasks requiring commonsense and
semantic understanding, but fail in challenging urban tasks which
require professional domain knowledge and precise numeric calculations. The extensive results from CityBench demonstrate the
potential the applying LLMs and VLMs in various urban tasks and

CityBench: Evaluating the Capabilities of Large Language Models for Urban Tasks
Mobility Prediction Urba
Task: Infer the <next_place_id>. Task: Choose the op
Requirement: Answer in a JSON object containing direction to get to the
"prediction" and "reason". Requirement: Direc
Logic
Error Llama3-8B Uninformed Int
Answer: … The user has a repeated visit to place 83 Answer: … I apolo
on Saturday morning, and the target stay is also on options provided do
Saturday afternoon, which suggests a high destination. To prov
probability of visiting the same place. either have more info
ensure that the option
Misf
A
o
n
rm
sw
a
e
t
r
te
:
d
**Predic
I
t
n
io
te
n
r
*
n
*
l
:
m
Pl
2
a
.
c
5
e
-
I
7
D
B
1491
Misformatted L
**Reason**: The user has shown a preference for Answer: …Let's
visiting place ID 1491 on Thursdays.… République towards
Invalid
Action
Internlm2.5-20B Refusal
Answer: python import pandas as pd
Answer: …My su
# Define the historical stays
navigation service
history = [ ('07:04 AM', 'Sunday', 158), ('04:51 PM',
platform to get th
'Tuesday', 1148), ('03:38 PM', 'Wednesday', 2710),
directions to your de
('03:37 PM', 'Tuesday', 2710)…
Figure 6: Error analysis in mobility prediction, urban explora
errors, format errors, invalid actions, refusal to answer, and
also shed light for the future research of developing more powerful
LLMs and VLMs for urban tasks.
References
[1] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal
Anadkat, et al. 2023. Gpt-4 technical report. arXiv:2303.08774 (2023).
[2] Michael Batty, Kay W Axhausen, Fosca Giannotti, Alexei Pozdnoukhov, Armando
Bazzani, Monica Wachowicz, Georgios Ouzounis, and Yuval Portugali. 2012.
Smart cities of the future. The European Physical Journal Special Topics 214 (2012),
481–518.
[3] Prabin Bhandari, Antonios Anastasopoulos, and Dieter Pfoser. 2023. Are large
language models geospatially knowledgeable?. In Proceedings of the 31st ACM
International Conference on Advances in Geographic Information Systems. 1–4.
[4] Howard Chen, Alane Suhr, Dipendra Misra, Noah Snavely, and Yoav Artzi. 2019.
Touchdown: Natural language navigation and spatial reasoning in visual street
environments. In CVPR. 12538–12547.
[5] Wei Chen, Yuxuan Liang, Yuanshao Zhu, Yanchuan Chang, Kang Luo, Haomin
Wen, Lei Li, Yanwei Yu, Qingsong Wen, Chao Chen, et al. 2024. Deep learning for
trajectory data management and mining: A survey and beyond. arXiv preprint
arXiv:2403.14151 (2024).
[6] Cheng Deng, Tianhang Zhang, Zhongmou He, Qiyuan Chen, Yuanyuan Shi, Le
Zhou, Luoyi Fu, Weinan Zhang, Xinbing Wang, Chenghu Zhou, et al. 2023. Learning A Foundation Language Model for Geoscience Knowledge Understanding
and Utilization. arXiv preprint arXiv:2306.05064 (2023).
[7] Jingtao Ding, Yunke Zhang, Yu Shang, Yuheng Zhang, Zefang Zong, Jie Feng,
Yuan Yuan, Hongyuan Su, Nian Li, Nicholas Sukiennik, et al. 2024. Understanding
World or Predicting Future? A Comprehensive Survey of World Models. arXiv
preprint arXiv:2411.14499 (2024).
[8] Haodong Duan, Junming Yang, Yuxuan Qiao, Xinyu Fang, Lin Chen, Yuan Liu,
Xiaoyi Dong, Yuhang Zang, Pan Zhang, Jiaqi Wang, et al. 2024. Vlmevalkit: An
open-source toolkit for evaluating large multi-modality models. In Proceedings of
the 32nd ACM International Conference on Multimedia. 11198–11201.
[9] Russell A Epstein, Eva Zita Patai, Joshua B Julian, and Hugo J Spiers. 2017. The
cognitive map in humans: spatial navigation and beyond. Nature neuroscience 20,
11 (2017), 1504–1513.
[10] Zhuangyuan Fan, Fan Zhang, Becky PY Loo, and Carlo Ratti. 2023. Urban visual
intelligence: Uncovering hidden city profiles with street view images. Proceedings
of the National Academy of Sciences 120, 27 (2023), e2220417120.
[11] Jie Feng, Yuwei Du, Jie Zhao, and Yong Li. 2025. AgentMove: A large language
model based agentic framework for zero-shot next location prediction. In NAACL.
[12] Jie Feng, Tianhui Liu, Yuwei Du, Siqi Guo, Yuming Lin, and Yong Li. 2024.
CityGPT: Empowering Urban Spatial Cognition of Large Language Models. arXiv
preprint arXiv:2406.13948 (2024).
[13] Jie Feng, Jinwei Zeng, Qingyue Long, Hongyi Chen, Jie Zhao, Yanxin Xi, Zhilun
Zhou, Yuan Yuan, Shengyuan Wang, Qingbin Zeng, et al. 2025. A Survey of

Submission #15, KDD Datasets and Benchmarks, 2025
ploration Traffic Signal
road and its corresponding Task: Choose the most effective traffic signal option.
ation. Requirement: <signal>YOUR_NUMBER</signal>
ose the option.
2.5-7B
Uninformed Llama3-70B
Answer: …The phase with the lowest waiting
or the confusion, but the vehicle count is Phase Option 1, with 8 waiting
orrespond to the desired vehicles. This suggests that Phase Option 1 will most
seful response, I need to significantly improve the traffic condition during the
n about the destination or next phase.
ided are accurate.
3-8B
Misformatted Gemma2-9B
Answer: …Step 2: Chosen Phase Option\n\nSince
west on Avenue de la all options are equally effective, we can choose any
tination! of them. Let's arbitrarily choose **Phase Option 0**.
2-7B
Invalid
Action
Llama3-8B
tion would be to use a Answer: …Instead, I will recommend that the traffic
oogle Maps or a similar signal controller consider other factors to determine
t accurate and updated the optimal traffic signal phase.
on. **Signal:** <signal>None</signal>
, and traffic signal control tasks reveals common issues: logic
ucinations. Full prompts for each task are in the appendix.
Large Language Model-Powered Spatial Intelligence Across Scales: Advances in
Embodied Agents, Smart Cities, and Earth Science. arXiv preprint arXiv:2504.09848
(2025).
[14] Shuo Feng, Xintao Yan, Haowei Sun, Yiheng Feng, and Henry X Liu. 2021. Intelligent driving intelligence test for autonomous vehicles with naturalistic and
adversarial environment. Nature communications 12, 1 (2021), 748.
[15] Jiahui Gong, Jingtao Ding, Fanjin Meng, Guilong Chen, Hong Chen, Shen Zhao,
Haisheng Lu, and Yong Li. 2024. A population-to-individual tuning framework
for adapting pretrained LM to on-device user intent prediction. In KDD. 896–907.
[16] Wes Gurnee and Max Tegmark. 2023. Language models represent space and time.
arXiv preprint arXiv:2310.02207 (2023).
[17] Lukas Haas, Silas Alberti, and Michal Skreta. 2023. Pigeon: Predicting image
geolocations. arXiv preprint arXiv:2307.05845 (2023).
[18] Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng Cheng, Jinlin Wang, Ceyao
Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, et al. 2023.
Metagpt: Meta programming for multi-agent collaborative framework. arXiv
preprint arXiv:2308.00352 (2023).
[19] Paradox Interactive. 2023. "Cities: Skylines II". "https://www.paradoxinteractive.
com/games/cities-skylines-ii/about"
[20] Neal Jean, Marshall Burke, Michael Xie, W Matthew Davis, David B Lobell, and
Stefano Ermon. 2016. Combining satellite imagery and machine learning to
predict poverty. Science 353, 6301 (2016), 790–794.
[21] Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch, and et al. 2023. Mistral
7B. arXiv preprint arXiv:2310.06825 (2023).
[22] Albert Q Jiang, Alexandre Sablayrolles, Antoine Roux, and et al. 2024. Mixtral of
experts. arXiv preprint arXiv:2401.04088 (2024).
[23] Arne Kesting, Martin Treiber, and Dirk Helbing. 2007. General lane-changing
model MOBIL for car-following models. Transportation Research Record 1999, 1
(2007), 86–94.
[24] Kartik Kuckreja, Muhammad Sohail Danish, Muzammal Naseer, Abhijit Das,
Salman Khan, and Fahad Shahbaz Khan. 2023. Geochat: Grounded large visionlanguage model for remote sensing. arXiv preprint arXiv:2311.15826 (2023).
[25] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng,
Cody Hao Yu, Joseph Gonzalez, Hao Zhang, and Ion Stoica. 2023. Efficient
memory management for large language model serving with pagedattention. In
Proceedings of the 29th Symposium on Operating Systems Principles. 611–626.
[26] Siqi Lai, Zhao Xu, Weijia Zhang, Hao Liu, and Hui Xiong. 2023. Large language
models as traffic signal control agents: Capacity and opportunity. arXiv preprint
arXiv:2312.16044 (2023).
[27] Fan Liu, Delong Chen, Zhangqingyun Guan, Xiaocong Zhou, Jiale Zhu, Qiaolin
Ye, Liyong Fu, and Jun Zhou. 2024. RemoteCLIP: A Vision Language Foundation
Model for Remote Sensing. IEEE TGRS 62 (2024), 1–16.
[28] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. 2024. Visual instruction tuning. Advances in neural information processing systems 36 (2024).
[29] Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu,
Hangliang Ding, Kaiwen Men, Kejuan Yang, et al. 2023. Agentbench: Evaluating

Submission #15, KDD Datasets and Benchmarks, 2025
llms as agents. arXiv preprint arXiv:2308.03688 (2023).
[30] Yu Liu, Jingtao Ding, Yanjie Fu, and Yong Li. 2023. Urbankg: An urban knowledge
graph system. ACM TIST 14, 4 (2023), 1–25.
[31] Pablo Alvarez Lopez, Michael Behrisch, Laura Bieker-Walz, and et al. 2018. Microscopic Traffic Simulation using SUMO, In The 21st IEEE International Conference
on Intelligent Transportation Systems. IEEE ITSC.
[32] Kevin Lynch. 1964. The image of the city. MIT press.
[33] Gengchen Mai, Weiming Huang, Jin Sun, and et al. 2023. On the opportunities
and challenges of foundation models for geospatial artificial intelligence. arXiv
preprint arXiv:2304.06798 (2023).
[34] Gengchen Mai, Krzysztof Janowicz, Rui Zhu, Ling Cai, and Ni Lao. 2021. Geographic question answering: challenges, uniqueness, classification, and future
directions. AGILE: GIScience series 2 (2021), 8.
[35] Rohin Manvi, Samar Khanna, Marshall Burke, David Lobell, and Stefano Ermon. 2024. Large language models are geographically biased. arXiv preprint
arXiv:2402.02680 (2024).
[36] Rohin Manvi, Samar Khanna, Gengchen Mai, Marshall Burke, David Lobell,
and Stefano Ermon. 2023. Geollm: Extracting geospatial knowledge from large
language models. arXiv preprint arXiv:2310.06213 (2023).
[37] Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun,
and Thomas Scialom. 2023. Gaia: a benchmark for general ai assistants. arXiv
preprint arXiv:2311.12983 (2023).
[38] Piotr Mirowski, Matt Grimes, Mateusz Malinowski, and et al. 2018. Learning
to navigate in cities without a map. Advances in neural information processing
systems 31 (2018).
[39] Peter Mooney, Wencong Cui, Boyuan Guan, and Levente Juhász. 2023. Towards
understanding the geospatial skills of chatgpt: Taking a geographic information
systems (gis) exam. In SIGSPATIAL Workshop.
[40] OpenBMB. 2024. MiniCPM-Llama3-V 2.5. https://github.com/OpenBMB/
MiniCPM-V
[41] Xavier Puig, Kevin Ra, Marko Boben, Jiaman Li, Tingwu Wang, Sanja Fidler,
and Antonio Torralba. 2018. Virtualhome: Simulating household activities via
programs. In CVPR. 8494–8502.
[42] Scott Reed, Konrad Zolna, Emilio Parisotto, and et al. 2022. A generalist agent.
arXiv:2205.06175 (2022).
[43] Raphael Schumann, Wanrong Zhu, Weixi Feng, Tsu-Jui Fu, Stefan Riezler, and
William Yang Wang. 2024. Velma: Verbalization embodiment of llm agents for
vision and language navigation in street view. In AAAI.
[44] Zhihong Shao, Damai Dai, Daya Guo, and Bo Liu. 2024. DeepSeek-V2: A Strong,
Economical, and Efficient Mixture-of-Experts Language Model.
[45] Ke Sun, Tieyun Qian, Tong Chen, Yile Liang, Quoc Viet Hung Nguyen, and
Hongzhi Yin. 2020. Where to go next: Modeling long-and short-term user preferences for point-of-interest recommendation. In Proceedings of the AAAI conference
on artificial intelligence, Vol. 34. 214–221.
[46] Mirac Suzgun, Nathan Scales, Nathanael Schärli, Sebastian Gehrmann, Yi Tay,
Hyung Won Chung, Aakanksha Chowdhery, Quoc V Le, Ed H Chi, Denny Zhou,
et al. 2022. Challenging big-bench tasks and whether chain-of-thought can solve
them. arXiv preprint arXiv:2210.09261 (2022).
[47] Andrew J Tatem. 2017. WorldPop, open data for spatial demography. Scientific
data 4, 1 (2017), 1–4.
[48] Hugo Touvron, Louis Martin, Kevin Stone, and et al. 2023. Llama 2: Open
foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288 (2023).
[49] Martin Treiber, Ansgar Hennecke, and Dirk Helbing. 2000. Congested traffic
states in empirical observations and microscopic simulations. Physical review E

Jie Feng et al.
62, 2 (2000), 1805.
[50] Pravin Varaiya. 2013. The max-pressure controller for arbitrary networks of
signalized intersections. In Advances in dynamic network modeling in complex
transportation systems. Springer, 27–66.
[51] Vicente Vivanco Cepeda, Gaurav Kumar Nayak, and Mubarak Shah. 2024. Geoclip:
Clip-inspired alignment between locations and images for effective worldwide
geo-localization. Advances in Neural Information Processing Systems 36 (2024).
[52] Di Wang, Qiming Zhang, Yufei Xu, Jing Zhang, Bo Du, Dacheng Tao, and Liangpei Zhang. 2022. Advancing plain vision transformer toward remote sensing
foundation model. IEEE Transactions on Geoscience and Remote Sensing 61 (2022).
[53] Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang,
Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, et al. 2024. A survey on large
language model based autonomous agents. Frontiers of Computer Science 18, 6
(2024), 1–26.
[54] Ruoyao Wang, Graham Todd, Ziang Xiao, Xingdi Yuan, Marc-Alexandre Côté,
Peter Clark, and Peter Jansen. 2024. Can Language Models Serve as Text-Based
World Simulators? arXiv preprint arXiv:2406.06485 (2024).
[55] Weihan Wang, Qingsong Lv, Wenmeng Yu, Wenyi Hong, Ji Qi, Yan Wang, Junhui
Ji, Zhuoyi Yang, Lei Zhao, Xixuan Song, Jiazheng Xu, Bin Xu, Juanzi Li, Yuxiao
Dong, Ming Ding, and Jie Tang. 2023. CogVLM: Visual Expert for Pretrained
Language Models. arXiv:2311.03079 [cs.CV]
[56] Xinglei Wang, Meng Fang, Zichao Zeng, and Tao Cheng. 2023. Where would i
go next? large language models as human mobility predictors. arXiv preprint
arXiv:2308.15197 (2023).
[57] Hua Wei, Guanjie Zheng, Vikash Gayah, and Zhenhui Li. 2019. A survey on
traffic signal control methods. arXiv preprint arXiv:1904.08117 (2019).
[58] Jason Wei, Yi Tay, Rishi Bommasani, and et al. 2022. Emergent abilities of large
language models. arXiv:2206.07682 (2022).
[59] Jiannan Xiang, Tianhua Tao, Yi Gu, Tianmin Shu, Zirui Wang, Zichao Yang, and
Zhiting Hu. 2024. Language models meet world models: Embodied experiences
enhance language models. NeurIPS (2024).
[60] Yibo Yan, Haomin Wen, Siru Zhong, and et al. 2024. UrbanCLIP: Learning Textenhanced Urban Region Profiling with Contrastive Language-Image Pretraining
from the Web. In The Web Conference 2024.
[61] Dingqi Yang, Daqing Zhang, and Bingqing Qu. 2016. Participatory cultural
mapping based on collective behavior data in location-based social networks.
ACM Transactions on Intelligent Systems and Technology (TIST) 7, 3 (2016), 1–23.
[62] Jihan Yang, Runyu Ding, Ellis Brown, Xiaojuan Qi, and Saining Xie. 2024. V-IRL:
Grounding Virtual Intelligence in Real Life. arXiv:2402.03310 (2024).
[63] Mengjiao Yang, Yilun Du, Kamyar Ghasemipour, Jonathan Tompson, Dale Schuurmans, and Pieter Abbeel. 2023. Learning interactive real-world simulators.
arXiv preprint arXiv:2310.06114 (2023).
[64] Christopher Yeh, Anthony Perez, Anne Driscoll, George Azzari, Zhongyi Tang,
David Lobell, Stefano Ermon, and Marshall Burke. 2020. Using publicly available
satellite imagery and deep learning to understand economic well-being in Africa.
Nature communications 11, 1 (2020), 2583.
[65] Jirong Zha, Yuxuan Fan, Xiao Yang, Chen Gao, and Xinlei Chen. 2025. How to
Enable LLM with 3D Capacity? A Survey of Spatial Reasoning in LLM. IJCAI
(2025).
[66] Huichu Zhang, Siyuan Feng, Chang Liu, and et al. 2019. Cityflow: A multi-agent
reinforcement learning environment for large scale city traffic scenario. In The
world wide web conference. 3620–3624.
[67] Yu Zheng, Licia Capra, Ouri Wolfson, and Hai Yang. 2014. Urban computing:
concepts, methodologies, and applications. ACM Transactions on Intelligent
Systems and Technology (TIST) 5, 3 (2014), 1–55.

CityBench: Evaluating the Capabilities of Large Language Models for Urban Tasks
A Appendix
A.1 Few-Shot Performance of LLMs in
CityBench
Here, we present the few-shot performance of several representative
LLMs in Beijing in the Table 4. For all text-based tasks, we use 2-shot
as the default few-shot method. As shown in the table, the impact
of few-shot learning varies across different models and tasks. For
instance, few-shot learning improves performance for Gemma-27B
in GeoQA but reduces it for Gemma2-9B on the same task. Similarly,
it benefits Gemma2 in traffic signal tasks but proves detrimental
for Llama3.
A.2 Details of Quality Control
In CityBench, the authors will participate in the quality control
process for some tasks, following the automatic quality control
stage. Taking the manual checking of GeoQA as an example, the
original data from OpenStreetMap contains low-quality information, with missing or incorrect details about AOI, POI, and roads.
When this low-quality data is used in the evaluation task, LLMs may
become confused and generate meaningless answers. In such cases,
the authors review the questions to ensure that the information
in the context is meaningful. However, due to time limitations for
participants, we can only randomly sample the evaluation cases.
For instances from cities and regions where authors are unfamiliar, we filter out low-quality instances. For instances from cities
and regions where authors are familiar, we rewrite low-quality
instances using external information, such as commercial map services. Finally, if data quality remains unsatisfactory after filtering
and rewriting, we will regenerate a certain number of cases to fill
the gaps. In fact, while considering the probabilities of filtering, we
generate enough candidate instances during the initial generation.
A.3 Additional Results of Geospatial Bias
Analysis
Taking three well-performing cities (New York, London, Paris) and
three under-performing cities (Shanghai, CapeTown, Nairobi) as
examples, Table 5 illustrates the relationship between the performance of street view image localization tasks and the size of the
training corpus for LLMs. The training corpus size is approximated
by the number of Google search entries and Wikipedia entries
for each city. Compared to the well-performing cities, the underperforming cities have significantly smaller ‘training corpora’ in
the public websites. Additionally, open-source models exhibit significantly worse performance than commercial models in terms
of geospatial bias. This observation provides initial evidence for
analyzing geographical bias, but we believe there are more diverse
factors contributing to this phenomenon.

Submission #15, KDD Datasets and Benchmarks, 2025
A.4 Error Analysis of VLMs
Urban visual tasks require the model to make decisions directly
without going through an explanation process. As a result, as shown
in Figure 7, common errors include format errors, invalid actions,
refusal to answer and hallucinations. In the image geolocalization
task, InternVL2-2B provides a response that do not follow the required format, while Yi-VL-34B gives an irrelevant invalid response.
CogVLM2-19B and Yi-VL-34B, in the geospatial prediction and
infrastructure inference tasks respectively, repeat the examples
provided in the question and refuse to answer the actual question.
Due to the response format requirements of the tasks, the most
common error made by VLMs in urban visual tasks is misformatted
responses.
A.5 Map building tool in CityData
The map building tool 9 enhances open-source map data to support
subsequent behavior simulations, encompassing lane topology recovery, relationship recognition, intersection reconstruction, area
of interest (AOI) mapping, point of interest (POI) clustering, basic
traffic rule generation, and right-of-way construction.
A.6 Discussion
We discuss some limitation of current work as below.
Limitations. While our platform is based on the public data from
various sources, the quality of different data may play a important
role in the evaluation results. In the future, we plan to collect more
kinds of tasks with global scale groundtruth data to further improve
the reliability and representativeness of benchmark.
Ethical considerations and potential societal impact. Our
benchmark is designed for enable the global evaluation of LLMs
and VLMs for various cities with different cultures and countries.
We try our best to improve the ease-of-use and fairness for cities
with different development levels. However, due to the limitation
of accessed data, the evaluation results for different cites varies a
lot. Therefore, the variation in evaluation results caused by data
quality may lead to a certain degree of misunderstanding regarding the performance on some urban problems. We call the whole
community for attention to this issue to improve the usability of
LLMs across different races and countries, promoting fairness and
sustainable development of the world.
Develop foundation model for urban domain. Based on the
results of our benchmark, we find existing LLMs perform poorly
on many urban tasks, even worse than some classic simple baseline
algorithms. Developing LLMs tailored for urban domain is urgently
necessary. We hope our benchmark can accelerate this development and we look forward to a more comprehensive and robust
evaluation framework for urban domain.
9https://github.com/tsinghua-fib-lab/mosstool

Submission #15, KDD Datasets and Benchmarks, 2025 Jie Feng et al.
Table 4: Few-shot performance of several representative LLMs in Beijing.
GeoQA Mobility Prediction Urban Exploration Traffic Signal
Model@Beijing
Accuracy Top1 Acc F1 Succ Rate Steps Throughput Travel Time Queue Length
Gemma2-9B-fewshot 0.306 0.115 0.101 0.728 6.152 1528 2129.21 64.269
Gemma2-9B-zeroshot 0.339 0.131 0.120 0.716 5.679 1448 2214.451 71.729
Gemma2-27B-fewshot 0.359 0.109 0.076 0.696 6.260 2240 1746.89 31.683
Gemma2-27B-zeroshot 0.349 0.145 0.118 0.713 5.733 2187 1762.182 33.322
LLama3-8B-fewshot 0.288 0.095 0.0546 0.692 6.424 1547 2132.233 61.84
LLama3-8B-zeroshot 0.297 0.130 0.094 0.747 5.304 2128 1873.757 40.941
Llama3-70B-fewshot 0.343 0.089 0.0620 0.796 4.941 1810 1962.493 50.541
Llama3-70B-zeroshot 0.329 0.159 0.130 0.74 5.876 2031 1893.517 43.475
Table 5: The performance of street view image localization tasks in different cities and its relationship with the amount of data
in the ‘training corpus’ of LLMs, where the amount of data in the training corpus is approximated by the number of Google
search entries and Wikipedia entries for each city.
Cities GPT4o MiniCPM-V2.5 Google Search Pages Wikipedia Pages
Shanghai 59% 0.4% 582,000,000 62,495
CapeTown 81% 0 587,000,000 54,724
Nairobi 58.19% 0 205,000,000 14,226
New York 94.39% 80% 7,070,000,000 1,039,264
London 88.80% 43.8% 5,460,000,000 848,381
Paris 92.80% 49% 4,170,000,000 353,500
Image Geolocalization Geospatial Prediction Infrastructure Inference
Task: Infer city name and location of the image. Task: Analyze the population density of the image. Task: Choose the infrastructure type of the image.
Requirement: Only answer with the city name and Requirement: ‘My answer is X.X.’, where ‘X.X’ Requirement: ‘My answer is X, Y, ... and Z.’where ‘X,
location. Do not output any explanational sentences. represents your rating of the population density. Y, ... and Z’ represent the infrastructure types.
Refusal InternVL2-2B Refusal CogVLM2-19B Refusal Yi-VL-34B
Answer: … Given the lack of clear geographical Answer: My answer is X.X. Answer: My answer is X, Y, ... and Z.
markers, it is challenging to accurately determine the
city and its location. Therefore, I cannot provide a
specific city name and location. Misformatted InternVL2-2B Misformatted CogVLM2-19B
Answer: My answer is 7.7. Answer: Based on the image provided, the identified
Misformatted InternVL2-2B E
m
x
ix
pla
o
n
f
a
g
ti
r
o
ee
n
n
: T
sp
h
a
e
ce
i
s
m
a
a
n
g
d
e
d
s
e
h
v
o
e
w
lo
s
p
a
ed
la
a
r
r
g
e
e
as
a
.
r
T
ea
he
w
g
i
r
th
een
a i
-
nf
R
ra
o
s
u
t
n
ru
d
c
a
t
b
u
o
re
u t
t
,
y
-
p
S
es
to
a
r
r
a
e
g
:
e
-
T
G
a
r
n
o
k
u
,
n
-
d
T
T
en
ra
n
c
i
k
s C
Fi
o
e
u
ld
rt
,
…
Answer: The image appears to be taken in Beijing, areas appear to be more densely packed, indicating a
China. The longitude and latitude value of its location higher population density. …
Inval
i
i
s
d
a p
A
p
c
ro
ti
x
o
i
n
mately 39.
Y
71
i
2
-V
8°
L
N
-
,
3
1
4
1
B
6.3276° E.
Invali
A
d
n
A
sw
ct
e
i
r
o
:
n
…There
Q
fo
w
re
e
:
n
M
V
y
L P
a
l
n
u
s
s
wer is N/A (Not
Inval
A G
id
n r o
A
s u w
c
n e
t
d
i
r
o
:
n
T M rac y k a F n
Q
s ie w
w
ld e , r
en
B i
2
s r
V
id O
L
g v
-
e
2
, er
B
p S a t s a s d , iu R m o , un A da ir b p o o u r t t , ,
Baseball Field, Roundabout, Overpass, Stadium,
Answer: Ho Chi Minh City Applicable). Airport, Baseball Field, Roundabout…
Figure 7: Error analysis in image geolocalization, geospatial prediction and infrastructure inference tasks.
Table 6: Detailed information of 8 evaluation tasks in CityBench, including data modality, metric and data instances. Task
settings across different cities keep consistent.
CityBench Tasks Modality Metrics Instances Images
Image Geolocalization Image Acc, Acc@1km/25km 6500 6500
Perception& Geospatial Prediction Image 𝑟2, RMSE 5739 5739
Understanding Infrastructure Inference Image Accuracy, Recall 5739 5739
GeoQA for City Elements Text Accuracy 13126 /
Mobility Prediction Text Top1-Acc, F1 6500 /
Planning& Urban Exploration Text Steps, Success Rate 650 /
Decision Making Outdoor Navigation Image Distance, Steps, Success Rate 650 55984
Traffic Signal Control Text Queue Length, Throughput 1hour × 13 cities /
