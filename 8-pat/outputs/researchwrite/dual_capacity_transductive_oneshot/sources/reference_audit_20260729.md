# DCTPR reference search and verification audit

Date: 2026-07-29

## Scope and method

Workflows: multi-source literature search and citation verification.

The search targeted four manuscript claims rather than attempting a survey:

1. strong frozen or transfer-based representations make simple few-shot
   classifiers competitive;
2. fine-grained few-shot recognition requires modeling subtle local or
   cross-image differences;
3. transductive prototype, graph, and transport methods form the closest method
   boundary;
4. balanced query marginals improve efficiency but restrict applicability under
   class imbalance.

OpenAlex was used for discovery and Crossref for primary metadata verification.
When Crossref did not register an arXiv DOI, OpenAlex DOI records were used.
Results were deduplicated by normalized DOI, then by exact title and first
author. The academic-search MCP was unavailable; the bundled OpenAlex script
was also blocked by sandbox DNS, so direct public Crossref/OpenAlex endpoints
were used and source failures were not silently ignored.

## Outcome

- Existing bibliography entries audited: 11.
- New primary papers selected and cited: 8.
- Final cited bibliography: 19 entries.
- New coverage: transfer/simple baselines (3), fine-grained few-shot methods
  (3), simple efficient few-shot inference (2).
- No survey-only padding was added.

## Corrections to existing entries

| Key | Status | Correction |
|---|---|---|
| `ptmap` | verified, canonical version changed | Replaced the 2020 arXiv record with the ECCV 2020 Workshops chapter, published in the 2021 proceedings volume, pp. 487--499, DOI 10.1007/978-3-030-86340-1_39. |
| `realistictransduction` | verified as preprint | Removed the unsupported NeurIPS 2021 attribution; retained the verifiable 2022 arXiv record, DOI 10.48550/arXiv.2204.11181. |
| `iterativegraph` | verified, canonical version changed | Replaced the arXiv entry with CVPR 2023, pp. 23996--24006, DOI 10.1109/CVPR52729.2023.02298. |
| `conditionaltransport` | verified | Added ICCV pages 16271--16280. Crossref and the arXiv/OpenAlex record disagree on the middle-author ordering; the manuscript keeps the order in the paper/preprint record and notes the conflict here. |
| `adaptivemanifold` | mismatch corrected | Corrected pages from 2297--2306 to 2286--2295 using the IEEE/Crossref proceedings record. |
| `laplacianshot` | verified | Added arXiv DOI 10.48550/arXiv.2006.15486; ICML/PMLR venue, volume, and pages match. |
| `tim` | verified | Added arXiv DOI 10.48550/arXiv.2008.11297; NeurIPS 2020 attribution matches. |

The DINOv2, CUB, Stanford Dogs, and Sinkhorn entries were retained. DINOv2 is
an OpenReview/TMLR record, while both dataset records are non-DOI technical or
workshop publications; their identity and year were checked by exact-title
lookup rather than assigning invented DOIs.

## Added and cited primary papers

| Key | Claim supported | Venue/year | DOI |
|---|---|---|---|
| `closerlook` | strong supervised embeddings and simple classifiers | ICLR 2019 | 10.48550/arXiv.1904.04232 |
| `goodembedding` | transfer learning as a strong few-shot baseline | ECCV 2020 | 10.1007/978-3-030-58568-6_16 |
| `simpleshot` | competitive nearest-neighbor/centroid inference | ICLR 2020 | 10.48550/arXiv.1911.04623 |
| `mamlfgvc` | attention for fine-grained few-shot recognition | IJCAI 2020 | 10.24963/ijcai.2020/152 |
| `dualattention` | dual attention for fine-grained few-shot recognition | AAAI 2022 | 10.1609/aaai.v36i3.20196 |
| `bfrn` | cross-image feature reconstruction | AAAI 2023 | 10.1609/aaai.v37i3.25383 |
| `squeezefeatures` | efficient feature preprocessing for few-shot learning | Algorithms 2022 | 10.3390/a15050147 |
| `easy` | strong few-shot performance from simple components | Journal of Imaging 2022 | 10.3390/jimaging8070179 |

## Deliberate exclusions

DeepEMD and several newer fine-grained networks were relevant search hits but
were not cited because the selected attention and reconstruction papers already
support the corresponding claims. Transductive CLIP was excluded because the
paper does not use CLIP and a citation would broaden the method boundary without
supporting a necessary sentence. High-way search results were too indirect to
support a standalone claim, so the manuscript describes high-way as its own
evaluation setting rather than implying an established high-way literature.

## Final verification

BibTeX completed without missing entries. The final LaTeX log contains no
undefined citations, undefined cross-references, or overfull boxes. All six PDF
pages were re-rendered at 120 dpi and visually checked; the 19-item bibliography
is complete and readable across pages 5--6.
