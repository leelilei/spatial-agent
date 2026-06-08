# GPT-Image-2 Figure Redraw Prompts

Draft status: execution prompts for raster redraws of Figure 1-Figure 6.

Global settings:

- Model: `gpt-image-2`
- Mode: image edit using the current SVG-rendered PNG as reference
- Size: `2048x1280`
- Quality: `high`
- Output format: `png`
- Visual style: academic information graphic, restrained, readable, publication-safe
- Text strategy: sparse exact text only; captions/specs carry details
- Shared constraints: no watermark, no logo, no invented paper names, no decorative clutter, no unsupported causal claims

## Figure 1 Prompt

Redraw the provided reference as a polished academic information graphic for a survey paper.

Show the evidence-role structure of the corpus with a clean central Core area, a nested or layered distinction between `anchor_core` and `bridge_core`, and separate side roles for `Adjacent`, `Foundational`, and `Boundary`.

Use sparse exact text only:

- Title: `Figure 1. Corpus and Evidence Roles`
- `anchor_core: 17 sources / 19 rows`
- `bridge_core: 15 sources / 15 rows`
- `Adjacent: feasibility and boundary evidence`
- `Foundational: theory and transferable hypotheses`
- `Boundary: HC01 / TW-02 not counted as stable Core`
- Claim rule: `role -> layer -> evidence status`

Make the style refined and journal-ready: warm off-white background, muted greens for Core, muted blue for Adjacent, muted tan for Foundational/Boundary, crisp vector-like shapes, strong spacing, high legibility. Do not include small paragraphs from the reference. Do not imply Adjacent or Foundational are direct LLM-agent social-effect evidence.

## Figure 2 Prompt

Redraw the provided reference as a polished two-panel academic PRISMA-style information graphic.

Panel A should show bibliographic screening. Panel B should show evidence-map stabilization. Keep PRISMA screening counts visually separate from row-level evidence-map counts.

Use sparse exact text only:

- Title: `Figure 2. Screening and Evidence-Map Stabilization`
- Panel A: `Bibliographic screening`
- `Records screened: 417`
- `Core: 12`
- `Adjacent: 42`
- `Foundational: 47`
- `Excluded: 316`
- `E1: 85 / E2: 54 / E3: 177`
- Panel B: `Evidence-map stabilization`
- `Strict anchor: 17 sources / 19 rows`
- `Bridge review`
- `HC01: Adjacent`
- `TW-02: boundary only`
- `Stable widened Core: 32 sources / 34 rows`
- Note: `screening counts != coded rows`

Make it clean, restrained, and suitable for a survey paper: off-white background, black/charcoal outlines, muted green included boxes, muted red excluded box, muted yellow boundary boxes. No extra records, no extra counts, no invented databases.

## Figure 3 Prompt

Redraw the provided reference as a polished academic taxonomy diagram.

Show a left-to-right `L0` to `L5` taxonomy of agent-accessible spatial representation. Emphasize that the coding is about what the agent receives, not simulator backend richness.

Use sparse exact text only:

- Title: `Figure 3. Agent-Accessible Spatial Representation Taxonomy`
- Main rule: `code agent input, not backend`
- `L0 none: 0`
- `L1 labels: 1`
- `L2 semantic scene: 8`
- `L3 local relations: 18`
- `L4 global abstract: 1`
- `L5 geometry / embodiment: 6`
- Backend strip: `text-only`, `2D grid`, `graph`, `3D engine`
- Caution: `rich backend != higher level unless agent-facing`

Use a refined left-to-right sequence with subtle color progression, clear level cards, and a bottom backend strip. Keep all text large and readable. Do not include dense explanatory paragraphs.

## Figure 4 Prompt

Redraw the provided reference as a polished academic distribution chart.

Show representation distribution by core layer, split into `anchor_core` and `bridge_core`. Use a stacked or grouped bar chart that makes the `L4` gap visually obvious.

Use sparse exact text only:

- Title: `Figure 4. Representation Distribution by Core Layer`
- Legend: `anchor_core`, `bridge_core`
- X-axis levels: `L1`, `L2`, `L3`, `L4`, `L5`
- Counts:
- `L1: 1 anchor / 0 bridge`
- `L2: 0 anchor / 8 bridge`
- `L3: 15 anchor / 3 bridge`
- `L4: 0 anchor / 1 bridge`
- `L5: 3 anchor / 3 bridge`
- Callout: `L4 absent from anchor_core`
- Callout: `bridge recovery is not anchor evidence`

Use a publication-safe chart style with muted green for anchor and light green for bridge, off-white background, crisp axes, and large readable labels. Do not add extra data series or percentages.

## Figure 5 Prompt

Redraw the provided reference as a polished academic worked-example graph.

Show that local adjacency is not global configuration. Use a two-panel layout: Panel A shows two local egocentric views that look equivalent, and Panel B shows the same nodes in a whole graph where their global positions differ.

Use sparse exact text only:

- Title: `Figure 5. Local Adjacency Is Not Global Configuration`
- Panel A: `Local view: same immediate neighbors`
- `B: local degree 2`
- `G: local degree 2`
- Panel B: `Whole-layout position differs`
- `L3: local adjacency`
- `L4: global configuration`
- Bottom note: `local neighbors do not equal depth, integration, control, or choice`

Use clean node-link visuals, high contrast, muted green for node `B`, muted amber for node `G`, and clear spacing. Do not add complex equations or extra graph metrics.

## Figure 6 Prompt

Redraw the provided reference as a polished academic research agenda map.

Show a central evidence-map result connected to five agenda directions: representation, mechanism, emergence, generalization, and applications. The figure should read as future work, not current evidence.

Use sparse exact text only:

- Title: `Figure 6. Research Agenda Map`
- Center: `Evidence-map result: L3 concentrated / L4 sparse`
- `1. Representation`
- `2. Mechanism`
- `3. Emergence`
- `4. Generalization`
- `5. Applications`
- Guardrail: `future-work claims require exposed structure + observed evidence`

Use a refined radial or hub-and-spoke academic infographic style with muted colors, generous whitespace, and clear hierarchy. Do not imply that richer spatial representation has already been validated.
