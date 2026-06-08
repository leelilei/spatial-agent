# Core PDF Acquisition Log

Date: 2026-05-01

Scope: stable widened-Core rows in `spatial-agent-survey/paper/appendix/appendix_evidence_table.csv`.

## Result

- Starting PDF coverage: `23 / 34`
- Newly acquired PDFs: `10`
- Current PDF coverage: `33 / 34`
- Remaining PDF gaps: `1`
- Remaining route check: `assets/survey_paper/evidence_closure/pdf_gap_route_check_2026-05-01.md`

## Newly Acquired PDFs

| ID | Source | PDF path | Fulltext path |
|---|---|---|---|
| `R3-03` | MDPI static PDF | `assets/survey_paper/pdfs/phase1_round3_candidates/R3-03_Cognitive_Agents_Urban_Mobility_2025.pdf` | `assets/survey_paper/pdfs/phase1_round3_candidates/R3-03_Cognitive_Agents_Urban_Mobility_2025.fulltext.md` |
| `R3-04` | MDPI static PDF | `assets/survey_paper/pdfs/phase1_round3_candidates/R3-04_LLM_Epidemic_Economic_Dynamics_2026.pdf` | `assets/survey_paper/pdfs/phase1_round3_candidates/R3-04_LLM_Epidemic_Economic_Dynamics_2026.fulltext.md` |
| `R3-05` | arXiv PDF | `assets/survey_paper/pdfs/phase1_round3_candidates/R3-05_CoELA_2024.pdf` | `assets/survey_paper/pdfs/phase1_round3_candidates/R3-05_CoELA_2024.fulltext.md` |
| `TW-09` | arXiv PDF | `assets/survey_paper/pdfs/phase1_adjacent/12_TW-09_ELLMA-T_Social_VR_2024.pdf` | `assets/survey_paper/pdfs/phase1_adjacent/12_TW-09_ELLMA-T_Social_VR_2024.fulltext.md` |
| `TW-11` | KITopen repository PDF | `assets/survey_paper/pdfs/phase1_adjacent/15_TW-11_Office_Whispers_GenAI_NPCs_2026.pdf` | `assets/survey_paper/pdfs/phase1_adjacent/15_TW-11_Office_Whispers_GenAI_NPCs_2026.fulltext.md` |
| `TW-12` | MDPI static PDF | `assets/survey_paper/pdfs/phase1_adjacent/13_TW-12_Virtual_Tutoring_System_2026.pdf` | `assets/survey_paper/pdfs/phase1_adjacent/13_TW-12_Virtual_Tutoring_System_2026.fulltext.md` |
| `TW-13` | Frontiers PDF | `assets/survey_paper/pdfs/phase1_adjacent/14_TW-13_TUMSphere_Next_Gen_Orientation_2026.pdf` | `assets/survey_paper/pdfs/phase1_adjacent/14_TW-13_TUMSphere_Next_Gen_Orientation_2026.fulltext.md` |
| `HC11` | user-provided IEEE VR PDF | `assets/survey_paper/pdfs/phase1_adjacent/17_HC11_Environment_Aware_VR_Roleplay_2025.pdf` | `assets/survey_paper/pdfs/phase1_adjacent/17_HC11_Environment_Aware_VR_Roleplay_2025.fulltext.md` |
| `BK08` | user-provided ScienceDirect PDF | `assets/survey_paper/pdfs/phase1_adjacent/18_BK08_Online_Community_Collective_Behaviors_2026.pdf` | `assets/survey_paper/pdfs/phase1_adjacent/18_BK08_Online_Community_Collective_Behaviors_2026.fulltext.md` |
| `BK03` | author/project page PDF | `assets/survey_paper/pdfs/phase1_adjacent/19_BK03_Context_Aware_Onboarding_Metaverse_2024.pdf` | `assets/survey_paper/pdfs/phase1_adjacent/19_BK03_Context_Aware_Onboarding_Metaverse_2024.fulltext.md` |

## Remaining Gaps

| ID | Paper | Attempted route | Result | Next action |
|---|---|---|---|---|
| `BK02` | `When LLMs Recognize Your Space: Research on Experiences with Spatially Aware LLM Agents` | PubMed/IEEE/public search; IEEE stamp probe | No open PDF located; IEEE returned `418` | Needs institutional IEEE/TVCG access or author copy; otherwise keep as non-PDF bridge note only. |

## Notes

- Earlier failed attempts did not leave valid PDF files in the archive.
- All newly acquired PDFs were verified with `file` and converted using `spatial-agent-survey/scripts/pdf2text.py --emit-meta`.
- The updated manifest is `assets/survey_paper/evidence_closure/pdf_markdown_archive_manifest_2026-05-01.md`.
