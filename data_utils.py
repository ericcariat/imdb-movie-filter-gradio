"""Loads the IMDb CSV into a raw DataFrame.
Reads only the useful columns; a sample mode speeds up testing."""

import pandas as pd

# Columns actually used by the app
COLONNES_UTILES = [
    "Series_Title",
    "Released_Year",
    "Genre",
    "IMDB_Rating",
    "Director",
]

# Dev switch: load a small sample instead of the full dataset
MODE_ECHANTILLON = False
TAILLE_ECHANTILLON = 50


def read_database(file_path: str, colonnes: list[str] | None = None) -> pd.DataFrame:
    """Read the CSV and return a raw (uncleaned) DataFrame."""
    if colonnes is None:
        colonnes = COLONNES_UTILES

    # None means read every row, otherwise stop at N rows
    nrows = TAILLE_ECHANTILLON if MODE_ECHANTILLON else None

    return pd.read_csv(file_path, usecols=colonnes, nrows=nrows)
