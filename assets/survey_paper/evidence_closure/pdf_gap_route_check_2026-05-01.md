# Remaining Core PDF Gap Route Check

Date: 2026-05-01

Scope: stable widened-Core rows still missing local PDF after archiving the user-provided IEEE VR PDF, the user-provided ScienceDirect PDF, and the BK03 author/project-page PDF.

## Current Archive State

- Stable widened-Core PDF coverage: `33 / 34`
- Resolved in this pass:
  - `HC11`: archived at `assets/survey_paper/pdfs/phase1_adjacent/17_HC11_Environment_Aware_VR_Roleplay_2025.pdf`; full text extracted with 39 pages and 117,089 text characters.
  - `BK08`: archived at `assets/survey_paper/pdfs/phase1_adjacent/18_BK08_Online_Community_Collective_Behaviors_2026.pdf`; full text extracted with 14 pages and 75,934 text characters.
  - `BK03`: archived at `assets/survey_paper/pdfs/phase1_adjacent/19_BK03_Context_Aware_Onboarding_Metaverse_2024.pdf`; full text extracted and evidence table now points to the PDF.
- Remaining gap: `BK02`

## BK02 Route Check

Paper: `When LLMs Recognize Your Space: Research on Experiences with Spatially Aware LLM Agents`

- DOI: `10.1109/TVCG.2025.3616809`
- IEEEXplore document: `11192586`
- PubMed: `41052126`
- PubMed route: abstract page is accessible, but no PDF/full-text link was found.
- IEEE route: `stamp.jsp` probes return HTTP `418` in the command environment.
- OpenAlex route: reports `open_access.is_oa=false`, `best_oa_location=null`, and no repository full text.
- ResearchGate route: page exists, but reports no full text available and offers only author-request workflow.
- Crossref route: metadata includes a staging PDF URL marked for similarity-checking use; not used as an archive source because it is not a public/open access acquisition route.

Viable next action: acquire through institutional IEEE/TVCG access or request an author copy. If neither is available, keep `BK02` as a source-note bridge or downgrade it from final widened-Core claims.

## BK08 Route Check

Paper: `Unveiling the collective behaviors of large language model-based autonomous agents in an online community: A social network analysis perspective`

- DOI: `10.1016/j.dim.2025.100107`
- PII: `S2543925125000154`
- ScienceDirect issue route: article is listed as an open-access research article with a `View PDF` link.
- Exact PDF URL discovered from ScienceDirect issue page:
  `https://www.sciencedirect.com/science/article/pii/S2543925125000154/pdfft?md5=a484536766a5b7bd3f43fe37476eb692&pid=1-s2.0-S2543925125000154-main.pdf`
- Command download result: the URL saves a Cloudflare HTML challenge, not a valid PDF.
- Elsevier API route: unauthenticated `httpAccept=application/pdf` returns HTTP `406`; `text/xml` returns only core metadata.
- OpenAlex/Crossref route: confirms open-access status and CC BY-NC-ND license, but does not expose a direct PDF URL independent of ScienceDirect.

Status after user-provided file: acquired and archived at `assets/survey_paper/pdfs/phase1_adjacent/18_BK08_Online_Community_Collective_Behaviors_2026.pdf`; evidence table now points to the PDF and the paired full-text markdown exists.
