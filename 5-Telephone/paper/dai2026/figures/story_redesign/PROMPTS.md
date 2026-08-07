# Story-aligned figure prompts

Generation mode: built-in image generation, one call per figure.

Shared style: wide landscape scientific infographic; white background; deep
navy typography; cobalt blue for current/provenance-aware signals; cool gray
for baselines and unknown; muted orange only for stale or corrupted values;
flat vector-like editorial drawing; large type at double-column print size;
no gradients, shadows, 3D, logos, author names, or venue branding.

## Figure 1 — phenomenon

Core prompt: show one persistent source introducing “Sunday” into a compact
agent society, followed by two aligned evidence lanes. Public speech moves
from 62.9% to 81.8% (+18.9 pt, descriptive); population retrieval moves from
12.0% to 15.2% (+3.2 pt, 95% CI −5.6 to 12.0). End with “PUBLIC VISIBILITY ≠
POPULATION RETRIEVAL”. Do not depict the same agent saying the update and then
forgetting it. Do not use a baseline-to-source process diagram.

Title: “PUBLIC SPEECH MOVES; POPULATION RETRIEVAL BARELY DOES”.

## Figure 2 — causal localization

Core prompt: arrange a left-to-right chain. Panel a freezes one identical
ordered received stream and copies it into GA and PROV listener memories.
Panel b is the hero: PROV-generated streams move from 32.0% to 60.5%
(+28.5 pt, 95% CI 21.5–35.5, 8/8 seeds), and GA-generated streams supplied
with controlled-task versions move from 15.0% to 41.0% (+26.0 pt, 95% CI
16.5–35.5, 8/8 seeds). Panel c holds all other operations fixed and compares
frequency 62.5% with maximum version 71.5% (+9.0 pt, 95% CI 4.4–13.6,
8/8 seeds). End with “UPDATE ORDER > MENTION COUNT”. Do not attribute the
complete-pipeline effect entirely to the selector.

Title: “SAME EVIDENCE REVEALS THE MISSING UPDATE RULE”.

## Figure 3 — protocol boundary

Core prompt: organize three stages, PRESERVE → STRESS → AUTHENTICATE. Panel a
contrasts default dialogue (markers 0/720; current 16/75) with a protocolized
attribution norm (markers 610/720; current 75/75). Panel b plots exact current
HELD values over perturbation rates 0, .3, .6, .9: drop metadata =
93, 100, 93, 26; garble value = 93, 74, 42, 24; GA reference = 22%.
Panel c shows the forged-version pilot: naive PROV = 25 current, 43 stale,
7 unknown; origin-anchored APM = 48 current, 0 stale, 27 unknown. End with
“A STATE-UPDATE PROTOCOL MUST PRESERVE, RESOLVE, AND AUTHENTICATE PROVENANCE”.
Mark the channel and attack tests as bounded rather than a general security
guarantee.

Title: “PROVENANCE MUST SURVIVE AND BE AUTHENTICATED”.

## Method overview — GPT Image 2 draft

Core prompt: build a wide four-zone workflow—CHANGING FACT → AGENT SOCIETY →
LISTENER STATE UPDATE → PRIVATE RETRIEVAL.  Show Sunday (v0, stale) changing to
Monday (v1, current), propagation through pairwise dialogue with HEARD and SAID
measurement tags, and one ordered stream entering a locked “SAME RECEIVED
STREAM” fork.  The upper branch uses frequency-based memory, where repeated v0
mentions mean that stale may win.  The lower branch uses a provenance-aware
update with PRESERVE → RESOLVE → AUTHENTICATE and ends in CURRENT STATE.  The
private interview reports HELD as CURRENT, STALE, or UNKNOWN.  A subordinate
bottom strip shows OBSERVE THE GAP → FREEZE EVIDENCE → SWAP MEMORY RULE → STRESS
THE PROTOCOL, with drop metadata, garble value, and forge version.  Use a
restrained flat vector-like style, short labels, direct arrows, and no
quantitative results or unsupported mechanisms.

Core claim: “The same communicated evidence can produce different retrievable
states because the listener applies a different state-update rule.”

Output: `fig2_method_overview_image2_v1.png` (1717 × 916 px).
