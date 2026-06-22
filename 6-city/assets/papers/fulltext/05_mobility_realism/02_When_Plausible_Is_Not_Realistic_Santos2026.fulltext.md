---
title: "When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Simulation"
source_pdf: "05_mobility_realism\\02_When_Plausible_Is_Not_Realistic_Santos2026.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-06-22T16:10:39+00:00
page_count: 14
status: ok
text_char_count: 82865
quality_flags: []
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\05_mobility_realism\02_When_Plausible_Is_Not_Realistic_Santos2026.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-06-22T16:10:39+00:00
- Page count: 14
- Status: ok
- Text chars: 82865
- Quality flags: none

## Metadata

- Title: When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Simulation
- Author: Gustavo H. Santos; Aline Carneiro Viana; Thiago H. Silva
- DOI: unknown
- Keywords: Large Language Models, Generative Agents, Urban Simulation, Human Mobility, Mobility Validation, Agent-Based Simulation
- Subject: -  Information systems  ->  Spatial-temporal systems.-  Computing methodologies  ->  Simulation support systems.Artificial intelligence.

## Extracted Abstract

LLM-based generative agents are increasingly used in urban simulators, yet it remains unclear whether they reproduce empirically realistic human mobility patterns or merely generate plausible mobility narratives. We introduce a validation framework for evaluating the mobility of generative agents of LLM-based urban simulators against real-world mobility data. For this, we use mobility laws, temporal rhythms, network motifs, semantic activity transitions, and behavioral mobility profiles. Using datasets from the Greater Paris region and Shanghai, we evaluate AgentSociety and CitySim across multiple dimensions of mobility realism. Our analysis reveals a substantial gap between narrative plausibility and empirical mobility realism. Although the simulators capture some high-level semantic activity distributions, they struggle to reproduce core spatial and temporal constraints, including realistic trip-length distributions, origin-destination flows, dwell times, and transition dynamics. We further observe that realistic mobility diversity is unstable across default prompting configurations and may require explicit profile-aware initialization. To support reproducible evaluation, we also contribute scalable and open LLM-driven infrastructure for regional-scale map generation, observability-enhanced simulation, mobility-metric computation, and traffic simulation. Our findings highlight the need for rigorous empirical validation of LLM-based urban simulators and provide practical tools for building more realistic and reproducible urban simulation systems.

## Outline

- Abstract (page 1)
- 1 Introduction (page 1)
- 2 The Human Mobility Landscape (page 2)
  - 2.1 Empirical Human Mobility Patterns (page 2)
  - 2.2 Behavioral and Semantic Mobility (page 2)
  - 2.3 LLM-Based Urban Simulators (page 2)
- 3 Mobility Realism Evaluation Framework (page 3)
  - 3.1 Mobility Traceability and Observability Enhancement (page 3)
  - 3.2 Analytical Framework (page 4)
- 4 Evaluation Setup (page 4)
  - 4.1 Datasets Description and Preprocessing (page 4)
  - 4.2 Simulation Setup (page 5)
  - 4.3 Population Sampling (page 5)
- 5 Mobility Realism Empirical Results (page 5)
  - 5.1 Spatial Mobility Realism (page 5)
  - 5.2 Temporal Mobility Dynamics (page 7)
  - 5.3 Mobility Motifs (page 7)
  - 5.4 Behavioral Mobility Profiles (page 8)
  - 5.5 Semantic Mobility Dynamics (page 8)
- 6 Toward High-Fidelity Urban Simulation (page 9)
  - 6.1 Improving Spatial and Semantic Realism (page 9)
  - 6.2 Advancing Behavioral and Social Dynamics (page 9)
  - 6.3 Computational Efficiency and Open Science (page 10)
- 7 Conclusion (page 10)
- Acknowledgments (page 10)
- References (page 11)
- A Map Generation Scalability Benchmark (page 13)
- B CitySim Reimplementation Choices (page 13)
  - B.1 Persona Module (page 13)
  - B.2 Memory Module (page 13)
  - B.3 Long-Term Goal Module (page 13)
  - B.4 Planning Module (page 13)
  - B.5 Destination Selection Module (page 13)
  - B.6 Multimodal and Social Modules (page 13)
- C Mobility Metrics and Laws (page 13)
- D Spatial Mobility-Law Population Comparisons (page 13)
- E Computational Costs (page 13)

## Markdown Content

When Plausible Is Not Realistic: Evaluating Human Mobility in
LLM-Based Urban Simulation
Gustavo H. Santos∗ Aline Carneiro Viana Thiago H. Silva
UTFPR, Brazil and Inria, France UTFPR, Brazil and
Inria, France U. of Toronto, Canada

Abstract
LLM-based generative agents are increasingly used in urban simulators, yet it remains unclear whether they reproduce empirically realistic human mobility patterns or merely generate plausible mobility
narratives. We introduce a validation framework for evaluating
the mobility of generative agents of LLM-based urban simulators
against real-world mobility data. For this, we use mobility laws, temporal rhythms, network motifs, semantic activity transitions, and
behavioral mobility profiles. Using datasets from the Greater Paris
region and Shanghai, we evaluate AgentSociety and CitySim across
multiple dimensions of mobility realism. Our analysis reveals a substantial gap between narrative plausibility and empirical mobility
realism. Although the simulators capture some high-level semantic activity distributions, they struggle to reproduce core spatial
and temporal constraints, including realistic trip-length distributions, origin-destination flows, dwell times, and transition dynamics. We further observe that realistic mobility diversity is unstable
across default prompting configurations and may require explicit
profile-aware initialization. To support reproducible evaluation, we
also contribute scalable and open LLM-driven infrastructure for
regional-scale map generation, observability-enhanced simulation,
mobility-metric computation, and traffic simulation. Our findings
highlight the need for rigorous empirical validation of LLM-based
urban simulators and provide practical tools for building more
realistic and reproducible urban simulation systems.
CCS Concepts
• Information systems → Spatial-temporal systems; • Computing methodologies → Simulation support systems; Artificial intelligence.
Keywords
Large Language Models, Generative Agents, Urban Simulation,
Human Mobility, Mobility Validation, Agent-Based Simulation
ACM Reference Format:
Gustavo H. Santos, Aline Carneiro Viana, and Thiago H. Silva. 2026. When
Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Simulation. In Proceedings of The 34th ACM SIGSPATIAL International
∗Corresponding author: gustavohenriquesantos@alunos.utfpr.edu.br

Conference on Advances in Geographic Information Systems (SIGSPATIAL’26).
ACM, New York, NY, USA, 14 pages. https://doi.org/XXXXXXX.XXXXXXX
1 Introduction
Large Language Models (LLMs) are increasingly used to simulate
urban behavior and human mobility [25, 36, 45]. Recent frameworks
such as AgentSociety [30] and CitySim [9] support generative agents
operating in simulated urban environments, enabling them to plan
routines, engage in social interactions, and adapt to contextual
information, as weather, work schedules, and personal needs. These
systems suggest a new paradigm for urban simulation, but raise
a central question: Do synthetic agents reproduce empirical human
mobility laws, or only generate trajectories that appear plausible?
This distinction is fundamental for simulation validity. Decades
of mobility research characterized the complexity of human behavior, the structured circadian routines, and the novelty-seeking behavior of individuals, identifying patterns such as truncated power
laws in travel distance [16], predictable visitation dynamics [35, 37],
recurrent topological mobility motifs [33], and heterogeneous yet
not-random mobility profiles [1, 5, 23]. Traditional mobility simulators are routinely validated against these empirical patterns before
being applied to policy analysis or forecasting [8, 12, 20, 31]. In
contrast, LLM-driven simulators are typically evaluated through
plausibility-oriented assessments, focusing on whether generated
schedules or behaviors appear coherent and believable [9, 30].
While such evaluations may capture temporal or narrative consistency, they do not establish realistic mobility behavior. Indeed,
plausibility-based mobility evaluations primarily capture a form of
“face validity” – i.e., whether generated behavior appears reasonable
or believable – rather than “objective mobility realism”: an agent’s
mobility may appear plausible (waking up at 7:00, going to work,
having lunch at noon, returning to home at 18:00 every week day),
while the underlying mobility process may still fail to reproduce empirical human mobility dynamics (e.g., exhibiting unrealistic travel
distances, random visitation frequencies, incorrect exploration dynamics, or the absence of spatial confinement effects). We define
mobility realism as the joint reproduction of spatial visitation dynamics and temporal activity organization according to empirical human
mobility regularities. However, evaluations of existing LLM-driven
simulators generally lack systematic validation of these coupled
spatio-temporal properties [15, 19, 24].
We introduce a comprehensive validation framework for LLMbased urban simulators grounded in real-world mobility data and
seminal literature on human mobility laws. To the best of our knowledge, this is the first systematic evaluation of LLM-based urban simulators against established empirical mobility laws and spatio-temporal
behavioral metrics of human mobility. Our findings highlight the
need for rigorous empirical validation as a standard practice alongside plausibility-oriented assessments. We release a set of artifacts

SIGSPATIAL’26, November 03–06, 2026, Riverside, CA, USA
providing a foundation for building more realistic and reproducible
urban simulation systems. Overall, we make three contributions:
Methodological: After a detailed literature review (cf. §2), we propose a modular framework for LLM-driven mobility realism evaluation (cf. §3) across five dimensions: spatial mobility laws, temporal
rhythms, topological motifs, behavioral profiles, and semantic/spatiotemporal activity patterns. Together, these components assess whethe
simulated trajectories reproduce empirical human mobility regularities across spatial and temporal dimensions.
Empirical: Using pseudoanonymized mobility datasets from Greater
Paris and Shanghai, we evaluate AgentSociety [30] and CitySim [9]
beyond narrative plausibility. For this, we introduce En-AgentSociety,
an enhanced version of AgentSociety with improved mobility traceability, observability, and scalability. Across metrics, we find a
consistent gap between plausible agent behavior and empirically
valid mobility (§5): Simulators reproduce some high-level semantic/activity distributions but fail to recover key spatial constraints,
displacement patterns, visitation structures, and transition dynamics. We show that behavioral diversity cannot be achieved through
generic persona prompting alone, but requires profile-aware initialization and stronger spatial constraints.
Artifact: Methodological and empirical contributions compose a released infrastructure for reproducible large-scale evaluation of LLMdriven mobility simulations1. The stack includes regional-scale map
generation, an observability-enhanced fork of AgentSociety, scalable
Rust+Python metric computation, and an open reimplementation of
the traffic simulator AgentSociety and CitySim depend on. Together,
they support standardized benchmarking of LLM-based mobility
simulators at regional scale.
We discuss paths toward higher-fidelity LLM-based urban simulation in §6 and conclude in §7.
2 The Human Mobility Landscape
Realistic city-scale mobility simulation supports data-driven urban services, but its reliability depends on accurately reproducing
human mobility patterns. This section reviews empirical mobility
regularities and limitations of recent LLM-based urban simulators.
2.1 Empirical Human Mobility Patterns
Human mobility exhibits strong statistical regularities across spatial and temporal scales. Using mobility traces from more than
100,000 mobile-phone users, González et al. [16] showed that human travel distance follows truncated power-law distributions and
that individual movements remain spatially bounded according
to a characteristic radius of gyration. Subsequent work by Song
et al. [35] demonstrated that human trajectories are highly predictable, estimating an upper-bound predictability of approximately
93% despite population-scale behavioral diversity.
Prior studies also revealed strong regularities in daily mobility
structure. Schneider et al. [33] showed that a small set of recurrent mobility motifs can represent up to 90% of weekday mobility
patterns, while the number of daily visits approximately follows
a log-normal distribution. More recently, Schläpfer et al. [32] explored the joint relationship between travel distance and visitation
1To be released. Anonymous for the revision phase

Santos et al.
frequency, showing that frequent short-range trips and infrequent
long-range trips emerge at different spatial scales [3], from neighborhoods to metropolitan regions, with important implications for
processes such as disease spreading [17].
Need: Human mobility is governed by robust empirical laws rather
than arbitrary movement behavior. Consequently, urban simulators
based on LLM-driven agents should be evaluated not only by the
plausibility of generated narratives, but also by their ability to
reproduce these established mobility patterns.
2.2 Behavioral and Semantic Mobility
Besides exhibiting strong regularities shaped by routine behaviors,
human mobility also includes periods of exploration that vary substantially across individuals. Prior work proposed metrics such as
entropy, regularity, stationarity, and diversity to characterize these
differences [38, 40]. Building on these measures, Amichi et al. [5]
identified three major mobility profiles: Scouters, who frequently explore new locations; Routiners, who primarily revisit familiar places;
and Regulars, who exhibit intermediate behavior. These behavioral
distinctions have important implications for mobility prediction
and simulation [4, 6, 13, 21, 22].
Need: Realistic simulators should capture both routine-like mobility
laws and heterogeneous exploration patterns across individuals.
Beyond behavioral diversity, realistic urban simulation must also
capture the semantic context underlying mobility decisions. While
Location-Based Social Network (LBSN) datasets present known demographic and platform biases [42], they provide valuable semantic
information such as POI categories and activity transitions that
are often absent from traditional mobility datasets. Recent mobility
datasets and LLM-based urban simulators increasingly incorporate this semantic dimension through activity types, transportation
modes, and spatio-temporal activity analysis [10, 43].
Need: The semantically rich trajectories generated by LLM-based
simulators require evaluation metrics that capture semantic and
spatio-temporal dynamics beyond spatial statistics.
2.3 LLM-Based Urban Simulators
Recent LLM-based urban simulators aim to reproduce human behavior through large-scale generative agents:
AgentSociety [30]: an open-source, OpenStreetMap-based framework combining LLM-driven decision-making and psychologically
inspired behavioral modules – including economic, cognitive, planning, mobility, and social components – for urban trajectory generation. After a detailed framework review and the enhancements we
brought to the AgentSociety simulator (cf. §3.1), we designed Fig. 1
to illustrate the simulation pipeline and module interactions. At
initialization (cf. Fig. 1), the EconomyBlock and NeedsBlock assign
demographic, financial, and behavioral attributes to each agent,
including occupation, income, consumption level, and dynamic
needs such as hunger, energy, safety, and social connection. Needs
evolve over time according to Maslow’s Hierarchy [27] and influence subsequent planning decisions. Daily behavior is generated
through the PlanBlock, which uses LLM calls guided by the Theory
of Planned Behavior [2]. Based on the agent’s current state (e.g.,
location, time, weather, emotions, occupation, and dominant need),

When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Sim
the simulator first selects a high-level behavioral strategy and then
generates a sequence of fine-grained actions associated with specific execution modules. The DispatcherBlock routes each action to
the corresponding simulator component.
The MobilityBlock governs movement decisions and destination
selection. For each movement step, the LLM selects a POI category,
subtype, and exploration radius conditioned on the agent’s current plan and contextual state. Candidate POIs are then sampled
using a Density-aware Gravity model based on Distance-decayed
Attraction: 𝑤 𝑖 = 𝜌 𝑑 𝑘 2 , where 𝜌 𝑘 represents the POI density within
𝑖
spatial ring 𝑘, and 𝑑 𝑖 is the distance to candidate POI 𝑖. Selection
probabilities are computed by normalizing these weights over the
candidate set. This mobility-selection mechanism is central to our
later analysis because many observed spatial mismatches originate
from failures in POI selection and movement generation.
At the end of each simulation step, the CognitionBlock updates
the agent’s internal state, including emotions, memories, and contextual reasoning, while the OtherBlock estimates durations for actions not directly handled by specialized modules. The SocialBlock
manages interactions between agents using a weighted social graph.
Because AgentSociety does not generate this graph automatically and
modeling realistic social ties introduces additional complexity, we
disable this component in our experiments and initialize agents with
empty social networks. Finally, agents maintain a temporal memory structure recording observations, locations, and prior actions,
allowing previous experiences to influence future decisions/plans.
CitySim [9]: an extended, closed-source version of AgentSociety
with richer cognitive, spatial, and social mechanisms aimed at improving behavioral realism. In addition to demographic attributes,
agents are initialized with personality traits, preferences, and longterm goals that evolve according to need fulfillment and life context. The framework also introduces a spatial-memory system that
stores subjective beliefs about previously visited POIs, influencing
future destination choices. Compared with AgentSociety, CitySim
employs more detailed planning and mobility-selection strategies.
Daily schedules are generated using fine-grained time blocking,
while destination selection combines distance-based attraction with
memory-aware preferences and contextual reasoning. The framework also incorporates transport-mode selection and dynamically
evolving social interactions through weighted social networks.
Need: AgentSociety and CitySim exhibit promising qualitative and
semantic behaviors, but their evaluation remains limited with respect to established empirical mobility laws and behavioral mobility
patterns. Existing assessments primarily focus on the plausibility and
coherence of generated activities rather than on whether simulated
trajectories reproduce real-world spatial, temporal, and topological
mobility dynamics [9, 30]. This gap motivates the need for systematic
mobility-grounded validation of LLM-based urban simulators.
3 Mobility Realism Evaluation Framework
Evaluating the realism of human mobility patterns in urban simulators requires (i) a broad set of metrics to quantitatively characterize
urban dynamics and (ii) complete traceability and interpretability of
generated mobility behaviors. However, current simulators lack the
capabilities necessary for rigorous mobility evaluation. This section
first presents the design enhancements introduced into the studied

on SIGSPATIAL’26, November 03–06, 2026, Riverside, CA, USA
simulators, followed by the analytical framework and metrics used
to evaluate mobility realism.
3.1 Mobility Traceability and Observability
Enhancement
AgentSociety [30] lacks several features essential for rigorous validation, particularly in the context of mobility modeling:
- Lack of Traceability: AgentSociety does not record visited POIs
or their categories, which obscures the underlying location-selection
mechanism and prevents verification of whether destination
choices are genuinely needs-driven or effectively random.
- Limited Transparency and Observability: AgentSociety does
not log block execution order or prompt-response pairs (lack of
traceability), limiting reproducibility and systematic analysis of
agent decision-making.
- Unconstrained POI selection: Although AgentSociety uses
LLM-driven planning to determine daily activities and select POI
categories, we observed that needs-driven mobility actions could
select destinations from the full set of POIs available in the simulated map, rather than from POIs semantically consistent with
the active need and spatially plausible given the agent’s current
context. As a result, agents with low hunger satisfaction could be
routed to semantically unrelated or distant POIs, producing unrealistic trip distances, dwell patterns, and activity transitions. This
behavior motivated our enhancements for recording selected
POIs, POI categories, and mobility-decision traces.
AgentSociety enhancement. To address these limitations, we developed En-AgentSociety, an enhanced version of AgentSociety that
improves mobility traceability, simulator observability, and scalability. Fig. 1 presents the main modules and the information flows
of En-AgentSociety for a simulated daily mobility routine. Several
lower-level components are consolidated into eight high-level modules shown on the right side of the figure. The central timestamped
workflow shows, at each 10-minute simulation step, the sequence
of modules involved in an agent’s decision-making, while the sequence of module calls illustrates the information exchanged during
the simulation process. The figure also summarizes the 49 agent
attributes used throughout the simulation, displayed at the top.
The workflow is annotated with timestamps that are color-coded
according to the agent’s location (e.g., home or work). It is worth
highlighting that the visualization of the timestamped workflow,
agent locations over time, and module interactions is enabled by
the traceability and observability enhancements described below.
- Traceability: refers to information collection and storage. The
enhanced framework logs complete mobility traces (visited locations and POIs), execution traces, and prompt–response pairs,
enabling systematic analysis of agent decisions and simulator
behavior. Logs are stored in a Dockerized ClickHouse database,
with an optional local DuckDB backend for lightweight execution.
Since prompt–response logs can be very large, detailed logging
can be disabled through the simulator configuration.
- Observability: refers to monitoring, statistics, latency analysis,
and performance diagnosis. Building on the collected logs, the
enhanced framework integrates an LGTM observability stack to

SIGSPATIAL’26, November 03–06, 2026, Riverside, CA, USA
monitor resource utilization, identify prompt-level latency bottlenecks, and provide aggregated execution statistics to support
optimization efforts (cf. §6).
- Scalability: AgentSociety depends on MOSSTool [47] to generate simulation maps from OpenStreetMap data. While suitable
for city-scale environments, the original implementation does
not scale efficiently to large regions due to costly spatial matching and redundant serialization. To address these limitations,
we implemented spatial indexing and batch-based processing,
enabling scalable regional map generation. We release this optimized implementation as a public artifact 2. Additional scalability
benchmarks are reported in the Appendix A.
Figure 1: Overview of the AgentSociety simulation pipeline
and LLM calls modules during a daily mobility routine.
Timestamped rows correspond to a 10-minute simulation
step: e.g, at 07:10, the diagram shows two DispatcherBlock
calls, one MobilityBlock call, and one CognitionBlock call.
These correspond to dispatching the agent’s plan to the appropriate module (i.e., commuting to work), executing the
mobility action, and updating the agent’s internal state.
CitySim implementation. Because CitySim [9] is a non-public
extension of AgentSociety (v1.5), we manually implemented its
documented functionalities based on the descriptions provided in
the associated publications. The resulting reconstruction was integrated into the same En-AgentSociety artifact, enabling a consistent
comparison between AgentSociety and CitySim under a common
simulation infrastructure. We do not provide a dedicated CitySim
illustration because its execution workflow follows the same overall structure as that shown in Fig. 1, albeit with additional agent
attributes and decision-making blocks. Notably, the unconstrained
POI selection mechanism inherited from AgentSociety was corrected, reducing trip-length discrepancies and improving behavioral consistency. Nevertheless, the resulting mobility patterns remain substantially different from the real-world mobility baseline,
likely due to the increased complexity of the simulator and its
decision-making process (cf. §5). Additional implementation details
for CitySim are provided in Appendix B.
3.2 Analytical Framework
For metrics with well-established parameterized formulations, we
retain their original definitions as proposed in the literature. The
complete mathematical expressions and computation procedures
are reported in Table 6 in Appendix C. For metrics whose parameter
2To be released. Anonymous for the revision phase

Santos et al.
choices require further justification or adaptation to the AgentSociety context, we provide a detailed discussion of the chosen parameter values and their rationale in the following.
• Travel distance (Δ𝑟) [16] follows the truncated power law 𝑃 (Δ𝑟) =
(Δ𝑟 + Δ𝑟 )−𝛽 exp(−Δ𝑟/𝜅), where Δ𝑟 is the distance between con0
secutive locations, 𝛽 is the scaling exponent, Δ𝑟 regularizes
0
short distances, and 𝜅 is the exponential cutoff representing the
characteristic travel limit of the population. In §5, we use the
classical reference values for travel distance: 𝛽 = 1.75, Δ𝑟 = 1.5
0
km, and 𝜅 = 400 km. To reduce GPS and discretization noise, we
filter movements shorter than 200 meters, matching the spatial
resolution of the processed Shanghai dataset. We do the same for
radius of gyration, which follows a similar power-law, using the
reference values from the same work.
• Distance-frequency law [32] is computed as 𝜌 𝑖 (𝑟, 𝑓 ) = (𝑟 𝜇 𝑓 𝑖 )𝜂 ,
where 𝑟 is the distance from the individual’s home, 𝑓 is the visitation frequency over the analysis period, 𝜇 𝑖 represents location
attractiveness, and 𝜂 ≈ 2 is the universal scaling exponent.
• Behavioral mobility profiling [5], locations in individual trajectories are first identified as exploration (𝑈 ) or return (𝑅) using the
visitation-frequency-based approach as in [4], where 𝑈 denotes
a visit to a previously unseen or rarely visited location and 𝑅
denotes a revisit to a known location. We compute two features
from these sequences: Intermittency, which captures how persistently users remain in the same behavioral state before switching
to another one (𝑈 → 𝑅 or 𝑅 → 𝑈 ), and Degree of Return, which
measures the overall tendency to revisit familiar locations (𝑅)
rather than continuously exploring new ones. After min-max
normalization, we use Gaussian Mixture Model (GMM) clustering with Silhouette-score optimization to assign users to Scouters,
Routiners, and Regulars profiles.
4 Evaluation Setup
The comparison and validation of simulators’ realism across both
semantic and topological metrics requires high-quality human mobility datasets. Next, we describe the considered datasets, their
processing and sampling procedures applied prior to analysis, as
well as the simulator setup used in the realism investigation.
4.1 Datasets Description and Preprocessing
We use two spatiotemporal mobility datasets that differ in scale,
spatial resolution, and semantic richness.
GreaterParis dataset [10]: A non-public GNSS-based anonymized
dataset offering a multi-dimensional view of the mobility behavior
of 3,337 residents in the Île-de-France region, France, over a continuous 7-day period (collected between October 2022 and May 2023).
Volunteers were equipped with the BT-Q1000XT Bluetooth® A-GPS
eXtreme Travel Recorder, a GNSS receiver that determines position and velocity using signals from satellite systems. The dataset
combines GPS trajectories with validated travel diaries, comprising
more than 80,000 trips annotated with visit purposes (e.g., home,
work, leisure) and transportation modes (e.g., walk, car, rail). The
dataset further includes calibrated population weights designed
to correct for sociodemographic and temporal biases, which are
incorporated where appropriate in our analyses. All participants

When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Sim
provided informed consent for the data collection, which was conducted in accordance with data protection regulations. The start
and end locations of each trip are spatially anonymized using the
centroid of the corresponding H3 cell (level 10). Since GPS observations are recorded only during movement (i.e., points outside
validated trips were removed from the dataset), we infer stationary
periods from the trajectory structure and visit annotations.
- Preprocessing: To reduce noise and spatial fragmentation, we
define each visit location as the modal coordinate within a ±10minute window. Since home/work labels are provided, we consolidate neighboring same-purpose H3 cells within a 2-ring neighborhood to the most frequent centroid. These anonymized centroids
are representative spatial anchors, not exact locations. This aggregation increased primary-home coverage from 43.3% to 75.5%.
Shanghai [13]: Cellular Data Record (CDR) dataset collected by
a major telecom operator in metropolitan Shanghai, China. The
dataset contains hourly mobility records for 58,502 anonymized
users over ten consecutive days, totaling more than 9 million observations across 10,396 spatial cells. Unlike CDRs, user locations in
this dataset correspond to the centroid of the spatial grid cell nearest
to the dominant connected base station during each hour, providing
a more stable spatial representation of user mobility. Compared
with the GreaterParis dataset, the Shanghai dataset offers substantially larger population coverage but lacks semantic annotations
such as activity purposes and transportation modes.
- Preprocessing: We use a pre-processed version of the Shanghai
dataset introduced in prior work [13], which addressed common
sparsity issues in CDR-like mobility data through temporal completion and spatial normalization [11]. Missing records during
stable inactivity periods were imputed using dominant home
and workplace proxy locations inferred from recurring temporal
patterns. Locations were subsequently mapped to a 200m × 200m
OpenStreetMap grid using Scikit-Mobility [29], replacing raw coordinates with spatial-cell centroids. To reduce redundancy and
remove inactive users, only one observation per user per location
was retained within each hourly interval, and users with fewer
than 10 active days or 120 total observations were excluded.
4.2 Simulation Setup
To manage computational constraints while preserving representative urban coverage, we define bounded regions for each dataset.
For the GreaterParis dataset, instead of simulating the full Île-deFrance region, we restrict the environment to a smaller bounding
box3 covering 61.7% of the total regional area while encompassing
89.3% of active urban zones according to Copernicus Land Usage
data [14]. For Shanghai, we use a bounding box4 covering all available mobility records. Figure 2 illustrates both simulation regions.
To match the temporal scope of the empirical datasets, simulations are executed for 7 days in the GreaterParis dataset and 10 days
in Shanghai using a 10-minute simulation step. We use the default
AgentSociety parameter configuration, including the recommended
LLM, Qwen-2.5-32B-Instruct model. Results correspond to three
independent runs for both AgentSociety and CitySim.
3Île-de-France BBOX: (1.6, 48.5, 2.975, 49.16)
4Shanghai BBOX: (120.88, 30.63, 122.06, 31.84)

on SIGSPATIAL’26, November 03–06, 2026, Riverside, CA, USA
Urban IDF Boundary
Rural Simulation Map
(a) Île-de-France (b) Shanghai
Figure 2: Simulated bounded regions used in the experiments.
4.3 Population Sampling
Due to the computational cost of LLM-based mobility generation,
we downsample both datasets to approximately 500 representative
users. This subset size enables the generation of a matching population size of simulated agents and facilitates a direct comparison
between real-world and simulated mobility patterns.
In GreaterParis, Sample’s candidate users were restricted to
individuals: (i) whose trips remained within the simulation boundaries (cf. §4.2); (ii) with complete 7-day records, including days
with no recorded trips, which we treat as non-travel days; and (iii)
with stable home and work anchors, defined as representative H3
level-10 cells visited at least five times for home and three times for
work. Because this resulted in a subset of 504 users (15% Scouters,
48% Regulars, and 37% Routiners), we retained all of them without
additional stratified sampling of profiles. For comparison, the profile
distribution in the full dataset is 27% Scouters, 37% Regulars, and 36%
Routiners. From this sample, we extract demographic attributes and
representative home/work spatial anchors to initialize simulated
agents.
In Shanghai, two independent 500-user samples were generated:
Sample 1: We select 500 users with stable spatial anchors, defined
as users whose inferred work location remains unchanged across
morning and afternoon periods. This restriction is required because
both simulators support a single work location per agent. To preserve population-level behavioral diversity, sampling is stratified
to maintain the mobility-profile distribution observed in the full
dataset (17% Scouters, 56% Regulars, and 27% Routiners).
Reference sample: We draw a second disjoint 500-user sample
using the same eligibility criteria to estimate sample-to-sample
variability. This sample is not used to initialize agents, but serves as
a real-data benchmark for interpreting simulator discrepancies in §5.
An analogous GreaterParis reference sample cannot be constructed
because too few eligible users remain after filtering.
5 Mobility Realism Empirical Results
This section reports the comparison results between simulated and
real-world mobility datasets.
5.1 Spatial Mobility Realism
LLM-based agents capture the main qualitative mobility-law patterns observed in the literature and empirical datasets, but fail to
accurately capture individual-level spatial mobility behavior.

SIGSPATIAL’26, November 03–06, 2026, Riverside, CA, USA
Fig. 3 compares the empirical mobility-law distributions observed in the real sampled datasets (denoted as GParis/Shanghai
Sample) with those generated by AgentSociety and CitySim (denoted as AG/CT GParis or AG/CT Shanghai). The corresponding
theoretical reference distributions reported in the literature are
shown as dotted lines and labeled “ref” in the figure.
Overall, both simulators capture the main qualitative mobilitylaw patterns observed in literature and sampled datasets; the generated trajectories exhibit: (i) travel-distance distributions consistent
with a truncated power law, characterized by a predominance of
short trips and progressively fewer long-distance movements [16];
(ii) radius-of-gyration distributions indicating spatially bounded
daily mobility, with most individuals exhibiting confined mobility
within a few kilometers of their primary activity locations [16];
(iii) a distance–frequency scaling relationship in which visitation
frequency decreases with distance from home, reflecting mobility
patterns dominated by frequent short-range visits and occasional
long-range trips [32]; and (iv) a daily number of visited locations
that approximately follows a log-normal distribution [33].
100
10 1
10 2
10 3
10 4
10 5
10 1 6 0 2 10 1 100 101 102 103
r (km)
)r (P
100
10 1
10 2
10 3
10 4
10 5
10 1 6 0 2 10 1 100 101 102 103
rg (km)
(a) Travel Distance (Δ𝑟)
)r(P g
(b) Radius of gyration (𝑟 𝑔)
101
100
10 1
10 2
10 3
10 4
100 101 102
r f (km)
)2mk
srotisiv(
)f,r(
i
100
10 2
10 4
10 6
10 8
10 10
10 12 1 2 3 5 10 15
Number of Visited Locations (N)
(c) Distance-Frequency Law
)N(f
noitubirtsiD
(d) Daily Visits Law
Figure 3: Comparison of empirical mobility-law distributions
between real and simulated trajectories across GreaterParis
and Shanghai. AG refers to AgentSociety and CT to CitySim.
Table 1: Comparison of real vs simulated distribution of spatial mobility metrics.
Dataset Source Δ𝑟 (𝑊 1) 𝑟𝑔 (𝑊 1)
GreaterParis AgentSociety 14.83 ± 0.35 7.29 ± 0.28
GreaterParis CitySim 7.53 ± 1.67 3.47 ± 0.23
Shanghai AgentSociety 8.73 ± 0.48 4.30 ± 0.67
Shanghai CitySim 3.97 ± 0.11 4.86 ± 0.09
Shanghai Reference sample 0.48 1.01
Tables 1 and 2 summarize the spatial realism results across
datasets and simulators. Table 1 compares the travel-distance (Δ𝑟)
and radius of gyration (𝑟 𝑔) distributions of the real and simulated
datasets using the Wasserstein distance (𝑊 ), where lower values
1

Santos et al.
indicate greater similarity between real and simulated mobility
patterns. Additionally, Table 2 (i) reports 𝑊 values comparing sim1
ulated against empirical mobility patterns using Spatio-Temporal
Visit Distribution (STVD) at different spatial resolutions and (ii) evaluates the similarity between real and simulated OD matrices using
the Common Part of Commuters (CPC) metric. Higher CPC values
indicate greater similarity between mobility flows. Results obtained
using the complete dataset populations are reported in Appendix
D. Relative to the Shanghai reference sample, simulator errors are
much larger, indicating deviations beyond sampling variability.
As shown, datasets generated by AgentSociety exhibit substantial spatial discrepancies in both GreaterParis dataset and Shanghai
scenarios. These discrepancies are reflected in the Δ𝑟 and 𝑟 𝑔 distributions, which consistently yield larger 𝑊 than those obtained
1
with CitySim. Similar discrepancies are observed for the STVD metric in both simulators, indicating partial reproduction of visit spatial
distributions. At the flow level, OD-matrix similarity remains weak
across all scenarios, as reflected by the low CPC values, suggesting that neither AgentSociety nor CitySim fully captures realistic
large-scale mobility flows between locations. These results suggest
that the generated trajectories capture some high-level behavioral
structure while failing to reproduce these dynamics.
Spatial realism limitations are more pronounced in AgentSociety outputs. Analysis of the generation pipeline suggests that mismatches
are partially associated with instability in POI selection and destination reasoning, leading to trajectories influenced by local mapdensity artifacts rather than coherent large-scale mobility patterns.
CitySim partially mitigates these spatial inconsistencies. In the
GreaterParis dataset, Δ𝑟 error decreases from 14.83 km (in AgentSociety case) to 7.53 km, while radius of gyration error decreases from
7.29 km to 3.47 km. In Shanghai, CitySim further reduces Δ𝑟 error
to 3.97 km and radius of gyration error to 4.86 km. Nevertheless, ODmatrix agreement remains weak, particularly in the GreaterParis
dataset (CPC H8 = 0.138 ± 0.018).
While CitySim improves destination and spatial selection relative
to AgentSociety, these enhancements alone do not yield realistic
large-scale mobility patterns.
To further examine the spatiotemporal fidelity results reported
in Table 2, we analyze the STVD in greater detail. Figure 4 presents
hexagonal bivariate maps that jointly visualize visit-volume differences and temporal displacement of peak activity (Peak Shift)
between simulated and empirical mobility patterns. For clarity, we
show only the AgentSociety simulations, as AgentSociety achieves
lower STVD 𝑊 values than CitySim, despite CitySim’s better agree1
ment for individual-level Δ𝑟 and 𝑟 𝑔 distributions. At H3 resolution 8,
the GreaterParis dataset STVD 𝑊 equals 607.69 ± 5.88 for AgentSo1
ciety and 748.71 ± 23.00 forCitySim. For the same resolution, the
Shanghai STVD 𝑊 is also lower for AgentSociety. Results suggest
1
that the simpler gravity-based destination selection used in AgentSociety outperforms CitySim’s LLM-driven POI-selection strategy in
reproducing the most frequently visited urban areas.
Increasing POI-selection complexity does not necessarily improve
the reproduction of highly visited urban areas.
In GreaterParis dataset (Fig. 4a), the simulation captures the
broad spatial distribution of user activity but exhibits noticeable

When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Sim
(a) GreaterParis (b) Shanghai
Figure 4: Spatio-Temporal Visit Distribution (STVD) comparing real and simulated mobility patterns.
temporal discrepancies. Agents tend to visit the correct regions,
yet peak activity is often shifted by 3 to 12 hours, suggesting that
the model predicts where urban activity occurs more accurately
than when it occurs. Aggregate visit volumes are also slightly underestimated in central Paris. In contrast, Shanghai (Fig. 4b) exhibits stronger spatiotemporal divergence in the urban core, characterized by dense clusters of visit-volume and temporal errors
(red hexagons). This divergence may stem from dataset-specific
limitations, such as sparse contextual information or challenges
in extracting POI metadata, though peripheral areas align more
closely with the empirical baseline. Recall that STVD similarity
is measured using an approximate Wasserstein distance in which
a temporal difference of 10 minutes incurs the same penalty as a
spatial displacement of 100 m (cf. Table 2).
Table 2: Spatio-Temporal realism metrics comparing datasets’
STVD and OD matrix across resolutions.
Dataset Source Resolution STVD (𝑊 1) OD Matrix (CPC)
H7 505.83 ± 7.20 0.206 ± 0.004
AgentSociety H8 607.69 ± 5.88 0.088 ± 0.002
H9 694.77 ± 2.66 0.027 ± 0.001
GreaterParis
H7 628.60 ± 6.07 0.270 ± 0.026
CitySim H8 748.71 ± 23.00 0.138 ± 0.018
H9 844.26 ± 22.18 0.038 ± 0.006
H7 111.16 ± 42.77 0.135 ± 0.019
AgentSociety H8 113.88 ± 39.04 0.046 ± 0.008
H9 145.02 ± 60.10 0.010 ± 0.003
Shanghai CitySim H H 7 8 4 4 2 3 2 2 . . 1 5 1 5 ± ± 1 1 7 7 . . 3 1 2 1 0 0 . . 0 0 5 4 4 2 ± ± 0 0 . . 0 0 1 1 3 3
H9 449.21 ± 31.84 0.011 ± 0.005
H7 21.11 0.297
Reference sample H8 6.29 0.092
H9 35.02 0.045
5.2 Temporal Mobility Dynamics
Spatial deviations propagate into unrealistic temporal dynamics.
Fig. 5 compares the temporal distributions observed in the empirical datasets with those generated by AgentSociety and CitySim,
while Table 3 summarizes the main temporal realism metrics across
datasets and simulators. Since destination selection and travel distances jointly influence travel and waiting times, deviations in
spatial behavior are expected to impact daily temporal rhythms.
AgentSociety exhibits substantial discrepancies in trip duration,
dwell time, and visitation frequency across both datasets. In the

on SIGSPATIAL’26, November 03–06, 2026, Riverside, CA, USA
Table 3: Temporal mobility realism metrics comparing real
and simulated trajectories.
Dataset Source TD. (min) (𝑊 1) DT. (h) (𝑊 1) Vf. (𝑊 1)
GreaterParis AgentSociety 24.41 ± 0.24 3.96 ± 0.12 9.63 ± 0.19
GreaterParis CitySim 24.32 ± 18.93 30.24 ± 29.63 19.46 ± 3.62
Shanghai AgentSociety 9.30 ± 0.24 4.79 ± 0.37 12.31 ± 4.19
Shanghai CitySim 19.30 ± 0.27 36.39 ± 4.91 24.95 ± 0.65
Shanghai Ref. sample 0.29 0.26 2.07
GreaterParis dataset, trip duration error reaches 𝑊 = 24.41 ± 0.24
1
minutes, while dwell time shows a large mismatch (𝑊 = 3.96 ± 0.12
1
hours). Similar patterns appear in Shanghai with lower absolute
errors, likely due to the dataset’s coarser temporal resolution. Regarding visitation frequency, which empirically follows a log-normal
distribution, AgentSociety captures the overall shape of the distribution but consistently underestimates daily visits. Over the multi-day
simulation, this daily underestimation accumulates, leading to a
substantial deficit in total visits across both scenarios.
1.0
0.8
0.6
0.4
0.2
0.00 50 100
Trip Duration (minutes)
FDC
1.0
0.8
0.6
0.4
0.2
0.00 10 20
Dwell Time (hours)
(a) Trip Duration
FDC
1.0
0.8
0.6
0.4
0.2
0.00 20 40 60
# Visits per User
(b) Dwell Time
FDC
(c) Visit Frequency
Figure 5: Comparison of temporal distributions between real
and simulated trajectories across GreaterParis and Shanghai.
Although CitySim improves spatial realism metrics such as Δ𝑟
and 𝑟 𝑔 (cf. § 5.1), Table 3 shows that these gains are accompanied by
a degradation in temporal realism. The inclusion of goals/hobbies
(e.g., looking for bird spotting POI categories instead of parks)
and more complex LLM prompts for POI selection leads to longer
decision times and increased residence time at home locations,
reducing overall mobility activity.
Mobility realism requires jointly reproducing spatial visitation patterns and temporal activity schedules; improving spatial realism
alone may degrade temporal consistency.
Compared with the Shanghai reference sample, whose temporal
discrepancies are small (𝑊 = 0.29 minutes for trip duration, 𝑊 =
1 1
0.26 hours for dwell time, and 𝑊 = 2.07 for visitation frequency),
1
both simulators exhibit substantially larger errors.
Temporal discrepancies reflect systematic biases in the simulated
mobility dynamics rather than finite-sample variability.
5.3 Mobility Motifs
Simulated trajectories reproduce dominant routine motifs but fail to
capture the full diversity of empirical daily mobility structures.
Fig. 6 shows the 16 most frequent mobility motifs [33] as well as
their distributions observed in all datasets, allowing comparison
between empirical and simulated outputs. Motif label −1 denotes

SIGSPATIAL’26, November 03–06, 2026, Riverside, CA, USA
60
40
20
0
)%(
egatnecreP
AgentSociety CitySim GParis
60
40
20
0
-1
(a) GreaterParis Motifs
)%(
egatnecreP
AgentSociety CitySim Shanghai
-1
(b) Shanghai Motifs
Figure 6: Comparison of the most frequent daily mobility
motifs observed in real and simulated trajectories.
motifs with more than six nodes, while the unlabeled bar aggregates motifs outside the top 16 motifs observed in the GreaterParis
and Shanghai datasets. Table 4 reports the JSD between real and
simulated motif distributions. The columns indicate the reference
distribution against which each Source is compared: the corresponding 500-user empirical sample (Sample), the full empirical dataset
(Population), or the canonical motif distribution reported in [33]
(Literature). The rows quantify how far the main 500-user empirical
sample deviates from the full population and literature references,
while the Shanghai reference-sample row quantifies the variability
between two disjoint empirical Shanghai samples of the same size.
Table 4: JSD for mobility motif distributions. Sample, Population, and Literature denote the reference distribution used
in Source comparisons.
Dataset Source Sample Population Literature
GreaterParis AgentSociety 0.1186 ± 0.0026 0.1290 ± 0.0013 0.0463 ± 0.0030
GreaterParis CitySim 0.3272 ± 0.0975 0.2845 ± 0.1193 0.2034 ± 0.0789
Shanghai AgentSociety 0.0612 ± 0.0027 0.1084 ± 0.0109 0.0406 ± 0.0036
Shanghai CitySim 0.3298 ± 0.0206 0.4489 ± 0.0199 0.3447 ± 0.0109
GreaterParis Empirical sample n/a 0.006 0.05
Shanghai Empirical sample n/a 0.05 0.04
Shanghai Reference sample 0.0045 0.0620 0.04
Across both datasets, the simulations are strongly dominated
by simple two-node motifs, indicating that agents frequently alternate between a small number of anchors, such as home and work.
While this captures part of the repetitive structure observed in real
mobility, many empirical daily routines remain unmatched.
In the GreaterParis dataset, mismatch is partly associated with
open-ended daily trajectories in which individuals start and end
the day in different locations, producing unclosed motif loops. In
Shanghai, mismatch is more strongly driven by the higher spatial
granularity and density of recorded locations, which frequently
generate complex motifs exceeding six nodes and therefore fall
outside the evaluated motif space. Finally, the Shanghai referencesample JSD is much smaller than the simulators’ JSDs in the Sample
column, indicating that motif mismatches are substantially larger
than what would be expected from sampling variability alone.
Predictability gives the same pattern a useful second angle. In
GreaterParis, empirical trajectories have mean predictability 0.472,
while AgentSociety and CitySim increase this value to 0.539 ± 0.007
and 0.598±0.114, respectively, consistent with an overproduction of
simple routine structures. In Shanghai, the empirical value is higher
(0.666); AgentSociety underestimates it (0.501 ± 0.014), whereas
CitySim is closer but slightly higher (0.689 ± 0.005).

Santos et al.
Similar motif-level errors can arise from different degrees of regularity in the generated trajectories.
Despite these limitations, the middle of the ranked motif distribution exhibits partially similar variability between empirical and
simulated trajectories, suggesting that LLM-based agents capture
some coarse routine regularities while failing to reproduce the full
topological diversity of real-world mobility behavior.
GP S (15/48/37) AG GP #1 (36/40/24) AG GP #2 (43/54/3) AG GP #3 (45/51/4)
GP P (27/37/36) CT GP #1 (38/52/10) CT GP #2 (23/67/10) CT GP #3 (23/67/10)
SH S (17/56/27) AG SH #1 (37/60/3) AG SH #2 (40/55/5) AG SH #3 (41/54/5)
SH P (17/56/27) CT SH #1 (9/59/32) CT SH #2 (13/60/27) CT SH #3 (6/56/38)
Regularity Diversity
1.00 1.00
0.75 0.75
0.50 0.50
0.25 0.25
0.00 0.00
Stationarity Entropy
1.00 1.00
0.75 0.75
0.50 0.50
0.25 0.25
0.00 0.00
Scouter Regular Routiner Scouter Regular Routiner
Figure 7: Behavioral mobility metrics and profile distributions across empirical and simulated trajectories.
5.4 Behavioral Mobility Profiles
Simulated trajectories partially reproduce the expected behavioral
mobility profile structure with routine and exploration dynamics.
Fig. 7 summarizes the behavioral mobility metrics –regularity,
diversity, stationarity, and entropy – associated with the profile distributions in parentheses in the legend (Scouters/Regulars/Routiners)
across empirical and simulated datasets. S, P, GP, and SH refer to
Sample, Population, GreaterParis, and Shanghai, respectively.
Overall, the simulated profiles broadly align with mobility-profiling
literature: Routiners exhibit higher regularity and stationarity with
lower diversity and entropy, while Scouters exhibit the opposite
behavior. This suggests that LLM-based agents capture part of
the exploration-return dynamics underlying human mobility. The
GreaterParis dataset profile-distribution JSD remains relatively
low for AgentSociety (0.13 ± 0.08), while CitySim is slightly lower
(0.09 ± 0.01).
Some Shanghai simulation runs exhibit extreme outliers with
unusually high diversity and entropy. These anomalies appear consistent with instability in POI-selection behavior, where agents
repeatedly search for unavailable or overly specific destination
types, producing erratic movement patterns that artificially increase exploratory behavior and shift agents toward the Scouter
profile. Across most runs, a small fraction of agents are classified as
Routiners despite remaining at home for nearly the entire simulation, exhibiting maximum stationarity and near-zero regularity, i.e.,
a degenerate routine pattern rather than realistic routine behavior.
5.5 Semantic Mobility Dynamics
LLM-based agents reproduce first-order semantic activity distributions more reliably than temporal and sequential semantic dynamics.

When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Sim
Table 5: Semantic mobility realism metrics comparing empirical and simulated trajectories.
Dataset Source VPD (JSD) ATM (JSD) DARD (JSD)
GreaterParis AgentSociety 0.0296 ± 0.0010 0.1125 ± 0.0029 0.0110 ± 0.0004
GreaterParis CitySim 0.0883 ± 0.0255 0.2405 ± 0.0559 0.1573 ± 0.2156
Fig. 8 summarizes semantic activity behavior in the GreaterParis
dataset through aggregate visit-purpose distributions and differences in activity-transition probabilities, while Table 5 reports the
corresponding JSD metrics. We report semantic metrics only for the
GreaterParis dataset, since the Shanghai dataset does not include
activity-purpose annotations.
HEALTH
STUDIES GParis HOME
HEALTH AG GParis LEISURE CT GParis
LEISURE OTHER
PURCHASE PURCHASE
OTHER STUDIES
WORK
WORK
HOME
0 % 2 o 0 f Visits 40 HEALTH HOM L E EISURE T OT O P H U E A R R C c H t A iv S S E i T t U y DIES WORK
(a) Visit Purpose Distribution
ytivitcA
MORF
10.0 -0.00 0.27 -0.15 -0.13 0.21 -0.03 -0.07
7.5
0.47 3.31 1.92 2.06 5.90 -0.31-11.55 5.0
-0.19 0.70 -0.68 -1.98 0.34 -0.24 -1.63 2.5
-0.17 -0.73 -1.92 -2.25 0.65 -0.30 0.07 0.0
0.07 7.67 0.36 0.46 1.28 -0.02 1.71 2.5
-0.01 -0.63 -0.17 -0.29 -0.02 -0.03 -0.22 5.0
7.5
-0.16 -5.02 -3.19 -3.13 2.96 -0.49 5.30
10.0
)stniop
%(
noitalumiS
naeM
- siraPG
(b) Activity Transition Matrix
Figure 8: Semantic mobility patterns for the GreaterParis.
For the GreaterParis dataset, AgentSociety produces semantic
activity proportions broadly matching the empirical data, despite
generating fewer visits overall. This is reflected in its low VPD divergence (0.0296 ± 0.0010). The main discrepancy occurs in purchaserelated activities, which are underrepresented in the simulation.
This mismatch may reflect limitations in POI classification, POI
availability, or destination-selection behavior within the simulation.
Compared to CitySim, AgentSociety more closely matches empirical semantic behavior across all three metrics. Although CitySim
introduces more complex destination-selection mechanisms, these
additional constraints may reduce robustness when compatible
POIs are sparse or unavailable, reducing semantic activity accuracy.
HEALTH
20
HOME
LEISURE 10
OTHER 0
PURCHASE 10
STUDIES 20
WORK
00:00 01:00 02:00 03:00 04:00 05:00 06:00 07:00 08:00 09:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00 18:00 19:00 20:00 21:00 22:00 23:00
Time of Day
GParis
- Mean
Simulation
(%
points)
Figure 9: Daily Activity Routine Distribution (DARD) differences for the GreaterParis dataset.
Fig. 9 further shows that simulated agents partially reproduce
coarse daily activity rhythms throughout the day, although some
activity purposes remain over- or under-represented at specific
time intervals. However, the larger ATM divergence indicates that
realistic aggregate activity proportions do not necessarily translate
into realistic activity sequences.

on SIGSPATIAL’26, November 03–06, 2026, Riverside, CA, USA
Generating plausible individual activities is easier than reproducing the ordered transitions through which these activities occur in
empirical mobility.
6 Toward High-Fidelity Urban Simulation
This section discusses potential directions for improving the mobility realism limitations identified in LLM-based urban simulators.
6.1 Improving Spatial and Semantic Realism
Improving POI Representation. Our analysis suggests that part
of the observed spatial and semantic mismatch originates from
limitations in the underlying POI representation. In Greater Paris
area, 57.45% of the 223,149 OpenStreetMap (OSM) POIs correspond
to benches, bicycle parking, waste baskets, recycling points, or
post boxes, leaving fewer than 100,000 semantically meaningful
destinations for agent decision-making.
To evaluate if richer POI coverage improves simulation realism,
we augmented the map with 178,884 deduplicated Overture Maps
POIs [28]. We then compared semantic POI density at H3 resolution
8 against the official French facility inventory, Base Permanente des
Équipements (BPE) [18]. The Pearson correlation increased from
0.55±0.23 using OSM data alone to 0.80±0.20 using OSM+Overture.
Results suggest that improving semantic map coverage may substantially improve destination selection and activity realism in LLMbased urban simulators.
Transport Mode and Routing Realism. Transport behavior also
plays a central role in mobility realism. In the original AgentSociety mobility layer, car-based routing relies on simplified traveltime assumptions, including a fixed-duration fallback, rather than
context-sensitive travel times. This simplification directly affects Δ𝑟
distributions, dwell time, visitation frequency, and temporal activity
rhythms.
Although CitySim introduces transport-mode selection mechanisms [9], reproducing its full routing behavior remains difficult
because AgentSociety depends on a partially closed-source binary
traffic layer [46]. We provide an open reimplementation of this
traffic layer for car-based trips for comparability; routing for other
transport modes remains future work.
Future urban simulators should integrate fully open and multimodal
routing engines capable of modeling realistic travel times across
walking, rail, cycling, and vehicular transportation systems.
6.2 Advancing Behavioral and Social Dynamics
Explicit Mobility Profiling. Our results suggest that realistic behavioral diversity does not reliably emerge solely from generic
prompting. Incorporating behavioral constraints may improve individual mobility realism and aggregate population structure.
Future simulation frameworks should incorporate explicit mobilitybehavior mechanisms capable of modeling heterogeneous exploration and return dynamics across individuals. Rather than assuming patterns naturally emerge from high-level personas or preferences, simulators could directly condition agent behavior on mobility
characteristics such as exploration persistence, routine stability, preferred motif complexity, or the tendency to revisit familiar locations.

SIGSPATIAL’26, November 03–06, 2026, Riverside, CA, USA
Social Network Effects. Social interactions also influence mobility
behavior through group activities, co-location patterns, and new
places’ discovery. However, the initialization and evolution of social
relationships remain poorly documented in current LLM-based
urban simulators such as AgentSociety [30] and CitySim [9]. Because
our evaluation focused primarily on mobility realism, we did not
systematically analyze the impact of social-network structure.
Future work should investigate how different social-network initialization strategies influence exploration behavior, routine formation,
and collective mobility dynamics.
6.3 Computational Efficiency and Open Science
Computational Cost and Scalability. Large-scale LLM-based urban simulation remains computationally expensive. Consequently,
several mobility laws and population-level dynamics could not be
evaluated at their full scale, as our experiments were restricted to
populations of approximately 500 agents. Table 8 in Appendix E,
shows that simulating 7–10 days of activity for 500 agents with
GPT-4o-mini, i.e., the same model used in CitySim [9], would cost
roughly $130–200. These simulations consume 700–900 million input tokens and 65–110 million output tokens, resulting in execution
times of several days even at this limited scale.
Future systems will likely require hierarchical or hybrid architectures
that combine LLM reasoning with lightweight specialized models.
Routine tasks such as dispatcher classification, regression updates
in NeedsBlock, or repetitive behavioral decisions could perhaps be
handled by fine-tuned compact models or other more efficient alternatives, reserving larger LLM calls for planning, reasoning, and
complex social interactions.
Observability and Reproducibility. Transparent and reproducible
infrastructure is essential for evaluating LLM-based urban simulators. Closed-source systems, as CitySim, limit external validation
and debugging, while open platforms, as AgentSociety, enable inspection of cognitive and mobility-generation mechanisms. Nevertheless, effective observability requires more than source-code access
alone; the original AgentSociety implementation provided only limited visibility into the internal state and decisions driving agent
behavior, motivating enhancements introduced in this work.
For reproducibility and debugging, we release an anonymized fork of
AgentSociety with built-in observability and support for switching
between AgentSociety and CitySim configurations.
The framework5 records visited POIs, semantic categories, prompt
and responses, memories, emotions, attitudes, thoughts, block execution times, LLM latency, token consumption, and call frequencies.
Beyond enabling detailed cost and behavior analysis, this state tracking also improves fault tolerance by supporting checkpoint-based
recovery, allowing long-running simulations to resume from the last
saved state after failures, rather than restarting from the beginning.
Open Mobility Evaluation Infrastructure. We additionally release four complementary anonymized artifacts. First, a scalable
regional map generation tool. Second, we release En-AgentSociety6,
5To be released
6To be released

Santos et al.
an extended and fully reproducible version of AgentSociety that
integrates our reimplementation of both AgentSociety and CitySim
within a unified simulation artifact. En-AgentSociety also reimplements modules supporting future studies of multimodal mobility
and social interactions (see Appendix B.6). Third, a Rust+Python
evaluation framework7 computes all mobility and semantic metrics
used in this work, including spatial, temporal, network, behavioralprofile, and POI-transition measures. Fourth, an open reimplementation of the traffic simulator AgentSociety and CitySim uses. This
framework facilitates debugging of routing and mobility behavior while establishing a public foundation for future multimodal
transportation support.
7 Conclusion
This work introduced an empirical mobility realism evaluation
framework for LLM-driven urban simulators grounded in realworld mobility data. Using datasets from Greater Paris area and
Shanghai, we evaluated AgentSociety and CitySim across multiple
dimensions of mobility realism, including spatial mobility laws,
temporal dynamics, topological motifs, semantic activity behavior,
and behavioral mobility profiles.
Our results show that current LLM-based simulators can reproduce portions of routine human behavior, particularly coarse
semantic activity distributions and simple repetitive mobility structures. However, substantial discrepancies remain in large-scale
spatial flows, temporal rhythms, sequential activity transitions,
and heterogeneous exploration behavior. These findings suggest
that generating plausible individual trajectories is fundamentally
different from reproducing empirically grounded urban mobility
dynamics, highlighting the need for more observable, scalable, and
behaviorally grounded urban simulation systems.
This study has two main limitations. First, because CitySim is
not publicly available, our evaluation relies on a reimplementation
based on the functionalities described in the original paper; implementation differences may therefore affect the observed results.
Second, semantic mobility evaluation is restricted to the GreaterParis dataset, since the Shanghai dataset does not include activitypurpose annotations. Future work should evaluate additional public
simulators, richer semantic mobility datasets, and stronger spatial
constraints for LLM-based mobility generation.
Acknowledgments
This study was supported by CNPq (processes 314603/2023-9, 441444/20237, and 444724/2024-9) - and the PEPR MOBIDEC Mob Sci-Dat Factory project. This research is also part of the INCT TILD-IAR funded
by CNPq (proc. 408490/2024-1).
7To be released

When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Sim
References
[1] A. Cuttone, S. Lehmann and M. C. Gonzalez. 2018. Understanding predictability
and exploration in human mobility. EPJ Data Science 7, 1 (Jan. 2018).
[2] Icek Ajzen. 1991. The theory of planned behavior. Organizational Behavior and
Human Decision Processes 50, 2 (1991), 179–211. doi:10.1016/0749-5978(91)90020T Theories of Cognitive Self-Regulation.
[3] Laura Alessandretti, Ulf Aslak, and Sune Lehmann. 2020. The scales of human
mobility. Nature 587, 7834 (Nov. 2020), 402–407.
[4] Licia Amichi, Aline Carneiro Viana, Mark Crovella, and Antonio A. F Loureiro.
2022. Revealing an inherently limiting factor in human mobility prediction. IEEE
Transactions on Emerging Topics in Computing (2022). doi:10.1109/TETC.2022.
3229088
[5] Licia Amichi, Aline Carneiro Viana, Mark Crovella, and Antonio A.F. Loureiro.
2020. Understanding individuals’ proclivity for novelty seeking. In Proceedings of
the 28th International Conference on Advances in Geographic Information Systems
(Seattle, WA, USA) (SIGSPATIAL ’20). Association for Computing Machinery, New
York, NY, USA, 314–324. doi:10.1145/3397536.3422248
[6] Licia Amichi, Aline Carneiro Viana, Mark Crovella, and Antonio A.F. Loureiro.
2021. From movement purpose to perceptive spatial mobility prediction. In
Proceedings of the 29th International Conference on Advances in Geographic Information Systems (Beijing, China) (SIGSPATIAL ’21). Association for Computing
Machinery, New York, NY, USA, 500–511. doi:10.1145/3474717.3484220
[7] Hugo Barbosa, Marc Barthelemy, Gourab Ghoshal, Charlotte R. James, Maxime
Lenormand, Thomas Louail, Ronaldo Menezes, José J. Ramasco, Filippo Simini,
and Marcello Tomasini. 2018. Human mobility: Models and applications. Physics
Reports 734 (March 2018), 1–74. doi:10.1016/j.physrep.2018.01.001
[8] Michael Batty. 2024. The Computable City: Histories, Technologies, Stories, Predictions. The MIT Press. doi:10.7551/mitpress/14099.001.0001
[9] Nicolas Bougie and Narimawa Watanabe. 2025. CitySim: Modeling Urban Behaviors and City Dynamics with Large-Scale LLM-Driven Agent Simulation. In
Proceedings of the 2025 Conference on Empirical Methods in Natural Language
Processing: Industry Track, Saloni Potdar, Lina Rojas-Barahona, and Sebastien
Montella (Eds.). Association for Computational Linguistics, Suzhou (China), 215–
229. doi:10.18653/v1/2025.emnlp-industry.15
[10] Alexandre Chasse, Anne Josiane Kouam, Aline Carneiro Viana, Razvan Stanica, Wellington Lobato, Geymerson Ramos, Geoffrey Deperle, Abdelmounaim
Bouroudi, Suzanne Bussod, and Fernando Molano Ortiz. 2025. The NetMob25
Dataset: A High-resolution Multi-layered View of Individual Mobility in Greater
Paris Region. (June 2025). https://hal.science/hal-05365088 working paper or
preprint.
[11] Guangshuo Chen, Aline Carneiro Viana, Marco Fiore, and Carlos Sarraute. 2019.
Complete trajectory reconstruction from sparse mobile phone data. EPJ Data
Science 8, 1 (Oct. 2019). doi:10.1140/epjds/s13688-019-0206-8
[12] Joshua M Epstein. 2007. Generative social science. Princeton University Press,
Princeton, NJ.
[13] João Paulo Esper, Aline Carneiro Viana, and Jussara M. Almeida. 2024. Beauty
or Beast: Human Behavioral Insights and Learning Power of Federated Mobility
Prediction. In Proceedings of the 32nd ACM International Conference on Advances in
Geographic Information Systems (Atlanta, GA, USA) (SIGSPATIAL ’24). Association
for Computing Machinery, New York, NY, USA, 325–337. doi:10.1145/3678717.
3691323
[14] European Environment Agency. 2019. CORINE Land Cover 2018 (raster 100 m),
Europe, 6-yearly - version 2020_20u1, May 2020. doi:10.2909/960998C1-18704E82-8051-6485205EBBAC
[15] Jie Gao and Yaoxin Wu. 2026. LLMs for Human Mobility: Opportunities, Challenges, and Future Directions. arXiv:2603.12420 [cs.HC] https://arxiv.org/abs/
2603.12420
[16] Marta C. González, César A. Hidalgo, and Albert-László Barabási. 2008. Understanding individual human mobility patterns. Nature 453, 7196 (June 2008),
779–782. doi:10.1038/nature06958
[17] Cate Heine, Kevin P O’Keeffe, Paolo Santi, Li Yan, and Carlo Ratti. 2023. Travel
distance, frequency of return, and the spread of disease. Sci. Rep. 13, 1 (Aug. 2023),
14064.
[18] Institut National de la Statistique et des Études Économiques. 2024. Base permanente des équipements (BPE) 2023. https://www.insee.fr/fr/metadonnees/
source/operation/s2155/bases-donnees-ligne Accessed: 2026-02-03.
[19] Alexandra Kapp, Julia Hansmeyer, and Helena Mihaljević. 2023. Generative
Models for Synthetic Urban Mobility Data: A Systematic Literature Review.
Comput. Surveys 56, 4 (Nov. 2023), 1–37. doi:10.1145/3610224
[20] Jack P.C. Kleijnen. 1995. Verification and validation of simulation models. European Journal of Operational Research 82, 1 (1995), 145–162. doi:10.1016/03772217(94)00016-6
[21] Anne Josiane Kouam, Aline Carneiro Viana, Mariano G. Beiró, Leo Ferres, and
Luca Pappalardo. 2025. Beyond Aggregates: A Fine-Grained Analysis of Individual Mobility and Traffic Dependencies. In MSWiM 2025 - 27th International
Conference on Modeling, Analysis and Simulation of Wireless and Mobile Systems.
IEEE, Barcelona, Spain, 201–210. doi:10.1109/MSWiM67937.2025.11309071

on SIGSPATIAL’26, November 03–06, 2026, Riverside, CA, USA
[22] Anne Josiane Kouam, Aline Carneiro Viana, and Alain Tchana. 2023. Zen: LSTMbased generation of individual spatiotemporal cellular traffic with interactions.
arXiv:2301.02059 [cs.NI] https://arxiv.org/abs/2301.02059
[23] L. Pappalardo, F. Simini, S. Rinzivillo, D. Pedreschi, F. Giannotti and A.-L. Barabási.
2015. Returners and explorers dichotomy in human mobility. Nature Communications 6, 8166 (Sep 2015).
[24] Maik Larooij and Petter Törnberg. 2025. Do Large Language Models Solve the
Problems of Agent-Based Modeling? A Critical Review of Generative Social
Simulations. arXiv:2504.03274 [cs.MA] https://arxiv.org/abs/2504.03274
[25] Yuebing Liang, Yichao Liu, Xiaohan Wang, and Zhan Zhao. 2024. Exploring large
language models for human mobility prediction under public events. Computers,
Environment and Urban Systems 112 (2024), 102153.
[26] J. Lin. 2006. Divergence measures based on the Shannon entropy. IEEE Trans. Inf.
Theor. 37, 1 (Sept. 2006), 145–151. doi:10.1109/18.61115
[27] A. H. Maslow. 1943. A theory of human motivation. Psychological Review 50, 4
(1943), 370–396. doi:10.1037/h0054346
[28] Overture Maps Foundation. 2026. Overture Maps Dataset. https://overturemaps.
org. Accessed: 2026-02-03. Data includes content from © OpenStreetMap contributors, licensed under the Open Database License (ODbL)..
[29] Luca Pappalardo, Filippo Simini, Gianni Barlacchi, and Roberto Pellungrini. 2022.
scikit-mobility: A Python Library for the Analysis, Generation, and Risk Assessment of Mobility Data. Journal of Statistical Software 103, 1 (2022), 1–38.
doi:10.18637/jss.v103.i04
[30] Jinghua Piao, Yuwei Yan, Jun Zhang, Nian Li, Junbo Yan, Xiaochong Lan, Zhihong
Lu, Zhiheng Zheng, Jing Yi Wang, Di Zhou, Chen Gao, Fengli Xu, Fang Zhang,
Ke Rong, Jun Su, and Yong Li. 2025. AgentSociety: Large-Scale Simulation of
LLM-Driven Generative Agents Advances Understanding of Human Behaviors
and Society. arXiv:2502.08691 [cs.SI] https://arxiv.org/abs/2502.08691
[31] R G Sargent. 2013. Verification and validation of simulation models. Journal of
Simulation 7, 1 (2013), 12–24. arXiv:https://doi.org/10.1057/jos.2012.20 doi:10.
1057/jos.2012.20
[32] Markus Schläpfer, Lei Dong, Kevin O’Keeffe, Paolo Santi, Michael Szell, Hadrien
Salat, Samuel Anklesaria, Mohammad Vazifeh, Carlo Ratti, and Geoffrey B West.
2021. The universal visitation law of human mobility. Nature 593, 7860 (May
2021), 522–527.
[33] Christian M. Schneider, Vitaly Belik, Thomas Couronné, Zbigniew Smoreda, and
Marta C. González. 2013. Unravelling daily human mobility motifs. Journal of
The Royal Society Interface 10, 84 (2013), 20130246. doi:10.1098/rsif.2013.0246
[34] Helen Senefonte, Gabriel Frizzo, Myriam Delgado, Ricardo Luders, Daniel Silver,
and Thiago Silva. 2020. Regional Influences on Tourists Mobility Through the
Lens of Social Sensing. In Proc. of the International Conference on Social Informatics
(SocInfo’20). Pisa, Italy.
[35] Chaoming Song, Zehui Qu, Nicholas Blumm, and Albert-László Barabási. 2010.
Limits of Predictability in Human Mobility. Science 327, 5968 (2010), 1018–
1021. arXiv:https://www.science.org/doi/pdf/10.1126/science.1177170 doi:10.
1126/science.1177170
[36] Siyoun Sung, Changmu Jung, and Yunmi Park. 2026. Planning with ComPlanAI:
Comparative insights from a human–AI evaluation of comprehensive plans. Cities
172 (2026), 106898.
[37] Douglas Teixeira, Jussara Almeida, and Aline Carneiro Viana. 2021. On estimating
the predictability of human mobility: the role of routine. EPJ Data Science 10, 1
(Sept. 2021).
[38] Douglas do Couto Teixeira, Jussara M. Almeida, and Aline Carneiro Viana. 2021.
On estimating the predictability of human mobility: the role of routine. EPJ Data
Science 10, 1 (Sept. 2021). doi:10.1140/epjds/s13688-021-00304-8
[39] Douglas Do Couto Teixeira, Aline Carneiro Viana, Jussara Marques Almeida, and
Mário S. Alvim. 2021. Revealing challenges in human mobility predictability.
ACM Transactions on Spatial Algorithms and Systems (April 2021). https://inria.
hal.science/hal-03128639
[40] Douglas do Couto Teixeira, Aline Carneiro Viana, Mário S. Alvim, and Jussara M.
Almeida. 2019. Deciphering Predictability Limits in Human Mobility. In Proceedings of the 27th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems (Chicago, IL, USA) (SIGSPATIAL ’19). Association for
Computing Machinery, New York, NY, USA, 52–61. doi:10.1145/3347146.3359093
[41] Cédric Villani. 2003. Topics in Optimal Transportation. American Mathematical
Society, Providence, UNITED STATES. http://ebookcentral.proquest.com/lib/
ecnu/detail.action?docID=3114588
[42] Gang Wang, Sarita Schoenebeck, Haitao Zheng, and Ben Zhao. 2021. ”Will
Check-in for Badges”: Understanding Bias and Misbehavior on Location-Based
Social Networks. Proceedings of the International AAAI Conference on Web and
Social Media 10, 1 (Aug. 2021), 417–426. doi:10.1609/icwsm.v10i1.14718
[43] Jiawei Wang, Renhe Jiang, Chuang Yang, Zengqing Wu, Makoto Onizuka,
Ryosuke Shibasaki, Noboru Koshizuka, and Chuan Xiao. 2024. Large Language
Models as Urban Residents: An LLM Agent Framework for Personal Mobility
Generation. arXiv:2402.14744 [cs.AI] https://arxiv.org/abs/2402.14744
[44] Peter Widhalm, Yingxiang Yang, Michael Ulm, Shounak Athavale, and Marta C.
González. 2015. Discovering urban activity patterns in cell phone data. Transportation 42, 4 (March 2015), 597–623. doi:10.1007/s11116-015-9598-x

SIGSPATIAL’26, November 03–06, 2026, Riverside, CA, USA Santos et al.
[45] Qingbin Zeng, Ruotong Zhao, Jinzhu Mao, Haoyang Li, Fengli Xu, and Yong
Li. 2025. CrimeMind: Simulating Urban Crime with Multi-Modal LLM Agents.
arXiv:2506.05981 [cs.AI] https://arxiv.org/abs/2506.05981
[46] Jun Zhang, Wenxuan Ao, Depeng Jin, Li Liu, and Yong Li. 2023. A City-level Highperformance Spatio-temporal Mobility Simulation System. In Proceedings of the
1st ACM SIGSPATIAL International Workshop on Sustainable Mobility (Hamburg,
Germany) (SuMob ’23). Association for Computing Machinery, New York, NY,
USA, 23–32. doi:10.1145/3615899.3627936
[47] Jun Zhang, Wenxuan Ao, Junbo Yan, Depeng Jin, and Yong Li. 2024. A GPUaccelerated Large-scale Simulator for Transportation System Optimization Benchmarking. arXiv:2406.10661 [cs.AI] https://arxiv.org/abs/2406.10661

When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Sim
A Map Generation Scalability Benchmark
We benchmark our optimized map-generation pipeline against the
original MOSSTool. As discussed in §4.2, MOSSTool struggles with
large regions due to costly spatial matching and memory-intensive
serialization. Our spatial indexing and batch-processing optimizations reduce runtime and memory use, enabling regional-scale map
generation. Table 7 reports results for Massy, a representative urban
subset in Greater Paris area.
B CitySim Reimplementation Choices
Next, we summarize the choices used to reimplement the CitySim
reported functionalities within our AgentSociety-based artifact.
B.1 Persona Module
We extend the AgentSociety persona with the attributes described in
CitySim: life stage, Big Five traits, habits/hobbies, and preferences.
Since CitySim derives these attributes from questionnaires, we
approximate them from the agent attributes already available in
AgentSociety’s synthetic personas using LLM prompting.
B.2 Memory Module
We model CitySim’s spatial memory as POI-level beliefs over price,
atmosphere, satisfaction, and convenience. Unvisited POIs are initialized from embedding similarity to previously visited locations
with uncertainty 𝑢 = 0.25.
0
After each visit, the NeedsBlock updates the agent’s needs, and
an LLM estimates the four subjective beliefs from the agent profile
and POI context. Spatial memory is updated with a 1D Kalman filter
using fixed observation noise 𝜎 = 0.2, with each belief updated
obs
as 𝐾 · observation + (1 − 𝐾) · prior, where 𝐾 depends on current
uncertainty. Updated POIs are re-embedded, and beliefs decay daily
toward a neutral baseline with 𝛼 = 0.03.
decay
B.3 Long-Term Goal Module
The long-term goal module generates and revises agent aspirations
from persona, financial status, recent activity, social context, and
previously generated goals. We compute the prompt-level behavioral indicators described in CitySim: need fulfillment, financial
stress, social isolation, and interest in recently visited POIs. Need
fulfillment is the share of the day in which core needs remain above
target thresholds. As in CitySim, goals are updated monthly.
B.4 Planning Module
We reimplement CitySim’s planning mechanics through a custom
DailyScheduleBlock integrated into AgentSociety’s Forward pass,
preserving the simulator’s memory and environment interfaces.
Planning has two phases. At the start of each simulated day, the
block queries the LLM for a structured JSON schedule using the
agent profile, Big Five traits, preferences, chronotype, and current
need satisfaction. Following CitySim’s recursive decomposition
strategy, high-priority tasks such as sleep and work are scheduled
before medium-priority tasks such as meals and hygiene; remaining
intervals are marked as [EMPTY] for leisure or long-term goals.
When simulation time reaches an [EMPTY] block, the module
triggers value-driven execution: it retrieves the agent’s location,

on SIGSPATIAL’26, November 03–06, 2026, Riverside, CA, USA
emotional state, recent thoughts, and urgent needs, then asks the
LLM to generate and evaluate 2–4 candidate activities. The selected
activity maximizes expected satisfaction gain under the Maslowstyle need hierarchy.
B.5 Destination Selection Module
We implement belief-aware destination selection through a multistage PlaceSelectionBlock, which adds a Neighborhood-level
spatial hierarchy to AgentSociety’s map queries and falls back to
AOIs when neighborhood data are unavailable.
Macro-level area selection: When an agent forms an intention, the LLM predicts primary/secondary POI categories and an
acceptable travel radius from risk tolerance, emotional state, and
weather. Matching POIs are mapped to enclosing Neighborhood
polygons, and the LLM selects 3–5 candidate Neighborhoods using
the persona, 7-day visit history, and matching-POI density. If this
fails, the block falls back to AOI-level selection ranked by distance
and popularity.
Micro-level POI selection: Within selected Neighborhoods or
AOIs, candidate POIs are filtered and ranked using a belief-weighted
gravity model. We average the four spatial-memory beliefs into
score 𝑏 𝑗 and use distance decay 𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒1+𝛾 (𝑏𝑗 −0.5) , with 𝛾 = 2.0,
allowing highly valued POIs to attract longer trips while preserving
distance sensitivity. The selected POI is passed to MoveBlock.
B.6 Multimodal and Social Modules
Although not evaluated in this work, we reimplement Multimodal
and Social modules in En-AgentSociety to support future studies of
multimodal mobility and social interactions. We exclude them from
our experiments because reproducible multimodal routing and realistic social-network initialization remain insufficiently supported
in the available simulator infrastructure.
C Mobility Metrics and Laws
Table 6 presents all metrics and laws used in the study.
D Spatial Mobility-Law Population
Comparisons
We compare spatial mobility-law distributions across simulated
trajectories, the 500-user empirical samples, and the full empirical
populations. Since overlaying all groups in the mobility-law plots
reduces readability, we report CDFs for travel distance (Δ𝑟) and
radius of gyration (𝑟 𝑔) – see Figure 10.
E Computational Costs
Table 8 reports token usage and estimated API costs for the simulation runs.
Received 30 May 2026; revised x March 2026; accepted x June 2026

SIGSPATIAL’26, November 03–06, 2026, Riverside, CA, USA
Table 6: Mobility metrics and laws used to validate LLM-base
Type Laws / Metric Formulation
Travel distance (Δ𝑟) [16] Δ𝑟𝑖 = ||𝑥𝑖+1 − 𝑥𝑖 ||; 𝑃 (Δ𝑟 ) = (Δ
Spatial laws and
Δ𝑟 0)−𝛽𝑒−Δ𝑟/𝜅
√︃
empiriral scaling Radius of Gyration 𝑟𝑔 = 𝑛 1 (cid:205) 𝑖 ∥𝑙𝑖 − 𝑙 cm ∥2
laws (𝑟𝑔) [16]
Daily visits [33] 𝑁𝑑𝑎𝑦 = |{𝑙𝑜𝑐𝑎𝑡𝑖𝑜𝑛𝑖 : 𝑡𝑖 ∈ 𝑑𝑎𝑦}|
Predictability [35] Πmax from 𝑆 = −Π log2 Π − (1− Π) log2
Distance-frequency [32] 𝜌 Π 𝑖 ) ( + 𝑟, ( 𝑓 1 ) − = Π (𝑟 ) 𝜇 𝑓 l 𝑖 o ) g 𝜂 2 (𝑁 − 1)
OD matrix [7] 𝐹𝑎𝑏 = (cid:205) 𝑖 1(𝑎→𝑏)𝑖
Trip duration (TD.) [7] 𝜏𝑖 = 𝑡 𝑖 a + rr 1 ival − 𝑡 𝑖 departure
Temporal metrics
Dwell time (DT) [7] 𝛿𝑖 = 𝑡 𝑖 departure − 𝑡 𝑖 arrival
Visitation frequency (Vf.) 𝑓𝑙 = (cid:205) 𝑖 1[𝑙𝑖 = 𝑙 ]
[33]
Topological laws Mobility motifs [33] 𝐺𝑑 = (𝑉𝑑, 𝐸𝑑 ) from daily location seque
motif = graph isomorphism class
Mobility profiles [5, 13] profile = GMM(Intermittency, Deg. of R
Regularity [38, 39] Reg. = 𝑇 1 (cid:205) 𝑡 1[𝑙𝑡 ∈ 𝐿 known]
Behavioral metrics Stationarity [38, 39] Stat. = 𝑇 1 −1 (cid:205) 𝑡 1[𝑙𝑡 = 𝑙𝑡+1]
Diversity [38] Div. = |{subtrajectory patterns}|
Entropy [35, 39, 40] 𝑆 real ≈ 𝑛 (cid:205) l 𝑖 o ≤ g 𝑛 2( Λ 𝑛 𝑖 )
Semantic and Visit Purpose Distribution 𝑃 (𝑐) = 𝑁 1 (cid:205) 𝑖 1[𝑐𝑖 = 𝑐]
(VPD) [44]
s la p w at s io-temporal Activity Transition Matrix 𝑃 (𝑐𝑗 | 𝑐𝑖 ) = (cid:205)𝑘 #( # 𝑐 ( 𝑖 𝑐 → 𝑖→ 𝑐𝑗 𝑐 ) 𝑘 )
(ATM) [34]
Daily Activity Routine Dis- 𝑃 (𝑐,𝑡) = 𝑁 1 (cid:205) 𝑖 1[𝑐𝑖 = 𝑐,𝑡𝑖 = 𝑡 ]
tribution (DARD) [43]
Spatio-Temporal Visit Dis- 𝑃 (𝑐,ℎ,𝑡) = 𝑁 1 (cid:205) 𝑖 1[𝑐𝑖 = 𝑐,ℎ𝑖 = ℎ,𝑡𝑖 =
tribution (STVD) [43]
Jensen-Shannon Diver- JSD(𝑃,𝑄) = 1 2 𝐷 KL (𝑃 ∥𝑀) + 1 2 𝐷 KL (𝑄 ∥
Similarity metrics gence (JSD) [26] 𝑀 = 𝑃+𝑄
2
C m o u m te m rs o ( n CPC Pa ) r [ t 7] of Com- CPC = 2 (cid:205) (cid:205) 𝑎 𝑎 𝑏 𝑏 𝐹 m 𝑎𝑏 in + (𝐹 (cid:205) 𝑎 𝑎 𝑏 𝑏 ,𝐹 𝐹 ˆ ˆ 𝑎 𝑎 𝑏 𝑏 )
Wasserstein distance (𝑊 1) 𝑊 1 (𝑃,𝑄)
[41] inf𝛾∈Γ(𝑃,𝑄) E (𝑥,𝑦)∼𝛾 [𝑑 (𝑥, 𝑦)]
Table 8: Estimated API costs for simulation runs. Costs use
GPT-4o-mini pricing following the CitySim configuration [9]:
0.15$/𝑀 input tokens and 0.60$/𝑀 output tokens. Values provide a normalized cost comparison rather than actual billing
for all configurations.
Dataset / Source # Agents # Days In/Out Tokens Cost (USD)
GreaterParis (AG) 504 7 720.7 M / 110.9 M $174.65
Shanghai (AG) 500 10 887.8 M / 97.5 M $191.67
GreaterParis (CT) 504 7 609.6 M / 66.7 M $131.46
Shanghai (CT) 500 10 950.9 M / 106.6 M $206.60
Table 7: Map generation performance for Massy (GP).
Implementation Execution Time (s) Peak Memory (MB)
Original MOSSTool 135.86 ± 5.99 633.63 ± 0.21
Optimized Pipeline (Ours) 63.87 ± 0.54 546.92 ± 50.23

Santos et al.
rban simulators against empirical human mobility behavior.
Intuition / Interpretation
Captures distances between consecutive locations. Real mobility follows a truncated power-law
distribution, so deviations indicate unrealistic displacement scales.
Measures each individual’s characteristic spatial range around their center of mass, capturing
whether simulated agents remain realistically spatially bounded.
Captures the number of distinct locations visited per day, which empirically follows a lognormal-like distribution.
Estimates the upper bound of mobility predictability from trajectory entropy, indicating whether
simulated mobility is too regular or too random.
Captures the joint relationship between travel distance from home and visitation frequency,
distinguishing frequent short-range visits from infrequent long-range trips.
Measures agreement between empirical and simulated origin-destination movement flows at
multiple H3 resolutions.
Captures the distribution of travel times between consecutive visits, reflecting routing, transportation, and distance-generation realism.
Measures how long agents remain at locations before moving again, capturing activity-duration
realism.
Captures how often users visit locations over the analysis period, exposing under- or overgeneration of mobility events.
Represents daily routines as directed graphs with up to six nodes, capturing recurrent topological structures in everyday mobility.
) Classifies individuals as Scouters, Regulars, or Routiners from exploration and return dynamics.
Measures the tendency to repeatedly revisit the same locations.
Captures the frequency with which users remain in the same location across consecutive
observations.
Quantifies the variety of observed sub-trajectories or location-sequence patterns in an individual’s mobility behavior.
Measures the uncertainty and temporal complexity of trajectories, complementing profile-level
exploration behavior.
Captures the overall distribution of activity categories, such as home, work, shopping, and
leisure.
Measures sequential transitions between activity types, testing whether plausible activities
occur in realistic orders.
Captures activity distributions across 10-minute intervals throughout the day, measuring
temporal semantic rhythms.
Extends DARD by jointly modeling visits across time intervals and spatial regions, such as H3
cells.
Compares categorical distributions, including VPD, ATM, DARD, STVD, motifs, and profile
distributions.
Evaluates overlap between empirical and simulated OD matrices; higher values indicate better
flow agreement.
Compares ordinal or numerical distributions, including travel distance, trip duration, radius of
gyration, dwell time, and visitation frequency.
1.0
0.8
0.6
0.4
0.2
0.0
0 20 40 60
Trip Length (km)
FDC
1.0
0.8
0.6
0.4
0.2
0.0
0 20 40
Radius of Gyration (km)
(a) Δ𝑟
FDC
(b) 𝑟 𝑔
Figure 10: CDFs of travel distance (Δ𝑟) and radius of gyration
(𝑟 𝑔) for empirical samples, full populations, and simulated
trajectories.
