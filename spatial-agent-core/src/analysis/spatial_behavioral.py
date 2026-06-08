"""空间-行为相关性分析模块。"""

from __future__ import annotations

import math
from typing import Any

import networkx as nx
import numpy as np
import pandas as pd
from scipy.stats import spearmanr


HYPOTHESIS_SPECS = {
    "h1": {"event_type": "social", "metric": "integration_z"},
    "h2": {"event_type": "privacy", "metric": "mean_depth_z"},
    "h3": {"event_type": "gatekeeping", "metric": "control_value_z"},
}


def compute_run_level_alignment(
    visits_frame: pd.DataFrame,
    events_frame: pd.DataFrame,
    metrics_frame: pd.DataFrame,
    *,
    round_start: int = 1,
    round_end: int | None = None,
    min_location_visits: int = 5,
) -> dict[str, float]:
    """按 v7 protocol 计算 run-level TAR / BSR。"""
    visits = visits_frame.loc[visits_frame["round"] >= round_start].copy()
    if round_end is not None:
        visits = visits.loc[visits["round"] <= round_end]

    events = events_frame.loc[events_frame["round"] >= round_start].copy()
    if round_end is not None:
        events = events.loc[events["round"] <= round_end]

    visit_counts = visits.groupby("location").size().rename("visits")
    visit_distribution = visit_counts / max(float(visit_counts.sum()), 1.0)
    entropy = _normalized_entropy(visit_distribution.to_numpy())

    frame = (
        metrics_frame.set_index("node_id")
        .join(visit_counts, how="left")
        .fillna({"visits": 0})
        .reset_index()
        .rename(columns={"index": "node_id"})
    )

    output: dict[str, float] = {
        "entropy_run": entropy,
        "num_visited_locations": float((frame["visits"] > 0).sum()),
    }
    valid_frame = frame.loc[frame["visits"] >= min_location_visits].copy()

    for hypothesis, spec in HYPOTHESIS_SPECS.items():
        event_counts = (
            events.loc[events["event_type"] == spec["event_type"]]
            .groupby("location")
            .size()
            .rename(f"{hypothesis}_count")
        )
        hypothesis_frame = valid_frame.set_index("node_id").join(event_counts, how="left").fillna(0.0)
        hypothesis_frame[f"{hypothesis}_rate"] = (
            hypothesis_frame[f"{hypothesis}_count"] / hypothesis_frame["visits"].clip(lower=1)
        )
        rho = _safe_spearman(
            hypothesis_frame[f"{hypothesis}_rate"].to_numpy(),
            hypothesis_frame[spec["metric"]].to_numpy(),
        )
        tar = _fisher_z(rho) if not math.isnan(rho) else float("nan")
        output[f"rho_{hypothesis}_run"] = rho
        output[f"tar_{hypothesis}_run"] = tar
        output[f"bsr_{hypothesis}_run"] = abs(tar) if not math.isnan(tar) else float("nan")

    return output


def compute_windowed_run_metrics(
    visits_frame: pd.DataFrame,
    events_frame: pd.DataFrame,
    metrics_frame: pd.DataFrame,
    *,
    window_size: int,
    min_location_visits: int = 5,
) -> pd.DataFrame:
    """按时间窗口计算 run-level 指标。"""
    max_round = int(visits_frame["round"].max())
    rows = []
    for start in range(1, max_round + 1, window_size):
        end = min(start + window_size - 1, max_round)
        row = compute_run_level_alignment(
            visits_frame,
            events_frame,
            metrics_frame,
            round_start=start,
            round_end=end,
            min_location_visits=min_location_visits,
        )
        row["window_start"] = start
        row["window_end"] = end
        row["window_index"] = (start - 1) // window_size
        rows.append(row)
    return pd.DataFrame(rows)


def compute_mic_variance_report(
    run_window_frame: pd.DataFrame,
    *,
    comparisons: list[tuple[str, str]],
    dvs: list[str],
    unmatched_bootstrap: int = 200,
) -> pd.DataFrame:
    """比较 matched / unmatched 条件下的差值方差。"""
    rows: list[dict[str, Any]] = []
    rng = np.random.default_rng(20260318)

    for dv in dvs:
        dv_frame = run_window_frame.dropna(subset=[dv]).copy()
        for window_index, window_slice in dv_frame.groupby("window_index"):
            for left, right in comparisons:
                pair = window_slice.loc[window_slice["condition"].isin([left, right])]
                left_frame = pair.loc[pair["condition"] == left, ["seed", dv]].rename(columns={dv: "left_value"})
                right_frame = pair.loc[pair["condition"] == right, ["seed", dv]].rename(columns={dv: "right_value"})
                matched = left_frame.merge(right_frame, on="seed", how="inner")
                if matched.empty:
                    continue

                matched_diff = matched["left_value"] - matched["right_value"]
                matched_variance = float(matched_diff.var(ddof=1)) if len(matched_diff) > 1 else 0.0
                unmatched_variances = []
                right_values = matched["right_value"].to_numpy()
                for _ in range(unmatched_bootstrap):
                    permuted = rng.permutation(right_values)
                    unmatched_variances.append(
                        float(pd.Series(matched["left_value"].to_numpy() - permuted).var(ddof=1))
                    )
                unmatched_variance = float(np.mean(unmatched_variances))
                variance_reduction = (
                    1.0 - matched_variance / unmatched_variance if unmatched_variance > 0 else 0.0
                )
                icc_seed = estimate_seed_icc(pair[["seed", "condition", dv]].rename(columns={dv: "value"}))
                rows.append(
                    {
                        "window_index": int(window_index),
                        "window_start": int(window_slice["window_start"].min()),
                        "window_end": int(window_slice["window_end"].max()),
                        "dv": dv,
                        "comparison": f"{left}-{right}",
                        "matched_variance": matched_variance,
                        "unmatched_variance": unmatched_variance,
                        "variance_reduction": variance_reduction,
                        "icc_seed": icc_seed,
                    }
                )
    return pd.DataFrame(rows)


def estimate_seed_icc(frame: pd.DataFrame) -> float:
    """基于 seed × condition 面板估计 seed 层面的 ICC(1,k)。"""
    pivot = frame.pivot_table(index="seed", columns="condition", values="value")
    pivot = pivot.dropna(axis=0, how="any")
    if pivot.shape[0] < 2 or pivot.shape[1] < 2:
        return float("nan")

    k = pivot.shape[1]
    grand_mean = float(pivot.to_numpy().mean())
    row_means = pivot.mean(axis=1)
    ss_between = float(k * ((row_means - grand_mean) ** 2).sum())
    ss_within = float(((pivot.sub(row_means, axis=0)) ** 2).to_numpy().sum())
    ms_between = ss_between / max(pivot.shape[0] - 1, 1)
    ms_within = ss_within / max(pivot.shape[0] * (k - 1), 1)
    denominator = ms_between + (k - 1) * ms_within
    if np.isclose(denominator, 0.0):
        return 0.0
    return float(max((ms_between - ms_within) / denominator, 0.0))


def compute_windowed_network_metrics(
    social_events: pd.DataFrame,
    *,
    num_agents: int,
    num_rounds: int,
    window_size: int,
) -> pd.DataFrame:
    """按窗口计算网络收敛指标。"""
    rows = []
    for start in range(1, num_rounds + 1, window_size):
        end = min(start + window_size - 1, num_rounds)
        window_events = social_events.loc[
            (social_events["round"] >= start) & (social_events["round"] <= end)
        ]

        graph = nx.Graph()
        graph.add_nodes_from(range(num_agents))
        if not window_events.empty:
            for _, event in window_events.iterrows():
                edge = tuple(sorted((int(event["agent_id"]), int(event["target_id"]))))
                weight = graph.get_edge_data(*edge, default={}).get("weight", 0)
                graph.add_edge(*edge, weight=weight + 1)

        weights = [attrs.get("weight", 1.0) for _, _, attrs in graph.edges(data=True)]
        degree_sequence = [degree for _, degree in graph.degree()]
        rows.append(
            {
                "window_index": (start - 1) // window_size,
                "window_start": start,
                "window_end": end,
                "density": float(nx.density(graph)),
                "clustering": float(nx.average_clustering(graph)) if graph.number_of_edges() else 0.0,
                "degree_gini": _gini(degree_sequence),
                "mean_interaction_strength": float(np.mean(weights)) if weights else 0.0,
            }
        )
    return pd.DataFrame(rows)


def assess_convergence(
    window_metrics: pd.DataFrame,
    *,
    window_size: int,
    delta_threshold: float,
    min_stable_windows: int,
    holdout_rounds: int,
) -> dict[str, Any]:
    """按 v7 的窗口规则判断是否收敛。"""
    metric_columns = ["density", "clustering", "degree_gini", "mean_interaction_strength"]
    ordered = window_metrics.sort_values("window_index").reset_index(drop=True)
    denominators = ordered[metric_columns].std(ddof=0).replace(0, 1e-6)

    delta_rows = []
    stable_flags = []
    for index in range(len(ordered)):
        if index == 0:
            deltas = {f"delta_{column}": float("nan") for column in metric_columns}
            stable = False
        else:
            deltas = {}
            stable = True
            for column in metric_columns:
                delta = abs(ordered.loc[index, column] - ordered.loc[index - 1, column]) / max(
                    float(denominators[column]), 1e-6
                )
                deltas[f"delta_{column}"] = float(delta)
                stable = stable and delta < delta_threshold
        stable_flags.append(stable)
        delta_rows.append(deltas)

    delta_frame = pd.concat([ordered, pd.DataFrame(delta_rows)], axis=1)
    delta_frame["stable"] = stable_flags
    holdout_windows = int(math.ceil(holdout_rounds / window_size))

    convergence_round = None
    holdout_passed = False
    for index in range(min_stable_windows - 1, len(delta_frame)):
        stable_slice = delta_frame.loc[index - min_stable_windows + 1 : index, "stable"]
        if not stable_slice.all():
            continue
        holdout_slice = delta_frame.loc[index + 1 : index + holdout_windows, "stable"]
        if len(holdout_slice) >= holdout_windows and holdout_slice.all():
            convergence_round = int(delta_frame.loc[index, "window_end"])
            holdout_passed = True
            break

    recommended_rounds = 200 if convergence_round and convergence_round <= 200 else 300
    return {
        "converged": convergence_round is not None,
        "convergence_round": convergence_round,
        "holdout_passed": holdout_passed,
        "recommended_rounds": recommended_rounds,
        "delta_threshold": delta_threshold,
        "min_stable_windows": min_stable_windows,
        "holdout_rounds": holdout_rounds,
        "window_metrics": delta_frame,
    }


def _safe_spearman(left: np.ndarray, right: np.ndarray) -> float:
    if len(left) < 3 or len(right) < 3:
        return float("nan")
    if np.allclose(left, left[0]) or np.allclose(right, right[0]):
        return float("nan")
    rho, _ = spearmanr(left, right)
    return float(rho) if rho == rho else float("nan")


def _fisher_z(rho: float) -> float:
    clipped = float(np.clip(rho, -0.999999, 0.999999))
    return float(np.arctanh(clipped))


def _normalized_entropy(probabilities: np.ndarray) -> float:
    probabilities = probabilities[probabilities > 0]
    if len(probabilities) <= 1:
        return 0.0
    entropy = -float(np.sum(probabilities * np.log(probabilities)))
    return float(entropy / np.log(len(probabilities)))


def _gini(values: list[float]) -> float:
    array = np.sort(np.asarray(values, dtype=float))
    if array.size == 0 or np.isclose(array.sum(), 0.0):
        return 0.0
    index = np.arange(1, array.size + 1)
    return float((2 * np.sum(index * array) / (array.size * array.sum())) - (array.size + 1) / array.size)
