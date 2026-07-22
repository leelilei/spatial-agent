# Co-Presence Evidence-Gap Anatomy

Why baselines fail co-presence outcomes, by tier and policy. Each cell counts
failed co_presence outcomes attributed to a mechanism. `entered_no_interact`
and `interact_rejected` are the pure 'legal but ineffective' modes: the agent
reached the venue but never converted it into environment-accepted co-presence.

## Easy tier

| Policy | Failed/Total | no_venue_entry | entered_no_interact | interact_rejected | window_overrun | wrong_target | other |
|---|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety` | 17/21 | 6 | 8 | 2 | 1 | 0 | 0 |
| `gatsim` | 6/21 | 0 | 0 | 6 | 0 | 0 | 0 |
| `generative_agents` | 19/21 | 6 | 12 | 0 | 1 | 0 | 0 |
| `plan_and_execute` | 3/21 | 0 | 0 | 2 | 1 | 0 | 0 |
| `react_tool_policy` | 0/21 | 0 | 0 | 0 | 0 | 0 | 0 |
| `sotopia` | 21/21 | 19 | 2 | 0 | 0 | 0 | 0 |

## Hard tier

| Policy | Failed/Total | no_venue_entry | entered_no_interact | interact_rejected | window_overrun | wrong_target | other |
|---|---:|---:|---:|---:|---:|---:|---:|
| `agentsociety` | 23/27 | 10 | 5 | 7 | 1 | 0 | 0 |
| `gatsim` | 6/27 | 0 | 0 | 3 | 3 | 0 | 0 |
| `generative_agents` | 24/27 | 4 | 12 | 5 | 3 | 0 | 0 |
| `plan_and_execute` | 17/27 | 0 | 1 | 7 | 9 | 0 | 0 |
| `react_tool_policy` | 6/27 | 0 | 1 | 1 | 4 | 0 | 0 |
| `sotopia` | 27/27 | 22 | 5 | 0 | 0 | 0 | 0 |

## Exemplar 'legal but ineffective' traces

- **easy/social_copresence_two_party** (plan_and_execute, interact_rejected): feasibility=0.875, messages=0, entered correct venue=['cafe_central'], interact actions issued=1, accepted interactions=[{'with': 'casey', 'minutes': 5, 'time': 756, 'start_time': 756, 'end_time': 761, 'location': 'park'}]
- **easy/social_copresence_two_party** (plan_and_execute, interact_rejected): feasibility=0.778, messages=0, entered correct venue=['cafe_central'], interact actions issued=2, accepted interactions=[{'with': 'casey', 'minutes': 5, 'time': 766, 'start_time': 766, 'end_time': 771, 'location': 'park'}]
- **easy/social_copresence_decoy_location** (gatsim, interact_rejected): feasibility=0.4, messages=0, entered correct venue=['quiet_cafe'], interact actions issued=6, accepted interactions=[]
- **easy/social_copresence_decoy_location** (agentsociety, entered_no_interact): feasibility=0.7, messages=4, entered correct venue=['quiet_cafe'], interact actions issued=0, accepted interactions=[]
- **easy/social_copresence_event_window** (generative_agents, entered_no_interact): feasibility=0.4, messages=0, entered correct venue=['market'], interact actions issued=0, accepted interactions=[]
- **easy/social_copresence_event_window** (agentsociety, interact_rejected): feasibility=0.3, messages=0, entered correct venue=['market'], interact actions issued=1, accepted interactions=[]
- **easy/social_copresence_message_gated** (gatsim, interact_rejected): feasibility=0.75, messages=0, entered correct venue=['quiet_cafe'], interact actions issued=1, accepted interactions=[]
- **easy/social_copresence_message_gated** (agentsociety, entered_no_interact): feasibility=1.0, messages=1, entered correct venue=['quiet_cafe'], interact actions issued=0, accepted interactions=[]
- **easy/social_copresence_open_meet** (generative_agents, entered_no_interact): feasibility=0.778, messages=0, entered correct venue=['park'], interact actions issued=0, accepted interactions=[]
- **easy/social_copresence_open_meet** (agentsociety, interact_rejected): feasibility=0.75, messages=0, entered correct venue=['park'], interact actions issued=1, accepted interactions=[]
- **easy/social_copresence_with_errand** (generative_agents, entered_no_interact): feasibility=0.778, messages=0, entered correct venue=['market'], interact actions issued=0, accepted interactions=[]
- **easy/social_copresence_decoy_location** (gatsim, interact_rejected): feasibility=0.4, messages=0, entered correct venue=['quiet_cafe'], interact actions issued=6, accepted interactions=[]
- **easy/social_copresence_decoy_location** (generative_agents, entered_no_interact): feasibility=0.714, messages=1, entered correct venue=['quiet_cafe'], interact actions issued=0, accepted interactions=[]
- **easy/social_copresence_decoy_location** (agentsociety, entered_no_interact): feasibility=0.5, messages=4, entered correct venue=['quiet_cafe'], interact actions issued=0, accepted interactions=[]
