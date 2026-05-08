# Space Syntax Primer

Draft status: paragraph-level draft aligned to the current claim matrix and the 2026-05-01 closure baseline.

This section provides only the Space Syntax concepts needed for the rest of the survey. Its role is not to reteach the whole Space Syntax literature, but to give AI and multi-agent-systems readers a precise vocabulary for configuration, movement opportunity, encounter structure, and claim boundaries. The section should be read as a theoretical bridge: physical-space findings motivate hypotheses for LLM-agent systems, but they are not direct evidence about current LLM-agent social behavior.

[Table 5 about here: Space Syntax measure primer; draft asset: `paper/tables/table_5_space_syntax_measure_primer.md`]

[Figure 5 about here: local-to-global claim-boundary graph; draft assets: `paper/figures/figure_5_local_vs_global_configuration.svg`, `paper/figures/gpt_image_2/figure_5_local_global_claim_boundary_gpt_image_2_v3.png`]

## 2.1 Why Configuration Matters Here

The key idea this survey borrows from Space Syntax is that spatial behavior is shaped not only by individual places, but by the way places are configured in relation to the whole layout. A room, street, corridor, plaza, or virtual location does not have only local properties. It also has a position in a wider system of possible movement, visibility, access, and encounter. That whole-layout position can affect who passes through, who meets whom, where activity concentrates, and where withdrawal or privacy becomes easier.

This is directly relevant to LLM-agent social simulation because many current systems place agents in environments but expose only a partial spatial interface to them. A system may contain a map, a 3D world, or a graph backend while giving the agent only a place name, a scene description, a nearby-agent list, or a set of local movement options. Space Syntax helps articulate what is missing from such interfaces: configuration-wide structure that summarizes how a location sits within the broader environment.

The transfer boundary is essential. Space Syntax findings in physical environments can motivate hypotheses about movement, co-presence, encounter probability, access asymmetry, privacy, and route choice. They do not by themselves show that LLM-agent societies are already configuration-mediated. For that claim to be testable, the relevant structure must be exposed to the agent and linked to reported behavior under an appropriate comparison.

## 2.2 Measures the Reader Needs

The rest of the survey uses a small set of Space Syntax concepts. `Integration` describes how accessible a location is relative to the whole layout. Highly integrated locations are easier to reach from many other locations and are often hypothesized to support movement concentration, publicness, and encounter opportunity. In an LLM-agent system, an integration-based claim would require agents to receive a layout-wide accessibility cue, a derived rank, or geometry from which such a relation can be meaningfully used under controlled conditions.

`Depth` describes how many steps or transitions separate one location from others. A deeper location is more segregated from the rest of the layout. In the context of LLM-agent systems, depth-related hypotheses would concern privacy, withdrawal, selective interaction, or reduced incidental contact. A local place label or immediate neighbor list is not enough to support a depth-based claim unless the broader structure is agent-facing.

`Control` describes how much a location mediates access between its neighbors and the surrounding structure. In social terms, control can motivate hypotheses about monitoring, guarding, brokerage, chokepoints, and constrained route choice. For this survey, the important point is not the formula but the interface requirement: a researcher-side control calculation does not count as agent-accessible `L4` unless the agent receives or can use that mediation information.

`Choice` describes how often a location lies on plausible paths between other locations; it is related to path betweenness. Choice is useful for thinking about route allocation, incidental co-presence, and flow concentration. Again, mobility in a rich environment is not itself evidence of choice-based social mediation. The agent must receive route alternatives, path-structure cues, or embodied geometry in a design where those cues can be isolated.

Finally, visibility or openness describes what can be seen or perceived from a location, including line-of-sight, field-of-view, occlusion, or observable zones. This concept may enter an LLM-agent system as `L5` visual or embodied input, or as a more symbolic structured cue, depending on what the agent consumes. The level is not determined by the existence of a visual engine. It is determined by the agent-facing interface.

Table 5 summarizes these concepts in the terms used by this survey. The table deliberately includes a claim-boundary column because each measure can easily be overclaimed. The measures are useful because they define testable representational targets. They do not convert physical-space evidence into direct evidence about LLM-agent social behavior.

## 2.3 Local Adjacency Is Not Global Configuration

The most important distinction for the evidence map is the difference between local adjacency and global configuration. Two locations can expose the same local relation to an agent while occupying different positions in the whole environment. For example, both locations may have two immediate neighbors. If the agent receives only those immediate neighbors, the two locations can look equivalent from the agent's perspective. Yet one may be near a main spine, shallow in the broader layout, or positioned along many likely routes, while the other may sit deeper in a side branch.

This distinction is why the survey separates `L3` from `L4`. `L3` captures local relations: adjacency, co-presence, nearby agents, local movement options, and local graph exposure. These are important because they structure immediate interaction opportunities. But `L3` does not automatically provide whole-layout position. Claims about depth, integration, control, or choice require additional information about the broader configuration.

Figure 5 visualizes this claim boundary. Panel A shows local views that can look equivalent. Panel B reveals their different whole-layout positions. Panel C states the resulting inference rule: local opportunity or co-presence claims can often be discussed at `L3`, but configuration-wide claims require `L4` or controlled geometry-bearing `L5`. This is an explanatory diagram, not evidence from a coded system.

The implication is methodological. If a paper reports that agents move, meet, or coordinate in a spatial environment, the review still asks what spatial structure the agent received. A global layout may exist in the simulator. A researcher may compute graph metrics after the fact. Neither condition is enough for a configurational agent-facing claim unless the relevant structure was part of the agent's decision interface.

## 2.4 Transfer Boundary for the Survey

Space Syntax enters this survey as a source of transferable propositions and missing representation layers. It supplies a vocabulary for asking whether accessibility, segregation, mediation, route structure, or visibility could affect LLM-agent movement and interaction if such structure were exposed to agents. It does not supply direct validation of current LLM-agent systems.

This boundary shapes the rest of the paper. In Section 3, the evidence map asks whether current systems expose the relevant structures. The answer is mostly no for `L4`: agent-facing global abstract structure is absent from the strict anchor core and appears only once in the stable widened Core, as a digital-network bridge case rather than a physical-layout validation case. In Section 5, Space Syntax propositions are therefore treated as hypotheses for future social-simulation research, not as conclusions already supported by the LLM-agent corpus. In Section 6, the same distinction becomes an evaluation requirement: stronger spatial-behavior claims require matched controls over what agents receive.

The practical rule is the same throughout the survey. If a system exposes only labels, semantic scene descriptions, or local co-presence, then configuration-level claims remain untested no matter how rich the backend world may be. If a system exposes global abstract structure, geometry, or embodied perception to agents, then stronger spatial hypotheses become testable, but still require observed behavioral evidence and appropriate controls before mechanism language is justified.
