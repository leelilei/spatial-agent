# 01_Feng2025_Spatial_Intelligence_Across_Scales

Source PDF: `/Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/review_library/01_Feng2025_Spatial_Intelligence_Across_Scales.pdf`

Extraction backend: `PyMuPDF`

## Page 1

A Survey of Large Language Model-Powered Spatial Intelligence Across Scales:
Advances in Embodied Agents, Smart Cities, and Earth Science
Jie Feng, Jinwei Zeng, Qingyue Long, βHongyi Chen, Jie Zhao, †Yanxin Xi, Zhilun Zhou,
Yuan Yuan, §Shengyuan Wang, Qingbin Zeng, Songwei Li, Yunke Zhang,
Yuming Lin, Tong Li, Jingtao Ding, Chen Gao, Fengli Xu, Yong Li
Department of Electronic Engineering, BNRist, Tsinghua University, Beijing, China,
β Shenzhen International Graduate School, Tsinghua University, Shenzhen, China,
§Department of Computer Science, Tsinghua University, Beijing, China,
†Department of Computer Science, University of Helsinki, Helsinki, Finland
{fengjie, liyong07}@tsinghua.edu.cn
Abstract
Over the past year, the development of large lan-
guage models (LLMs) has brought spatial intelli-
gence into focus, with much attention on vision-
based embodied intelligence. However, spatial in-
telligence spans a broader range of disciplines and
scales, from navigation and urban planning to re-
mote sensing and earth science. What are the differ-
ences and connections between spatial intelligence
across these fields? In this paper, we first review
human spatial cognition and its implications for spa-
tial intelligence in LLMs. We then examine spatial
memory, knowledge representations, and abstract
reasoning in LLMs, highlighting their roles and con-
nections. Finally, we analyze spatial intelligence
across scales—from embodied to urban and global
levels—following a framework that progresses from
spatial memory and understanding to spatial rea-
soning and intelligence. Through this survey, we
aim to provide insights into interdisciplinary spatial
intelligence research and inspire future studies.
1
Introduction
Spatial intelligence is an inherently interdisciplinary research
field, encompassing diverse challenges, application scenarios,
and methodologies across multiple domains. For example, nav-
igating within a room requires spatial intelligence, designing a
15-minute community relies on spatial intelligence, predicting
the possible location of an image involves spatial intelligence,
and analyzing the spatial patterns of climate is also a form
of spatial intelligence. In other words, spatial intelligence
is ubiquitous and plays a crucial role in human society and
physical world.
Research on spatial intelligence has deep historical roots.
On the one hand, it serves as a crucial avenue for humans
to understand their own cognitive and perceptual mecha-
nisms [Ishikawa, 2021; Eichenbaum and Cohen, 2014]. Stud-
ies on human spatial cognition, ranging from mental mapping
All authors contribute equally to this work.
to wayfinding strategies, have provided foundational insights
into human intelligence. On the other hand, spatial intelligence
has long had practical significance in real-world applications,
such as embodied navigation [Lin et al., 2024], geographic
information systems (GIS) [Zhao et al., 2024], and climate
prediction [She et al., 2024]. The study of spatial intelligence
continues to evolve, bridging cognitive science, artificial intel-
ligence, and applied domains.
The rapid advancements in deep learning, particularly in
large language models (LLMs), have significantly contributed
to spatial intelligence research of recent years. LLMs have
made notable progress with world knowledge, planning and
reasoning capabilities, and powerful generalization across
tasks. These advancements have fueled research in embodied
intelligence [Gupta et al., 2021], where LLMs play a central
role in areas such as robotic navigation, multimodal perception,
and control. Recent works, such as SpatialVLM [Chen et al.,
2024] and Voxposer [Huang et al., 2023b], have demonstrated
how LLMs can improve spatial reasoning and decision-making
in embodied agents, enabling them to operate more effectively
in complex environments.
Beyond embodied intelligence, LLMs have also inspired
new research in urban and global-scale spatial intelligence.
In urban research, for example, LLMs have been integrated
with geospatial data to optimize urban planning [Zhou et al.,
2024b], traffic prediction [Li et al., 2024e] and infrastructure
management [Lai et al., 2023]. At a global scale, researchers
have explored how LLMs can enhance remote sensing analy-
sis [Kuckreja et al., 2024] and disaster prediction [Zhang et
al., 2023b], and so on, which illustrate the potential of LLMs
to process large-scale geospatial information and generate
meaningful insights for global-scale decision-making. These
interdisciplinary applications highlight the transformative im-
pact of LLMs on spatial intelligence research, paving the way
for future developments across multiple domains.
Despite the growing of research on spatial intelligence
across various fields, there is still a lack of a unified framework
for comprehensively understanding and analyzing it. Existing
studies often focus on specific aspects, such as vision-based
embodied intelligence, urban planning, or remote sensing in-
telligence, without integrating insights across disciplines and
arXiv:2504.09848v1  [cs.AI]  14 Apr 2025

## Page 2

Embodied Spatial Intelligence
Urban Spatial Intelligence
Earth Spatial Intelligence
Figure 1: Multiple scale spatial intelligence in real world: from embodied spatial intelligence to earth spatial intelligence.
scales. To bridge this gap, this survey traces the development
of spatial intelligence from the perspective of human cogni-
tion, fundamental spatial capabilities, and multi-scale system
intelligence from embodied agents, urban intelligence and
earth science. By synthesizing these perspectives, we aim to
provide a cohesive foundation for interdisciplinary research,
offering insights and inspiration for future advancements in
spatial intelligence.
Our survey makes three key contributions. First, it estab-
lishes a structured analytical framework for understanding
spatial intelligence across diverse disciplines and scales, ad-
vancing from spatial memory and perception to reasoning
and higher-level intelligence. Second, it synthesizes exist-
ing literature on spatial intelligence applications with LLMs
across multiple fields, alongside discussions on spatial mem-
ory, knowledge representation, and spatial reasoning in LLMs,
providing researchers with a timely and valuable reference.
Third, it explores key challenges and open questions in interdis-
ciplinary spatial intelligence research, uncovering connections
between embodied, urban, and global-scale intelligence while
outlining promising directions for future exploration.
2
Background and Taxonomy
2.1
Spatial Intelligence of Human
Here, we first review human spatial intelligence research from
the perspectives of neuroscience and cognitive science, eluci-
dating the potential abilities and origins of spatial intelligence
across various domains and scales. Furthermore, we explore
the relationship between spatial intelligence and other human
intelligences. These findings will enhance our understanding
of the critical capabilities of cross-domain spatial intelligence
and facilitate the development of more effective methods for
constructing and enhancing spatial intelligence.
2.1.1
Cognitive Map
Spatial cognitive map is the internal representation of envi-
ronmental knowledge, characterized by subjectivity and dis-
tortion [Ishikawa, 2021]. Tolman introduced this concept in
1948 [Tolman, 1948], later expanded by Eichenbaum et al. [Co-
hen, 1993; Eichenbaum and Cohen, 2014], emphasizing the
hippocampus’s role in spatial and non-spatial memory. At the
neural level, spatial representation relies on place cells in the
hippocampus and grid cells in the entorhinal cortex [Moser
et al., 2008; Moser et al., 2017]. Place cells activate when
an individual is in a specific location, while grid cells pro-
vide a coordinate-like system for mapping the environment.
These cells, along with head direction cells and boundary
cells, form the neural basis for constructing spatial cognitive
maps [Long et al., 2025]. Recent advancements, such as
the Tolman-Eichenbaum Machine (TEM) [Whittington et al.,
2020], highlight the ability to generalize spatial and relational
memory through structural abstraction and cross-environment
representation by grid cells. Comparatively, large language
models (LLMs) leverage Transformer architectures to emu-
late spatial tasks, such as positional encoding and navigation,
drawing parallels to hippocampal functions [Whittington et
al., 2021].
2.1.2
Spatial Schema
Schemas are high-level knowledge structures that encapsulate
the common features abstracted from multiple experiences.
These structures play a critical role in the processes of perceiv-
ing, interpreting, and remembering events. They continuously
evolve with the accumulation of new experiences and memo-
ries, influencing the formation, consolidation, and retrieval of
memory [Gilboa and Marlatte, 2017]. In human spatial cog-
nition, schemas play a crucial role. Spatial schemas are high-
level spatial cognitive structures formed through the transfer
and generalization of experiences across different environ-
ments. Unlike cognitive maps, their processing is centered in
specific regions of the neocortex. Spatial schemas are highly
abstract in nature, emerging through the integration of over-
lapping neural representations in similar environments. They
serve as higher-order spatial representations that transcend
specific environments, such as the anticipated layout of a mod-
ern city [Farzanfar et al., 2023]. Spatial schemas and cognitive
maps, as distinct levels of spatial cognitive structures, interact
and influence each other, jointly contributing to human spatial
cognition.
Recent research has explored the similarities and connec-
tions between spatial intelligence based on LLMs and human

## Page 3

Large Language Model-Empowered Spatial Intelligence
Foundational
Capabilities
Spatial Memory
and Knowledge
Internal Encoded [Petroni et al., 2019], [Gurnee and Tegmark, 2024], [Roberts et al., 2020]
Externally Integrated [Mansourian and Oucheikh, 2024] [Yu et al., 2024b]
Abstract Spatial
Reasoning
Qualitative Reasoning [Yamada et al., 2023], [Sharma, 2023], [Lehnert et al., 2024], [Li et al., 2024a]
Geometric Reasoning: GeoEval [Zhang et al., 2024], GeomVerse [Kazemi et al., 2023]
Graph-theoretical Reasoning: GraphInstruct [Luo et al., 2024]
Spatial Intelligence
for Real World
Embodied Spatial
Intelligence
Spatial Perception and Understanding: LLMI3D [Yang et al., 2024a], 3D-MEM [Yang et al., 2024d],
EmbodiedScan [Wang et al., 2024b], Scene-LLM [Fu et al., 2024], SpatialBot [Cai et al., 2024]
Spatial Interaction and Navigation: RT-2 [Zitkovich et al., 2023], VIMA [Jiang et al., 2022],
Guide-LLM [Song et al., 2024], NavGPT [Zhou et al., 2024a], TopV-Nav [Zhong et al., 2024]
Urban Spatial
Intelligence
Spatial Understanding and Memory: GeoLLM [Manvi et al., 2023], GeoChat [Kuckreja et al., 2024],
UrbanCLIP [Yan et al., 2024], ReFound [Xiao et al., 2024], UrbanKGEnt [Ning and Liu, 2024]
Spatial Reasoning and Intelligence: GeoReasoner [Li et al., 2024c], LLMob [Wang et al., 2024a],
AgentMove [Feng et al., 2024b], Mobility-LLM [Gong et al., 2024], FLAME [Xu et al., 2024a],
Earth Spatial
Intelligence
Global Encoding: TorchSpatial Benchmark [Wu et al., 2024]
Climate: LLMDiff [She et al., 2024], CLLMate [Li et al., 2024b], GenCast [Ravuri et al., 2021]
Geography: GeoGPT [Zhang et al., 2023a], GeoSEE [Han et al., 2024], GeoReasoner [Yan and Lee, 2024]
Other Disciplines: OceanPlan [Yang et al., 2024c], Orca [Li et al., 2024d], MineAgent[Yu et al., 2024a]
Figure 2: A taxonomy of large language model-empowered spatial intelligence with representative examples.
spatial intelligence, e.g., Momennejad et al. [Momennejad
et al., 2024] assessed their cognitive mapping capabilities.
However, LLMs exhibit limitations, including topological
reasoning errors (e.g., fictitious paths, inefficiency) and visual-
spatial perception gaps. While studying cognitive maps in
both humans and LLMs provides valuable insights into spa-
tial intelligence, significant challenges remain in enhancing
LLMs’ schema learning and spatial syntax integration.
2.2
Taxonomy of Spatial Intelligence
Building on human spatial memory and intelligence, we pro-
pose a taxonomy for spatial memory and intelligence in LLMs,
as illustrated in Figure 2, and provide a comprehensive survey
of current research based on this framework. Specifically, we
first introduce the foundational capabilities that enable spatial
intelligence in LLMs, which are divided into spatial memory
and knowledge, as well as abstract spatial reasoning abilities.
Subsequently, we focus on the application of spatial intelli-
gence in the real world, exploring three dimensions: embodied
intelligence, urban intelligence, and earth intelligence.
3
Foundational Capabilities of Spatial
Intelligence in LLMs
3.1
Spatial Memory and Knowledge in LLMs
Spatial memory refers to the cognitive ability to recall spa-
tial relationships, entities, and attributes encountered in the
past. Spatial knowledge, a broader concept, encompasses not
only this memory but also commonsense reasoning and logical
thinking related to space. General spatial memory and knowl-
edge combine both abstract spatial cognition and real-world
environmental capabilities.
Recently, state-of-the-art large language models (LLMs)
have demonstrated their proficiency in handling spatial tasks
with spatial memory and knowledge [Bhandari et al., 2023].
Multi-modal large language models (MLLMs) also extend
this capability, exhibiting their memory and knowledge about
spatial information from both linguistic and visual modali-
ties [Yang et al., 2024b]. Spatial memory and knowledge
can be derived from internal or external sources.
Inter-
nally, spatial memory and knowledge are encoded within
the parameters of LLMs during pretraining or post-training
stages [Petroni et al., 2019; Gurnee and Tegmark, 2024;
Roberts et al., 2020]. Externally, LLM’s can utilize outer
spatial memory or knowledge storage for specific information
when needed [Mansourian and Oucheikh, 2024]. LLMs’ spa-
tial memory and knowledge is an essential part of their spatial
intelligence. Many general and spatial-specific tasks are based
on accurate and adequate memory and knowledge about the
spatial environment, including question answering [Mai et al.,
2021; Yamada et al., 2023], navigation[Epstein et al., 2017;
Feng et al., 2024c], and geolocalization[Haas et al., 2024].
Practices to improve LLM’s spatial memory and knowledge
emerge along the bloom of pre-trained generative models.
Various training methods are implemented to encode spatial
information [Feng et al., 2024a]. Other works integrate exter-
nal knowledge base to provide spatial memory and knowledge
[Yu et al., 2024b]. Previous works have also attempted to
leverage compressed spatial knowledge within LLMs [Manvi
et al., 2023].
Despite these rapid advancements, challenges remain in
the domain of spatial memory and knowledge in LLMs.
One significant challenge is hallucination [Lee et al., 2022],
where LLMs may generate non-factual or non-faithful con-
tents [Huang et al., 2023a], undermining the effectiveness of
task in spatial contexts. Another pressing challenge is knowl-
edge editing [Zhang et al., 2023c]. Given the dynamic nature
of the spatial environment, it is necessary to continually and

## Page 4

Spatial memory and
knowledge are encoded
within the parameters
Spatial memory and
knowledge are stored in
external knowledge base
…
Spatial Relation
Entity and Attribute
Commonsense Reasoning
Spatial logical thinking
Spatial Memory and Knowledge in LLMs
Hallucination
Mitigation
Knowledge
Editing
Challenges
Internal
External
Question Answering
Navigation
Geolocalization
Down-stream Tasks
…
Pre-
training/
Post-
training
Inference
…
Sources
Figure 3: This figure illustrates the core concepts of Spatial Memory and Knowledge in LLMs. LLMs build their spatial memory and
knowledge from both internal and external sources to perform tasks like question answering, navigation, and geolocalization, while also facing
challenges such as hallucination mitigation and knowledge editing.
timely update LLM’s memory and knowledge to reflect accu-
rate spatial information.
3.2
Abstract Spatial Reasoning of LLMs
Abstract reasoning ability is a crucial cognitive capability that
enables intelligent agents to simplify complex reality into op-
erable mental models. In the context of spatial intelligence,
abstract reasoning plays a crucial role: it not only simplifies
complex physical spaces into manageable mental models but
also provides a foundation for higher-level spatial cognition,
serving as a vital bridge between objective spatial environ-
ments and cognitive representations.
With LLMs showing promise in cognitive tasks, assess-
ing their spatial abstract reasoning capabilities has emerged
as a critical research direction, both for understanding their
limitations and guiding future improvements. Current assess-
ments of LLMs’ spatial abstract reasoning capabilities pri-
marily focus on three directions: qualitative spatial reason-
ing [Yamada et al., 2023; Sharma, 2023; Lehnert et al., 2024;
Li et al., 2024a], geometric reasoning [Zhang et al., 2024;
Kazemi et al., 2023], and graph-theoretical reasoning [Luo
et al., 2024]. Qualitative spatial reasoning evaluates mod-
els’ ability to understand and reason about spatial relations
and transformations through linguistic descriptions. In this
domain, LLMs have revealed significant performance degra-
dation in multi-hop reasoning tasks while demonstrating that
structured thinking frameworks can effectively mitigate these
limitations [Li et al., 2024a]. In spatial planning problems,
[Lehnert et al., 2024] show that training strategies like search
dynamics bootstrapping have shown notable improvements
in complex spatial planning tasks. Geometric reasoning fo-
cuses on assessing models’ understanding of mathematical-
geometric concepts and their applications in spatial problem-
solving. GeoEval [Zhang et al., 2024] comprehensively eval-
uates LLMs across various geometry domains and identified
their weakness in inverse reasoning compared to forward rea-
soning while showing the effectiveness of problem rephrasing
strategies. GeomVerse [Kazemi et al., 2023] systematically
demonstrates VLMs’ struggles with deep geometric reason-
ing tasks requiring long inference chains rather than simple
knowledge retrieval. Graph-theoretical reasoning examines
models’ capabilities in understanding and manipulating graph
structures. In this field, GraphInstruct [Luo et al., 2024] de-
veloped a comprehensive test set, which revealed that LLMs
still struggle with complex graph algorithms like minimum
spanning trees, Hamiltonian paths, and shortest paths. How-
ever, their research also demonstrated that these limitations
can be overcome through structured training approaches that
emphasize intermediate reasoning steps. Besides, Xu [Xu et
al., 2025] et al. pioneer a psychometric framework that defines
five basic spatial abilities (BSAs) in vision-language models
(VLMs), while highlighting issues such as weak geometry
encoding and the absence of dynamic simulation capabilities.
In summary, current evaluations across these three direc-
tions reveal that pre-trained LLMs primarily rely on language
understanding to process abstract spatial problems, lacking
genuine spatial cognitive abilities. Methodological improve-
ments, including structured reasoning frameworks, knowledge-
guided training, and intermediate process supervision, have
shown promise in addressing these limitations. Moving for-
ward, the field requires both more comprehensive evaluation
standards and meaningful comparisons with human perfor-
mance to better understand and advance LLMs’ spatial reason-
ing capabilities.
4
LLM based Spatial Intelligence for the Real
World
4.1
Embodied Spatial Intelligence
As shown in Fig. 5, spatial intelligence in embodied AI com-
prises two key stages: 1) spatial perception and understanding,
where agents acquire and process spatial information to con-
struct internal representations of the environment, and 2) spa-
tial interaction and navigation, where these representations are
leveraged for movement, task execution, and decision-making.

## Page 5

Spatial Relations
Planning
Transformations
…
Shapes
Problem solving
Visual logic
…
Networks
Paths
Patterns
…
Qualitative
Geometric
Graph
Mental Models for Spatial Tasks
Abstract Spatial Modeling in LLMs
Challenge: Bridging Language Understanding to Spatial Cognition
Figure 4: Conceptual framework of Abstract Spatial Reasoning. The framework illustrates three primary dimensions of spatial reasoning
capabilities: qualitative reasoning, geometric reasoning, and graph reasoning. LLMs still face the challenge of bridging language understand to
abstract spatial cognition.
4.1.1
Spatial Perception and Understanding
Spatial perception and understanding are essential for em-
bodied intelligence, allowing agents (e.g., robots) to navi-
gate, interact, and reason about their surroundings. Recent
research has explored how multi-modal large language models
(MLLMs) enhance these capabilities by integrating visual and
textual data, improving spatial reasoning, and enabling inter-
active decision-making. Advancements in this field primarily
involve three aspects: multi-modal spatial perception, scene-
level spatial reasoning, and memory-based spatial exploration.
Multimodal spatial perception focuses on fusing RGB,
depth, and textual information to enhance object localization
and understanding. For instance, LLMI3D [Yang et al., 2024a]
enables 3D object position estimation from a single 2D im-
age using spatial-enhanced feature extraction and 3D query
token-based decoding. SpatialBot [Cai et al., 2024] integrates
depth perception to improve robotic manipulation and spatial
reasoning, supported by its SpatialQA dataset, which trains
models in depth estimation and object grounding. While these
approaches expand LLMs’ perceptual abilities, challenges re-
main in effectively integrating multi-modal data and improving
fine-grained depth reasoning.
Beyond object-level perception, scene-level spatial reason-
ing enables agents to understand spatial relationships, align
multi-view information, and interpret dynamic environments.
Video-3D LLM [Zheng et al., 2024] enhances video-based
LLMs by embedding 3D spatial coordinates into video fea-
tures, supporting 3D question answering, visual grounding,
and dense captioning. Scene-LLM [Fu et al., 2024] integrates
egocentric and global 3D scene representations, using 3D
point-based features for more effective scene understanding
and interactive planning. These models improve agents’ ability
to process spatial information over time, though aligning con-
tinuous 3D spatial structures with language-based reasoning
remains an open challenge.
For long-term spatial reasoning and adaptive decision-
making, memory-based spatial exploration allows agents
to retain and recall spatial knowledge. For example, 3D-
Mem [Yang et al., 2024d] introduces multi-view Memory
Snapshots to store explored spatial data and frontier snapshots
to identify unexplored areas, helping agents balance knowl-
edge retrieval and active exploration. This approach enhances
lifelong learning and autonomous adaptation, yet ensuring
scalability and developing efficient retrieval mechanisms will
be important for practical deployment.
As research progresses, improving multi-modal fusion, re-
fining spatial reasoning, and optimizing memory mechanisms
will be crucial for advancing LLM-driven spatial perception
and understanding in embodied intelligence.
4.1.2
Spatial Interaction and Navigation
Spatial interaction and navigation involve action execution
based on spatial perception and understanding. The actions
include planning robotic actions and predicting future trajec-
tories in spatial environments. Emerging research has dived
into combining MLLMs in spatial interaction and navigation.
Progress in this area mainly focuses on two aspects: motion
control and navigation.
Motion control can be categorized into simple action gen-
eration and interaction with a complex environment. The
former applies the perception ability of MLLMs to directly
generate the target action. For example, RT-2 [Zitkovich et al.,
2023] integrates vision-language models (VLMs) pre-trained
on internet-scale data into robot actions generation. VIMA
[Jiang et al., 2022] leverages a transformer-based architecture
designed to process multimodal prompts and generate motor
actions autoregressively. However, in a complex environment,
the reasoning ability enables spatial intelligence to handle
open-set tasks. VexPoser [Huang et al., 2023b] generates 3D
spatial representations and plan robot actions by leveraging
MLLMs’ reasoning and code-writing capabilities. GAJ-VGG
[Wang et al., 2023] designs a graph neural network (Graph
Action Justification) to construct a graph data representing the
layout of obstacles and their surrounding environment through
spatial and semantic relationships, and the robot outputs the
optimal action.

## Page 6

Spatial Perception and
Understanding
Spatial Interaction and 
Navigation
object identify
scene understanding
spatial memory
Environment with
Multimodal Data
Embodied
Agent
observe
move
manipulate
Complex
Spatial Task
'
Figure 5: A simple schematic of embodied spatial intelligence. The framework illustrates two sequential stages: spatial perception and
understanding and spatial interaction and navigation.
Navigation task perceives and memorizes the surrounding
environment, and predict the next location through reason-
ing. Based on the category of large model employed, navi-
gation can be divided into language-model-based and vision-
language-model-based task. By feeding structured text-based
maps into an LLM, Guide-LLM [Song et al., 2024] achieves
indoor spatial perception and leverages the reasoning capabili-
ties of LLM for path planning. NavGPT [Zhou et al., 2024a]
perceives the environment by using vision models to convert
environment images into text and applies an LLM to integrate
the current environmental descriptions with historical environ-
ment summaries, and perform trajectory planning. To bridge
the gap between LLM-based navigation paradigms and Vision-
Language-Navigation(VLN)-specialized models, NavGPT-2
[Zhou et al., 2025] integrates indoor visual observation with
MLLMs and combining navigation policy networks to im-
prove navigational reasoning. TopV-Nav [Zhong et al., 2024]
prompts MLLMs with the spatial arrangement of objects using
bounding boxes and text labels in the bird-view environment
image and conducts dynamic map scaling and target-guided
navigation through MLLM reasoning. MP5 [Qin et al., 2024]
designs an embodied system that decomposes complex open-
world tasks and perceives the environment through active per-
ception in Minecraft by calling MLLMS. VSI-Bench [Yang et
al., 2024b] probes the MLLMs to conduct indoor route plan-
ning and finds that MLLMs can work effectively with naive
cognitive map design. NWM [Bar et al., 2024] proposes a
controllable video generation model that predicts future target
frame for navigation.
4.2
Urban Spatial Intelligence
The embodied spatial intelligence primarily involves interac-
tion and movement within arm’s-reach micro-spaces, whereas
at larger scales, LLMs necessitate fundamentally distinct spa-
tial reasoning paradigms. This paradigm shift stems from
a critical scaling effect: as spatial dimensions expand, the
agent’s physical size becomes negligible relative to the en-
vironment. Consequently, the agent transitions from oper-
ating within a body-embedded concrete space to processing
extended spatial domains beyond immediate physical reach.
This transformation necessitates a cognitive shift from subjec-
tive embodiment to objective spatial representation, requiring
LLMs to conceptualize space as an independent entity with
abstract properties. Such representational capacity enables
advanced spatial functions including but not limited to cogni-
tive mapping, pathfinding, trajectory optimization, and even
generative spatial design.
Urban environments emerge as an optimal testing ground
for these macro-scale spatial intelligence developments. As
the most complex human-created spatial systems, cities in-
tegrate heterogeneous elements into multilayered structures
encompassing physical infrastructure, functional zones, and
socioeconomic networks. Their inherent spatial complexity
has already propelled interdisciplinary research frontiers like
urban computing and spatial econometrics, establishing es-
sential methodological foundations. As shown in Figure 6,
to systematically investigate urban spatial intelligence, we
propose a framework that distinguishes between understand-
ing, memory, reasoning, and intelligence capabilities. The
former evaluates the ability of LLMs to encode and retain
massive urban elements, while the latter examines their op-
erational competence in executing urban-specific tasks such
as mobility simulation, service allocation optimization, and
urban planning.
4.2.1
Spatial Understanding and Memory
Spatial memory refers to the ability of models to recall geo-
graphic information and relationships between different spatial
elements [Gurnee and Tegmark, 2024]. Pre-trained large lan-
guage models (LLMs) naturally acquire spatial priors from the
geographical data embedded in their training corpus [Manvi
et al., 2024]. This enables models to recognize, store, and
retrieve spatial information in a way that mimics human spa-
tial memory, which is crucial for tasks that require geographic
reasoning or interpretation.
It can be categorized into two key aspects: (1) regional fea-
ture understanding and (2) reasoning about spatial locations
and relationships. To understand regional features, Manvi et
al. [Manvi et al., 2023] have proposed GEOLLM to extract
geospatial knowledge from LLMs. The biases in geographic
information learned by LLMs are also examined [Manvi et
al., 2024].
Kuckreja et al.[Kuckreja et al., 2024] utilize
satellite images to understand regional features.
Satellite
images, combined with LLMs, are also used to predict so-
cioeconomic indicators [Yan et al., 2024]. Moreover, multi-
modal data—such as satellite images, language, and Points
of Interest (POIs)—is employed to better understand regional
characteristics and predict socioeconomic outcomes [Xiao
et al., 2024].
To reason about spatial locations and rela-
tionships, Ning et al.[Ning and Liu, 2024] leverage LLM-

## Page 7

Urban
Environment
•
Extract geospatial knowledge with
prompt engineering
•
Use LLMs to generate
       training data
Paradigms
Regional Feature Understanding
Tasks
•
Design a workflow to
       break down tasks
•
Integrate multiple factors to
reason
Paradigms
Geo-localization
Tasks
Mobility Generation
•
Utilize LLM agents
•
Align multimodal data
Paradigms
Navigation
Tasks
Signal Control
Planning
•
Store spatial relationship
based on LLM
•
Use tools to construct spatial
relationship datasets
Paradigms
Spatial Relationships
Tasks
Figure 6: Urban spatial intelligence can be categorized into four main types: spatial understanding, spatial memory, spatial reasoning, and
spatial intelligence. Each type includes its unique tasks and paradigms.
Agent to construct urban knowledge graphs [Liu et al., 2022;
Liu et al., 2023]. We summarize the key methodologies for
both aspects of spatial understanding. For regional feature un-
derstanding, one common approach is extracting prior knowl-
edge through prompt engineering, which involves collecting
spatial information from open-source data and aligning re-
gional features using multimodal data integration. Another
important strategy is leveraging LLMs to assist downstream
tasks by generating training data and providing guidance for
model training. Regarding spatial locations and relationships,
models can infer spatial structures based on their pre-trained
priors, using embedded geographic knowledge to reason about
spatial relationships. Additionally, automated tools have been
developed to construct and validate relationship datasets, fa-
cilitating the structured representation of spatial data and en-
hancing geographic reasoning.
4.2.2
Spatial Reasoning and Intelligence
Spatial reasoning in cities refers to deriving new spatial infor-
mation or predicting future urban dynamics based on spatial
data or spatial relationships through reasoning. For exam-
ple, GeoReasoner is a framework that integrates LLMs for
geospatial localization, leveraging high-quality street view
datasets to enhance spatial reasoning capabilities [Li et al.,
2024c]. Moreover, some research focuses on reasoning about
the potential behavior patterns of urban residents. Wang et
al. use LLM to model individual mobility in two stages: first,
identifying spatiotemporal patterns of residents’ mobility, and
second, using these patterns to generate trajectories [Wang et
al., 2024a]. Similarly, Feng et al. break the trajectory predic-
tion into three sub-tasks that influence mobility: remembering
individual mobility patterns, learning shared spatial transition
relationships of the group, and integrating spatial knowledge
of urban structures, fully leveraging LLMs’ knowledge of ge-
ographic space [Feng et al., 2024b]. Shao et al. develop a
Chain of Planned Behavior, which leverages the step-by-step
reasoning capability of LLMs to achieve recursive inference
of mobility intentions [Shao et al., 2024]. Gong et al. design a
visiting intent memory network and a human travel preference
prompt pool to help LLMs better understand the semantics of
visiting intentions and travel preferences [Gong et al., 2024].
Spatial intelligence in cities focuses on making decisions
and responding based on spatial data, with the ability to make
real-time judgments in complex urban environments. For ex-
ample, urban planning is a typical task that requires spatial
decision-making. Zhou et al. propose a multi-agent collabora-
tive framework for participatory urban planning [Zhou et al.,
2024b]. Moreover, traffic signal control dynamically adjusts to
the spatial environment, optimizing the traffic system’s overall
efficiency. LLMLight integrates the task description and real-
time traffic conditions into the prompt, leveraging the LLM’s
Chain-of-Thought reasoning capability to determine the opti-
mal control strategy [Lai et al., 2023]. Navigation tasks can
recognize real-time changes in complex spatial environments,
providing optimal navigation solutions. For example, Xu et
al. propose Flame [Xu et al., 2024a], which enhances reason-
ing capabilities in three stages: from understanding a single
street view description task to handling path planning tasks
with multiple images, and ultimately achieving end-to-end
spatial decision-making for navigation. Schumann et al. com-
bine LLM with real-world environmental interaction, using
a linguistic approach to process trajectories and visual obser-
vations, providing contextual prompts to the LLM to solve
decision-making problems in navigation tasks [Schumann et
al., 2024]. Specifically, Zeng et al. propose a Perceive-Reflect-
Plan workflow, enabling the LLM agent to autonomously nav-
igate in urban environments [Zeng et al., 2024].
4.3
Earth Spatial Intelligence
Earth Spatial Intelligence (ESI) is an interdisciplinary field
at the intersection of artificial intelligence and Earth sciences.
ESI addresses complex challenges across domains, includ-
ing climate science, geography, oceanography, and geology,
by leveraging large-scale spatio-temporal data and cutting-

## Page 8

Other Disciplines
Paradigms
•
Align spatial features with
LLM input embeddings
•
Design agentic workflow for
complex spatial reasoning
Tasks
AUV
Control
Wave Height
Prediction
Geological
Prediction
Geographic
Paradigms
•
Integrating GIS tools for autonomous
geospatial workflow
•
Directly query LLM or fine-tune LLM for
geospatial tasks
Tasks
Climate
Paradigms
•
Align multi-modal input data
for VLM encoding
•
Incorporate the pretrained
transformer layer in LLM for
time-series modeling
Tasks
Extreme Weather
Forecast
Temperature
Prediction
GIS Tool
Automation
Geospatial
Reasoning
Spatial Representation
Figure 7: Illustrations of representative earth spatial intelligence fields and paradigms.
edge techniques like LLMs and multimodal LLMs (MLLMs).
These models process vast datasets, uncover patterns, and
generate insights that drive modeling, decision-making, and
environmental resilience advancements. In climate science,
LLMs enhance the forecasting of precipitation and climate
events by capturing spatio-temporal dependencies and integrat-
ing meteorological raster data. In geography, they combine
with Geographic Information Systems (GIS) for automated
geospatial reasoning and localized spatial analyses while im-
proving contextual deduction through adaptive modules and
contrastive learning. In oceanography, vision-language models
enable natural language control of Autonomous Underwater
Vehicles (AUVs), while spatio-temporal encoding addresses
data sparsity, advancing wave height prediction and marine
environmental modeling. In geology, LLMs integrate imagery
and surveys to model geological phenomena, improve spa-
tial reasoning, and streamline remote sensing-based mineral
exploration. ESI is transforming Earth sciences by uniting
natural language understanding, multimodal integration, and
spatio-temporal reasoning. This rapidly evolving field offers
profound opportunities for scientific discovery, sustainable re-
source management, and tackling pressing global challenges.
4.3.1
Global Encoding
At the global scale, a crucial aspect of intelligence is the
proper encoding of location, enabling machines to perceive
and understand spatial information effectively. While large
language model-based applications typically represent lo-
cation using longitude and latitude [Manvi et al., 2023;
Yan and Lee, 2024], machine learning and deep learning ap-
proaches have adopted a variety of spatial representation meth-
ods [Wu et al., 2024]. Specifically, 2D representation methods
include approaches such as direct tile ID encoding, sinusoidal
location encoders, and kernel-based techniques, while 3D
methods encompass Cartesian coordinate encoding and vari-
ous self-supervised representation strategies. According to the
TorchSpatial benchmark [Wu et al., 2024], the Sphere2Vec-
sphereC+ method [Mai et al., 2023]—a self-supervised 3D
encoding technique that preserves the order between any two
points on Earth—is the most effective and informative location
encoding approach. Notably, even the direct tile ID encoding
method—despite being the lowest-performing among common
spatial representation techniques—significantly outperforms
GPT-4V [Wu et al., 2024]. This phenomenon may underscore
the discouraging applicability of large language models to
explicit spatial learning tasks; however, they excel in few-shot,
zero-shot, and similar scenarios, and demonstrate remarkable
flexibility in leveraging multi-source data.
4.3.2
Climate
Climate events have a strong spatio-temporal dependency,
which has been summarized as knowledge and commanded
by language models to some extent. Therefore, there has been
some trials in utilizing language models to predict or forecast
climate events. LLMDiff incorporated a frozen transformer
block from pre-trained LLM to serve as a universal visual en-
coder layer, with an intention of capturing long-term temporal
dependencies and accurately estimating motion trends for im-
proved precipitation nowcasting [She et al., 2024]. CLLMate
incorporated LLM and VLM to align meteorological raster
data with weather and climate event information and train on
the aligned datasets, enabling accurate forecasting of climate
events with raster data [Li et al., 2024b]. Notably, for the
climate domain, large models have been largely applied and
explored. GenCast [Ravuri et al., 2021] proposed a machine
learning-based weather prediction model that generates accu-
rate 15-day probabilistic ensemble weather forecasts. Pangu-
Weather [Bi et al., 2023] introduced three-dimensional deep
networks with Earth-specific priors and a hierarchical temporal
aggregation strategy to achieve medium-range global weather
forecasting. NowcastNet [Zhang et al., 2023b] achieved non-
linear nowcasting for extreme precipitation by combining
physical-evolution schemes and conditional-learning meth-
ods to produce high-resolution, physically plausible forecasts
with lead times up to 3 hours. Fuxi [Chen et al., 2023] in-
troduced a cascaded machine learning weather forecasting
system, which utilizes 39 years of ECMWF ERA5 reanalysis
data to provide 15-day global forecasts at a 6-hour temporal
resolution and 0.25° spatial resolution. The success of large
models in climate modeling validates the growing prediction
capabilities through training with large-scale data.
4.3.3
Geography
Considering the rich geographic knowledge commanded by
large language models, their direct application to geography-

## Page 9

related tasks has been widely explored. Geography-related
tasks either involve the extraction and sensing of location-
related knowledge across the global scale, or tasks requiring
direct judgments and operations involving specific locations,
such as localization and mapping. Two benchmark works com-
prehensively assess large language models’ capacities in these
two types of tasks. Manvi et al. find that naively querying
LLMs using geographic coordinates alone is ineffective for
predicting key indicators like population density; however, in-
corporating auxiliary map data from OpenStreetMap into the
prompts significantly improves prediction accuracy [Manvi
et al., 2023]. Roberts et al. find that while MLLMs perform
well in memory-based geographic tasks, such as identifying
locations or recognizing patterns from provided information,
they face significant challenges in reasoning-based or more
intelligent tasks, such as contextual deduction and advanced
geospatial analysis [Roberts et al., 2024]. To address the ex-
isting limitations of large language models, GeoGPT utilizes
mature GIS tools to tackle geospatial tasks, integrating the
semantic understanding ability of LLMs with GIS tools in
an autonomous manner [Zhang et al., 2023a]. GeoSEE in-
corporates six information collection modules, which LLMs
automatically select to adapt to specific indicators and coun-
tries [Han et al., 2024]. GeoReasoner incorporates two con-
trastive losses to enhance the reasoning ability of language
models by making representations of nearby locations and the
same entities more similar [Yan and Lee, 2024].
4.3.4
Other Disciplines
LLMs have also been applied in other disciplines such as
marine science and geology. With remarkable abilities like
natural language understanding, generalizability, and reason-
ing, LLMs have been leveraged to tackle typical challenges in
these disciplines such as data sparsity and complex decision-
making.
In marine science, LLMs have been used for vehicle control
due to their capability of spatial planning and reasoning. For
example, OceanPlan leverages LLMs to control Autonomous
Underwater Vehicle (AUV) through natural language com-
mand [Yang et al., 2024c]. Specifically, it leverages a vision-
language model to convert image observation into textual
semantic map to memorize the explored ocean environment. It
further proposes a hierarchical planning framework to convert
natural language commands to control inputs for AUV, and
adaptively adjust the plan in special circumstances. Moreover,
the generalization and few-shot learning abilities of LLMs
are suitable for addressing the data-sparsity issue in spatial
prediction. Li et al. use LLMs to predict the ocean significant
wave height with sparse observation data [Li et al., 2024d]. To
enhance the spatial understanding ability of LLM, they first
encode the spatio-temporal features from the observation data
through a spatio-temporal encoder, which is then aligned with
the embeddings of natural language prompt and fed into the
LLM together for prediction.
In geology, Xu et al. use LLMs to predict the geological
condition in tunnels [Xu et al., 2024b]. They first construct a
knowledge graph (KG) to integrate multimodal data and trans-
form them into low-dimensional KG embeddings. Then they
align the KG embeddings with prompt embeddings through
patch reprogramming, and input them into LLM for prediction.
Yu et al. propose a multi-agent collaboration framework to
enhance the spatial reasoning ability of MLLM for remote-
sensing mineral exploration [Yu et al., 2024a]. It construct
multiple MLLM agents responsible for identifying different
features from different remote-sensing images and integrate
them together, which shows considerable performance.
Overall, the application of LLM spatial intelligence in these
disciplines can be summarized in two ways: (1) Aligning
spatial features with prompt embeddings and input them into
the LLM for prediction tasks. (2) Designing agentic workflow
with LLMs to enable complex spatial reasoning.
5
Challenges and Discussions
5.1
Fundamental Spatial Intelligence
The study of fundamental spatial intelligence raises several
critical questions and challenges. First, the form of spatial
reasoning—the core of spatial intelligence—remains a central
issue: is language-based spatial reasoning the most effective
form currently known, or are there more universal and effec-
tive modeling approaches, such as graph-based representa-
tions or multi-modal frameworks? Second, the comprehensive
evaluation of general spatial intelligence poses a significant
challenge. Current frameworks often focus on specific tasks
or domains, lacking a unified approach to assess spatial intel-
ligence across diverse contexts, domains, and scales. Such
a unified evaluation is crucial for understanding the relation-
ship between fundamental spatial intelligence and its mani-
festations in other domains. This requires investigating how
core spatial abilities, like mental rotation or spatial memory,
translate into higher-order applications in specialized fields.
Addressing these questions will not only advance our theoreti-
cal understanding of spatial intelligence but also inform the
development of more robust and effective models for artificial
general intelligence.
5.2
Embodied Spatial Intelligence
For embodied intelligence, two significant challenges remain
in the research on spatial memory and intelligence. First,
the current work on embodied intelligence only partially in-
corporates prior knowledge of spatial cognition as a source
of inspiration in method design. While some studies draw
loosely from principles of human spatial cognition—such as
wayfinding, mental mapping, or object manipulation—these
inspirations are often superficial and lack a systematic inte-
gration into the computational models. Therefore, there is
a pressing need for an approach that deeply couples model
design with the underlying mechanisms of human spatial cog-
nition. Such an approach would not only improve the robust-
ness and adaptability of these models but also provide insights
into the fundamental principles of human intelligence. How-
ever, achieving this integration is inherently challenging, as
it requires bridging the gap between cognitive science, neuro-
science, and embodied artificial intelligence. Second, research
on embodied intelligence encompasses a wide spectrum of
multi-level spatial intelligence and cognition, each with dis-
tinct characteristics. For example, at the lower level, tasks

## Page 10

such as robotic manipulation demand fine-grained motor con-
trol and precise spatial reasoning to interact with objects in
a constrained environment. On the other hand, higher-level
tasks like path-planning for unmanned aerial vehicles (UAVs)
involve large-scale spatial reasoning. Therefore, it is an open
question whether it is possible to build a universal model inte-
grating multi-level (i.e., multi-grained) spatial intelligence in
embodied AI tasks.
5.3
Urban Spatial Intelligence
Although significant progress has been made in urban spa-
tial intelligence, several critical challenges remain. First, the
heterogeneity of urban data poses fundamental limitations:
current frameworks struggle to harmonize multimodal inputs
(e.g., satellite imagery, POIs, and mobility patterns) into uni-
fied spatial representations, often leading to fragmented un-
derstanding. And the most often text-based representation
of complex spatial structures is always doubtable for urban
professionals. Second, the robustness of spatial reasoning re-
mains constrained by LLMs’ reliance on static training data,
which inadequately capture dynamic urban phenomena such
as real-time traffic flows or evolving socioeconomic factors.
Third, the interpretability gap in LLM-driven spatial decisions
in urban planning and navigation tasks raises concerns about
trustworthiness, particularly when models prioritize statisti-
cal correlations over causal spatial relationships. Therefore,
future research may prioritize three directions: (1) dynamic
spatial modeling to integrate real-time data with LLMs, en-
abling adaptive responses to urban dynamics while address-
ing constraints; (2) Causal spatial reasoning frameworks that
disentangle environmental, social, and infrastructural interde-
pendencies, solving the concern and resistance about dealing
spatial information in text paradigm; (3) Ethical challenges
in the mitigation of spatial bias, which is highlighted by geo-
graphic priors in LLM, demand systematic auditing methods
to ensure equitable urban intelligence applications.
5.4
Earth Spatial Intelligence
LLM holds transformative potential for advancing Earth Spa-
tial Intelligence, but several challenges must be overcome
to fully realize their capabilities. One key limitation is their
performance in reasoning-intensive tasks, such as contextual
deduction and advanced spatial analysis in geography, geol-
ogy, and other domains, where bottlenecks persist. While
multimodal LLMs (MLLMs) and emerging frameworks like
GeoReasoner and MineAgent show promise by leveraging
contrastive learning and multi-agent systems, further inno-
vation is required to achieve robust geospatial understand-
ing. The integration of domain-specific data also presents
significant hurdles. For instance, marine sciences often grap-
ple with data sparsity, necessitating tailored solutions like
OceanGPT and spatio-temporal encoders. Meanwhile, do-
mains like geology and climate science depend heavily on
complex and multimodal inputs, including knowledge graph
embeddings and specialized prompts, which demand seamless
alignment within LLM architectures. Future research direc-
tions include leveraging transfer learning to adapt pre-trained
models across related Earth science domains, thereby reducing
data requirements and fostering knowledge sharing. Bench-
marking platforms like OceanBench and integrated systems
such as GeoGPT could provide standardization and rigorous
evaluation across ESI subfields, enabling targeted advance-
ments. Human-in-the-loop systems and explainable AI (XAI)
frameworks could further enhance interpretability and trust,
while advances in causal inference offer the potential to better
capture dynamic Earth processes. Interdisciplinary collabo-
ration will be essential to translate these advancements into
actionable solutions for climate resilience and sustainable de-
velopment. By tackling these challenges, LLMs can unlock
more precise predictions and insights to address global envi-
ronmental challenges.
5.5
Relation with World Model
In this paper, we investigate spatial understanding and task-
solving within the domain of spatial intelligence. The concept
of world models has recently emerged as a significant topic
in this field, particularly in embodied spatial intelligence, pro-
pelled by advancements in diffusion-based generative models.
As outlined in a recent survey [Ding et al., 2024], world mod-
els—rooted in psychological mental models—serve two key
functions: constructing internal representations to interpret
the underlying mechanisms of the world and predicting future
states to guide decision-making. Our work primarily focuses
on the first function, developing internal representations to
deepen spatial comprehension. In computational terms, this
aligns with model-based reinforcement learning, where param-
eterized environmental models enhance intelligent behavior.
While we address most aspects of world models, our emphasis
lies in understanding rather than the generative aspect, such
as forecasting outcomes. For a more extensive exploration of
generative capabilities, we refer readers to [Ding et al., 2024].
Looking forward, we propose that integrating these generative
capabilities into spatial intelligence modeling holds consider-
able promise. This could enable more robust systems capable
of not only understanding but also predicting and acting within
the physical world, potentially addressing limitations seen in
current foundation models, such as the lack of granularity in
urban knowledge highlighted by Feng et al. [Feng et al., 2024a;
Feng et al., 2024c].
6
Conclusion
This paper begins with a discussion of human spatial intelli-
gence research in neuroscience and cognitive science, review-
ing and summarizing studies on spatial intelligence across var-
ious disciplines, particularly at different spatial scales, since
the era of LLMs. It aims to provide a comprehensive overview
of spatial intelligence research across domains, helping to
contextualize existing studies and inspire future research di-
rections. We believe that cross-domain spatial intelligence
research at multi-scales will emerge as a crucial area of study
in the future, generating significant impacts and profound
applications across multiple fields. Furthermore, in-depth in-
vestigations into spatial intelligence will, in turn, inform the
development of general artificial intelligence, laying a solid
foundation for humanity’s advancement toward true artificial
general intelligence.

## Page 11

References
[Bar et al., 2024] Amir Bar, Gaoyue Zhou, Danny Tran,
Trevor Darrell, and Yann LeCun. Navigation world models.
arXiv preprint arXiv:2412.03572, 2024.
[Bhandari et al., 2023] Prabin Bhandari, Antonios Anasta-
sopoulos, and Dieter Pfoser. Are large language models
geospatially knowledgeable? In Proceedings of the 31st
ACM International Conference on Advances in Geographic
Information Systems, pages 1–4, 2023.
[Bi et al., 2023] Kaifeng Bi, Lingxi Xie, Hengheng Zhang,
Xin Chen, Xiaotao Gu, and Qi Tian. Accurate medium-
range global weather forecasting with 3d neural networks.
Nature, 619(7970):533–538, 2023.
[Cai et al., 2024] Wenxiao Cai, Yaroslav Ponomarenko, Jian-
hao Yuan, Xiaoqi Li, Wankou Yang, Hao Dong, and
Bo Zhao. Spatialbot: Precise spatial understanding with
vision language models. arXiv preprint arXiv:2406.13642,
2024.
[Chen et al., 2023] Lei Chen, Xiaohui Zhong, et al. Fuxi: A
cascade machine learning forecasting system for 15-day
global weather forecast. npj Clim. Atmos. Sci., 2023.
[Chen et al., 2024] Boyuan Chen, Zhuo Xu, et al. Spatialvlm:
Endowing vision-language models with spatial reasoning
capabilities. In Proc. of CVPR, 2024.
[Cohen, 1993] NJ Cohen.
Memory, amnesia and the hip-
pocampal system. MIT Press, 1993.
[Ding et al., 2024] Jingtao Ding, Yunke Zhang, Yu Shang,
Yuheng Zhang, Zefang Zong, Jie Feng, Yuan Yuan,
Hongyuan Su, Nian Li, Nicholas Sukiennik, et al. Un-
derstanding world or predicting future? a comprehensive
survey of world models. arXiv preprint arXiv:2411.14499,
2024.
[Eichenbaum and Cohen, 2014] Howard Eichenbaum and
Neal J Cohen. Can we reconcile the declarative mem-
ory and spatial navigation views on hippocampal function?
Neuron, 83(4):764–770, 2014.
[Epstein et al., 2017] Russell A Epstein, Eva Zita Patai,
Joshua B Julian, and Hugo J Spiers. The cognitive map
in humans: spatial navigation and beyond. Nature neuro-
science, 20(11):1504–1513, 2017.
[Farzanfar et al., 2023] Delaram Farzanfar, Hugo J Spiers,
Morris Moscovitch, and R Shayna Rosenbaum. From cogni-
tive maps to spatial schemas. Nature Reviews Neuroscience,
24(2):63–79, 2023.
[Feng et al., 2024a] Jie Feng, Yuwei Du, Tianhui Liu, Siqi
Guo, Yuming Lin, and Yong Li. Citygpt: Empowering
urban spatial cognition of large language models. arXiv
preprint arXiv:2406.13948, 2024.
[Feng et al., 2024b] Jie Feng, Yuwei Du, Jie Zhao, and Yong
Li. Agentmove: Predicting human mobility anywhere using
large language model based agentic framework. arXiv
preprint arXiv:2408.13986, 2024.
[Feng et al., 2024c] Jie Feng, Jun Zhang, Tianhui Liu, Xin
Zhang, Tianjian Ouyang, Junbo Yan, Yuwei Du, Siqi Guo,
and Yong Li. Citybench: Evaluating the capabilities of
large language models for urban tasks, 2024.
[Fu et al., 2024] Rao Fu, Jingyu Liu, Xilun Chen, Yixin Nie,
and Wenhan Xiong. Scene-llm: Extending language model
for 3d visual understanding and reasoning. arXiv preprint
arXiv:2403.11401, 2024.
[Gilboa and Marlatte, 2017] Asaf Gilboa and Hannah Mar-
latte. Neurobiology of schemas and schema-mediated mem-
ory. Trends in cognitive sciences, 21(8):618–631, 2017.
[Gong et al., 2024] Letian Gong, Yan Lin, Xinyue Zhang, Yi-
wen Lu, Xuedi Han, Yichen Liu, Shengnan Guo, Youfang
Lin, and Huaiyu Wan.
Mobility-llm: Learning visit-
ing intentions and travel preferences from human mo-
bility data with large language models. arXiv preprint
arXiv:2411.00823, 2024.
[Gupta et al., 2021] Agrim Gupta, Silvio Savarese, et al. Em-
bodied intelligence via learning and evolution.
Nature
communications, 2021.
[Gurnee and Tegmark, 2024] Wes Gurnee and Max Tegmark.
Language models represent space and time, 2024.
[Haas et al., 2024] Lukas Haas, Michal Skreta, Silas Alberti,
and Chelsea Finn. Pigeon: Predicting image geolocations.
In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pages 12893–12902, 2024.
[Han et al., 2024] Sungwon Han, Donghyun Ahn, Seungeon
Lee, Minhyuk Song, Sungwon Park, Sangyoon Park, Ji-
hee Kim, and Meeyoung Cha. Geosee: Regional socio-
economic estimation with a large language model. arXiv
preprint arXiv:2406.09799, 2024.
[Huang et al., 2023a] Lei Huang, Weijiang Yu, Weitao Ma,
Weihong Zhong, Zhangyin Feng, Haotian Wang, Qiang-
long Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, et al.
A survey on hallucination in large language models: Prin-
ciples, taxonomy, challenges, and open questions. arXiv
preprint arXiv:2311.05232, 2023.
[Huang et al., 2023b] Wenlong Huang, Chen Wang, Ruohan
Zhang, Yunzhu Li, Jiajun Wu, and Li Fei-Fei. Voxposer:
Composable 3d value maps for robotic manipulation with
language models. arXiv preprint arXiv:2307.05973, 2023.
[Ishikawa, 2021] Toru Ishikawa. Spatial thinking, cognitive
mapping, and spatial awareness. Cognitive Processing,
22(Suppl 1):89–96, 2021.
[Jiang et al., 2022] Yunfan Jiang, Agrim Gupta, Zichen
Zhang, Guanzhi Wang, Yongqiang Dou, Yanjun Chen,
Li Fei-Fei, Anima Anandkumar, Yuke Zhu, and Linxi
Fan. Vima: General robot manipulation with multimodal
prompts. arXiv preprint arXiv:2210.03094, 2(3):6, 2022.
[Kazemi et al., 2023] Mehran Kazemi, Hamidreza Alvari,
Ankit Anand, Jialin Wu, Xi Chen, and Radu Soricut. Ge-
omverse: A systematic evaluation of large models for geo-
metric reasoning. arXiv preprint arXiv:2312.12241, 2023.
[Kuckreja et al., 2024] Kartik Kuckreja, Muhammad Sohail
Danish, Muzammal Naseer, Abhijit Das, Salman Khan,
and Fahad Shahbaz Khan. Geochat: Grounded large vision-
language model for remote sensing. In Proceedings of the

## Page 12

IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 27831–27840, 2024.
[Lai et al., 2023] Siqi Lai, Zhao Xu, Weijia Zhang, Hao Liu,
and Hui Xiong. Large language models as traffic signal
control agents: Capacity and opportunity. arXiv preprint
arXiv:2312.16044, 2023.
[Lee et al., 2022] Nayeon Lee, Wei Ping, Peng Xu, Mostofa
Patwary, Pascale N Fung, Mohammad Shoeybi, and Bryan
Catanzaro. Factuality enhanced language models for open-
ended text generation. Advances in Neural Information
Processing Systems, 35:34586–34599, 2022.
[Lehnert et al., 2024] Lucas Lehnert, Sainbayar Sukhbaatar,
DiJia Su, Qinqing Zheng, Paul Mcvay, Michael Rabbat,
and Yuandong Tian. Beyond a*: Better planning with
transformers via search dynamics bootstrapping. arXiv
preprint arXiv:2402.14083, 2024.
[Li et al., 2024a] Fangjun Li, David C Hogg, and Anthony G
Cohn. Advancing spatial reasoning in large language mod-
els: An in-depth evaluation and enhancement using the
stepgame benchmark. In Proceedings of the AAAI Confer-
ence on Artificial Intelligence, volume 38, pages 18500–
18507, 2024.
[Li et al., 2024b] Haobo Li, Zhaowei Wang, Jiachen Wang,
Alexis Kai Hon Lau, and Huamin Qu. Cllmate: A multi-
modal llm for weather and climate events forecasting. arXiv
preprint arXiv:2409.19058, 2024.
[Li et al., 2024c] Ling Li, Yu Ye, Bingchuan Jiang, and Wei
Zeng. Georeasoner: Geo-localization with reasoning in
street views using a large vision-language model. In Forty-
first International Conference on Machine Learning, 2024.
[Li et al., 2024d] Zhe Li, Ronghui Xu, Jilin Hu, Zhong Peng,
Xi Lu, Chenjuan Guo, and Bin Yang. Ocean significant
wave height estimation with spatio-temporally aware large
language models. In Proceedings of the 33rd ACM Interna-
tional Conference on Information and Knowledge Manage-
ment, pages 3892–3896, 2024.
[Li et al., 2024e] Zhonghang Li, Lianghao Xia, et al. Ur-
bangpt: Spatio-temporal large language models. In Proc.
of KDD, 2024.
[Lin et al., 2024] Jinzhou Lin, Han Gao, et al. Advances in
Embodied Navigation Using Large Language Models: A
survey. arXiv:2311.00530, 2024.
[Liu et al., 2022] Yu Liu, Jingtao Ding, and Yong Li. Devel-
oping knowledge graph based system for urban computing.
In Proceedings of the 1st ACM SIGSPATIAL International
Workshop on Geospatial Knowledge Graphs, pages 3–7,
2022.
[Liu et al., 2023] Yu Liu, Jingtao Ding, Yanjie Fu, and
Yong Li. Urbankg: An urban knowledge graph system.
ACM Transactions on Intelligent Systems and Technology,
14(4):1–25, 2023.
[Long et al., 2025] Xiaoyang Long, Daniel Bush, Bin Deng,
Neil Burgess, and Sheng-Jia Zhang. Allocentric and ego-
centric spatial representations coexist in rodent medial en-
torhinal cortex. Nature Communications, 16(1):356, 2025.
[Luo et al., 2024] Zihan Luo, Xiran Song, Hong Huang,
Jianxun Lian, Chenhao Zhang, Jinqi Jiang, and Xing
Xie. Graphinstruct: Empowering large language models
with graph understanding and reasoning capability. arXiv
preprint arXiv:2403.04483, 2024.
[Mai et al., 2021] Gengchen Mai, Krzysztof Janowicz, Rui
Zhu, Ling Cai, and Ni Lao. Geographic question answering:
challenges, uniqueness, classification, and future directions.
AGILE: GIScience series, 2:8, 2021.
[Mai et al., 2023] Gengchen
Mai,
Yao
Xuan,
et
al.
Sphere2Vec:
A general-purpose location representa-
tion learning over a spherical surface for large-scale
geospatial predictions. ISPRS J. P. Remote Sens., 2023.
[Mansourian and Oucheikh, 2024] Ali
Mansourian
and
Rachid Oucheikh. Chatgeoai: Enabling geospatial analysis
for public through natural language, with large language
models. ISPRS International Journal of Geo-Information,
13(10):348, 2024.
[Manvi et al., 2023] Rohin Manvi, Samar Khanna, Gengchen
Mai, Marshall Burke, David Lobell, and Stefano Ermon.
Geollm: Extracting geospatial knowledge from large lan-
guage models. arXiv preprint arXiv:2310.06213, 2023.
[Manvi et al., 2024] Rohin Manvi, Samar Khanna, Marshall
Burke, David Lobell, and Stefano Ermon.
Large lan-
guage models are geographically biased. arXiv preprint
arXiv:2402.02680, 2024.
[Momennejad et al., 2024] Ida Momennejad, Hosein Hasan-
beig, Felipe Vieira Frujeri, Hiteshi Sharma, Nebojsa Jojic,
Hamid Palangi, Robert Ness, and Jonathan Larson. Evaluat-
ing cognitive maps and planning in large language models
with cogeval. Advances in Neural Information Processing
Systems, 36, 2024.
[Moser et al., 2008] Edvard I Moser, Emilio Kropff, and
May-Britt Moser. Place cells, grid cells, and the brain’s spa-
tial representation system. Annu. Rev. Neurosci., 31(1):69–
89, 2008.
[Moser et al., 2017] Edvard I Moser, May-Britt Moser, and
Bruce L McNaughton. Spatial representation in the hip-
pocampal formation: a history.
Nature neuroscience,
20(11):1448–1464, 2017.
[Ning and Liu, 2024] Yansong Ning and Hao Liu.
Ur-
bankgent: A unified large language model agent framework
for urban knowledge graph construction. arXiv preprint
arXiv:2402.06861, 2024.
[Petroni et al., 2019] Fabio Petroni, Tim Rockt¨aschel, Patrick
Lewis, Anton Bakhtin, Yuxiang Wu, Alexander H Miller,
and Sebastian Riedel. Language models as knowledge
bases? arXiv preprint arXiv:1909.01066, 2019.
[Qin et al., 2024] Yiran Qin, Enshen Zhou, Qichang Liu,
Zhenfei Yin, Lu Sheng, Ruimao Zhang, Yu Qiao, and Jing
Shao. Mp5: A multi-modal open-ended embodied system
in minecraft via active perception. In 2024 IEEE/CVF
Conference on Computer Vision and Pattern Recognition
(CVPR), pages 16307–16316. IEEE, 2024.

## Page 13

[Ravuri et al., 2021] Suman Ravuri, Karel Lenc, Matthew
Willson, Dmitry Kangin, Remi Lam, Piotr Mirowski,
Megan Fitzsimons,
Maria Athanassiadou,
Sheleem
Kashem, Sam Madge, et al. Skilful precipitation now-
casting using deep generative models of radar. Nature,
597(7878):672–677, 2021.
[Roberts et al., 2020] Adam Roberts, Colin Raffel, and Noam
Shazeer.
How much knowledge can you pack into
the parameters of a language model?
arXiv preprint
arXiv:2002.08910, 2020.
[Roberts et al., 2024] Jonathan Roberts, Timo L¨uddecke, Re-
han Sheikh, Kai Han, and Samuel Albanie. Charting new
territories: Exploring the geographic and geospatial capabil-
ities of multimodal llms. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition,
pages 554–563, 2024.
[Schumann et al., 2024] Raphael Schumann, Wanrong Zhu,
Weixi Feng, Tsu-Jui Fu, Stefan Riezler, and William Yang
Wang. Velma: Verbalization embodiment of llm agents
for vision and language navigation in street view. In Pro-
ceedings of the AAAI Conference on Artificial Intelligence,
volume 38, pages 18924–18933, 2024.
[Shao et al., 2024] Chenyang Shao, Fengli Xu, Bingbing Fan,
Jingtao Ding, Yuan Yuan, Meng Wang, and Yong Li. Be-
yond imitation: Generating human mobility from context-
aware reasoning with large language models. arXiv preprint
arXiv:2402.09836, 2024.
[Sharma, 2023] Manasi Sharma. Exploring and improving
the spatial reasoning abilities of large language models. In
I Can’t Believe It’s Not Better Workshop: Failure Modes in
the Age of Foundation Models, 2023.
[She et al., 2024] Lei She, Chenghong Zhang, Xin Man, and
Jie Shao. Llmdiff: Diffusion model using frozen llm trans-
formers for precipitation nowcasting. Sensors, 24(18):6049,
2024.
[Song et al., 2024] Sangmim Song, Sarath Kodagoda, Amal
Gunatilake, Marc G Carmichael, Karthick Thiyagarajan,
and Jodi Martin. Guide-llm: An embodied llm agent and
text-based topological map for robotic guidance of people
with visual impairments. arXiv preprint arXiv:2410.20666,
2024.
[Tolman, 1948] Edward C Tolman. Cognitive maps in rats
and men. Psychological review, 55(4):189, 1948.
[Wang et al., 2023] Xiaohan Wang, Yuehu Liu, Xinhang
Song, Beibei Wang, and Shuqiang Jiang. Generating ex-
planations for embodied action decision from visual ob-
servation. In Proceedings of the 31st ACM International
Conference on Multimedia, pages 2838–2846, 2023.
[Wang et al., 2024a] Jiawei Wang, Renhe Jiang, Chuang
Yang, Zengqing Wu, Makoto Onizuka, Ryosuke Shibasaki,
Noboru Koshizuka, and Chuan Xiao. Large language mod-
els as urban residents: An llm agent framework for personal
mobility generation.
arXiv preprint arXiv:2402.14744,
2024.
[Wang et al., 2024b] Tai Wang, Xiaohan Mao, Chenming
Zhu, Runsen Xu, Ruiyuan Lyu, Peisen Li, Xiao Chen, Wen-
wei Zhang, Kai Chen, Tianfan Xue, et al. Embodiedscan: A
holistic multi-modal 3d perception suite towards embodied
ai. In Proceedings of the IEEE/CVF Conference on Com-
puter Vision and Pattern Recognition, pages 19757–19767,
2024.
[Whittington et al., 2020] James CR Whittington, Timothy H
Muller, Shirley Mark, Guifen Chen, Caswell Barry,
Neil Burgess, and Timothy EJ Behrens.
The tolman-
eichenbaum machine: unifying space and relational mem-
ory through generalization in the hippocampal formation.
Cell, 183(5):1249–1263, 2020.
[Whittington et al., 2021] James CR Whittington, Joseph
Warren, and Timothy EJ Behrens. Relating transformers
to models and neural representations of the hippocampal
formation. arXiv preprint arXiv:2112.04035, 2021.
[Wu et al., 2024] Nemin Wu, Qian Cao, et al. Torchspatial:
A location encoding framework and benchmark for spatial
representation learning. In Proc. of NeurIPS, 2024.
[Xiao et al., 2024] Congxi Xiao, Jingbo Zhou, Yixiong Xiao,
Jizhou Huang, and Hui Xiong. Refound: Crafting a founda-
tion model for urban region understanding upon language
and visual foundations. In Proceedings of the 30th ACM
SIGKDD Conference on Knowledge Discovery and Data
Mining, pages 3527–3538, 2024.
[Xu et al., 2024a] Yunzhe Xu, Yiyuan Pan, Zhe Liu, and
Hesheng Wang.
Flame:
Learning to navigate with
multimodal llm in urban environments. arXiv preprint
arXiv:2408.11051, 2024.
[Xu et al., 2024b] Zhenhao Xu, Zhaoyang Wang, Shucai Li,
Xiao Zhang, and Peng Lin. Geopredict-llm: Intelligent
tunnel advanced geological prediction by reprogramming
large language models. Intelligent Geoengineering, 1(1):49–
57, 2024.
[Xu et al., 2025] Wenrui Xu, Dalin Lyu, Weihang Wang, Jie
Feng, Chen Gao, and Yong Li. Defining and evaluating
visual language models’ basic spatial abilities: A perspec-
tive from psychometrics. arXiv preprint arXiv:2502.11859,
2025.
[Yamada et al., 2023] Yutaro Yamada, Yihan Bao, Andrew K
Lampinen, Jungo Kasai, and Ilker Yildirim. Evaluating
spatial understanding of large language models.
arXiv
preprint arXiv:2310.14540, 2023.
[Yan and Lee, 2024] Yibo Yan and Joey Lee. Georeasoner:
Reasoning on geospatially grounded context for natural
language understanding. In Proceedings of the 33rd ACM
International Conference on Information and Knowledge
Management, pages 4163–4167, 2024.
[Yan et al., 2024] Yibo Yan, Haomin Wen, Siru Zhong, Wei
Chen, Haodong Chen, Qingsong Wen, Roger Zimmermann,
and Yuxuan Liang. Urbanclip: Learning text-enhanced
urban region profiling with contrastive language-image pre-
training from the web. In Proceedings of the ACM on Web
Conference 2024, pages 4006–4017, 2024.

## Page 14

[Yang et al., 2024a] Fan Yang, Sicheng Zhao, Yanhao Zhang,
Haoxiang Chen, Hui Chen, Wenbo Tang, Haonan Lu,
Pengfei Xu, Zhenyu Yang, Jungong Han, et al. Llmi3d:
Empowering llm with 3d perception from a single 2d image.
arXiv preprint arXiv:2408.07422, 2024.
[Yang et al., 2024b] Jihan Yang, Shusheng Yang, Anjali W.
Gupta, Rilyn Han, Li Fei-Fei, and Saining Xie. Think-
ing in space: How multimodal large language models see,
remember, and recall spaces, 2024.
[Yang et al., 2024c] Ruochu Yang,
Fumin Zhang,
and
Mengxue Hou.
Oceanplan: Hierarchical planning and
replanning for natural language auv piloting in large-
scale unexplored ocean environments.
arXiv preprint
arXiv:2403.15369, 2024.
[Yang et al., 2024d] Yuncong Yang, Han Yang, Jiachen Zhou,
Peihao Chen, Hongxin Zhang, Yilun Du, and Chuang Gan.
3d-mem: 3d scene memory for embodied exploration and
reasoning. arXiv preprint arXiv:2411.17735, 2024.
[Yu et al., 2024a] Beibei Yu, Tao Shen, Hongbin Na, Ling
Chen, and Denqi Li. Mineagent: Towards remote-sensing
mineral exploration with multimodal large language mod-
els. arXiv preprint arXiv:2412.17339, 2024.
[Yu et al., 2024b] Jun Yu, Yunxiang Zhang, Zerui Zhang,
Zhao Yang, Gongpeng Zhao, Fengzhao Sun, Fanrui Zhang,
Qingsong Liu, Jianqing Sun, Jiaen Liang, et al. Rag-guided
large language models for visual spatial description with
adaptive hallucination corrector. In Proceedings of the
32nd ACM International Conference on Multimedia, pages
11407–11413, 2024.
[Zeng et al., 2024] Qingbin Zeng, Qinglong Yang, Shunan
Dong, Heming Du, Liang Zheng, Fengli Xu, and Yong
Li. Perceive, reflect, and plan: Designing llm agent for
goal-directed city navigation without instructions. arXiv
preprint arXiv:2408.04168, 2024.
[Zhang et al., 2023a] Yifan Zhang, Cheng Wei, Shangyou
Wu, Zhengting He, and Wenhao Yu. Geogpt: understand-
ing and processing geospatial tasks through an autonomous
gpt. arXiv preprint arXiv:2307.07930, 2023.
[Zhang et al., 2023b] Yuchen
Zhang,
Mingsheng
Long,
Kaiyuan Chen, Lanxiang Xing, Ronghua Jin, Michael I
Jordan, and Jianmin Wang. Skilful nowcasting of extreme
precipitation with nowcastnet. Nature, 619(7970):526–532,
2023.
[Zhang et al., 2023c] Zihan Zhang, Meng Fang, Ling Chen,
Mohammad-Reza Namazi-Rad, and Jun Wang. How do
large language models capture the ever-changing world
knowledge? a review of recent advances. arXiv preprint
arXiv:2310.07343, 2023.
[Zhang et al., 2024] Jiaxin Zhang, Zhongzhi Li, Mingliang
Zhang, Fei Yin, Chenglin Liu, and Yashar Moshfeghi.
Geoeval: benchmark for evaluating llms and multi-modal
models on geometry problem-solving.
arXiv preprint
arXiv:2402.10104, 2024.
[Zhao et al., 2024] Tianjie Zhao, Sheng Wang, et al. Artifi-
cial intelligence for geoscience: Progress, challenges and
perspectives. The Innovation, 2024.
[Zheng et al., 2024] Duo Zheng, Shijia Huang, and Liwei
Wang. Video-3d llm: Learning position-aware video rep-
resentation for 3d scene understanding. arXiv preprint
arXiv:2412.00493, 2024.
[Zhong et al., 2024] Linqing Zhong, Chen Gao, Zihan Ding,
Yue Liao, and Si Liu. Topv-nav: Unlocking the top-view
spatial reasoning potential of mllm for zero-shot object
navigation. arXiv preprint arXiv:2411.16425, 2024.
[Zhou et al., 2024a] Gengze Zhou, Yicong Hong, and Qi Wu.
Navgpt: Explicit reasoning in vision-and-language nav-
igation with large language models. In Proceedings of
the AAAI Conference on Artificial Intelligence, volume 38,
pages 7641–7649, 2024.
[Zhou et al., 2024b] Zhilun Zhou, Yuming Lin, Depeng Jin,
and Yong Li. Large language model for participatory urban
planning. arXiv preprint arXiv:2402.17161, 2024.
[Zhou et al., 2025] Gengze Zhou, Yicong Hong, Zun Wang,
Xin Eric Wang, and Qi Wu. Navgpt-2: Unleashing naviga-
tional reasoning capability for large vision-language mod-
els. In European Conference on Computer Vision, pages
260–278. Springer, 2025.
[Zitkovich et al., 2023] Brianna
Zitkovich,
Tianhe
Yu,
Sichun Xu, Peng Xu, Ted Xiao, Fei Xia, Jialin Wu, Paul
Wohlhart, Stefan Welker, Ayzaan Wahid, et al.
Rt-2:
Vision-language-action models transfer web knowledge to
robotic control. In Conference on Robot Learning, pages
2165–2183. PMLR, 2023.
