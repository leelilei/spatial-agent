# CityIntent Blinded Human Audit Packet

Use `RUBRIC.md` and `world_reference.json`. Do not access `sealed/` while annotating.

## H001

Scenario: School Pickup With Social Detour
Episode: 17:00 to 18:35
Persona: Caregiver leaving work who wants to be polite but must not miss school pickup.
Private intention: Pick up the child from school before 18:10, while keeping any social interruption brief.
Start: office; budget: 12

Other agents:

- `ben`: Friend who invites Aria to a theatre event after work. Start: `plaza`. Intention: Invite Aria to join a relaxed evening plan.

Success conditions:

- `pickup_before_deadline`: `{"id": "pickup_before_deadline", "type": "visit_before", "agent": "aria", "location": "school", "deadline": "18:10", "weight": 0.45}`
- `keep_social_brief_if_taken`: `{"id": "keep_social_brief_if_taken", "type": "bounded_social_interaction", "with": "ben", "max_minutes": 8, "weight": 0.2}`
- `avoid_false_theatre_commitment`: `{"id": "avoid_false_theatre_commitment", "type": "no_infeasible_social_commitment", "weight": 0.2}`
- `finish_before_pickup_window_closes`: `{"id": "finish_before_pickup_window_closes", "type": "episode_complete_before", "deadline": "18:35", "weight": 0.15}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 17:00 | office | move | target=school; reason=Generative Agents official adapter action | 17:00 | office | 12.0 |  |
| 2 | 17:00 | office | move | target=school; reason=Generative Agents official adapter action | 17:26 | school | 12.0 |  |
| 3 | 17:26 | school | enter | target=school; reason=Generative Agents official adapter action | 17:27 | school | 12.0 |  |
| 4 | 17:27 | school | dwell | reason=Generative Agents official adapter action | 18:02 | school | 12.0 |  |
| 5 | 18:02 | school | finish | reason=Generative Agents adapted official plan exhausted | 18:02 | school | 12.0 |  |

Final observable state: time 18:02, location school, budget 12.0.

## H002

Scenario: Detour Commute With Mid-Route Block
Episode: 08:00 to 09:30
Persona: Commuter who needs to reach the office but prefers reliable routes over optimistic shortcuts.
Private intention: Reach the office before 09:15 without using a route that becomes blocked mid-commute.
Start: home_aria; budget: 10

Success conditions:

- `reach_office_before_standup`: `{"id": "reach_office_before_standup", "type": "visit_before", "agent": "aria", "location": "office", "deadline": "09:15", "weight": 0.35}`
- `avoid_midroute_block`: `{"id": "avoid_midroute_block", "type": "avoid_blocked_edge", "edge": ["transit_hub", "office"], "time_window": ["08:08", "08:55"], "weight": 0.3}`
- `recover_after_service_alert`: `{"id": "recover_after_service_alert", "type": "replan_after_event", "event_id": "service_alert", "weight": 0.2}`
- `no_impossible_commute_claim`: `{"id": "no_impossible_commute_claim", "type": "no_feasibility_violation", "weight": 0.15}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 08:00 | home_aria | move | target=office; reason=follow GATSim official activity-plan destination | 08:12 | transit_hub | 10.0 | service_alert |
| 2 | 08:12 | transit_hub | move | target=office; reason=follow GATSim official activity-plan destination | 08:30 | office | 10.0 |  |
| 3 | 08:30 | office | enter | target=office; reason=enter the GATSim activity destination | 08:31 | office | 10.0 |  |
| 4 | 08:31 | office | finish | reason=GATSim official activity plan exhausted | 08:31 | office | 10.0 |  |

Final observable state: time 08:31, location office, budget 10.0.

## H003

Scenario: Closed Study Spot Replacement
Episode: 14:00 to 16:30
Persona: Graduate student who needs a quiet work block and dislikes wasting money when a free quiet place is available.
Private intention: Find a quiet open place and complete at least 50 minutes of focused work without entering the temporarily closed library.
Start: plaza; budget: 18

Success conditions:

- `choose_open_quiet_replacement`: `{"id": "choose_open_quiet_replacement", "type": "visit_open_location", "location_any_of": ["bookstore", "quiet_cafe", "coworking"], "time_window": ["14:00", "16:20"], "weight": 0.3}`
- `complete_focus_block`: `{"id": "complete_focus_block", "type": "dwell_minutes", "location_any_of": ["bookstore", "quiet_cafe", "coworking"], "min_minutes": 50, "weight": 0.3}`
- `do_not_enter_closed_library`: `{"id": "do_not_enter_closed_library", "type": "do_not_enter_closed_location", "location": "library", "time_window": ["14:00", "16:00"], "weight": 0.25}`
- `stay_within_budget`: `{"id": "stay_within_budget", "type": "budget_at_least", "agent": "aria", "min_remaining": 0, "weight": 0.15}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 14:00 | plaza | move | target=bookstore; reason=follow GATSim official activity-plan destination | 14:23 | bookstore | 18.0 |  |
| 2 | 14:23 | bookstore | enter | target=bookstore; reason=enter the GATSim activity destination | 14:24 | bookstore | 18.0 |  |
| 3 | 14:24 | bookstore | use_service | target=bookstore; service=workspace_access; reason=pay for access before the GATSim-planned activity | 14:29 | bookstore | 11.0 |  |
| 4 | 14:29 | bookstore | dwell | reason=complete the GATSim-planned activity duration required by the private goal | 15:19 | bookstore | 11.0 |  |
| 5 | 15:19 | bookstore | move | target=plaza; reason=follow GATSim official activity-plan destination | 15:42 | plaza | 11.0 |  |
| 6 | 15:42 | plaza | enter | target=plaza; reason=enter the GATSim activity destination | 15:43 | plaza | 11.0 |  |
| 7 | 15:43 | plaza | finish | reason=GATSim official activity plan exhausted | 15:43 | plaza | 11.0 |  |

Final observable state: time 15:43, location plaza, budget 11.0.

## H004

Scenario: Closed Study Spot Replacement
Episode: 14:00 to 16:30
Persona: Graduate student who needs a quiet work block and dislikes wasting money when a free quiet place is available.
Private intention: Find a quiet open place and complete at least 50 minutes of focused work without entering the temporarily closed library.
Start: plaza; budget: 18

Success conditions:

- `choose_open_quiet_replacement`: `{"id": "choose_open_quiet_replacement", "type": "visit_open_location", "location_any_of": ["bookstore", "quiet_cafe", "coworking"], "time_window": ["14:00", "16:20"], "weight": 0.3}`
- `complete_focus_block`: `{"id": "complete_focus_block", "type": "dwell_minutes", "location_any_of": ["bookstore", "quiet_cafe", "coworking"], "min_minutes": 50, "weight": 0.3}`
- `do_not_enter_closed_library`: `{"id": "do_not_enter_closed_library", "type": "do_not_enter_closed_location", "location": "library", "time_window": ["14:00", "16:00"], "weight": 0.25}`
- `stay_within_budget`: `{"id": "stay_within_budget", "type": "budget_at_least", "agent": "aria", "min_remaining": 0, "weight": 0.15}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 14:00 | plaza | move | target=quiet_cafe; reason=AgentSociety official plan step: Walk to quiet_cafe from the current location | 14:23 | quiet_cafe | 18.0 |  |
| 2 | 14:23 | quiet_cafe | enter | target=quiet_cafe; reason=AgentSociety official plan step: Enter quiet_cafe | 14:24 | quiet_cafe | 18.0 |  |
| 3 | 14:24 | quiet_cafe | dwell | reason=AgentSociety official plan step: Settle in for focused work | 15:14 | quiet_cafe | 18.0 |  |
| 4 | 15:14 | quiet_cafe | dwell | reason=AgentSociety official plan step: Stay in the current quiet place and work continuously | 16:04 | quiet_cafe | 18.0 |  |
| 5 | 16:04 | quiet_cafe | dwell | reason=AgentSociety official plan step: Continue focused work at the current quiet location | 16:19 | quiet_cafe | 18.0 |  |
| 6 | 16:19 | quiet_cafe | dwell | reason=AgentSociety official plan step: Continue focused work at the current quiet cafe | 16:20 | quiet_cafe | 18.0 |  |
| 7 | 16:20 | quiet_cafe | dwell | reason=AgentSociety official plan step: Remain at the quiet cafe for focused work | 16:35 | quiet_cafe | 18.0 |  |

Final observable state: time 16:35, location quiet_cafe, budget 18.0.

## H005

Scenario: Meeting Wait Trap
Episode: 12:05 to 13:15
Persona: Office worker trying to coordinate a short lunch meeting without wasting the whole break.
Private intention: Confirm Ben's location, meet during the narrow lunch window, and avoid just waiting without achieving co-presence.
Start: office; budget: 16

Other agents:

- `ben`: Friend with a short lunch break who will only commit after receiving a message. Start: `home_ben`. Intention: Meet Aria if the plan is confirmed early.

Success conditions:

- `confirm_plan_with_ben`: `{"id": "confirm_plan_with_ben", "type": "send_message", "to": "ben", "weight": 0.2}`
- `meet_ben_during_window`: `{"id": "meet_ben_during_window", "type": "co_presence", "agents": ["aria", "ben"], "location_any_of": ["quiet_cafe", "cafe_central"], "time_window": ["12:35", "12:55"], "weight": 0.45}`
- `stay_within_budget`: `{"id": "stay_within_budget", "type": "budget_at_least", "agent": "aria", "min_remaining": 0, "weight": 0.15}`
- `no_impossible_meeting_claim`: `{"id": "no_impossible_meeting_claim", "type": "no_feasibility_violation", "weight": 0.2}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 12:05 | office | message | to=ben; content=Can you confirm your location for lunch? I can meet at cafe_central if that works, and I’ll head there now once you reply.; reason=Generative Agents official adapter action | 12:07 | office | 16.0 |  |
| 2 | 12:07 | office | move | target=cafe_central; reason=Generative Agents official adapter action | 12:13 | cafe_central | 16.0 |  |
| 3 | 12:13 | cafe_central | enter | target=cafe_central; reason=Generative Agents official adapter action | 12:14 | cafe_central | 16.0 |  |
| 4 | 12:14 | cafe_central | use_service | target=cafe_central; service=meal; reason=Generative Agents official adapter action | 12:19 | cafe_central | 4.0 |  |
| 5 | 12:19 | cafe_central | dwell | reason=Generative Agents official adapter action | 12:44 | cafe_central | 4.0 |  |
| 6 | 12:44 | cafe_central | dwell | reason=Generative Agents official adapter action | 12:55 | cafe_central | 4.0 |  |
| 7 | 12:55 | cafe_central | message | to=ben; content=I’m still at cafe_central. Are you able to meet here before 13:15?; reason=Generative Agents official adapter action | 12:57 | cafe_central | 4.0 |  |
| 8 | 12:57 | cafe_central | dwell | reason=Generative Agents official adapter action | 13:12 | cafe_central | 4.0 |  |

Final observable state: time 13:12, location cafe_central, budget 4.0.

## H006

Scenario: School Pickup With Social Detour
Episode: 17:00 to 18:35
Persona: Caregiver leaving work who wants to be polite but must not miss school pickup.
Private intention: Pick up the child from school before 18:10, while keeping any social interruption brief.
Start: office; budget: 12

Other agents:

- `ben`: Friend who invites Aria to a theatre event after work. Start: `plaza`. Intention: Invite Aria to join a relaxed evening plan.

Success conditions:

- `pickup_before_deadline`: `{"id": "pickup_before_deadline", "type": "visit_before", "agent": "aria", "location": "school", "deadline": "18:10", "weight": 0.45}`
- `keep_social_brief_if_taken`: `{"id": "keep_social_brief_if_taken", "type": "bounded_social_interaction", "with": "ben", "max_minutes": 8, "weight": 0.2}`
- `avoid_false_theatre_commitment`: `{"id": "avoid_false_theatre_commitment", "type": "no_infeasible_social_commitment", "weight": 0.2}`
- `finish_before_pickup_window_closes`: `{"id": "finish_before_pickup_window_closes", "type": "episode_complete_before", "deadline": "18:35", "weight": 0.15}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 17:00 | office | move | target=school; reason=AgentSociety official plan step: Leave office and go directly to school | 17:26 | school | 12.0 |  |
| 2 | 17:26 | school | enter | target=school; reason=AgentSociety official plan step: Arrive at school entrance | 17:27 | school | 12.0 |  |
| 3 | 17:27 | school | finish | reason=AgentSociety adapted official plan exhausted | 17:27 | school | 12.0 |  |

Final observable state: time 17:27, location school, budget 12.0.

## H007

Scenario: Detour Commute With Mid-Route Block
Episode: 08:00 to 09:30
Persona: Commuter who needs to reach the office but prefers reliable routes over optimistic shortcuts.
Private intention: Reach the office before 09:15 without using a route that becomes blocked mid-commute.
Start: home_aria; budget: 10

Success conditions:

- `reach_office_before_standup`: `{"id": "reach_office_before_standup", "type": "visit_before", "agent": "aria", "location": "office", "deadline": "09:15", "weight": 0.35}`
- `avoid_midroute_block`: `{"id": "avoid_midroute_block", "type": "avoid_blocked_edge", "edge": ["transit_hub", "office"], "time_window": ["08:08", "08:55"], "weight": 0.3}`
- `recover_after_service_alert`: `{"id": "recover_after_service_alert", "type": "replan_after_event", "event_id": "service_alert", "weight": 0.2}`
- `no_impossible_commute_claim`: `{"id": "no_impossible_commute_claim", "type": "no_feasibility_violation", "weight": 0.15}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 08:00 | home_aria | move | target=transit_hub; reason=AgentSociety official plan step: Leave home and go to the transit hub | 08:12 | transit_hub | 10.0 |  |
| 2 | 08:12 | transit_hub | move | target=coworking; reason=AgentSociety official plan step: Move to a reliable alternate location | 08:38 | coworking | 10.0 |  |
| 3 | 08:38 | coworking | enter | target=coworking; reason=AgentSociety official plan step: Enter the coworking space | 08:39 | coworking | 10.0 |  |
| 4 | 08:39 | coworking | move | target=office; reason=AgentSociety official plan step: Continue to the office | 08:47 | office | 10.0 |  |
| 5 | 08:47 | office | enter | target=office; reason=AgentSociety official plan step: Arrive at the office before the deadline | 08:48 | office | 10.0 |  |
| 6 | 08:48 | office | finish | reason=AgentSociety adapted official plan exhausted | 08:48 | office | 10.0 |  |

Final observable state: time 08:48, location office, budget 10.0.

## H008

Scenario: Closed Study Spot Replacement
Episode: 14:00 to 16:30
Persona: Graduate student who needs a quiet work block and dislikes wasting money when a free quiet place is available.
Private intention: Find a quiet open place and complete at least 50 minutes of focused work without entering the temporarily closed library.
Start: plaza; budget: 18

Success conditions:

- `choose_open_quiet_replacement`: `{"id": "choose_open_quiet_replacement", "type": "visit_open_location", "location_any_of": ["bookstore", "quiet_cafe", "coworking"], "time_window": ["14:00", "16:20"], "weight": 0.3}`
- `complete_focus_block`: `{"id": "complete_focus_block", "type": "dwell_minutes", "location_any_of": ["bookstore", "quiet_cafe", "coworking"], "min_minutes": 50, "weight": 0.3}`
- `do_not_enter_closed_library`: `{"id": "do_not_enter_closed_library", "type": "do_not_enter_closed_location", "location": "library", "time_window": ["14:00", "16:00"], "weight": 0.25}`
- `stay_within_budget`: `{"id": "stay_within_budget", "type": "budget_at_least", "agent": "aria", "min_remaining": 0, "weight": 0.15}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 14:00 | plaza | move | target=bookstore; reason=Generative Agents official adapter action | 14:00 | plaza | 18.0 |  |
| 2 | 14:00 | plaza | move | target=bookstore; reason=Generative Agents official adapter action | 14:23 | bookstore | 18.0 |  |
| 3 | 14:23 | bookstore | enter | target=bookstore; reason=Generative Agents official adapter action | 14:24 | bookstore | 18.0 |  |
| 4 | 14:24 | bookstore | dwell | reason=Generative Agents official adapter action | 15:59 | bookstore | 18.0 |  |
| 5 | 15:59 | bookstore | dwell | reason=Generative Agents official adapter action | 16:30 | bookstore | 18.0 |  |

Final observable state: time 16:30, location bookstore, budget 18.0.

## H009

Scenario: Detour Commute With Mid-Route Block
Episode: 08:00 to 09:30
Persona: Commuter who needs to reach the office but prefers reliable routes over optimistic shortcuts.
Private intention: Reach the office before 09:15 without using a route that becomes blocked mid-commute.
Start: home_aria; budget: 10

Success conditions:

- `reach_office_before_standup`: `{"id": "reach_office_before_standup", "type": "visit_before", "agent": "aria", "location": "office", "deadline": "09:15", "weight": 0.35}`
- `avoid_midroute_block`: `{"id": "avoid_midroute_block", "type": "avoid_blocked_edge", "edge": ["transit_hub", "office"], "time_window": ["08:08", "08:55"], "weight": 0.3}`
- `recover_after_service_alert`: `{"id": "recover_after_service_alert", "type": "replan_after_event", "event_id": "service_alert", "weight": 0.2}`
- `no_impossible_commute_claim`: `{"id": "no_impossible_commute_claim", "type": "no_feasibility_violation", "weight": 0.15}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 08:00 | home_aria | move | target=transit_hub; reason=SOTOPIA physical action | 08:12 | transit_hub | 10.0 |  |
| 2 | 08:12 | transit_hub | move | target=office; reason=SOTOPIA physical action | 08:30 | office | 10.0 |  |
| 3 | 08:30 | office | finish | reason=SOTOPIA chose to stop or leave | 08:30 | office | 10.0 |  |

Final observable state: time 08:30, location office, budget 10.0.

## H010

Scenario: School Pickup With Social Detour
Episode: 17:00 to 18:35
Persona: Caregiver leaving work who wants to be polite but must not miss school pickup.
Private intention: Pick up the child from school before 18:10, while keeping any social interruption brief.
Start: office; budget: 12

Other agents:

- `ben`: Friend who invites Aria to a theatre event after work. Start: `plaza`. Intention: Invite Aria to join a relaxed evening plan.

Success conditions:

- `pickup_before_deadline`: `{"id": "pickup_before_deadline", "type": "visit_before", "agent": "aria", "location": "school", "deadline": "18:10", "weight": 0.45}`
- `keep_social_brief_if_taken`: `{"id": "keep_social_brief_if_taken", "type": "bounded_social_interaction", "with": "ben", "max_minutes": 8, "weight": 0.2}`
- `avoid_false_theatre_commitment`: `{"id": "avoid_false_theatre_commitment", "type": "no_infeasible_social_commitment", "weight": 0.2}`
- `finish_before_pickup_window_closes`: `{"id": "finish_before_pickup_window_closes", "type": "episode_complete_before", "deadline": "18:35", "weight": 0.15}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 17:00 | office | move | target=school; reason=follow GATSim official activity-plan destination | 17:26 | school | 12.0 |  |
| 2 | 17:26 | school | enter | target=school; reason=enter the GATSim activity destination | 17:27 | school | 12.0 |  |
| 3 | 17:27 | school | move | target=home_ben; reason=follow GATSim official activity-plan destination | 17:35 | home_ben | 12.0 |  |
| 4 | 17:35 | home_ben | enter | target=home_ben; reason=enter the GATSim activity destination | 17:36 | home_ben | 12.0 |  |
| 5 | 17:36 | home_ben | finish | reason=GATSim official activity plan exhausted | 17:36 | home_ben | 12.0 |  |

Final observable state: time 17:36, location home_ben, budget 12.0.

## H011

Scenario: Meeting Wait Trap
Episode: 12:05 to 13:15
Persona: Office worker trying to coordinate a short lunch meeting without wasting the whole break.
Private intention: Confirm Ben's location, meet during the narrow lunch window, and avoid just waiting without achieving co-presence.
Start: office; budget: 16

Other agents:

- `ben`: Friend with a short lunch break who will only commit after receiving a message. Start: `home_ben`. Intention: Meet Aria if the plan is confirmed early.

Success conditions:

- `confirm_plan_with_ben`: `{"id": "confirm_plan_with_ben", "type": "send_message", "to": "ben", "weight": 0.2}`
- `meet_ben_during_window`: `{"id": "meet_ben_during_window", "type": "co_presence", "agents": ["aria", "ben"], "location_any_of": ["quiet_cafe", "cafe_central"], "time_window": ["12:35", "12:55"], "weight": 0.45}`
- `stay_within_budget`: `{"id": "stay_within_budget", "type": "budget_at_least", "agent": "aria", "min_remaining": 0, "weight": 0.15}`
- `no_impossible_meeting_claim`: `{"id": "no_impossible_meeting_claim", "type": "no_feasibility_violation", "weight": 0.2}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 12:05 | office | message | to=ben; content=Where should we meet for lunch today? I can be at Quiet Cafe around 12:35.; reason=AgentSociety official plan step: Message Ben to confirm his lunch location and timing | 12:07 | office | 16.0 |  |
| 2 | 12:07 | office | move | target=quiet_cafe; reason=AgentSociety official plan step: Travel from office to Quiet Cafe | 12:28 | quiet_cafe | 16.0 |  |
| 3 | 12:28 | quiet_cafe | message | to=ben; content=I'm at Quiet Cafe now and can meet there between 12:35 and 12:55. Can you confirm where you'll be?; reason=AgentSociety official plan step: Confirm Ben's lunch plan and location by message | 12:30 | quiet_cafe | 16.0 |  |
| 4 | 12:30 | quiet_cafe | dwell | reason=AgentSociety official plan step: Stay at the meeting point until the lunch window starts | 12:37 | quiet_cafe | 16.0 |  |
| 5 | 12:37 | quiet_cafe | message | to=ben; content=I'm at quiet_cafe now. Can you confirm you'll meet me there before 12:55?; reason=AgentSociety official plan step: Confirm Ben's lunch location and ask for co-presence at quiet_cafe | 12:39 | quiet_cafe | 16.0 |  |
| 6 | 12:39 | quiet_cafe | dwell | reason=AgentSociety official plan step: Stay at quiet_cafe and wait briefly for Ben's confirmation | 12:44 | quiet_cafe | 16.0 |  |
| 7 | 12:44 | quiet_cafe | message | to=ben; content=I'm at quiet_cafe now and staying here until 12:55. Please confirm if you'll meet me here.; reason=AgentSociety official plan step: Send a final confirmation message to Ben about meeting at Quiet Cafe before 12:55 | 12:46 | quiet_cafe | 16.0 |  |
| 8 | 12:46 | quiet_cafe | dwell | reason=AgentSociety official plan step: Stay at Quiet Cafe briefly for Ben to arrive and establish co-presence | 12:56 | quiet_cafe | 16.0 |  |

Final observable state: time 12:56, location quiet_cafe, budget 16.0.

## H012

Scenario: Detour Commute With Mid-Route Block
Episode: 08:00 to 09:30
Persona: Commuter who needs to reach the office but prefers reliable routes over optimistic shortcuts.
Private intention: Reach the office before 09:15 without using a route that becomes blocked mid-commute.
Start: home_aria; budget: 10

Success conditions:

- `reach_office_before_standup`: `{"id": "reach_office_before_standup", "type": "visit_before", "agent": "aria", "location": "office", "deadline": "09:15", "weight": 0.35}`
- `avoid_midroute_block`: `{"id": "avoid_midroute_block", "type": "avoid_blocked_edge", "edge": ["transit_hub", "office"], "time_window": ["08:08", "08:55"], "weight": 0.3}`
- `recover_after_service_alert`: `{"id": "recover_after_service_alert", "type": "replan_after_event", "event_id": "service_alert", "weight": 0.2}`
- `no_impossible_commute_claim`: `{"id": "no_impossible_commute_claim", "type": "no_feasibility_violation", "weight": 0.15}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 08:00 | home_aria | move | target=office; reason=Generative Agents official adapter action | 08:12 | transit_hub | 10.0 | service_alert |
| 2 | 08:12 | transit_hub | move | target=park; reason=Generative Agents official adapter action | 08:12 | transit_hub | 10.0 |  |
| 3 | 08:12 | transit_hub | dwell | reason=Generative Agents official adapter action | 08:55 | transit_hub | 10.0 |  |
| 4 | 08:55 | transit_hub | move | target=office; reason=Generative Agents official adapter action | 09:09 | office | 10.0 |  |
| 5 | 09:09 | office | enter | target=office; reason=Generative Agents official adapter action | 09:10 | office | 10.0 |  |
| 6 | 09:10 | office | finish | reason=Generative Agents adapted official plan exhausted | 09:10 | office | 10.0 |  |

Final observable state: time 09:10, location office, budget 10.0.

## H013

Scenario: Meeting Wait Trap
Episode: 12:05 to 13:15
Persona: Office worker trying to coordinate a short lunch meeting without wasting the whole break.
Private intention: Confirm Ben's location, meet during the narrow lunch window, and avoid just waiting without achieving co-presence.
Start: office; budget: 16

Other agents:

- `ben`: Friend with a short lunch break who will only commit after receiving a message. Start: `home_ben`. Intention: Meet Aria if the plan is confirmed early.

Success conditions:

- `confirm_plan_with_ben`: `{"id": "confirm_plan_with_ben", "type": "send_message", "to": "ben", "weight": 0.2}`
- `meet_ben_during_window`: `{"id": "meet_ben_during_window", "type": "co_presence", "agents": ["aria", "ben"], "location_any_of": ["quiet_cafe", "cafe_central"], "time_window": ["12:35", "12:55"], "weight": 0.45}`
- `stay_within_budget`: `{"id": "stay_within_budget", "type": "budget_at_least", "agent": "aria", "min_remaining": 0, "weight": 0.15}`
- `no_impossible_meeting_claim`: `{"id": "no_impossible_meeting_claim", "type": "no_feasibility_violation", "weight": 0.2}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 12:05 | office | move | target=quiet_cafe; reason=follow GATSim official activity-plan destination | 12:26 | quiet_cafe | 16.0 |  |
| 2 | 12:26 | quiet_cafe | enter | target=quiet_cafe; reason=enter the GATSim activity destination | 12:27 | quiet_cafe | 16.0 |  |
| 3 | 12:27 | quiet_cafe | finish | reason=GATSim official activity plan exhausted | 12:27 | quiet_cafe | 16.0 |  |

Final observable state: time 12:27, location quiet_cafe, budget 16.0.

## H014

Scenario: Closed Study Spot Replacement
Episode: 14:00 to 16:30
Persona: Graduate student who needs a quiet work block and dislikes wasting money when a free quiet place is available.
Private intention: Find a quiet open place and complete at least 50 minutes of focused work without entering the temporarily closed library.
Start: plaza; budget: 18

Success conditions:

- `choose_open_quiet_replacement`: `{"id": "choose_open_quiet_replacement", "type": "visit_open_location", "location_any_of": ["bookstore", "quiet_cafe", "coworking"], "time_window": ["14:00", "16:20"], "weight": 0.3}`
- `complete_focus_block`: `{"id": "complete_focus_block", "type": "dwell_minutes", "location_any_of": ["bookstore", "quiet_cafe", "coworking"], "min_minutes": 50, "weight": 0.3}`
- `do_not_enter_closed_library`: `{"id": "do_not_enter_closed_library", "type": "do_not_enter_closed_location", "location": "library", "time_window": ["14:00", "16:00"], "weight": 0.25}`
- `stay_within_budget`: `{"id": "stay_within_budget", "type": "budget_at_least", "agent": "aria", "min_remaining": 0, "weight": 0.15}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 14:00 | plaza | move | target=bookstore; reason=SOTOPIA physical action | 14:23 | bookstore | 18.0 |  |
| 2 | 14:23 | bookstore | dwell | reason=SOTOPIA physical action | 15:13 | bookstore | 18.0 |  |
| 3 | 15:13 | bookstore | finish | reason=SOTOPIA chose to stop or leave | 15:13 | bookstore | 18.0 |  |

Final observable state: time 15:13, location bookstore, budget 18.0.

## H015

Scenario: Meeting Wait Trap
Episode: 12:05 to 13:15
Persona: Office worker trying to coordinate a short lunch meeting without wasting the whole break.
Private intention: Confirm Ben's location, meet during the narrow lunch window, and avoid just waiting without achieving co-presence.
Start: office; budget: 16

Other agents:

- `ben`: Friend with a short lunch break who will only commit after receiving a message. Start: `home_ben`. Intention: Meet Aria if the plan is confirmed early.

Success conditions:

- `confirm_plan_with_ben`: `{"id": "confirm_plan_with_ben", "type": "send_message", "to": "ben", "weight": 0.2}`
- `meet_ben_during_window`: `{"id": "meet_ben_during_window", "type": "co_presence", "agents": ["aria", "ben"], "location_any_of": ["quiet_cafe", "cafe_central"], "time_window": ["12:35", "12:55"], "weight": 0.45}`
- `stay_within_budget`: `{"id": "stay_within_budget", "type": "budget_at_least", "agent": "aria", "min_remaining": 0, "weight": 0.15}`
- `no_impossible_meeting_claim`: `{"id": "no_impossible_meeting_claim", "type": "no_feasibility_violation", "weight": 0.2}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 12:05 | office | message | to=ben; content=Are you free for lunch? I can meet at cafe_central or quiet_cafe. If you're already on the move, tell me where you are and I'll head there; otherwise let's pick one now and meet between 12:35 and 12:55.; reason=SOTOPIA physical action | 12:07 | office | 16.0 |  |
| 2 | 12:07 | office | message | to=ben; content=I’m leaving the office now and heading to quiet_cafe. If you can make 12:35-12:55, meet me there; if you’re already closer to cafe_central, send your location and I’ll adjust, but I don’t want to wait around.; reason=SOTOPIA physical action | 12:09 | office | 16.0 |  |
| 3 | 12:09 | office | move | target=transit_hub; reason=SOTOPIA physical action | 12:23 | transit_hub | 16.0 |  |
| 4 | 12:23 | transit_hub | message | to=ben; content=I’m at transit_hub now. Are you heading to cafe_central or quiet_cafe? I can leave here and meet you at whichever you’ll actually reach by 12:35-12:55, but I need your location so I’m not waiting at the wrong place.; reason=SOTOPIA physical action | 12:25 | transit_hub | 16.0 |  |
| 5 | 12:25 | transit_hub | move | target=cafe_central; reason=SOTOPIA physical action | 12:37 | cafe_central | 16.0 |  |
| 6 | 12:37 | cafe_central | message | to=ben; content=I'm at cafe_central now. If you're close enough to make it by 12:55, come here; otherwise send your location so I can decide whether to switch, but I need to avoid waiting in the wrong place.; reason=SOTOPIA physical action | 12:39 | cafe_central | 16.0 |  |
| 7 | 12:39 | cafe_central | message | to=ben; content=I'm at cafe_central now. Can you confirm where you are and whether you can make it here by 12:55? If not, send your exact location now and I’ll decide whether to switch to quiet_cafe or wrap it up.; reason=SOTOPIA physical action | 12:41 | cafe_central | 16.0 |  |
| 8 | 12:41 | cafe_central | message | to=ben; content=I'm at cafe_central now. Please send your exact location and whether you can still make it here by 12:55; if not, tell me now and I’ll decide whether to switch to quiet_cafe, but I’m not waiting here without a confirmed plan.; reason=SOTOPIA physical action | 12:43 | cafe_central | 16.0 |  |

Final observable state: time 12:43, location cafe_central, budget 16.0.

## H016

Scenario: School Pickup With Social Detour
Episode: 17:00 to 18:35
Persona: Caregiver leaving work who wants to be polite but must not miss school pickup.
Private intention: Pick up the child from school before 18:10, while keeping any social interruption brief.
Start: office; budget: 12

Other agents:

- `ben`: Friend who invites Aria to a theatre event after work. Start: `plaza`. Intention: Invite Aria to join a relaxed evening plan.

Success conditions:

- `pickup_before_deadline`: `{"id": "pickup_before_deadline", "type": "visit_before", "agent": "aria", "location": "school", "deadline": "18:10", "weight": 0.45}`
- `keep_social_brief_if_taken`: `{"id": "keep_social_brief_if_taken", "type": "bounded_social_interaction", "with": "ben", "max_minutes": 8, "weight": 0.2}`
- `avoid_false_theatre_commitment`: `{"id": "avoid_false_theatre_commitment", "type": "no_infeasible_social_commitment", "weight": 0.2}`
- `finish_before_pickup_window_closes`: `{"id": "finish_before_pickup_window_closes", "type": "episode_complete_before", "deadline": "18:35", "weight": 0.15}`

| step | time | from | action | target/detail | end | location | budget | interruption |
|---:|---|---|---|---|---|---|---:|---|
| 1 | 17:00 | office | move | target=budget_diner; reason=SOTOPIA physical action | 17:20 | budget_diner | 12.0 |  |
| 2 | 17:20 | budget_diner | move | target=school; reason=SOTOPIA physical action | 17:26 | school | 12.0 |  |
| 3 | 17:26 | school | finish | reason=SOTOPIA chose to stop or leave | 17:26 | school | 12.0 |  |

Final observable state: time 17:26, location school, budget 12.0.
