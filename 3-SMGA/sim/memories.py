#!/usr/bin/env python3
"""Pluggable memory implementations for the society simulation.

Fair ablation: the conversation prompt is identical across conditions; the ONLY
difference is what `retrieve()` surfaces.

- GAReflectionMemory : append-only event stream + periodic free-text reflections;
  retrieval = keyword/recency over events+reflections (the GA baseline). May surface
  stale or conflicting information.
- SMGAv2Memory       : maintains a set of CURRENT, currency-resolved social facts
  (superseded facts dropped from retrieval); retrieval = current facts relevant to
  the query. The improvement we are testing — currency resolution in a live society.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

from llm import LLM


def _recent(events: list[dict[str, Any]], k: int) -> list[dict[str, Any]]:
    return events[-k:]


# Shared relevance retrieval (fair across memory conditions): rank by content-word
# overlap with the query, NOT by recency — so a held but older fact is still surfaced
# instead of being dropped by a recency cutoff. Both GA and SMGA use this; only the
# underlying representation (events+reflections vs current facts) differs.
_STOP = {
    "the", "a", "an", "of", "to", "and", "or", "in", "on", "at", "is", "are", "was",
    "were", "be", "being", "been", "for", "with", "about", "when", "where", "what",
    "who", "how", "why", "now", "you", "your", "i", "my", "me", "it", "its", "this",
    "that", "they", "them", "their", "we", "us", "he", "she", "his", "her", "do",
    "does", "did", "will", "would", "can", "could", "should", "as", "by", "from",
}


def _content_terms(text: str) -> set[str]:
    out = set()
    for raw in str(text).lower().split():
        tok = raw.strip(".,!?;:'\"()[]")
        if tok and tok not in _STOP and len(tok) > 1:
            out.add(tok)
    return out


def _lexical_rank(query: str, items: list[tuple[str, Any]], k: int) -> list[Any]:
    """Fallback retriever: rank by content-word overlap; recency when nothing overlaps."""
    q = _content_terms(query)
    scored = [(len(q & _content_terms(text)), idx, payload) for idx, (text, payload) in enumerate(items)]
    relevant = [s for s in scored if s[0] > 0]
    if relevant:
        relevant.sort(key=lambda s: (s[0], s[1]), reverse=True)  # score, then recency
        return [s[2] for s in relevant[:k]]
    return [payload for _, payload in items[-k:]]


# Embedding retriever (GA-faithful: Park 2023 retrieval is embedding cosine, not keyword).
# Static distilled embeddings (model2vec) — fast, CPU-only, no torch, zero per-call API.
# Lazily loaded once; if unavailable we degrade to the lexical retriever so --mock and
# dependency-free environments still run. Override the model via SMGA_EMBED_MODEL.
_EMBED_MODEL_NAME = __import__("os").environ.get("SMGA_EMBED_MODEL", "minishlab/potion-retrieval-32M")
_EMBEDDER: Any = None  # None = not yet tried; False = unavailable; else a loaded model


def _get_embedder() -> Any:
    global _EMBEDDER
    if _EMBEDDER is None:
        try:
            from model2vec import StaticModel  # type: ignore
            _EMBEDDER = StaticModel.from_pretrained(_EMBED_MODEL_NAME)
        except Exception:
            _EMBEDDER = False
    return _EMBEDDER


def _embed_rank(query: str, items: list[tuple[str, Any]], k: int, model: Any) -> list[Any]:
    import numpy as np
    texts = [t for t, _ in items]
    vecs = np.asarray(model.encode([query] + texts), dtype="float32")
    qv, mv = vecs[0], vecs[1:]
    sims = mv @ qv / (np.linalg.norm(mv, axis=1) * (np.linalg.norm(qv) + 1e-9) + 1e-9)
    order = np.argsort(-sims)[:k]
    return [items[i][1] for i in order]


def _rank_by_relevance(query: str, items: list[tuple[str, Any]], k: int) -> list[Any]:
    """items = [(text_to_match, payload)]; return top-k payloads most relevant to query.

    Embedding cosine when available (robust to paraphrase, GA-faithful), else lexical."""
    if not items:
        return []
    model = _get_embedder()
    if model:
        try:
            return _embed_rank(query, items, k, model)
        except Exception:
            pass
    return _lexical_rank(query, items, k)


@dataclass
class GAReflectionMemory:
    llm: LLM
    reflect_every: int = 1
    events: list[dict[str, Any]] = field(default_factory=list)
    reflections: list[str] = field(default_factory=list)
    _round: int = 0

    def observe(self, event: dict[str, Any]) -> None:
        self.events.append(event)

    def retrieve(self, query: str) -> str:
        # Same relevance-ranked retrieval as SMGA (fair): only the representation differs
        # (raw events + free-text reflections, which may surface stale/conflicting items).
        ev = _rank_by_relevance(query, [(str(e.get("text", "")), e) for e in self.events], 6)
        rf = _rank_by_relevance(query, [(r, r) for r in self.reflections], 3)
        lines = [f"- {e.get('text','')}" for e in ev]
        lines += [f"- (reflection) {r}" for r in rf]
        return "\n".join(lines)

    def consolidate(self) -> None:
        self._round += 1
        if self._round % self.reflect_every != 0:
            return
        recent = _recent(self.events, 10)
        if not recent:
            return
        statements = "\n".join(f"{i+1}. {e.get('text','')}" for i, e in enumerate(recent))
        out = self.llm.complete_json(
            "You are a generative agent reflecting on your recent interactions, GA-style. "
            "Infer up to 3 short high-level insights about the people and relationships. "
            'Return ONLY JSON: {"insights": ["...", ...]}',
            f"Recent events:\n{statements}",
        )
        for ins in (out.get("insights") or [])[:3]:
            if str(ins).strip():
                self.reflections.append(str(ins).strip())

    def snapshot(self) -> dict[str, Any]:
        return {"kind": "ga_reflection", "n_events": len(self.events),
                "reflections": self.reflections, "events": self.events}


@dataclass
class SMGAv2Memory:
    llm: LLM
    events: list[dict[str, Any]] = field(default_factory=list)
    facts: list[dict[str, Any]] = field(default_factory=list)        # current, currency-resolved
    superseded: list[dict[str, Any]] = field(default_factory=list)   # kept for audit only

    def observe(self, event: dict[str, Any]) -> None:
        self.events.append(event)

    def retrieve(self, query: str) -> str:
        # Relevance-ranked (not recency-capped): a held but older current fact is still
        # surfaced instead of being dropped by a `[-6:]` recency cutoff. This replaces the
        # brittle keyword set-intersection that mis-blocked held facts in the gate
        # experiment (see sim/RESULTS.md, 2026-06-17). Shared scorer with GA for fairness.
        items = [(str(f.get("claim", "")) + " " + " ".join(f.get("subject", []) or []), f)
                 for f in self.facts]
        use = _rank_by_relevance(query, items, 6)
        return "\n".join(f"- {f.get('claim','')} (current)" for f in use)

    def consolidate(self) -> None:
        recent = _recent(self.events, 10)
        if not recent:
            return
        existing = json.dumps([{"claim": f.get("claim"), "subject": f.get("subject", [])} for f in self.facts], ensure_ascii=False)
        statements = "\n".join(f"{i+1}. {e.get('text','')}" for i, e in enumerate(recent))
        out = self.llm.complete_json(
            "You maintain a small set of CURRENT social facts (relationships, commitments, "
            "who-knows-what, plans). Given the existing current facts and recent events, return "
            "the UPDATED set of facts that are currently true. If a recent event updates or "
            "contradicts an earlier fact, the new value is current and the old is dropped. "
            "Each claim MUST be SELF-CONTAINED and unambiguous on its own: name the specific "
            "event/topic/people it refers to (e.g. 'The repair drive is on Sunday at the "
            "community center'), never a bare pronoun like 'It is Sunday...' or a dangling "
            "reference. A reader seeing only that one claim must know what/who it is about. "
            'Each fact: {"claim": str, "subject": [names]}. Return ONLY JSON: {"facts": [...]}',
            f"Existing current facts:\n{existing}\n\nRecent events:\n{statements}",
        )
        new_facts = out.get("facts")
        if isinstance(new_facts, list) and new_facts:
            # anything previously current but not in the new set is treated as superseded
            new_claims = {str(f.get("claim", "")).strip().lower() for f in new_facts}
            for f in self.facts:
                if str(f.get("claim", "")).strip().lower() not in new_claims:
                    self.superseded.append(f)
            self.facts = [{"claim": str(f.get("claim", "")), "subject": list(f.get("subject", []) or []),
                           "currency_status": "current"} for f in new_facts if str(f.get("claim", "")).strip()]

    def snapshot(self) -> dict[str, Any]:
        return {"kind": "smga_v2", "n_events": len(self.events),
                "current_facts": self.facts, "superseded_facts": self.superseded, "events": self.events}


_WEEKDAYS = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")


def _sub_weekday(text: str, day: str) -> str:
    """Re-point any weekday mention in a dependent fact to the event's current day."""
    if not day:
        return text
    out = text
    for wd in _WEEKDAYS:
        if wd in out.lower() and wd != day.lower():
            # case-insensitive replace, keep it simple
            import re as _re
            out = _re.sub(wd, day, out, flags=_re.IGNORECASE)
    return out


@dataclass
class SMGAv3Memory:
    """Entity-centric currency memory (the B in the B+C plan).

    The v2 failure: a changed central fact (drive moves Saturday->Sunday) leaves a web
    of DEPENDENT facts ('Sam brings tools Saturday') stranded on the old value, so agents
    answer stale. v3 keeps a single source of truth — an EVENT REGISTRY of canonical
    current attributes (day/place/time) — and stores dependent facts WITHOUT baking the
    volatile attribute in (they carry depends_on instead). Retrieval LATE-BINDS the
    volatile attribute from the registry, so dependents structurally cannot go stale.
    """

    llm: LLM
    events: list[dict[str, Any]] = field(default_factory=list)
    facts: list[dict[str, Any]] = field(default_factory=list)          # {claim, subject, depends_on}
    registry: dict[str, dict[str, str]] = field(default_factory=dict)  # event -> {day, place, time}

    def observe(self, event: dict[str, Any]) -> None:
        self.events.append(event)

    def retrieve(self, query: str) -> str:
        q = _content_terms(query)
        lines: list[str] = []
        # 1) canonical event state (authoritative, single source of truth) for relevant events
        relevant_events = set()
        for name, attrs in self.registry.items():
            if _content_terms(name) & q:
                relevant_events.add(name)
                parts = []
                if attrs.get("day"):
                    parts.append(f"on {attrs['day']}")
                if attrs.get("time"):
                    parts.append(f"at {attrs['time']}")
                if attrs.get("place"):
                    parts.append(f"at the {attrs['place']}")
                lines.append(f"- The {name} is currently {' '.join(parts)}. (current, authoritative)")
        # 2) dependent facts: late-bind the volatile day from the registry
        deps = [f for f in self.facts if f.get("depends_on") in self.registry]
        for f in deps[:4]:
            day = self.registry.get(f.get("depends_on", ""), {}).get("day", "")
            lines.append(f"- {_sub_weekday(str(f.get('claim', '')), day)}")
        # 3) other independent facts, embedding-ranked
        others = [f for f in self.facts if f.get("depends_on") not in self.registry]
        items = [(str(f.get("claim", "")) + " " + " ".join(f.get("subject", []) or []), f) for f in others]
        for f in _rank_by_relevance(query, items, 4):
            lines.append(f"- {f.get('claim', '')}")
        return "\n".join(lines)

    def consolidate(self) -> None:
        recent = _recent(self.events, 10)
        if not recent:
            return
        reg = json.dumps(self.registry, ensure_ascii=False)
        existing = json.dumps([{"claim": f.get("claim"), "subject": f.get("subject", []),
                                "depends_on": f.get("depends_on")} for f in self.facts], ensure_ascii=False)
        statements = "\n".join(f"{i+1}. {e.get('text','')}" for i, e in enumerate(recent))
        out = self.llm.complete_json(
            "You maintain TWO structures and return their updated state. "
            "(1) An EVENT REGISTRY: the single source of truth for each scheduled event's CURRENT "
            "volatile attributes (day, place, time). If a recent event changes a value (e.g. the "
            "repair drive moved from Saturday to Sunday, or front porch to community center), the "
            "NEW value REPLACES the old; the registry holds only what is current. "
            "(2) FACTS: current social facts. CRUCIAL: do NOT bake an event's volatile day/place into "
            "a dependent fact. A commitment that depends on an event (e.g. 'Sam brings tools for the "
            "repair drive') must set depends_on to that event's exact name and state only the durable "
            "part ('Sam brings tools'), NOT the day/place. Independent facts set depends_on to null and "
            "stay self-contained (name who/what they are about, no bare pronouns). "
            'Return ONLY JSON: {"events":[{"name":str,"day":str,"place":str,"time":str}],'
            '"facts":[{"claim":str,"subject":[names],"depends_on":str_or_null}]}',
            f"Existing registry:\n{reg}\n\nExisting facts:\n{existing}\n\nRecent events:\n{statements}",
        )
        for ev in (out.get("events") or []):
            name = str(ev.get("name", "")).strip()
            if not name:
                continue
            slot = self.registry.setdefault(name, {})
            for k in ("day", "place", "time"):
                v = str(ev.get(k, "") or "").strip()
                if v:
                    slot[k] = v  # new value supersedes (currency resolution in ONE place)
        new_facts = out.get("facts")
        if isinstance(new_facts, list) and new_facts:
            self.facts = [{"claim": str(f.get("claim", "")), "subject": list(f.get("subject", []) or []),
                           "depends_on": (str(f.get("depends_on")).strip() if f.get("depends_on") else None)}
                          for f in new_facts if str(f.get("claim", "")).strip()]

    def snapshot(self) -> dict[str, Any]:
        return {"kind": "smga_v3", "n_events": len(self.events),
                "registry": self.registry, "current_facts": self.facts, "events": self.events}
