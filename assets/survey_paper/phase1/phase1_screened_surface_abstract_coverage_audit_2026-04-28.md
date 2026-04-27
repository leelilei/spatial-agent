# Phase 1 Screened Surface Abstract Coverage Audit

Date: 2026-04-28

Purpose: clarify whether the current `581` screened-candidate surface has full abstract coverage and whether all records have been abstract-read.

## Short Answer

No.

The current `581` should not be described as `581 abstract-screened papers`.

It should be described as:

> `581` identified/title-screened candidate records after a fresh targeted L4-tilt search, with abstract/full-text screening completed for prioritized subsets.

## Count Breakdown

### Original Phase 1 Candidate Pool

Source:

- `assets/survey_paper/phase1/phase1_candidate_pool_2026-04-13.csv`

Coverage:

| Pool | Total | With abstract | Without abstract |
|---|---:|---:|---:|
| Original Phase 1 candidate pool | 417 | 348 | 69 |

Interpretation:

- Most original candidates had abstracts.
- But not all `417` had abstracts.
- The original broad pool should be called `title/abstract screened where abstract was available`, not uniformly abstract-screened.

### Abstract Rereview Subset

Source:

- `assets/survey_paper/phase1/phase1_abstract_rereview_round1_2026-04-13.csv`

Coverage:

| Pool | Total | With abstract | Without abstract |
|---|---:|---:|---:|
| Abstract rereview round 1 | 117 | 109 | 8 |

Interpretation:

- This is the subset that most clearly had abstract-level rereview.
- Even here, `8` rows did not have a normal abstract field and were judged from other metadata/source basis.

### Fresh L4-Tilt Targeted Screen

Sources:

- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_candidates_raw_2026-04-27.csv`
- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_screening_2026-04-27.csv`
- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_disposition_2026-04-28.csv`
- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_abstracts_2026-04-28.csv`
- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_abstract_disposition_2026-04-28.csv`

Coverage:

| Pool | Total | Abstract available | Abstract missing |
|---|---:|---:|---:|
| Fresh L4-tilt deduplicated rows | 179 | 166 | 13 |
| Fresh rows non-duplicate vs original pool | 164 | 151 | 13 |
| Fresh rows non-duplicate vs original and prior targeted screen | 161 | 148 | 13 |

Interpretation:

- The fresh OpenAlex pull initially saved title, DOI, year, venue, URL, query, citation count, and duplicate flags.
- A follow-up abstract completion pass retrieved and reconstructed OpenAlex inverted-index abstracts.
- Most fresh L4-tilt rows now have abstract-level disposition; `13` remain abstract-missing and are explicitly marked as metadata-only.

## Current Fresh-Screen Disposition

Original title/metadata disposition source:

- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_disposition_2026-04-28.csv`

| Disposition status | Rows | Screening depth |
|---|---:|---|
| `fulltext_checked_promote` | 3 | full-text checked |
| `fulltext_checked_reserve` | 1 | full-text checked |
| `fulltext_checked_adjacent` | 1 | full-text checked |
| `queued_for_recheck` | 7 | title/metadata screened, queued for abstract/full-text |
| `title_abstract_keep` | 7 | title-level keep; abstract not yet systematically captured |
| `background_or_adjacent` | 33 | title/metadata screened |
| `title_abstract_exclude` | 107 | title-level excluded |
| `duplicate_existing_pool` | 16 | duplicate/covered |
| `duplicate_prior_targeted` | 3 | duplicate/covered |
| `duplicate_or_covered` | 1 | duplicate/covered |
| **Total** | **179** |  |

Updated abstract-level disposition source:

- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_abstract_disposition_2026-04-28.csv`

| Abstract disposition status | Rows |
|---|---:|
| `fulltext_checked_promote` | 3 |
| `fulltext_checked_reserve` | 1 |
| `fulltext_checked_adjacent` | 1 |
| `queued_for_recheck` | 7 |
| `abstract_keep` | 15 |
| `abstract_keep_adjacent` | 16 |
| `abstract_background_or_adjacent` | 53 |
| `abstract_exclude` | 50 |
| `abstract_missing_keep_metadata` | 4 |
| `abstract_missing_exclude` | 8 |
| `duplicate_existing_pool` | 17 |
| `duplicate_prior_targeted` | 3 |
| `duplicate_or_covered` | 1 |
| **Total** | **179** |

## Correct Method Wording

Safe:

- `581 records were identified and title/metadata screened.`
- `Abstract screening was completed for records with available abstracts in the original pool and fresh L4-tilt screen.`
- `The fresh L4-tilt supplementary search was screened at abstract level where OpenAlex abstracts were available; abstract-missing records were explicitly marked and screened from title/metadata.`

Not safe:

- `581 abstracts were screened.`
- `All 581 records were abstract-reviewed.`
- `The 581-record screen has complete abstract coverage.`

## What Was Done Next

The abstract completion pass has now been completed for all `179` fresh L4-tilt rows:

- `166` abstracts retrieved and reconstructed from OpenAlex;
- `13` abstract-missing rows explicitly marked;
- abstract-level disposition table generated for all `179` rows.

Remaining limitation:

- the original `417` pool still contains `69` rows without a local abstract field.
- this is acceptable if methods state `title/abstract screening where abstracts were available`.
