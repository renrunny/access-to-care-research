"""
Visualization helpers for access-to-care research.

Publication-quality chart templates for referral timelines,
geographic patterns, and payer disparity analyses.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

PALETTE = ["#2171b5", "#6baed6", "#bdd7e7", "#f16913", "#fdae6b", "#969696"]
FIGSIZE_WIDE = (12, 6)
FONT_SIZE = 11


def set_publication_style():
    """Apply clean, publication-ready matplotlib defaults."""
    sns.set_theme(style="whitegrid", font_scale=1.1)
    plt.rcParams.update({
        "figure.dpi": 150, "savefig.dpi": 300, "savefig.bbox": "tight",
        "font.size": FONT_SIZE, "axes.titlesize": 13, "axes.labelsize": 12,
    })


def plot_wait_time_distribution(df, days_col="days_to_admission", group_col=None,
                                 title="Referral-to-Admission Wait Time", save_path=None):
    """Plot distribution of wait times, optionally grouped."""
    set_publication_style()
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
    if group_col:
        sns.boxplot(data=df, x=group_col, y=days_col, palette=PALETTE, ax=ax)
        ax.set_xlabel(group_col.replace("_", " ").title())
    else:
        sns.histplot(data=df, x=days_col, kde=True, color=PALETTE[0], ax=ax)
    ax.set_ylabel("Days")
    ax.set_title(title)
    if save_path:
        fig.savefig(save_path)
    return fig, ax


def plot_payer_comparison(df, metric_col, payer_col="payer_category",
                          title="Access Metric by Payer", save_path=None):
    """Bar chart comparing a metric across payer categories."""
    set_publication_style()
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
    order = df.groupby(payer_col)[metric_col].median().sort_values(ascending=False).index
    sns.barplot(data=df, x=payer_col, y=metric_col, order=order, palette=PALETTE, ax=ax, errorbar="ci")
    ax.set_title(title)
    ax.set_xlabel("")
    ax.set_ylabel(metric_col.replace("_", " ").title())
    if save_path:
        fig.savefig(save_path)
    return fig, ax


def plot_conversion_funnel(stages: dict, title="Referral Conversion Funnel", save_path=None):
    """Horizontal funnel chart showing referral pipeline stages."""
    set_publication_style()
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
    labels, values = list(stages.keys()), list(stages.values())
    max_val = max(values)
    colors = sns.color_palette("Blues_r", len(labels))
    ax.barh(range(len(labels)), values, color=colors, edgecolor="white", height=0.6)
    for i, (label, val) in enumerate(zip(labels, values)):
        ax.text(val + max_val * 0.01, i, f"{val:,} ({val/max_val*100:.0f}%)", va="center", fontsize=FONT_SIZE)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_title(title)
    ax.set_xlabel("Count")
    if save_path:
        fig.savefig(save_path)
    return fig, ax
