# Co-Presence Evidence-Gap Anatomy

Why baselines fail co-presence outcomes, by tier and policy. Each cell counts
failed co_presence outcomes attributed to a mechanism. `entered_no_interact`
and `interact_rejected` are the pure 'legal but ineffective' modes: the agent
reached the venue but never converted it into environment-accepted co-presence.

## Easy tier

| Policy | Failed/Total | no_venue_entry | entered_no_interact | interact_rejected | window_overrun | wrong_target | other |
|---|---:|---:|---:|---:|---:|---:|---:|
| `plan_and_execute` | 3/21 | 0 | 0 | 2 | 1 | 0 | 0 |
| `react_tool_policy` | 0/21 | 0 | 0 | 0 | 0 | 0 | 0 |

## Hard tier

| Policy | Failed/Total | no_venue_entry | entered_no_interact | interact_rejected | window_overrun | wrong_target | other |
|---|---:|---:|---:|---:|---:|---:|---:|
| `plan_and_execute` | 17/27 | 0 | 1 | 7 | 9 | 0 | 0 |
| `react_tool_policy` | 6/27 | 0 | 1 | 1 | 4 | 0 | 0 |

## Exemplar 'legal but ineffective' traces

- **easy/social_copresence_two_party** (plan_and_execute, interact_rejected): feasibility=0.875, messages=0, entered correct venue=['cafe_central'], interact actions issued=1, accepted interactions=[{'with': 'casey', 'minutes': 5, 'time': 756, 'start_time': 756, 'end_time': 761, 'location': 'park'}]
- **easy/social_copresence_two_party** (plan_and_execute, interact_rejected): feasibility=0.778, messages=0, entered correct venue=['cafe_central'], interact actions issued=2, accepted interactions=[{'with': 'casey', 'minutes': 5, 'time': 766, 'start_time': 766, 'end_time': 771, 'location': 'park'}]
- **hard/hard_budget_entangled_meet** (plan_and_execute, interact_rejected): feasibility=0.778, messages=0, entered correct venue=['quiet_cafe'], interact actions issued=1, accepted interactions=[]
- **hard/hard_deadline_then_meet** (plan_and_execute, interact_rejected): feasibility=0.875, messages=0, entered correct venue=['quiet_cafe'], interact actions issued=1, accepted interactions=[]
- **hard/hard_overlapping_windows** (plan_and_execute, interact_rejected): feasibility=0.875, messages=0, entered correct venue=['cafe_central'], interact actions issued=1, accepted interactions=[{'with': 'casey', 'minutes': 10, 'time': 756, 'start_time': 756, 'end_time': 766, 'location': 'park'}]
- **hard/hard_stale_plan_override** (react_tool_policy, interact_rejected): feasibility=0.5, messages=1, entered correct venue=['quiet_cafe'], interact actions issued=4, accepted interactions=[]
- **hard/hard_stale_plan_override** (plan_and_execute, interact_rejected): feasibility=0.833, messages=1, entered correct venue=['quiet_cafe'], interact actions issued=1, accepted interactions=[]
- **hard/hard_deadline_then_meet** (react_tool_policy, entered_no_interact): feasibility=0.875, messages=0, entered correct venue=['quiet_cafe'], interact actions issued=0, accepted interactions=[]
