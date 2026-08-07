#!/usr/bin/env python3
"""Generate the four main-text figures for the DAI 2026 manuscript."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "exports"
OUT.mkdir(parents=True, exist_ok=True)
DATA = json.loads((ROOT / "figure_source_data.json").read_text())

INK = "#27313A"
MID = "#6E7A85"
LIGHT = "#D9E0E6"
PALE = "#F3F5F7"
BLUE = "#3E6F9E"
BLUE_DARK = "#244A70"
BLUE_LIGHT = "#B9CEE0"
AMBER = "#C9833E"
GREEN = "#5C8A72"
WHITE = "#FFFFFF"

mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
        "font.size": 7.2,
        "axes.titlesize": 8.2,
        "axes.labelsize": 7.2,
        "xtick.labelsize": 6.8,
        "ytick.labelsize": 6.8,
        "axes.linewidth": 0.75,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "legend.frameon": False,
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "savefig.facecolor": "white",
        "figure.facecolor": "white",
    }
)


def save(fig: plt.Figure, stem: str) -> None:
    fig.savefig(OUT / f"{stem}.svg", bbox_inches="tight")
    fig.savefig(OUT / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{stem}.png", dpi=400, bbox_inches="tight")
    plt.close(fig)


def panel_label(ax: plt.Axes, label: str, x: float = -0.12, y: float = 1.04) -> None:
    ax.text(
        x,
        y,
        label,
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=8.4,
        fontweight="bold",
        color=INK,
    )


def clean(ax: plt.Axes) -> None:
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def arrow(
    ax: plt.Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    color: str = MID,
    lw: float = 0.9,
    scale: float = 8,
) -> None:
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=scale,
            linewidth=lw,
            color=color,
            shrinkA=0,
            shrinkB=0,
        )
    )


def figure_1() -> None:
    """Single-column task and measurement schematic."""
    fig, ax = plt.subplots(figsize=(3.32, 2.05))
    clean(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    xs = [0.09, 0.34, 0.64, 0.88]
    y = 0.66
    arrow(ax, (0.08, y), (0.90, y), color=LIGHT, lw=1.4, scale=7)

    ax.add_patch(Circle((xs[0], y), 0.035, facecolor=WHITE, edgecolor=MID, lw=1.1))
    ax.text(xs[0], 0.89, "Initialize", ha="center", fontweight="bold", color=INK)
    ax.text(xs[0], 0.80, "$v_0$: Saturday\nfront porch", ha="center", va="top", color=MID, fontsize=6.2)

    diamond = np.array(
        [[xs[1], y + 0.05], [xs[1] + 0.05, y], [xs[1], y - 0.05], [xs[1] - 0.05, y]]
    )
    ax.add_patch(Polygon(diamond, closed=True, facecolor=BLUE, edgecolor=BLUE_DARK, lw=0.8))
    ax.text(xs[1], 0.89, "Inject update", ha="center", fontweight="bold", color=INK)
    ax.text(xs[1], 0.80, "$v_1$: Sunday\ncommunity center", ha="center", va="top", color=BLUE_DARK, fontsize=6.2)

    relay_points = [(0.54, 0.66), (0.62, 0.72), (0.70, 0.61), (0.77, 0.69)]
    for rx, ry in relay_points:
        ax.add_patch(Circle((rx, ry), 0.021, facecolor=WHITE, edgecolor=MID, lw=0.8))
    for p0, p1 in zip(relay_points[:-1], relay_points[1:]):
        arrow(ax, p0, p1, color=MID, lw=0.7, scale=5)
    ax.text(xs[2], 0.89, "Relay", ha="center", fontweight="bold", color=INK)
    ax.text(xs[2], 0.80, "rounds 2–5 · 25 agents", ha="center", va="top", color=MID, fontsize=6.2)

    ax.add_patch(Circle((xs[3], y), 0.043, facecolor=WHITE, edgecolor=INK, lw=1.1))
    ax.add_patch(Circle((xs[3], y), 0.014, facecolor=BLUE_DARK, edgecolor=BLUE_DARK))
    ax.text(xs[3], 0.89, "Probe", ha="center", fontweight="bold", color=INK)

    # Measurements align with the point at which each quantity is observed.
    metrics = [
        (0.54, "HEARD", "received\nevidence"),
        (0.70, "SAID", "public\nutterance"),
        (0.88, "HELD", "private\nanswer"),
    ]
    for x, head, sub in metrics:
        ax.plot([x, x], [0.55, 0.43], color=LIGHT, lw=0.9)
        ax.text(x, 0.37, head, ha="center", va="center", fontweight="bold", color=INK)
        ax.text(x, 0.28, sub, ha="center", va="top", color=MID, fontsize=5.6, linespacing=0.9)

    # Terminal verdicts belong to the probe, not the relay.
    verdicts = [
        (0.74, "current", BLUE_LIGHT, BLUE_DARK),
        (0.845, "stale", "#F0D3B7", AMBER),
        (0.95, "unknown", LIGHT, MID),
    ]
    for x, label, face, edge in verdicts:
        ax.add_patch(
            FancyBboxPatch(
                (x - 0.039, 0.08),
                0.078,
                0.09,
                boxstyle="round,pad=0.01,rounding_size=0.015",
                facecolor=face,
                edgecolor=edge,
                lw=0.7,
            )
        )
        ax.text(x, 0.125, label, ha="center", va="center", color=INK, fontsize=5.1)
    arrow(ax, (0.88, 0.25), (0.88, 0.18), color=LIGHT, lw=0.8, scale=6)

    save(fig, "fig1_probe")


def figure_2() -> None:
    """Single-column SAID/HELD dissociation with broadcast as a quiet control."""
    d = DATA["figure_2"]
    fig, (said, held) = plt.subplots(
        2,
        1,
        figsize=(3.32, 3.25),
        sharex=True,
        gridspec_kw={"height_ratios": [0.86, 1.14], "hspace": 0.22},
    )
    x = np.array([0.0, 1.0, 2.0])

    said_counts = [d["said"][k] for k in ["baseline", "source", "broadcast"]]
    said_values = [100 * v["current"] / v["valued"] for v in said_counts]
    said.plot(x[:2], said_values[:2], color=BLUE_DARK, lw=1.5, zorder=2)
    said.scatter(x[:2], said_values[:2], s=34, color=[MID, BLUE], edgecolor=WHITE, lw=0.5, zorder=3)
    said.scatter(
        [x[2]],
        [said_values[2]],
        s=34,
        facecolor=WHITE,
        edgecolor=GREEN,
        lw=1.3,
        zorder=3,
    )
    for xpos, value, counts in zip(x, said_values, said_counts):
        said.text(
            xpos,
            value + (5 if xpos < 2 else -8),
            f"{value:.0f}%\n{counts['current']}/{counts['valued']}",
            ha="center",
            va="bottom" if xpos < 2 else "top",
            color=INK if xpos == 1 else MID,
            fontweight="bold" if xpos == 1 else "normal",
            fontsize=6.5,
        )
    said.text(0.5, 35, "descriptive Δ +19 pt", ha="center", color=BLUE_DARK, fontweight="bold")
    said.set_ylim(0, 105)
    said.set_yticks([0, 50, 100])
    said.set_ylabel("current (%)")
    said.set_title("Public utterance · SAID", loc="left", fontweight="bold", pad=3)
    panel_label(said, "a", x=-0.17, y=1.03)

    base = np.array(d["held"]["baseline_per_seed_percent"], dtype=float)
    source = np.array(d["held"]["source_per_seed_percent"], dtype=float)
    rng = np.random.default_rng(11)
    jitter = rng.uniform(-0.025, 0.025, size=len(base))
    for j, b, s in zip(jitter, base, source):
        held.plot([j, 1 + j], [b, s], color=LIGHT, lw=0.9, zorder=1)
        held.scatter([j, 1 + j], [b, s], s=13, facecolor=WHITE, edgecolor=MID, lw=0.7, zorder=2)
    means = [base.mean(), source.mean()]
    held.plot(x[:2], means, color=BLUE_DARK, lw=1.6, zorder=3)
    held.scatter(
        x[:2],
        means,
        s=38,
        facecolor=[WHITE, BLUE],
        edgecolor=BLUE_DARK,
        lw=1.0,
        zorder=4,
    )
    held.scatter(
        [x[2]],
        [d["held"]["broadcast_percent"]],
        s=34,
        facecolor=WHITE,
        edgecolor=GREEN,
        lw=1.3,
        zorder=3,
    )
    held.text(-0.10, means[0], f"{means[0]:.1f}%", ha="right", va="center", color=MID)
    held.text(1.10, means[1], f"{means[1]:.1f}%", ha="left", va="center", color=BLUE_DARK, fontweight="bold")
    held.text(2.0, 94, "99.2%\npositive control", ha="center", va="top", color=GREEN, fontsize=6.3)
    held.text(0.5, 29, "Δ +3.2 pt  ·  95% CI [−5.6, 12.0]", ha="center", color=INK, fontsize=6.5)
    held.set_ylim(0, 105)
    held.set_yticks([0, 25, 50, 75, 100])
    held.set_ylabel("current (%)")
    held.set_xticks(x)
    held.set_xticklabels(["Baseline", "Source", "Broadcast"])
    held.set_title("Private answer · HELD", loc="left", fontweight="bold", pad=3)
    panel_label(held, "b", x=-0.17, y=1.03)
    for ax in [said, held]:
        ax.spines["left"].set_color(MID)
        ax.spines["bottom"].set_color(MID)
        ax.tick_params(colors=INK, length=2.5)

    save(fig, "fig2_dissociation")


def paired_panel(
    ax: plt.Axes,
    left: np.ndarray,
    right: np.ndarray,
    labels: tuple[str, str],
    title: str,
    annotation: str,
) -> None:
    rng = np.random.default_rng(17)
    jitter = rng.uniform(-0.022, 0.022, size=len(left))
    for j, lval, rval in zip(jitter, left, right):
        ax.plot([j, 1 + j], [lval, rval], color=LIGHT, lw=0.75, zorder=1)
        ax.scatter([j, 1 + j], [lval, rval], s=12, facecolor=WHITE, edgecolor=MID, lw=0.7, zorder=2)
    means = [left.mean(), right.mean()]
    ax.plot([0, 1], means, color=BLUE_DARK, lw=1.7, zorder=3)
    ax.scatter([0, 1], means, s=40, facecolor=[WHITE, BLUE], edgecolor=BLUE_DARK, lw=1.0, zorder=4)
    ax.text(-0.08, means[0], f"{means[0]:.1f}", ha="right", va="center", color=MID)
    ax.text(1.08, means[1], f"{means[1]:.1f}", ha="left", va="center", color=BLUE_DARK, fontweight="bold")
    ax.text(0.50, 94, annotation, ha="center", va="center", color=INK, fontsize=6.2)
    ax.set_xlim(-0.24, 1.24)
    ax.set_ylim(0, 100)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(labels)
    ax.set_yticks([0, 50, 100])
    ax.set_title(title, loc="left", fontweight="bold", pad=3)


def shift_panel(
    ax: plt.Axes,
    baseline_counts: np.ndarray,
    method_counts: np.ndarray,
    title: str,
) -> None:
    labels = ["current", "stale", "unknown"]
    delta = method_counts - baseline_counts
    colors = [BLUE if value > 0 else AMBER if label == "stale" else LIGHT for label, value in zip(labels, delta)]
    y = np.arange(3)[::-1]
    ax.axvline(0, color=MID, lw=0.7)
    ax.barh(y, delta, height=0.42, color=colors, edgecolor=INK, linewidth=0.5)
    for yi, label, value in zip(y, labels, delta):
        ax.text(
            value + (2.5 if value >= 0 else -2.5),
            yi,
            f"{value:+d}",
            ha="left" if value >= 0 else "right",
            va="center",
            color=INK,
        )
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.tick_params(axis="y", length=0)
    ax.set_xlim(-60, 65)
    ax.set_xticks([-50, 0, 50])
    ax.set_xlabel("change in pooled answers")
    ax.set_title(title, loc="left", fontweight="bold", pad=3)
    for spine in ["left", "right", "top"]:
        ax.spines[spine].set_visible(False)


def figure_3() -> None:
    """Double-column nested causal evidence figure."""
    d = DATA["figure_3"]
    fig = plt.figure(figsize=(7.0, 3.55))
    gs = fig.add_gridspec(
        2,
        3,
        width_ratios=[1.14, 1.85, 1.0],
        height_ratios=[1.0, 1.0],
        hspace=0.58,
        wspace=0.42,
    )
    architecture = fig.add_subplot(gs[:, 0])
    complete = fig.add_subplot(gs[0, 1])
    selector = fig.add_subplot(gs[1, 1])
    shift_complete = fig.add_subplot(gs[0, 2])
    shift_selector = fig.add_subplot(gs[1, 2])

    methods = list(d["controlled_memory_percent"].keys())
    values = np.array(list(d["controlled_memory_percent"].values()), dtype=float)
    y = np.arange(len(methods))[::-1]
    colors = [BLUE if method == "PROV" else LIGHT for method in methods]
    architecture.barh(y, values, color=colors, edgecolor=INK, linewidth=0.5, height=0.58)
    architecture.set_yticks(y)
    architecture.set_yticklabels(methods)
    architecture.set_xlim(0, 65)
    architecture.set_xticks([0, 25, 50])
    architecture.set_xlabel("current HELD (%)")
    architecture.set_title("End-to-end comparison", loc="left", fontweight="bold", pad=3)
    for yi, value, method in zip(y, values, methods):
        architecture.text(value + 1.5, yi, f"{value:.0f}", va="center", color=BLUE_DARK if method == "PROV" else MID)
    panel_label(architecture, "a", x=-0.21, y=1.02)

    fixed = d["fixed_stream"]
    paired_panel(
        complete,
        np.array(fixed["ga_per_seed_percent"]),
        np.array(fixed["prov_per_seed_percent"]),
        ("GA", "PROV"),
        "Same PROV-generated streams",
        "Δ +28.5 pt [21.5, 35.5] · 8/8 seeds",
    )
    complete.set_ylabel("current HELD (%)")
    panel_label(complete, "b", x=-0.16, y=1.02)
    shift_panel(
        shift_complete,
        np.array(fixed["ga_counts"]),
        np.array(fixed["prov_counts"]),
        "Where outcomes move",
    )
    panel_label(shift_complete, "c", x=-0.20, y=1.02)

    selector_data = d["selector"]
    paired_panel(
        selector,
        np.array(selector_data["frequency_per_seed_percent"]),
        np.array(selector_data["version_per_seed_percent"]),
        ("Frequency", "Max version"),
        "Same normalized candidates",
        "Δ +9.0 pt [4.4, 13.6] · 8/8 seeds",
    )
    selector.set_ylabel("current HELD (%)")
    panel_label(selector, "d", x=-0.16, y=1.02)
    shift_panel(
        shift_selector,
        np.array(selector_data["frequency_counts"]),
        np.array(selector_data["version_counts"]),
        "Where outcomes move",
    )
    panel_label(shift_selector, "e", x=-0.20, y=1.02)

    save(fig, "fig3_nested_evidence")


def stacked_outcomes(ax: plt.Axes, rows: list[tuple[str, np.ndarray]]) -> None:
    for y, (name, counts) in enumerate(rows[::-1]):
        widths = counts / counts.sum() * 100
        left = 0.0
        for width, color in zip(widths, [BLUE, AMBER, LIGHT]):
            ax.barh(y, width, left=left, height=0.48, color=color, edgecolor=WHITE, linewidth=0.5)
            left += width
        ax.text(-4, y, name, ha="right", va="center", color=INK)
    ax.set_xlim(-25, 100)
    ax.set_yticks([])
    ax.set_xticks([0, 50, 100])
    ax.set_xlabel("answer composition (%)")
    for spine in ["left", "right", "top"]:
        ax.spines[spine].set_visible(False)


def figure_4() -> None:
    """Double-column boundary and hardening figure."""
    d = DATA["figure_4"]
    fig = plt.figure(figsize=(7.0, 2.45))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.02, 1.34, 1.08], wspace=0.48)
    preserve = fig.add_subplot(gs[0, 0])
    stress = fig.add_subplot(gs[0, 1])
    attack = fig.add_subplot(gs[0, 2])

    text = d["text_preservation"]
    conditions = ["Default", "Attribution\nnorm"]
    marked = np.array(
        [
            100 * text["default"]["marked"] / text["default"]["utterances"],
            100 * text["norm"]["marked"] / text["norm"]["utterances"],
        ]
    )
    current = np.array(
        [
            100 * text["default"]["current"] / 75,
            100 * text["norm"]["current"] / 75,
        ]
    )
    x = np.array([0, 1])
    preserve.plot(x, marked, color=MID, lw=1.2, ls="--")
    preserve.plot(x, current, color=BLUE_DARK, lw=1.5)
    preserve.scatter(x, marked, s=28, facecolor=WHITE, edgecolor=MID, lw=0.9, zorder=3)
    preserve.scatter(x, current, s=32, facecolor=[WHITE, BLUE], edgecolor=BLUE_DARK, lw=0.9, zorder=3)
    preserve.text(0.03, 9, "markers 0/720", color=MID, fontsize=6.1)
    preserve.text(0.93, 86, "610/720", ha="right", color=MID, fontsize=6.1)
    preserve.text(0.03, 29, "HELD 16/75", color=BLUE_DARK, fontsize=6.1)
    preserve.text(0.93, 96, "75/75", ha="right", color=BLUE_DARK, fontsize=6.1)
    preserve.set_xlim(-0.18, 1.18)
    preserve.set_ylim(0, 105)
    preserve.set_xticks(x)
    preserve.set_xticklabels(conditions)
    preserve.set_yticks([0, 50, 100])
    preserve.set_ylabel("share (%)")
    preserve.set_title("Text preservation", loc="left", fontweight="bold", pad=3)
    panel_label(preserve, "a", x=-0.20, y=1.03)

    channel = d["channel_stress"]
    rates = np.array(channel["rates"])
    stress.plot(rates, channel["drop_current_percent"], "-o", color=BLUE, lw=1.5, ms=4, label="drop metadata")
    stress.plot(rates, channel["garble_current_percent"], "-s", color=AMBER, lw=1.5, ms=4, label="garble value")
    stress.axhline(channel["ga_reference_percent"], color=MID, lw=0.9, ls=(0, (3, 2)))
    stress.text(0.89, channel["ga_reference_percent"] + 3, "GA reference 22%", ha="right", color=MID, fontsize=6.0)
    stress.set_xlim(-0.03, 0.93)
    stress.set_ylim(0, 105)
    stress.set_xticks(rates)
    stress.set_xticklabels(["0", ".3", ".6", ".9"])
    stress.set_yticks([0, 50, 100])
    stress.set_xlabel("peer-relay perturbation rate")
    stress.set_ylabel("current HELD (%)")
    stress.set_title("Channel stress", loc="left", fontweight="bold", pad=3)
    stress.legend(loc="lower left", fontsize=6.0, handlelength=2.2)
    panel_label(stress, "b", x=-0.16, y=1.03)

    attack_data = d["forged_version"]
    stacked_outcomes(
        attack,
        [
            ("Naive PROV", np.array(attack_data["naive_prov_counts"], dtype=float)),
            ("APM", np.array(attack_data["apm_counts"], dtype=float)),
        ],
    )
    attack.set_title("Forged-version defense", loc="left", fontweight="bold", pad=3)
    attack.text(0.02, 0.96, "current", transform=attack.transAxes, color=BLUE, fontsize=5.8)
    attack.text(0.26, 0.96, "stale", transform=attack.transAxes, color=AMBER, fontsize=5.8)
    attack.text(0.42, 0.96, "unknown", transform=attack.transAxes, color=MID, fontsize=5.8)
    attack.text(44, 1, "43 stale", ha="center", va="center", color=WHITE, fontsize=6.1, fontweight="bold")
    attack.text(50, 0, "0 stale", ha="center", va="center", color=WHITE, fontsize=6.1, fontweight="bold")
    panel_label(attack, "c", x=-0.18, y=1.03)

    save(fig, "fig4_boundaries")


def main() -> None:
    figure_1()
    figure_2()
    figure_3()
    figure_4()
    print(f"Saved final figures to {OUT}")


if __name__ == "__main__":
    main()
