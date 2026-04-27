# Phase 1 Core Manual Acquisition Checklist

Date: 2026-04-22

Purpose: keep a short checklist for the remaining Core papers that still need valid local PDFs.

## Rules

- Final archive directory: `assets/survey_paper/pdfs/phase1_core/`
- Placeholder HTML directory: `assets/survey_paper/pdfs/phase1_placeholders/`
- A successful download must be a real PDF, not an HTML anti-bot page
- Quick checks:
  - file size is usually well above `100 KB`
  - the file header starts with `%PDF`
  - if the file starts with `<html>` or `<!doctype`, the download failed

## Archive status after 2026-04-22

- Valid `batch1` PDFs have already been archived into `phase1_core/`
- Fake PDF downloads were moved into `phase1_placeholders/`
- New manually acquired valid PDFs should go directly into `phase1_core/`, not back into `phase1_core_batch1/`
- `HC01` was archived on 2026-04-27 as `assets/survey_paper/pdfs/phase1_core/00_HC01_TravelAgent_Noyman2025.pdf`; full-text review recommends treating it as Adjacent/boundary evidence rather than stable Core social-behavior evidence.

## HC13

- Target filename: `assets/survey_paper/pdfs/phase1_core/14_HC13_Fire_Evacuation_CA.pdf`
- Current placeholder file: `assets/survey_paper/pdfs/phase1_placeholders/HC13_Fire_Evacuation_CA.placeholder.html`
- Suggested routes:
  - ScienceDirect: `https://www.sciencedirect.com/science/article/pii/S0925753525001602`
  - DOI: `https://doi.org/10.1016/j.ssci.2025.106935`
  - ResearchGate: `https://www.researchgate.net/publication/397145175_Large-language-model-driven_agents_for_fire_evacuation_simulation_in_a_cellular_automata_environment`
- Action:
  1. Try `View PDF` in a normal browser.
  2. If unavailable, try ResearchGate full-text request.
  3. If still unavailable, use institution access or author copy.

## HC14

- Target filename: `assets/survey_paper/pdfs/phase1_core/15_HC14_Crowd_Evacuation_Disaster.pdf`
- Current placeholder file: `assets/survey_paper/pdfs/phase1_placeholders/HC14_Crowd_Evacuation_Disaster.placeholder.html`
- Suggested routes:
  - ScienceDirect: `https://www.sciencedirect.com/science/article/pii/S0951832025012554`
  - DOI: `https://doi.org/10.1016/j.ress.2025.112056`
  - ResearchGate: `https://www.researchgate.net/publication/398196301_When_Agents_Learn_to_Think_Large_Language_Model-Enhanced_Agent-Based_Modeling_for_Crowd_Evacuation_in_Disaster_Scenarios`
- Action:
  1. Try `View PDF` in a normal browser.
  2. If unavailable, try ResearchGate full-text request.
  3. If still unavailable, use institution access or author copy.

## After each successful acquisition

Update:

- `assets/survey_paper/phase1/phase1_fulltext_sanity_check_batch1_2026-04-22.csv`

Recommended fields to revise:

- `pdf_status -> downloaded`
- `full_text_status -> partial_reviewed` or `reviewed`
- `next_action ->` the actual next coding or extraction step
