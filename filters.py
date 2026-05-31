"""Applies the 4 IMDb filters to a cleaned DataFrame.
Filtering is progressive: each criterion narrows the result."""

import pandas as pd

# Columns shown in the results table
COLONNES_AFFICHEES = [
    "Series_Title",
    "Released_Year",
    "Genre",
    "IMDB_Rating",
    "Director",
]


def filter_movies(
    df: pd.DataFrame,
    titre: str = "",
    genre: str = "Tous",
    note_min: float = 0.0,
    annee_min: int = 0,
    annee_max: int = 9999,
) -> pd.DataFrame:
    """Apply the 4 filters and return the displayed columns."""
    result = df

    # Title: case-insensitive partial match
    if titre:
        result = result[
            result["Series_Title"].str.contains(titre, case=False, na=False)
        ]

    # Genre: search inside the multi-valued text
    if genre and genre != "Tous":
        result = result[
            result["Genre"].str.contains(genre, case=False, na=False)
        ]

    # Rating: keep movies at or above the minimum (NaN excluded)
    result = result[result["IMDB_Rating"] >= note_min]

    # Year: keep movies within [annee_min, annee_max]
    result = result[
        (result["Released_Year"] >= annee_min)
        & (result["Released_Year"] <= annee_max)
    ]

    return result[COLONNES_AFFICHEES]
