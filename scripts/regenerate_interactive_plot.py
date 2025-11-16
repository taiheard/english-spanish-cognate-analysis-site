#!/usr/bin/env python3
"""Regenerate the Plotly interactive scatter plot with jittered points."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "language_analysis_masterframe25OCT.csv"
OUTPUT_PATH = ROOT / "assets" / "interactive_option_8_enhanced.html"

DOMAIN_MAP: Dict[str, Dict[str, str]] = {
    "religion_spirituality": {"label": "Religion", "color": "#A52A2A"},
    "technology_tools": {"label": "Technology", "color": "#4682B4"},
}

X_JITTER_RANGE = (-3.0, 3.0)  # years
Y_JITTER_RANGE = (-5.0, 5.0)  # years
RANDOM_SEED = 2025

HOVER_TEMPLATE = (
    "<b style=\"font-size:16px\">%{customdata[0]} / %{customdata[1]}</b><br><br>"
    "<b>Domain:</b> %{meta}<br>"
    "<b>Spanish Word:</b> %{customdata[0]}<br>"
    "<b>English Word:</b> %{customdata[1]}<br>"
    "<b>English First Attestation:</b> %{customdata[3]}<br>"
    "<b>Spanish First Attestation:</b> %{customdata[2]}<br>"
    "<b>Time Gap:</b> %{customdata[4]} years"
    "<extra></extra>"
)


def load_dataset(domains: Iterable[str]) -> pd.DataFrame:
    """Load and clean the master dataset with the required fields."""
    df = pd.read_csv(DATA_PATH)
    df = df[df["cultural_domain"].isin(domains)].copy()

    numeric_cols = [
        "first_attestation_english",
        "first_attestation_spanish",
        "levenshtein_similarity",
        "complexity_overall_complexity",
    ]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    df = df.dropna(subset=["first_attestation_english", "first_attestation_spanish"])
    df["first_attestation_english"] = df["first_attestation_english"].astype(int)
    df["first_attestation_spanish"] = df["first_attestation_spanish"].astype(int)
    df["time_gap"] = df["first_attestation_spanish"] - df["first_attestation_english"]
    df = df.reset_index(drop=True)
    return df


def apply_jitter(df: pd.DataFrame) -> pd.DataFrame:
    """Add deterministic jitter to avoid overlap in dense areas."""
    rng = np.random.default_rng(RANDOM_SEED)
    df = df.copy()
    df["x_jitter"] = (
        df["first_attestation_english"] + rng.uniform(*X_JITTER_RANGE, len(df))
    ).round(2)
    df["y_jitter"] = (
        df["time_gap"] + rng.uniform(*Y_JITTER_RANGE, len(df))
    ).round(2)
    return df


def build_figure(df: pd.DataFrame) -> go.Figure:
    fig = go.Figure()

    # Calculate fixed axis ranges based on all data (including jitter)
    # This ensures the grid stays fixed when traces are hidden/shown
    x_min = df["x_jitter"].min()
    x_max = df["x_jitter"].max()
    y_min = df["y_jitter"].min()
    y_max = df["y_jitter"].max()
    
    # Add small padding to ranges for better visualization
    x_padding = (x_max - x_min) * 0.05
    y_padding = (y_max - y_min) * 0.05
    x_range = [x_min - x_padding, x_max + x_padding]
    y_range = [y_min - y_padding, y_max + y_padding]

    for domain_key, meta in DOMAIN_MAP.items():
        subset = df[df["cultural_domain"] == domain_key]
        if subset.empty:
            continue

        customdata = np.stack(
            [
                subset["spanish_word"],
                subset["english_word"],
                subset["first_attestation_spanish"],
                subset["first_attestation_english"],
                subset["time_gap"],
            ],
            axis=-1,
        )

        fig.add_trace(
            go.Scatter(
                x=subset["x_jitter"],
                y=subset["y_jitter"],
                mode="markers",
                name=meta["label"],
                meta=meta["label"],
                customdata=customdata,
                marker={
                    "color": meta["color"],
                    "size": 12,
                    "opacity": 0.7,
                    "line": {"color": "black", "width": 1},
                },
                hovertemplate=HOVER_TEMPLATE,
            )
        )

    fig.add_shape(
        type="line",
        x0=0,
        x1=1,
        xref="x domain",
        y0=0,
        y1=0,
        yref="y",
        line={"color": "gray", "width": 1, "dash": "dash"},
        opacity=0.5,
    )

    fig.update_layout(
        title={
            "text": (
                "Cross-Linguistic Attestation Patterns: Religion vs Technology Terms in "
                "English and Spanish<br><sub>Hover over dots to see detailed word "
                "information</sub>"
            ),
            "x": 0.5,
            "xanchor": "center",
            "font": {"family": "Arial, sans-serif", "size": 24},
        },
        font={"family": "Arial, sans-serif", "size": 14},
        legend={
            "bgcolor": "rgba(255, 255, 255, 0.9)",
            "bordercolor": "black",
            "borderwidth": 1,
            "font": {"size": 14},
            "x": 0.88,
            "y": 0.98,
        },
        margin={"l": 80, "r": 80, "t": 100, "b": 120},
        plot_bgcolor="white",
        hovermode="closest",
        template="plotly_white",
    )

    fig.update_xaxes(
        title="English Attestation Year",
        showgrid=True,
        gridcolor="lightgray",
        gridwidth=1,
        showline=True,
        linecolor="black",
        linewidth=2,
        range=x_range,  # Fixed range prevents grid from changing
        autorange=False,  # Disable auto-ranging when traces are hidden/shown
        fixedrange=False,  # Allow zoom/pan but maintain base range
    )

    fig.update_yaxes(
        title="Time Gap (Spanish-English)",
        showgrid=True,
        gridcolor="lightgray",
        gridwidth=1,
        showline=True,
        linecolor="black",
        linewidth=2,
        zeroline=True,
        range=y_range,  # Fixed range prevents grid from changing
        autorange=False,  # Disable auto-ranging when traces are hidden/shown
        fixedrange=False,  # Allow zoom/pan but maintain base range
    )

    return fig


def main() -> None:
    df = load_dataset(DOMAIN_MAP.keys())
    jittered = apply_jitter(df)
    fig = build_figure(jittered)
    config = {"responsive": True, "displayModeBar": False}
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    pio.write_html(fig, OUTPUT_PATH, include_plotlyjs="cdn", full_html=True, config=config)
    print(f"Updated plot saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
