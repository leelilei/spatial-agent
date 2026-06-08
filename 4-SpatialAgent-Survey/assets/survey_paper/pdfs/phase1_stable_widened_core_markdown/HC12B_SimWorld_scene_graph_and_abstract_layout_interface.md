# HC12B - SimWorld: scene-graph and abstract-layout interface

## Stable Widened-Core Snapshot

- core_layer: `anchor_core`
- admission_status: `stable_anchor`
- corpus_tier: `Core`
- system_family: `SimWorld`
- paper_refs: `SimWorld2025`
- year: `2025`
- agent_count: `2-10`
- environment_side_representation: `3D_engine`
- agent_accessible_representation: `L3`
- behavioral_scale: `mixed`
- behavior_type: `cooperation; conflict; mobility; other`
- evidence_status: `designed_affordance_only`
- spatial_behavior_coupling: `explicit`
- evaluation_method: `auto_metric`
- space_syntax_construct: `none`
- source_basis: `local_pdf_ocr_and_adjudication_memo`
- artifact_class: `local_pdf`

## Representation Gap Note

This split row captures the structured interface where observations are abstracted into scene graphs or layouts without requiring the agent to act on full geometry directly.

## Original Artifact Pointer

- local_artifact_path: `assets/survey_paper/pdfs/phase1_core/12_HC12_SimWorld.pdf`

## Source Content

Title: SimWorld: An Open-ended Realistic Simulator for Autonomous Agents in Physical and Social Worlds

Source PDF: D:\0-AI相关研究\1-spatialagent\spatial-agent\assets\survey_paper\pdfs\phase1_core\12_HC12_SimWorld.pdf

Extraction:
- backend: pypdf
- extracted_at_utc: 2026-04-28T16:32:54+00:00
- page_count: 24
- status: ok
- text_char_count: 78568

Metadata:
- author: Jiawei Ren; Yan Zhuang; Xiaokang Ye; Lingjun Mao; Xuhong He; Jianzhi Shen; Mrinaal Dogra; Yiming Liang; Ruixuan Zhang; Tianai Yue; Yiqing Yang; Eric Liu; Ryan Wu; Kevin Benavente; Rajiv Mandya Nagaraju; Muhammad Faayez; Xiyan Zhang; Dhruv Vivek Sharma; Xianrui Zhong; Ziqiao Ma; Tianmin Shu; Zhiting Hu; Lianhui Qin
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 3)
- The SimWorld Simulator (page 4)
  - Unreal Engine Backend (page 4)
    - Diverse Scenes (page 5)
    - Rich Assets and Physics Realism (page 6)
  - Environment (page 8)
    - Procedural City Generation (page 8)
    - LLM-based Scene Editing (page 9)
    - Waypoint System (page 9)
    - Traffic System (page 10)
    - Gym-like Interface for Agent-Environment Interaction (page 11)
  - Agent (page 12)
    - Agent Framework (page 12)
    - Observation Space (page 12)
    - Action Space (page 12)
    - Action Planner (page 13)
  - UnrealCV+ Communication Module (page 15)
- Case Study: Delivery Task (page 15)
  - Task Formulation (page 15)
  - Main Results (page 16)
  - Ablation Study (page 17)
- Related Works (page 20)

Markdown Content:

Technical Report
SimWorld: An Open-ended Realistic Simulator for
Autonomous Agents in Physical and Social Worlds
Jiawei Ren1* Yan Zhuang2* Xiaokang Ye1* Lingjun Mao1 Xuhong He3 Jianzhi Shen4
Mrinaal Dogra1 Yiming Liang5 Ruixuan Zhang4 Tianai Yue4 Yiqing Yang6 Eric Liu7 Ryan Wu4
Kevin Benavente1 Rajiv Mandya Nagaraju7 Muhammad Faayez4 Xiyan Zhang4
Dhruv Vivek Sharma1 Xianrui Zhong3 Ziqiao Ma8 Tianmin Shu4† Zhiting Hu1† Lianhui Qin1†
1UCSD 2UVA 3UIUC 4JHU 5Purdue 6PolyU 7USC 8UMich
https://simworld.org
Social InteractionTraffic
Open-endedness
Realistic Simulation
DiverseUse
LLM/VLM agents in SimWorld
Open-ended Environment
Large-scale SimulationReal-world Planning
Recorded FPV Video
RotationData SynthesisPositionAction
Open-ended Action
Physics
Diverse ScenesText-to-3D Generation
Robots
Spawna taxi car
collision
replanning
Figure 1:An Overview of theSimWorldSimulator, featuring three key designs: (1) realistic, open-ended
world simulation, (2) rich interface for LLM/VLM agents, and (3) diverse physical and social reasoning scenarios.
* Equal contribution;†Equal advising
arXiv:2512.01078v2  [cs.AI]  22 Jan 2026

While LLM/VLM-powered AI agents have advanced rapidly in math, coding, and computer use, their
applications in complex physical and social environments remain challenging. Building agents that can
survive and thrive in the real world (e.g., by autonomously earning income or running a business) requires
massive-scale interaction, reasoning, training, and evaluation across diverse embodied scenarios. However,
existingworldsimulatorsforsuchdevelopmentfallshort: theyoftenrelyonlimitedhand-craftedenvironments,
simulate simplified game-like physics and social rules, and lack native support for LLM/VLM agents. We
introduceSimWorld, a new simulator built on Unreal Engine 5, designed for developing and evaluating
LLM/VLM agents in rich, real-world-like settings.SimWorldoffers three core capabilities:(1) realistic,
open-ended world simulation,includingaccuratephysicalandsocialdynamicsandlanguage-drivenprocedural
environment generation;(2) rich interface for LLM/VLM agents, with multi-modal world inputs/feedback
and open-vocabulary action outputs at varying levels of abstraction; and(3) diverse extensible physical and
social reasoning scenariosthat are easily customizable by users. We demonstrateSimWorldby deploying
frontier LLM agents (e.g.,GPT-4o, Gemini-2.5-Flash, Claude-3.5, and DeepSeek-Prover-V2) on
long-horizon multi-agent delivery tasks involving strategic cooperation and competition. The results reveal
distinct reasoning patterns and limitations across models. We open-sourceSimWorldand hope it becomes a
foundational platform for advancing real-world agent intelligence across disciplines: https://simworld.org.
Table of Contents
1 Introduction 3
2 TheSimWorldSimulator 4
2.1 Unreal Engine Backend . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.1.1 Diverse Scenes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.1.2 Rich Assets and Physics Realism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 Environment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2.1 Procedural City Generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2.2 LLM-based Scene Editing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.2.3 Waypoint System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.2.4 Traffic System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.2.5 Gym-like Interface for Agent-Environment Interaction . . . . . . . . . . . . . . . . . . 11
2.3 Agent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3.1 Agent Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3.2 Observation Space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3.3 Action Space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3.4 Action Planner . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.4 UnrealCV+ Communication Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3 Case Study: Delivery Task 15
3.1 Task Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.2 Main Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.3 Ablation Study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4 Related Works 20
2

1. Introduction
Large language and vision models (e.g., LLMs and VLMs) have emerged as powerful foundations for building
intelligent agents, demonstrating remarkable reasoning capabilities, particularly in structured domains such as
mathematics, coding, and computer use (e.g., web browsing). However, thesemathematicalanddigitalsettings
are relatively clean, with well-defined rules and clear feedback. In contrast, the embodiedphysicalandsocial
worlds, where real-world agents and robots are ultimately expected to operate, are inherently complex, noisy,
dynamic, and unpredictable. In such environments, agents must interact with rich and evolving contexts, from
navigating urban spaces and interacting with humans, to pursuing long-term goals such as earning a living,
building a career, or running an organization (Brohan et al., 2023; Driess et al., 2023; Wang et al., 2023).
To advance embodied agent development, recent efforts haveexploredsimulation environmentsthat offer different
interactiveexperiencesfortrainingandevaluation(Table1). However,game-likeplatformssuchasMinecraft(Fan
et al., 2022; White et al., 2025; Wang et al., 2023; Long et al., 2024; Liu et al., 2024; Li et al., 2025b) and
Pokémon (Ha, 2025; Anthropic, 2025) provide accessible setups for embodied interaction but lack realistic
physical dynamics and social structures, limiting real-world generalization. Domain-specific simulators such
as CARLA (Dosovitskiy et al., 2017) and AI2-THOR (Kolve et al., 2017) target areas like autonomous driving
and household robotics but are limited to narrow task scopes or static environments. Social sandboxes such
as Virtual Village (Park et al., 2023) and Project Sid (AL et al., 2024) simulate interpersonal interactions in
scripted, small-scale communities, but lack the open-endedness and scalability required for modeling richer social
complexity. Moreover, many of these environments do not support natural language interfaces for goal setting,
planning, and control, limiting their compatibility with modern LLM-based agents.
To meet these growing demands, we presentSimWorld, a platform designed to support the development and
evaluation of autonomous agents in complex, dynamic, and interactive environments.SimWorldis grounded in
three core design principles (Figure 1):
1)Realistic, Open-Ended World Simulation.SimWorldadvances simulation by integrating two key aspects:
realisticphysical and social dynamics, andopen-ended, language-steerableworld generation. On the realism
side,SimWorldproduces complex, dynamic environments grounded in physical laws (e.g., gravity, momentum)
and enriched with dynamic elements such as lighting, weather, and pedestrian flow in city-scale 3D scenes.
It also embeds socially grounded behaviors, such as obeying traffic signals and maintaining personal space,
directly into agent logic to support realistic interactions. On the open-ended side,SimWorldoffers a broad
range of scenes (e.g., city, countryside, wilderness, islands) and supports infinite environment expansion through
procedural generation, including diverse road networks, building layouts, and urban configurations. Moreover,
usersorAIagentscanmodifysceneson-the-flyvianaturallanguageprompts(e.g.,“ add a tree next to the
hospital”). Powered bySimWorld’s LLM-based editing and asset-generation modules, this capability enables
adaptive, interactive world creation.
2)Rich Interface for LLM/VLM Agents.SimWorldprovides aGym-like interfacethat enables LLM/VLM
agents to interact with simulated worlds usingopen-ended natural language actions. Agents can perceive rich
multimodal observations (e.g., visual scenes, abstract layouts, and action feedback) and respond with high-level
language commands. For example, an agent may reason and generate an abstract action, “sit on the nearest
chair,” whichSimWorldautomatically decomposes into a sequence of low-level actions (e.g., navigating
through waypoints, sitting down). After executing the actions, the simulator provides updated observations and
feedback, allowing the agent to refine its strategy and continue reasoning. This closed-loop interaction supports
open-ended, language-driven behaviors and empowers agents to perform long-horizon reasoning at a proper
abstraction level.
3)Diverse Physical and Social Reasoning Scenarios.Building on the above physically and socially grounded
environments and the agentic interface,SimWorldnaturally supports systematic evaluation and training of agent
reasoning in diverse realistic, long-horizon settings. Beyond short, task-oriented behaviors, agents can pursue
extended objectives such as earning money, developing a career trajectory, or running a multi-agent business,
where strategic decisions compound over time and social dynamics influence outcomes. To illustrate how these
capabilities integrate in practice, we showcase aDelivery Task, a case study demonstrating how physical and
social reasoning jointly lead to multi-agent collaboration and competition inSimWorld. The task models an
urban delivery economy in which agents bid, invest, and share orders while navigating dynamic environments.
3

Table 1:Comparison ofSimWorldand Existing Simulatorsacross key dimensions:Open-ended World
(proceduralscene/assetgeneration, language-controllableediting),Physical/SocialRealism(fidelitytoreal-world
mechanics),Action Space(action abstraction level, open-vocabulary action space),Agent Type(types of
controllable agents: Humanoid (Hum.), Robot, Drone or Vehicle (Veh.)), andPhysics Engine(underlying
simulation engine). H means high-level actions (e.g., “deliver”, “navigate to ”), and L means low-level
actions (e.g., “forward by 1 step”).
Simulator Open-ended World Physical/Social
Realism
Action Space Agent Type Physics Engine
Procedural Lang.-Ctrl Abstr. Open-Vocab
Minedojo (Fan et al., 2022)✓ ✗+ L✗Hum. Minecraft
Mindcraft (White et al., 2025)✓ ✗+ H✗Hum. Minecraft
MetaUrban (Wu et al., 2025)✓ ✗++ L✗Veh. PyBullet
EmbodiedCity (Gao et al., 2024)✗ ✗+++ L✗Drone/Veh. Unreal Engine
CARLA (Dosovitskiy et al., 2017)✗ ✗+++ L✗Veh. UE & Unity
GRUtopia (Wang et al., 2024a)✗ ✗++ L✗Hum./Robot Isaac Sim
OmniGibson (Li et al., 2024)✗ ✗++ H/L✗Robot Omniverse
AI2-THOR (Kolve et al., 2017)✓ ✗++ L✗Robot Unity
Habitat 3.0 (Puig et al., 2023)✗ ✗++ L✗Hum./Robot Bullet
Genesis (Authors, 2024)✓ ✗+++ L✗Robot Taichi
VirtualCommunity (Zhou et al., 2025)✓ ✗++ L✗Hum./Robot Genesis
UnrealZoo (Zhong et al., 2025)✗ ✗+++ L✗Hum./Robot/Veh. Unreal Engine
SimWorld✓ ✓+++ H/L✓Hum./Robot/Veh. Unreal Engine
With different personas, budgets, and tools (e.g., vehicles), agents develop diverse strategies shaped by their goals
and changing conditions (e.g., fluctuating prices). The task highlights complex decision-making and long-horizon
planning, where cooperation, competition, and emergent social behaviors arise naturally.
We deploy frontier LLMs as agents such asGPT-4o, Claude-3.5-Sonnet, Gemini-2.5-Flash, and others on
theDelivery Task. We observe thatClaude-3.5-Sonnetand DeepSeek-V3earn the highest profits, but often
behave erratically, such as overbidding on low-value orders or spending all their money on scooters they never use.
In contrast,Gemini-2.5-Flash and DeepSeek-Prover-V2 follow more conservative, stable strategies, trading
peak performance for consistency. Personality traits also shape agent behavior: conscientious agents focus on
task completion, while open agents explore but frequently lose money. These findings expose both the strengths
and limitations of LLM-based agents, while revealing rich, often unexpected behaviors that emerge from their
interaction with complex environments.
We open-sourceSimWorldwith the aim of establishing a foundational infrastructure for real-world agent
research across disciplines. By supporting advanced LLM/VLM-based agents and enabling large-scale, realistic
agent–environment and agent–agent interactions,SimWorldexpands the capabilities of modernagent-based
simulation (ABS). This allows researchers in robotics, business, public health, social science, education, and
beyond to study complex systems and emergent behaviors in rich, dynamic, and controllable environments. More
details of theSimWorldproject are available at https://simworld.org.
2. TheSimWorldSimulator
Realistic,open-ended,andnativelyLLM/VLM-compatiblesimulatorsarecrucialforadvancingagentdevelopment
incomplexphysicalandsocialscenarios.SimWorldtakesasteptowardthisgoalthroughathree-tierarchitecture
as illustrated in Figure 2. It separates theUnreal Engine Backend(§2.1) from two added Python layers: the
Environmentlayer providing infinite environment generation and standard Gym-like environment-agent interface
(§2.2), and theAgentlayer supporting diverse input observations, open-ended output actions, and different
reasoning/planning components (§2.3). In addition, theUnrealCV+communication module enables seamless
interaction between the Unreal Engine backend and the Environment layer (§2.4).
2.1. Unreal Engine Backend
The Unreal Engine backend forms the foundation ofSimWorld, providing high-fidelity rendering and physics
simulation. It consists of three tightly coupled modules: (1)Scenes(§2.1.1) supporting both procedurally
generated and curated maps; (2)Asset Library(§2.1.2) ensuring diverse and physically grounded content; and
4

Environment
(Python)
Unreal
Engine
Backend
(C++)
Asset Library Physics Simulation
Traffic
Simulation
Execute
Action
Get
Observation
Agent
(Python)
Import
Text-to-3D
Object Assets
UE marketplace
Traffic System
Add
Details
Procedural Generation
Scene
Generation
Observation
Character Assets
Scenes
LLM/VLM Backend
Effect Assets
UnrealCV+
(TCP)
Animation Assets
Action Planner
Gym-like Interface
def agent_thread(agent):
    def step(action):
         env.execute(action)
         obs = env.get_observation()
Scene Editing
Place a tree to the
right of the hospital.
Agent Framework
World
Model
Memory
Mental
State
History
Step 45: Pick up
Step 44: Move to (-8, 10)
Step 43: Turn left 75°
…
…Sensors
root
road 1st Avanue 2nd Street
building school
Scene Graph
 GPS
Observation Action
Perception
Reasoning
Planning
Figure 2:Architecture ofSimWorld.SimWorldadopts a hierarchical, closed-loop architecture that decouples
agent reasoning from high-performance rendering while maintaining coherent information flow across modules.
Atitscore,theUnreal Engine Backendprovideshigh-fidelityscenes,assets,andphysics,servingasthefoundation
for realistic simulation. Built upon it, theEnvironmentlayer functions as an intermediary that abstracts the
underlying rendering and physics into structured representations. It enables procedural city generation, traffic
simulation, and exposes a Gym-like interface for agent interaction throughUnrealCV+. TheAgentlayer operates
on this interface, integrating LLM/VLM agents that interpret observations from theEnvironment, perform
reasoning, and issue actions that are subsequently executed through theEnvironment’s connection to theUnreal
Engine Backend, thereby forming a closed perception–planning-action loop.
(3)Physics Simulation(§2.1.2) governing realistic physical behaviors.
2.1.1. Diverse Scenes
SimWorldsupports two scene-building modes: handcrafted scenes and procedurally generated scenes.
Handcrafted Scenes.Thanks toSimWorld’s foundation in Unreal Engine, users can easily import a large
collection of high-quality environments directly from the Unreal Engine Marketplace1 or create custom scenes by
1https://www.fab.com/
5

Figure 3:Example Scenes inSimWorld.
hand. In our current implementation, we curate over 100 handcrafted scenes2 spanning a wide variety of visual
and structural styles, from ancient towns and natural landscapes to futuristic cities and imaginative fantasy worlds.
Eachsceneprovidesdistinctvisualcues, spatiallayouts, andinteractionaffordances, enablingthoroughevaluation
of embodied agents across diverse settings. Figure 3 illustrates several examples.
Procedurally Generated Scenes.Complementing these handcrafted assets,SimWorldfeatures a procedural
generation module for automatically constructing diverse urban environments. Users can specify high-level
parameters (e.g., city size, road density, layout style), and the system generates large numbers of city variants
efficiently and consistently. This supports scalable experimentation under controlled, customizable conditions.
Additional details are provided in Section 2.2.1.
By combining high-fidelity handcrafted scenes with flexible procedural generation,SimWorldoffers a broad and
extensible set of environments suitable for both controlled experiments and open-ended agent research.
2.1.2. Rich Assets and Physics Realism
SimWorldprovides a comprehensive asset library to support realistic, physics-driven simulations across diverse
environments. The system integrates static assets (e.g., buildings) and dynamic assets (e.g., pedestrians), and
further incorporates environmental factors (e.g., lighting, weather) to create immersive virtual worlds. It also
supports a wide range of animations and interactions, enabling agents to perform diverse actions faithfully within
the environments.
Object Assets.The object asset library forms the structural backbone ofSimWorldenvironments, where each
scene can be viewed as a composition of multiple object assets. These assets include detailed material definitions
and collision meshes, enabling a wide range of physically accurate interactions such as reflection, occlusion,
and contact dynamics. Overall, they can be broadly grouped into three categories: (i)Building assets:Primary
2TheSimWorldrelease includes all scenes as executable builds, available athttps://github.com/SimWorld-AI/SimWorld.
6

Vehicle HumanRobot
Figure 4:Embodied Agents.SimWorldsupports three types of agent embodiments: vehicle, robot, and human.
structural elements of urban scenes, covering a wide range of architectural types (e.g., residential, commercial,
industrial) and supporting both indoor and outdoor environment construction. (ii)Vegetation assets:Natural
elements such as trees, grass, and shrubs, modeled with realistic material appearance and optional seasonal
variations. (iii)Urban prop assets:Fine-grained objects such as benches, mailboxes, lampposts, and traffic signs,
enabling diverse agent interactions such as sitting, opening, or manipulating objects.
Text-to-3D Asset Generation.To further expand the range of available objects,SimWorldintroduces an
Asset Generation Pipelinebased on recent Text-to-3D models (Hunyuan3D, 2025). This system allows users
to describe assets in natural language, automatically generating 3D objects with consistent scale, texture, and
physical properties. The generated assets can be seamlessly integrated into the simulator, inheriting various
properties (e.g., materials, lighting, collision configurations) compatible with UE’s physics engine.
Characters and Embodiments.Character assets inSimWorldrepresent embodied entities capable of acting,
navigating, and interacting within the virtual environment. The system supports three primary types of agent
embodiments: human, vehicle, and robot (Figure 4). Human embodiments capture diverse human appearances
and employ fully rigged skeletal structures that enable realistic animations produced through coordinated
bone articulation, such as running or carrying objects. Vehicle embodiments reproduce a range of real-world
transportation modes (e.g., buses, cars) and implement accurate physical driving dynamics, such as acceleration,
steering,braking,andtraction. Roboticembodimentsmodelspecificcategoriesofrobots(e.g.,quadrupedsystems)
with realistic actuation, joint control, and sensing modules, making them suitable for evaluating robot locomotion
and stability across different environments and tasks. All these embodiments operate within a unified physics
framework and share common attributes (e.g., mass, inertia, contact forces), which ensures consistent handling of
physical properties and interactions across all entities.
Weather and Lighting.SimWorldsupports a wide range of lighting and weather conditions. The lighting
system models multiple light types (e.g., directional, ambient, and dynamic sources) with controllable parameters
such as intensity, orientation, and color temperature. The weather system supports a variety of conditions (e.g.,
rain, snow, and fog) that influence visual appearance and drive atmospheric effects, including phenomena like
fog-induced light scattering. Together, these components recreate the complexity and dynamism of real-world
environments, enabling the study of embodied agents’ perception and adaptation under realistic conditions.
Physical Dynamics and Animations.Powered by Unreal Engine,SimWorldprovides accurate and continuous
physical simulation. Unlike popular agent environments such as Minecraft (Fan et al., 2022; Yu et al., 2024),
which rely on discrete, block-based mechanics without real gravity or inertia,SimWorldmodels real-world
physicaldynamics. Agentsaresubjecttophysicalforcesthatproducegroundedbehaviorslikeslidingdownslopes
or tripping over steps. These effects produce physically grounded, embodied interactions. By combining Unreal
Engine’s physics engine with physically informed animations (e.g., motion blending, inverse kinematics, collision
responses),SimWorldmaintains coherence between motion and environmental forces, enabling believable and
adaptable agent behaviors in complex environments.
7

Algorithm 1Procedural City Layout Generation using QuadTree
1:Input:Configuration parametersconf ig
2:Output:Final QuadTreeQ city representing the city layout
3:Initialize empty QuadTreeQ city
4:ifs=roadthen
5:Generate road network via growth-based model▷Procedural street expansion
6:Insert road geometries intoQ s ▷Store road segments
7:MergeQ s intoQ city ▷Integrate road layout
8:ifs=buildingthen
9:Sample building candidates (orientation, position)
10:Reject invalid samples by collision test▷Spatial consistency filtering
11:Greedy fill remaining gaps with valid buildings
12:Insert buildings intoQ s
13:MergeQ s intoQ city ▷Integrate building layout
14:ifs=street elementthen
15:Sample decorative/environmental elements
16:Reject overlapping samples by collision test
17:Insert detail elements intoQ s
18:MergeQ s intoQ city ▷Integrate street-level details
19:returnQ city
2.2. Environment
SimWorldintroduces an environment layer on top of the Unreal Engine backend (Figure 2). This layer manages
the creation and organization of simulated environments and provides a clean abstraction that enables easy
deployment of agents into Unreal Engine–based worlds through AI-native, user-friendly interfaces, without
requiring users to handle the complexities of the underlying UE system. Specifically, the environment layer
integrates modules for Procedural City Generation (§2.2.1), LLM-based Scene Editing (§2.2.2), Traffic Systems
(§2.2.4), and, crucially, aGym-likeInterface(§2.2.5)foragent–environmentinteraction. Italsooffersanauxiliary
Waypoint System (§2.2.3) that simplifies agent navigation within complex worlds.
2.2.1. Procedural City Generation
Previous simulators typically rely on a limited set of hand-crafted scenes (e.g., 15 scenes in CARLA and 211
scenes in Habitat 3.0).SimWorlddevelops a procedural generation system (Figure 5a) capable of producing
diverse,unlimitedurbanenvironments,includingroadnetworks,buildinglayouts,dynamictraffic,andfine-grained
elements like street furniture, enabling effectively infinite simulation scenarios. All parameters (e.g., city size,
buildingdensity,vehicleandpedestriancount)arecustomizable,allowinguserstogeneratevariedandcontrollable
environments with minimal manual effort.
Inspired by (Phiresky, 2024),SimWorld’s procedural generation system adopts a modular and extensible
architecture. The pipeline proceeds through three sequential stages: road generation, building generation, and
street element generation, each progressively enriching the environment with structural and visual complexity.
The system constructs a hierarchical scene graph based on a quadtree data structure as illustrated in Algorithm 1.
Road Generation.Road generation defines the structural backbone of the city layout. Roads are first initialized
andthenexpandedusingaspanning-tree–basedalgorithmwithapriorityqueuethatbalancesdepthandbranching
during network construction. Additional procedures, including road-end attachment and intersection validation,
maintain topological coherence and realism in the generated layout.
Building Generation.Following the road generation stage, the pipeline proceeds to building generation, where
building assets are procedurally instantiated along road segments. Candidate locations are sampled and validated
for spatial feasibility to prevent overlap. A greedy placement strategy then fills residual gaps near intersections
and road ends, improving spatial utilization and maintaining visual consistency.
8

Road Generation Building Generation Element Generation
(a) Procedural City Generation
“Add some tablesand treesin front of the gate of hospital near clock tower”
Add TablesAdd Trees x 4x 42
1
Assets Library
tablestrees
Text to 3D Generation
Retrieval (b) LLM-Controllable Scene Edit
Figure 5:Overview of Procedural City Generation and LLM-Based Scene Editing.
Street Element Generation.Finally, street element generation adds detailed environmental elements (e.g.,
trees, road cones, benches, and parked vehicles). Elements are categorized and positioned based on contextual
zones, either adjacent to buildings or along sidewalks. While strict collision enforcement is relaxed to maintain
performance, placement still respects basic accessibility and spatial coherence constraints.
2.2.2. LLM-based Scene Editing
Beyond procedural generation,SimWorldsupports natural language-based scene editing (Figure 5b), enabling
dynamic world construction through open-ended instructions. Users or AI agents can modify scenes on-the-fly
with commands such as “add a red sports car next to the hospital near a museum ”.SimWorld
contains a retrieval-augmented LLM-based scene agent that grounds the command by querying the current
environment’s scene graph. The agent identifies the intended location using spatial anchors (e.g., “hospital”)
and contextual landmarks (“museum”), retrieves a matching asset from a library, and inserts it accordingly. If a
suitable asset is unavailable, the agent invokes an off-the-shelf text-to-3D generation model (Hunyuan3D, 2025)
to synthesize a new object from the prompt (“red sports car ”), converts it into a compatible format, and
integrates it into the environment. This approach enables semantically grounded, spatially coherent, and scalable
world construction, laying the foundation for interactive and compositional simulation.
2.2.3. Waypoint System
SimWorldimplements a waypoint system that provides a structured representation of navigable space to support
agent navigation and path planning (Figure 6). As an auxiliary abstraction layer, the waypoint system simplifies
movement by offering a clean, graph-based representation of where agents can go and how they can get there. It
forms the spatial backbone for both the traffic system (§2.2.4) and the action planner (§2.3.4), enabling agents to
move efficiently through complex environments.
Thesystemincludestwocomplementarywaypointrepresentations,coarse-grainedandfine-grained,whichtogether
create a unified navigation graph. Coarse waypoints capture high-level connectivity (e.g., roads, intersections),
while fine-grained waypoints represent detailed walkable paths. This hierarchical structure enables flexible and
robust navigation behaviors, including lane following, turning, detouring, and obstacle avoidance.
Coarse-grained Waypoints.The coarse-grained waypoints are generated from the geometric outputs of the
procedural city generation module (§2.2.1), including road centerlines and intersection coordinates. These
waypoints represent major structural points within the road network and capture the primary connectivity among
different routes.
Fine-grained Waypoints.The fine-grained waypoints are interpolated along the roads between coarse-grained
waypoints. These additional points increase the density of the navigation graph, allowing agents to follow
9

Figure 6:Overview of Waypoint System.Vehicles and pedestrians navigate through the environment by
following waypoints.
Traffic
Controller
Vehicle
Manager
Pedestrian
Manager
Intersection
Manager
Traffic
Network
Traffic Lane Sidewalk Crosswalk Vehicle Pedestrian Intersection
Traffic SignalPID Controller
Figure 7:Architecture of Traffic System inSimWorld.
smootherandmorecontinuoustrajectories. Parameterssuchasinterpolationstepsizeandspatialoffsetmagnitude
can be customized by users.
2.2.4. Traffic System
The traffic system inSimWorldsimulates dynamic road usage involving both vehicles and pedestrians. It models
realistic traffic flow through modules of vehicle spawning, route assignment, intersection control, and pedestrian
movement (Figure 7). By managing interactions among agents and coordinating traffic signals, the system
supports complex urban phenomena such as congestion, pedestrian crossings, and traffic light synchronization.
The traffic simulation supports route assignment, intersection control, and pedestrian flow simulation, running on
a fixed-timestep update loop for consistent and deterministic updates (Algorithm 2). Vehicle motion is governed
byaproportional–integral–derivative(PID)controller,withempiricallytunedparametersforrealisticacceleration,
braking, and turning dynamics (Jain & Babel, 2024). Pedestrian motion follows a lightweight model that adjusts
pedestrians’ orientations incrementally toward their goals based on angular differences. To simulate realistic
patterns,SimWorlduses a stochastic routing policy at intersections, i.e., agents select outgoing routes according
to predefined probability distributions. This stochastic behavior introduces natural variability and enhances scene
diversity.
The traffic system is built upon the waypoint system (§2.2.3), enabling traffic simulation that generalizes to any
procedurally generated city layout. Using the waypoints, the system calculates the detailed traffic areas (e.g.,
road lanes, sidewalks, and crosswalks) and procedurally instantiates vehicles, pedestrians, and traffic signals
accordingly. Three specialized managers coordinate these processes:
VehicleManager.Vehiclemanagerinitializesvehiclesalongdesignatedtrafficlanesandassignseitherpredefined
or dynamically generated routes through the navigation network.
10

Algorithm 2Simulation Loop for Urban Traffic Environments
1:Initialize:Sample initial states for vehiclesV, pedestriansP, and traffic signalsS.
2:Set simulation timet←0.
3:whilet < T max do▷Main simulation loop
4: UpdateVehicles(V,P,S)
5: UpdatePedestrians(P,V,S)
6: UpdateSignals(S, t)
7:t←t+ ∆t
10:functionUpdateVehicles(V,P,S)
11:for allv∈ Vdo
12:Perceive environment(V,P,S)
13:Execute driving model (throttle, brake, steering)
14:Updatev’s state (position, velocity)
16:functionUpdatePedestrians(P,V,S)
17:for allp∈ Pdo
18:Perceive(V,S), execute walking logic
19:Updatep’s position
21:functionUpdateSignals(S, t)
22:for alls∈ Sdo
23:Updatesaccording to timing plan or adaptive policy
Pedestrian Manager.Pedestrian manager spawns pedestrians on sidewalks and governs their motion patterns,
including crossing behavior and local avoidance at intersections.
Intersection Manager.Intersection manager detects intersections within the traffic network and deploys traffic
signals that regulate right-of-way according to configurable timing cycles or adaptive control policies.
Together, these components constitute a unified traffic simulation pipeline, enabling the virtual city to exhibit
realistic, adaptive, and scalable mobility dynamics across diverse urban layouts.
2.2.5. Gym-like Interface for Agent-Environment Interaction
SimWorldprovides a standard Gym-like interface, enabling seamless integration with existing reinforcement
learning pipelines and agent frameworks. Because this interface follows the widely adopted API conventions
of Gym (Farama Foundation, 2023), such as standardizedreset(), step(), and observation–action exchange
(Figure 2), it becomes straightforward for users to plug in their RL agents and immediately begin interacting
withSimWorld’s simulated environments. This design significantly lowers the barrier for conducting large-
scale experimentation, benchmarking, and agent–environment interaction studies using modern LLM/VLM or
policy-based agents.
Tosupportabroadvarietyofresearchgoalsrangingfromopen-endedsimulationstohighlycontrolledevaluations,
SimWorldoffers two simulation modes inspired by prior work such as CARLA (Dosovitskiy et al., 2017):
asynchronous and synchronous execution.
Asynchronous Mode.In asynchronous mode, each agent runs in its own thread and advances independently,
without waiting for other agents to finish their reasoning or action generation. Agents pull observations from a
centralized buffer and submit actions whenever they are ready. The environment processes all received actions at
fixed intervals (default: 0.1s), allowing real-time, continuous, and scalable multi-agent interactions. This mode is
ideal for large-scale, open-ended, or exploratory simulations where throughput, diversity, and responsiveness are
key.
Synchronous Mode.In synchronous mode, all agents advance in lockstep: the simulator proceeds to the next
steponlyaftereveryagenthassubmitteditsaction. Thisensuresstricttemporalalignmentbetweenperceptionand
control, making the mode particularly suitable for experiments requiring reproducibility, coordinated multi-agent
11

behavior, or high-quality data collection (e.g., video generation or RL training with fixed step timing).
2.3. Agent
SimWorldprovides a unified interface for LLM/VLM agents, supporting a flexibleAgent Framework(§2.3.1),
a diverseObservation Space(§2.3.2) and an open-endedAction Space(§2.3.3). This interface is designed to
accommodate both low-level control and high-level reasoning for LLM/VLM agents through anAction Planner
(§2.3.4) module, serving as the primary entry point for agent–environment interaction.
2.3.1. Agent Framework
The agent framework inSimWorlddefines a unified interface that structures the full agent loop of perception,
reasoning, planning, and execution. Across different embodiments—humanoids, vehicles, and robots—the
framework provides a common control pipeline.
Each agent first acquires observations fromSimWorld’s observation space (§2.3.2) via API calls (e.g.,
get_camera_observation(), get_agent_location()). These observations (e.g., visual inputs, scene
graphs) are then processed by the agent’s reasoning backend, which may incorporate LLMs, VLMs, VLAs, or
other decision-making models. Based on these observations, agents can employ any advanced reasoning or
planning algorithms (Guo et al., 2025; Hao et al., 2023; AL et al., 2024).
Reasoning outputs may be expressed in natural language (e.g., “sit on the nearest chair ”) or in structured
formats such as function calls. Both formats are compatible with the action planner (§2.3.4), which interprets
them into executable low-level actions.
The framework is also highly extensible. Researchers can plug in advanced reasoning components such as world
models(Hu&Shu,2023;Xingetal.,2025),memorysystems(Hoetal.,2025;Wangetal.,2024b),ormental-state
modules (e.g., emotions or preferences), enabling broad investigation into long-horizon reasoning, planning, and
embodied intelligence.
2.3.2. Observation Space
SimWorldprovides multiple observation modalities for agent perception and reasoning. The observation space
is organized into two primary categories: visual observations and structured semantic information (Figure 2).
Visual Observations.Agents can access three types of camera-based inputs from a first-person view: (1) color
images capturing the raw visual appearance of the environment, (2) depth maps encoding geometric distance from
the agent’s viewpoint, and (3) semantic segmentation masks providing pixel-level object category information.
Structured Semantic Observations.Beyond pixel-based perception,SimWorldexposes high-level spatial and
semantic representations, including a semantic scene graph and GPS-like localization information. The scene
graphencodesentities,attributes,andrelationalstructureswithintheenvironment,offeringasymbolicabstraction
of the 3D world. The localization interface specifies each agent’s or object’s position and orientation, enabling
precise reasoning about spatial relationships.
2.3.3. Action Space
SimWorldenables open-vocabulary action execution by organizing the action space into two hierarchical layers:
high-level semantic actions and low-level primitive actions:
High-Level Semantic Actions.To facilitate abstract reasoning and long-horizon decision-making, agents can
issue natural language commands. These commands are interpreted and executed by the built-in action planner
(§2.3.4), enabling flexible, open-ended behaviors (e.g., “sit on the nearest chair”).
Low-Level Primitive Actions.Primitive actions provide fine-grained control over agents. Vehicles support
continuous control signals (e.g., “acceleration”, “braking”, and “steering”). Robots allow continuous
translation and rotation (e.g., “forward”, “backward”, “lateral_movement”, and “rotation”). Human
12

Table 2:Low-Level Primitive Actions inSimWorld.
Action Agent Type Description
Object Interaction Actions
Pick Up / Drop Off Humanoid Grasp or release an object
Carry / Put Down Heavy Object Humanoid Transport and place large objects
Sit Down / Stand Up Humanoid Transition between seated and standing states
Open Door / Enter / Exit Car Humanoid Interact with doors or vehicles
Ride Scooter Humanoid Control and ride a scooter
Observation Actions
Look Up / Down Humanoid, Dog Adjust gaze vertically
Focus Humanoid, Dog Narrow or widen the field of view
Take Photo All Capture current view as an image
Social Actions
Have Conversation / Discuss Humanoid Exchange verbal communication
Point Direction / Wave Hand Humanoid Use gestures for social signaling
Argue with Body Language Humanoid Express disagreement through gestures
Navigation Actions
Move Forward / Step Forward–BackwardHumanoid, Dog Move or step in the current direction for a short duration
Rotate / Steering Humanoid, Dog, Vehicle Adjust facing or steering direction
Throttle / Brake Vehicle Accelerate or decelerate the vehicle
Stop All Halt all current motion
agents can navigate (“move”, “turn”) and perform interactive actions, including human–object (e.g., “pick_up”,
“drop”, “sit”), human–vehicle (e.g., “enter_car”, “exit_car”), and human–human (e.g., “wave_hands”,
“discussion”) interactions. A complete list of supported actions is provided in Table 2.
2.3.4. Action Planner
SimWorldincludesanactionplannermodulethatbridgeshigh-levelreasoningwithlow-levelexecution,allowing
researchers to focus on abstract planning without needing to manage embodiment-specific control details. The
planner consists of two components: aparserand anexecutor. The parser receives high-level plans from the
agent, often expressed in natural language or structured function calls, and translates them into sequences of
low-level primitive actions. The executor then carries out these actions step by step, conditioned on the current
environment state.
To support diverse research objectives,SimWorldprovides two executor variants: arule-basedexecutor,
which operates on abstract city-layout information, and avisual-basedexecutor, which directly consumes visual
observations from the simulator. The latter enables seamless integration with VLMs or VLAs, supporting
end-to-end perception–reasoning–action pipelines.
By handling the translation from high-level intent to low-level control, the action planner enables agents to
perform long-horizon, semantic planning whileSimWorldautomatically manages movement, navigation, and
interaction details.
For example, when the action planner receives a plan such as “go to the nearest chair and sit down ”,
the parser first decomposes the instruction into an action list: “navigate” and “agent_sit_down". The
navigate action is non-atomic and can be further expanded into primitive operations such as “step_forward”
and “rotate” by executor. In therule-basedexecution mode, the planner computes the shortest path from the
agent’s current position to the nearest chair, generating a sequence of navigation primitives such asnavigate(0,
1), navigate(1, 10) , andnavigate(10, 10) , where(10, 10) denotes the chair’s location. Once the agent
reaches the chair, the executor executes “agent_sit_down” and terminates when the action list becomes empty.
In thevisual-basedmode, the executor directly feeds environmental observations into a VLM (e.g., GPT-4o),
which determines the next action step by step (e.g., execute “step_forward” then “step_forward” and finally
“agent_sit_down”) based on visual context.
13

1. Assets Preparation
2. Scene Preparation
4. Simulation
5. Evaluation
Download from FAB MarketplaceGenerated by assets generation models
Managing and control task pipeline
Load layouts to Unreal
Evaluate agents capabilities
👍
Broadcast Collaboration
bid for 100$bid for 80$I have an order…Dispatch Order
Go picking up order 1Next waypoint: (100, 20)
Track ActionsDelivery Task Loop
Load
Download
Analysis agent behaviors
3DAssetsGeneration Model
3. Spawning AgentLayouts of ScenesRendered Scenes in Unreal Engine
Spawn vehicles, pedestrains and agents step by step
A motor cycle with orange body color…
Calculate Reward
Overview of Buildings
Original ScenePedestrians/Vehicles SpawnedAgents Spawned
Figure 8:Workflow for Constructing a Task Suite inSimWorld.
14

2.4. UnrealCV+ Communication Module
Inspired by UnrealCV (Qiu et al., 2017), we develop UnrealCV+ as a communication module that bridges the
Unreal Enginebackend (§2.1)with theenvironment layer(§2.2). By establishingaTransmission ControlProtocol
(TCP) connection, UnrealCV+ enables efficient, reliable, and bidirectional communication between the two sides.
Implemented in both Python and C++, the module supports flexible data exchange and fine-grained control of the
simulation.
To adapt UnrealCV+ to agent-task scenarios, we introduce a customized command set for scene control,
actor manipulation, and data querying. For example, the environment layer can issue commands to the
Unreal Engine backend such as “spawn actors at locations ”, “get position of a pedestrian ”, or
“execute action of a robot”.
Within the simulation loop, the environment layer governs the logical evolution of the simulation, while the
Unreal Engine backend continuously returns updated physical states and visual observations of all agents.
All communications are transmitted through UnrealCV+. This decoupled architecture cleanly separates logic
computation from rendering, improving flexibility, scalability, and modularity.
3. Case Study: Delivery Task
SimWorldis built with extensibility and evaluation task creation as core design goals. It provides tools to easily
define tasks, agent roles, reward functions, and evaluation metrics, minimizing the engineering effort required to
create new experiments. Figure 8 showcases how to define a multi-agent delivery task within theSimWorld
ecosystem. The process is delineated as follows:
First, users prepare assets for the delivery task, either by importing 3D assets purchased from third-party
marketplaces or by generating them using text-to-3D models. Next,SimWorldinitializes the city environments
via its procedural city generation module to build roads, buildings, trees, and city props. Third, vehicles,
pedestrians and delivery agents are spawned. Fourth, the simulation runs, allowing delivery agents to act and
interact within the configured environment dynamics. Finally, delivery agents are evaluated across multiple
dimensions, such as delivery success rate, average completion time, and total profit. The following sections
provide detailed definitions and analysis. The eventual architecture of the delivery task is shown in Figure 9.
3.1. Task Formulation
The delivery task is designed to evaluate the social reasoning capabilities of foundation models in realistic,
open-world urban environments. LLM agents are deployed as delivery agents in a city-scale environment built
usingSimWorld. Theirgoalistogrowandthriveinthisdynamicsetting. Toenhancerealismandcomplexity,the
environment incorporates several dynamic systems: (1) an energy system, where agents must manage stamina and
replenish it through consumables; (2) an economic system, where agents earn and spend currency on purchases
such as scooters and drinks; (3) an order-sharing mechanism, enabling agents to collaborate by sharing delivery
tasks and optimizing group performance. These components create a rich, interactive simulation environment for
evaluating agents’ decision-making, adaptability, and social reasoning in complex urban scenarios. The overview
of the delivery task is shown in Figure 10.
Environment.All experiments are conducted on the same map generated by the procedural city generation
module inSimWorld. To ensure fair and efficient evaluation, graphical rendering is disabled during simulation.
However, the physical simulation and evaluation modules remain active to preserve environment dynamics and
task fidelity.
Action Space.The task features a two-tiered action space: high-level actions decided by LLM agents and
low-level actions executed by theSimWorldaction planner. At each decision step, the agent may choose:Bid
Order(offer a price to compete for a new order),Pick Up Order(navigate to the pick-up point),Deliver Order
(complete delivery at the destination),Share Order(publish the order for collaboration),Purchase Scooter
(purchase a scooter and equip it to move faster). The full action space is shown in Table 3.
15

Simulator
Agent
Scenes
EvaluationAvg.Success Rate Avg.Delay Time Avg. Invalid Action Rate Avg. Order Shared Rate Avg.Profit
Multi-modal Observations
Local Planner
SimulatedScene
Prompt:You are a delivery man in the city. Your goal is maximize your proﬁt.Your current state is: <Current State>You have observations as <Muti-modal Observations>Your action history is: <Action History>
Output: Next Activity DescriptionActivity: go and pick up Order 1Route Plan: I need ﬁrst go to intersection 1, and then go straight, and then turn left … Action: pick_up(order1)
LoggingMessage
LLMs
Logging History
+10$-   x1
balance 0+10=10$
balance 5-10 < 0$
-10$+   x1
Action Checker
-10$+   x1
balance 50-10=40$
TaskStateMachineS1S2A1A2
 StateAction: MovingEnerge left: 89Speed: 100Balance: 25$
Action HistoryMoving_forwardTure_leftMoving_forward…State & Action History
Figure 9:Architecture of the Delivery Task.
Baseline Agents.We evaluate multiple foundation models serving as the backbone of delivery agents, including
Claude-3.5-Sonnet, DeepSeek-V3, GPT-4o, Gemini-2.5-Flash, and QWQ. The ReAct (Yao et al., 2022)
prompting framework is employed to explicitly separate reasoning and action selection.
Metrics.Aligned with the agent’s hierarchical decision-making, we design a three-level evaluation framework.
Overall performance is measured bytotal profit(the cumulative monetary gain the agent achieves over the
simulation period), while operational effectiveness is assessed usingorder success rate(the proportion of orders
that the agent successfully completes relative to the total assigned orders),energy efficiency(the ratio of energy
consumed to revenue generated),order sharing count(the number of sharing orders), andinvestment count(the
number of strategic investments).
3.2. Main Results
Foreachevaluation,wesample20agentscontrolledbythesamelanguagemodel,eachrunningfor5000simulation
steps. At each step, an agent issues two API requests, averaging around 7000 tokens per request. Based on
results in Table 4, our empirical analysis over three simulation rounds reveals distinct operational behaviors across
models.
DeepSeek-V3 (69.475±16.772 ) and Claude-3.5-Sonnet (69.068±20.685 ) achieved the highest mean
profits, withClaude-3.5-Sonnet also leading in mean successful orders (2.733±1.102 ) and energy efficiency
(0.5411±0.1981 ). Notably, these superior average outcomes were associated with substantial performance
variability, as reflected in their respective standard deviations.
Conversely, Gemini-2.5-Flash, while attaining a moderate mean profit of42.423, exhibited markedly more
consistent profit generation with a standard deviation of±3.103, and also demonstrated stability in successful
orders (2.100±0.173 ). Extreme variability was evident in specific metrics for certain models; for instance,
sharing counts forDeepSeek-Prover-V2(7.333±8.386 ) andClaude-3.5-Sonnet(11.333±8.386 ) showed
standard deviations exceeding their means, indicating highly unpredictable behavior in this aspect.
16

Case Study: Delivey Task-Multi-Agent Collaboration and CompetitionPursuing Profit
Collaborating
Competing
MakingInvestment
-$100Speed x 5Efficiency x 2
Go picking uporder 1
Next waypoint: (100, 20)
Current StatePersonality: conscientiousBalance: -30$Current Order: order1Energy: 100Speed: 200cm/s
Current StatePersonality: openBalance: 100$Current Order: NullEnergy: 100Speed: 200cm/s
Current StatePersonality: extrovertedBalance: 0$Current Order: order3Energy: 100Speed: 200cm/s
Current StatePersonality: neuroticBalance: 30$Current Order: NullEnergy: 100Speed: 200cm/s
bid for 100$bid for 80$I have an order…
👍
Init Money
Big-five Personality
$-30
$0
$100
$30
Store1pos: (120, 150)
Customer1pos: (100, 20)
Order1been assignedOrder2Is in bidding
LLM
ReasoningMy current balance is -30$, I need to make money by delivering order. My currernt order is order1. I need to pick it up. The next waypoint is (100, 20)Reasoningmy current balance is 100$. I am open to try new method in work, and buying a scooter can bring me potential benefit. I will spend 100$ to do investement.
ReasoningI am an extroverted delivery man. I am open to cooperate with others. I'll share my current order with others so that both of us can benefit from it.
ReasoningI need to make money . I do not take any order and order2 has the lowest bid at 100$. I will bid order2 for price 80$ to get this order.
Figure 10:Delivery Task.A delivery scenario requiring multi-agent collaboration and competition. Each agent
is initialized with distinct personalities and internal states and can act to grow, thrive, and ultimately maximize its
earnings.
The GPT-4o-minimodel consistently yielded zero values across all metrics (0.000±0.000 ), suggesting it does
not truly understand the goals well enough to make reasonable decisions based on the given instructions and
context.
Higherinvestmentstrategies,suchasthoseadoptedby DeepSeek-V3(8.000±3.000 )and Claude-3.5-Sonnet
(9.000±3.464 ), generally correlated with greater mean profit achievement but also with increased outcome
volatility. These findings underscore a prevalent trade-off between optimizing for peak average performance
metrics and ensuring consistent, predictable agent behavior, a critical consideration for robust deployment in
dynamic environments.
Takeaway: Model Performances in Multi-agent Tasks
Top-performing models such asDeepSeek-V3 and Claude-3.5-Sonnet achieve high average profits
but show greater variance, whereasGemini-2.5-Flash demonstrates more consistent yet moderate
performance. GPT-4o-mini failed entirely across all metrics. Overall, the results highlight a trade-off
between maximizing average performance and ensuring consistent, reliable behavior (Table 4).
3.3. Ablation Study
To take a step deeper on multi-agent collaboration and competition, we conduct three ablation experiments. In
theModel Competitionsetting, we sample 24 agents controlled by 12 models, with each model managing
two agents over 1000 rounds. In this ablation experiment, we study how models make choices within a highly
competitive environment in order to maximize their returns; In theEnvironment Configurationsetting, we vary
two environment configurations: the initial financial budget and the global order volume. For each configuration,
we sample several stages from low to high to observe how agents’ behavior changes with the environment
conditions; In thePersonasetting, we use the model with the best performance to control the agents with persona
17

Table 3:Hierarchical Action Space Design in Delivery Task.High-level actions are given to language models
to make decision, which correspond to strategic decisions, while low-level actions are only exposed to local action
planner module to execute concrete movements and interactions.
Action Level Action Name Description Invocation Method
High-Level
Bid Order Offer a price to a new order on platform to compete with other Model Generations
Model Generation
Pick Up Order Navigate to the pick-up point of order
Deliver Order Navigate to the delivery point and complete the order
Share Order Publish the order for multi-model generation cooperation
Cancel Share Order Cancel a shared order that has been published
Go to Meet-point Navigate to the meet point for the shared orde
Purchase Scooter Buy and use a scooter
Purchase Drinks Buy consumables to restore energy
Adjust Speed Adjust travel speed
Low-Level
Move Forward Basic movement action
Action Planner
Stop Stop moving
Rotate Adjust the facing direction
Change Speed Adjust walking speed
Drive Scooter Control a scooter for movement
Table 4:Performance of Model-Controlled Agents.Metrics are reported as mean (Avg) and standard deviation
(Std) over three 5000-step simulations. Bold indicates the best Avg per column.
Model Profit Successful Orders Energy EfficiencySharing Count Investment Count
Avg Std Avg Std Avg Std Avg Std Avg Std
DeepSeek-V369.4816.77 2.10 0.47 0.34 0.07 2.33 0.47 8.00 3.00
Claude-3.5-Sonnet 69.07 20.692.731.100.540.2011.338.399.003.46
GPT-4o 43.91 14.16 1.63 0.43 0.30 0.06 0.67 0.47 4.67 0.47
Gemini-2.5-Flash 42.42 3.10 2.10 0.17 0.17 0.04 2.67 1.25 2.00 2.00
Gemini-2.0-Flash 28.72 12.04 1.53 0.58 0.11 0.03 0.67 0.47 0.67 1.00
Qwen3-32B 24.73 7.95 1.37 0.13 0.40 0.17 1.33 0.47 5.33 2.06
DeepSeek-Prover-V2 21.66 7.18 0.67 0.14 0.42 0.03 7.33 8.39 1.00 1.00
QwQ 17.31 4.07 0.87 0.20 0.41 0.20 0.33 0.47 3.33 2.52
GPT-4o-mini 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
description in prompts. We sample 20 agents, assign each persona to two agents, and observe how these personas
shape the agents’ behaviors and decision strategies.
Model Competition.To intensify inter-agent competition, we constrain each agent to handle at most one order
at a time and set the environment’s hunger rate to 0.9, ensuring a high demand for delivery. In each experimental
session, 24 agents are jointly controlled by 12 different models, where each model governs two agents. These
agents actively bid for orders in a shared environment with the goal of maximizing profit. Each session runs for
1000 simulation steps, and results are averaged across three random seeds.
As shown in Figure 11a, models exhibit distinct bidding behaviors. Notably, Claude-3.7-Sonnet,
Gemini-2.5-Flash and Gemini-2.0-Flash demonstrate broad bid price distributions, indicating a flexi-
ble bidding strategy. This flexibility increases their chances of winning orders when in competition with other
models. In contrast, models such asLLaMA-4-Scout and LLaMA-3.2-11b tend to use narrower bidding ranges,
which limits their competitiveness and results in lower win rates.
Figure 11b presents the head-to-head competition outcomes.Deepseek-Prover-V2 and Qwen3-32B achieve
the highest win rates against other models. This is primarily because they often bid lower prices, making their
offers more likely to be accepted by the platform. Conversely, models likeGPT-4o and LLaMA-3.2-11b tend
to place higher bids, reducing their success rate despite frequent participation. Models such asQwQ-32B and
GPT-4o-mini are less active overall, leading to fewer bids and lower order acquisition rates. This inactivity
contributes to their diminished final profit, as shown in Table 4.
18

Takeaway: Multi-Agent Competition
Models with flexible bidding strategies, likeClaude-3.7-Sonnet and Gemini-2.5-Flash, achieve
higher order win rates, while those with narrow or high bids, likeLLaMA-3.2-11b and GPT-4o, un-
derperform. Models that bid aggressively, such asDeepseek-Prover-V2 and Qwen3-32B, dominate
head-to-head competitions, whereas inactive models likeGPT-4o-minifail to secure bids and profits.QwQ
andGPT-4o-minishow minimal bidding activity and weak task participation (Figure 11).
100 110 120 130 140 150
Bid Price
gemini-2.0-flash
gpt-4o
claude-3.7-sonnet
claude-3.5-sonnet
llama-4-scout
llama-3.2-11b
deepseek-prover-v2
deepseek-v3
gemini-2.5-flash
qwen3-32b
Bid Distribution by Model
All Bids
Successful Bids
(a)Bidpricedistributionbymodel. Theviolinplotsillustratethedistribution
of bid prices generated by each model. Red points indicate bids that were
successfully accepted.
claude-3.7-sonnetgemini-2.5-flashgemini-2.0-flashllama-4-scout
claude-3.5-sonnetdeepseek-prover-v2
deepseek-v3
gpt-4o
llama-3.2-11bqwen3-32bgpt-4o-miniqwq-32b
Opponent Model
claude-3.7-sonnet
gemini-2.5-flash
gemini-2.0-flash
llama-4-scout
claude-3.5-sonnet
deepseek-prover-v2
deepseek-v3
gpt-4o
llama-3.2-11b
qwen3-32b
gpt-4o-mini
qwq-32b
Model
0 1 2 4 1 -2 1 2 -2 -1 0 0
-1 0 -13-12 -3 9 7 7 -2 2 0 0
-2 13 0 -8 2 -2 -1 3 2 -2 0 0
-4 12 8 0 4 4 -8 10 13 -7 0 0
-1 3 -2 -4 0 -2 -1 6 -1 -2 1 0
2 -9 2 -4 2 0 2 4 3 -2 0 0
-1 -7 1 8 1 -2 0 1 7 -2 0 1
-2 -7 -3 -10 -6 -4 -1 0 -1 0 0 0
2 2 -2 -13 1 -3 -7 1 0 -3 0 0
1 -2 2 7 2 2 2 0 3 0 0 0
0 0 0 0 -1 0 0 0 0 0 0 0
0 0 0 0 0 0 -1 0 0 0 0 0
Head-to-Head Results with
 competition between models
10
5
0
5
10
Wins (+) / Losses (-) (b) Win-Loss Matrix of Model Competition.
Figure 11:Bidding Behavior and Evaluation Results. (a)Lower bid prices may increase the likelihood of being
assigned an order, but often come at the cost of reduced profit margins.(b)Higher values in red represent more
wins; lower values in blue indicate more frequent losses in pairs.
Environment Configuration.We further investigate how different environmental configurations impact agent
behavior and overall performance. Specifically, we explore two key factors: the global order availability and the
agents’ initial financial endowment. For each factor, we conduct a series of controlled experiments to observe how
variations affect agents’ action distributions.
As shown in Figure 12a, when the total number of available orders increases, agents tend to perform fewer
pickup and delivery actions and instead choose thedo nothing action more frequently. This suggests that in
resource-rich environments, agents are more inclined to conserve energy and avoid unnecessary effort, opting
to wait for optimal opportunities rather than actively pursue deliveries. Conversely, in low-resource settings,
agents are more motivated to engage in delivery tasks to secure profits. Additionally, as resource abundance
increases, agents demonstrate a higher tendency to initiate and complete shared deliveries, likely as a means to
reduce energy costs through collaboration.
Figure 12b illustrates the impact of agents’ initial monetary resources. As initial capital increases, agents are
less reliant on aggressive bidding and instead prioritize actions such as order pickup. When funds are limited,
competition intensifies, leading to more frequent bidding behavior. Furthermore, with sufficient initial capital,
agents are more willing to invest in infrastructure, such as purchasing a scooter, which enhances their long-term
delivery efficiency.
Takeaway: Resource and Decision-Making Strategy
Order resource scarcity increases agent competitiveness and task urgency. Sufficient agent initial money
leads to more relaxed, profit-insensitive behavior (Figure 12).
Theseobservationssuggestthatagentsaremorecompetitiveandtask-driveninresource-constrainedenvironments.
In contrast, resource-rich conditions reduce the urgency to complete tasks and generate immediate profits.
Importantly, agents are also more likely to engage in actions that involve upfront costs but promise long-term
benefits—such as investment and shared delivery—provided they have the financial capacity and enough orders
taken to do so.
19

DO_NOTHING
BID_ORDER
PICK_UP_ORDER
DELIVER_ORDER
BUY_BEVERAGE
OPEN_SHARED_ORDER
GO_TO_MEETING_POINT
CHANGE_WALKING_SPEED
BUY_BIKE
/uni00000014/uni0000001a/uni0000001b/uni00000015/uni00000017/uni00000018/uni00000016/uni0000001a/uni00000017/uni00000019/uni0000001c/uni00000014/uni0000001c/uni00000018/uni00000014/uni00000015/uni00000014/uni00000018/uni00000018
Total Order Quantity
/uni00000013
/uni00000015/uni00000013/uni00000013
/uni00000017/uni00000013/uni00000013Count
Main Actions
/uni00000014/uni0000001a/uni0000001b/uni00000015/uni00000017/uni00000018/uni00000016/uni0000001a/uni00000017/uni00000019/uni0000001c/uni00000014/uni0000001c/uni00000018/uni00000014/uni00000015/uni00000014/uni00000018/uni00000018
Total Order Quantity
/uni00000013
/uni00000015
/uni00000017
/uni00000019Count
Auxiliary Actions
(a) Effect of Order Quantity
1209060300-30
Agent Initial Money
0
200
400
600Count
Main Actions
1209060300-30
Agent Initial Money
0
5
10
15Count
Auxiliary Actions (b) Effect of Initial Money
Figure 12:Action Distribution across Environmental Settings.(a) shows how global order quantity affects
agent behavior; (b) shows the effect of initial money on action selection.
Influence of Persona.Personality traits significantly affect the decision-making and performance of delivery
agents. As shown in Figure 13, agents with higher Conscientiousness tend to exhibit a lower frequency of bidding
actions, a higher frequency of task-completion actions (e.g., picking up orders), and achieve a higher bid win rate.
This suggests that conscientious agents prioritize task completion over strategic competition. Agents with higher
Agreeableness are less likely to remain inactive (i.e., performdo nothing actions) and tend to achieve higher
bid win rates. Conversely, agents with lower Agreeableness display higher inactivity and narrower bidding price
ranges, limiting their competitiveness. Interestingly, agents with higher Openness exhibit reduced engagement in
deliverytasks, possiblybecausetheyexplorecompetitiveorunconventionalbiddingstrategiesthatdivertattention
from task execution.
Bid Win RateBid Order Count
Pick Up Order CountDeliver Order CountBuy Beverage CountDo Nothing CountBuy Bike Count
Openness
Conscientiousness
Extraversion
Agreeableness
Neuroticism
0.02 0.38 -0.10 -0.70 -0.44 -0.04 0.51
0.65 -0.64 0.66 0.08 0.44 0.28 -0.42
0.25 -0.03 0.15 -0.37 0.00 -0.01 0.53
0.63 0.34 -0.20 0.01 -0.35 -0.70 0.00
0.08 -0.11 0.19 0.04 -0.07 -0.08 -0.39
Trait vs Win Rate/Action Proportion
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
(a) Pearson correlation b/w Big Five personality traits and
agent behaviors.
0.0 0.2 0.4 0.6 0.8
Conscientiousness
0.5
0.6
0.7
0.8
0.9
Bid Order
r = -0.64
RMSE = 0.096
Conscientiousness
 vs Bid Order
0.2 0.4 0.6 0.8 1.0
Agreeableness
0.00
0.01
0.02
0.03
0.04
0.05
0.06
0.07
Do Nothing
r = -0.70
RMSE = 0.016
Agreeableness
 vs Do Nothing
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
Openness
0.000
0.025
0.050
0.075
0.100
0.125
0.150
0.175
Deliver Order
r = -0.70
RMSE = 0.035
Openness vs
 Deliver Order
0.0 0.2 0.4 0.6 0.8
Conscientiousness
0.03
0.04
0.05
0.06
0.07
0.08
0.09
0.10
Bid Win Rate r = 0.65
RMSE = 0.017
Conscientiousness
  vs Bid Win Rate
0.2 0.4 0.6 0.8 1.0
Agreeableness
0.03
0.04
0.05
0.06
0.07
0.08
0.09
0.10
Bid Win Rate r = 0.63
RMSE = 0.017
Agreeableness
 vs Bid Win Rate
0.0 0.2 0.4 0.6 0.8
Conscientiousness
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40
Pick Up Order
r = 0.66
RMSE = 0.076
Conscientiousness
  vs Pick Up Order
(b) Linear Regression Reveals Strong Correlations between Behaviors and
Persona Traits.
Figure 13:Persona Influence on Agent Performance and Behavior. (a)Agents with higher Agreeableness are
less likely to remain inactive and tend to achieve higher bid win rates. Conversely, agents with lower agreeable–
ness display higher inactivity and narrower bidding price ranges, limiting their competitiveness.(b)The results
demonstrate that agent behaviors are tightly aligned with their corresponding persona attributes, highlighting the
effectiveness of trait-driven behavior modeling.
Takeaway: Impact of Persona in Multi-agent Interaction
Agent personalities shape strategic tendencies: conscientious agents prioritize task fulfillment, while
openness and agreeableness modulate competitiveness and inactivity (Figure 13).
4. Related Works
Simulations have played a crucial role in constructing environments for training and evaluating autonomous
agents. Text-based simulators often emphasize social scenarios, such as human interaction (Yang et al., 2024),
20

daily activities (Park et al., 2023), and relational polarization (Piao et al., 2025). Popular embodied simulators
support a broader range of applications, particularly in embodied AI research and 2D/3D scene synthesis (Li et al.,
2025a). However, most embodied simulators remain constrained to either indoor household environments (e.g.,
AI2-THOR (Kolve et al., 2017), Habitat (Puig et al., 2023), iGibson (Li et al., 2021)) or outdoor driving scenarios
(e.g., CARLA (Dosovitskiy et al., 2017), MetaDrive (Li et al., 2022)) or natural scenes (e.g., AirSim (Shah
et al., 2017)). Most of these simulators (Dosovitskiy et al., 2017; Puig et al., 2023; Li et al., 2021; Shah et al.,
2017; Wang et al., 2024a; Gao et al., 2024) rely on a limited number of manually crafted scenes, which hinders
scalability and diversity. Some platforms, such as MetaUrban (Wu et al., 2025), MetaDrive (Li et al., 2022),
AI2-THOR (Kolve et al., 2017) and Genesis (Authors, 2024), introduce rule-based procedural generation to
alleviate this issue. Nonetheless, existing embodied simulators typically lack support for dynamic multi-agent
interactions in complex diverse environments.
Recentadvancementshaveintroducedlarge-scale,language-drivensocialsimulatorscapableofmodelingcomplex
societal behaviors. OASIS (Yang et al., 2024) simulates up to one million LLM-powered agents interacting on
social media platforms, capturing phenomena such as information diffusion, echo chambers, and polarization.
Casevo(Jiangetal.,2024)integrateschain-of-thoughtreasoning,retrieval-augmentedgeneration,andcustomizable
memory mechanisms to simulate intricate social phenomena and decision-making processes. MineLand (Yu
et al., 2024) offers a multi-agent Minecraft environment where agents, driven by physiological needs and limited
multimodal perception, engage in collective behaviors, fostering ecological and detailed simulations. Project
sid (AL et al., 2024) further advances this landscape by deploying a large number of AI agents within a Minecraft
environment to explore the emergence of AI civilizations. VirtualCommunity (Zhou et al., 2025) leverages
Genesissimulatortoconductcommunityinfluencetaskinoutdoor,multi-agentscenes. Thesesimulationplatforms
demonstrate agents’ capabilities to form complex social structures, economies, andgovernance systems, providing
insights into large-scale societal simulations and agentic organizational intelligence.
None of the existing simulators are explicitly designed to support dynamic, multi-agent interactions in large-scale
outdoor and other diverse environments with both realistic rendering and physical simulation.SimWorld
addresses this limitation by providing a scalable, procedurally generated, and LLM/VLM-compatible platform
that enables multi-agent collaboration and competition, language-grounded interactions, and comprehensive
benchmarking for embodied intelligence.
Another emerging direction in world simulation involves end-to-end neural world models, which generate
interactivevideopredictionsconditionedonenvironmentstates,agentactions,andhigh-levelcontrols(Xiangetal.,
2024; DeepMind, 2025; Xiang et al., 2025). Recent systems can simulate short video rollouts or 3D-consistent
scenes using learned dynamics, offering a flexible alternative to traditional engine-based simulation. On the other
hand,SimWorld, built on the Unreal Engine, provides high-fidelity, physically grounded, and deterministically
controllable environments capable of supporting thousands to even millions of interacting agents at scale.
Moreover, becauseSimWorldsupports diverse, high-quality procedural and handcrafted scenes, it can serve as
a powerful generator of large-scale training data, offering a rich source of supervised trajectories, multi-agent
interactions, and physically realistic rollouts that can be used to train and improve neural world models.
References
AL, A., Ahn, A., Becker, N., Carroll, S., Christie, N., Cortes, M., Demirci, A., Du, M., Li, F., Luo, S., Wang,
P. Y., Willows, M., Yang, F., and Yang, G. R. Project sid: Many-agent simulations toward ai civilization, 2024.
URLhttps://arxiv.org/abs/2411.00114.
Anthropic. Claude’s extended thinking, 2025. URL https://www.anthropic.com/research/
visible-extended-thinking. Accessed: 2025-05-14.
Authors, G. Genesis: A generative and universal physics engine for robotics and beyond, December 2024. URL
https://github.com/Genesis-Embodied-AI/Genesis.
Brohan, A., Chebotar, Y., Finn, C., Hausman, K., Herzog, A., Ho, D., Ibarz, J., Irpan, A., Jang, E., Julian, R.,
et al. Do as i can, not as i say: Grounding language in robotic affordances. InConferenceonrobotlearning, pp.
287–318. PMLR, 2023.
21

DeepMind. Genie 3: A new frontier for world models. https://deepmind.google/blog/
genie-3-a-new-frontier-for-world-models/, 2025. Accessed: 2025-11-27.
Dosovitskiy, A., Ros, G., Codevilla, F., Lopez, A., and Koltun, V. CARLA: An open urban driving simulator. In
Proceedings ofthe1stAnnual ConferenceonRobotLearning, pp. 1–16, 2017.
Driess, D., Xia, F., Sajjadi, M. S., Lynch, C., Chowdhery, A., Wahid, A., Tompson, J., Vuong, Q., Yu, T., Huang,
W., et al. Palm-e: An embodied multimodal language model. 2023.
Fan,L.,Wang,G.,Jiang,Y.,Mandlekar,A.,Yang,Y.,Zhu,H.,Tang,A.,Huang,D.-A.,Zhu,Y.,andAnandkumar,
A. Minedojo: Building open-ended embodied agents with internet-scale knowledge.Advances in Neural
InformationProcessingSystems, 35:18343–18362, 2022.
Farama Foundation. Gymnasium.https://gymnasium.farama.org/, 2023. Accessed: 2025-11-27.
Gao,C.,Zhao,B.,Zhang,W.,Mao,J.,Zhang,J.,Zheng,Z.,Man,F.,Fang,J.,Zhou,Z.,Cui,J.,etal. Embodiedcity:
A benchmark platform for embodied agent in real-world city environment.arXivpreprint arXiv:2410.09604,
2024.
Guo, D., Yang, D., Zhang, H., Song, J., Zhang, R., Xu, R., Zhu, Q., Ma, S., Wang, P., Bi, X., et al. Deepseek-r1:
Incentivizing reasoning capability in llms via reinforcement learning.arXivpreprint arXiv:2501.12948, 2025.
Ha, A. Google’s gemini has beaten pokémon blue (with a little
help). TechCrunch, 2025. URL https://techcrunch.com/2025/05/03/
googles-gemini-has-beaten-pokemon-blue-with-a-little-help/. Accessed: 2025-05-14.
Hao, S., Gu, Y., Ma, H., Hong, J. J., Wang, Z., Wang, D. Z., and Hu, Z. Reasoning with language model is
planning with world model.arXivpreprint arXiv:2305.14992, 2023.
Ho, M., Si, C., Feng, Z., Yu, F., Yang, Y., Liu, Z., Hu, Z., and Qin, L. Arcmemo: Abstract reasoning composition
with lifelong llm memory.arXivpreprint arXiv:2509.04439, 2025.
Hu, Z. and Shu, T. Language models, agent models, and world models: The law for machine reasoning and
planning. arXivpreprint arXiv:2312.05230, 2023.
Hunyuan3D, T. Hunyuan3d 2.0: Scaling diffusion models for high resolution textured 3d assets generation, 2025.
Jain, H. and Babel, P. A comprehensive survey of pid and pure pursuit control algorithms for autonomous vehicle
navigation. arXivpreprint arXiv:2409.09848, 2024.
Jiang, Z., Shi, Y., Li, M., Xiao, H., Qin, Y., Wei, Q., Wang, Y., and Zhang, Y. Casevo: A cognitive agents and
social evolution simulator.arXivpreprint arXiv:2412.19498, 2024.
Kolve, E., Mottaghi, R., Han, W., VanderBilt, E., Weihs, L., Herrasti, A., Deitke, M., Ehsani, K., Gordon, D., Zhu,
Y., et al. Ai2-thor: An interactive 3d environment for visual ai.arXiv preprint arXiv:1712.05474, 2017.
Li, C., Xia, F., Martín-Martín, R., Lingelbach, M., Srivastava, S., Shen, B., Vainio, K., Gokmen, C., Dharan, G.,
Jain, T., et al. igibson 2.0: Object-centric simulation for robot learning of everyday household tasks.arXiv
preprint arXiv:2108.03272, 2021.
Li, C., Zhang, R., Wong, J., Gokmen, C., Srivastava, S., Martín-Martín, R., Wang, C., Levine, G., Ai, W.,
Martinez, B., et al. Behavior-1k: A human-centered, embodied ai benchmark with 1,000 everyday activities
and realistic simulation.arXivpreprint arXiv:2403.09227, 2024.
Li, Q., Peng, Z., Feng, L., Zhang, Q., Xue, Z., and Zhou, B. Metadrive: Composing diverse driving scenarios for
generalizable reinforcement learning.IEEE transactions on pattern analysisand machineintelligence, 45(3):
3461–3475, 2022.
Li, X., Song, R., Xie, Q., Wu, Y., Zeng, N., and Ai, Y. Simworld: A unified benchmark for simulator-conditioned
scene generation via world model.arXiv preprint arXiv:2503.13952, 2025a.
22

Li, Z., Xie, Y., Shao, R., Chen, G., Jiang, D., and Nie, L. Optimus-2: Multimodal minecraft agent with
goal-observation-action conditioned policy. InProceedings of the Computer Visionand Pattern Recognition
Conference(CVPR), pp. 9039–9049, June 2025b.
Liu, S. et al. Odyssey: Empowering minecraft agents with open-world skills.arXivpreprint arXiv:2407.15325,
2024.
Long, Q., Li, Z., Gong, R., Wu, Y. N., Terzopoulos, D., and Gao, X. Teamcraft: A benchmark for multi-modal
multi-agent systems in minecraft.arXivpreprint arXiv:2412.05255, 2024.
Park, J. S., O’Brien, J., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. Generative agents: Interactive
simulacra of human behavior. InProceedings of the 36th annual acm symposium on user interface software
andtechnology, pp. 1–22, 2023.
Phiresky. procedural-cities.https://github.com/phiresky/procedural-cities, 2024.
Piao, J., Yan, Y., Zhang, J., Li, N., Yan, J., Lan, X., Lu, Z., Zheng, Z., Wang, J. Y., Zhou, D., et al. Agentsociety:
Large-scale simulation of llm-driven generative agents advances understanding of human behaviors and society.
arXivpreprint arXiv:2502.08691, 2025.
Puig, X., Undersander, E., Szot, A., Cote, M. D., Yang, T.-Y., Partsey, R., Desai, R., Clegg, A. W., Hlavac, M.,
Min, S. Y., et al. Habitat 3.0: A co-habitat for humans, avatars and robots.arXiv preprint arXiv:2310.13724,
2023.
Qiu, W., Zhong, F., Zhang, Y., Qiao, S., Xiao, Z., Kim, T. S., and Wang, Y. Unrealcv: Virtual worlds for
computer vision. In Proceedings of the 25th ACM International Conference on Multimedia, MM ’17, pp.
1221–1224, New York, NY, USA, 2017. Association for Computing Machinery. ISBN 9781450349062. doi:
10.1145/3123266.3129396. URLhttps://doi.org/10.1145/3123266.3129396.
Shah,S.,Dey,D.,Lovett,C.,andKapoor,A. Airsim: High-fidelityvisualandphysicalsimulationforautonomous
vehicles. InField and service robotics: Results of the 11th international conference, pp. 621–635. Springer,
2017.
Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L., and Anandkumar, A. Voyager: An
open-ended embodied agent with large language models.arXivpreprint arXiv:2305.16291, 2023.
Wang, H., Chen, J., Huang, W., Ben, Q., Wang, T., Mi, B., Huang, T., Zhao, S., Chen, Y., Yang, S., etal. Grutopia:
Dream general robots in a city at scale.arXiv preprint arXiv:2407.10943, 2024a.
Wang,Y.,Gao,Y.,Chen,X.,Jiang,H.,Li,S.,Yang,J.,Yin,Q.,Li,Z.,Li,X.,Yin,B.,etal. Memoryllm: Towards
self-updatable large language models.arXiv preprint arXiv:2402.04624, 2024b.
White, I., Nottingham, K., Maniar, A., Robinson, M., Lillemark, H., Maheshwari, M., Qin, L., and Ammanabrolu,
P. Collaborating action by action: A multi-agent llm framework for embodied reasoning.arXiv preprint
arXiv:2504.17950, 2025.
Wu, W., He, H., He, J., Wang, Y., Duan, C., Liu, Z., Li, Q., and Zhou, B. Metaurban: An embodied ai simulation
platform for urban micromobility.International ConferenceonLearning Representation, 2025.
Xiang, J., Liu, G., Gu, Y., Gao, Q., Ning, Y., Zha, Y., Feng, Z., Tao, T., Hao, S., Shi, Y., et al. Pandora: Towards
general world model with natural language actions and video states.arXivpreprint arXiv:2406.09455, 2024.
Xiang, J., Gu, Y., Liu, Z., Feng, Z., Gao, Q., Hu, Y., Huang, B., Liu, G., Yang, Y., Zhou, K., et al. PAN: A world
model for general, interactable, and long-horizon world simulation.arXivpreprint arXiv:2511.09057, 2025.
Xing, E., Deng, M., Hou, J., and Hu, Z. Critiques of world models.arXivpreprint arXiv:2507.05169, 2025.
Yang, Z., Zhang, Z., Zheng, Z., Jiang, Y., Gan, Z., Wang, Z., Ling, Z., Chen, J., Ma, M., Dong, B., et al. Oasis:
Open agents social interaction simulations on one million agents.arXivpreprint arXiv:2411.11581, 2024.
23

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. R., and Cao, Y. React: Synergizing reasoning and
acting in language models. InThe eleventhinternational conferenceonlearning representations, 2022.
Yu, X., Fu, J., Deng, R., and Han, W. Mineland: Simulating large-scale multi-agent interactions with limited
multimodal senses and physical needs.arXiv preprint arXiv:2403.19267, 2024.
Zhong, F., Wu, K., Wang, C., Chen, H., Ci, H., Li, Z., and Wang, Y. Unrealzoo: Enriching photo-realistic virtual
worlds for embodied ai. InProceedings of the IEEE/CVF International Conferenceon Computer Vision, pp.
5769–5779, 2025.
Zhou, Q., Zhang, H., Lin, X., Zhang, Z., Chen, Y., Liu, W., Zhang, Z., Chen, S., Fang, L., Lyu, Q., et al. Virtual
community: An open world for humans, robots, and society.arXivpreprint arXiv:2508.14893, 2025.
24
