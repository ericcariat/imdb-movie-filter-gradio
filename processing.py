"""Cleans the raw IMDb data and exposes helpers for the UI widgets.
Pure pandas, no Gradio dependency."""

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy with Released_Year as a numeric column."""
    df = df.copy()
    # Invalid years (e.g. "PG") become NaN instead of crashing
    df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
    return df


def get_genres(df: pd.DataFrame) -> list[str]:
    """Return the sorted list of unique genres."""
    # Genre is multi-valued ("Action, Crime") -> split then explode
    genres = (
        df["Genre"]
        .str.split(",")
        .explode()
        .str.strip()
        .dropna()
        .unique()
    )
    return sorted(genres)


def get_year_bounds(df: pd.DataFrame) -> tuple[int, int]:
    """Return (min_year, max_year), ignoring missing values."""
    years = df["Released_Year"].dropna()
    return int(years.min()), int(years.max())


def get_rating_bounds(df: pd.DataFrame) -> tuple[float, float]:
    """Return (min_rating, max_rating) from IMDB_Rating."""
    return float(df["IMDB_Rating"].min()), float(df["IMDB_Rating"].max())
