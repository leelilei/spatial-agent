"""空间拓扑图构建模块。"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import networkx as nx
import yaml


def load_layout(path: str | Path) -> dict[str, Any]:
    """从 YAML 文件中加载 layout 定义。"""
    with Path(path).open("r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle) or {}
    layout = payload.get("layout", payload)
    if not layout:
        raise ValueError(f"Layout file is empty: {path}")
    if "nodes" not in layout or "edges" not in layout:
        raise ValueError(f"Layout file must define nodes and edges: {path}")
    return layout


def build_graph(layout: dict[str, Any]) -> nx.Graph:
    """将 layout 字典转换为带属性的无向图。"""
    graph = nx.Graph(name=layout.get("name", "layout"))

    for node in layout.get("nodes", []):
        node_id = node["id"]
        attrs = {key: value for key, value in node.items() if key != "id"}
        graph.add_node(node_id, **attrs)

    for edge in layout.get("edges", []):
        if isinstance(edge, dict):
            source = edge["source"]
            target = edge["target"]
            attrs = {key: value for key, value in edge.items() if key not in {"source", "target"}}
        else:
            source, target = edge
            attrs = {}
        graph.add_edge(source, target, **attrs)

    if not nx.is_connected(graph):
        raise ValueError("Layout graph must be connected for space syntax metrics.")
    return graph


def load_layout_graph(path: str | Path) -> nx.Graph:
    """快捷加载 layout 文件并构图。"""
    return build_graph(load_layout(path))
