#!/usr/bin/env python3
"""Generate first-pass reading notes for the 6-city paper archive."""

from __future__ import annotations

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


def main() -> int:
    rows = []
    for paper in PAPERS:
        note_dir = NOTES_ROOT / paper["category"]
        note_dir.mkdir(parents=True, exist_ok=True)
        note_path = note_dir / f"{paper['file']}.md"
        note_path.write_text(note_content(paper), encoding="utf-8")
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
    print(f"Wrote {len(rows)} notes and INDEX.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

