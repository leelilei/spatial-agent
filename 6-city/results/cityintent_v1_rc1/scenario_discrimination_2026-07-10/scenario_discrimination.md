# Scenario Discrimination (item analysis)

Per scenario: difficulty (mean task_completion across policies), how well it
separates policies (sd / range), and item-total correlation against the rest
of the benchmark. A scenario with range ≈ 0 carries no information; a negative
item-total correlation means it ranks policies against the overall ordering.

| Scenario | Family | Policies | Mean | SD | Range | Item-total r | Flag |
|---|---|---:|---:|---:|---:|---:|---|
| `budget_errand_chain` | budget_constraint | 4 | 0.65 | 0.409 | 1.0 | 0.867 | ok |
| `commute_disruption` | disruption | 4 | 0.25 | 0.433 | 1.0 | 0.721 | ok |
| `detour_commute_midroute_block` | disruption | 4 | 0.542 | 0.32 | 0.833 | 0.791 | ok |
| `memory_dependent_place_choice` | memory | 4 | 0.516 | 0.354 | 1.0 | 0.997 | ok |
| `unexpected_friend_encounter` | opportunistic_social | 4 | 0.864 | 0.236 | 0.545 | 0.863 | ok |
| `paired_study_a` | paired_disruption | 4 | 0.75 | 0.433 | 1.0 | 0.855 | ok |
| `paired_commute_a` | paired_disruption | 4 | 0.5 | 0.5 | 1.0 | 0.698 | ok |
| `paired_commute_b` | paired_disruption | 4 | 0.75 | 0.433 | 1.0 | 0.855 | ok |
| `paired_pickup_a` | paired_disruption | 4 | 0.75 | 0.433 | 1.0 | 0.855 | ok |
| `paired_pickup_b` | paired_disruption | 4 | 0.75 | 0.433 | 1.0 | 0.855 | ok |
| `paired_study_b` | paired_disruption | 4 | 0.682 | 0.189 | 0.462 | 0.789 | ok |
| `closed_poi_replacement` | poi_closure | 4 | 0.25 | 0.433 | 1.0 | 0.721 | ok |
| `closed_study_spot_replacement` | poi_closure | 4 | 0.688 | 0.297 | 0.75 | 0.883 | ok |
| `avoid_crowd_event` | preference_constraint | 4 | 0.375 | 0.217 | 0.5 | 0.864 | ok |
| `social_copresence_decoy_location` | social_outcome | 6 | 0.526 | 0.37 | 1.0 | 0.389 | ok |
| `social_copresence_event_window` | social_outcome | 6 | 0.5 | 0.5 | 1.0 | 0.84 | ok |
| `social_copresence_message_gated` | social_outcome | 6 | 0.487 | 0.379 | 1.0 | 0.41 | ok |
| `social_copresence_open_meet` | social_outcome | 6 | 0.556 | 0.458 | 1.0 | 0.873 | ok |
| `social_copresence_two_party` | social_outcome | 6 | 0.417 | 0.449 | 1.0 | 0.782 | ok |
| `social_copresence_with_errand` | social_outcome | 6 | 0.745 | 0.385 | 1.0 | 0.861 | ok |
| `hard_stale_plan_override` | social_outcome_hard | 6 | 0.555 | 0.287 | 0.889 | 0.131 | ok |
| `hard_three_meeting_relay` | social_outcome_hard | 6 | 0.676 | 0.259 | 0.722 | 0.832 | ok |
| `hard_deadline_then_meet` | social_outcome_hard | 6 | 0.569 | 0.261 | 0.667 | 0.858 | ok |
| `hard_budget_entangled_meet` | social_outcome_hard | 6 | 0.596 | 0.195 | 0.615 | 0.819 | ok |
| `hard_full_evening_chain` | social_outcome_hard | 6 | 0.716 | 0.196 | 0.488 | 0.66 | ok |
| `hard_overlapping_windows` | social_outcome_hard | 6 | 0.444 | 0.133 | 0.417 | 0.848 | ok |
| `conflicting_social_obligation` | social_spatial_tradeoff | 4 | 0.5 | 0.358 | 1.0 | 0.156 | ok |
| `school_pickup_social_detour` | social_spatial_tradeoff | 4 | 0.792 | 0.361 | 0.833 | 0.858 | ok |
| `lunch_meeting_time_pressure` | time_pressure | 4 | 0.25 | 0.433 | 1.0 | 0.721 | ok |
| `meeting_wait_trap` | time_pressure | 4 | 0.231 | 0.133 | 0.308 | -0.759 | anti-correlated |

**Informative scenarios: 30/30** (range ≥ 0.15, not at ceiling or floor).

## Reading

**No dead items.** All 30 scenarios discriminate (range ≥ 0.15) and none sits at
ceiling or floor across policies. The scenario set is healthy; nothing needs to be
cut for being uninformative.

**One red flag — `meeting_wait_trap`, item-total r = −0.759.** It ranks policies
*against* the overall ordering: policies that are strong on the benchmark as a
whole do worse here. It also has the lowest discrimination (range 0.308) and the
lowest mean (0.231). A correlation that strongly negative is not noise — the item
measures something other than what the rest of the benchmark measures.

A likely cause is known: this is the scenario whose co-presence is gated behind a
`send_message` condition, and E4 showed GATSim's adapter cannot emit a `message`
action at all. An item that is unreachable-by-construction for some scaffolds
tests *action-surface coverage*, not decision quality, which would invert the
ranking exactly this way. It should either be reported separately or excluded
from aggregate scores, and any per-policy claim resting on it needs the E4 caveat.

**Three weakly-correlated items** — `hard_stale_plan_override` (0.13),
`conflicting_social_obligation` (0.16), and the decoy / message-gated co-presence
pair (≈0.39–0.41) — may be measuring separable dimensions rather than a single
underlying ability. Worth checking before reporting a single aggregate score as if
the benchmark were unidimensional.
