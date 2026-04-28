# Feasibility

Draft status: scaffold aligned to the widened-Core baseline dated 2026-04-28.

This section asks a narrower question than the overall survey question. It does not ask whether richer spatial representation has already been shown to shape LLM-agent social behavior. It asks whether current models and adjacent systems provide enough evidence to treat richer spatial input, including configurational input, as technically plausible for future social-simulation research.

The safe conclusion of this section should be about `input-side feasibility`, not about `behavior-side validation`.

## 4.1 Spatial Reasoning Benchmarks as Feasibility Evidence

The first source of feasibility evidence comes from `Adjacent` work on spatial reasoning benchmarks and spatially aware LLM systems. This literature is useful because it probes whether current models can process at least some kinds of topological, relational, or geometry-sensitive input. It is not useful because it proves downstream social effects. The key argumentative move in this subsection is therefore conditional: if models can process some structured spatial information under benchmark or controlled agent settings, then richer spatial representation is at least a live design option for future social-simulation systems.

The subsection should synthesize the benchmark story at a high level rather than cataloguing every task family. The important distinction is between tasks that require simple spatial language matching and tasks that require maintaining structured relations across objects, places, routes, or viewpoints. The closer a benchmark comes to relational structure maintenance, the more relevant it becomes for the survey's feasibility question. Even there, however, benchmark success should be described as suggestive rather than decisive, because these tasks are still far from long-horizon multi-agent social simulation.

Drafting note:

- Use the adjacent benchmark literature to justify plausibility, not accomplishment.
- Keep the language conditional: `suggests`, `may support`, `is consistent with`.
- Do not treat benchmark accuracy as evidence of socially meaningful spatial mediation.

## 4.2 Topological Structure vs Geometry vs Configuration

Feasibility depends on distinguishing several different kinds of spatial input that are often collapsed together in casual discussion. Some systems process named places or semantic scene descriptions. Some handle local adjacency or co-presence relations. Some incorporate geometry, coordinates, or embodied visual context. Configurational input, however, is narrower: it refers to global abstract structure that summarizes how a broader environment is organized beyond only the next local step.

This subsection should make explicit why those distinctions matter. A model that can interpret scene descriptions is not automatically shown to reason over layout-wide structure. A model that operates in a 3D environment is not automatically shown to use geometry in the strong, agent-facing sense relevant to `L5`. And a system that uses route or graph context is not automatically shown to operate over `L4`-style global abstract structure. The point is not to deny feasibility, but to avoid claiming the wrong kind of feasibility for the wrong kind of input.

The clean argumentative progression is:

1. semantic and local relational input are already common enough to count as feasible design primitives;
2. geometry-bearing interfaces are present, though still limited and heterogeneous;
3. configurational/global abstract input remains the least demonstrated category, but it is no longer outside the imaginable design space.

## 4.3 Pattern Matching vs World-Structured Reasoning

The second caution in the feasibility argument concerns interpretation. Even if a model performs well on structured spatial tasks or within spatially situated agents, this does not tell us by itself whether the model is building stable internal structure, exploiting shallow lexical regularities, or relying on task-specific shortcuts. For the survey, this uncertainty is not a side issue; it is part of the feasibility story itself.

This subsection should therefore separate two claims. The weaker claim is that current models may be able to consume richer spatial inputs if those inputs are presented in a stable, legible format. The stronger claim would be that models robustly reason over such inputs in a way that could support configurationally mediated social behavior. The first claim is supportable here. The second is not yet supportable from the current evidence base.

Safe synthesis sentences for this subsection:

- current evidence is consistent with partial structured-input feasibility;
- it remains unclear whether benchmark or agent performance reflects robust world-structured reasoning rather than shallow task adaptation;
- this uncertainty strengthens the need for explicit controls in later evaluation.

## 4.4 Existing Spatially Aware Agents and Embodied Bridge Systems

Beyond benchmarks, the feasibility story is strengthened by a small but meaningful set of adjacent and bridge systems that already expose more structured spatial inputs. These include embodied or geometry-bearing cases, spatially aware human-agent interaction systems, and socially situated VR/NPC environments. Their importance is not that they resolve the social-effect question. Their importance is that they show multiple implementation routes by which spatial structure can be exposed to an agent.

The discussion here should connect directly to the representation gap identified in Section 3. Some systems demonstrate that geometry-bearing input can be delivered at the interface. Others show that scene-level, proximity-level, or role-play-level spatial context can be incorporated into interaction. Still others suggest that global or network-level structure can be surfaced in a limited bridge form. Together, these cases make it difficult to argue that richer spatial input is technically impossible. What remains open is not whether such input can be provided at all, but how much of it is stable, interpretable, and behaviorally meaningful in multi-agent social settings.

Drafting note:

- Mention that much of the strongest feasibility evidence comes from `Adjacent` or `bridge_core`, not from the strict anchor nucleus.
- Keep that evidential asymmetry visible.
- Do not let bridge or adjacent cases silently become direct Core social-effect evidence.

## 4.5 Feasibility Assessment for Configurational Input

The overall conclusion of this section should be cautious but positive. Richer spatial input is technically plausible. Geometry-bearing input is already implemented in a limited set of systems. Local and mid-structure representations are clearly feasible. Agent-facing global abstract structure remains the weakest category, but the widened evidence map and adjacent literature together indicate that it should be treated as an open design frontier rather than as an implausible one.

What this section cannot conclude is equally important. It cannot conclude that models already understand configurational input robustly. It cannot conclude that richer spatial input already improves social simulation in a stable way. And it cannot conclude that the presence of embodied or 3D systems solves the representation problem by itself. The real contribution of the feasibility argument is narrower: it licenses the research agenda to move from "can we even provide this kind of input?" to "how should we provide it, and how would we know whether it matters?"

Safe synthesis sentences for this section:

- current evidence is consistent with the technical feasibility of richer spatial input;
- configurational input remains the least demonstrated but still plausible design layer;
- feasibility should be treated as a necessary precondition, not as proof of spatially mediated social behavior.

Do not write here:

- that models already solve configurational reasoning;
- that embodied or 3D systems validate the survey's downstream social-effect claims;
- that feasibility evidence is equivalent to social-simulation evidence.
