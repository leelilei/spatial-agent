import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "v1_1" / "generate_worlds.py"
SPEC = importlib.util.spec_from_file_location("cityintent_v1_1_generate_worlds", MODULE_PATH)
assert SPEC and SPEC.loader
worldgen = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = worldgen
SPEC.loader.exec_module(worldgen)


def _reachable(world):
    graph = {location["id"]: set() for location in world["locations"]}
    for edge in world["edges"]:
        graph[edge["from"]].add(edge["to"])
        graph[edge["to"]].add(edge["from"])
    start = next(iter(graph))
    seen = {start}
    frontier = [start]
    while frontier:
        node = frontier.pop()
        for neighbor in graph[node] - seen:
            seen.add(neighbor)
            frontier.append(neighbor)
    return seen


def test_world_pack_has_required_distinct_connected_topologies():
    worlds = [worldgen.build_world(spec) for spec in worldgen.world_specs()]
    assert len(worlds) == 5
    assert len({world["world_id"] for world in worlds}) == 5
    assert len({world["topology_archetype"] for world in worlds}) == 5
    assert [world["release_visibility"] for world in worlds].count("public") == 3
    assert [world["release_visibility"] for world in worlds].count("private") == 2

    required_roles = {row[0] for row in worldgen.ROLE_SPECS}
    all_location_ids = set()
    edge_fingerprints = set()
    for world in worlds:
        location_ids = {location["id"] for location in world["locations"]}
        assert len(location_ids) == len(required_roles)
        assert not all_location_ids.intersection(location_ids)
        all_location_ids.update(location_ids)
        assert {location["semantic_role"] for location in world["locations"]} == required_roles
        assert _reachable(world) == location_ids
        edge_fingerprints.add(tuple(sorted((edge["from"].split("_", 1)[1], edge["to"].split("_", 1)[1]) for edge in world["edges"])))
    assert len(edge_fingerprints) == 5


def test_world_generation_is_deterministic_and_manifest_hashes_content(tmp_path):
    first = worldgen.generate_pack(tmp_path / "first")
    second = worldgen.generate_pack(tmp_path / "second")
    assert first == second
    for entry in first["worlds"]:
        world = json.loads((tmp_path / "first" / entry["path"]).read_text(encoding="utf-8"))
        assert entry["sha256"] == worldgen.canonical_sha256(world)
