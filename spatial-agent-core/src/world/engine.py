"""预实验用的轻量模拟引擎。"""

from __future__ import annotations

from dataclasses import dataclass

import networkx as nx
import numpy as np
import pandas as pd


@dataclass(frozen=True)
class ConditionSpec:
    name: str
    perception_weight: float
    movement_weight: float
    sampling_weight: float


CONDITIONS = {
    "C1": ConditionSpec("C1", perception_weight=0.0, movement_weight=0.0, sampling_weight=0.0),
    "C2": ConditionSpec("C2", perception_weight=0.25, movement_weight=0.0, sampling_weight=0.0),
    "C6m": ConditionSpec("C6m", perception_weight=0.7, movement_weight=0.0, sampling_weight=0.0),
    "C6f": ConditionSpec("C6f", perception_weight=0.7, movement_weight=0.55, sampling_weight=0.0),
    "C4": ConditionSpec("C4", perception_weight=0.8, movement_weight=0.6, sampling_weight=0.4),
}


@dataclass
class AgentState:
    agent_id: int
    location: str
    sociability: float
    privacy_need: float
    vigilance: float


class PilotSimulationEngine:
    """用于 preflight / pilot 的可重复轻量模拟器。"""

    def __init__(
        self,
        graph: nx.Graph,
        metrics_frame: pd.DataFrame,
        *,
        num_agents: int,
        num_rounds: int,
        seed: int,
        condition: str,
    ) -> None:
        if condition not in CONDITIONS:
            raise ValueError(f"Unsupported condition: {condition}")
        self.graph = graph
        self.metrics = metrics_frame.set_index("node_id")
        self.num_agents = num_agents
        self.num_rounds = num_rounds
        self.seed = seed
        self.condition = CONDITIONS[condition]
        self.rng = np.random.default_rng(seed)
        self.node_ids = list(self.metrics.index)
        self.node_lookup = {node_id: index for index, node_id in enumerate(self.node_ids)}
        self.agents = self._init_agents()
        self.external_schedule = self.rng.normal(loc=0.0, scale=0.35, size=num_rounds)

    def _init_agents(self) -> list[AgentState]:
        start_locations = self.rng.choice(self.node_ids, size=self.num_agents, replace=True)
        agents = []
        for agent_id in range(self.num_agents):
            agents.append(
                AgentState(
                    agent_id=agent_id,
                    location=str(start_locations[agent_id]),
                    sociability=float(self.rng.uniform(0.2, 0.95)),
                    privacy_need=float(self.rng.uniform(0.15, 0.95)),
                    vigilance=float(self.rng.uniform(0.1, 0.9)),
                )
            )
        return agents

    def run(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        visits: list[dict[str, object]] = []
        events: list[dict[str, object]] = []

        for round_index in range(1, self.num_rounds + 1):
            occupancy: dict[str, list[AgentState]] = {node_id: [] for node_id in self.node_ids}
            for agent in self.agents:
                next_location = self._choose_next_location(agent, round_index)
                agent.location = next_location
                occupancy[next_location].append(agent)
                visits.append(
                    {
                        "round": round_index,
                        "agent_id": agent.agent_id,
                        "location": next_location,
                    }
                )

            for location, colocated_agents in occupancy.items():
                if not colocated_agents:
                    continue
                events.extend(self._sample_events(round_index, location, colocated_agents))

        return pd.DataFrame(visits), pd.DataFrame(events)

    def _choose_next_location(self, agent: AgentState, round_index: int) -> str:
        current = agent.location
        candidates = [current, *self.graph.neighbors(current)]
        noise_scale = 0.28 + max(float(self.external_schedule[round_index - 1]), -0.2)
        scores = []
        for node_id in candidates:
            node = self.graph.nodes[node_id]
            metric = self.metrics.loc[node_id]
            affordance_score = (
                agent.sociability * float(node.get("publicness", 0.0))
                + agent.privacy_need * float(node.get("privacy", 0.0))
                + agent.vigilance * float(node.get("guardedness", 0.0))
            )
            structural_score = (
                agent.sociability * float(metric["integration_norm"])
                + agent.privacy_need * float(metric["mean_depth_norm"])
                + agent.vigilance * float(metric["control_value_norm"])
            )
            stay_bonus = 0.08 if node_id == current else 0.0
            score = (
                affordance_score
                + self.condition.movement_weight * structural_score
                + stay_bonus
                + float(self.rng.normal(0.0, max(noise_scale, 0.05)))
            )
            scores.append(score)
        best_index = int(np.argmax(scores))
        return str(candidates[best_index])

    def _sample_events(
        self,
        round_index: int,
        location: str,
        colocated_agents: list[AgentState],
    ) -> list[dict[str, object]]:
        metric = self.metrics.loc[location]
        occupancy_norm = min(len(colocated_agents) / max(self.num_agents / 2, 1), 1.0)
        events = []

        for agent in colocated_agents:
            scores = {
                "social": (
                    -0.8
                    + 1.25 * agent.sociability
                    + 0.45 * occupancy_norm
                    + 0.25 * float(self.graph.nodes[location].get("publicness", 0.0))
                    + self.condition.perception_weight * 1.1 * float(metric["integration_norm"])
                    + self.condition.sampling_weight * 0.45
                ),
                "privacy": (
                    -1.2
                    + 1.2 * agent.privacy_need
                    + 0.5 * (1 - occupancy_norm)
                    + 0.15 * float(self.graph.nodes[location].get("privacy", 0.0))
                    + self.condition.perception_weight * 1.2 * float(metric["mean_depth_norm"])
                    + self.condition.sampling_weight * 0.35
                ),
                "gatekeeping": (
                    -1.35
                    + 1.35 * agent.vigilance
                    + 0.4 * occupancy_norm
                    + 0.2 * float(self.graph.nodes[location].get("guardedness", 0.0))
                    + self.condition.perception_weight * 1.1 * float(metric["control_value_norm"])
                    + self.condition.sampling_weight * 0.4
                ),
            }
            event_type = max(scores, key=scores.get)
            probability = 1.0 / (1.0 + np.exp(-scores[event_type]))

            if event_type == "social" and len(colocated_agents) < 2:
                continue
            if event_type == "privacy" and len(colocated_agents) > 2:
                continue
            if event_type == "gatekeeping" and self.graph.degree(location) < 2:
                continue
            if float(self.rng.random()) > probability:
                continue

            target_id = None
            if event_type == "social":
                options = [peer.agent_id for peer in colocated_agents if peer.agent_id != agent.agent_id]
                target_id = int(self.rng.choice(options)) if options else None
            events.append(
                {
                    "round": round_index,
                    "agent_id": agent.agent_id,
                    "target_id": target_id,
                    "location": location,
                    "event_type": event_type,
                }
            )

        return events
