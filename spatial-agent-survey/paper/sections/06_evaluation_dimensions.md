# Evaluation Dimensions

Draft status: scaffold aligned to the widened-Core baseline dated 2026-04-28.

This section asks what would count as credible evidence for spatially mediated social behavior in future LLM-agent research. It should not read like a general evaluation survey. Its job is narrower: to translate the gaps diagnosed in Sections 3 to 5 into concrete evaluation requirements that could separate simple spatial affordance from meaningful spatial-behavior coupling.

[Table 7 about here: evaluation dimension table]

## 6.1 What Would Spatial Behavioral Validity Mean?

The first task of this section is conceptual. "Spatial behavioral validity" should not mean only that an agent can move, navigate, or mention places correctly. For this survey, it should mean that variation in agent-facing spatial representation can be linked to variation in behavior at the level of movement, interaction, or emergent social structure under controlled conditions. That definition makes the target harder, but it also prevents the section from collapsing into generic navigation or usability evaluation.

This subsection should distinguish at least three levels of success. The weakest level is spatial affordance: a system contains spatial scenes, places, routes, or embodied interaction. The middle level is spatial sensitivity: behavior changes when relevant spatial context changes. The strongest level is spatial mediation: the study shows that a specific kind of agent-facing spatial structure contributes to a behavioral outcome in a way that survives comparison against matched controls. Most current systems in the corpus reach the first level. Some rows plausibly reach the second. Very few, if any, cleanly establish the third.

Safe synthesis sentence:

- the next evaluation target is not spatial presence alone, but behavior that is demonstrably sensitive to agent-facing spatial structure.

## 6.2 Candidate Evaluation Dimensions

Table 7 should be the center of the section, not an afterthought. Each evaluation dimension should specify four things:

- the behavior being measured;
- the minimum spatial representation needed for the test to be meaningful;
- the control or comparison required;
- the strongest evidence status the result could support.

The section should group candidate dimensions in a way that matches the survey's actual gap structure. A workable grouping is:

1. movement and route choice;
2. co-presence and encounter structure;
3. interaction allocation across places or network positions;
4. group formation, segregation, or role differentiation;
5. macro-level social structure under altered spatial layouts.

The prose should make clear that not every dimension requires `L4`. Some questions can be meaningfully tested at `L2`, `L3`, or `L5`. But any claim about configurational mediation should require a representation that actually exposes global or layout-wide structure to the agent. This is where the section should explicitly connect back to the evidence-map result that `L4` remains nearly absent and that geometry-bearing `L5` cases are still limited and heterogeneous.

Drafting note:

- Keep each dimension operational.
- Avoid abstract "evaluation principles" that cannot be turned into a concrete table row.
- Use the claim matrix to label what kind of conclusion each evaluation could and could not support.

## 6.3 Controls, Baselines, and Confound Separation

The main methodological challenge is confound separation. If a study changes both spatial representation and unrelated agent information at the same time, then any observed behavioral change is uninterpretable. This subsection should therefore explain that future evaluation needs matched controls: same task, same agent family, same social setting, but different spatial interface conditions.

The control logic should be phrased in progressively stronger forms:

- `L1/L2` versus `L3`: does local relational structure matter beyond place naming or scene semantics?
- `L3` versus `L4`: does global abstract structure matter beyond local co-presence and adjacency?
- `L3` or `L4` versus `L5`: does embodied or geometry-bearing input change behavior beyond symbolic structure alone?

The section should also caution against overreading common but insufficient proxies. Navigation completion by itself is not enough. User satisfaction by itself is not enough. Emergent macro patterns without representation controls are not enough. These can all be useful components of an evaluation package, but none of them alone establishes spatial mediation in the sense required by this survey.

Safe synthesis sentences for this subsection:

- credible evaluation requires matched controls over the agent-facing spatial interface;
- navigation, immersion, or usability metrics alone do not establish spatial mediation;
- stronger causal language requires stronger control over representational confounds.

## 6.4 Evidence Ladder for Future Studies

This subsection should end the section by turning the evaluation discussion back into claim discipline. Different evaluation outcomes should map onto different allowable claims. A successful test may support that a system is spatially sensitive without yet supporting that it exhibits stable configuration-mediated social emergence. A carefully controlled comparison may support a limited observed-effect claim without settling mechanism. Only repeated, well-controlled findings across systems and environments would begin to justify stronger language.

This is the point where the section should connect most explicitly to `docs/plans/claim_matrix.md`. The contribution of Table 7 is not just to propose good experiments. It is to define what kinds of future evidence would allow the field to move from `designed_affordance_only` and feasibility arguments toward stronger observed-effect and, much later, mechanism claims.

The final sentence of the section should motivate Section 7: once evaluation dimensions are made explicit, the research agenda can be organized around the missing representation layers, missing controls, and missing cross-scale tests that the current corpus leaves unresolved.
