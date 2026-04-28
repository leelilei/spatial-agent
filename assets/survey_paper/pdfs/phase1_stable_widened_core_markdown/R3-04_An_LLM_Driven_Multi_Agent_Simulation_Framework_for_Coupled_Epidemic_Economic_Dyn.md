# R3-04 - An LLM-Driven Multi-Agent Simulation Framework for Coupled Epidemic-Economic Dynamics

## Stable Widened-Core Snapshot

- core_layer: `anchor_core`
- admission_status: `stable_anchor`
- corpus_tier: `Core`
- system_family: `LLM Epidemic-Economic Dynamics`
- paper_refs: `LLMEpidemicEconomic2026`
- year: `2026`
- agent_count: `100+`
- environment_side_representation: `2D_grid`
- agent_accessible_representation: `L3`
- behavioral_scale: `emergent_social_structure`
- behavior_type: `mobility; other`
- evidence_status: `observed_effect`
- spatial_behavior_coupling: `explicit`
- evaluation_method: `mixed`
- space_syntax_construct: `none`
- source_basis: `local_markdown_round3_fulltext_review`
- artifact_class: `local_markdown_fulltext`

## Representation Gap Note

The abstract city is a rectangular 2D grid with local contact distance and role-specific constraints, but the agent interface is still prompt-mediated state summaries rather than direct geometry streams.

## Original Artifact Pointer

- local_artifact_path: `assets/survey_paper/pdfs/phase1_round3_candidates/R3-04_LLM_Epidemic_Economic_Dynamics_2026.fulltext.md`

## Source Content

Title: An LLM-Driven Multi-Agent Simulation Framework for Coupled Epidemic–Economic Dynamics

URL Source: https://www.mdpi.com/2078-2489/17/3/259

Markdown Content:
## 1. Introduction

The outbreak of infectious diseases poses a dual challenge to modern society: managing the biological propagation of the virus while mitigating the socio-economic shockwaves caused by containment measures. Since the foundational work of Kermack and McKendrick[[1](https://www.mdpi.com/2078-2489/17/3/259#B1-information-17-00259)], mathematical models have been the bedrock of epidemiological forecasting. However, as highlighted during the COVID-19 pandemic, the interplay between public health policies and individual economic behaviors creates a complex adaptive system that often defies the predictions of aggregate equation-based models[[2](https://www.mdpi.com/2078-2489/17/3/259#B2-information-17-00259)].

To understand these non-linear dynamics, computational social science has increasingly turned to in silico experiments, with Agent-based Models (ABMs) emerging as a powerful paradigm for growing macroscopic social phenomena from the bottom up[[3](https://www.mdpi.com/2078-2489/17/3/259#B3-information-17-00259),[4](https://www.mdpi.com/2078-2489/17/3/259#B4-information-17-00259)]. By modeling heterogeneous agents interacting in a shared environment, ABMs allows researchers to explore how individual decisions accumulate into systemic outcomes. Yet, traditional ABMs face a critical challenge: they predominantly rely on pre-defined, static rules to govern agent behavior.

Recently, LLMs have demonstrated impressive capabilities in human-level intelligence[[5](https://www.mdpi.com/2078-2489/17/3/259#B5-information-17-00259)]. Unlike rule-based scripts, it can offers a transformative solution to this bottleneck by leveraging their vast internalized knowledge and common-sense reasoning capabilities[[6](https://www.mdpi.com/2078-2489/17/3/259#B6-information-17-00259)]. Building upon these advances, Large Language Model-based Multi-Agent Systems (MASs) have further extended the power of LLMs into multi-agent interactions and simulation, injecting new vitality into the field of ABMs. And the recent studies have demonstrated that LLM-based MASs has achieved great success in ABMs for various applications[[7](https://www.mdpi.com/2078-2489/17/3/259#B7-information-17-00259),[8](https://www.mdpi.com/2078-2489/17/3/259#B8-information-17-00259)]. However, LLM-based MASs for epidemiological ABMs remain under-explored.

In this paper, we propose an LLM-driven Multi-Agent Simulation framework specifically designed to investigate the coupled epidemic–economic dynamics. In our system, each agent is not merely a data point but a cognitive entity that perceives its infection status and financial pressure, deliberates on the risks of going to work versus the safety of staying home, and makes autonomous decisions that feed back into the macroscopic system. This approach allows us to build a high-fidelity “Computational Policy Laboratory”, where the impact of NPIs (Non-Pharmaceutical Interventions) can be evaluated not just by infection curves, but by the emergent behavioral responses of a diverse population.

The contributions of this paper are listed below:

*   Framework Proposal: We propose a novel LLM-driven Multi-Agent Simulation framework for coupled epidemic–economic dynamics, enabling agents to exhibit human-level reasoning and adaptive behaviors, thus overcoming the rigidity of traditional rule-based models.

*   Cognitive Architecture: We design a Perception-Deliberation-Action (PDA) loop with a Chain-of-Thought-Action (CoTA) mechanism, effectively translating complex environmental states into natural language prompts and mapping LLM reasoning back into executable simulation actions.

*   High-Fidelity Simulation: We demonstrate the framework’s capability to achieve high-fidelity simulation of real-world epidemic dynamics, effectively capturing the complex, non-linear evolution of virus propagation driven by adaptive human behaviors, offering a valuable reference for managing public health crises.

*   Robustness & Generalization Validation: Through comprehensive experiments, we substantiate the system’s robustness across diverse Large Language Model backends and population scales, quantifying the divergent socio-economic trajectories that emerge under distinct macroscopic conditions.

## 2. Related Work

This research intersects three domains: Agent-Based Modeling (ABM), coupled epidemic–economic dynamics, and LLM-based Multi-Agent Systems.

### 2.1. ABM in Social Science

ABM is a core tool for simulating bottom-up social phenomena, enabling the exploration of emergent macro-patterns from micro-level interactions[[3](https://www.mdpi.com/2078-2489/17/3/259#B3-information-17-00259),[9](https://www.mdpi.com/2078-2489/17/3/259#B9-information-17-00259)]. This paradigm has been applied across domains from urban dynamics to financial markets[[4](https://www.mdpi.com/2078-2489/17/3/259#B4-information-17-00259),[10](https://www.mdpi.com/2078-2489/17/3/259#B10-information-17-00259)]. However, traditional ABMs, often governed by rigid heuristics, face challenges in behavioral realism and adaptability, particularly in crisis scenarios[[11](https://www.mdpi.com/2078-2489/17/3/259#B11-information-17-00259)]. Recent advances aim to bridge this gap by calibrating ABMs with large-scale empirical data to create “digital twins” of society and by integrating formal causal inference methods to enhance policy evaluation capabilities[[12](https://www.mdpi.com/2078-2489/17/3/259#B12-information-17-00259)]. Furthermore, as ABMs increasingly incorporate complex AI, new research is exploring the emergent ethical dilemmas within these simulated societies[[13](https://www.mdpi.com/2078-2489/17/3/259#B13-information-17-00259)].

### 2.2. Coupled Epidemic–Economic Models

Epidemic–economic interactions are studied via two main approaches. Macro-level models[[14](https://www.mdpi.com/2078-2489/17/3/259#B14-information-17-00259),[15](https://www.mdpi.com/2078-2489/17/3/259#B15-information-17-00259),[16](https://www.mdpi.com/2078-2489/17/3/259#B16-information-17-00259)] couple epidemiological equations with representative agent optimization, excelling at policy trade-off analysis but overlooking heterogeneity crucial for targeted interventions. Micro-level ABMs offer granularity but traditionally rely on static rules. For instance, while influential models like COVID-ABS[[17](https://www.mdpi.com/2078-2489/17/3/259#B17-information-17-00259)] successfully capture basic transmission mechanics, their agents act on rigid heuristics (e.g., fixed compliance rates) that fail to reflect the adaptive, nuanced, and often irrational trade-offs humans make when facing the dilemma of “health versus livelihood.”

### 2.3. LLM-Based Multi-Agent Systems

Integrating LLMs into MAS enables agents to act as sophisticated “computational social entities”[[5](https://www.mdpi.com/2078-2489/17/3/259#B5-information-17-00259),[18](https://www.mdpi.com/2078-2489/17/3/259#B18-information-17-00259)]. Pioneering works[[8](https://www.mdpi.com/2078-2489/17/3/259#B8-information-17-00259)] demonstrated LLM agents’ capacity for memory and reflection, while advances in cognitive architectures[[19](https://www.mdpi.com/2078-2489/17/3/259#B19-information-17-00259)] enhance their reasoning. This has spurred a new wave of large-scale simulations, from evolving social networks to complex legal systems[[20](https://www.mdpi.com/2078-2489/17/3/259#B20-information-17-00259)]. While LLM agents have been applied to economic competition[[7](https://www.mdpi.com/2078-2489/17/3/259#B7-information-17-00259),[11](https://www.mdpi.com/2078-2489/17/3/259#B11-information-17-00259)] and domain-specific challenges like climate change[[21](https://www.mdpi.com/2078-2489/17/3/259#B21-information-17-00259)] and geospatial analysis[[22](https://www.mdpi.com/2078-2489/17/3/259#B22-information-17-00259)], their application to coupled epidemic–economic crisis management remains nascent. Our work addresses this gap, leveraging LLMs to simulate adaptive decision-making in high-stakes policy scenarios.

## 3. Materials and Methods

To investigate the behavior and consequences of LLM-driven agents in a coupled socio-economic–epidemiological system, we designed and implemented an LLM-MAS simulation platform. This section details its core components: the simulation environment, agent design, and the LLM interaction mechanism that serves as the agent’s cognitive core ([Figure 1](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f001)).

**Figure 1.** System Architecture of the LLM-Driven Multi-Agent Simulation Framework. The diagram illustrates the core feedback loop: The Dynamic Simulation Environment provides perceptual state to the Multi-level Agent Population. Agents, governed by the LLM Cognitive Engine via a PDA loop, make decisions and execute actions that, in turn, modify the environment.

### 3.1. Simulation Environment

Our simulation environment is a rectangular 2D grid world, representing an abstract city. The environment contains three types of entities: Persons, Businesses, and Government. Individuals move, work, and consume in the environment; businesses serve as workplaces and providers of goods/services; the government acts as the formulator and enforcer of macro policies. Time progresses in discrete “iterations” (hours).

The epidemic spread follows the classic SEIR model framework, but adapted for agent-based execution using biological timers rather than explicit state bins.

*   Exposure and Latency (E-phase): Upon successful transmission (probability $p_{t r a n s} = 0.9$ within contact distance $d_{c o n t a c t} = 1.0$), an agent enters the latent phase. While their internal status is flagged as infected, they remain non-infectious until their infection timer $t_{i n f}$ exceeds the incubation period ($T_{e x p} = 5$ days).

*   Infectiousness (I-phase): Agents become contagious only during the window $T_{e x p} < t_{i n f} < \left(\right. T_{e x p} + T_{i n f} \left.\right)$. During this phase, they can transmit the virus to Susceptible neighbors.

*   Disease Progression: Clinical severity (Asymptomatic → Hospitalization → Critical → Death) is probabilistically determined daily based on age-stratified risk tables, as detailed in [Table 1](https://www.mdpi.com/2078-2489/17/3/259#table_body_display_information-17-00259-t001).

*   Recovery: If an agent survives beyond the recovery threshold ($T_{r e c} = 20$ days), they transition to the Recovered state, gaining permanent immunity.

This granular temporal modeling allows for the emergence of realistic transmission chains, including pre-symptomatic spread and variable viral shedding windows.

**Table 1.** Epidemiological parameters stratified by age group. Projections adapted from[[2](https://www.mdpi.com/2078-2489/17/3/259#B2-information-17-00259)].

**Table 1.** Epidemiological parameters stratified by age group. Projections adapted from[[2](https://www.mdpi.com/2078-2489/17/3/259#B2-information-17-00259)].

| Age Cohort (Years) | Hospitalization (%) | ICU Requirement (%) | Fatality Ratio (%) |
| --- | --- | --- | --- |
| 0–9 | 0.1 | 5.0 | 0.002 |
| 10–19 | 0.3 | 5.0 | 0.006 |
| 20–29 | 1.2 | 5.0 | 0.030 |
| 30–39 | 3.2 | 5.0 | 0.080 |
| 40–49 | 4.9 | 6.3 | 0.150 |
| 50–59 | 10.2 | 12.2 | 0.600 |
| 60–69 | 16.6 | 27.4 | 2.200 |
| 70–79 | 24.3 | 43.2 | 5.100 |
| 80+ | 27.3 | 70.9 | 9.300 |

To rigorously define the interaction topology, the simulation is structured as a multi-layered network connecting the State, Businesses, and Population:

*   Government-State Layer: The State is modeled as a centralized singleton entity (Government Agent) that functions as the macro-regulator. It is fully connected to the entire population network through two vertical channels: a policy channel for broadcasting mandates (e.g., Lockdowns) and a fiscal channel for collecting taxes and distributing stimulus.

*   Socio-Economic Layer: The population is embedded in a dual-network structure. Socially, agents are grouped into distinct Household Units representing co-living networks. Economically, agents are linked to Business Entities via employment contracts, forming a bipartite graph that governs labor flows and income generation.

*   Physical Contact Layer: Superimposed on these structural links is a dynamic spatial network. Disease transmission occurs not through static edges but through physical proximity within the continuous 2D grid, allowing for emergent transmission chains that respect both social clustering and stochastic encounters.

### 3.2. Agent Design

The platform defines three distinct agent types: Persons, Businesses, and Government, each characterized by specific states, objectives, and action spaces.

Person Agent. As the fundamental decision-making unit, each individual maintains a dynamic state encompassing health (SEIR status), wealth, and occupation. Their primary objective is to balance economic survival with health preservation. Their action space includes: Move (selecting destinations), Work (earning income), Consume (purchasing essentials), along with additional actions that simulate common human behaviors in real-world environments.

Business Agent. Representing commercial enterprises, these agents manage wealth and workforce with the goal of profit maximization. Key actions include Hire or Fire (adjusting workforce) and setting the Operational Mode (e.g., remote work policies).

Government Agent. Acting as the macro-regulator, this agent manages fiscal reserves to control the epidemic while maintaining economic stability. Its interventions include issuing Lockdown Orders and distributing Economic Stimulus to unemployed agents.

### 3.3. LLM-Driven Cognitive Architecture

The core of our framework is a Perception–Deliberation–Action (PDA) cycle that bridges micro-level cognition with macro-level simulation. To emulate humans’ reasoning capability and maintain rigorous simulation logic, we enforce a strict separation between global state evolution and individual decision-making.

Perception and Information Filtering. Agent actions are driven by a filtered perception layer that constrains observability across biological and spatial dimensions. Biologically, observability is partial: agents scan their immediate locality but can only detect infection based on visible symptoms; exposed or asymptomatic carriers appear indistinguishable from healthy individuals, forcing agents to act under uncertainty. Informationally, we enforce strict temporal causality: agents base their decisions on the global state frozen at the start of the current iteration. This design is not merely for computational convenience but is critical to creating realistic concurrency. It ensures that all agents deliberate simultaneously based on the same snapshot of reality, preventing “look-ahead bias” where agents acting later in the loop could artificially react to the decisions of earlier agents within the same time step. (Detailed prompts can be found in [Appendix A](https://www.mdpi.com/2078-2489/17/3/259#app1-information-17-00259)).

Reasoning and Execution. These constrained observations are synthesized into dynamic prompts using a Chain-of-Thought–Action (CoTA) strategy. The LLM explicitly deliberates on trade-offs—such as weighing income stability against infection risk—before generating a structured decision. To ensure that agent interactions remain fair and realistic, we implement a Concurrent Execution Mechanism. Instead of processing agents one by one, the system works in two distinct phases: first, all agents independently “think” and submit their decisions based on the same frozen snapshot of the world; only after everyone has decided are these actions applied to the environment together. This prevents early-acting agents from altering the world for those acting later in the same moment, strictly preserving the simultaneous nature of real-world behavior.

### 3.4. Implementation Architecture

To operationalize the theoretical PDA loop, we developed a multi-layered architecture centered on a Status Pool. This component acts as a centralized repository for environmental states and agent memories, implementing strict protocols to enforce realistic information asymmetry. The simulation proceeds through a three-phase pipeline: (1) State Aggregation, computing global epidemiological and economic indicators; (2) Cognitive Processing, where the system constructs prompts by integrating environmental context, agent profiles, and decision histories prior to dispatching batched LLM queries; and (3) Action Execution, where an Action Registry validates and maps natural language decisions to executable primitives. To ensure behavioral concurrency, a buffering mechanism temporarily holds all decisions for the current iteration. This prevents early actors from prematurely altering the environment state seen by others, thereby simulating the simultaneous nature of real-world human decision-making. Additionally, periodic economic activities (e.g., payrolls) are triggered by fixed timers, operating independently of the cognitive loop to authentically simulate universally accepted real-world economic cycles.

[Figure 2](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f002) provides a comprehensive visual overview of this execution pipeline. It delineates the sequential flow from system initialization, through the cyclic iteration of the main simulation loop (encompassing environmental evolution, the LLM-driven PDA cycle, and action synchronization), to the final data analysis phase. This structural mapping ensures that the theoretical cognitive model is rigorously translated into executable procedural logic.

**Figure 2.** Operational Workflow of the Simulation Platform. The flowchart details the Three-Phase Pipeline: (1) Initialization establishes the demographic and economic baseline; (2) Main Loop orchestrates the concurrent PDA cycle, where environmental evolution and agent deliberation occur in synchronized steps; (3) Output and Analysis logs multi-dimensional data for post hoc visualization.

### 3.5. Model Parameter Configuration

To ensure reproducibility and real-world alignment, this section details the key parameters. We referenced and expanded upon the parameter settings from the baseline paper[[17](https://www.mdpi.com/2078-2489/17/3/259#B17-information-17-00259)], leveraging publicly available data from highly credible third-party organizations as the fundamental configuration parameters, while incorporating empirical data to ensure high realism. Specifically, the synthetic population ($N = 50$) is generated to mirror real-world demographic structures. Age assignments follow a Beta distribution ($\alpha = 2 , \beta = 4$) scaled to $\left[\right. 0 , 100 \left]\right.$ to reflect a realistic age pyramid[[23](https://www.mdpi.com/2078-2489/17/3/259#B23-information-17-00259)], while household composition and vulnerability layers are initialized based on official census and homeless population reports[[24](https://www.mdpi.com/2078-2489/17/3/259#B24-information-17-00259),[25](https://www.mdpi.com/2078-2489/17/3/259#B25-information-17-00259)]. Furthermore, initial wealth is allocated according to Lorenz curve principles ([Table 2](https://www.mdpi.com/2078-2489/17/3/259#table_body_display_information-17-00259-t002)), ensuring a representative wealth inequality distribution ([Table 3](https://www.mdpi.com/2078-2489/17/3/259#table_body_display_information-17-00259-t003)).

**Table 2.** Income stratification based on World Bank quintile data ($\gamma_{d i s t}$)[[26](https://www.mdpi.com/2078-2489/17/3/259#B26-information-17-00259)].

**Table 3.** Simulation configuration: Economic structure and Agent dynamics.

## 4. Experimental Design

To rigorously assess the validity and heuristic power of the proposed framework, we structured the experimental evaluation into two distinct phases: (1) Core Scenario Exploration, which functions as a “computational policy laboratory” to investigate emergent socio-economic dynamics under distinct macroscopic conditions; and (2) Model Robustness Validation, which scrutinizes the internal consistency of the LLM-driven cognitive architecture across different parameter scales and backend models.

### 4.1. Stage One: Core Scenario Exploration

We designed three representative scenarios to explore the non-linear coupling between epidemic control and economic sustainability. To ensure statistical reliability and mitigate the impact of stochasticity, each scenario was repeated five times using the DeepSeek-V3 model in the standard experimental environment ($N = 50$, see [Table 4](https://www.mdpi.com/2078-2489/17/3/259#table_body_display_information-17-00259-t004)). Crucially, to eliminate bias from specific initialization artifacts, the population is resampled for each run using independent random seeds. This ensures that the aggregated results reflect robust systemic dynamics valid across diverse demographic configurations, rather than accumulating from a single fixed population structure.

**Table 4.** Simulation configuration: Environmental and Epidemiological parameters ($N = 50$).

#### 4.1.1. Scenario A: The Baseline (Laissez-Faire)

This control scenario simulates the system’s natural evolution without centralized intervention. The Government agent is passive, issuing no NPIs or fiscal stimulus, simulating a government that imposes no restrictions during the pandemic, allowing agents to act freely as they would during non-pandemic periods. Individual agents rely entirely on their autonomous risk-reward assessments to navigate the crisis. The objective is to establish the baseline trajectory of the epidemic–economic system, isolating the endogenous interaction dynamics between viral spread and spontaneous agent behavior.

#### 4.1.2. Scenario B: Health-Priority Intervention (Lockdown + Stimulus)

This scenario simulates an aggressive, health-centric government strategy implementing the following approaches to model a government that prioritizes citizens’ lives as its primary protection goal: (1) Dynamic circuit breaker mechanism, triggering mandatory stay-at-home orders when infection rates exceed 5% and lifting them when transmission falls to safe levels; (2) Targeted economic relief, with the government automatically distributing fiscal stimulus to unemployed agents; (3) Reinforced government intervention, emphasizing in the prompts to government agents their governing style—willing to protect public health at all costs, regardless of economic consequences. Our objective is to assess the trade-offs of suppression strategies, specifically quantifying the extent to which strict containment flattens the infection curve and whether parallel fiscal aid buffers economic volatility.

#### 4.1.3. Scenario C: Decentralized Adaptation (Remote Work)

This scenario differs from top-down mandates by introducing labor market flexibility. The Work From Home Action (WFH) mechanism is activated, allowing agents to autonomously switch to remote work based on risk perception. We model a modern digital economy where remote work is fully efficient, enabling agents to maintain full income without physical presence. We investigate whether decentralized autonomous adaptation can serve as a viable soft containment strategy, balancing public health and economic continuity.

### 4.2. Stage Two: Model Robustness Validation

This stage addresses a fundamental epistemological question in LLM-based simulation: To what extent are the observed macroscopic phenomena attributable to the system’s structural design rather than stochastic artifacts, parameter scale, or model-specific biases?

#### 4.2.1. Parameter Scale Setup

We conducted comparative experiments using the DeepSeek-V3 model at a larger scale ($N = 500$) to verify if the macroscopic trends observed in the standard environment ($N = 50$) hold true. The $N = 500$ experiments were repeated twice due to higher computational costs. [Table 5](https://www.mdpi.com/2078-2489/17/3/259#table_body_display_information-17-00259-t005) summarizes the scaling logic.

**Table 5.** Parameter configuration for the robustness experiments.

#### 4.2.2. LLM Generalization Setup

We deployed four distinct commercial and open-source LLMs (DeepSeek-V3, GPT-4o-mini, Qwen2.5, Gemini2.0-flash) to drive the agent population in the standard environment ($N = 50$). The simulation parameters mirrored the Baseline Scenario (Scenario A), allowing for a direct comparison of time-series outputs across key macroscopic indicators.

## 5. Results

This section presents the results of our computational experiments. We first detail the socio-economic dynamics revealed by the core scenarios, then provide a microscopic analysis of agent behaviors to demonstrate high fidelity, and finally confirm the system’s robustness.

### 5.1. Core Scenario Exploration Results

We simulated the three core scenarios, and the comparison of their macroscopic results reveals profound differences under distinct macroscopic conditions. [Figure 3](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f003) provides an overall comparison of key metrics, while [Figure 4](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f004), [Figure 5](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f005) and [Figure 6](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f006) present detailed dynamics.

**Figure 3.** Macroscopic Dynamics Comparison across Core Scenarios. This figure contrasts the infection curves and economic indicators (such as unemployment and GDP loss) across the distinct macroscopic conditions, highlighting the trade-offs between health and economy.

**Figure 4.** Detailed Dynamics of Scenario A (Baseline). The panels show the time evolution of the epidemic (SEIR states) and economic status (wealth, unemployment) under a laissez-faire policy.

**Figure 5.** Detailed Dynamics of Scenario B (Health Priority). The panels illustrate the impact of dynamic lockdown policies, showing “flattened” infection curves but significant fluctuations in economic activity.

**Figure 6.** Detailed Dynamics of Scenario C (Remote Work). The panels show the outcomes of the WFH mechanism, highlighting a “Soft Landing” effect on both health and economy.

#### 5.1.1. Scenario A: Baseline

The results of the baseline scenario ([Figure 4](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f004)) reveal the natural evolutionary trajectory of the system without external intervention. Epidemiologically, the system experienced dramatic exponential growth, with the infected population peaking around day 24 and leading to rapid depletion of susceptible individuals. Deaths continued to rise, stabilizing at approximately 12% of the population. Economically, while wealth interaction remained stable initially, the rapid epidemic spread caused a healthcare system collapse and excessive medical expenses. These results demonstrate that a laissez-faire strategy in the face of a highly contagious epidemic inevitably leads to a dual crisis in public health and the economy.

#### 5.1.2. Scenario B: Dynamic Health Priority

In Scenario B ([Figure 5](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f005)), the dynamic lockdown strategy successfully flattened the curve, delaying the infection peak and reducing total fatalities. However, this success came at a steep economic price. The stop-and-go nature of lockdowns caused severe fluctuations in business operations, leading to cyclical spikes in unemployment. This illustrates the classic trade-off: strict containment preserves life but induces deep, intermittent economic recessions disproportionately affecting lower-income agents.

#### 5.1.3. Scenario C: Decentralized Adaptation

Scenario C ([Figure 6](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f006)) demonstrates the Soft Landing effect of the decentralized WFH mechanism. As infection rates rose, agents spontaneously shifted to remote work, reducing contact density without government coercion. This autonomous adaptation significantly lowered the peak infection rate. Economically, as the simulation models a digital economy where remote productivity is fully preserved, the system avoided the deep recession seen in Scenario B. This suggests that empowering individual flexibility can be a superior strategy to rigid top-down mandates.

### 5.2. Deep Mechanism Analysis

Beyond verifying basic rationality, our deep analysis of the simulation logs reveals complex causal chains that drive the divergent outcomes. To systematically explain these emergent phenomena, we constructed a Causal Loop Diagram ([Figure 7](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f007)) based on the agent interaction traces.

**Figure 7.** Causal Influence Diagram of Pandemic Economics. This figure maps the distinct logic chains for each scenario, derived from the simulation’s execution traces. It illustrates how micro-level behaviors (e.g., WFH, Lockdown) propagate through the economic network to produce macro-level outcomes (e.g., Deficit, Recovery). Arrows indicate causal direction.

In the Baseline scenario, the economic collapse is driven by a passive drain mechanism. The exponential infection rate leads to a surge in medical expenses. The model design specifies that medical costs are shared: 50% is paid by the individual (depleting household savings) and the remainder is subsidized by the government (via the healthcare system). This creates a Cost-Push Deficit where the government, despite having no active fiscal policy, is drained by the massive healthcare bill, leading to the dual bankruptcy of both households and the state.

Scenario B reveals the hidden economic costs of strict containment. While the lockdown effectively curbed transmission by restricting mobility, it induced a dual stagnation in both consumption and production. On the demand side, confined individuals drastically reduced shopping, causing business revenues to decline significantly. On the supply side, businesses continued to incur fixed operational costs despite workforce absence. To balance their books, firms were forced to execute mass layoffs, leading to a sharp spike in unemployment (as shown in [Figure 8](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f008)).

**Figure 8.** Comparison of Unemployment Metrics across Scenarios. The radar chart highlights the structural damage to the labor market in Scenario B compared to the resilience observed in Scenario C.

However, this economic resilience comes at an epidemiological cost. [Figure 9](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f009) presents the total cumulative case counts across the three scenarios. While Scenario C avoids economic collapse, it results in a higher average total infection count ($47.0 \pm 1.67$) compared to Scenarios A ($39.8 \pm 17.9$) and B ($33.2 \pm 18.6$). The remarkably low variance in Scenario C reflects the “Soft Landing” mechanism, where decentralized adaptation flattens the curve but prolongs the epidemic duration, leading to a stable, deterministic progression. In contrast, Scenarios A and B exhibit high volatility due to their reliance on extreme strategies—either complete laissez-faire or rigid blocking. Particularly in Scenario B, the outcome is hypersensitive to intervention timing; slight variations in the government’s decision window can lead to vastly different trajectories, causing the system to bifurcate between successful suppression and full-scale outbreak.

**Figure 9.** Comparison of Total Cumulative Cases across Scenarios. The bar chart displays the final infected population count (Mean ± Std). Scenario C shows higher total infections but with minimal variance, reflecting a consistent “flattening” strategy that prolongs the outbreak, whereas A and B show high outcome uncertainty.

Scenario C presents a complex trade-off between epidemic duration and economic resilience. The remote work mechanism functioned as a “soft isolation,” successfully lowering the infection peak but significantly extending the epidemic’s tail. Unlike the other scenarios which concluded within a month, Scenario C persisted into the second month. However, the critical advantage of this strategy lies in its preservation of the labor market: by maintaining core productivity through remote work, businesses avoided the mass layoffs seen in Scenario B.

Fine-Grained Analysis of Macro-Economic Mechanisms. A detailed decomposition of the experimental results reveals that Scenario B (Health-Priority Intervention), despite imposing strict limitations on economic activity, preserves the highest level of Government Wealth among the explored scenarios. This phenomenon stems from the distinct interaction patterns between epidemiological loads and fiscal trigger mechanisms in each setting.

In the Baseline Scenario (A), the unmitigated transmission of the virus generates a substantial medical financial burden. Under the model’s mechanism where healthcare costs are shared between individuals and the government, the high infection rate translates into an accumulation of medical liabilities. At the end of the monthly billing cycle, the government is required to settle these extensive costs, resulting in a direct and severe reduction in fiscal reserves.

In Scenario C (Decentralized Adaptation), although remote work strategies maintain infection rates closer to Scenario B levels, a discordance emerges between continued payroll obligations and reduced consumption. Analysis of the agent decision logs (specifically the consumption frequency audit) indicates that while agents secure income via telework, their risk-averse behavior leads to a marked decline in physical shopping activities. Consequently, business revenues fall significantly below the wage obligations required to be paid at month-end. To ensure the survival of economic entities, the government is triggered to provide financial aid to cover these wage deficits, thereby transferring the private sector’s operating losses to the public fiscal balance.

Furthermore, the sharp economic volatility observed near Day 30 across all scenarios is driven by the system’s synchronized financial cycle. At the end of each month, a compound settlement event occurs where businesses disburse wages, households and firms pay taxes, and the government clears accumulated medical subsidies while distributing unemployment stimulus. This simultaneous liquidity clearing creates a distinct “pulse” in the wealth trajectories (visible in [Figure 4](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f004)), physically modeling the periodic nature of real-world macroeconomic flows.

In contrast, Scenario B effectively minimizes both expenditure vectors. Epidemiologically, the dynamic circuit breaker keeps infection rates significantly below those of Scenario A. Critically, given the substantial disparity in financial implications across different income strata (referencing [Table 2](https://www.mdpi.com/2078-2489/17/3/259#table_body_display_information-17-00259-t002)), even moderate reductions in infection prevalence prevent the disproportionate accumulation of medical costs associated with widespread transmission, thereby significantly amplifying the fiscal advantages of low infection rates. Economically, the mandatory business closures in Scenario B suspend not only revenue generation but also the immediate pressure of wage payment obligations. Unlike Scenario C, where the government must intervene to bridge the revenue-wage gap, the suspended economic state of Scenario B alleviates the need for emergency fiscal stimulus. Thus, by simultaneously mitigating the medical expenditure shock observed in Scenario A and avoiding the subsidy burdens activated in Scenario C, Scenario B demonstrates superior performance in preserving government fiscal solvency.

### 5.3. Model Robustness Validation Results

#### 5.3.1. Parameter Scale Results

We compared the macroscopic infection and economic curves between the $N = 50$ and $N = 500$ experiments (both using DeepSeek-V3). The results indicate that while the absolute values scale proportionally, the key structural features—such as the timing of the infection peak (Day 24 vs. Day 26), the final infection rate (≈98%), and the shape of the recession curve—remain highly consistent. This confirms that our findings are robust to population scale and that the $N = 50$ experimental setup is a valid proxy for larger-scale dynamics.

#### 5.3.2. LLM Generalization Results

The experimental results ([Figure 10](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f010)) clearly indicate that simulations driven by the four models converge to highly similar social dynamics at the macroscopic level. Specifically, the peak of the infection curve is reached around day 25 for all, and the final mortality rate and magnitude of economic recession are also of the same order. This cross-model consistency strongly demonstrates that the socio-economic–epidemiological interaction patterns revealed by our simulation framework are a universal feature of the LLM-driven, common-sense-based agent architecture, rather than an artifact of any specific LLM.

**Figure 10.** LLM Generalization Comparison. The figure demonstrates the robustness of our framework across four different LLM backends (DeepSeek-V3, GPT-4o-mini, Qwen2.5, Gemini2.0-flash). Despite differences in underlying architectures, the macroscopic socio-economic dynamics—including infection peaks and economic recession trends—remain qualitatively consistent.

### 5.4. Sensitivity Analysis

To validate the model’s responsiveness to critical parameters and ensure its reliability as a policy laboratory, we performed sensitivity analyses on both epidemiological and economic dimensions. In these analyses, the baseline metrics are derived from the averaged experimental results of Scenario A.

Impact of Transmission Probability. [Figure 11](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f011) illustrates the system’s response to varying viral transmission probabilities ($p_{t r a n s}$), with the $p_{t r a n s} = 0.9$ curve representing the baseline data from Scenario A. The results demonstrate a clear and significant sensitivity: as $p_{t r a n s}$ decreases to 0.6 and 0.3, the cumulative mortality rate drops disproportionately, and the curve’s growth trajectory flattens markedly. This non-linear response confirms that the model correctly captures the mechanical sensitivity of infection dynamics to changes in contact parameters.

**Figure 11.** Sensitivity of Epidemic Mortality to Transmission Probability ($p_{t r a n s}$). The solid red line represents the baseline data from Scenario A ($p_{t r a n s} = 0.9$). The dashed lines simulate lower transmission scenarios ($p = 0.6 , 0.3$), showing a non-linear reduction in cumulative deaths and flattened growth curves, demonstrating the model’s epidemiological responsiveness.

Impact of Medical Costs on Household Wealth. We further examined the model’s sensitivity to economic variables by varying the daily medical expense parameter. [Figure 12](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f012) compares the wealth trajectories under Low, Medium (Scenario A baseline), and High cost conditions. The model exhibits distinct behavioral responses to these parameter shifts: during the outbreak phase (Days 0–30), the High Cost scenario triggers a drastic depletion of household wealth compared to the baseline, while the Low Cost scenario demonstrates significant economic preservation. This sharp, phase-dependent divergence highlights the model’s capability to sensitively reflect how economic shock parameters interact with epidemiological states, confirming its efficacy in quantifying the granular impact of economic variables within coupled dynamics.

**Figure 12.** Sensitivity of Personal Wealth to Medical Expenses. The Green line represents the baseline wealth trajectory from Scenario A (Medium Cost). The significant deviation of the Red (High Cost) and Blue (Low Cost) lines during Month 1 illustrates the distinct economic shocks caused by varying medical costs during the infection peak, followed by parallel recovery trends.

### 5.5. External Validation Against Empirical Epidemic Data

To validate the macroscopic emergent behaviors of our LLM-based multi-agent simulation and enhance the persuasiveness of our results, we conducted an external validation by comparing our baseline temporal trajectories with real-world epidemiological data from the early stages of the COVID-19 outbreak. According to the comprehensive epidemiological characteristics report of 72,314 cases published by the Chinese Center for Disease Control and Prevention (China CDC)[[34](https://www.mdpi.com/2078-2489/17/3/259#B34-information-17-00259)], the real-world epidemic curve exhibited an initial exponential growth phase around 12 January 2020, which subsequently reached its first major incidence peak on 24 January 2020. This represents a natural evolution period of approximately 12 days from the early outbreak stage to the first epidemic peak.

It is crucial to note that the infection status on 12 January in the empirical data closely mirrors the initial state of our simulation. Remarkably, the temporal dynamics generated by our simulation align closely with these empirical observations. In our unmitigated baseline scenario (Scenario A), starting from this comparable initial infection state, the simulation demonstrated that the infection rate peaked at Tick 284. Given that each tick in our model represents one hour of simulated time, this translates to exactly 11.83 days. The near-perfect alignment between the simulated time-to-peak (11.83 days) and the real-world time-to-peak (12 days) from similar starting conditions provides strong evidence that our LLM-driven agents, despite operating on individual behavioral prompts, collectively generate macroscopic epidemiological trajectories that are highly consistent with real-world infectious disease dynamics. As illustrated in [Figure 13](https://www.mdpi.com/2078-2489/17/3/259#fig_body_display_information-17-00259-f013), the simulated infection ratio curve closely tracks the exponential growth and peak timing of the empirical daily new cases, visually confirming the temporal validity of our model.

**Figure 13.** Comparison of Epidemic Trajectories: Empirical Data vs. Simulation. The blue line (left axis) represents the empirical daily new cases from the China CDC report, starting from 12 January (Day 0). The red dashed line (right axis) represents the simulated infection ratio from our baseline Scenario A. Both curves exhibit a highly synchronized exponential growth phase, reaching their respective peaks at approximately Day 12 (24 January in the empirical timeline), demonstrating the model’s temporal validity.

## 6. Discussion

The core contribution of this study is the proposal and validation of a multi-agent simulation framework driven by LLMs for exploring complex socio-economic–epidemiological systems. In this section, we delve into the theoretical and practical implications of the experimental results, compare our work with existing research, and candidly discuss its limitations and future directions.

### 6.1. Theoretical Implications

Our experiments demonstrate that LLMs can effectively serve as the “cognitive engine” for computational social agents. The high fidelity observed in the Micro-Behavioral Analysis suggests that LLMs successfully internalize human-like risk assessment and decision-making logic. This offers a theoretical bridge between micro-level cognitive psychology and macro-level social dynamics, supporting the generative social science paradigm.

### 6.2. Practical Implications

The Core Scenario Exploration vividly demonstrates the wicked nature of policymaking. Our “Computational Policy Laboratory” reveals that there are no perfect solutions, only trade-offs. The health-priority strategy saves lives but inflicts economic pain, while the decentralized adaptation strategy offers a promising middle path. Crucially, our deep mechanism analysis uncovered hidden liabilities—such as the government’s role as the payer of last resort—that are often invisible in standard aggregate models. These findings provide policymakers with a quantifiable reference for anticipating the complex, non-linear consequences of their interventions before implementation.

### 6.3. Comparison with Related Work

Our framework offers distinct advantages over existing paradigms. Unlike Equation-Based Models that rely on homogeneous mixing assumptions, our approach connects macro-phenomena to micro-behavioral foundations. Compared to Rule-Based ABMs, it enables the endogenous emergence of heterogeneous behaviors without pre-scripted rules. Furthermore, while recent LLM-based simulations often focus on general social interactions[[8](https://www.mdpi.com/2078-2489/17/3/259#B8-information-17-00259)], our work rigorously targets the high-stakes domain of epidemic–economic coupling, providing a specialized testbed for policy evaluation.

## 7. Conclusions

This paper introduces a novel LLM-driven multi-agent simulation framework for coupled epidemic–economic dynamics. Our experiments demonstrate that this approach can generate high-fidelity, emergent social behaviors and provide a powerful computational laboratory for policy analysis. By replacing rigid heuristics with the nuanced reasoning of LLMs, we offer a new paradigm for building more realistic and adaptive models in computational social science, bridging the gap between micro-level cognition and macro-level societal outcomes.

### 7.1. Limitations and Future Perspectives

#### 7.1.1. Limitations of Model Simplification

The current model simplifies real-world complexities such as detailed contact networks and supply chains; incorporating richer empirical structures would improve realism. In terms of epidemiological fidelity, while the SEIR framework captures fundamental transmission dynamics, it currently abstracts away complex pharmaceutical interventions. The system does not yet account for vaccinated compartments, immune waning, or variant-specific reinfection pathways, limiting its applicability to long-term endemic scenarios. Furthermore, the economic module approximates healthcare impacts through aggregate government subsidies, simplifying the granular financial shocks of hospitalization on diverse household strata.

#### 7.1.2. Computational Feasibility and Scalability Analysis

Regarding the computational and financial costs of large-scale simulations, we acknowledge that using LLM inference for every agent at every time step constitutes a significant resource bottleneck. In our experimental configuration (using the DeepSeek-V3 model), the average inference time for a single agent’s decision step is approximately 1.2 s. For a simulation scale of $N = 50$, the parallel processing mechanism implemented via

ThreadPoolExecutor
keeps the total computational time per update cycle (simulation hour) within 10 s. However, costs grow linearly with scale, posing a barrier to direct expansion to city-level populations ($N$> 10,000).

To mitigate this issue, we have adopted the following optimization strategies in our engineering implementation and future planning:

Parallel Execution and Context Storage Optimization: Our system employs a

ThreadPoolExecutor
-based concurrent inference architecture to mask network latency. Simultaneously, we implement context storage optimization during the ecosystem Prompt construction phase to strictly control Token consumption, preventing costs from growing exponentially with environmental complexity.

Model Compatibility and Cost Optimization: The LLM generalization analysis in this paper (see [Section 4.2.2](https://www.mdpi.com/2078-2489/17/3/259#sec4dot2dot2-information-17-00259)) confirms that our multi-agent framework exhibits highly consistent macroscopic socio-economic dynamics across different LLM backends (including DeepSeek-V3, GPT-4o-mini, Qwen2.5, and Gemini2.0-flash). This finding indicates the framework’s robustness regarding the choice of “cognitive engine.” The experimental results establish a clear path for low-cost scaling: researchers can safely switch to lightweight models with fewer parameters and lower inference costs (such as GPT-4o-mini or open-source models) to significantly reduce the computational and financial costs of large-scale simulations without sacrificing the validity and fidelity of the results.

Future work will focus on enriching the model with finer-grained empirical data, supported by the aforementioned computational optimization techniques to enable larger-scale simulations. Specifically, we will pursue three key directions: (1) Epidemiological Extension, incorporating vaccination, immune decay, and detailed hospitalization cost models; (2) Cognitive Enhancement, enriching agents with long-term memory and communication protocols to simulate collective behaviors like rumor propagation; and (3) Scale and Efficiency, leveraging low-cost lightweight models to scale simulations to city-level populations while exploring model distillation techniques.

## Author Contributions

Conceptualization, S.W. and H.L.; methodology, S.W.; software, S.W. and Q.Y.; validation, S.W., S.Z. and Q.Y.; formal analysis, S.W.; investigation, S.Z.; resources, H.L.; data curation, S.W.; writing—original draft preparation, S.W.; writing—review and editing, H.L.; visualization, S.W.; supervision, H.L.; project administration, H.L. All authors have read and agreed to the published version of the manuscript.

## Funding

This research received no external funding.

## Institutional Review Board Statement

Not applicable.

## Informed Consent Statement

Not applicable.

## Data Availability Statement

The original contributions presented in this study are included in the article. Further inquiries can be directed to the corresponding author.

## Conflicts of Interest

The authors declare no conflicts of interest.

## Appendix A. LLM Prompt Templates

To ensure reproducibility, this appendix provides the complete prompt templates sent to the Large Language Models (LLMs). Our system uses a dynamic prompt construction mechanism that generates prompts based on the agent’s immediate state (Perception Layer) and static attributes (Role Layer).

*   Computational Environment: This framework was implemented in Python (version 3.12, [https://www.python.org/](https://www.python.org/)). The following boxes present the core prompt templates used to guide the LLM agents’ behavior during the simulation.

### Appendix A.1. System Prompt

The system prompt sets the basic role and simulation constraints for the agent.

![Image 1: Information 17 00259 i001](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-i001.png)

### Appendix A.2. User Context Prompt

The user prompt provides current observation state, environmental information, and available action space.

![Image 2: Information 17 00259 i002](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-i002.png)

### Appendix A.3. Sample Output

The LLM returns a decision compliant with the JSON format:

![Image 3: Information 17 00259 i003](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-i003.png)

### Appendix A.4. Core Logic Implementation

To further increase transparency, we provide the core Python function logic used to generate the above prompts (Listings A1 and A2).

![Image 4: Information 17 00259 i004](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-i004.png)

![Image 5: Information 17 00259 i005](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-i005.png)

### Appendix A.5. Action Descriptions

Each option in the action space has a specific description informing the LLM of potential consequences.

**Table A1.** Action Descriptions used in Prompts.

**Table A1.** Action Descriptions used in Prompts.

| Action | Description Prompt |
| --- | --- |
| GoToWork | Go to work—Normal work schedule, earn salary income (exposure risk) [CRITICAL] Missing work for 3 consecutive days (72 h) will result in termination and job loss. [INCOME] Work provides monthly salary. Unemployed = no regular income. [RISK] Exposure to coworkers and customers during epidemic. |
| StayHome | Stay home—Avoid exposure risk, but has employment consequences [SAFETY] Stay home to protect health and avoid virus exposure. [WARNING] If employed: Missing work for 3 consecutive DAYS (72 h) will result in TERMINATION—You will be fired and lose your job. [BALANCE] Consider if staying home is worth risking job loss. |
| GoShopping | Go shopping—Purchase household necessities [PURPOSE] Maintain household supplies and support local economy. [CONSIDERATIONS]—Health risk: Exposure to other people—Economic impact: Supports local businesses—Household needs: Important when supplies are running low. |

## References

1.   Kermack, W.O.; McKendrick, A.G. A contribution to the mathematical theory of epidemics. Proc. R. Soc. Lond. Ser. A Contain. Pap. Math. Phys. Character**1927**, 115, 700–721. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=A+contribution+to+the+mathematical+theory+of+epidemics&author=Kermack,+W.O.&author=McKendrick,+A.G.&publication_year=1927&journal=Proc.+R.+Soc.+Lond.+Ser.+A+Contain.+Pap.+Math.+Phys.+Character&volume=115&pages=700%E2%80%93721&doi=10.1098/rspa.1927.0118)] [[CrossRef](https://doi.org/10.1098/rspa.1927.0118)]
2.   Ferguson, N.M.; Laydon, D.; Nedjati-Gilani, G.; Imai, N.; Ainslie, K.; Baguelin, M.; Bhatia, S.; Boonyasiri, A.; Cucunuba, Z.; Cuomo-Dannenburg, G.; et al. Report 9: Impact of Non-Pharmaceutical Interventions (NPIs) to Reduce COVID-19 Mortality and Healthcare Demand; Report 9; Imperial College London: London, UK, 2020. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Report+9:+Impact+of+Non-Pharmaceutical+Interventions+(NPIs)+to+Reduce+COVID-19+Mortality+and+Healthcare+Demand&author=Ferguson,+N.M.&author=Laydon,+D.&author=Nedjati-Gilani,+G.&author=Imai,+N.&author=Ainslie,+K.&author=Baguelin,+M.&author=Bhatia,+S.&author=Boonyasiri,+A.&author=Cucunuba,+Z.&author=Cuomo-Dannenburg,+G.&author=et+al.&publication_year=2020)] [[CrossRef](https://doi.org/10.25561/77482)]
3.   Epstein, J.M. Generative Social Science: Studies in Agent-Based Computational Modeling; Princeton University Press: Princeton, NJ, USA, 2006. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Generative+Social+Science:+Studies+in+Agent-Based+Computational+Modeling&author=Epstein,+J.M.&publication_year=2006)]
4.   Helbing, D.; Balietti, S. Agent-based modeling. In Social Self-Organization: Agent-Based Simulations and Experiments to Study Emergent Social Behavior; Springer: Berlin/Heidelberg, Germany, 2012; pp. 25–70. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Agent-based+modeling&author=Helbing,+D.&author=Balietti,+S.&publication_year=2012&pages=25%E2%80%9370)]
5.   Wang, L.; Ma, C.; Feng, X.; Zhang, Z.; Yang, H.; Zhang, J.; Chen, Z.; Tang, J.; Chen, X.; Lin, Y.; et al. A survey on large language model based autonomous agents. Front. Comput. Sci.**2024**, 18, 186345. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=A+survey+on+large+language+model+based+autonomous+agents&author=Wang,+L.&author=Ma,+C.&author=Feng,+X.&author=Zhang,+Z.&author=Yang,+H.&author=Zhang,+J.&author=Chen,+Z.&author=Tang,+J.&author=Chen,+X.&author=Lin,+Y.&author=et+al.&publication_year=2024&journal=Front.+Comput.+Sci.&volume=18&pages=186345&doi=10.1007/s11704-024-40231-1)] [[CrossRef](https://doi.org/10.1007/s11704-024-40231-1)]
6.   Bommasani, R.; Hudson, D.A.; Adeli, E.; Altman, R.; Arora, S.; von Arx, S.; Bernstein, M.S.; Bohg, J.; Bosselut, A.; Brunskill, E.; et al. On the Opportunities and Risks of Foundation Models. arXiv**2021**, arXiv:2108.07258. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=On+the+Opportunities+and+Risks+of+Foundation+Models&author=Bommasani,+R.&author=Hudson,+D.A.&author=Adeli,+E.&author=Altman,+R.&author=Arora,+S.&author=von+Arx,+S.&author=Bernstein,+M.S.&author=Bohg,+J.&author=Bosselut,+A.&author=Brunskill,+E.&author=et+al.&publication_year=2021&journal=arXiv)]
7.   Zhao, Q.; Wang, J.; Zhang, Y.; Jin, Y.; Zhu, K.; Chen, H.; Xie, X. Competeai: Understanding the competition dynamics in large language model-based agents. arXiv**2023**, arXiv:2310.17512. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Competeai:+Understanding+the+competition+dynamics+in+large+language+model-based+agents&author=Zhao,+Q.&author=Wang,+J.&author=Zhang,+Y.&author=Jin,+Y.&author=Zhu,+K.&author=Chen,+H.&author=Xie,+X.&publication_year=2023&journal=arXiv)]
8.   Park, J.S.; O’Brien, J.C.; Cai, C.J.; Morris, M.R.; Liang, P.; Bernstein, M.S. Generative agents: Interactive simulacra of human behavior. arXiv**2023**, arXiv:2304.03442. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Generative+agents:+Interactive+simulacra+of+human+behavior&author=Park,+J.S.&author=O%E2%80%99Brien,+J.C.&author=Cai,+C.J.&author=Morris,+M.R.&author=Liang,+P.&author=Bernstein,+M.S.&publication_year=2023&journal=arXiv)]
9.   De Marchi, S.; Page, S.E. Agent-based models. Annu. Rev. Political Sci.**2014**, 17, 1–20. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Agent-based+models&author=De+Marchi,+S.&author=Page,+S.E.&publication_year=2014&journal=Annu.+Rev.+Political+Sci.&volume=17&pages=1%E2%80%9320&doi=10.1146/annurev-polisci-080812-191558)] [[CrossRef](https://doi.org/10.1146/annurev-polisci-080812-191558)]
10.   Farmer, J.D.; Foley, D. The economy needs agent-based modelling. Nature**2009**, 460, 685–686. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=The+economy+needs+agent-based+modelling&author=Farmer,+J.D.&author=Foley,+D.&publication_year=2009&journal=Nature&volume=460&pages=685%E2%80%93686&doi=10.1038/460685a)] [[CrossRef](https://doi.org/10.1038/460685a)]
11.   Filippas, A.; Horton, J.J.; Manning, B.S. Large language models as simulated economic agents: What can we learn from homo silicus? In Proceedings of the 25th ACM Conference on Economics and Computation, New Haven, CT, USA, 8–11 July 2024; pp. 614–615. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Large+language+models+as+simulated+economic+agents:+What+can+we+learn+from+homo+silicus?&conference=Proceedings+of+the+25th+ACM+Conference+on+Economics+and+Computation&author=Filippas,+A.&author=Horton,+J.J.&author=Manning,+B.S.&publication_year=2024&pages=614%E2%80%93615)]
12.   Pearl, J.; Glymour, M.; Jewell, N.P. Causal Inference in Statistics: A Primer; John Wiley & Sons: Hoboken, NJ, USA, 2016. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Causal+Inference+in+Statistics:+A+Primer&author=Pearl,+J.&author=Glymour,+M.&author=Jewell,+N.P.&publication_year=2016)]
13.   Hornyak, T. Agentic AI Is Here—But Are We Ready? Res. Technol. Manag.**2025**, 68, 59–60. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Agentic+AI+Is+Here%E2%80%94But+Are+We+Ready?&author=Hornyak,+T.&publication_year=2025&journal=Res.+Technol.+Manag.&volume=68&pages=59%E2%80%9360&doi=10.1080/08956308.2025.2532320)] [[CrossRef](https://doi.org/10.1080/08956308.2025.2532320)]
14.   Eichenbaum, M.S.; Rebelo, S.; Trabandt, M. The macroeconomics of epidemics. Rev. Financ. Stud.**2021**, 34, 5149–5187. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=The+macroeconomics+of+epidemics&author=Eichenbaum,+M.S.&author=Rebelo,+S.&author=Trabandt,+M.&publication_year=2021&journal=Rev.+Financ.+Stud.&volume=34&pages=5149%E2%80%935187&doi=10.1093/rfs/hhab040)] [[CrossRef](https://doi.org/10.1093/rfs/hhab040)]
15.   Acemoglu, D.; Chernozhukov, V.; Werning, I.; Whinston, M.D. Optimal targeted lockdowns in a multigroup SIR model. Am. Econ. Rev. Insights**2021**, 3, 487–502. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Optimal+targeted+lockdowns+in+a+multigroup+SIR+model&author=Acemoglu,+D.&author=Chernozhukov,+V.&author=Werning,+I.&author=Whinston,+M.D.&publication_year=2021&journal=Am.+Econ.+Rev.+Insights&volume=3&pages=487%E2%80%93502&doi=10.1257/aeri.20200590)] [[CrossRef](https://doi.org/10.1257/aeri.20200590)]
16.   Alvarez, F.; Argente, D.; Lippi, F. A simple planning problem for COVID-19 lock-down, testing, and tracing. Am. Econ. Rev. Insights**2021**, 3, 367–382. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=A+simple+planning+problem+for+COVID-19+lock-down,+testing,+and+tracing&author=Alvarez,+F.&author=Argente,+D.&author=Lippi,+F.&publication_year=2021&journal=Am.+Econ.+Rev.+Insights&volume=3&pages=367%E2%80%93382&doi=10.1257/aeri.20200201)] [[CrossRef](https://doi.org/10.1257/aeri.20200201)]
17.   Silva, P.C.; Batista, P.V.; Lima, H.S.; Alves, M.A.; Guimarães, F.G.; Silva, R.C. COVID-ABS: An agent-based model of COVID-19 epidemic to simulate health and economic effects of social distancing interventions. Chaos Solitons Fractals**2020**, 139, 110088. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=COVID-ABS:+An+agent-based+model+of+COVID-19+epidemic+to+simulate+health+and+economic+effects+of+social+distancing+interventions&author=Silva,+P.C.&author=Batista,+P.V.&author=Lima,+H.S.&author=Alves,+M.A.&author=Guimar%C3%A3es,+F.G.&author=Silva,+R.C.&publication_year=2020&journal=Chaos+Solitons+Fractals&volume=139&pages=110088&doi=10.1016/j.chaos.2020.110088)] [[CrossRef](https://doi.org/10.1016/j.chaos.2020.110088)]
18.   Xi, Z.; Chen, W.; Guo, X.; He, W.; Ding, Y.; Hong, B.; Zhang, M.; Wang, J.; Jin, S.; Zhou, E.; et al. The rise and potential of large language model based agents: A survey. Sci. China Inf. Sci.**2025**, 68, 121101. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=The+rise+and+potential+of+large+language+model+based+agents:+A+survey&author=Xi,+Z.&author=Chen,+W.&author=Guo,+X.&author=He,+W.&author=Ding,+Y.&author=Hong,+B.&author=Zhang,+M.&author=Wang,+J.&author=Jin,+S.&author=Zhou,+E.&author=et+al.&publication_year=2025&journal=Sci.+China+Inf.+Sci.&volume=68&pages=121101&doi=10.1007/s11432-024-4222-0)] [[CrossRef](https://doi.org/10.1007/s11432-024-4222-0)]
19.   Sumers, T.; Yao, S.; Narasimhan, K.; Griffiths, T. Cognitive architectures for language agents. Trans. Mach. Learn. Res.**2023**. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Cognitive+architectures+for+language+agents&author=Sumers,+T.&author=Yao,+S.&author=Narasimhan,+K.&author=Griffiths,+T.&publication_year=2023&journal=Trans.+Mach.+Learn.+Res.)]
20.   Tao, L.; Liu, H.; Ning, G.; Cao, W.; Huang, B.; Lu, C. LLM-based framework for bearing fault diagnosis. Mech. Syst. Signal Process.**2025**, 224, 112127. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=LLM-based+framework+for+bearing+fault+diagnosis&author=Tao,+L.&author=Liu,+H.&author=Ning,+G.&author=Cao,+W.&author=Huang,+B.&author=Lu,+C.&publication_year=2025&journal=Mech.+Syst.+Signal+Process.&volume=224&pages=112127&doi=10.1016/j.ymssp.2024.112127)] [[CrossRef](https://doi.org/10.1016/j.ymssp.2024.112127)]
21.   Wang, L.; He, X.; Luo, D. Deep reinforcement learning for greenhouse climate control. In Proceedings of the 2020 IEEE International Conference on Knowledge Graph (ICKG), Nanjing, China, 9–11 August 2020; pp. 474–480. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Deep+reinforcement+learning+for+greenhouse+climate+control&conference=Proceedings+of+the+2020+IEEE+International+Conference+on+Knowledge+Graph+(ICKG)&author=Wang,+L.&author=He,+X.&author=Luo,+D.&publication_year=2020&pages=474%E2%80%93480)]
22.   Zhang, Y.; Wei, C.; Wu, S.; He, Z.; Yu, W. Geogpt: Understanding and processing geospatial tasks through an autonomous GPT. arXiv**2023**, arXiv:2307.07930. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Geogpt:+Understanding+and+processing+geospatial+tasks+through+an+autonomous+GPT&author=Zhang,+Y.&author=Wei,+C.&author=Wu,+S.&author=He,+Z.&author=Yu,+W.&publication_year=2023&journal=arXiv)]
23.   IBGE. Pirâmide Etária. 2020. Available online: [https://educa.ibge.gov.br/jovens/conheca-o-brasil/populacao/18318-piramide-etaria.html](https://educa.ibge.gov.br/jovens/conheca-o-brasil/populacao/18318-piramide-etaria.html) (accessed on 2 June 2020).
24.   IBGE. Censo demográfico: Tabela 2019—Moradores em Domicílios Particulares Permanentes por Densidade de Moradores por Cômodo e Número de Banheiros. 2020. Available online: [https://sidra.ibge.gov.br/tabela/2019](https://sidra.ibge.gov.br/tabela/2019) (accessed on 2 June 2020).
25.   IPEA. Estimativa da População em Situação de Rua no Brasil; Texto para Discussão 2246; Instituto de Pesquisa Econômica Aplicada: Brasília, Brazil, 2020.
26.   World Bank. Lac Equity Lab: Income Inequality—Composition by Quintile. 2020. Available online: [https://www.worldbank.org/en/topic/poverty/lac-equity-lab1/income-inequality/composition-by-quintile](https://www.worldbank.org/en/topic/poverty/lac-equity-lab1/income-inequality/composition-by-quintile) (accessed on 3 June 2020).
27.   IBGE. Demografia das Empresas e Empreendedorismo 2017: Taxa de Sobrevivência foi de 84.8%. IBGE Agência de Notícias, Release 25738, 2017. Available online: [https://agenciadenoticias.ibge.gov.br/](https://agenciadenoticias.ibge.gov.br/) (accessed on 2 June 2020).
28.   World Bank. Business Density and the Number of New Business Registrations. 2020. Available online: [https://data.worldbank.org/indicator/IC.BUS.NREG](https://data.worldbank.org/indicator/IC.BUS.NREG) (accessed on 1 December 2024).
29.   Exame. Desemprego Atinge 12.2% No 1º Trimestre, diz IBGE. 2020. Available online: [https://exame.com/economia/brasil-tem-desemprego-de-122-no-primeiro-trimestre-diz-ibge/](https://exame.com/economia/brasil-tem-desemprego-de-122-no-primeiro-trimestre-diz-ibge/) (accessed on 3 June 2020).
30.   Lima, C.M.A.d.O. Informações sobre o novo coronavírus (COVID-19). Radiol. Bras.**2020**, 53, V–VI. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Informa%C3%A7%C3%B5es+sobre+o+novo+coronav%C3%ADrus+(COVID-19)&author=Lima,+C.M.A.d.O.&publication_year=2020&journal=Radiol.+Bras.&volume=53&pages=V%E2%80%93VI&doi=10.1590/0100-3984.2020.53.2e1)] [[CrossRef](https://doi.org/10.1590/0100-3984.2020.53.2e1)]
31.   Li, Q.; Guan, X.; Wu, P.; Wang, X.; Zhou, L.; Tong, Y.; Ren, R.; Leung, K.S.; Lau, E.H.; Wong, J.Y.; et al. Early transmission dynamics in Wuhan, China, of novel coronavirus–infected pneumonia. N. Engl. J. Med.**2020**, 382, 1199–1207. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Early+transmission+dynamics+in+Wuhan,+China,+of+novel+coronavirus%E2%80%93infected+pneumonia&author=Li,+Q.&author=Guan,+X.&author=Wu,+P.&author=Wang,+X.&author=Zhou,+L.&author=Tong,+Y.&author=Ren,+R.&author=Leung,+K.S.&author=Lau,+E.H.&author=Wong,+J.Y.&author=et+al.&publication_year=2020&journal=N.+Engl.+J.+Med.&volume=382&pages=1199%E2%80%931207&doi=10.1056/NEJMoa2001316&pmid=31995857)] [[CrossRef](https://doi.org/10.1056/NEJMoa2001316)] [[PubMed](https://www.ncbi.nlm.nih.gov/pubmed/31995857)]
32.   Lauer, S.A.; Grantz, K.H.; Bi, Q.; Jones, F.K.; Zheng, Q.; Meredith, H.R.; Azman, A.S.; Reich, N.G.; Lessler, J. The incubation period of coronavirus disease 2019 (COVID-19) from publicly reported confirmed cases: Estimation and application. Ann. Intern. Med.**2020**, 172, 577–582. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=The+incubation+period+of+coronavirus+disease+2019+(COVID-19)+from+publicly+reported+confirmed+cases:+Estimation+and+application&author=Lauer,+S.A.&author=Grantz,+K.H.&author=Bi,+Q.&author=Jones,+F.K.&author=Zheng,+Q.&author=Meredith,+H.R.&author=Azman,+A.S.&author=Reich,+N.G.&author=Lessler,+J.&publication_year=2020&journal=Ann.+Intern.+Med.&volume=172&pages=577%E2%80%93582&doi=10.7326/M20-0504)] [[CrossRef](https://doi.org/10.7326/M20-0504)]
33.   Housen, T.; Parry, A.E.; Sheel, M. How Long Are You Infectious When you Have Coronavirus? Conversation**2020**, 135295. Available online: [https://theconversation.com/](https://theconversation.com/) (accessed on 2 June 2020).
34.   Epidemiology Working Group for NCIP Epidemic Response, Chinese Center for Disease Control and Prevention. The epidemiological characteristics of an outbreak of 2019 novel coronavirus diseases (COVID-19) in China. Zhonghua Liu Xing Bing Xue Za Zhi = Zhonghua Liuxingbingxue Zazhi**2020**, 41, 145–151. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=The+epidemiological+characteristics+of+an+outbreak+of+2019+novel+coronavirus+diseases+(COVID-19)+in+China&author=Epidemiology+Working+Group+for+NCIP+Epidemic+Response,+Chinese+Center+for+Disease+Control+and+Prevention&publication_year=2020&journal=Zhonghua+Liu+Xing+Bing+Xue+Za+Zhi+=+Zhonghua+Liuxingbingxue+Zazhi&volume=41&pages=145%E2%80%93151&doi=10.3760/cma.j.issn.0254-6450.2020.02.003)] [[CrossRef](https://doi.org/10.3760/cma.j.issn.0254-6450.2020.02.003)]

**Figure 1.** System Architecture of the LLM-Driven Multi-Agent Simulation Framework. The diagram illustrates the core feedback loop: The Dynamic Simulation Environment provides perceptual state to the Multi-level Agent Population. Agents, governed by the LLM Cognitive Engine via a PDA loop, make decisions and execute actions that, in turn, modify the environment.

[![Image 6: Information 17 00259 g001](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g001.png)](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g001.png)

**Figure 2.** Operational Workflow of the Simulation Platform. The flowchart details the Three-Phase Pipeline: (1) Initialization establishes the demographic and economic baseline; (2) Main Loop orchestrates the concurrent PDA cycle, where environmental evolution and agent deliberation occur in synchronized steps; (3) Output and Analysis logs multi-dimensional data for post hoc visualization.

[![Image 7: Information 17 00259 g002](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g002.png)](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g002.png)

**Figure 3.** Macroscopic Dynamics Comparison across Core Scenarios. This figure contrasts the infection curves and economic indicators (such as unemployment and GDP loss) across the distinct macroscopic conditions, highlighting the trade-offs between health and economy.

[![Image 8: Information 17 00259 g003](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g003.png)](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g003.png)

**Figure 4.** Detailed Dynamics of Scenario A (Baseline). The panels show the time evolution of the epidemic (SEIR states) and economic status (wealth, unemployment) under a laissez-faire policy.

[![Image 9: Information 17 00259 g004](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g004.png)](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g004.png)

**Figure 5.** Detailed Dynamics of Scenario B (Health Priority). The panels illustrate the impact of dynamic lockdown policies, showing “flattened” infection curves but significant fluctuations in economic activity.

[![Image 10: Information 17 00259 g005](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g005.png)](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g005.png)

**Figure 6.** Detailed Dynamics of Scenario C (Remote Work). The panels show the outcomes of the WFH mechanism, highlighting a “Soft Landing” effect on both health and economy.

[![Image 11: Information 17 00259 g006](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g006.png)](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g006.png)

**Figure 7.** Causal Influence Diagram of Pandemic Economics. This figure maps the distinct logic chains for each scenario, derived from the simulation’s execution traces. It illustrates how micro-level behaviors (e.g., WFH, Lockdown) propagate through the economic network to produce macro-level outcomes (e.g., Deficit, Recovery). Arrows indicate causal direction.

[![Image 12: Information 17 00259 g007](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g007.png)](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g007.png)

**Figure 8.** Comparison of Unemployment Metrics across Scenarios. The radar chart highlights the structural damage to the labor market in Scenario B compared to the resilience observed in Scenario C.

[![Image 13: Information 17 00259 g008](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g008.png)](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g008.png)

**Figure 9.** Comparison of Total Cumulative Cases across Scenarios. The bar chart displays the final infected population count (Mean ± Std). Scenario C shows higher total infections but with minimal variance, reflecting a consistent “flattening” strategy that prolongs the outbreak, whereas A and B show high outcome uncertainty.

[![Image 14: Information 17 00259 g009](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g009.png)](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g009.png)

**Figure 10.** LLM Generalization Comparison. The figure demonstrates the robustness of our framework across four different LLM backends (DeepSeek-V3, GPT-4o-mini, Qwen2.5, Gemini2.0-flash). Despite differences in underlying architectures, the macroscopic socio-economic dynamics—including infection peaks and economic recession trends—remain qualitatively consistent.

[![Image 15: Information 17 00259 g010](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g010.png)](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g010.png)

**Figure 11.** Sensitivity of Epidemic Mortality to Transmission Probability ($p_{t r a n s}$). The solid red line represents the baseline data from Scenario A ($p_{t r a n s} = 0.9$). The dashed lines simulate lower transmission scenarios ($p = 0.6 , 0.3$), showing a non-linear reduction in cumulative deaths and flattened growth curves, demonstrating the model’s epidemiological responsiveness.

[![Image 16: Information 17 00259 g011](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g011.png)](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g011.png)

**Figure 12.** Sensitivity of Personal Wealth to Medical Expenses. The Green line represents the baseline wealth trajectory from Scenario A (Medium Cost). The significant deviation of the Red (High Cost) and Blue (Low Cost) lines during Month 1 illustrates the distinct economic shocks caused by varying medical costs during the infection peak, followed by parallel recovery trends.

[![Image 17: Information 17 00259 g012](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g012.png)](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g012.png)

**Figure 13.** Comparison of Epidemic Trajectories: Empirical Data vs. Simulation. The blue line (left axis) represents the empirical daily new cases from the China CDC report, starting from 12 January (Day 0). The red dashed line (right axis) represents the simulated infection ratio from our baseline Scenario A. Both curves exhibit a highly synchronized exponential growth phase, reaching their respective peaks at approximately Day 12 (24 January in the empirical timeline), demonstrating the model’s temporal validity.

[![Image 18: Information 17 00259 g013](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g013.png)](https://www.mdpi.com/information/information-17-00259/article_deploy/html/images/information-17-00259-g013.png)

**Table 2.** Income stratification based on World Bank quintile data ($\gamma_{d i s t}$)[[26](https://www.mdpi.com/2078-2489/17/3/259#B26-information-17-00259)].

| Income Quintile | Class Designation | Wealth Share (%) | Cumulative (%) |
| --- | --- | --- | --- |
| Q1 | Lowest Income | 3.62 | 3.62 |
| Q2 | Low Income | 7.88 | 11.50 |
| Q3 | Middle Income | 12.62 | 24.17 |
| Q4 | High Income | 19.71 | 43.88 |
| Q5 | Highest Income | 56.12 | 100.00 |

**Table 3.** Simulation configuration: Economic structure and Agent dynamics.

| Symbol | Parameter | Value | Description | Source |
| --- | --- | --- | --- | --- |
| Business & Agent Dynamics |
| $N_{b i z}$ | Business Count | 5 | Total enterprises | [[27](https://www.mdpi.com/2078-2489/17/3/259#B27-information-17-00259)] |
| $\Delta t_{p / b / g}$ | Agent Time Step | 2/24/72 h | Decision cycles | Empirically Defined |
| Economic Structure |
| $\gamma_{d i s t}$ | Income Distribution | [Table 2](https://www.mdpi.com/2078-2489/17/3/259#table_body_display_information-17-00259-t002) | Income strata | [[26](https://www.mdpi.com/2078-2489/17/3/259#B26-information-17-00259)] |
| $\gamma_{d e n s}$ | Business Density | 0.01875 | Firms per capita | [[28](https://www.mdpi.com/2078-2489/17/3/259#B28-information-17-00259)] |
| $Y_{i n i t}$ | Initial System GDP | 1.8 M | Total system wealth | Empirically Defined |
| $u_{i n i t}$ | Initial Unemployment | 0.12 | Initial rate | [[29](https://www.mdpi.com/2078-2489/17/3/259#B29-information-17-00259)] |

**Table 4.** Simulation configuration: Environmental and Epidemiological parameters ($N = 50$).

| Symbol | Parameter | Value | Description | Source |
| --- | --- | --- | --- | --- |
| Social and Demographic |
| $H_{g r i d} , W_{g r i d}$ | Grid Dimensions | $207 \times 207$ | Map dimensions | Empirically Defined |
| $N_{p o p}$ | Total Population | 50 | Total agent count | Empirically Defined |
| $\mathcal{D}_{a g e}$ | Age Distribution | $\beta \left(\right. 2 , 4 \left.\right)$ | Age structure | [[23](https://www.mdpi.com/2078-2489/17/3/259#B23-information-17-00259)] |
| $S_{f a m i l y}$ | Mean Family Size | 3 (Std: 1) | Mean household size | [[24](https://www.mdpi.com/2078-2489/17/3/259#B24-information-17-00259)] |
| $\rho_{h o m e}$ | Homelessness Ratio | 0.0005 | Homeless ratio | [[25](https://www.mdpi.com/2078-2489/17/3/259#B25-information-17-00259)] |
| Epidemiological |
| $d_{c o n t a c t}$ | Contact Distance | 1.0 | Safe distance | [[2](https://www.mdpi.com/2078-2489/17/3/259#B2-information-17-00259)] |
| $p_{t r a n s}$ | Transmission Prob. | 0.9 | Transmission rate | [[2](https://www.mdpi.com/2078-2489/17/3/259#B2-information-17-00259)] |
| $T_{e x p}$ | Latency Period | 5 | Incubation days | [[30](https://www.mdpi.com/2078-2489/17/3/259#B30-information-17-00259),[31](https://www.mdpi.com/2078-2489/17/3/259#B31-information-17-00259)] |
| $T_{i n f}$ | Infectiousness Period | 10 | Infectious days | [[32](https://www.mdpi.com/2078-2489/17/3/259#B32-information-17-00259)] |
| $T_{r e c}$ | Recovery Period | 20 | Recovery days | [[33](https://www.mdpi.com/2078-2489/17/3/259#B33-information-17-00259)] |

**Table 5.** Parameter configuration for the robustness experiments.

| Parameter | Main Exp. | Scale Exp. | Rationale |
| --- | --- | --- | --- |
| Population ($N_{p o p}$) | 50 | 500 | 10× scale factor |
| Grid ($H \times W$) | $207 \times 207$ | $655 \times 655$ | Constant density |
| Businesses ($N_{b i z}$) | 5 | 15 | 1 vs. 3 per stratum |
| GDP ($Y_{i n i t}$) | 1.8 M | 18 M | Proportional (36 k/capita) |

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.

© 2026 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the [Creative Commons Attribution (CC BY) license](https://creativecommons.org/licenses/by/4.0/).
