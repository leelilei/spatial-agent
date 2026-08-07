#!/usr/bin/env python3
"""Deterministically generate the CityIntent v1.1 multi-world pack."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
GENERATOR_VERSION = "cityintent-worldgen-1.0.0"


@dataclass(frozen=True)
class WorldSpec:
    world_id: str
    name: str
    prefix: str
    topology: str
    visibility: str
    seed: int
    time_shift: int
    cost_scale: float


PUBLIC_WORLD_SPECS = (
    WorldSpec("harbor_grid_v1", "Harbor Grid", "hgd", "dense_grid", "public", 1103, -15, 1.10),
    WorldSpec("metro_radial_v1", "Metro Radial", "mtr", "radial_transit", "public", 2207, 10, 1.35),
    WorldSpec("suburb_polycentric_v1", "Suburb Polycentric", "spc", "sparse_polycentric", "public", 3301, 25, 0.85),
)


# role, type, tags, opening, capacity, typical cost
ROLE_SPECS = (
    ("home_primary", "home", ("home", "quiet"), ("00:00", "23:59"), 2, None),
    ("home_friend", "home", ("home",), ("00:00", "23:59"), 2, None),
    ("office", "work", ("work", "wifi"), ("07:00", "21:00"), 20, None),
    ("transit_hub", "transit", ("transit", "crowded"), ("05:00", "23:30"), 80, None),
    ("plaza", "public_space", ("outdoor", "event_space", "crowded"), ("00:00", "23:59"), 120, None),
    ("meeting_cafe", "food", ("coffee", "meeting", "moderate_noise"), ("07:30", "20:00"), 24, 12),
    ("quiet_cafe", "food", ("coffee", "quiet", "wifi", "vegan"), ("08:00", "21:00"), 18, 10),
    ("library", "study", ("quiet", "free", "wifi"), ("09:00", "18:00"), 40, 0),
    ("coworking", "work", ("quiet", "wifi", "paid"), ("08:00", "22:00"), 30, 15),
    ("civic_service", "service", ("appointment", "public_service"), ("09:00", "17:00"), 50, None),
    ("park", "recreation", ("outdoor", "low_cost", "exercise"), ("06:00", "22:00"), 100, None),
    ("gym", "recreation", ("exercise", "paid"), ("06:00", "23:00"), 25, 8),
    ("market", "shopping", ("groceries", "busy"), ("08:00", "21:00"), 60, 14),
    ("pharmacy", "shopping", ("medicine", "errand"), ("08:00", "22:00"), 12, 9),
    ("clinic", "health", ("health", "appointment"), ("08:30", "19:00"), 20, 20),
    ("budget_food", "food", ("meal", "cheap"), ("07:00", "22:00"), 30, 6),
    ("school", "school", ("family", "pickup"), ("07:30", "18:30"), 80, None),
    ("culture", "culture", ("social", "ticketed"), ("17:00", "23:00"), 50, 18),
    ("bookstore", "shopping", ("quiet", "books", "wifi"), ("10:00", "20:00"), 20, 7),
)


def _shift_time(value: str, minutes: int) -> str:
    hour, minute = (int(part) for part in value.split(":"))
    total = max(0, min(23 * 60 + 59, hour * 60 + minute + minutes))
    return f"{total // 60:02d}:{total % 60:02d}"


def _location_id(spec: WorldSpec, role: str) -> str:
    return f"{spec.prefix}_{role}"


def _make_locations(spec: WorldSpec) -> list[dict[str, Any]]:
    rng = random.Random(spec.seed)
    locations: list[dict[str, Any]] = []
    for index, (role, kind, tags, hours, capacity, cost) in enumerate(ROLE_SPECS):
        opening_jitter = rng.choice((-10, 0, 10)) if role not in {"home_primary", "home_friend", "plaza"} else 0
        location: dict[str, Any] = {
            "id": _location_id(spec, role),
            "name": f"{spec.name} {role.replace('_', ' ').title()}",
            "semantic_role": role,
            "type": kind,
            "tags": list(tags),
            "open": [
                _shift_time(hours[0], spec.time_shift + opening_jitter),
                _shift_time(hours[1], spec.time_shift + opening_jitter),
            ],
            "capacity": max(2, round(capacity * rng.uniform(0.75, 1.25))),
            "map_index": index,
        }
        if cost is not None:
            location["typical_cost"] = round(cost * spec.cost_scale * rng.uniform(0.85, 1.15))
        locations.append(location)
    return locations


def _topology_pairs(topology: str) -> list[tuple[int, int]]:
    n = len(ROLE_SPECS)
    if topology == "dense_grid":
        pairs = []
        width = 5
        for i in range(n):
            if i % width < width - 1 and i + 1 < n:
                pairs.append((i, i + 1))
            if i + width < n:
                pairs.append((i, i + width))
        pairs.extend(((0, 6), (4, 8), (10, 16)))
        return pairs
    if topology == "radial_transit":
        hub = 3
        ring = [0, 2, 5, 4, 9, 14, 13, 12, 15, 16, 1, 10, 11, 6, 7, 18, 17, 8]
        pairs = [(hub, node) for node in ring]
        pairs.extend((ring[i], ring[(i + 1) % len(ring)]) for i in range(len(ring)))
        return pairs
    if topology == "sparse_polycentric":
        clusters = ((3, (0, 2, 5, 14, 9)), (4, (1, 12, 13, 15, 16, 17)), (7, (6, 8, 10, 11, 18)))
        pairs = [(center, node) for center, nodes in clusters for node in nodes]
        pairs.extend(((3, 4), (4, 7), (3, 7), (14, 13), (16, 10)))
        return pairs
    if topology == "bottleneck_crossing":
        west = list(range(0, 9))
        east = list(range(9, n))
        pairs = [(west[i], west[i + 1]) for i in range(len(west) - 1)]
        pairs += [(east[i], east[i + 1]) for i in range(len(east) - 1)]
        pairs += [(0, 4), (2, 6), (9, 14), (11, 17), (4, 9)]
        return pairs
    if topology == "mixed_irregular":
        return [
            (0, 3), (0, 11), (1, 16), (1, 3), (2, 3), (2, 5), (2, 8),
            (3, 4), (3, 14), (4, 5), (4, 9), (4, 12), (5, 17), (6, 7),
            (6, 10), (6, 17), (7, 8), (7, 18), (8, 18), (9, 13), (9, 14),
            (10, 11), (10, 12), (12, 13), (12, 15), (13, 14), (15, 16),
            (17, 18),
        ]
    raise ValueError(f"unknown topology: {topology}")


def build_world(spec: WorldSpec) -> dict[str, Any]:
    rng = random.Random(spec.seed + 97)
    locations = _make_locations(spec)
    ids = [location["id"] for location in locations]
    edges = [
        {
            "from": ids[a],
            "to": ids[b],
            "minutes": rng.randint(3, 13) + (4 if spec.topology in {"sparse_polycentric", "bottleneck_crossing"} and (a + b) % 4 == 0 else 0),
        }
        for a, b in _topology_pairs(spec.topology)
    ]
    return {
        "world_id": spec.world_id,
        "name": spec.name,
        "description": f"A {spec.topology.replace('_', ' ')} CityIntent evaluation world.",
        "time_unit": "minutes",
        "currency": "credits",
        "topology_archetype": spec.topology,
        "release_visibility": spec.visibility,
        "generator_provenance": {"generator_version": GENERATOR_VERSION, "seed": spec.seed},
        "locations": locations,
        "edges": edges,
    }


def canonical_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def world_specs(root: Path = ROOT, include_private: bool = True) -> tuple[WorldSpec, ...]:
    specs = list(PUBLIC_WORLD_SPECS)
    private_spec_path = root / "internal" / "private_world_specs.json"
    if include_private and private_spec_path.exists():
        for item in json.loads(private_spec_path.read_text(encoding="utf-8")):
            specs.append(WorldSpec(**item))
    return tuple(specs)


def generate_pack(output_root: Path = ROOT, include_private: bool = True) -> dict[str, Any]:
    entries = []
    for spec in world_specs(ROOT, include_private=include_private):
        world = build_world(spec)
        relative_path = Path("worlds") / spec.visibility / f"{spec.world_id}.json"
        output_path = output_root / relative_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(world, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        entries.append(
            {
                "world_id": spec.world_id,
                "visibility": spec.visibility,
                "topology_archetype": spec.topology,
                "path": relative_path.as_posix(),
                "sha256": canonical_sha256(world),
                "generator_version": GENERATOR_VERSION,
                "seed": spec.seed,
                "location_count": len(world["locations"]),
                "edge_count": len(world["edges"]),
            }
        )
    manifest = {
        "schema_version": "cityintent_world_manifest_v1",
        "benchmark_version": "1.1.0",
        "generator_version": GENERATOR_VERSION,
        "world_count": len(entries),
        "worlds": entries,
    }
    manifest_path = output_root / "manifests" / "worlds_manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=ROOT)
    parser.add_argument("--public-only", action="store_true")
    args = parser.parse_args()
    manifest = generate_pack(args.output_root.resolve(), include_private=not args.public_only)
    print(json.dumps({"world_count": manifest["world_count"], "output_root": str(args.output_root.resolve())}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
