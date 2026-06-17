#!/usr/bin/env python3
"""Minimal multi-agent social simulation for SMGA.

The diagnostic_v0 harness uses SCRIPTED scenarios (pre-written event logs), which we
proved is a regime where memory architecture cannot be decisively ranked. This module
adds the missing piece: a small, controllable society where agents actually interact,
generate their own history, and update memory — the regime where social memory matters.

Design goals: minimal (no spatial map / Phaser), controllable (set #agents, horizon,
the seeded dynamic), cheap (pluggable model + mockable), and instrumented (per-round
logs in a simple JSON form our extraction/judge tools can parse).

The memory mechanism is PLUGGABLE via the `Memory` protocol so we can compare
SMGA v2 vs a GA-reflection baseline in the same loop. This file is the engine +
skeleton; concrete memory impls and the LLM-backed conversation live alongside it.
"""

from __future__ import annotations

import json
import random
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Protocol


# --------------------------------------------------------------------------- #
# Memory interface (pluggable: GA-reflection baseline vs SMGA v2)
# --------------------------------------------------------------------------- #
class Memory(Protocol):
    """Per-agent memory. Implementations differ in how they store/surface social state."""

    def observe(self, event: dict[str, Any]) -> None:
        """Record a perceived event (an utterance heard, an action seen)."""

    def retrieve(self, query: str) -> str:
        """Return a natural-language context block relevant to `query`, for conditioning."""

    def consolidate(self) -> None:
        """End-of-round consolidation (reflection / currency resolution). May be a no-op."""

    def snapshot(self) -> dict[str, Any]:
        """Serializable view of what the agent currently holds (for logging/diagnostics)."""


@dataclass
class RawStreamMemory:
    """A trivial baseline: append-only event list, retrieval = keyword recency.

    Stands in until the GA-reflection and SMGA v2 memories are wired. Good enough to
    validate the simulation loop end to end offline.
    """

    events: list[dict[str, Any]] = field(default_factory=list)

    def observe(self, event: dict[str, Any]) -> None:
        self.events.append(event)

    def retrieve(self, query: str) -> str:
        terms = {t.lower() for t in query.split()}
        scored = [e for e in self.events if terms & {t.lower() for t in str(e.get("text", "")).split()}]
        recent = (scored or self.events)[-6:]
        return "\n".join(f"- {e.get('text','')}" for e in recent)

    def consolidate(self) -> None:
        return None

    def snapshot(self) -> dict[str, Any]:
        return {"kind": "raw_stream", "n_events": len(self.events), "events": self.events}


# --------------------------------------------------------------------------- #
# Agents and world
# --------------------------------------------------------------------------- #
@dataclass
class Agent:
    agent_id: str
    name: str
    persona: str
    memory: Memory
    # seeded private intents/commitments the agent starts with (drives social dynamics)
    seeds: list[str] = field(default_factory=list)

    def context_for(self, partner_name: str, topic: str) -> str:
        return self.memory.retrieve(f"{partner_name} {topic}")


# A converse function: (speaker, listener, topic, history) -> list of utterance dicts.
# Pluggable so we can run mock (offline) or LLM-backed.
ConverseFn = Callable[["Agent", "Agent", str, list[dict[str, Any]]], list[dict[str, Any]]]


def mock_converse(a: Agent, b: Agent, topic: str, history: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Offline stand-in: deterministic 2-turn exchange that passes seeds along.

    Lets us validate the loop (scheduling, observation, logging, diffusion) with no API.
    """
    utts = []
    seed_line = a.seeds[0] if a.seeds else f"how the {topic} is going"
    utts.append({"speaker": a.name, "listener": b.name, "text": f"{a.name}: I wanted to mention {seed_line}."})
    utts.append({"speaker": b.name, "listener": a.name, "text": f"{b.name}: Thanks {a.name}, noted about {seed_line}."})
    return utts


CONVERSE_SYSTEM = (
    "You are role-playing a person in a small neighborhood. Stay in character and stay "
    "consistent with your memory notes — only act on what is currently true and honor any "
    "commitments you have made. Reply with ONE short, natural utterance (1-2 sentences). "
    'Return ONLY JSON: {"utterance": "..."}'
)


def make_llm_converse(llm: "Any", turns: int = 4) -> ConverseFn:
    """LLM-backed conversation; the system prompt is identical across memory conditions."""

    def converse(a: Agent, b: Agent, topic: str, history: list[dict[str, Any]]) -> list[dict[str, Any]]:
        utts: list[dict[str, Any]] = []
        order = [(a, b), (b, a)]
        for t in range(turns):
            speaker, listener = order[t % 2]
            context = speaker.context_for(listener.name, topic)
            convo = "\n".join(u["text"] for u in utts) or "(start of conversation)"
            user = (
                f"You are {speaker.name}: {speaker.persona}.\n"
                f"You are talking with {listener.name} about {topic}.\n\n"
                f"Your memory notes:\n{context or '(nothing relevant yet)'}\n\n"
                f"Conversation so far:\n{convo}\n\n"
                f"What does {speaker.name} say next?"
            )
            out = llm.complete_json(CONVERSE_SYSTEM, user)
            text = str(out.get("utterance", "")).strip()
            if not text:
                continue
            utts.append({"speaker": speaker.name, "listener": listener.name, "text": f"{speaker.name}: {text}"})
        return utts

    return converse


@dataclass
class World:
    agents: list[Agent]
    topic: str = "the neighborhood plan"
    rng: random.Random = field(default_factory=lambda: random.Random(7))
    # exogenous updates injected into specific agents at a round: {round: [(agent_id, text)]}
    injections: dict[int, list[tuple[str, str]]] = field(default_factory=dict)
    # encounters per agent per round (connectivity). 1 = single chain (slow diffusion);
    # 2-3 = a realistically connected neighborhood where an update can actually spread.
    meetings_per_round: int = 1

    def schedule(self, round_idx: int) -> list[tuple[Agent, Agent]]:
        """Who meets whom this round: `meetings_per_round` independent random matchings.

        Higher connectivity lets a single-source update diffuse through the society
        instead of crawling one hop per round. Duplicate pairs within a round are
        de-duplicated so the same two agents don't hold the same conversation twice."""
        seen: set[frozenset[str]] = set()
        pairs: list[tuple[Agent, Agent]] = []
        for _ in range(max(1, self.meetings_per_round)):
            pool = list(self.agents)
            self.rng.shuffle(pool)
            for i in range(0, len(pool) - 1, 2):
                key = frozenset((pool[i].agent_id, pool[i + 1].agent_id))
                if key in seen:
                    continue
                seen.add(key)
                pairs.append((pool[i], pool[i + 1]))
        return pairs

    def agent_by_id(self, agent_id: str) -> Agent | None:
        return next((a for a in self.agents if a.agent_id == agent_id), None)


# --------------------------------------------------------------------------- #
# Simulation loop
# --------------------------------------------------------------------------- #
def _run_encounter(
    *,
    round_idx: int,
    topic: str,
    a: Agent,
    b: Agent,
    converse: ConverseFn,
) -> tuple[dict[str, Any], list[tuple[Agent, Agent, dict[str, Any]]]]:
    history: list[dict[str, Any]] = []
    utts = converse(a, b, topic, history)
    observations = []
    for u in utts:
        event = {"round": round_idx, "text": u["text"], "speaker": u["speaker"], "listener": u["listener"]}
        observations.append((a, b, event))
    return {"a": a.name, "b": b.name, "utterances": utts}, observations


def run_round(world: World, round_idx: int, converse: ConverseFn, *, workers: int = 1) -> dict[str, Any]:
    encounters = []
    observations: list[tuple[Agent, Agent, dict[str, Any]]] = []
    pairs = world.schedule(round_idx)
    if workers > 1 and len(pairs) > 1:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [
                executor.submit(
                    _run_encounter,
                    round_idx=round_idx,
                    topic=world.topic,
                    a=a,
                    b=b,
                    converse=converse,
                )
                for a, b in pairs
            ]
            for future in futures:
                encounter, obs = future.result()
                encounters.append(encounter)
                observations.extend(obs)
    else:
        for a, b in pairs:
            encounter, obs = _run_encounter(
                round_idx=round_idx,
                topic=world.topic,
                a=a,
                b=b,
                converse=converse,
            )
            encounters.append(encounter)
            observations.extend(obs)

    for a, b, event in observations:
        # both participants perceive every utterance in the encounter
        a.memory.observe(event)
        b.memory.observe(event)
    # apply exogenous updates this round (a fact changes -> currency stress)
    injected = []
    for agent_id, text in world.injections.get(round_idx, []):
        agent = world.agent_by_id(agent_id)
        if agent is None:
            continue
        event = {"round": round_idx, "text": text, "speaker": "world", "listener": agent.name, "injected": True}
        agent.memory.observe(event)
        injected.append({"agent": agent.name, "text": text})
    if workers > 1 and len(world.agents) > 1:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            list(executor.map(lambda agent: agent.memory.consolidate(), world.agents))
    else:
        for agent in world.agents:
            agent.memory.consolidate()
    return {"round": round_idx, "encounters": encounters, "injected": injected}


def run_sim(world: World, rounds: int, converse: ConverseFn, out_dir: Path, *, workers: int = 1) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    round_logs = []
    for r in range(rounds):
        log = run_round(world, r, converse, workers=workers)
        round_logs.append(log)
        (out_dir / f"round_{r:03d}.json").write_text(
            json.dumps(log, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    # final per-agent memory snapshots (the "what each agent believes" ground truth)
    snapshots = {a.agent_id: a.memory.snapshot() for a in world.agents}
    (out_dir / "memory_snapshots.json").write_text(
        json.dumps(snapshots, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    summary = {
        "agents": [{"id": a.agent_id, "name": a.name} for a in world.agents],
        "rounds": rounds,
        "topic": world.topic,
        "encounters_total": sum(len(rl["encounters"]) for rl in round_logs),
    }
    (out_dir / "sim_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return summary


def demo_world(memory_factory: Callable[[], Memory], *, rng_seed: int = 7, agent_count: int = 4,
               meetings_per_round: int = 1) -> World:
    """A configurable society with one seeded social dynamic (an event to organize)."""
    roster = [
        Agent("a01", "Rosa", "the block coordinator, organized and warm", memory_factory(),
               seeds=["I am organizing a repair drive this Saturday at the front porch and need helpers"]),
        Agent("a02", "Sam", "a reliable neighbor who likes to help", memory_factory()),
        Agent("a03", "Tess", "a chatty neighbor who passes news along", memory_factory()),
        Agent("a04", "Uli", "a quiet neighbor dealing with a private hardship", memory_factory()),
        Agent("a05", "Mina", "a practical neighbor who asks direct questions", memory_factory()),
        Agent("a06", "Oren", "a forgetful but well-meaning neighbor", memory_factory()),
        Agent("a07", "Pia", "a cautious neighbor who worries about logistics", memory_factory()),
        Agent("a08", "Vik", "a social neighbor who repeats plans to others", memory_factory()),
        Agent("a09", "Nell", "a newer neighbor who relies on second-hand updates", memory_factory()),
        Agent("a10", "Bo", "a busy neighbor who skims details", memory_factory()),
        Agent("a11", "Cleo", "a neighbor who keeps track of supplies", memory_factory()),
        Agent("a12", "Dane", "a neighbor who often joins late", memory_factory()),
        Agent("a13", "Eli", "a retired neighbor who likes routine and clear plans", memory_factory()),
        Agent("a14", "Faye", "a parent who coordinates around school schedules", memory_factory()),
        Agent("a15", "Gus", "a handy neighbor who often volunteers tools", memory_factory()),
        Agent("a16", "Hana", "a careful listener who checks details before acting", memory_factory()),
        Agent("a17", "Ira", "a neighbor who hears updates while running errands", memory_factory()),
        Agent("a18", "Jules", "a friendly neighbor who connects separate friend groups", memory_factory()),
        Agent("a19", "Kira", "a skeptical neighbor who asks for confirmation", memory_factory()),
        Agent("a20", "Leo", "a neighbor who prefers short practical messages", memory_factory()),
        Agent("a21", "Mara", "a community-minded neighbor who remembers commitments", memory_factory()),
        Agent("a22", "Noah", "a distracted neighbor who sometimes misses changes", memory_factory()),
        Agent("a23", "Opal", "a detail-oriented neighbor who tracks locations", memory_factory()),
        Agent("a24", "Quinn", "a sociable neighbor who spreads invitations quickly", memory_factory()),
        Agent("a25", "Rey", "a quiet neighbor who mostly learns through one-on-one chats", memory_factory()),
    ]
    if agent_count < 2 or agent_count > len(roster):
        raise ValueError(f"agent_count must be between 2 and {len(roster)}")
    agents = roster[:agent_count]
    # currency stress: at round 1 the drive's time+place are CHANGED (Rosa hears it).
    # The current truth becomes Sunday / community center; Saturday / front porch is stale.
    injections = {1: [("a01",
        "Update: the repair drive has been moved from Saturday at the front porch to "
        "Sunday at the community center.")]}
    return World(
        agents=agents,
        topic="the repair drive",
        rng=random.Random(rng_seed),
        injections=injections,
        meetings_per_round=meetings_per_round,
    )


INTERVIEW_SYSTEM = (
    "Answer the question using ONLY the memory notes, reflecting the CURRENT state. "
    'Reply with one short sentence. Return ONLY JSON: {"answer": "..."}'
)


def interview(world: World, question: str, llm: "Any") -> dict[str, Any]:
    """Ask every agent a probe and score current-vs-stale (a live currency / C4 check)."""
    current_markers = ("sunday", "community center")
    stale_markers = ("saturday", "front porch", "porch")
    results = {}
    for a in world.agents:
        ctx = a.memory.retrieve(question)
        out = llm.complete_json(INTERVIEW_SYSTEM, f"Memory notes:\n{ctx or '(none)'}\n\nQuestion: {question}")
        ans = str(out.get("answer", "")).lower()
        has_current = any(m in ans for m in current_markers)
        has_stale = any(m in ans for m in stale_markers)
        verdict = "current" if (has_current and not has_stale) else ("stale" if has_stale else "unknown")
        results[a.agent_id] = {"name": a.name, "answer": out.get("answer", ""), "verdict": verdict}
    return results


def build_memory_factory(kind: str, llm: "Any") -> Callable[[], Memory]:
    if kind == "raw":
        return lambda: RawStreamMemory()
    if kind == "ga":
        from memories import GAReflectionMemory
        return lambda: GAReflectionMemory(llm=llm)
    if kind == "smga":
        from memories import SMGAv2Memory
        return lambda: SMGAv2Memory(llm=llm)
    raise ValueError(f"unknown memory kind: {kind}")


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Run the minimal SMGA society simulation.")
    parser.add_argument("--memory", choices=["raw", "ga", "smga"], default="raw")
    parser.add_argument("--rounds", type=int, default=4)
    parser.add_argument("--turns", type=int, default=4, help="utterances per encounter")
    parser.add_argument("--agent-count", type=int, default=4, help="number of agents from the demo roster")
    parser.add_argument("--meetings", type=int, default=1, help="encounters per agent per round (connectivity)")
    parser.add_argument("--seed", type=int, default=7, help="random seed for encounter scheduling")
    parser.add_argument("--workers", type=int, default=1, help="concurrent encounters/consolidations per round")
    parser.add_argument("--mock", action="store_true", help="offline; no LLM calls")
    parser.add_argument("--config", type=Path, default=None)
    parser.add_argument("--model", default=None)
    parser.add_argument("--out-dir", type=Path, default=None)
    args = parser.parse_args()

    if args.mock:
        llm = None
        converse: ConverseFn = mock_converse
    else:
        from llm import LLM, DEFAULT_CONFIG
        llm = LLM(config=args.config or DEFAULT_CONFIG, model=args.model)
        converse = make_llm_converse(llm, turns=args.turns)

    world = demo_world(build_memory_factory(args.memory, llm), rng_seed=args.seed,
                       agent_count=args.agent_count, meetings_per_round=args.meetings)
    out_dir = args.out_dir or Path(f"sim/runs/{args.memory}_demo")
    summary = run_sim(world, args.rounds, converse, out_dir, workers=max(1, args.workers))
    summary["rng_seed"] = args.seed
    summary["agent_count"] = args.agent_count

    # Live currency check (C4): after the mid-sim update, which agents report the CURRENT
    # time/place of the drive vs the stale one?
    if not args.mock:
        question = "When and where is the repair drive being held now?"
        interview_res = interview(world, question, llm)
        (out_dir / "interview_currency.json").write_text(json.dumps(
            {"question": question, "results": interview_res}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        tally = {"current": 0, "stale": 0, "unknown": 0}
        for r in interview_res.values():
            tally[r["verdict"]] += 1
        summary["currency_interview"] = tally
    (out_dir / "sim_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"\nmemory={args.memory}  logs -> {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
