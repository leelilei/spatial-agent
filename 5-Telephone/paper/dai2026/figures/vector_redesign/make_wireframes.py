#!/usr/bin/env python3
"""Generate monochrome editorial wireframes for the four DAI figures."""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle


OUT = Path(__file__).resolve().parent / "wireframes"
OUT.mkdir(parents=True, exist_ok=True)

INK = "#24292F"
MID = "#737B84"
LIGHT = "#D8DDE2"
PALE = "#F3F4F5"
WHITE = "#FFFFFF"

mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
        "font.size": 7.4,
        "axes.titlesize": 8.2,
        "axes.labelsize": 7.4,
        "xtick.labelsize": 6.8,
        "ytick.labelsize": 6.8,
        "axes.linewidth": 0.7,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "legend.frameon": False,
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "savefig.facecolor": "white",
        "figure.facecolor": "white",
    }
)


def save(fig: plt.Figure, name: str) -> None:
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight")
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{name}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def panel_label(ax: plt.Axes, letter: str, x: float = -0.04, y: float = 1.03) -> None:
    ax.text(
        x,
        y,
        letter,
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=9,
        fontweight="bold",
        color=INK,
    )


def arrow(
    ax: plt.Axes,
    p0: tuple[float, float],
    p1: tuple[float, float],
    color: str = MID,
    lw: float = 0.9,
    style: str = "-|>",
    mutation_scale: float = 8,
) -> None:
    ax.add_patch(
        FancyArrowPatch(
            p0,
            p1,
            arrowstyle=style,
            mutation_scale=mutation_scale,
            linewidth=lw,
            color=color,
            shrinkA=0,
            shrinkB=0,
        )
    )


def clean(ax: plt.Axes) -> None:
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def figure_1() -> None:
    fig = plt.figure(figsize=(7.2, 2.75))
    gs = fig.add_gridspec(2, 1, height_ratios=[1.58, 0.94], hspace=0.03)
    ax = fig.add_subplot(gs[0])
    strip = fig.add_subplot(gs[1])
    clean(ax)
    clean(strip)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    strip.set_xlim(0, 1)
    strip.set_ylim(0, 1)
    panel_label(ax, "a", x=-0.025, y=0.94)

    # Continuous information journey.
    y = 0.61
    arrow(ax, (0.08, y), (0.90, y), color=LIGHT, lw=1.0, mutation_scale=7)
    stages = [0.09, 0.33, 0.64, 0.90]
    labels = ["Initialize $v_0$", "Inject $v_1$", "Pairwise relay", "Private probe"]
    for x, label in zip(stages, labels):
        ax.text(x, 0.87, label, ha="center", va="center", fontweight="bold", color=INK)

    # Old state, authoritative update, representative relays, and private probe.
    ax.add_patch(Circle((stages[0], y), 0.026, facecolor=WHITE, edgecolor=MID, lw=1.0))
    diamond = np.array(
        [
            [stages[1], y + 0.036],
            [stages[1] + 0.036, y],
            [stages[1], y - 0.036],
            [stages[1] - 0.036, y],
        ]
    )
    ax.add_patch(Polygon(diamond, closed=True, facecolor=INK, edgecolor=INK, lw=0.9))
    relay_x = [0.55, 0.62, 0.69, 0.76]
    relay_y = [0.61, 0.68, 0.56, 0.64]
    for rx, ry in zip(relay_x, relay_y):
        ax.add_patch(Circle((rx, ry), 0.018, facecolor=WHITE, edgecolor=MID, lw=0.8))
    for p0, p1 in zip(zip(relay_x[:-1], relay_y[:-1]), zip(relay_x[1:], relay_y[1:])):
        arrow(ax, p0, p1, color=MID, lw=0.65, mutation_scale=5)
    ax.add_patch(Circle((stages[3], y), 0.031, facecolor=WHITE, edgecolor=INK, lw=1.0))
    ax.add_patch(Circle((stages[3], y), 0.011, facecolor=INK, edgecolor=INK, lw=0.8))

    ax.text(stages[0], 0.40, "Saturday · front porch", ha="center", color=MID)
    ax.text(stages[1], 0.40, "Sunday · community center", ha="center", color=INK)
    ax.text(0.65, 0.40, "Rounds 2–5 · 25 agents", ha="center", color=MID)

    metrics = [(0.30, "HEARD", "received events"), (0.62, "SAID", "public utterance"), (0.90, "HELD", "private answer")]
    for x, head, sub in metrics:
        ax.plot([x, x], [0.35, 0.23], color=LIGHT, lw=0.8)
        ax.text(x, 0.17, head, ha="center", va="center", fontweight="bold", color=INK)
        ax.text(x, 0.08, sub, ha="center", va="center", color=MID)
    ax.plot([0.755, 0.79], [0.17, 0.17], color=INK, lw=0.8, ls=(0, (2, 2)))
    ax.text(0.773, 0.25, "possible break", ha="center", va="bottom", fontsize=6.5, color=MID)

    # Two compact, parallel causal contrasts.
    strip.plot([0.03, 0.97], [0.98, 0.98], color=LIGHT, lw=0.6)
    rows = [
        (0.72, "same frozen stream $E_i$", "GA", "PROV", "complete pipeline"),
        (0.27, "same candidates", "Frequency", "Max version", "selector only"),
    ]
    for yy, source, upper, lower, note in rows:
        strip.text(0.03, yy, source, ha="left", va="center", fontweight="bold", color=INK)
        arrow(strip, (0.25, yy), (0.34, yy), color=LIGHT, lw=0.8, mutation_scale=6)
        strip.text(0.39, yy + 0.105, upper, ha="center", va="center", color=MID)
        strip.text(0.39, yy - 0.105, lower, ha="center", va="center", fontweight="bold", color=INK)
        strip.plot([0.34, 0.36], [yy, yy + 0.105], color=MID, lw=0.75)
        strip.plot([0.34, 0.36], [yy, yy - 0.105], color=MID, lw=0.75)
        strip.plot([0.45, 0.48], [yy + 0.105, yy], color=MID, lw=0.75)
        strip.plot([0.45, 0.48], [yy - 0.105, yy], color=MID, lw=0.75)
        arrow(strip, (0.48, yy), (0.63, yy), color=MID, lw=0.8, mutation_scale=6)
        strip.text(0.67, yy, "same interview", ha="left", va="center", color=INK)
        strip.text(0.97, yy, note, ha="right", va="center", color=MID, fontsize=6.4)

    save(fig, "fig1_wireframe")


def figure_2() -> None:
    fig = plt.figure(figsize=(7.2, 3.15))
    gs = fig.add_gridspec(2, 2, height_ratios=[2.25, 0.82], width_ratios=[0.82, 1.18], hspace=0.58, wspace=0.34)
    said = fig.add_subplot(gs[0, 0])
    held = fig.add_subplot(gs[0, 1])
    outcomes = fig.add_subplot(gs[1, :])
    panel_label(said, "a", x=-0.08)
    panel_label(held, "b", x=-0.08)
    panel_label(outcomes, "c", x=-0.015, y=1.12)

    # SAID: one strong descriptive movement, broadcast visually secondary.
    said_values = [62.9, 81.8]
    said.scatter([0, 1], said_values, s=[34, 34], color=[MID, INK], zorder=3)
    said.vlines([0, 1], 0, said_values, color=[MID, INK], lw=1.0)
    arrow(said, (0.12, 65), (0.88, 80), color=INK, lw=1.0, mutation_scale=7)
    said.text(0.51, 73, "+18.9 pt", ha="center", va="center", fontsize=10, fontweight="bold", color=INK)
    said.text(0, 67.5, "62.9%\n22 / 35", ha="center", va="bottom", color=MID)
    said.text(1, 85.5, "81.8%\n27 / 33", ha="center", va="bottom", color=INK, fontweight="bold")
    said.scatter([1.62], [100], s=20, facecolor=WHITE, edgecolor=MID, lw=0.9, zorder=3)
    said.text(1.62, 94, "broadcast\n100% · 226/226", ha="center", va="top", color=MID, fontsize=6.4)
    said.set_xlim(-0.35, 1.95)
    said.set_ylim(0, 105)
    said.set_xticks([0, 1])
    said.set_xticklabels(["Baseline", "Source"])
    said.set_yticks([0, 50, 100])
    said.set_ylabel("current-mention share (%)")
    said.set_title("SAID", loc="left", fontweight="bold", pad=5)
    said.text(0.0, -0.26, "among value-bearing utterances", transform=said.transAxes, color=MID, fontsize=6.4)

    # HELD: seed-level pairing, with positive control as a small annotation.
    baseline = np.array([8, 20, 20, 4, 8])
    source = np.array([20, 16, 16, 8, 16])
    for b, s in zip(baseline, source):
        held.plot([0, 1], [b, s], color=LIGHT, lw=0.8, zorder=1)
        held.scatter([0, 1], [b, s], s=14, color=[MID, INK], zorder=2)
    held.plot([0, 1], [12.0, 15.2], color=INK, lw=1.6, zorder=3)
    held.scatter([0, 1], [12.0, 15.2], s=38, facecolor=[WHITE, INK], edgecolor=INK, lw=1.0, zorder=4)
    held.text(-0.08, 12.0, "12.0%", ha="right", va="center", color=MID)
    held.text(1.08, 15.2, "15.2%", ha="left", va="center", color=INK, fontweight="bold")
    held.text(0.5, 26.0, "+3.2 pt", ha="center", va="center", fontsize=10, fontweight="bold", color=INK)
    held.text(0.5, 22.8, "95% CI  [−5.6, 12.0]", ha="center", va="center", color=MID)
    held.text(
        1.42,
        26.0,
        "positive control\nbroadcast 99.2%",
        ha="center",
        va="center",
        fontsize=6.4,
        color=MID,
    )
    held.plot([1.30, 1.30], [0, 29], color=LIGHT, lw=0.7)
    held.set_xlim(-0.35, 1.70)
    held.set_ylim(0, 30)
    held.set_xticks([0, 1])
    held.set_xticklabels(["Baseline", "Source"])
    held.set_yticks([0, 10, 20, 30])
    held.set_ylabel("current HELD (%)")
    held.set_title("HELD", loc="left", fontweight="bold", pad=5)

    # One thin composition strip, not three dashboard charts.
    counts = {
        "Baseline": (15, 15, 95),
        "Source": (19, 3, 103),
        "Broadcast": (124, 0, 1),
    }
    y_positions = [2, 1, 0]
    for y, (name, vals) in zip(y_positions, counts.items()):
        current, stale, unknown = vals
        total = sum(vals)
        fractions = np.array(vals) / total * 100
        left = 0.0
        styles = [
            dict(facecolor=INK, edgecolor=INK, hatch=None),
            dict(facecolor=WHITE, edgecolor=INK, hatch="////"),
            dict(facecolor=LIGHT, edgecolor=WHITE, hatch=None),
        ]
        for width, style in zip(fractions, styles):
            outcomes.barh(y, width, left=left, height=0.42, linewidth=0.55, **style)
            left += width
        outcomes.text(-2.5, y, name, ha="right", va="center", color=INK)
        outcomes.text(102, y, f"{current} / {stale} / {unknown}", ha="left", va="center", color=MID, fontsize=6.4)
    outcomes.set_xlim(-15, 126)
    outcomes.set_ylim(-0.5, 2.5)
    outcomes.set_yticks([])
    outcomes.set_xticks([])
    for spine in outcomes.spines.values():
        spine.set_visible(False)
    outcomes.text(0.12, 1.12, "HELD outcomes", transform=outcomes.transAxes, ha="left", va="bottom", fontweight="bold")
    outcomes.text(
        0.98,
        1.12,
        "counts: current / stale / unknown",
        transform=outcomes.transAxes,
        ha="right",
        va="bottom",
        color=MID,
        fontsize=6.1,
    )

    save(fig, "fig2_wireframe")


def paired_panel(
    ax: plt.Axes,
    left_values: np.ndarray,
    right_values: np.ndarray,
    left_label: str,
    right_label: str,
    mean_left: float,
    mean_right: float,
    title: str,
) -> None:
    rng = np.random.default_rng(7)
    jitter = rng.uniform(-0.025, 0.025, size=len(left_values))
    for j, lval, rval in zip(jitter, left_values, right_values):
        ax.plot([j, 1 + j], [lval, rval], color=LIGHT, lw=0.75, zorder=1)
        ax.scatter([j, 1 + j], [lval, rval], s=11, facecolor=WHITE, edgecolor=MID, lw=0.7, zorder=2)
    ax.plot([0, 1], [mean_left, mean_right], color=INK, lw=1.65, zorder=3)
    ax.scatter([0, 1], [mean_left, mean_right], s=38, facecolor=[WHITE, INK], edgecolor=INK, lw=1.0, zorder=4)
    ax.text(-0.10, mean_left, f"{mean_left:.1f}", ha="right", va="center", color=MID)
    ax.text(1.10, mean_right, f"{mean_right:.1f}", ha="left", va="center", color=INK, fontweight="bold")
    ax.set_xlim(-0.25, 1.25)
    ax.set_ylim(0, 100)
    ax.set_xticks([0, 1])
    ax.set_xticklabels([left_label, right_label])
    ax.set_yticks([0, 50, 100])
    ax.set_ylabel("current HELD (%)")
    ax.set_title(title, loc="left", fontweight="bold", pad=11)


def tiny_branch(ax: plt.Axes, y: float, source: str, left: str, right: str) -> None:
    ax.text(0.05, y + 0.12, source, ha="left", va="bottom", fontweight="bold", color=INK)
    ax.plot([0.14, 0.30], [y, y], color=LIGHT, lw=0.9)
    ax.plot([0.30, 0.42], [y, y + 0.11], color=MID, lw=0.8)
    ax.plot([0.30, 0.42], [y, y - 0.11], color=MID, lw=0.8)
    ax.text(0.46, y + 0.11, left, ha="left", va="center", color=MID)
    ax.text(0.46, y - 0.11, right, ha="left", va="center", color=INK, fontweight="bold")
    ax.plot([0.69, 0.80], [y + 0.11, y], color=MID, lw=0.8)
    ax.plot([0.69, 0.80], [y - 0.11, y], color=MID, lw=0.8)
    arrow(ax, (0.80, y), (0.94, y), color=LIGHT, lw=0.9, mutation_scale=6)


def delta_panel(ax: plt.Axes, title: str, labels: list[str], values: list[int]) -> None:
    y = np.arange(len(labels))[::-1]
    for yi, label, value in zip(y, labels, values):
        style = dict(facecolor=INK if value > 0 else LIGHT, edgecolor=INK, linewidth=0.6)
        ax.barh(yi, value, height=0.38, **style)
        ax.text(value + (3 if value >= 0 else -3), yi, f"{value:+d}", ha="left" if value >= 0 else "right", va="center", color=INK)
    ax.axvline(0, color=MID, lw=0.7)
    ax.set_xlim(-60, 65)
    ax.set_ylim(-0.6, len(labels) - 0.4)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, color=MID)
    ax.tick_params(axis="y", length=0, pad=3)
    ax.set_xticks([-50, 0, 50])
    ax.set_title(title, loc="left", fontweight="bold", pad=4)
    ax.set_xlabel("change in pooled answers")
    for spine in ["left", "right", "top"]:
        ax.spines[spine].set_visible(False)


def figure_3() -> None:
    fig = plt.figure(figsize=(7.2, 4.05))
    gs = fig.add_gridspec(2, 3, width_ratios=[1.00, 2.65, 1.15], hspace=0.66, wspace=0.43)
    design = fig.add_subplot(gs[:, 0])
    complete = fig.add_subplot(gs[0, 1])
    selector = fig.add_subplot(gs[1, 1])
    delta_complete = fig.add_subplot(gs[0, 2])
    delta_selector = fig.add_subplot(gs[1, 2])
    clean(design)
    design.set_xlim(0, 1)
    design.set_ylim(0, 1)
    panel_label(design, "a", x=-0.08, y=1.01)
    panel_label(complete, "b", x=-0.21, y=1.10)
    panel_label(selector, "c", x=-0.21, y=1.10)
    panel_label(delta_complete, "d", x=-0.18, y=1.10)

    tiny_branch(design, 0.72, "same frozen stream $E_i$", "GA", "PROV")
    design.text(0.94, 0.72, "interview", ha="right", va="bottom", color=MID, fontsize=6.2)
    tiny_branch(design, 0.30, "same candidates", "Frequency", "Max version")
    design.text(0.94, 0.30, "interview", ha="right", va="bottom", color=MID, fontsize=6.2)
    design.text(0.05, 0.05, "conversation feedback removed", ha="left", va="center", color=MID, fontsize=6.2)

    ga = np.array([36, 36, 24, 28, 28, 36, 36, 32])
    prov = np.array([72, 64, 64, 60, 40, 60, 64, 60])
    frequency = np.array([72, 68, 80, 68, 52, 44, 60, 56])
    max_version = np.array([76, 76, 84, 76, 56, 64, 72, 68])
    paired_panel(complete, ga, prov, "GA", "PROV", 32.0, 60.5, "Complete pipeline")
    paired_panel(selector, frequency, max_version, "Frequency", "Max version", 62.5, 71.5, "Selector only")
    complete.text(
        0.98,
        1.045,
        "Δ +28.5 pt  [21.5, 35.5]  ·  8/8  ·  p=.0078",
        transform=complete.transAxes,
        ha="right",
        va="bottom",
        fontsize=5.9,
        color=INK,
    )
    selector.text(
        0.98,
        1.045,
        "Δ +9.0 pt  [4.4, 13.6]  ·  8/8  ·  p=.0078",
        transform=selector.transAxes,
        ha="right",
        va="bottom",
        fontsize=5.9,
        color=INK,
    )

    delta_panel(delta_complete, "Error shift", ["current", "stale", "unknown"], [57, -5, -52])
    delta_panel(delta_selector, "Error shift", ["current", "stale", "unknown"], [18, -18, 0])
    save(fig, "fig3_wireframe")


def reliability_step_title(ax: plt.Axes, label: str, number: str) -> None:
    ax.text(0.02, 1.18, label, transform=ax.transAxes, ha="left", va="bottom", fontweight="bold", fontsize=7.6, color=INK)
    ax.text(0.02, 1.08, number, transform=ax.transAxes, ha="left", va="bottom", fontweight="bold", fontsize=6.4, color=MID)


def figure_4() -> None:
    fig = plt.figure(figsize=(7.2, 3.20))
    gs = fig.add_gridspec(2, 4, height_ratios=[0.62, 1.55], hspace=0.88, wspace=0.46)
    chain = fig.add_subplot(gs[0, :])
    mini = [fig.add_subplot(gs[1, i]) for i in range(4)]
    clean(chain)
    chain.set_xlim(0, 1)
    chain.set_ylim(0, 1)
    panel_label(chain, "a", x=-0.015, y=0.92)

    xs = [0.08, 0.36, 0.64, 0.92]
    names = ["Reach", "Preserve", "Resolve", "Authenticate"]
    numbers = ["10–19 / 25", "0 → 610 / 720", "+9.0 pt", "43 → 0 stale"]
    arrow(chain, (0.08, 0.56), (0.92, 0.56), color=LIGHT, lw=1.1, mutation_scale=7)
    for x, name, number in zip(xs, names, numbers):
        chain.add_patch(Circle((x, 0.56), 0.026, facecolor=WHITE, edgecolor=INK, lw=1.0))
        chain.text(x, 0.80, name, ha="center", va="center", fontweight="bold", color=INK, fontsize=8.1)
        chain.text(x, 0.25, number, ha="center", va="center", color=MID, fontsize=6.6)

    # Reach: observed receiver range, not a fabricated point estimate.
    ax = mini[0]
    panel_label(ax, "b", x=-0.12, y=1.18)
    reliability_step_title(ax, "Update reach", "10–19 / 25")
    ax.hlines(0, 10, 19, color=INK, lw=3.0)
    ax.scatter([10, 19], [0, 0], s=22, facecolor=WHITE, edgecolor=INK, zorder=3)
    ax.set_xlim(0, 25)
    ax.set_ylim(-1, 1)
    ax.set_yticks([])
    ax.set_xticks([0, 10, 19, 25])
    ax.set_xlabel("receivers")
    for spine in ["left", "right", "top"]:
        ax.spines[spine].set_visible(False)

    # Preserve: default versus explicit norm.
    ax = mini[1]
    panel_label(ax, "c", x=-0.12, y=1.18)
    reliability_step_title(ax, "Text preservation", "0 → 610 / 720")
    vals = [0, 610 / 720 * 100]
    ax.vlines([0, 1], 0, vals, color=[MID, INK], lw=1.1)
    ax.scatter([0, 1], vals, s=26, facecolor=[WHITE, INK], edgecolor=INK, zorder=3)
    ax.text(0, 6, "0", ha="center", va="bottom", color=MID)
    ax.text(1, vals[1] + 6, "84.7%", ha="center", va="bottom", color=INK, fontweight="bold")
    ax.set_xlim(-0.45, 1.45)
    ax.set_ylim(0, 100)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Default", "Strong norm"])
    ax.set_yticks([0, 50, 100])
    ax.set_ylabel("marked utterances (%)")

    # Resolve: matched selector estimate.
    ax = mini[2]
    panel_label(ax, "d", x=-0.12, y=1.18)
    reliability_step_title(ax, "Conflict resolution", "+9.0 pt")
    ax.plot([0, 1], [62.5, 71.5], color=INK, lw=1.6)
    ax.scatter([0, 1], [62.5, 71.5], s=30, facecolor=[WHITE, INK], edgecolor=INK, zorder=3)
    ax.text(0, 59.5, "62.5", ha="center", va="top", color=MID)
    ax.text(1, 74.5, "71.5", ha="center", va="bottom", color=INK, fontweight="bold")
    ax.set_xlim(-0.45, 1.45)
    ax.set_ylim(50, 82)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Frequency", "Max version"])
    ax.set_yticks([50, 65, 80])
    ax.set_ylabel("current HELD (%)")

    # Authenticate: stale acceptance disappears, unknown increases.
    ax = mini[3]
    panel_label(ax, "e", x=-0.12, y=1.18)
    reliability_step_title(ax, "Origin check", "43 → 0 stale")
    rows = [("Naive", (25, 43, 7)), ("APM", (48, 0, 27))]
    for y, (name, vals) in zip([1, 0], rows):
        total = sum(vals)
        widths = np.array(vals) / total * 100
        left = 0.0
        styles = [
            dict(facecolor=INK, edgecolor=INK, hatch=None),
            dict(facecolor=WHITE, edgecolor=INK, hatch="////"),
            dict(facecolor=LIGHT, edgecolor=WHITE, hatch=None),
        ]
        for width, style in zip(widths, styles):
            ax.barh(y, width, left=left, height=0.42, linewidth=0.55, **style)
            left += width
        ax.text(-4, y, name, ha="right", va="center", color=INK)
    ax.set_xlim(-28, 100)
    ax.set_ylim(-0.6, 1.6)
    ax.set_yticks([])
    ax.set_xticks([0, 50, 100])
    ax.set_xlabel("outcome share (%)")
    for spine in ["left", "right", "top"]:
        ax.spines[spine].set_visible(False)
    ax.text(0.5, -0.40, "stale blocked · abstention rises", transform=ax.transAxes, ha="center", va="top", color=MID, fontsize=6.0)

    save(fig, "fig4_wireframe")


def main() -> None:
    figure_1()
    figure_2()
    figure_3()
    figure_4()
    print(f"Saved wireframes to {OUT}")


if __name__ == "__main__":
    main()
