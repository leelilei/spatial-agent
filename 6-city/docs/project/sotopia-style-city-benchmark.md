# Sotopia-Style City Benchmark Sketch

Date: 2026-06-22

Working name: **CityIntent**.

Earlier shorthand used a SOTOPIA-derived name because the benchmark borrows
SOTOPIA's private-goal interactive evaluation pattern. We should not use that as
the final name: it makes the contribution sound like a SOTOPIA extension rather
than an independent benchmark for intention-driven urban agency.

## Why SOTOPIA Is the Right Analogy

SOTOPIA is useful because it does not evaluate agents through static QA. It creates an interactive episode:

```text
scenario context
+ characters
+ relationships
+ private goals
+ multi-turn interaction
+ multi-dimensional evaluation
```

For citysim agents, the analogous structure should be:

```text
urban scenario context
+ agents / personas
+ relationships and social anchors
+ private intentions / needs
+ spatial environment with constraints
+ multi-step movement and interaction episode
+ multi-dimensional evaluation
```

The important transfer is not "make agents chat more." The important transfer is:

> Give each agent a private goal under a shared scenario, let them act in an environment, then evaluate more than final task success.

## Mapping SOTOPIA to City Agents

| SOTOPIA concept | City benchmark analogue |
|---|---|
| Social scenario | Urban situation: commute disruption, public event, facility closure, social invitation, limited time window |
| Character profile | Resident persona: job, home, routines, preferences, mobility constraints, budget |
| Relationship | Social graph: friend, colleague, family, stranger, weak tie |
| Private social goal | Private urban intention: meet friend, avoid crowd, save money, explore, get work done, maintain routine |
| Shared context | City state visible to everyone: time, weather, map, public events |
| Partial observability | Agent-specific memories, beliefs about POIs, private plans, local observations |
| Actions | move, wait, enter POI, talk, invite, buy, reroute, ask info, abandon plan |
| Episode | Simulated time window: 2-8 hours, or one day |
| SOTOPIA-EVAL | CityAgency-EVAL: goal, feasibility, spatial sensitivity, relationship, consistency, cost, believability |

## What We Should Copy

1. **Scenario-first design**

   Each benchmark item should be a scenario package, not just a map. The package includes world layout, time, events, agents, goals, constraints, and scoring rules.

2. **Private goals**

   If all goals are public, the benchmark becomes path planning. Private goals create social and strategic behavior: an agent may want to meet someone, avoid someone, keep a promise, or preserve a relationship.

3. **Multi-dimensional scores**

   SOTOPIA is strong because it does not only score goal completion. We need the same move. A city agent can complete a goal while violating time, spatial, social, or budget constraints.

4. **Hard subset**

   SOTOPIA-hard is a useful idea. We can later define CityAgency-hard: scenarios where strong models fail because spatial cost, social goals, memory, and time pressure conflict.

5. **Human/LLM judge calibration**

   We can use deterministic metrics for spatial feasibility, then use LLM judges only for soft dimensions such as believability or relationship change. This is safer than using LLM judges for everything.

## What We Must Change

SOTOPIA episodes are mostly dialogue-centered and short. City agency needs an explicit environment loop:

```text
observe -> choose intention/action -> environment validates -> move/time passes -> observe outcome -> update memory
```

The environment should own truth:

- shortest path and travel time
- POI opening hours and capacity
- agent location
- co-presence
- events and disruptions
- budget and time constraints

The LLM should not be allowed to invent success. It can choose an intention and explain why; the simulator decides whether the action is possible.

## Candidate Evaluation Dimensions

| Dimension | Range | Mostly automatic? | Meaning |
|---|---:|---|---|
| Goal completion | 0-10 | mixed | Did the agent satisfy its private intention or assigned task? |
| Spatial feasibility | 0-10 | yes | Were movements physically possible under the map and time budget? |
| Constraint compliance | -10-0 | yes | Did the agent violate opening hours, budget, capacity, privacy, or role constraints? |
| Spatial sensitivity | 0-10 | yes/mixed | Did behavior change appropriately when layout, distance, congestion, or POI access changed? |
| Adaptation / replanning | 0-10 | mixed | Did the agent recover from closures, delays, missed meetings, or unexpected encounters? |
| Persona consistency | 0-10 | mixed | Did actions align with stated preferences, habits, mobility limits, and prior choices? |
| Relationship outcome | -5-5 | mixed | Did interactions preserve, improve, or damage relationships? |
| Believability | 0-10 | LLM/human | Does the trajectory look like plausible urban behavior? |
| Cost efficiency | 0-10 | yes | Token/API cost and number of unnecessary LLM calls for a comparable outcome |

## First Benchmark Families

### Family A: Spatial Layout Sensitivity

Question:

> Holding agents and facilities constant, do different spatial layouts produce stable and explainable differences in movement and encounter patterns?

Controlled variables:

- same POIs
- same agents
- same social graph
- same private goals
- different graph layout: central plaza, linear corridor, clustered neighborhoods, bottleneck bridge

Metrics:

- encounters per agent
- weak-tie formation
- average travel time
- missed appointments
- POI diversity
- layout effect size across repeated seeds

### Family B: Intention Conflict

Question:

> When internal needs conflict with spatial cost and social obligations, does the agent make stable, explainable choices?

Example:

- Agent is tired and hungry.
- Friend invites them to a distant event.
- A nearby cafe is cheaper but boring.
- A favored cafe is far and crowded.

Metrics:

- decision trace quality
- consistency across paraphrased prompts
- appropriate tradeoff between need, memory, distance, and relationship

### Family C: Disruption and Replanning

Question:

> Can agents recover from environment changes without hallucinating impossible actions?

Examples:

- subway disruption
- closed store
- public event causing crowding
- route blocked
- friend changes meeting place

Metrics:

- recovery success
- invalid action rate
- time-to-replan
- final goal completion

### Family D: Social Encounter in Space

Question:

> Do spatial encounters create meaningful relationship and information dynamics?

Examples:

- two acquaintances repeatedly meet in a central public space
- a private rumor spreads faster in a compact layout
- a dispersed layout reduces accidental meetings but increases intentional trips

Metrics:

- relationship network change
- information spread rate
- privacy leakage
- encounter-to-interaction conversion rate

## Scenario Package Schema Draft

```json
{
  "benchmark_id": "city_agency_v0",
  "seed_id": "seed_0001",
  "scenario_id": "layout_sensitivity_plaza_001",
  "world": {
    "layout_id": "central_plaza",
    "nodes": [],
    "edges": [],
    "pois": [],
    "time_start": "2026-06-22T08:00:00",
    "time_end": "2026-06-22T14:00:00",
    "events": []
  },
  "agents": [
    {
      "agent_id": "agent_mia",
      "home": "home_mia",
      "persona": {},
      "private_goal": "Meet a friend for lunch while minimizing walking and avoiding crowded places.",
      "needs": {},
      "known_places": [],
      "relationships": []
    }
  ],
  "episode": {
    "max_steps": 24,
    "step_minutes": 15,
    "allowed_actions": ["move", "wait", "enter", "talk", "invite", "buy", "ask_info", "leave"]
  },
  "scoring": {
    "required_metrics": ["goal_completion", "spatial_feasibility", "spatial_sensitivity"],
    "hidden_checks": []
  }
}
```

## Key Difference From CitySim

CitySim asks:

> Can we simulate realistic urban behavior at scale?

CityIntent asks:

> Under controlled spatial perturbations, can different agent policies produce stable, explainable, feasible urban behavior?

That is smaller, but sharper.

## MVP Recommendation

Start with Family A and Family C.

Reasons:

- They need the least subjective judging.
- Spatial feasibility and layout sensitivity can be scored automatically.
- They directly test whether the agent is grounded in the environment.
- They avoid overclaiming "human realism" too early.

Minimum MVP:

- 4 layouts
- 20 agents
- 20 POIs
- 10 scenario seeds per family
- 3 policies: fixed schedule, utility policy, LLM intention policy
- automatic scorer for feasibility, travel time, encounter network, goal completion
- optional LLM judge only for explanations and believability

