#!/usr/bin/env python3
"""Generate first-pass reading notes for the 6-city paper archive."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from textwrap import fill


ROOT = Path(__file__).resolve().parents[3]
NOTES_ROOT = ROOT / "assets" / "papers" / "notes"


PAPERS = [
    {
        "category": "01_urban_benchmarks",
        "file": "01_CityBench_Feng2024",
        "title": "CityBench: Evaluating the Capabilities of Large Language Models for Urban Tasks",
        "source": "https://arxiv.org/abs/2406.13945",
        "role": "broad urban-task benchmark",
        "decision": "must-cite",
        "why": "CityBench is the broadest baseline for evaluating LLM capability on urban tasks. It helps us define what is already covered by current urban benchmarks before claiming a gap for city-agent behavior.",
        "claim": "The paper constructs a benchmark over urban tasks to test whether LLMs can handle city-relevant knowledge, reasoning, and planning-style questions.",
        "evidence": ["Broad task taxonomy for urban intelligence evaluation.", "Useful contrast between urban knowledge/reasoning benchmarks and interactive city-agent benchmarks."],
        "measures": "urban task competence, usually through static or question-answer style evaluation",
        "does_not": "long-horizon autonomous movement, private intentions, social interaction, or environment perturbation under resettable scenarios",
        "informs": "Use it as the umbrella related-work anchor, then position 6-city as a behavioral benchmark rather than another urban QA benchmark.",
        "add": "6-city can add controlled agent rollouts, private goals, spatial feasibility checks, and trajectory-level scoring.",
        "use": "CityBench establishes that LLM urban intelligence can be evaluated systematically, but our focus shifts from static urban task ability to situated, intention-driven city behavior.",
        "reason": "Central reference for the benchmark landscape we are entering.",
    },
    {
        "category": "01_urban_benchmarks",
        "file": "02_CityGPT_CityEval_Feng2024",
        "title": "CityGPT: Empowering Urban Spatial Cognition of Large Language Models",
        "source": "https://arxiv.org/abs/2406.13948",
        "role": "urban spatial cognition benchmark/model",
        "decision": "cite",
        "why": "CityGPT/CityEval is useful because it frames urban spatial cognition as a capability that can be benchmarked and improved, which is adjacent to our concern with spatially situated agents.",
        "claim": "The paper targets urban spatial cognition in LLMs and proposes evaluation/training resources around city-space understanding.",
        "evidence": ["Spatial cognition framing for urban LLMs.", "Evidence that city-space knowledge can be treated as a separable evaluation target."],
        "measures": "urban spatial cognition and city knowledge tasks",
        "does_not": "autonomous daily-life rollouts with dynamic goals and social encounters",
        "informs": "Helps separate our benchmark dimensions: spatial cognition is necessary, but not sufficient for believable city agency.",
        "add": "6-city can evaluate whether spatial cognition changes behavior under constraints, not just whether a model answers spatial questions correctly.",
        "use": "CityGPT/CityEval treats urban spatial cognition as a measurable LLM capability; 6-city asks whether that capability supports coherent action in a simulated city.",
        "reason": "Relevant spatial benchmark, but less direct than CityBench or USTBench for our claim.",
    },
    {
        "category": "01_urban_benchmarks",
        "file": "03_STBench_Wang2024",
        "title": "STBench: Assessing the Ability of Large Language Models in Spatio-Temporal Analysis",
        "source": "https://arxiv.org/abs/2406.19065",
        "role": "spatiotemporal reasoning benchmark",
        "decision": "cite",
        "why": "STBench gives us a reference for evaluating spatiotemporal reasoning, which city agents need for scheduling, route choice, opening hours, and event timing.",
        "claim": "The benchmark dissects LLM spatiotemporal capability into multiple categories, including knowledge, reasoning, computation, and downstream tasks.",
        "evidence": ["Task decomposition for spatiotemporal analysis.", "Large QA-style benchmark that can inspire our spatial-temporal probe design."],
        "measures": "spatiotemporal analysis and QA performance",
        "does_not": "agents embedded in a changing city world with action feasibility and state updates",
        "informs": "Reuse its decomposition when designing probes for time windows, route constraints, and schedule conflicts.",
        "add": "6-city can turn spatiotemporal questions into embodied decisions with consequences.",
        "use": "STBench motivates spatiotemporal reasoning as a distinct requirement, while 6-city evaluates how such reasoning affects agent trajectories.",
        "reason": "Useful methods reference for temporal/spatial subskills.",
    },
    {
        "category": "01_urban_benchmarks",
        "file": "04_USTBench_Liu2025",
        "title": "USTBench: Benchmarking and Dissecting Spatiotemporal Reasoning of LLMs as Urban Agents",
        "source": "https://arxiv.org/abs/2505.17572",
        "role": "urban-agent spatiotemporal benchmark",
        "decision": "must-cite",
        "why": "USTBench is one of the closest benchmark references because it explicitly talks about LLMs as urban agents and spatiotemporal reasoning in urban contexts.",
        "claim": "The paper benchmarks and analyzes spatiotemporal reasoning abilities of LLMs in urban-agent tasks.",
        "evidence": ["Direct use of the urban-agent framing.", "Evaluation categories for spatiotemporal reasoning that overlap with city-agent decisions."],
        "measures": "urban-agent reasoning tasks, especially spatiotemporal reasoning",
        "does_not": "SOTOPIA-style private-goal episodes with social and spatial constraints",
        "informs": "Use as a direct closest-neighbor benchmark and clarify whether 6-city is measuring behavior over episodes rather than single reasoning answers.",
        "add": "6-city can add private intentions, environmental perturbations, social relationships, and trace-level scoring.",
        "use": "USTBench brings LLM evaluation into the urban-agent setting; 6-city extends this line toward interactive episodes with verifiable city-state transitions.",
        "reason": "Closest benchmark neighbor for our direction.",
    },
    {
        "category": "01_urban_benchmarks",
        "file": "05_UrbanPlanBench_Luo2025",
        "title": "UrbanPlanBench: A Comprehensive Urban Planning Benchmark for Evaluating Large Language Models",
        "source": "https://arxiv.org/abs/2504.21027",
        "role": "urban planning benchmark",
        "decision": "cite",
        "why": "UrbanPlanBench gives us a contrast class: professional or planning-style urban judgment is not the same as daily-life agent behavior in a city.",
        "claim": "The paper evaluates LLMs on urban planning tasks through a dedicated benchmark.",
        "evidence": ["Planning-oriented benchmark dimensions.", "Useful example of expert-domain urban evaluation."],
        "measures": "urban planning knowledge and reasoning",
        "does_not": "micro-level residents, daily intentions, or socially situated movement",
        "informs": "Helps keep 6-city scoped away from urban-planner benchmarks and toward resident/agent behavior benchmarks.",
        "add": "6-city can evaluate agent-level action under city affordances rather than professional plan quality.",
        "use": "UrbanPlanBench evaluates planning judgment, whereas 6-city targets resident-like agents acting within a city environment.",
        "reason": "Useful contrast, not the central closest neighbor.",
    },
    {
        "category": "01_urban_benchmarks",
        "file": "06_UPBench_Liu2026",
        "title": "Can AI Reason Like an Urban Planner? Benchmarking Large Language Models Against Professional Judgment",
        "source": "https://arxiv.org/abs/2606.11678",
        "role": "urban planner judgment benchmark",
        "decision": "cite",
        "why": "UPBench is another planning-judgment benchmark, useful for contrasting expert urban reasoning with our intended behavioral benchmark.",
        "claim": "The paper benchmarks LLMs against professional urban planning judgment.",
        "evidence": ["Professional-judgment evaluation frame.", "Potential rubric ideas for comparing model outputs against human expert judgments."],
        "measures": "planner-like reasoning and judgment quality",
        "does_not": "daily-life agency, movement traces, or environment-grounded social interaction",
        "informs": "May inspire rubric language, but should not define our core task family.",
        "add": "6-city can evaluate situated behavior rather than professional advice.",
        "use": "Planner benchmarks such as UPBench evaluate expert judgment; our benchmark asks whether agents can live and adapt inside a city world.",
        "reason": "Useful planning contrast; check PDF/source before citing because the extracted abstract has a layout-noise flag.",
    },
    {
        "category": "01_urban_benchmarks",
        "file": "07_UrBench_Liu2024",
        "title": "UrBench: A Comprehensive Benchmark for Evaluating Large Multimodal Models in Multi-View Urban Scenarios",
        "source": "https://arxiv.org/abs/2408.17267",
        "role": "multimodal urban perception benchmark",
        "decision": "cite",
        "why": "UrBench matters if 6-city later adds visual or multi-view observations. It currently helps identify the perception side of urban intelligence.",
        "claim": "The paper builds a multimodal benchmark for evaluating urban scene understanding across multi-view scenarios.",
        "evidence": ["Multi-view urban scenario framing.", "Useful reference for perception-oriented urban benchmarks."],
        "measures": "urban multimodal perception and reasoning",
        "does_not": "long-horizon autonomous agents with private goals and action traces",
        "informs": "If we add visual observation, UrBench can inform perception tasks while SOTOPIA-style episodes handle agency.",
        "add": "6-city can connect perception to decisions and outcomes instead of evaluating perception alone.",
        "use": "UrBench covers multimodal urban perception; 6-city would evaluate how such observations shape city-agent behavior.",
        "reason": "Relevant for the embodied/multimodal branch, with extraction caveat.",
    },
    {
        "category": "01_urban_benchmarks",
        "file": "08_CityEQA_Zhang2025",
        "title": "CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space",
        "source": "https://arxiv.org/abs/2502.12532",
        "role": "embodied city QA benchmark",
        "decision": "must-cite",
        "why": "CityEQA is a direct embodied-city benchmark reference. It makes city-space navigation and question answering concrete.",
        "claim": "The paper presents an embodied question-answering benchmark in city space and a hierarchical LLM-agent approach.",
        "evidence": ["City-space embodied QA setup.", "Hierarchical agent design for navigation and answering."],
        "measures": "question answering grounded in city-space exploration/navigation",
        "does_not": "daily-life private goals, social encounters, or multi-objective city behavior",
        "informs": "Use as a close benchmark for embodied city navigation, then distinguish our resident-intention episode benchmark.",
        "add": "6-city can evaluate whether agents choose and revise actions for their own goals, not only find information for a query.",
        "use": "CityEQA demonstrates city-scale embodied QA; 6-city shifts the task from answering external questions to pursuing internal goals under spatial constraints.",
        "reason": "Closest reference for embodied city benchmark design.",
    },
    {
        "category": "01_urban_benchmarks",
        "file": "09_OpenCity_Ma2024",
        "title": "OpenCity: A Scalable Platform to Simulate Urban Activities with Massive LLM Agents",
        "source": "https://arxiv.org/abs/2410.21286",
        "role": "large-scale urban activity simulation platform",
        "decision": "cite",
        "why": "OpenCity is important because it treats LLM agents at urban scale. It is a systems/platform neighbor to our smaller benchmark idea.",
        "claim": "The paper proposes a scalable platform for simulating urban activities with many LLM agents.",
        "evidence": ["Large-scale urban agent simulation platform.", "System reference for scaling beyond controlled micro-city evaluation."],
        "measures": "urban activities at platform scale, depending on the simulation setup",
        "does_not": "controlled benchmark episodes and falsifiable scoring as the primary target",
        "informs": "Use as a systems neighbor and explain why 6-city starts smaller for controllability and verification.",
        "add": "6-city can trade scale for high-control scenario packages and benchmark-grade evaluation.",
        "use": "OpenCity shows the feasibility of large-scale LLM urban activity simulation; 6-city aims for smaller but more controlled evaluation episodes.",
        "reason": "Important related platform, not necessarily the benchmark template.",
    },
    {
        "category": "01_urban_benchmarks",
        "file": "10_MobileCity_Li2025",
        "title": "MobileCity: An Efficient Framework for Large-Scale Urban Behavior Simulation",
        "source": "https://arxiv.org/abs/2504.16946",
        "role": "efficient urban behavior simulation framework",
        "decision": "cite",
        "why": "MobileCity is useful for thinking about computational efficiency and large-scale urban behavior simulation, especially if our benchmark later scales beyond small scenarios.",
        "claim": "The paper proposes an efficient framework for large-scale urban behavior simulation.",
        "evidence": ["Efficiency/scaling design choices for urban behavior simulation.", "Potential contrast with high-control benchmark episodes."],
        "measures": "large-scale urban behavior simulation performance and outcomes",
        "does_not": "a SOTOPIA-style benchmark for private goals and controlled social-spatial constraints",
        "informs": "Useful later if we turn the benchmark into a scalable harness.",
        "add": "6-city can begin with rigorous small-scale evaluation before optimizing for massive scale.",
        "use": "MobileCity represents the scalable-simulation branch, while 6-city emphasizes verifiable micro-city benchmark episodes.",
        "reason": "Relevant scaling reference.",
    },
    {
        "category": "02_citysim_agents",
        "file": "01_CitySim_Wang2025",
        "title": "CitySim: Modeling Urban Behaviors and City Dynamics with Large-Scale LLM-Driven Agent Simulation",
        "source": "https://arxiv.org/abs/2506.21805",
        "role": "closest CitySim agent simulation neighbor",
        "decision": "must-cite",
        "why": "CitySim is the closest named reference to the direction we are discussing. It directly uses LLM-driven agents for urban behavior and city dynamics.",
        "claim": "The paper models urban behavior and city dynamics through large-scale LLM-driven agent simulation.",
        "evidence": ["LLM-driven city agent simulation design.", "Reference point for needs, schedules, mobility, and city dynamics."],
        "measures": "urban behavior and aggregate city dynamics in simulation",
        "does_not": "benchmark-grade controlled evaluation of agent autonomy, private intentions, and spatial sensitivity as the central product",
        "informs": "Use as closest simulation neighbor; position 6-city as a benchmark harness rather than a city simulator demo.",
        "add": "6-city can focus on resettable scenarios, counterfactual layout changes, private goals, and transparent scoring.",
        "use": "CitySim demonstrates large-scale LLM-driven urban simulation; 6-city asks how such agents should be benchmarked under controlled spatial and social conditions.",
        "reason": "Closest direct neighbor and required related work.",
    },
    {
        "category": "02_citysim_agents",
        "file": "02_GATSim_Liu2025",
        "title": "GATSim: Urban Mobility Simulation with Generative Agents",
        "source": "https://arxiv.org/abs/2506.23306",
        "role": "generative-agent urban mobility simulation",
        "decision": "must-cite",
        "why": "GATSim directly connects generative agents with urban mobility simulation, which overlaps with our concern about agents moving through a city under goals and constraints.",
        "claim": "The paper applies generative agents to urban mobility simulation.",
        "evidence": ["Generative-agent approach to mobility behavior.", "Potential baseline for trajectory and movement realism."],
        "measures": "mobility patterns and simulation outcomes",
        "does_not": "SOTOPIA-style private intentions, social conflict, or controlled counterfactual city layouts",
        "informs": "Use for the mobility branch of related work and for thinking about trajectory metrics.",
        "add": "6-city can add interaction-rich benchmark tasks where movement is only one component of goal pursuit.",
        "use": "GATSim brings generative agents into urban mobility; 6-city treats mobility as part of a broader benchmark of situated city agency.",
        "reason": "Closest mobility-specific neighbor.",
    },
    {
        "category": "02_citysim_agents",
        "file": "03_AgentSociety_Gao2025",
        "title": "AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society",
        "source": "https://arxiv.org/abs/2502.08691",
        "role": "large-scale generative-agent society simulation",
        "decision": "cite",
        "why": "AgentSociety provides broader context for LLM-driven agent societies and population-level simulation, even when not city-specific.",
        "claim": "The paper uses large-scale LLM-driven generative agents to simulate human behaviors and social phenomena.",
        "evidence": ["Large-scale agent-society simulation architecture.", "Reference for population-scale realism claims and evaluation risks."],
        "measures": "behavioral and social simulation outcomes at large scale",
        "does_not": "a controlled city benchmark with spatial layout perturbations and trajectory scoring",
        "informs": "Use as social-simulation background against which city-specific benchmarks can be positioned.",
        "add": "6-city narrows the setting to spatially grounded urban episodes with benchmark constraints.",
        "use": "AgentSociety shows the broader rise of LLM-driven social simulation; 6-city grounds such agents in city-space evaluation.",
        "reason": "Important background for LLM generative-agent societies.",
    },
    {
        "category": "02_citysim_agents",
        "file": "04_Concordia_Vezhnevets2023",
        "title": "Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia",
        "source": "https://arxiv.org/abs/2312.03664",
        "role": "grounded generative-agent framework",
        "decision": "must-cite",
        "why": "Concordia is methodologically important because it treats agent actions as grounded in physical, social, or digital spaces through a configurable environment/game-master structure.",
        "claim": "The framework supports generative agent-based modeling with actions grounded in explicit spaces.",
        "evidence": ["Grounding actions in spaces.", "Game-master/environment framing useful for separating agent intent from world truth."],
        "measures": "simulation behavior depending on configured scenarios and components",
        "does_not": "a city-agent benchmark with fixed task families and scoring rubrics",
        "informs": "Use its architecture idea: LLM chooses intent, environment validates actions, evaluator scores traces.",
        "add": "6-city can specialize this pattern into urban benchmark seeds and spatial counterfactual tests.",
        "use": "Concordia motivates environment-grounded generative agents; 6-city instantiates that idea as a benchmark for city-space agency.",
        "reason": "Core methodological foundation.",
    },
    {
        "category": "02_citysim_agents",
        "file": "05_ChatSUMO_Mao2024",
        "title": "ChatSUMO: Large Language Model for Automating Traffic Scenario Generation in Simulation of Urban Mobility",
        "source": "https://arxiv.org/abs/2409.09040",
        "role": "traffic scenario generation / SUMO reference",
        "decision": "background",
        "why": "ChatSUMO is useful if we include road networks or traffic scenarios, but it is less central to the SOTOPIA-style city-agent benchmark direction.",
        "claim": "The paper uses LLMs to automate traffic scenario generation for urban mobility simulation.",
        "evidence": ["LLM-assisted generation of traffic simulation scenarios.", "SUMO-related workflow reference."],
        "measures": "traffic scenario generation or mobility simulation setup quality",
        "does_not": "autonomous social city agents with private daily goals",
        "informs": "Keep as a background reference for a possible traffic/mobility task family.",
        "add": "6-city would evaluate agents acting inside scenarios, not only generate traffic scenarios.",
        "use": "ChatSUMO is relevant to traffic-simulation tooling, but 6-city targets broader city-agent behavior.",
        "reason": "Useful but peripheral for the current benchmark thesis.",
    },
    {
        "category": "02_citysim_agents",
        "file": "06_UrbanLLM_Zhang2024",
        "title": "UrbanLLM: Autonomous Urban Activity Planning and Management with Large Language Models",
        "source": "https://arxiv.org/abs/2406.12360",
        "role": "urban activity planning with LLMs",
        "decision": "cite",
        "why": "UrbanLLM is relevant because city agents need activity planning, daily scheduling, and management of urban tasks.",
        "claim": "The paper applies LLMs to autonomous urban activity planning and management.",
        "evidence": ["Urban activity planning framing.", "Potential baseline for schedule and activity-generation components."],
        "measures": "planning and management quality for urban activities",
        "does_not": "controlled interactive benchmark episodes with social relationships and spatial perturbations",
        "informs": "Use for the planning component in the benchmark taxonomy.",
        "add": "6-city can test whether planning translates into feasible and adaptive trajectories.",
        "use": "UrbanLLM studies LLM-based urban activity planning; 6-city evaluates planned activity as behavior in a constrained world.",
        "reason": "Relevant component-level reference.",
    },
    {
        "category": "02_citysim_agents",
        "file": "07_TrajAgent_Zhang2024",
        "title": "TrajAgent: An LLM-Agent Framework for Trajectory Modeling via Large-and-Small Model Collaboration",
        "source": "https://arxiv.org/abs/2410.20445",
        "role": "trajectory modeling agent framework",
        "decision": "cite",
        "why": "TrajAgent is useful for trajectory modeling and may inform how we score or generate movement traces in city episodes.",
        "claim": "The paper proposes an LLM-agent framework for trajectory modeling using large-and-small model collaboration.",
        "evidence": ["Trajectory modeling approach.", "Potential design pattern for separating high-level reasoning from efficient low-level modeling."],
        "measures": "trajectory modeling quality",
        "does_not": "social city-agent autonomy or private-goal benchmark scenarios",
        "informs": "Use for trajectory metrics and possible model architecture baselines.",
        "add": "6-city can score trajectories in relation to goals, constraints, and replanning, not only trajectory plausibility.",
        "use": "TrajAgent addresses trajectory modeling; 6-city evaluates trajectories as evidence of situated agency.",
        "reason": "Useful for movement/trace evaluation.",
    },
    {
        "category": "02_citysim_agents",
        "file": "08_Urban_Generative_Intelligence_Li2023",
        "title": "Urban Generative Intelligence (UGI): A Foundational Platform for Agents in Embodied City Environment",
        "source": "https://arxiv.org/abs/2312.11813",
        "role": "embodied-city agent platform foundation",
        "decision": "cite",
        "why": "UGI is an early bridge between generative agents and embodied city environments, useful for framing the embodied-city branch of the field.",
        "claim": "The paper proposes a foundational platform for agents in embodied city environments.",
        "evidence": ["Embodied city environment framing.", "Platform-level view of agents interacting with city spaces."],
        "measures": "platform capabilities and embodied-city agent tasks",
        "does_not": "a compact, controlled benchmark with SOTOPIA-style private goals and scoring dimensions",
        "informs": "Use as background for why city environments are an important embodied-agent setting.",
        "add": "6-city can turn this broad platform vision into tractable benchmark slices.",
        "use": "UGI frames embodied city environments as a foundation for agents; 6-city narrows this into controlled benchmark episodes.",
        "reason": "Good background bridge between city sim and embodied agents.",
    },
    {
        "category": "03_embodied_city",
        "file": "01_EmbodiedCity_Zhou2024",
        "title": "EmbodiedCity: A Benchmark Platform for Embodied Agent in Real-world City Environment",
        "source": "https://arxiv.org/abs/2410.09604",
        "role": "embodied city benchmark platform",
        "decision": "must-cite",
        "why": "EmbodiedCity is a central reference for city-scale embodied agents and real-world city environment benchmarks.",
        "claim": "The paper presents a benchmark platform for embodied agents in real-world city environments.",
        "evidence": ["Embodied city benchmark platform.", "Real-world city environment grounding."],
        "measures": "embodied agent performance in city environments, likely navigation and perception-heavy tasks",
        "does_not": "social/private-goal daily-life episodes in a controllable micro-city",
        "informs": "Use as a must-cite for embodied city benchmark work and as a boundary for our cheaper graph/grid benchmark version.",
        "add": "6-city can begin with weak embodiment and verifiable social-spatial scenarios before moving to visual embodiment.",
        "use": "EmbodiedCity grounds agents in real city environments; 6-city explores a lighter but more controllable benchmark for city agency.",
        "reason": "Core embodied-city benchmark reference.",
    },
    {
        "category": "03_embodied_city",
        "file": "02_UrbanLLaVA_Feng2025",
        "title": "UrbanLLaVA: A Multi-modal Large Language Model for Urban Intelligence with Spatial Reasoning and Understanding",
        "source": "https://arxiv.org/abs/2506.23219",
        "role": "urban multimodal model / spatial reasoning",
        "decision": "cite",
        "why": "UrbanLLaVA matters if our agents later receive image or street-view observations. It is model-side rather than benchmark-episode-side related work.",
        "claim": "The paper proposes a multimodal model for urban intelligence with spatial reasoning and understanding.",
        "evidence": ["Urban multimodal/spatial reasoning model.", "Useful reference for visual observation extensions."],
        "measures": "urban visual/spatial understanding tasks",
        "does_not": "autonomous goal pursuit in a simulated city world",
        "informs": "Use as model-side context for a visual version of 6-city.",
        "add": "6-city can evaluate how urban multimodal understanding affects decisions and trajectories.",
        "use": "UrbanLLaVA advances urban multimodal understanding; 6-city would evaluate whether such understanding supports coherent city-agent behavior.",
        "reason": "Relevant for future multimodal extension.",
    },
    {
        "category": "04_social_benchmark_foundations",
        "file": "01_Generative_Agents_Park2023",
        "title": "Generative Agents: Interactive Simulacra of Human Behavior",
        "source": "https://arxiv.org/abs/2304.03442",
        "role": "generative-agent foundation",
        "decision": "must-cite",
        "why": "Generative Agents is the foundation for believable LLM agents with memory, reflection, planning, and daily behavior in a simulated town.",
        "claim": "The paper shows that LLM agents with memory, reflection, and planning can produce believable interactive behavior in a sandbox environment.",
        "evidence": ["Memory-reflection-planning architecture.", "Small-town simulation as the ancestor of city-agent demos."],
        "measures": "believability and behavioral coherence in an interactive agent sandbox",
        "does_not": "a benchmark with controlled city layouts, private goal scoring, counterfactual perturbations, and standardized evaluation across models",
        "informs": "Use as the historical foundation, then argue that the next step is benchmark-grade evaluation of spatial agency.",
        "add": "6-city can turn the sandbox intuition into resettable scenarios with measurable autonomy, feasibility, and adaptation.",
        "use": "Generative Agents established the memory-planning architecture for believable agents; 6-city asks how such agents should be evaluated when they inhabit a city environment.",
        "reason": "Foundational prior for all generative-agent city work.",
    },
    {
        "category": "04_social_benchmark_foundations",
        "file": "02_SOTOPIA_Zhou2024_ICLR",
        "title": "SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents",
        "source": "https://openreview.net/forum?id=mM7VurbA4r",
        "role": "interactive social-agent benchmark foundation",
        "decision": "must-cite",
        "why": "SOTOPIA is the benchmark pattern we want to adapt: scenarios, private goals, characters, interaction traces, and evaluator dimensions.",
        "claim": "The paper proposes an interactive benchmark for social intelligence in language agents, using goal-driven social scenarios and evaluators.",
        "evidence": ["Scenario plus private-goal episode design.", "Evaluation dimensions for social interaction quality."],
        "measures": "social intelligence through interactive episodes and evaluator judgments",
        "does_not": "a spatial/city benchmark, because its constraints are social rather than urban-geometric",
        "informs": "Use its episode structure as the direct template for a SOTOPIA-City benchmark.",
        "add": "6-city can add maps, POIs, travel costs, opening hours, spatial counterfactuals, and trajectory validators to the SOTOPIA setup.",
        "use": "SOTOPIA provides the interactive evaluation pattern; 6-city spatializes that pattern into city-agent scenarios with verifiable movement and environmental constraints.",
        "reason": "Core benchmark-method foundation.",
    },
    {
        "category": "04_social_benchmark_foundations",
        "file": "03_AgentSense_2024",
        "title": "AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios",
        "source": "https://arxiv.org/abs/2410.19346",
        "role": "diverse interactive social-agent benchmark",
        "decision": "must-cite",
        "why": "AgentSense is a close social-benchmark neighbor because it tests goal pursuit and implicit reasoning across 1,225 interactive scenarios rather than relying on a small set of hand-written conversations.",
        "claim": "The paper constructs diverse multi-turn social scenarios from scripts and evaluates language agents on explicit goal completion and implicit social reasoning.",
        "evidence": ["Large, theory-grounded interactive scenario construction pipeline.", "Separate attention to goal completion, private information, and implicit reasoning."],
        "measures": "social goal achievement and implicit reasoning in multi-turn interactions",
        "does_not": "spatially grounded execution, travel feasibility, city-state transitions, or continuous mobility traces",
        "informs": "Reuse its scenario-diversity discipline and separate observable goal completion from latent social reasoning.",
        "add": "CityAgency can embed similarly diverse private goals in a city world where actions also have spatial, temporal, and resource consequences.",
        "use": "AgentSense broadens social-agent evaluation across diverse interactive scenarios; CityAgency adds executable urban state and trajectory validation to that episode structure.",
        "reason": "Close benchmark reference for private goals, scenario diversity, and social reasoning.",
    },
    {
        "category": "04_social_benchmark_foundations",
        "file": "04_Lifelong_SOTOPIA_2025",
        "title": "Lifelong-SOTOPIA: Evaluating Social Intelligence of Language Agents Over Lifelong Social Interactions",
        "source": "https://arxiv.org/abs/2506.12666",
        "role": "longitudinal social-agent benchmark",
        "decision": "cite",
        "why": "Lifelong-SOTOPIA shows that agent quality can degrade across episodes and that memory must be evaluated through later behavior, not only by inspecting stored summaries.",
        "claim": "The benchmark extends social-agent evaluation to linked multi-episode interactions that require agents to recover and use interaction history.",
        "evidence": ["Multi-episode evaluation with persistent character histories.", "Goal achievement and believability tracked over prolonged interaction."],
        "measures": "longitudinal social goal achievement, believability, and use of interaction history",
        "does_not": "persistent urban routines, spatial memories, or the feasibility of physical action over time",
        "informs": "Use linked episodes later to test whether agents remember places, people, obligations, and prior disruptions.",
        "add": "CityAgency can extend lifelong evaluation from social memory to spatial and commitment memory in a changing city.",
        "use": "Lifelong-SOTOPIA tests social intelligence across linked episodes; CityAgency can apply this principle to persistent urban commitments and spatial histories.",
        "reason": "Important extension path after the single-episode benchmark is stable.",
    },
    {
        "category": "04_social_benchmark_foundations",
        "file": "05_Misleading_Success_2024",
        "title": "Is This the Real Life? Is This Just Fantasy? The Misleading Success of Simulating Social Interactions With LLMs",
        "source": "https://arxiv.org/abs/2403.05020",
        "role": "information-asymmetry realism critique",
        "decision": "must-cite",
        "why": "This paper is a methodological warning for CityAgency: agents can look successful when the simulator grants them omniscient information that real people would not possess.",
        "claim": "The paper compares omniscient and non-omniscient social simulations and finds that apparent agent success falls under realistic information asymmetry.",
        "evidence": ["Controlled comparison of omniscient and information-asymmetric settings.", "Demonstration that simulator information design can inflate social-agent performance."],
        "measures": "social interaction performance under different information-access assumptions",
        "does_not": "physical observability, map knowledge, local sensing, or trace feasibility in a city",
        "informs": "Give each city agent an explicit observation boundary and keep hidden world state outside the prompt.",
        "add": "CityAgency can test whether plans remain valid when agents must discover closures, delays, and other agents' intentions through permitted observations.",
        "use": "Information-asymmetry studies warn that omniscient simulation can produce misleading success; CityAgency therefore separates agent observations from authoritative world state.",
        "reason": "Central validity reference for avoiding an unrealistically omniscient city benchmark.",
    },
    {
        "category": "04_social_benchmark_foundations",
        "file": "06_Can_LLM_Agents_Simulate_Multi_Turn_Human_Behavior_2025",
        "title": "Can LLM Agents Simulate Multi-Turn Human Behavior? Evidence from Real Online Customer Behavior Data",
        "source": "https://arxiv.org/abs/2503.20749",
        "role": "empirical step-by-step behavior benchmark",
        "decision": "must-cite",
        "why": "The paper directly challenges qualitative believability as evidence of human-like behavior and evaluates step-by-step actions against large-scale observed human traces.",
        "claim": "Using real online shopping sessions, the paper finds a substantial gap between plausible generated behavior and accurate next-action simulation.",
        "evidence": ["Action-level comparison against 31,865 real multi-turn sessions.", "Separation of qualitative believability from quantitative behavioral accuracy."],
        "measures": "next-action accuracy and final-outcome prediction against observed human traces",
        "does_not": "physical mobility, city constraints, or open-ended goal adaptation in an urban environment",
        "informs": "Keep trace-level behavioral validity distinct from judge-rated plausibility and add human data when available.",
        "add": "CityAgency can diagnose impossible or incoherent urban traces even before a large human-trajectory comparison dataset is available.",
        "use": "Empirical multi-turn studies show that believable narratives need not reproduce human action sequences; CityAgency tests the same gap in urban execution.",
        "reason": "Strong empirical support for the plausible-plan versus credible-trace story.",
    },
    {
        "category": "05_mobility_realism",
        "file": "01_MobiSim_Bench_Zhang2026_OpenReview",
        "title": "MobiSim-Bench: A Multi-Perspective Benchmark for Evaluating LLM-Agent-Based Human Mobility Simulation",
        "source": "https://openreview.net/forum?id=3QFvAXuNl7",
        "role": "closest mobility-simulation benchmark",
        "decision": "must-cite",
        "why": "MobiSim-Bench is the strongest direct benchmark neighbor because it evaluates LLM-agent mobility from robustness, realism, and responsiveness perspectives in both daily and extraordinary conditions.",
        "claim": "The benchmark evaluates human mobility simulation through complementary daily-mobility and hurricane-response settings using micro- and macro-level measurements.",
        "evidence": ["Three-part robustness, realism, and responsiveness framework.", "Daily and disruptive mobility scenarios implemented on an agent-society simulator."],
        "measures": "aggregate mobility realism, run robustness, and behavioral response to environmental disruption",
        "does_not": "fine-grained proof that an individual agent completed private goals through a valid continuous trace",
        "informs": "Use it as the macro-level benchmark anchor and make CityAgency's individual execution diagnostics explicit.",
        "add": "CityAgency can explain why a trajectory fails by checking goal evidence, world-state transitions, impossible movement, false continuation, and replanning decisions.",
        "use": "MobiSim-Bench evaluates whether populations reproduce robust and responsive mobility; CityAgency diagnoses whether individual agents execute intentions as valid city traces.",
        "reason": "Closest benchmark competitor and essential positioning reference.",
    },
    {
        "category": "05_mobility_realism",
        "file": "02_When_Plausible_Is_Not_Realistic_Santos2026",
        "title": "When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Simulation",
        "source": "https://arxiv.org/abs/2606.13835",
        "role": "empirical urban-mobility realism critique",
        "decision": "must-cite",
        "why": "This work provides direct evidence for our motivating gap: coherent mobility narratives can still violate empirical spatial, temporal, and transition patterns.",
        "claim": "The paper validates AgentSociety and CitySim against real mobility data and reports substantial discrepancies across mobility laws, rhythms, motifs, transitions, and profiles.",
        "evidence": ["Multi-dimensional comparison with mobility data from Greater Paris and Shanghai.", "Explicit separation between narrative plausibility and empirical mobility realism."],
        "measures": "population-level spatial, temporal, network, semantic, and profile realism",
        "does_not": "attribute failure to an individual agent's planning, action validity, goal maintenance, or recovery decisions",
        "informs": "Connect micro-level execution failures to downstream macro-level mobility distortions without claiming to replace empirical realism validation.",
        "add": "CityAgency supplies controlled causal probes beneath macro statistics, showing which agent behaviors produce implausible aggregate traces.",
        "use": "Empirical validation reveals that plausible urban narratives need not yield realistic mobility; CityAgency studies the individual execution failures beneath that discrepancy.",
        "reason": "Direct support for the paper title and the micro-versus-macro benchmark distinction.",
    },
    {
        "category": "06_agent_execution_benchmarks",
        "file": "01_ChinaTravel_Shao2024",
        "title": "ChinaTravel: An Open-Ended Travel Planning Benchmark with Compositional Constraint Validation for Language Agents",
        "source": "https://arxiv.org/abs/2412.13682",
        "role": "compositional travel-plan feasibility benchmark",
        "decision": "must-cite",
        "why": "ChinaTravel is a close feasibility neighbor because it translates open-ended travel requirements into compositional constraints that can be checked automatically.",
        "claim": "The benchmark combines a multi-day travel sandbox, a constraint DSL, human-authored requirements, and programmatic feasibility and preference validation.",
        "evidence": ["Domain-specific language for compositional constraint validation.", "Open-ended multi-POI plans with explicit and implicit human requirements."],
        "measures": "plan feasibility, constraint satisfaction, and preference quality",
        "does_not": "stepwise execution in a changing city, social encounters, or stateful replanning after disturbances",
        "informs": "Represent CityAgency goals and hard constraints as executable predicates instead of relying on free-form judge scores.",
        "add": "CityAgency can move from validating a proposed itinerary to validating every action and resulting world state during execution.",
        "use": "ChinaTravel demonstrates compositional validation of open-ended travel plans; CityAgency extends validation from plans to stateful urban execution traces.",
        "reason": "Closest planning-feasibility precedent for deterministic urban validators.",
    },
    {
        "category": "06_agent_execution_benchmarks",
        "file": "02_FeasiGen_Do_Agents_Know_What_They_Cant_Do_2026",
        "title": "Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents",
        "source": "https://arxiv.org/abs/2605.28532",
        "role": "agent infeasibility-awareness benchmark",
        "decision": "must-cite",
        "why": "FeasiGen isolates whether agents recognize that a task has become impossible and stop, a central failure mode when city resources, routes, or time windows disappear.",
        "claim": "The paper generates infeasible tasks by masking critical tools and evaluates whether agents detect infeasibility instead of continuing unproductively.",
        "evidence": ["Automatic construction of infeasible variants from successful tool traces.", "False-continue-style metrics for feasibility awareness."],
        "measures": "infeasibility detection, appropriate stopping, and wasted execution under missing capabilities",
        "does_not": "graded spatial feasibility or recovery through alternative routes, places, and social coordination",
        "informs": "Include paired feasible and infeasible city scenarios and report false continuation separately from task failure.",
        "add": "CityAgency can distinguish stop, repair, substitute, and impossible physical continuation under urban disruptions.",
        "use": "FeasiGen tests whether tool agents know when execution is impossible; CityAgency brings feasibility awareness into spatially and temporally constrained city worlds.",
        "reason": "Direct source for the false-continue metric and infeasible-scenario design.",
    },
    {
        "category": "06_agent_execution_benchmarks",
        "file": "03_tau_bench_Yao2024",
        "title": "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains",
        "source": "https://arxiv.org/abs/2406.12045",
        "role": "state-based interactive-agent benchmark",
        "decision": "must-cite",
        "why": "tau-bench provides two crucial design precedents: evaluate final environment state rather than verbal claims, and measure reliability over repeated executions.",
        "claim": "The benchmark evaluates agents interacting with simulated users and domain APIs by comparing the resulting database state with an annotated goal state.",
        "evidence": ["Authoritative state-based task evaluation.", "The pass^k metric for repeated-run behavioral reliability."],
        "measures": "goal-state correctness, policy compliance, and consistency over repeated trials",
        "does_not": "continuous space, travel time, embodied observations, or human-like urban traces",
        "informs": "Use world-state predicates for goal completion and repeated seeds for reliability instead of trusting self-reported success.",
        "add": "CityAgency can add trace continuity and intermediate-state validity, because the path to a city goal matters as well as the final state.",
        "use": "tau-bench validates agents against authoritative goal states and repeated trials; CityAgency extends this principle to continuous urban trajectories.",
        "reason": "Core methodological precedent for proof-carrying traces and repeated reliability.",
    },
    {
        "category": "06_agent_execution_benchmarks",
        "file": "04_AppWorld_Trivedi2024",
        "title": "AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents",
        "source": "https://arxiv.org/abs/2407.18901",
        "role": "executable world with programmatic state tests",
        "decision": "cite",
        "why": "AppWorld demonstrates how a rich simulated world can support multiple valid solution paths while still testing intended outcomes and unintended side effects programmatically.",
        "claim": "The work builds an executable multi-app environment and evaluates complex agent tasks with state-based unit tests, including checks for collateral damage.",
        "evidence": ["Programmatic evaluation over a large executable state space.", "Outcome tests that allow alternative solutions and detect unintended changes."],
        "measures": "functional task completion and collateral state changes",
        "does_not": "spatial continuity, mobility realism, or socially believable city behavior",
        "informs": "Write verifier tests over world-state deltas and permit any route that satisfies goals without invalid side effects.",
        "add": "CityAgency can adapt collateral-damage checks to missed commitments, overspending, invalid occupancy, and disruption of other agents.",
        "use": "AppWorld shows how open-ended agent behavior can be judged by executable state tests; CityAgency applies that pattern to urban worlds and traces.",
        "reason": "Strong engineering precedent for deterministic outcome and side-effect validation.",
    },
    {
        "category": "06_agent_execution_benchmarks",
        "file": "05_WebArena_Zhou2023",
        "title": "WebArena: A Realistic Web Environment for Building Autonomous Agents",
        "source": "https://arxiv.org/abs/2307.13854",
        "role": "reproducible long-horizon environment benchmark",
        "decision": "cite",
        "why": "WebArena is a mature example of evaluating agents in a realistic, resettable environment with long-horizon tasks and functional correctness checks.",
        "claim": "The benchmark provides reproducible functional websites and human-like tasks for evaluating language-guided autonomous web agents end to end.",
        "evidence": ["Self-hosted, resettable environment with realistic task domains.", "Functional task correctness rather than textual answer similarity."],
        "measures": "end-to-end functional success in long-horizon web tasks",
        "does_not": "private autonomous goals, physical travel, or trajectory believability",
        "informs": "Package city scenarios as resettable world snapshots with reproducible initial and goal states.",
        "add": "CityAgency can evaluate both functional completion and whether the intervening physical trace is possible and credible.",
        "use": "WebArena established resettable functional environments for agent evaluation; CityAgency transfers that rigor to urban action and movement.",
        "reason": "Useful benchmark-infrastructure and end-to-end evaluation precedent.",
    },
    {
        "category": "06_agent_execution_benchmarks",
        "file": "06_TheAgentCompany_Xu2024",
        "title": "TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks",
        "source": "https://arxiv.org/abs/2412.14161",
        "role": "consequential long-horizon agent benchmark",
        "decision": "cite",
        "why": "TheAgentCompany broadens executable evaluation to consequential workplace tasks involving tools, communication, and persistent organizational state.",
        "claim": "The benchmark creates a self-contained software-company environment in which agents complete realistic professional tasks across web, code, programs, and coworker communication.",
        "evidence": ["Consequential tasks spanning multiple tools and coworkers.", "Persistent environment where agent actions modify shared state."],
        "measures": "completion of long-horizon professional tasks in a stateful environment",
        "does_not": "physical city movement, resident routines, or empirical mobility realism",
        "informs": "Design city tasks whose actions affect later obligations and other agents rather than isolated one-shot navigation goals.",
        "add": "CityAgency can make consequences spatial and temporal, including missed meetings, unavailable resources, and downstream schedule failures.",
        "use": "TheAgentCompany evaluates consequential action in a persistent digital workplace; CityAgency studies analogous consequences in an urban world.",
        "reason": "Relevant long-horizon comparison for stateful, socially consequential execution.",
    },
]


def wrap(text: str) -> str:
    return fill(text.strip(), width=88)


def yaml_value(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def list_yaml(values: list[str]) -> str:
    return "[" + ", ".join(json.dumps(v, ensure_ascii=False) for v in values) + "]"


def abstract_snapshot(meta_path: Path, max_chars: int = 1200) -> str:
    if not meta_path.exists():
        return "[abstract unavailable]"
    meta = json.loads(meta_path.read_text(encoding="utf-8-sig"))
    abstract = (meta.get("abstract") or "").strip()
    if not abstract:
        return "[abstract not detected]"
    abstract = re.sub(r"\s+", " ", abstract)
    if len(abstract) <= max_chars:
        return abstract
    cut = abstract[:max_chars]
    sentence_end = max(cut.rfind(". "), cut.rfind("? "), cut.rfind("! "))
    if sentence_end > 400:
        return cut[: sentence_end + 1]
    return cut.rstrip() + "..."


def note_content(p: dict) -> str:
    pdf = f"assets/papers/pdf/{p['category']}/{p['file']}.pdf"
    fulltext = f"assets/papers/fulltext/{p['category']}/{p['file']}.fulltext.md"
    meta_path = ROOT / f"assets/papers/fulltext/{p['category']}/{p['file']}.meta.json"
    flags = []
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8-sig"))
        flags = meta.get("quality_flags") or []
    evidence = "\n".join(f"- {item}" for item in p["evidence"])
    caveat = "Extraction issues: " + (", ".join(flags) if flags else "none flagged by converter") + "."
    return f"""---
canonical: true
title: {yaml_value(p['title'])}
category: {p['category']}
role: {yaml_value(p['role'])}
decision: {p['decision']}
source: {yaml_value(p['source'])}
pdf: {yaml_value(pdf)}
fulltext: {yaml_value(fulltext)}
quality_flags: {list_yaml(flags)}
note_status: first_pass
---

# {p['title']}

## Why This Paper Matters For 6-city

{wrap(p['why'])}

## Core Claim / Contribution

{wrap(p['claim'])}

## Evidence We May Cite

{evidence}

## City Benchmark Bridge

- What it already measures: {p['measures']}.
- What it does not measure: {p['does_not']}.
- How it informs our SOTOPIA-style city benchmark: {p['informs']}

## What We Add Beyond This Paper

{wrap(p['add'])}

## Draft-Ready Use Sentence

> {p['use']}

## Caveats / Follow-Up

- {caveat}
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `{p['decision']}`

Reason: {p['reason']}

## Extracted Abstract Snapshot

{abstract_snapshot(meta_path)}
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate existing notes instead of only creating missing notes.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    rows = []
    written = 0
    preserved = 0
    for paper in PAPERS:
        note_dir = NOTES_ROOT / paper["category"]
        note_dir.mkdir(parents=True, exist_ok=True)
        note_path = note_dir / f"{paper['file']}.md"
        if args.force or not note_path.exists():
            note_path.write_text(note_content(paper), encoding="utf-8")
            written += 1
        else:
            preserved += 1
        rows.append(
            {
                "category": paper["category"],
                "title": paper["title"],
                "decision": paper["decision"],
                "role": paper["role"],
                "note": note_path.relative_to(ROOT).as_posix(),
                "fulltext": f"assets/papers/fulltext/{paper['category']}/{paper['file']}.fulltext.md",
            }
        )

    index_lines = [
        "# 6-city Paper Notes Index",
        "",
        "> Status: first-pass notes generated from converted fulltext and project literature map.",
        "> Next step: promote the must-cite papers to `reviewed` after manual PDF checks.",
        "",
        "## Decision Summary",
        "",
    ]
    for decision in ["must-cite", "cite", "background", "maybe", "replace", "exclude"]:
        count = sum(1 for row in rows if row["decision"] == decision)
        if count:
            index_lines.append(f"- `{decision}`: {count}")
    index_lines.extend(
        [
            "",
            "## Notes",
            "",
            "| Category | Decision | Paper | Role | Note | Fulltext |",
            "|---|---|---|---|---|---|",
        ]
    )
    for row in rows:
        title = row["title"].replace("|", "\\|")
        role = row["role"].replace("|", "\\|")
        index_lines.append(
            f"| `{row['category']}` | `{row['decision']}` | {title} | {role} | "
            f"`{row['note']}` | `{row['fulltext']}` |"
        )
    (NOTES_ROOT / "INDEX.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(
        f"Indexed {len(rows)} notes; wrote {written}, preserved {preserved}, "
        "and refreshed INDEX.md"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

