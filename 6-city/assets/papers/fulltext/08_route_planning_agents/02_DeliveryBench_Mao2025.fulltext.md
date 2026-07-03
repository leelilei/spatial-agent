---
title: "DeliveryBench: Can Agents Earn Profit in Real World?"
source_pdf: "08_route_planning_agents\\02_DeliveryBench_Mao2025.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-07-03T12:08:19+00:00
page_count: 20
status: ok
text_char_count: 87043
quality_flags: []
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\08_route_planning_agents\02_DeliveryBench_Mao2025.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-07-03T12:08:19+00:00
- Page count: 20
- Status: ok
- Text chars: 87043
- Quality flags: none

## Metadata

- Title: DeliveryBench: Can Agents Earn Profit in Real World?
- Author: Lingjun Mao; Jiawei Ren; Kun Zhou; Jixuan Chen; Ziqiao Ma; Lianhui Qin
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

LLMs and VLMs are increasingly deployed as embodied agents, yet existing benchmarks largely revolve around simple short-term tasks and struggle to capture rich realistic constraints that shape real-world decision making. To close this gap, we propose DELIVERYBENCH, a cityscale embodied benchmark grounded in the real-world profession of food delivery. Food couriers naturally operate under long-horizon objectives (maximizing net profit over hours) while managing diverse constraints, e.g. delivery deadline, transportation expense, vehicle battery, and necessary interactions with other couriers and customers. DELIVERYBENCH instantiates this setting in procedurally generated 3D cities with diverse road networks, buildings, functional locations, transportation modes, and realistic resource dynamics, enabling systematic evaluation of constraint-aware, long-horizon planning. We benchmark a range of VLM-based agents across nine cities and compare them with human players. Our results reveal a substantial performance gap to humans, and find that these agents are short-sighted and frequently break basic commonsense constraints. Additionally, we observe distinct personalities across models (e.g. adventurous GPT-5 vs. conservative Claude), highlighting both the brittleness and the diversity of current VLM-based embodied agents in realistic, constraint-dense environments. Our code, data, and benchmark are available at https : / / deliverybench . github.io.

## Outline

- Introduction (page 1)
- Related Works (page 2)
- DeliveryBench (page 3)
  - Profit-Earning Task (page 3)
    - Task Formulation (page 3)
    - Test Environment (page 3)
  - Multifaceted Realistic Constraints (page 3)
  - Benchmark Construction (page 4)
    - Task Setup (page 4)
    - Single- and Multi-agent Settings (page 5)
    - Evaluation Metrics (page 5)
- Agent Design (page 5)
- Experiments (page 6)
  - Experimental Setup (page 6)
  - Single-Agent Planning Results (page 6)
    - Global Performance (page 6)
    - Fine-grained Analysis (page 6)
  - Multi-Agent Planning Results (page 7)
    - Global Performance (page 7)
    - Impact of Team Size (page 7)
  - Agent Planning-Style Analysis (page 8)
  - Context Engineering and Fine-tuning Effects (page 8)
- Conclusion (page 8)
- Future Research Directions (page 12)
- DeliveryBench Details (page 12)
  - City Maps and Spatial Layout (page 12)
  - Transportation Modes (page 12)
  - Points of Interest (page 12)
  - Food Attributes (page 13)
  - Order Attributes (page 14)
- Agent Input–Output Specification (page 14)
  - Input Prompt Structure (page 14)
  - Output Format (page 15)
  - Action Space (page 15)
- Human Data Collection (page 15)
  - Human Interaction GUI (page 15)
  - LLM-enhanced Annotation (page 16)
- Evaluation Details (page 16)
  - Fine-grained Metric Definitions (page 16)
  - Planning Style Evaluation Prompts (page 16)
- Additional Experimental Results (page 16)
  - Interaction Frequency with Team Size (page 16)
  - Model Behaviors and Planning Styles (page 17)
  - Detailed Results for Context Engineering and Supervised Fine-tuning (page 17)
  - Ablation Studies (page 18)
  - Variance and Stability Analysis (page 20)

## Markdown Content

DeliveryBench: Can Agents Earn Profit in Real World?
Lingjun Mao1 Jiawei Ren1 Kun Zhou1 Jixuan Chen1 Ziqiao Ma2 Lianhui Qin1
1University of California, San Diego 2University of Michigan
lingjun@ucsd.edu

Abstract
LLMs and VLMs are increasingly deployed as embodied agents, yet existing benchmarks largely revolve around
simple short-term tasks and struggle to capture rich realistic constraints that shape real-world decision making.
To close this gap, we propose DELIVERYBENCH, a cityscale embodied benchmark grounded in the real-world profession of food delivery. Food couriers naturally operate under long-horizon objectives (maximizing net profit
over hours) while managing diverse constraints, e.g. delivery deadline, transportation expense, vehicle battery, and
necessary interactions with other couriers and customers.
DELIVERYBENCH instantiates this setting in procedurally
generated 3D cities with diverse road networks, buildings, functional locations, transportation modes, and realistic resource dynamics, enabling systematic evaluation of
constraint-aware, long-horizon planning. We benchmark a
range of VLM-based agents across nine cities and compare
them with human players. Our results reveal a substantial performance gap to humans, and find that these agents
are short-sighted and frequently break basic commonsense
constraints. Additionally, we observe distinct personalities across models (e.g. adventurous GPT-5 vs. conservative Claude), highlighting both the brittleness and the diversity of current VLM-based embodied agents in realistic,
constraint-dense environments. Our code, data, and benchmark are available at https : / / deliverybench .
github.io.
1. Introduction
Large language models (LLMs) and vision-language models (VLMs) have exhibited strong abilities in solving diverse real-world problems, such as mathematics [27, 47]
and programming [4, 37]. Building on these advances, recent research has begun exploring embodied agents that
can perceive, reason, and act in physical environments
[15, 18, 19, 23, 25]. Looking ahead, humans increasingly
envision AI agents that may one day operate autonomously
5202
ceD
22
]IA.sc[
1v43291.2152:viXra

in the real world, helping with household tasks, participating in scientific discovery, or even earning income on
our behalf. To move toward this vision, the community
has developed a series of embodied-agent planning benchmarks that approximate real-world challenges through simulated environments, including 3D simulators [9, 52, 58]
and open-world games such as Minecraft [26, 48]. By defining grounded tasks and modeling realistic constraints, these
platforms help evaluate emerging agent abilities and provide data to guide future system design or model training.
A core capability for autonomous agents operating in
the real world is to earn profit and sustain themselves
economically. Beyond completing isolated tasks, a truly
capable agent should be able to survive, adapt, and even
develop a long-term career, navigating decisions that balance cost, benefit, and risk in the real world. Building
and evaluating such agents requires environments that faithfully reflect the complexity of everyday life, where decisions unfold over long horizons, and outcomes depend on
interacting physical, economic, resource, and social factors.
To study it, a realistic benchmark should not only support
embodied perception and action, but also model the incentives, constraints, and trade-offs that determine whether an
agent can accumulate profit and operate sustainably. However, as shown in Table 1, existing benchmarks fall short
of this goal. They either overemphasize short-horizon subtasks (e.g. navigation, pickup-and-drop) or fail to encode
the nontrivial constraints that shape real decision-making.
In this paper, we aim to introduce a realistic embodiedagent benchmark that demands long-horizon planning while
adhering to multiple real-world constraints. To minimize
the gap between simulation and reality, such a benchmark
must be grounded in tasks that (i) truly exist in the real
world, (ii) naturally involve long-term objectives, and (iii)
require to simultaneously manage diverse constraints. After surveying a variety of real-world careers, we find that
food delivery provides an ideal testbed. A delivery courier
operating in a city must carefully sequence routes using appropriate transportation, interleave supportive actions (e.g.
recharging an e-scooter or purchasing tickets), and collaborate with others when needed, all to maximize completed

Table 1. Comparison of major embodied benchmarks. Benchma
dimensions, with DELIVERYBENCH featuring longer horizons and
Sequence Length — Task Const
Benchmark
(action steps)
Spatial Time Resource Ph
BEHAVIOR [33] — ✗ ✗ ✗
ManiSkill2 [14] — ✗ ✗ ✗
CookBench [7] > 100 ✓ ✓ ✗
ALFRED [39] ∼12 ✓ ✗ ✗
ReALFRED [20] ∼12 ✓ ✗ ✗
EB-ALFRED [52] ∼12 ✓ ✗ ✗
ALFWorld [40] ∼6 ✓ ✗ ✗
VirtualHome [34] ∼9 ✓ ✗ ✗
ET-Plan-bench [56] <20 ✓ ✗ ✗
EmbRACE-3K [24] ∼10 ✓ ✗ ✗
TEACh [32] — ✓ ✗ ✗
ProcTHOR [12] — ✓ ✗ ✗
TaPA [50] ∼25 ✓ ✗ ✗
DELIVERYBENCH > 100 ✓ ✓ ✓
orders and net earnings. An example is shown in Figure 1.
We develop DELIVERYBENCH, a city-scale benchmark
that evaluates embodied agents under physically and socially grounded delivery scenarios. Agents act as autonomous couriers navigating procedurally generated cities
to maximize long-term profit. To capture the open-ended
nature of real-world operations, DELIVERYBENCH features
dynamic, interactive environments populated with diverse
points of interest (POIs) and multiple modes of transportation, going beyond prior urban simulators [8, 15, 49] that
primarily offer static visual scenes. As deliveries unfold
across multiple in-game hours, agents must manage resources (e.g. stamina depletion), adapt to changing conditions, and strategically balance efficiency, timing, and cost.
When multiple agents coexist, they further encounter social dynamics such as competition and collaboration. By
jointly modeling economic, physical, and social dynamics
within a unified embodied environment, DELIVERYBENCH
provides a realistic and action-driven setting to test whether
VLM-based agents can make and execute plans that genuinely improve financial outcomes.
Using DELIVERYBENCH, we conduct extensive experiments on (i) a diverse set of state-of-the-art VLMs,
(ii) under both single-agent and multi-agent settings, and
(iii) across nine cities with distinct geographic layouts.
Our results reveal several findings. Frontier VLM-based
agents lag far behind human players, struggling with longhorizon, constraint-aware decision making and frequently
making na¨ıve mistakes (e.g. forgetting to recharge an escooter). Multi-agent performance does not scale with team
size and typically peaks with two-agent teams, suggesting coordination challenges. Context engineering on larger
models yields significant gains in improving the earned
profit. Finally, different VLMs exhibit distinct behavioral
styles—GPT-5 appears adventurous, Claude more conser-

are compared across sequence length per episode and six constraint
e comprehensive multidimensional constraints (see Section 3.2).
Order #24: 2 min left Stamina low, need rest
s —
l Economic Social
✗ ✗ Time
Resource
✗ ✗
✗ ✗
Economic
✗ ✗
Spatial
✗ ✗
✗ ✗
✗ ✗
Spend $6 for
✗ ✗
energy drink
✗ ✗ 2 km remaining
✗ ✗
✗ ✓ Social
✗ ✗
Physical
✗ ✗
✓ ✓
Ice cream melting Need help from others
vative, and Gemini comparatively careless.
2. Related Works
VLM-based Embodied Agent. Recent advances in
VLMs [3, 10, 30] and large-scale manipulation datasets [6,
31] have driven the development of embodied agents [13,
54, 59] that translate language instructions into grounded visual understanding and executable actions. Although these
models have shown strong performance on short-horizon
tasks, they still struggle with complex long-horizon scenarios, motivating the emergence of new agentic-workflow designs [28, 46] and training-based approaches [13, 53, 59]
in embodied settings. Agentic workflows aim to improve
model adaptivity by incorporating mechanisms such as explicit memory [22], reflection [16, 53], and feedback-driven
correction [21, 55]. In contrast, training-based approaches
emphasize end-to-end [17] or distilled learning [43] frameworks that unify perception, reasoning, and control. Yet,
it remains unclear how well these embodied agent designs
perform when faced with tasks that truly reflect the longhorizon nature and complexity of real-world settings.
Embodied Agent Benchmarks. Existing embodied
benchmarks vary widely in abstraction level and planning
horizon. Low-level control benchmarks such as BEHAVIOR [42], iGibson [38], SAPIEN [51], and ManiSkill2 [14]
emphasize fine-grained motor control and physical realism,
requiring precise actuator adjustment and object manipulation. These environments rely on high-fidelity physics
engines (e.g., MuJoCo [45], PyBullet [11]) to simulate
realistic dynamics and evaluate action-level precision. By
contrast, long-horizon embodied benchmarks such as ALFRED [39], ReALFRED [20], and TEACh [32] emphasize
multi-step instruction following (typically 10–30 steps)
and structured task planning. Later extensions (e.g., Proc-

THOR [12], EmbRACE-3K [24]) expand scene diversity
and interaction complexity, while others such as VirtualHome [34], ALFWorld [40], and ET-Plan-bench [56]
abstract tasks into programs or textual plans to probe
reasoning and decomposition abilities. However, existing
benchmarks often overlook multidimensional constraints
(e.g., economic, resource, or social) and still fall short
of truly open-ended, long-horizon decision-making. We
introduce DELIVERYBENCH to address these gaps.
3. DeliveryBench
In this section, we present our DELIVERYBENCH, a longhorizon planning benchmark for evaluating VLM-based
embodied agents under realistic, constraint-rich settings.
DELIVERYBENCH integrates heterogeneous task objectives, realistic multifaceted constraints, and diverse evaluation dimensions. An overview is illustrated in Figure 1.
3.1. Profit-Earning Task
We center our benchmark on the food-delivery scenario,
where an agent works in a virtual city and aims to maximize net profit by continuously completing delivery orders.
3.1.1. Task Formulation
The delivery task is formalized as a long-horizon constrained optimization problem, where a VLM-based agent
as a courier seeks to maximize net profit over an operational
horizon T (e.g. two virtual hours). To do so, the agent must
plan and execute a sequence of delivery and supportive tasks
while respecting diverse real-world constraints.
Long-term Profit Target. The agent earns income from
customer orders in two forms: (i) a base salary E upon
base
successful delivery; and (ii) rating-based rewards E , derating
termined by factors such as delivery punctuality, freshness,
and special instructions (e.g. face-to-face delivery). Meanwhile, operational costs (C) arise from purchasing items or
services (e.g. recharging, vehicle rental). The total income
and net profit are therefore
E = E + E , P = E − C. (1)
base rating
Constrained Decision Making. At each step, the agent
receives an observation O and selects an action a =
t t
π (O ) via policy π . The goal is to obtain an optimal policy
i t i
π⋆ that maximizes expected net profit while satisfying all
i
constraints C. Let Π be the set of feasible policies whose
C
induced trajectories obey all c ∈ C. Formally,
π⋆ ∈ arg max E [P ] . (2)
i
πi∈ΠC
πi
To achieve this objective, the agent must coordinate both
delivery-related tasks that directly contribute to revenue

(e.g. selecting, fulfilling orders, or managing freshness decay) and supportive tasks that indirectly maintain operational feasibility (e.g. recharging, resting, purchasing supplies, or renting vehicles).
3.1.2. Test Environment
To support realistic and versatile task execution, we simulate a high-fidelity 3D urban environment featuring diverse
city layouts, interactive points of interest (POIs), multiple
transportation modes, and rich physical dynamics.
Simulated 3D City. Based on SimWorld [36]’s procedural generator, in DELIVERYBENCH, we simulate different
scales of 3D city layouts inside Unreal Engine. Each city
contains realistic buildings, roads, humans, and other objects, where the complete action trajectory of the agent can
be logged and visualized to the user for monitoring and
evaluation. Besides, the realistic weather control, physics
simulation, and other features inside Unreal Engine, support
us to flexibly vary the environments and ensure the reality.
Interactive Infrastructure and POIs. Across all cities,
buildings are sampled as POIs with equal probability, including restaurants, customer homes, convenience stores,
car rentals and rest areas. Infrastructure such as bus stops
and charging stations is placed along the road network.
When an agent arrives at these these POIs and infrastructures, it can trigger context-specific actions (e.g. picking up
food, recharging vehicles, renting cars, or resting).
Transportation, Navigation, and Physics. The environment supports multiple transportation modes (e.g. walking,
e-scooters, cars, and public transit), with different speed,
cost, and stamina profiles. Because current models struggle with low-level 3D navigation [35, 41], we provide a
waypoint-based system that follows shortest paths while
still exposing motion control. Physical dynamics (e.g. temperature, collisions, odor diffusion) further affect food quality during transit, requiring agents to adapt routing and
mode choices to preserve freshness.
3.2. Multifaceted Realistic Constraints
DELIVERYBENCH is designed to expose agents to the types
of constraints that structure real-world decision making. As
summarized in Table 1, we categorize these constraints into
six major types: spatial, time, resource, physical, economic,
and social. Each type governs what actions are feasible and
how desirable different plans are, and together they induce
a rich, tightly coupled planning landscape.
• Spatial constraints: Spatial constraints specify where
actions can be executed. Certain operations are only valid
at designated POIs: for instance, order pickup must occur at the associated restaurant, and recharging is only
possible at charging stations. The agent must therefore

Task: Example Delivery Flow
view orders 15 min pick up food 8 min charge e-scooter
13th road Restaurant A 19th road
Orders 100 and 108 are Order 108 will be Start charging...
along the same route. I ready in 5 minutes, Meanwhile, I’ll head
can accept both. so I’ll wait here. to the drop-off on foot.
Environment
W

Delivery Agent
2D Maps 3D Cities POIs Tr
Figure 1. Overview of the DELIVERYBENCH environment. The p
picking up, and delivering orders) and supporting actions (e.g., rec
navigate the city and visit appropriate POIs in a coherent
sequence to complete deliveries and supportive tasks.
• Time constraints: Time constraints restrict when tasks
can be performed. Each task is associated with a feasible time window, and some tasks must follow others
in a fixed order (e.g. a delivery must happen after the
corresponding pickup). When windows overlap without
ordering requirements, the agent can interleave tasks to
improve efficiency, such as delivering an existing order
while waiting for a new meal to be prepared. Some tasks
also have deadlines: late deliveries reduce income, and
the overall episode is limited by a maximum working duration, forcing the agent to use its time budget carefully.
• Resource constraints: Agents must manage consumable
resources such as stamina, vehicle battery, and cash to
stay operational. Depleting any resource impairs related
abilities (e.g. cannot ride a e-scooter without recharging).
To stay self-sustained, the agent needs to schedule supportive actions such as resting, recharging, or purchasing
consumables, and can sometimes convert one resource
into another, e.g. spending cash to restore stamina.
• Physical constraints: Physical constraints capture how
environmental dynamics affect delivery outcomes. Temperature, motion, and collisions all influence food condition (e.g. ice cream melts, fragile items can be damaged).
As a result, route planning and transport mode must consider not only distance and time but also the fragility and
perishability of delivered items.
• Economic constraints: Economic constraints arise from
the balance between income and cost. Agents can earn
money from base pay and rating-based bonuses, but incur
expenses for actions such as recharging vehicles, renting
cars, or buying supplies. Some of these expenses can

+ $10.66 - $3.00
...
deliver orders drop off food 10 min buy ice pack
18th road customer’s home Store
Time’s running out. Delivery’s done, but not Got ice pack. Picking
I’ll head out before the best rating. Getting up scooter, then
it’s too late. an ice pack first. accepting new orders.
Evaluation
I’ll grab order #104; you
Scooter two can take #108.
$20 Per Hour
Bus
Rating: 3.1/5.0
rtation Single-agent Setting Multi-agent Setting
ss consists of both core delivery actions (e.g., viewing, accepting,
ing e-scooters, purchasing items) that assist sustained delivery.
be viewed as investments in long-term gains, requiring
agents to balance immediate costs against future benefits.
• Social constraints: In multi-agent settings, multiple
couriers operate in the same city, introducing additional
constraints from collaboration and competition. Agents
may coordinate implicitly or explicitly, for example by
serving different regions or handing off orders and resources, but they also compete for scarce opportunities
such as high-value orders and nearby charging spots.
3.3. Benchmark Construction
In this part, we describe how we build DELIVERYBENCH,
outline the task setup for both single- and multi-agent
settings, and introduce metrics to evaluate the multidimensional capabilities of VLM-based agents.
3.3.1. Task Setup
Multi-level Tasks Creation. We evaluate agents on nine
procedurally generated city maps covering three difficulty
levels: small (11–15 roads), medium (16–25 roads), and
large (26–30 roads). Each environment maintains an order
pool with a fixed number of active delivery orders, which is
continuously replenished as orders are accepted. For each
order, the system randomly samples a restaurant (pickup location) and a residential building (dropoff location); the delivery wage and time limit are then computed from the travel
distance with slight stochastic perturbations for variability.
We maintain a certain percentage of orders contain special
customer requirements (e.g. face-to-face delivery), and violations incur penalties. Each episode terminates when the
agent reaches either the lifetime or API calls budget.
Agent State Management. At the beginning of each
episode, agents are spawned at a designated starting loca-

tion in the city. All agents share the same embodiment,
camera configuration, and base movement speed. Their initial states are the same, with an initial value of the stamina,
balance, battery level and other related features. As agents
act, stamina and battery levels decrease according to their
activities. At the end of each episode, we log the complete
interaction trajectory, income, and expenses, which form
the basis for our evaluation metrics.
3.3.2. Single- and Multi-agent Settings
Single-agent regime. In the single-agent setting, one
agent operates as the sole courier in each city. This regime
isolates individual planning, reasoning, and constrainthandling ability without interference from other agents.
Each agent is evaluated on all nine maps under the same
task-generation process and episode termination criteria,
with results averaged over multiple separate runs.
Multi-agent regime. In the multi-agent setting, we deploy eight instances of the same agent in a shared environment to study competition and cooperation. All agents
draw from a global order pool and share infrastructure such
as charging stations, producing competition for high-value
orders and scarce resources. To control the degree of cooperation, we group them into different team structures: 8 × 1
(eight independent agents, purely competitive), 4 × 2 (four
cooperating pairs), 2 × 4 (two groups of four), and 1 × 8 (a
single fully cooperative team). Within each group, agents
can communicate and respond to help requests, enabling behaviors such as handing off orders and recharging a teammate’s e-scooter. This design probes how social structure
and team size affect performance and interaction patterns.
3.3.3. Evaluation Metrics
Global profit. Our primary performance metric is the
hourly net profit P¯ achieved in a 2-hour virtual episode. We
report P¯ aggregated over episodes as the main indicator.
Fine-grained Capability Analysis. To diagnose where
agents succeed or fail, we further evaluate model behavior along following three capability dimensions, and more
details about the evaluation metrics are in Appendix E.1.
• High-level planning. We measure time-sensitive longterm planning via order-selection quality, on-time delivery rate, time efficiency (effective delivery time including
parallel orders, normalized by episode time), and active
time ratio (fraction of time spent on purposeful actions
rather than idling or being incapacitated).
• Resource management. We assess self-sustaining behavior using hourly stamina consumption, interruption
count (e.g. stops due to resource depletion), and proactive prevention ratio (how often agents replenish critical
resources before they run out).
• Physical/environmental adaptation. We evaluate how

well agents handle implicit physical and environmental
constraints using violation rate (fraction of orders with
constraint violations), food-quality rating, and customer
rating (both on a 0–5 scale). These metrics capture
whether agents can handle realistic constraints.
Input
First-Person View City Map Task Prompt
Memory
[last five actions]: ...
[last-step plan]: ...
Delivery Agent
Agent 2 Scooter Inventory Orders
(-322.6m, 236.9m)
Stamina: 56%
Earning: $216
Battery: Drink × 1 #2 Cake
Transport: Scooter 26% Ice Pack× 2 #4 Sushi
Output and Execution
Reflection and Reasoning: I've just reached the intersection at (-17.00m,
383.00m) and need to continue...
Action: MOVFEutur(e P-lan1: A3fter 3deliv.er3ing 7ordemr #16,, I'l l i4mm2edia4tely .ch7arge0 mym scoote)r at the nearby charging station 9 at (-38.79m, 412.00m) since my battery...
Future Plan: After delivering order #16, I'll immediately
charge my scooter at the nearby charging station 9 at...
Figure 2. Overview of the agent’s perception–planning–execution
loop in DELIVERYBENCH.
4. Agent Design
Each agent follows an perception–planning–execution loop
and operates as a high-level planner over a rich embodied
environment. At each timestep t, the agent perceives the
city, reasons about its current tasks and constraints, and selects an action to update its trajectory and long-term plan.
The framework is illustrated in Figure 2.
Observation Space. The observation space aggregates
multiple complementary views of the city and the agent’s
operational status. A global map oglobal shows the full city
t
layout, including the agent’s location and major points of
interest (POIs); a local map olocal provides finer-grained det
tails of the nearby area; and a first-person view (FPV) ofpv
t
renders the agent’s embodied perspective, capturing streets,
buildings, and surrounding objects. In addition, the agent
can query auxiliary information oaux via explicit actions,
t
such as checking current orders, inventory, or public transport schedules. The full observation at time t is thus
O = { oglobal, olocal, ofpv, oaux }.
t t t t t
Action Space. The action space in DELIVERYBENCH
supports both high-level decision making and fine-grained
embodied control, denoted as A. We provide its full details in Appendix C.3. High-level actions allow the agent

to delegate complex procedures to the simulator; for example, MOVE TO takes a target coordinate (or POI) and
triggers automatic path planning and navigation along the
road network. Low-level actions provide direct control
over movement and orientation, such as STEP FORWARD
or TURN AROUND. Interaction actions enable the agent to
manipulate the environment and manage resources, including picking up or dropping off orders, purchasing or using
tools (e.g. batteries), and recharging or renting vehicles.
Planning Pipeline. To model decision making over long
horizons, we adopt a lightweight planning pipeline. At
timestep t, the agent receives the current observation O
t
and maintains a short-term memory M = {a } of
t t−k:t−1
its past k actions. It also conditions on the previous plan
P , produced at timestep t−1, and the most recent failure
t
signal F , which indicates whether the last action or plan
t−1
did not succeed as intended. The policy π then outputs
θ
both the current action a ∈ A and an updated plan P :
t t+1
(a , P ) = π (O , M , P , F ).
t t+1 θ t t t t−1
Through this iterative update mechanism, the agent can continuously refine its future plan while reacting to new observations and failures in the environment, enabling more stable and adaptive behavior over long time horizons.
5. Experiments
5.1. Experimental Setup
Simulation Protocol. Our evaluation spans nine procedurally generated city maps, distributed across three difficulty levels. The order pool maintains 10 active orders, with
40% containing special customer requirements. We fix the
weather to sunny with a temperature of 22°C. All VLMbased agents start with full stamina, an initial balance of
$100, and an e-scooter at 50% battery, together with basic insulation to slow food-quality degradation during transit. Agents continue acting in the virtual world until they
reach either a 2-hour lifetime budget or a cap of 300 API
calls. The simulation speed is set to three times that of real
time. To avoid bias from model response latency, we pause
each agent’s lifetime clock, order timers, and food dynamics while it is reasoning. Time only advances when actions
are executed. We fix random seeds to ensure identical order
generation across runs. Each model is evaluated over eight
independent runs per map, reporting average performance.
Baseline Models. We test seven representative models: four closed-source models (GPT-5 [30], GPT4o [29], Claude-3.7-Sonnet [3], and Gemini-2.5-Flash [10])
and three open-source models (Qwen2.5-VL-72B [5],
Qwen2.5-VL-32B, and LLaMA-3.2-90B-Vision [1]). For
GPT-5, we use the “minimal” reasoning effort setting. We

fix a temperature of 0 and a maximum completion length of
512 tokens. VLMs are accessed via the OpenRouter1.
Human Baseline. To establish a meaningful reference for
single-agent performance, we include a human baseline by
recruiting three participants to independently complete the
same delivery tasks. Each participant interacts via a custom
GUI and follows the same evaluation protocol as the models. Interface details and screenshots are provided in the
Appendix D.1. We also record their delivery trajectories for
subsequent supervised fine-tuning experiments.
5.2. Single-Agent Planning Results
In the single-agent setting, only one VLM-based agent acts
as the food delivery courier across nine city maps.
5.2.1. Global Performance
Table 2 summarizes the net profits earned over a 2 virtualhour episode across models and city sizes. Closed-source
models consistently achieve higher net profit than opensource models, with Claude-3.7-Sonnet achieving the highest net profit across all city sizes. Its relatively better performance in large cities reflects an advantage in handling
long-horizon tasks, which involve longer delivery routes
and more complex routing decisions. In contrast, many
open-source models even incur losses in these cities. We
also observe that closed-source models tend to have higher
expenses, but much of this reflects strategic investment for
future deliveries (e.g., tool purchases), ultimately yielding
higher profits. Nonetheless, humans still outperform all
models by a wide margin across all city sizes. On average,
they earn over $50/hour, whereas the best model reaches
only about $30/hour. We analyze this gap via a multidimensional breakdown.
5.2.2. Fine-grained Analysis
Table 3 presents the detailed results of the fine-grained
trajectory-level analysis. Our key findings are as follows:
• Agents struggle to exploit temporal overlap compared
with humans. Agents fail to utilize their 2-hour window
efficiently, often idling between actions (e.g., waiting to
charge an e-scooter) instead of performing tasks concurrently (e.g., picking up food while charging), thereby
wasting considerable time. They tend to deliver orders
sequentially rather than leveraging spatiotemporal alignment to complete multiple deliveries in parallel. Consequently, their active-time and time efficiency remain substantially lower than those of humans.
• Agents remain less self-sustaining, often neglecting
resource management and preventive actions. Most
agents experience more than one interruption per hour
due to stamina or battery depletion, and their proactive
1https://openrouter.ai/

Table 2. Global performance of different models across city sizes,
into base earnings (E ), rating-based bonuses or penalties (E
base rating
Small City
Model
P¯ E E C
base rating
GPT-5 $27.4 $31.1 $11.5 $15.2
GPT-4o $10.4 $23.6 $6.8 $20.0
Claude-3.7-Sonnet $31.3 $30.1 $14.8 $13.6
Gemini-2.5-Flash $30.4 $34.8 $10.7 $15.0
Qwen2.5-VL-72B-Ins $5.4 $15.1 $3.8 $13.5
Qwen2.5-VL-32B-Ins $9.8 $15.7 $5.5 $11.4
LLaMA-3.2-90B-Vision-Ins $6.0 $9.7 $2.0 $5.7
Human $63.6 $77.8 $24.4 $38.6
Table 3. Fine-grained evaluation of model capabilities across three
cal/Environmental Adaptation. Arrows indicate whether higher (↑)
Planning
Model
Order↑ OnTime↑ TimeEff↑ Active
GPT-5 3.38 0.34 0.89 0.56
GPT-4o 3.36 0.38 0.54 0.58
Claude-3.7-Sonnet 3.51 0.44 0.91 0.59
Gemini-2.5-Flash 3.31 0.27 0.98 0.54
Qwen2.5-VL-72B-Ins 3.12 0.17 0.40 0.53
Qwen2.5-VL-32B-Ins 3.43 0.16 0.48 0.47
LLaMA-3.2-90B-Vision-Ins 3.31 0.04 0.54 0.53
Human 3.09 0.51 2.90 0.94
prevention ratios remain far below human results. Even
stronger models, such as Claude-3.7-Sonnet, often overreplenish when resources are sufficient and fail to act
when depletion is imminent.
• Agents struggle to handle implicit, environmentdependent constraints. They often overlook many implicit rules in delivery, choosing improper placement or
transport methods that degrade food quality and trigger
customer complaints (e.g., placing ice cream with hot
food, causing it to melt). These constraint violations remain frequent, with both food and customer ratings staying relatively low, ultimately reducing their income.
5.3. Multi-Agent Planning Results
We further test VLM-based agents in multi-agent settings,
where competition and collaboration naturally emerge.
5.3.1. Global Performance
We report model’s average net profit across all multi-agent
group configurations on the medium-20roads map, as
shown in Table 4. Most models show a decline in profit
when transitioning from the single-agent setting (without
any competition or coordination) to multi-agent conditions.
Notably, GPT-4o exhibits the steepest drop. Compared to
the purely competitive setup, all models except GPT-5 benefit from small-team cooperation, though their performance

asured by average hourly net profit ($/h), with detailed breakdown
nd expenses (C).
Medium City Large City
E E C P¯ E E C
base rating base rating
5 $32.9 $7.6 $14.0 $20.4 $25.6 $8.3 $13.4
9 $25.4 $4.9 $16.3 $11.9 $20.6 $5.3 $13.9
2 $35.7 $10.5 $14.9 $25.8 $30.1 $13.0 $17.2
0 $32.3 $8.3 $11.5 $23.9 $27.2 $9.0 $12.3
$15.6 $3.3 $12.6 -$2.7 $6.4 $1.1 $10.3
$11.5 $4.5 $11.5 -$0.1 $8.7 $2.3 $11.1
$11.6 $2.3 $11.4 -$0.9 $7.0 $1.3 $9.3
5 $73.6 $12.8 $34.9 $55.4 $74.3 $12.8 $31.6
mensions: High-level Planning, Resource Management, and Physiower (↓) values are better.
Resources Physical & Env.
Stamina↓ Interrupts↓ Prevention↑ Violations↓ Food↑ Cust↑
1.13 1.17 0.75 0.72 3.93 3.96
1.28 1.61 0.66 0.69 3.82 3.94
1.02 1.04 0.79 0.62 4.09 4.02
1.24 1.42 0.62 0.75 3.93 3.86
1.38 1.50 0.53 0.70 4.10 3.73
0.98 1.05 0.74 0.65 3.87 3.48
1.39 1.66 0.59 0.69 3.98 3.45
2.39 0.91 0.91 0.61 4.29 4.06
still remains well below the single-agent case.
Table 4. Multi-agent evaluation of average hourly net profit (P¯)
under five regimes: single-agent (1×1), fully competitive (8×1),
and three cooperative structures (4×2, 2×4, 1×8). Underlines indicate the best-performing multi-agent configuration for each model.
Per-Agent Hourly Net Profit (P¯, $/h)
Model
(1×1) 8×1 4×2 2×4 1×8
GPT-5 $27.3 $20.5 $19.5 $8.7 $16.5
GPT-4o $16.9 $5.3 $5.5 $5.0 $6.9
Claude-3.7-Sonnet $31.7 $14.2 $22.6 $10.4 $9.6
Gemini-2.5-Flash $28.4 $21.2 $24.3 $12.6 $15.1
Qwen2.5-VL-72B-Ins $10.1 $4.5 $7.0 $8.7 $5.8
Qwen2.5-VL-32B-Ins $6.0 $3.0 $4.6 $3.4 $1.4
LLaMA-3.2-90B-Vision-Ins $1.4 $1.4 $2.0 $1.3 $1.5
5.3.2. Impact of Team Size
We analyze how team sizes affect coordination and interaction. As shown in Table 4, most models perform best in
pairs, but some show declines as team size grows, especially in the four-agent setting. Although interaction events
(e.g. messaging or help requests) rise with team size, they
also increase coordination overhead, as agents must manage more potential help requests alongside their own tasks,
making it harder to prioritize effectively (e.g., accepting
help requests but forgetting to act). The detailed change
in interaction frequency is provided in the Appendix F.1.

5.4. Agent Planning-Style Analysis
During both single- and multi-agent evaluations, we observe distinct decision-making and planning styles across
models. For instance, Claude behaves more cautiously,
choosing to head to a charging station once the e-scooter
battery is low and pausing other tasks, whereas GPT-5 is
more aggressive, often completing deliveries even with a
nearly depleted battery. To further analyze model behavior
in constraint-dense, real-world-like environments, we randomly sample delivery trajectories from each model and
pair them with their outcomes. GPT-4o then evaluates each
decision step across six dimensions on a 0–10 scale, including Risk (how aggressive the decision is), Horizon (preference for long-term planning or short-term gains), Explore
(tendency to try new strategies), Coop (willingness to cooperate with others), Detail (attention to operational and contextual factors), and Flex (frequency of plan adjustments).
Dimensions irrelevant to a given step are skipped. Figure 3
presents representative models with their planning styles
and example outputs, and the full set of model evaluations,
including action patterns, transportation modes, and spending distributions, is provided in the Appendix F.2.
GPT-5 Claude-3.7 Gemini-2.5
A bold adventurer A calm and A slightly careless
who dares to try rational strategist free spirit
Battery critically low My e-scooter battery Action: Put the items
at 5% (~123 m range), is low at 39% and my from order #6 (ice
but still enough to energy is at 40%, so I cream, stinky tofu,
complete the drop-off... should recharge both and hot dog) into
I’ll prioritize finishing before taking new compartment A.
the delivery first to... orders...
Low battery, Medium battery, Put everything together
deliver first. recharge first. without thinking twice.
Figure 3. Comparison of model planning styles across six behavior
dimensions, with example outputs provided as case studies.
5.5. Context Engineering and Fine-tuning Effects
We evaluate two widely-used strategies for improving performance: Context Engineering and Supervised Fine-tuning
(SFT) with human demonstrations, along with a baseline
where the model outputs only raw actions without explicit
planning for reference. All evaluations in this section are
conducted on the medium-20roads map.
Context Engineering. Context Engineering aims to enhance model reasoning through self-reflection on prior experience and environmental feedback. We evaluate two
methods: Agentic Context Engineering (ACE [57]) and Dynamic Cheatsheet (DC [44]). Each model undergoes a 4-

Table 5. Comparative results of context engineering and supervised fine-tuning. Green and red highlights improvements and regressions over the with-Plan baseline, respectively.
Model P¯ E C
GPT-5 (with Plan) $27.3 $38.8 $11.5
GPT-5 (w/o Plan) $8.6 $16.8 $8.2
GPT-5 (with Plan + ACE) $33.2 $46.1 $12.9
GPT-5 (with Plan + DC) $36.2 $47.3 $11.2
Claude-3.7-Sonnet (with Plan) $31.7 $51.6 $19.9
Claude-3.7-Sonnet (w/o Plan) $19.2 $25.6 $6.3
Claude-3.7-Sonnet (with Plan + ACE) $40.5 $56.3 $15.8
Claude-3.7-Sonnet (with Plan + DC) $44.5 $57.1 $12.6
Qwen2.5-VL-72B (with Plan) $2.3 $14.0 $11.7
Qwen2.5-VL-72B (w/o Plan) $2.0 $10.8 $8.8
Qwen2.5-VL-72B (with Plan + ACE) $0.1 $14.3 $14.2
Qwen2.5-VL-72B (with Plan + DC) $3.2 $16.6 $13.4
LLaVA-OneVision-8B (original) -$7.2 $4.4 $11.6
LLaVA-OneVision-8B (raw-action-ft) -$7.8 $7.2 $15.0
LLaVA-OneVision-8B (annotated-ft) $3.2 $12.7 $9.5
hour warm-up phase, during which it updates an internal
memory by summarizing key patterns from its past trajectories. This memory is then frozen for evaluation. As shown
in Table 4, context engineering consistently improves performance for GPT-5 and Claude-3.7-Sonnet, while the
weaker open-source model Qwen2.5-VL-72B benefits little,
with ACE even leading to a decline. Examples of the models’ memory summaries are provided in the Appendix F.3.
Supervised Fine-tuning. We fine-tune the open-source
model LLaVA-OneVision-8B [2] on 9 human delivery trajectories (2,110 observation–action pairs) collected from
the best-performing human on each map. We compare three
variants: (i) the original pretrained model, (ii) a model finetuned directly on human actions, and (iii) a model finetuned on annotated human actions, where each action is enriched with reasoning, reflection, and future plans generated
by GPT-4o. All variants are trained for 3 epochs. The model
fine-tuned on raw human actions exhibits more human-like
behaviors (e.g., bundling orders) but performs worse, often imitating patterns without understanding preconditions
(e.g. charging without reaching a station). In contrast, the
annotated variant performs better, achieving higher profits
and learning human-like parallel task strategies that significantly improve time efficiency and active ratio. The finegrained analysis can be found in Appendix F.3.
6. Conclusion
We introduced DELIVERYBENCH, an embodied benchmark
to evaluate VLM-based agents under realistic, long-horizon
delivery scenarios. In the grounded food-delivery profession, agents must maximize long-term profit while simultaneously handling spatial, temporal, resource, physical, eco-

nomic, and social constraints. By instantiating these demands in simulated 3D cities with diverse layouts, multiple transportation modes, and both single- and multi-agent
regimes, DELIVERYBENCH provided a more faithful and
diagnostic testbed for studying constraint-aware planning.
Our experiments across nine cities with a range of state-ofthe-art VLMs reveal a substantial gap to human couriers,
exhibiting their short-sighted behavior and frequent break
of basic commonsense constraints. Besides, different models display distinct behavioral personalities, highlighting
both diversity and brittleness in current VLM-based agents.
References
[1] Meta AI. Llama 3.2 vision (90b) model card. https:
//huggingface.co/meta- llama/Llama- 3.290B-Vision, 2024. Accessed 2025-10-25. 6
[2] Xiang An, Yin Xie, Kaicheng Yang, Wenkang Zhang,
Xiuwei Zhao, Zheng Cheng, Yirui Wang, Songcen Xu,
Changrui Chen, Chunsheng Wu, et al. Llava-onevision-1.5:
Fully open framework for democratized multimodal training.
arXiv preprint arXiv:2509.23661, 2025. 8
[3] Anthropic. Claude 3.7 sonnet and claude code. https:
/ / www . anthropic . com / news / claude - 3 - 7 -
sonnet, 2025. Accessed: 2025-02-24. 2, 6
[4] Anthropic. Claude code: Best practices for agentic coding,
2025. 1
[5] Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin
Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun
Tang, et al. Qwen2. 5-vl technical report. arXiv preprint
arXiv:2502.13923, 2025. 6
[6] Qingwen Bu, Jisong Cai, Li Chen, Xiuqi Cui, Yan Ding,
Siyuan Feng, Shenyuan Gao, Xindong He, Xuan Hu, Xu
Huang, et al. Agibot world colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. IROS, 2025. 2
[7] Muzhen Cai, Xiubo Chen, Yining An, Jiaxin Zhang,
Xuesong Wang, Wang Xu, Weinan Zhang, and Ting Liu.
Cookbench: A long-horizon embodied planning benchmark for complex cooking scenarios. arXiv preprint
arXiv:2508.03232v1, 2025. 2
[8] Feng Chen et al. Embodiedcity: A benchmark platform
for embodied agent in real-world city environment. arXiv
preprint arXiv:2410.09604, 2024. 2
[9] Zhili Cheng, Yuge Tu, Ran Li, Shiqi Dai, Jinyi Hu,
Shengding Hu, Jiahao Li, Yang Shi, Tianyu Yu, Weize Chen,
et al. Embodiedeval: Evaluate multimodal llms as embodied
agents. arXiv preprint arXiv:2501.11858, 2025. 1
[10] Gheorghe Comanici, Eric Bieber, Mike Schaekermann, Ice
Pasupat, Noveen Sachdeva, Inderjit Dhillon, Marcel Blistein, Ori Ram, Dan Zhang, Evan Rosen, et al. Gemini 2.5:
Pushing the frontier with advanced reasoning, multimodality,
long context, and next generation agentic capabilities. arXiv
preprint arXiv:2507.06261, 2025. 2, 6
[11] Erwin Coumans and Yunfei Bai. Pybullet, a python module for physics simulation for games, robotics and machine
learning, 2016. 2

[12] Matt Deitke, Eli VanderBilt, Alvaro Herrasti, Luca Weihs,
Kiana Ehsani, Jordi Salvador, Winson Han, Eric Kolve,
Aniruddha Kembhavi, and Roozbeh Mottaghi. Procthor: Large-scale embodied ai using procedural generation.
NeurIPS, 2022. 2, 3
[13] Danny Driess, Fei Xia, Mehdi SM Sajjadi, Corey Lynch,
Aakanksha Chowdhery, Ayzaan Wahid, Jonathan Tompson,
Quan Vuong, Tianhe Yu, Wenlong Huang, et al. Palm-e: An
embodied multimodal language model. ICML, 2023. 2
[14] Jiayuan Gu, Fanbo Xiang, Xuanlin Li, Zhan Ling, Xiqiang
Liu, Tongzhou Mu, Yihe Tang, Stone Tao, Xinyue Wei, Yunchao Yao, et al. Maniskill2: A unified benchmark for generalizable manipulation skills. ICLR, 2023. 2
[15] Yining Hong, Rui Sun, Bingxuan Li, Xingcheng Yao,
Maxine Wu, Alexander Chien, Da Yin, Ying Nian Wu,
Zhecan James Wang, and Kai-Wei Chang. Embodied web
agents: Bridging physical-digital realms for integrated agent
intelligence. NeurIPS, 2025. 1, 2
[16] Wenlong Huang, Fei Xia, Ted Xiao, Harris Chan, Jacky
Liang, Pete Florence, Andy Zeng, Jonathan Tompson, Igor
Mordatch, Yevgen Chebotar, et al. Inner monologue: Embodied reasoning through planning with language models.
CoRL, 2023. 2
[17] Physical Intelligence, Kevin Black, Noah Brown, James
Darpinian, Karan Dhabalia, Danny Driess, Adnan Esmail,
Michael Equi, Chelsea Finn, Niccolo Fusai, et al. π0. 5:
a vision-language-action model with open-world generalization. arXiv preprint arXiv:2505.21906, 2025. 2
[18] Md Mofijul Islam, Alexi Gladstone, Riashat Islam, and Tariq
Iqbal. Eqa-mx: Embodied question answering using multimodal expression. 2023. 1
[19] Bosung Kim and Prithviraj Ammanabrolu. Beyond needle
(s) in the embodied haystack: Environment, architecture,
and training considerations for long context reasoning. arXiv
preprint arXiv:2505.16928, 2025. 1
[20] Taewoong Kim, Cheolhong Min, Byeonghwi Kim, Jinyeon
Kim, Wonje Jeung, and Jonghyun Choi. Realfred: An embodied instruction following benchmark in photo-realistic
environments. ECCV, 2024. 2
[21] Nishanth Kumar, William Shen, Fabio Ramos, Dieter Fox,
Toma´s Lozano-Pe´rez, Leslie Pack Kaelbling, and Caelan Reed Garrett. Open-world task and motion planning via
vision-language model inferred constraints. ICRA, 2025. 2
[22] Mingcong Lei, Ge Wang, Yiming Zhao, Zhixin Mai, Qing
Zhao, Yao Guo, Zhen Li, Shuguang Cui, Yatong Han, and
Jinke Ren. Clea: Closed-loop embodied agent for enhancing
task execution in dynamic environments. IROS, 2025. 2
[23] Manling Li, Shiyu Zhao, Qineng Wang, Kangrui Wang, Yu
Zhou, Sanjana Srivastava, Cem Gokmen, Tony Lee, Erran Li
Li, Ruohan Zhang, et al. Embodied agent interface: Benchmarking llms for embodied decision making. NeurIPS, 2024.
1
[24] Mingxian Lin, Wei Huang, Yitang Li, Chengjie Jiang, Kui
Wu, Fangwei Zhong, Shengju Qian, Xin Wang, and Xiaojuan Qi. Embrace-3k: Embodied reasoning and action in
complex environments. arXiv preprint arXiv:2507.10548,
2025. 2, 3

[25] Xiao Liu, Tianjie Zhang, Yu Gu, Iat Long Iong, Yifan Xu,
Xixuan Song, Shudan Zhang, Hanyu Lai, Xinyi Liu, Hanlin
Zhao, et al. Visualagentbench: Towards large multimodal
models as visual foundation agents. ICLR, 2025. 1
[26] Qian Long, Zhi Li, Ran Gong, Ying Nian Wu, Demetri
Terzopoulos, and Xiaofeng Gao. Teamcraft: A benchmark
for multi-modal multi-agent systems in minecraft. arXiv
preprint arXiv:2412.05255, 2024. 1
[27] Xiaoliang Luo, Akilles Rechardt, Guangzhi Sun, Kevin K
Nejad, Felipe Ya´n˜ez, Bati Yilmaz, Kangjoo Lee, Alexandra O Cohen, Valentina Borghesani, Anton Pashkov, et al.
Large language models surpass human experts in predicting
neuroscience results. Nature human behaviour, 2025. 1
[28] Yao Mu, Qinglong Zhang, Mengkang Hu, Wenhai Wang,
Mingyu Ding, Jun Jin, Bin Wang, Jifeng Dai, Yu Qiao, and
Ping Luo. Embodiedgpt: Vision-language pre-training via
embodied chain of thought. NeurIPS, 2023. 2
[29] OpenAI. Gpt-4o mini. https://openai.com/index/
gpt - 4o - mini - advancing - cost - efficient -
intelligence/, 2024. Accessed: 2024-07-18. 6
[30] OpenAI. Gpt-5 system card. https://openai.com/
index/gpt-5-system-card/, 2025. Accessed 202510-25. 2, 6
[31] Abby O’Neill, Abdul Rehman, Abhiram Maddukuri, Abhishek Gupta, Abhishek Padalkar, Abraham Lee, Acorn Pooley, Agrim Gupta, Ajay Mandlekar, Ajinkya Jain, et al. Open
x-embodiment: Robotic learning datasets and rt-x models:
Open x-embodiment collaboration 0. 2024. 2
[32] Aishwarya Padmakumar, Jesse Thomason, Ayush Shrivastava, Patrick Lange, Anjali Narayan-Chen, Spandana Gella,
Robinson Piramithu, Gokhan Tur, and Dilek Hakkani-Tur.
Teach: Task-driven embodied agents that chat. AAAI, 2022.
2
[33] Yingqian Pan, Yufan Zhou, Zang Feng, Wenbo Hu, Xiaotian
Deng, Junyi Yang, Yali Liu, Guangjun Liu, Jie Hu, Guangtao
Yu, Ruijie He, Hong Liu, Yang Zhang, Qihuan Wu, Jianye
Hao, Wenxue Wang, Jun Guo, and Yang Liu. Large language models overcome the machine penalty when acting
fairly but not when acting selfishly or altruistically. arXiv
preprint arXiv:2410.03724, 2024. 2
[34] Xavier Puig, Kevin Ra, Marko Boben, Jiaman Li, Tingwu
Wang, Sanja Fidler, and Antonio Torralba. Virtualhome:
Simulating household activities via programs. CVPR, 2018.
2, 3
[35] Ram Ramrakhya, Eric Undersander, Dhruv Batra, and Abhishek Das. Habitat-web: Learning embodied object-search
strategies from human demonstrations at scale. CVPR, 2022.
3
[36] Jiawei Ren, Yan Zhuang, Xiaokang Ye, Lingjun Mao,
Xuhong He, Jianzhi Shen, Mrinaal Dogra, Yiming Liang,
Ruixuan Zhang, Tianai Yue, et al. Simworld: An open-ended
realistic simulator for autonomous agents in physical and social worlds. NeurIPS, 2025. 3
[37] Maxime Robeyns, Martin Szummer, and Laurence Aitchison. A self-improving coding agent. ICLR Workshop (SSIFM), 2025. 1

[38] Bokui Shen, Fei Xia, Chengshu Li, Roberto Mart´ın-Mart´ın,
Linxi Fan, Guanzhi Wang, Claudia Pe´rez-D’Arpino, Shyamal Buch, Sanjana Srivastava, Lyne Tchapmi, et al. igibson
1.0: A simulation environment for interactive tasks in large
realistic scenes. 2021. 2
[39] Mohit Shridhar, Jesse Thomason, Daniel Gordon, Yonatan
Bisk, Winson Han, Roozbeh Mottaghi, Luke Zettlemoyer,
and Dieter Fox. Alfred: A benchmark for interpreting
grounded instructions for everyday tasks. 2020. 2
[40] Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Coˆte´,
Yonatan Bisk, Adam Trischler, and Matthew Hausknecht.
Alfworld: Aligning text and embodied environments for interactive learning. ICLR, 2021. 2, 3
[41] Xinshuai Song, Weixing Chen, Yang Liu, Weikai Chen,
Guanbin Li, and Liang Lin. Towards long-horizon visionlanguage navigation: Platform, benchmark and method.
CVPR, 2025. 3
[42] Sanjana Srivastava, Chengshu Li, Michael Graf, Unnat
Aneja, Fei Xia, Gokul Demir, Roberto Martin-Martin, Joe
Su, N. Hudson Lang, Jiajun Wu, et al. Behavior: Benchmark
for everyday household activities in virtual, interactive, and
ecological environments. CoRL, 2021. 2
[43] Theodore Sumers, Kenneth Marino, Arun Ahuja, Rob Fergus, and Ishita Dasgupta. Distilling internet-scale visionlanguage models into embodied agents. ICML, 2023. 2
[44] Mirac Suzgun, Mert Yuksekgonul, Federico Bianchi, Dan
Jurafsky, and James Zou. Dynamic cheatsheet: Testtime learning with adaptive memory. arXiv preprint
arXiv:2504.07952, 2025. 8
[45] Emanuel Todorov, Tom Erez, and Yuval Tassa. Mujoco: A
physics engine for model-based control. 2012. 2
[46] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar,
Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anandkumar. Voyager: An open-ended embodied agent with large
language models. TMLR, 2023. 2
[47] Ke Wang, Junting Pan, Linda Wei, Aojun Zhou, Weikang
Shi, Zimu Lu, Han Xiao, Yunqiao Yang, Houxing Ren,
Mingjie Zhan, et al. Mathcoder-vl: Bridging vision and
code for enhanced multimodal mathematical reasoning. ACL
Findings, 2025. 1
[48] Isadora White, Kolby Nottingham, Ayush Maniar, Max
Robinson, Hansen Lillemark, Mehul Maheshwari, Lianhui
Qin, and Prithviraj Ammanabrolu. Collaborating action by
action: A multi-agent llm framework for embodied reasoning. arXiv preprint arXiv:2504.17950, 2025. 1
[49] Wayne Wu, Honglin He, Jack He, Yiran Wang, Chenda
Duan, Zhizheng Liu, Quanyi Li, and Bolei Zhou. Metaurban: An embodied ai simulation platform for urban micromobility. ICLR, 2025. 2
[50] Zhenyu Wu, Ziwei Wang, Xiuwei Xu, Jiwen Lu, and Haibin
Yan. Embodied task planning with large language models.
arXiv preprint arXiv:2307.01848, 2023. 2
[51] Fanbo Xiang, Yuzhe Qin, Kaichun Mo, Yikuan Xia, Hao
Zhu, Fangchen Liu, Minghua Liu, Hanxiao Jiang, Yifu Yuan,
He Wang, et al. Sapien: A simulated part-based interactive
environment. CVPR, 2020. 2
[52] Rui Yang, Hanyang Chen, Junyu Zhang, Mark Zhao, Cheng
Qian, Kangrui Wang, Qineng Wang, Teja Venkat Koripella,

Marziyeh Movahedi, Manling Li, et al. Embodiedbench:
Comprehensive benchmarking multi-modal large language
models for vision-driven embodied agents. ICML, 2025. 1,
2
[53] Yi Yang, Jiaxuan Sun, Siqi Kou, Yihan Wang, and Zhijie Deng. Lohovla: A unified vision-language-action
model for long-horizon embodied tasks. arXiv preprint
arXiv:2506.00411, 2025. 2
[54] Zhejian Yang, Yongchao Chen, Xueyang Zhou, Jiangyue
Yan, Dingjie Song, Yinuo Liu, Yuting Li, Yu Zhang, Pan
Zhou, Hechang Chen, et al. Agentic robot: A brain-inspired
framework for vision-language-action models in embodied
agents. arXiv preprint arXiv:2505.23450, 2025. 2
[55] Zhutian Yang, Caelan Garrett, Dieter Fox, Toma´s LozanoPe´rez, and Leslie Pack Kaelbling. Guiding long-horizon task
and motion planning with vision language models. 2025. 2
[56] Lingfeng Zhang, Yuening Wang, Hongjian Gu, Atia
Hamidizadeh, Zhanguang Zhang, Yuecheng Liu, Yutong
Wang, David Gamaliel Arcos Bravo, Junyi Dong, Shunbo
Zhou, et al. Et-plan-bench: Embodied task-level planning
benchmark towards spatial-temporal cognition with foundation models. IROS, 2025. 2, 3
[57] Qizheng Zhang, Changran Hu, Shubhangi Upasani, Boyuan
Ma, Fenglu Hong, Vamsidhar Kamanuru, Jay Rainton, Chen
Wu, Mengmeng Ji, Hanchen Li, et al. Agentic context engineering: Evolving contexts for self-improving language
models. arXiv preprint arXiv:2510.04618, 2025. 8
[58] Fangwei Zhong, Kui Wu, Churan Wang, Hao Chen, Hai Ci,
Zhoujun Li, and Yizhou Wang. Unrealzoo: Enriching photorealistic virtual worlds for embodied ai. ICCV, 2025. 1
[59] Brianna Zitkovich, Tianhe Yu, Sichun Xu, Peng Xu, Ted
Xiao, Fei Xia, Jialin Wu, Paul Wohlhart, Stefan Welker,
Ayzaan Wahid, et al. Rt-2: Vision-language-action models
transfer web knowledge to robotic control. In CoRL, 2023. 2

A. Future Research Directions
DELIVERYBENCH simulates real-world food-delivery task,
which naturally involves long-horizon objectives (e.g. maximizing net profit) intertwined with diverse physical, social,
and economic constraints, providing a testbed that more
faithfully reflects the complexity of real-world decisionmaking. As a next step, we aim to further extend this platform in several important directions:
Real-time reasoning. In the current setup, the simulator
pauses the environment whenever the model is “thinking”:
order timers, battery levels, food freshness, and other dynamic states are frozen. In contrast, real-world decisionmaking unfolds in a continuously evolving environment,
where time keeps progressing and other entities (e.g. couriers, pedestrians, customers) act in parallel. We plan to
support real-time planning in future versions, where agents
must reason within this dynamic setting and adapt to ongoing temporal and environmental changes (e.g., adjusting
their trajectory in real time to avoid pedestrians).
Learning from interaction data. Although DELIVERYBENCH currently serves primarily as an evaluation benchmark, the platform naturally supports collecting rich interaction data at scale. Such data can be used to study how different learning paradigms, including reinforcement learning, imitation learning, and memory-augmented agents,
adapt to our long-horizon delivery task. As shown in Section 5.5, we conduct preliminary experiments using basic
context engineering and small-scale supervised fine-tuning
from human demonstrations, but there remains substantial
room for further investigation, especially in understanding
how these methods scale as data and model size increase.
B. DELIVERYBENCH Details
We provide additional details of DELIVERYBENCH, including map construction, transportation and POI design, and
several task-specific mechanisms (e.g. food categories).
B.1. City Maps and Spatial Layout
We construct nine city maps spanning three difficulty levels: small (11–15 roads), medium (16–25 roads), and large
(26–30 roads), with three maps in each category. Every
map contains a diverse set of POIs distributed across the
road network, sampled under a uniform spatial density such
that larger maps naturally include more POIs. For each city,
we select the largest inscribed loop as the bus route, evenly
place bus stops along it, and deploy a single bus that continuously travels on this route. The overall spatial layouts
of the maps are illustrated in Figure 4, and the POI statistics
for each map are summarized in Table 7.

11-roads 13-roads 15-roads
18-roads 20-roads 22-roads
26-roads 28-roads 30-roads
Figure 4. Overview of the nine procedurally constructed city maps
used in our experiments.
B.2. Transportation Modes
We provide multiple transportation modes, including escooter, walking, driving, and public transit such as buses.
These modes differ in speed, stamina consumption, and additional costs (e.g., bus fares, car rental fees), requiring the
model to make context-dependent trade-offs. A summary
of these transportation modes is provided in Table 6.
Table 6. Different transportation modes in DeliveryBench.
Mode Speed (m/s) Stamina (%/m) Extra Cost
walk 2.0 0.08 –
e-scooter 6.0 0.01 battery 0.04%/m
drag e-scooter 1.5 0.10 –
car 12.0 0.008 rental $1.0/min
bus 10.0 0.006 $1 fare
B.3. Points of Interest
Our constructed city includes various POIs, each serving
distinct functions. Agents must navigate the city and interact with these POIs to accomplish different subtasks.
Restaurant. Restaurants serve as the pickup locations for
delivery orders. Once an order is accepted, the restaurant
begins food preparation. When the meal is ready, its state
(e.g., temperature or freshness) starts changing over time,
and the agent can visit the restaurant to collect it.
Store. Stores provide agents with access to purchasable
items, including energy drinks, e-scooter batteries, and
food-preservation tools such as ice packs and heat packs.
The prices and functions of these items are listed in Table 8.
Rest Area. Rest areas provide couriers with a place to
recover stamina, allowing agents to restore 10% of their
stamina per minute at no cost while resting.

Table 7. Counts of points of interest
Size #Roads Restaurant Store Rest Area Car
11 4 4 1
small 13 5 4 1
15 4 5 2
18 6 7 2
medium 20 5 7 3
22 7 7 3
26 7 9 4
large 28 8 11 3
30 9 9 4
Table 8. Prices and functions of store items.
Item Price ($) Function
Energy Drink 6 Restore 50% of stamina
E-Scooter Battery 10 Fully recharge e-scooter battery
Ice Pack 3 Cool food temperature
Heat Pack 3 Heat food temperature
Car Rental. Car rental stations allow agents to rent and
return cars. An agent can pick up a car at any rental station
and return it to any other. Rental fees are time-based and
cost $0.5 per minute, even when the vehicle is not in use.
Hospital. Hospitals handle agent recovery when stamina
is fully depleted. An agent who collapses is automatically
sent to a hospital for a 30-minute recovery process, during
which no actions can be performed and a $5 service fee is
charged. All environment dynamics, such as order timers
and food freshness, continue to progress normally. After
recovery, the agent resumes work starting from the hospital.
Charging Station. Charging stations provide recharging
services for agents’ e-scooters, with each station able to
serve only one scooter at a time. The charging cost is $0.05
per unit of battery, and the charging speed is 10 units per
minute. Agents may stop charging and retrieve their escooters at any time.
Bus Station. Bus stations allow agents to wait for the arriving bus and board it when it reaches the stop. Upon arrival, agents may pay a $1 ticket fee and ride the bus to any
other station on the route.
B.4. Food Attributes
We simulate 22 food types, each with a preparation time
and several quality-related attributes. These attributes influence how the food evolves during delivery and influence
the agent’s strategy. The main factors include temperature
dynamics, fragility, and odor sensitivity.
Temperature Dynamics. Temperature is the most influential factor affecting food quality. After preparation, a
food item’s temperature evolves according to a lightweight

Is) on each DELIVERYBENCH map.
al Hospital Charging Station Bus Station Bus Route
1 10 4 1
1 15 6 1
1 18 6 1
1 20 6 1
1 24 6 1
1 22 8 1
1 29 8 1
1 29 8 1
1 24 8 1
thermodynamic model that simulates heat exchange with its
surroundings. Each item has a temperature T and heat cai
pacity C , while each storage compartment has an air node
i
with temperature T and a small heat capacity C . Items
a ab
outside the insulated bag exchange heat with ambient air,
whereas items inside the bag primarily exchange heat with
others in the same compartment. We update temperatures
using a discrete heat-exchange rule with timestep ∆t:
(cid:88)
S = C (T − T ), (3)
i i a
i
S
T new = T + α , (4)
a a C
ab
T new = T + α(T − T ), (5)
i i a i
where S denotes the net heat flow from the food items to the
air node. The coefficient α = ∆t/τ controls the exchange
ex
rate and is clipped to α ≤ 0.5 for numerical stability, while
τ determines the effective speed of heat transfer.
ex
Fragility. Items such as cakes and soups are sensitive to
movement and require gentle handling. Actions involving
rapid movement (e.g., riding an e-scooter at high speed or
running) introduce a risk of damaging these items. Each
fragile item accumulates a fragility score when subjected to
excessive vibration or acceleration. Once the accumulated
damage exceeds a threshold, the food is considered ruined.
Odor Sensitivity. Strong-smelling foods (e.g. stinky tofu
or durian) can affect other items stored in close proximity.
When such foods are placed in the same insulated compartment as milder items, prolonged storage can lead to odor
transfer. We model this using a simple odor-mixing mechanism. Each food item maintains an odor level o ∈ [0, 1],
i
and items within the same compartment gradually converge
toward the highest odor level present in that compartment:
onew = o + α (cid:0) o − o (cid:1) ,
i i max i
where o is the maximum odor level among items in the
max
compartment, and α is a small timestep-based update coefficient. If o = 0, no odor transfers.
max

Input Prompt
System Prompt
You are a food-delivery courier in a simulated city. Your primary go
User Prompt
### agent_state
You are Agent 1. There are 8 delivery agents in total in this city. You
~2.0 m/s, energy is 77%. Your current pace is normal (×1.00). Earni
drink ×2. Scooter: parked, batt 100%, range 5000.0 m, parked at (-2
### store_catalog
Available items & effects: 1. energy_drink $6.00...
### active_orders
You have accepted the following active orders: [Order #0]{“Pickup”
224.62m) | road: 13th road (left), “Time Left”: 7 min $$: $9.42, “Sta
### map_snapshot
Agent position: (-423.20m, 53.69m) • restaurant 3 • 8th road (left)
The following are nearby locations and POIs with their coordinates
current delivery needs.
Next hops: N1: restaurant 3 at (-424.45m, 53.15m) • 14.2m • 8th roa
road (left); N3: waypoint at (-417.00m, 67.00m) • 19.5m • 8th road
N4: bus_station 6 at (-408.00m, 59.07m) • 20.6m • 8th road (left)
Next intersections: S1: intersection at (-417.00m, 183.00m) • 135.5m
All POIs by shortest-path distance: restaurant 3 / pick up address of
### recent_actions
Charge the e-scooter to 100%. - Move to (-424.45 m, 53.15 m) (~29
road (left). - [Your last successfully executed action] Place items int
### recent_errors
Attempted to rest, but the action failed because the agent was not in
### last_step_plan
Continue by heading toward the pickup location for Order #0, and th
Agent State Block Spatial M
Figure 5. Overview of the inp
B.5. Order Attributes
Orders serve as the fundamental task units in our simulation. Each order specifies a designated pickup restaurant, a
drop-off address, a delivery time window, and an associated
wage. Some orders may also include special customer requests, which agents must carefully consider during fulfillment. Upon successful delivery, the system automatically
settles the base wage and applies any additional bonuses
based on customer ratings.
Delivery Methods. Agents may choose from four delivery methods: leaving the item at the doorstep, calling the
customer, knocking on the door, or handing the order directly to the customer. For face-to-face delivery, the agent
must first locate the customer’s actual position (e.g., “under
the tree near the entrance”) and approach them to trigger
the handoff. The other methods only require reaching the
designated building entrance. If the order includes no customer notes, any of the four methods is acceptable. However, if specific delivery instructions are provided, the agent
must infer the most appropriate method from the context.
For example, a note saying “I’m in a meeting” suggests the
agent should leave the item at the door to avoid interruption,
while high-value items may warrant direct handoff. Choosing an inappropriate delivery method can result in customer

Delivery Agent
. Your Action Space is [ACTION_API]
rent transport mode is walk, at (-423.20m, 53.69m). Your speed is
s $97.38. Active orders: 0, 1, 4. Carrying: 1. Inventory: energy
9m, 212.56m).
30.84m, -224.45m) | road: 17th road (left), “Dropoff”: (-93.89m,
Ready for pickup} [Order #4]{...}
our reference. You should decide where to move based on your
ft); N2: charging_station 15 at (-412.00m, 61.24m) • 18.7m • 8th
..
: intersection at (-383.00m, 183.00m) • 169.5m; S3: intersection ...
1: at (-424.45m, 53.15m) • 8.0m 8th road (left);bus_station 6: at ...
m expected). - Wait for 180 seconds. - Pick up orders #1 at 8th
insulated bag using: "order 1: 3 -> B; 1,2 -> C".
designated rest area.
roceed to (-292.89m, 212.56m) to retrieve the scooter...
Block Interaction Memory Block
rompt used by delivery agents
dissatisfaction and lower ratings.
Base Delivery Pay. Each delivery order includes a fixed
base wage, which is granted in full if the agent completes
the delivery within the specified time window or a short
grace period (e.g. 1 minute). For late deliveries, the base
pay is proportionally reduced based on the delay duration,
but never falls below 30% of the original amount.
Customer Rating Bonus. Upon successful delivery, the
customer provides a rating from 0 to 5 based on overall satisfaction. This rating influences the agent’s compensation
through a bonus or penalty mechanism. The score reflects
three main factors: total customer waiting time, food condition upon arrival, and the suitability of the chosen delivery
method. If the rating exceeds 3 stars, the agent receives a
bonus of up to $3. If the rating falls below 3 stars, a fixed
$2 penalty is applied.
C. Agent Input–Output Specification
In this section, we specify the delivery agent’s input and
output formats, along with its action space.
C.1. Input Prompt Structure
At each decision step, the agent receives an input prompt
that summarizes all information needed for planning and

Figure 6. Hum
acting. The prompt consists of two parts: a System Prompt,
which remains fixed throughout the episode, and a User
Prompt, which is dynamically updated at every step. The
System Prompt specifies the agent’s role in the simulated
city, its primary delivery objective, and the available action
space. The User Prompt then provides three additional components: (i) an Agent State block describing the agent’s current status, such as its location, transport mode, speed, energy level, and active orders; (ii) a Spatial Map block encoding a compact map snapshot, including the next reachable
waypoints, nearby intersections, and the locations of relevant POIs; and (iii) an Interaction Memory block recording
recent actions, the previous step’s plan, and any error messages from failed actions. Sometimes the User Prompt also
includes context-specific information; for example, arriving at a restaurant reveals the list of available pickups, and
invoking an order-viewing action inserts the current order
pool into the prompt. An example of the full prompt structure is shown in Figure 5.
C.2. Output Format
The agent follows a fixed structured format when producing
its textual output. It first reflects on its recent memory and
current state to formulate a Reflection and Reasoning paragraph that explicitly articulates the thought process behind
the current decision. Based on this reasoning, the agent then
outputs an Action specifying the concrete operation to execute. Finally, it provides a Future Plan describing how it
intends to proceed after completing the current action.
C.3. Action Space
In DeliveryBench, the agent selects from a discrete action space of 30 actions, organized into several functional
categories: (i) Movement actions allow the agent to navigate across the city, either through high-level navigation

nteraction GUI.
commands that invoke the built-in shortest-path planner or
through simple low-level motion steps (e.g. stepping forward or turning around). (ii) Order-handling actions support core delivery operations such as browsing the order
pool, accepting orders, and completing drop-offs. (iii) Inventory and resource management actions involve managing the agent’s internal resources, enabling it to regulate stamina, battery levels, and food conditions (e.g. resting, inspecting the bag, consuming energy drinks or battery packs). (iv) Social and collaboration actions facilitate
multi-agent assistance, including viewing or posting help
requests, accepting cooperative tasks, and simple communication. (v) Transportation actions allow the agent to switch
transportation modes, rent or return vehicles, or use the public bus system.
D. Human Data Collection
To obtain a reasonable human performance reference and
collect data for supervised fine-tuning, we recruited three
human participants, each completing a two-hour delivery
session independently. All experimental settings and evaluation protocols were kept identical to those used for the
VLM agent. The resulting human trajectories were then
augmented using GPT-4o to generate the corresponding reflection, reasoning, and future-plan annotations.
D.1. Human Interaction GUI
Human participants interacted with the environment via a
custom-designed GUI that provides first-person observations, a map view, and contextual task information. Participants issued their actions directly through the interface.
During delivery, the GUI displays real-time information
such as the participant’s remaining stamina, current location, and accumulated earnings. All human trajectories are
automatically logged by the system. A detailed illustration

Table 9. Fine-grained metrics for delivery agents; arrows indicate whether higher (↑) or lower (↓) values are better.
Dimension Metric Definition Range
Average relative quality of the orders selected by the agent, evaluated based on
delivery-deadline feasibility relative to distance, reward relative to cost, and the
Planning Order (Quality) ↑ alignment between the order’s delivery route and the agent’s current trajectory. [0, 5]
Candidate orders are scored and ranked within the pool, with higher-ranked orders
indicating higher quality.
OnTime (Rate) ↑ Proportion of selected orders delivered before their deadlines. [0, 1]
Sum of effective delivery durations for all delivered orders, including periods
where multiple orders are handled in parallel, divided by the total episode time.
TimeEff (Time
Values greater than 1 indicate that the agent frequently handles multiple orders in [0, 1]
Efficiency) ↑
parallel, values close to 1 indicate that the agent is almost continuously engaged in
deliveries, and values below 1 indicate substantial idle time between deliveries.
Fraction of time spent performing purposeful actions (e.g. moving, picking up,
Active (Rate) ↑ [0, 1]
delivering, recharging), excluding waiting or incapacitated periods.
Resources StaminaUse ↓ Average stamina consumption per hour. ≥ 0
Number of forced interruptions per hour caused by resource depletion (e.g.
Interrupts ↓ ≥ 0
stamina or battery exhaustion).
Prevention ↑ Fraction of times the agent replenishes critical resources before they are depleted. [0, 1]
Proportion of orders that incur constraint violations, such as food-quality failures
Physical & Env. Violations ↓ [0, 1]
(e.g. melting, breakage, or odor transfer).
FoodRate ↑ Average rating of the food’s final quality upon delivery. [0, 5]
Average customer rating for each delivered order, reflecting overall satisfaction
CustRate ↑ [0, 5]
with factors such as waiting time, delivery behavior, and food condition.
of the GUI is provided in Figure 6. E.2. Planning Style Evaluation Prompts
D.2. LLM-enhanced Annotation We use GPT-4o as an evaluator to assess the planning style
exhibited by each model. At each evaluation step, GPT-4o
Since the human trajectories only record the actions chois given (i) the current environment observation and (ii) the
sen at each step, we use GPT-4o to reconstruct the full
model’s full output, which includes the chosen action, its
chain-of-thought annotations in the same structured format
chain-of-thought rationale, and the resulting consequences
described in Appendix C.2, ensuring consistency with the
of that decision (e.g., whether an accepted order later times
VLM agent’s outputs. For each human decision step, we
out or whether the action leads to future battery depletion).
provide GPT-4o with the corresponding observation and exGPT-4o then scores this decision across multiple planning
ecuted action, prompting the model to infer the underlying
dimensions. The complete evaluation prompt used for scorrationale behind the decision. We further supply the subseing is shown in Figure 7.
quent five human actions to GPT-4o, enabling it to generate
the future plan aligned with those actions.
F. Additional Experimental Results
E. Evaluation Details
F.1. Interaction Frequency with Team Size
E.1. Fine-grained Metric Definitions
In the multi-agent setting, we evaluate how interaction freTo analyze agent behavior beyond final delivery profit, we quency among models changes with team size, as shown
adopt a set of fine-grained metrics that capture different as- in Figure 8. Although the communication rate tends to inpects of long-horizon delivery performance. These metrics crease in larger teams, agents still interact only occasionassess high-level planning (order selection, deadline han- ally. However, this increase in communication does not
dling, time utilization), resource management (stamina us- improve task performance. As team size grows, coordinaage and proactive replenishment), and physical or environ- tion becomes more complex. Agents must balance maximental adaptation (food quality, constraint violations, cus- mizing their own utility with supporting their teammates,
tomer satisfaction). Their formal definitions and computa- which makes effective cooperation more difficult. As a retion methods are summarized in Table 9. sult, agents often overreact to teammate requests and aban-

Input Prompt for Pl
You are a step-level evaluator for a delivery agent.
For each evaluation step, you will receive: (1) a GLOBAL MAP im
prompt (observation/rules/context), (4) the agent’s JSON output for
Your task is to assign 0–10 scores for the behavioral dimensions def
materials. If a dimension is not evidenced in this step, assign -1 for t
Scoring dimensions (integers in [0,10], or -1 if not evidenced):
1) Risk (risk-taking vs conservatism): 10 = clearly high-risk behavi
delivery with insufficient resources; accepting multiple orders simul
behavior (e.g., one safe order at a time, pre-emptive charging/resting
2) Horizon (long-term planning): 10 = explicit multi-step foresight (
items for future benefit, or future plans extending beyond the next st
3) Explore (strategy diversity): 10 = use of non-routine tools or strat
renting vehicles, taking buses, purchasing functional items, using alt
4) Coop (collaboration): 10 = clear evidence of proactive collaborati
help, requesting assistance, jointly handling orders, or adjusting plan
on the agent’s own tasks, with no attempt to cooperate.
5) Detail (attention to operational constraints): 10 = careful handling
off methods, timing windows, melting risk, etc. 0 = clear oversight o
6) Flex (adaptability to state changes): 10 = evident plan adjustment
charge; correcting mistakes). 0 = blindly following an outdated plan
Output policy:
Judge ONLY from THIS STEP’s provided materials (text, maps, act
step is skipped by the caller; Return JSON ONLY with EXACT key
int, "Detail": int, "Flex": int}; No extra keys, no commentary, no ma
Figure 7. Prompt for
don their own tasks, or they promise help but fail to follow
through, leaving both sides stalled.
Figure 8. Interaction frequency across team sizes.
F.2. Model Behaviors and Planning Styles
In addition to the three examples of model planning styles
shown in Figure 3, we evaluate the behaviors of all models, with the remaining results presented in Figure 9. We
further analyze each model’s action distribution, spending
patterns, and transportation choices. As shown in Figure 10, Stronger models such as GPT-5 and Claude-3.7Sonnet exhibit broader action coverage and employ a richer
set of strategies, such as renting cars or purchasing tools.
In contrast, weaker open-source models such as LLaMA3.2-90B-Vision-Ins primarily rely on simple pickup-anddelivery routines. These weaker models also end up spending more money on hospital rescues due to stamina deple-

ng Style Evaluation
2) a LOCAL MAP image, and (3) TEXT containing the agent’s
step, and (5) the resulting consequences of the chosen action.
below. CRITICAL: Use ONLY the evidence present in THIS step’s
imension.
g., preferring far or high-reward orders; continuing long-distance
usly and attempting concurrent delivery.) 0 = strongly conservative
inking destinations, choosing spatially aligned orders; purchasing
0 = purely myopic, one-step reasoning.
beyond the standard charge→accept→pickup→deliver loop (e.g.,
ive coordination strategies). 0 = strictly routine behavior.
.g., initiating coordination or dialogue with teammates; offering
support others). 0 = purely individualistic behavior focused solely
erishables, temperature-sensitive items, fragile goods; correct dropportant constraints.
ed on new information (e.g., noticing low battery and rerouting to
nd consequences); If the model output is malformed or missing, the
integer values: {"Risk": int, "Horizon": int, "Explore": int, "Coop":
wn.
ning style evaluation.
tion and often use less efficient transportation modes (e.g.,
walking or dragging scooters). Their spending patterns are
summarized in Figure 11, and their transportation preferences are illustrated in Figure 12.
GPT-4o Qwen2.5-32B Qwen2.5-72B LLaMA-90B
A passionate yet A steady but A similar balancer, but A low-awareness
stubborn doer ordinary balancer even weaker than 32B. bumbler
The delivery was I’ll head toward the I've accepted Order I am currently
interrupted because I pickup point to save #0. The food is still towing a scooter
ran out of stamina, time, check if being prepared, so with 0% battery and
causing a 35-minute temperature packs I'll head there and have 3% energy.
delay. My priority are needed for the wait. Then I’ll My active order #10
now is to resume food, and recharge deliver it and accept is already picked up
delivery of order #16 the scooter if new orders... and needs to be
and complete... necessary to... delivered to...
Still delivers even Considers everything, Considers everything, Fails to realize the
with severe overtime. but shallowly. but shallowly. need to recharge.
Figure 9. Planning style visualizations for the remaining four models, complementing the examples shown in Figure 3.
F.3. Detailed Results for Context Engineering and
Supervised Fine-tuning
We provide additional experimental results and analyses
that complement the studies presented in Section 5.5, including more detailed metric breakdowns and illustrative

Figure 10. Action distributions of different models. For each mod
while the inner bars show the corresponding success rates.
Figure 11. Expenditure distribution across models.
Figure 12. Transportation mode distribution across models.
case studies of model-generated summaries under context
engineering.
Fine-grained Analysis. We further analyze model performance along three dimensions: high-level planning, resource management, and physical or environmental adaptation. As shown in Table 10, context engineering generally leads to higher on-time delivery rates, better time
efficiency, and a larger active-time ratio, which allow the
models to complete more orders and achieve higher earnings. However, the gains in resource management and environmental handling are less substantial. For the humantrajectory fine-tuning experiments, fine-tuning directly on
raw actions results in noticeable declines across multiple
capabilities. In contrast, fine-tuning on annotated trajecto-

he outer bars indicate the relative frequency of attempted actions,
ries produces significant improvements. In particular, timeefficiency scores even exceed those of large models such
as GPT-5 and Claude-3.7-Sonnet, indicating that the model
successfully learns the human strategy of handling multiple
orders in parallel.
Context Engineering Case Study. We present example
notebooks generated by Claude-3.7-Sonnet and Qwen2.5VL-72B under Agentic Context Engineering (ACE). In
this setting, each model autonomously summarizes patterns
from its past trajectories and maintains these summaries
as persistent memory to guide future deliveries. For each
model, we select the ten highest-quality examples, shown
in Figure 13 and Figure 14. Both models extract principles covering multiple aspects of delivery, including time
management and resource planning, and their summaries
closely align with the underlying task rules. In comparison,
Claude-3.7-Sonnet produces more detailed and actionable
guidelines, which in turn contributes to its larger performance improvement when ACE is applied.
F.4. Ablation Studies
Planning Ablation. We further analyze the results reported
in Table 5, which compare models that perform explicit
plan-and-execute reasoning with models that directly output a single action. For GPT-5 and Qwen2.5, planning
consistently improves most capability metrics and leads to
higher net profit. In contrast, Claude-3.7-Sonnet earns more
when planning is enabled, but its net profit decreases because of increased expenses. These additional costs mainly
arise from overplanning, such as repeatedly recharging the
e-scooter when the battery level is already sufficient or purchasing items that are not immediately necessary.
Waypoint Ablation. We evaluate whether VLM agents
can navigate without privileged spatial priors. We remove
preset waypoints and restrict them to step-by-step nav-

Table 10. Fine-grained metrics for planning, resource usage, and
vised fine-tuning. Green highlights improvements and red denotes
Planning
Model
Order↑ OnTime↑ TimeEff↑
GPT-5 (with Plan) 3.38 0.32 0.94
GPT-5 (w/o Plan) 3.24 0.25 0.45
GPT-5 (with Plan + ACE) 3.62 0.33 0.88
GPT-5 (with Plan + DC) 3.41 0.37 1.08
Claude-3.7-Sonnet (with Plan) 3.46 0.41 0.92
Claude-3.7-Sonnet (w/o Plan) 3.28 0.37 0.58
Claude-3.7-Sonnet (with Plan + ACE) 3.38 0.60 0.96
Claude-3.7-Sonnet (with Plan + DC) 3.41 0.52 1.06
Qwen2.5-VL-72B (with Plan) 3.12 0.17 0.40
Qwen2.5-VL-72B (w/o Plan) 3.07 0.21 0.38
Qwen2.5-VL-72B (with Plan + ACE) 2.97 0.14 0.88
Qwen2.5-VL-72B (with Plan + DC) 3.49 0.36 0.59
LLaVA-OneVision-8B (original) 3.22 0.05 0.15
LLaVA-OneVision-8B (human-ft) 3.05 0.06 0.72
LLaVA-OneVision-8B (annotated-ft) 3.36 0.16 1.51
Claude-3.7-Sonnet–G
• When both scooter battery and personal energy are critically low,
below 25%, as mobility is typically the more constraining resourc
• Before abandoning a scooter due to battery depletion, calculate w
efficient than walking to a charging station and back.
• Maintain a continuous awareness of nearby resource restoration p
route planning before resources reach critical levels.
• When managing multiple resource needs, plan a route that minim
proximity rather than treating each need as a separate journey.
• When multiple resource needs exist simultaneously (low persona
urgency and proximity to create efficient multi-objective routes.
• Add a 5-minute buffer to all delivery time estimates to account fo
arise during delivery.
• Before accepting orders, calculate the total journey distance (to p
personal energy and scooter battery are sufficient with at least a 4
• Before accepting new orders, check the map for nearby resources
replenishment options during the delivery journey.
• Avoid accepting orders that require significant backtracking, espe
minimize further delays.
• Before accepting distant orders, evaluate all available transportat
and resource levels to determine the most efficient delivery meth
Figure 13. Example ACE notebo
Qwen2.5-VL-72B–G
• While waiting for orders to be prepared, use the time to scout for
• When battery level drops below 20%, immediately prioritize mov
• Prioritize high payout-to-distance ratio orders when selecting bat
• When multiple orders are ready simultaneously, batch them based
• Regularly monitor energy levels and plan routes that include char
• Consider the urgency of orders (overtime status) when planning d
satisfaction.
• Utilize the map snapshot effectively to identify optimal paths and
• Consider alternative orders with shorter preparation times when f
• Monitor energy levels and plan breaks accordingly to maintain op
• Always assess the feasibility of new orders against current battery
Figure 14. Example ACE noteb
igation using only low-level actions (STEP FORWARD,
TURN AROUND) with egocentric observations. Agents
fail to complete even a single order under this setting, in-

ical/environmental behavior under context engineering and superessions over the with-Plan baseline.
Resources Physical & Env.
e↑ Stamina↓ Interrupts↓ Prevention↑ Violations↓ Food↑ Cust↑
6 1.35 1.35 0.72 0.65 3.95 3.79
8 1.32 1.86 0.48 0.75 3.35 3.20
3 1.66 2.50 0.62 0.89 3.56 3.56
8 1.29 2.96 0.79 0.68 3.83 4.04
9 0.78 0.64 0.77 0.62 3.80 3.72
4 1.05 0.39 0.77 0.78 3.88 3.76
2 0.79 0.50 0.91 0.70 4.00 4.30
7 1.22 1.06 0.54 0.72 3.92 4.16
3 1.38 1.50 0.53 0.70 4.11 3.73
1 1.42 2.13 0.24 0.75 3.61 3.35
3 1.76 3.00 0.40 1.00 3.80 3.40
2 0.98 1.26 0.44 0.62 4.16 4.03
0 2.32 2.49 0.16 0.74 3.67 3.52
8 2.49 2.99 0.14 0.82 3.63 3.04
8 0.64 2.38 0.47 0.58 4.02 3.96
ated ACE Notebook
itize addressing vehicle battery first unless personal energy is
er purchasing a battery pack would be more time and energy
(charging stations, stores, rest areas) and incorporate them into
otal travel distance by addressing needs at locations in close
gy, low scooter battery, pending orders), prioritize based on
xpected delays, traffic, or resource management needs that may
+ to delivery + return to strategic location) and verify both
uffer.
es, charging stations, rest areas) to ensure access to necessary
y when handling overtime deliveries that require direct routing to
ptions (walking, scooter, public transit) based on current location
generated by Claude-3.7-Sonnet.
ated ACE Notebook
by orders or pre-plan delivery sequences to optimize efficiency.
o the nearest charging station before continuing deliveries.
o maximize efficiency and profitability.
imilar drop-off directions to minimize backtracking and save time.
stations if needed, especially during long delivery sequences.
ry sequences to minimize penalties and improve customer
d unnecessary detours, ensuring efficient use of time and resources.
with long wait times at pickup locations.
l performance throughout the shift.
energy levels to avoid overcommitting.
generated by Qwen2.5-VL-72B.
dicating that current models struggle to translate visual understanding into embodied navigation. Explicit spatial coordinates remain a dependency for these models.

F.5. Variance and Stability Analysis
We further evaluate the stability of model performance
under repeated runs. For both Gemini-2.5-Flash and
Qwen2.5-VL-72B-Ins, we conduct three experimental
groups, each following the same setup as the main experiment and consisting of eight independent runs along with
their averaged results. As shown in Table 11, overall, both
models exhibit low variance across runs, demonstrating stable and reliable performance under identical conditions.
Table 11. Mean values and run-to-run variability for Gemini-2.5Flash and Qwen2.5-VL-72B-Ins.
Metric Gemini-2.5-Flash Qwen2.5-VL-72B-Ins
P¯ $28.46 ± 2.52 $5.96 ± 2.82
E $37.55 ± 2.11 $13.28 ± 2.90
C -$9.09 ± 1.32 -$7.32 ± 0.96
Order 3.32 ± 0.11 3.07 ± 0.09
OnTime 0.30 ± 0.07 0.18 ± 0.05
TimeEff 0.88 ± 0.08 0.45 ± 0.04
Active 0.52 ± 0.04 0.50 ± 0.05
Stamina 1.03 ± 0.06 1.42 ± 0.09
Interrupts 1.79 ± 0.05 1.57 ± 0.10
Prevention 0.78 ± 0.06 0.55 ± 0.08
Violations 0.70 ± 0.11 0.68 ± 0.14
Food 4.08 ± 0.11 4.01 ± 0.17
Cust 3.77 ± 0.20 3.62 ± 0.25
