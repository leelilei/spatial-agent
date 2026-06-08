# Phase 1 Bridge Core Reclassification

Date: 2026-04-27

Purpose: operationalize the widened `Core` boundary by re-adjudicating already known `Adjacent` and reserve cases before launching more search.

## Current baseline

- strict `Anchor Core`: `17` paper-level items
- stable coded rows: `19`

## Local widening pool

This pass identifies `12` local bridge candidates:

- `6` immediate promotions
- `5` quick-recheck promotions
- `1` reserve tail case

Immediate promotions:

- `HC01`
- `BK06`
- `BK07`
- `BK08`
- `R3-03`
- `R3-05`

Quick recheck promotions:

- `HC11`
- `BK02`
- `BK03`
- `BK04`
- `BK05`

Reserve only:

- `LD01`

## Count effect

If the immediate bridge cases are admitted:

- paper-level `Core` rises from `17` to `23`

If the immediate plus quick-recheck bridge cases are admitted:

- paper-level `Core` rises from `17` to `28`

That means the widened local pool already gets the project close to the new target of `30`.

## Representation effect

Most of the gain is in `L2` and `L5`:

- `L2` can stop being zero through `HC11`, `BK02`, `BK03`, `BK04`, and `BK05`
- `L5` gains additional bridge breadth through `HC01`, `BK06`, and `R3-05`

`L4` will only improve if the revised global-abstract-structure reading is applied during re-coding, especially for:

- `BK07`
- `BK08`

## External top-up after local reclassification

Only after the local widening pool is processed should the project run more search.

Current best external top-up cases:

- `INDOORWORLD`
- `BOOKWORLD`

Those two are enough to push the widened corpus from about `28` to about `30` if the quick-recheck local cases survive.

## Working rule

- Do not search first.
- Re-adjudicate known local bridge candidates first.
- Use `anchor_core` versus `bridge_core` to preserve claim discipline.
- Keep the old strict table as the anchor baseline rather than rewriting history.

## Execution status

The first execution pass has now been materialized in:

- `assets/survey_paper/phase1/phase1_widened_core_execution_memo_2026-04-27.md`
- `assets/survey_paper/phase1/phase1_widened_bridge_core_coding_draft_2026-04-27.csv`

Current execution split:

- `6` bridge cases can be promoted now under the widened rule: `HC01`, `BK06`, `BK07`, `BK08`, `R3-03`, `R3-05`
- `5` bridge cases need quick source recheck before stable counting: `HC11`, `BK02`, `BK03`, `BK04`, `BK05`
- `1` case remains reserve: `LD01`

Expected count effect:

- strict `anchor_core` remains `17` paper-level items
- widened Core after immediate bridge promotions becomes `23`
- widened Core after quick-recheck promotions can reach `28`
- external top-up should wait until the local quick-recheck pass is complete
