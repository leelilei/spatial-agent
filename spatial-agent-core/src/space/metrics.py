"""Space Syntax 指标计算模块。"""

from __future__ import annotations

from typing import Iterable

import networkx as nx
import numpy as np
import pandas as pd


METRIC_COLUMNS = [
    "connectivity",
    "integration",
    "mean_depth",
    "control_value",
    "openness",
]


def _safe_series_normalize(series: pd.Series) -> pd.Series:
    minimum = float(series.min())
    maximum = float(series.max())
    if np.isclose(minimum, maximum):
        return pd.Series(np.zeros(len(series)), index=series.index)
    return (series - minimum) / (maximum - minimum)


def compute_space_metrics(graph: nx.Graph) -> pd.DataFrame:
    """计算实验需要的核心空间指标。"""
    nodes = list(graph.nodes())
    shortest_paths = dict(nx.all_pairs_shortest_path_length(graph))
    closeness = nx.closeness_centrality(graph)

    records: list[dict[str, float | str]] = []
    for node in nodes:
        distances = [distance for target, distance in shortest_paths[node].items() if target != node]
        mean_depth = float(np.mean(distances))
        degree = float(graph.degree(node))
        control_value = float(
            sum(1.0 / max(graph.degree(neighbor), 1) for neighbor in graph.neighbors(node))
        )
        openness = float(graph.nodes[node].get("visibility", 0.0))

        records.append(
            {
                "node_id": node,
                "connectivity": degree,
                "integration": float(closeness[node]),
                "mean_depth": mean_depth,
                "control_value": control_value,
                "openness": openness,
            }
        )

    frame = pd.DataFrame.from_records(records).sort_values("node_id").reset_index(drop=True)
    for column in METRIC_COLUMNS:
        frame[f"{column}_z"] = _zscore(frame[column])
        frame[f"{column}_norm"] = _safe_series_normalize(frame[column])
    return frame


def _zscore(series: pd.Series) -> pd.Series:
    std = float(series.std(ddof=0))
    if np.isclose(std, 0.0):
        return pd.Series(np.zeros(len(series)), index=series.index)
    return (series - series.mean()) / std


def summarize_metric_quality(
    metrics_frame: pd.DataFrame,
    *,
    high_control_quantile: float = 0.8,
) -> dict[str, object]:
    """生成指标质量预检摘要。"""
    numeric = metrics_frame[METRIC_COLUMNS]
    control_threshold = float(metrics_frame["control_value"].quantile(high_control_quantile))
    high_control_nodes = metrics_frame.loc[
        metrics_frame["control_value"] >= control_threshold, "node_id"
    ].tolist()
    distribution = {}
    for column in METRIC_COLUMNS:
        values = metrics_frame[column]
        mean_value = float(values.mean())
        distribution[column] = {
            "mean": mean_value,
            "std": float(values.std(ddof=0)),
            "min": float(values.min()),
            "max": float(values.max()),
            "cv": float(values.std(ddof=0) / mean_value) if not np.isclose(mean_value, 0.0) else 0.0,
        }

    return {
        "metric_correlation": numeric.corr(method="spearman").round(4).to_dict(),
        "distribution": distribution,
        "high_control_quantile": high_control_quantile,
        "high_control_threshold": control_threshold,
        "high_control_nodes": high_control_nodes,
        "high_control_count": len(high_control_nodes),
        "low_discrimination_metrics": [
            column for column, stats in distribution.items() if stats["cv"] < 0.2
        ],
    }


def select_metric_columns(columns: Iterable[str]) -> list[str]:
    """筛出受支持的指标列。"""
    return [column for column in columns if column in METRIC_COLUMNS]
