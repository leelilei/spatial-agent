# Co-Presence Evidence-Gap Anatomy (E5, local analysis)

Date: 2026-07-10

## Question

The rc1 / hard-tier headline is "legal but ineffective": baselines stay feasible
yet fail co-presence outcomes. A reviewer's sharp follow-up is *why* — is the gap
a navigation failure, a refusal-to-engage, or something more specific? This is a
zero-API re-analysis of the 72 baseline traces already on disk (easy 2×6×3 +
hard 2×6×3), attributing every failed co_presence OUTCOME to a mechanism.

## Method

`tools/analyze_copresence_evidence_gap.py` replays each trace against its
scenario's co_presence requirements (venue set, time window, message gate) and
classifies each failed outcome into one mutually-exclusive class: `no_venue_entry`,
`entered_no_interact`, `interact_rejected` (tried but rejected at attempt time),
`window_overrun` (met the right person at the right venue, started inside the
window, but the interaction ran past the window close), or `wrong_target`.

Archived: `results/cityintent_v1_rc1/copresence_evidence_gap_2026-07-10/`.

## Result

| Tier | Policy | Failed/Total | no_venue_entry | entered_no_interact | interact_rejected | window_overrun |
|---|---|---:|---:|---:|---:|---:|
| easy | react_tool_policy | 0/21 | 0 | 0 | 0 | 0 |
| easy | plan_and_execute | 3/21 | 0 | 0 | 2 | 1 |
| hard | react_tool_policy | 6/27 | 0 | 1 | 1 | 4 |
| hard | plan_and_execute | 17/27 | 0 | 1 | 7 | 9 |

## The finding: the gap is temporal precision, not navigation

Across **all** cells, `no_venue_entry = 0`. Every failed co-presence outcome
reached the correct venue. The failures are almost entirely temporal:

- **Hard tier: 21 of 23 co-presence failures are timing failures**
  (`window_overrun` 13 + `interact_rejected` 8). Only 2 are `entered_no_interact`
  (reached the venue, never tried to meet). Zero are navigation failures.
- **`window_overrun` is the single largest class** (13/23): the agent met the
  right counterpart at the right place and started the interaction *inside* the
  window, but started too late, so it ended after the window closed and does not
  count. E.g. window `[745,760]`, interaction start 756, end 761 — off by one
  minute. window `[1080,1095]`, start 1091, end 1101.

So the plausible↔verified gap in these tasks is not "agents can't find the
place" or "agents don't try to socialize" — they navigate correctly and attempt
the meeting. They fail on the **temporal precision of the environment-accepted
social act**: leaving no margin for an interaction that must both start and end
within a narrow window. This is exactly the kind of commitment a fluent plan
("go meet Ben at the quiet cafe at 12:40") hides and the evidence contract
exposes.

## Why this sharpens Claim A

- It converts "legal but ineffective" from an aggregate score into a **named,
  counted mechanism** with concrete exemplars — the failure taxonomy Claim A
  promises.
- It pre-empts the "your agents just can't navigate the toy graph" objection:
  navigation failures are **zero**; the gap is temporal.
- It explains the ReAct vs Plan-and-Execute split mechanistically: Plan-and-Execute
  commits to a schedule and overruns the window (9 `window_overrun`); ReAct's
  observe-act loop lets it retry, so it overruns less (4) but still cuts windows
  too fine.

## Follow-ups

- Extend to the 4 official adapters once the hard adapter run lands (checkout
  machine), to see whether `window_overrun` vs `no_venue_entry` splits the weak
  scaffolds differently (SOTOPIA-style may fail earlier, at entry/interact).
- Guard the analyzer with a small test if it becomes a paper table generator.
