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
        terms = {t.lower().strip(".,") for t in query.split()}
        ev = [e for e in self.events if terms & {t.lower().strip(".,") for t in str(e.get("text", "")).split()}]
        rf = [r for r in self.reflections if terms & {t.lower().strip(".,") for t in r.split()}]
        lines = [f"- {e.get('text','')}" for e in (ev or self.events)[-6:]]
        lines += [f"- (reflection) {r}" for r in (rf or self.reflections)[-3:]]
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
        terms = {t.lower().strip(".,") for t in query.split()}
        rel = [f for f in self.facts
               if terms & {t.lower().strip(".,") for t in (str(f.get("claim", "")) + " " + " ".join(f.get("subject", []))).split()}]
        # NOTE (2026-06-17): a naive "evidence gate" (return an explicit no-fact marker
        # when `rel` is empty, no fallback) was tried and REVERTED. The keyword match is
        # too brittle: it mis-blocked agents that DID hold the current fact (3/8 unknown
        # answerers in the 25-agent r9 pilot held "Sunday/community center"), crashing
        # current-recall (r9 13->8) without reducing unsupported. A proper gate needs
        # SEMANTIC retrieval so it surfaces held facts reliably first. Until then, the
        # fallback (surface current facts) is the stronger version. See sim/RESULTS.md.
        use = rel or self.facts
        return "\n".join(f"- {f.get('claim','')} (current)" for f in use[-6:])

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
            "contradicts an earlier fact, the new value is current and the old is dropped. Each "
            'fact: {"claim": str, "subject": [names]}. Return ONLY JSON: {"facts": [...]}',
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
