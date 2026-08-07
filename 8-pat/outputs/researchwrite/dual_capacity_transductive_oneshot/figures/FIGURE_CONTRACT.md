# DCTPR figure contract

## Training-example image plate

- Core conclusion: CUB and Stanford Dogs require discrimination among visually
  similar classes under substantial pose and background variation.
- Archetype: image plate.
- Panel a: three CUB warbler classes from the official training partition.
- Panel b: Norfolk, Norwich, and Cairn terriers from the Stanford Dogs official
  training list.
- Processing: center crop to a common 4:3 aspect ratio; no brightness,
  contrast, color, pseudo-color, or local-content adjustment.
- Integrity: the source-data CSV records the class, source locator, training
  split evidence, processing, and SHA256 digest for every displayed image.
- Reviewer risk: the plate is illustrative task context, not evidence of model
  performance or a claim that the selected images are statistically typical.
- Export: double-column PDF/SVG plus 600-dpi TIFF and 300-dpi PNG preview.

## Accuracy--efficiency operating point

- Core conclusion: DCTPR approaches the strongest matched transductive
  accuracy at substantially lower task-level runtime.
- Archetype: quantitative grid.
- Hero evidence: mean accuracy versus mean task-head runtime on CUB and Dogs.
- Validation unit: three episodes and 30 support rotations per dataset.
- Statistics: points are descriptive means; no independence-based confidence
  interval is shown because rotations reuse episode images.
- Reviewer risk: BL-NCC has zero task-head runtime and cannot be placed on a
  logarithmic axis. It is shown as a horizontal inductive-reference line; the
  vertical line marks the predeclared 50-ms task-head budget.
- Export: double-column PDF/SVG plus 600-dpi TIFF and 300-dpi PNG preview.

## Prototype-refinement mechanism diagnostic

- Core conclusion: the frozen three-step update moves one-shot prototypes
  toward their true query-class centers and improves balanced assignments.
- Archetype: quantitative grid.
- Panel a: prototype-to-query-center cosine error at refinement steps 0--3.
- Panel b: balanced assignment accuracy at the same steps.
- Validation unit: three Stanford Dogs official-training episodes and 30
  support rotations; bands are descriptive rotation-level standard deviations.
- Source data: a per-episode, per-rotation, per-step CSV plus metadata containing
  the fixed settings, metric definitions, endpoint checks, and source-feature
  SHA256 digests.
- Reviewer risk: query labels are used only offline to compute true centers and
  score assignments, never as DCTPR inputs. Rotations share images and are not
  independent replicates.
- Export: double-column PDF/SVG plus 600-dpi TIFF and 300-dpi PNG preview.

## Per-class transfer and paired significance (PAT-K-260806-010)

- Core conclusion: refinement is broadly but not uniformly beneficial; roughly
  one class in seven degrades, and the 1.35-pp CUB gap vs TIM-ADM is
  consistently significant while the 0.61-pp Dogs gap vs MAP-RAW is not.
- Archetype: quantitative grid.
- Panel a (two sub-panels): per-class DCTPR minus BL-NCC accuracy, sorted
  descending, for CUB (200 classes) and Stanford Dogs (120 classes). Blue =
  positive transfer, red = negative, grey = neutral.
- Panel b (two sub-panels): per-rotation difference in exclusively-correct
  query counts between DCTPR and the strongest matched solver. Red bars reach
  two-sided exact McNemar significance at alpha=0.05; grey bars do not.
- Validation unit: six development episodes (3 CUB + 3 Dogs), 10 rotations
  each; 30 rotation comparisons per dataset.
- Source: analysis script `experiments/dinov2_capacity_kernel/analyze_per_class_transfer.py`,
  protocol `experiments/dinov2_capacity_kernel/PAT-K-260806-010_protocol.json`.
  No new inference. Official-test predictions not available locally.
- Statistical caveats: support rotations reuse episode images and are not
  independent replicates. McNemar tests paired decisions within a single
  rotation only; they are reported as rotation counts, not pooled.
- Reviewer risk: the negative-transfer tail is real but should not be read as
  systematic bias toward any identifiable class type; the correlation between
  baseline accuracy and transfer is weak and inconsistent across datasets.
- Source data: `source_data/fig_per_class_transfer.csv` and
  `source_data/per_class_transfer_summary.json`.
- Export: double-column PDF/SVG plus 600-dpi TIFF and 300-dpi PNG preview.

## Stability and prior boundary

- Core conclusion: the gain over nearest support is stable across all episodes,
  but depends on the balanced query marginal.
- Archetype: quantitative grid.
- Panel a: per-rotation DCTPR minus BL-NCC accuracy for six episodes.
- Panel b: balanced, mild-imbalance, and severe-imbalance macro balanced
  accuracy for BL-NCC, TIM-ADM, uniform-prior DCTPR, and oracle-count DCTPR.
- Statistics: individual rotations and arithmetic means are descriptive. The
  oracle curve is diagnostic only and is never a deployable input.
- Reviewer risk: support rotations share images; the figure must not describe
  their dispersion as independent-sample uncertainty.
- Export: double-column PDF/SVG plus 600-dpi TIFF and 300-dpi PNG preview.
