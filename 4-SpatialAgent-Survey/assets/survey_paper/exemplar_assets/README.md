# Exemplar Assets

Generated reference package for figure redesign prompts.

Generated at UTC: `2026-04-30T17:30:39+00:00`

Command:

```bash
extract_exemplar_assets.py --preset figure-redraw --render-pages figure --overwrite
```

## Processed Papers

| id | paper | pages | rendered pages | captions | figure assets | embedded images | folder |
|---|---|---:|---:|---:|---:|---:|---|
| 01 | `01_Feng2025_Spatial_Intelligence_Across_Scales.pdf` | 14 | 8 | 7 | 7 | 18 | `01_Feng2025_Spatial_Intelligence_Across_Scales/` |
| 05 | `05_Mou2024_Social_Simulation_LLM_Agents_Survey.pdf` | 35 | 12 | 12 | 12 | 24 | `05_Mou2024_Social_Simulation_LLM_Agents_Survey/` |
| 07 | `07_Luo2025_LLM_Agent_Methodology_Survey.pdf` | 26 | 12 | 11 | 11 | 12 | `07_Luo2025_LLM_Agent_Methodology_Survey/` |
| 11 | `11_Silacci2026_LLM_Agents_Scoping_Review.pdf` | 15 | 5 | 5 | 5 | 1 | `11_Silacci2026_LLM_Agents_Scoping_Review/` |
| 12 | `12_Leiser2025_LLM_Architectures_Scoping_Review.pdf` | 15 | 6 | 6 | 6 | 1 | `12_Leiser2025_LLM_Architectures_Scoping_Review/` |
| 13 | `13_TudorCar2020_Conversational_Agents_Scoping_Review.pdf` | 21 | 5 | 4 | 4 | 3 | `13_TudorCar2020_Conversational_Agents_Scoping_Review/` |
| 14 | `14_Tricco2018_PRISMA_ScR.pdf` | 29 | 3 | 3 | 3 | 6 | `14_Tricco2018_PRISMA_ScR/` |
| 15 | `15_Peters2024_JBI_Scoping_Reviews.pdf` | 190 | 23 | 29 | 29 | 49 | `15_Peters2024_JBI_Scoping_Reviews/` |

Each folder contains:

- `text.md`: page-level extracted text.
- `meta.json`: extraction metadata and counts.
- `figure_index.md`: figure/table caption hits and embedded image inventory.
- `figures/`: flat caption-level crops and same-name Markdown metadata, for example `figure1_multiple_scale_spatial_intelligence_in_real_world.png`.
- `pages/`: rendered reference pages selected by the extraction mode.
- `images/`: embedded raster images above the size threshold.
- `contact_sheet.png`: quick visual overview of rendered pages.

Target-figure planning files:

- `target_figure_reference_map.md`: maps Figure 1-Figure 6 to candidate exemplar assets.
- `target_figure_reference_analysis.md`: analyzes the exact reference images to borrow from, avoid, and convert into GPT-Image-2 prompts.
