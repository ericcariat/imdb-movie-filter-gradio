"""Gradio entry point for the IMDb explorer app.
Builds the UI and wires it to the data/filter modules."""

import gradio as gr

from data_utils import read_database
from processing import (
    clean_data,
    get_genres,
    get_year_bounds,
    get_rating_bounds,
)
from filters import filter_movies

# Load and clean the data once at startup
print("Lecture de la base...")
df = clean_data(read_database("imdb_top_1000.csv"))
print(f"Base chargee : {len(df)} films.")

# Values that populate the widgets (never hard-coded)
GENRES = ["Tous"] + get_genres(df)
ANNEE_MIN, ANNEE_MAX = get_year_bounds(df)
NOTE_MIN, NOTE_MAX = get_rating_bounds(df)


def update_results(titre, genre, note_min, annee_min, annee_max):
    """Adapter between the UI and filter_movies."""
    return filter_movies(df, titre, genre, note_min, annee_min, annee_max)


# UI
with gr.Blocks(title="Explorer les donnees IMDb") as demo:
    gr.Markdown("# 🎬 Explorer les donnees IMDb (Top 1000)")

    with gr.Tabs():
        # Tab 1: filters
        with gr.Tab("Filtres"):
            with gr.Row():
                titre_input = gr.Textbox(
                    label="Titre",
                    placeholder="ex : dark, godfather...",
                )
                genre_input = gr.Dropdown(
                    choices=GENRES,
                    value="Tous",
                    label="Genre",
                )
            with gr.Row():
                note_input = gr.Slider(
                    minimum=NOTE_MIN,
                    maximum=NOTE_MAX,
                    value=NOTE_MIN,
                    step=0.1,
                    label="Note IMDb minimale",
                )
                annee_min_input = gr.Slider(
                    minimum=ANNEE_MIN,
                    maximum=ANNEE_MAX,
                    value=ANNEE_MIN,
                    step=1,
                    label="Annee min",
                )
                annee_max_input = gr.Slider(
                    minimum=ANNEE_MIN,
                    maximum=ANNEE_MAX,
                    value=ANNEE_MAX,
                    step=1,
                    label="Annee max",
                )

            chercher_btn = gr.Button("Filtrer", variant="primary")

            resultats = gr.Dataframe(
                value=filter_movies(df),  # initial view: full catalog
                label="Resultats",
                interactive=False,
            )

            # Filter widgets, in the order update_results expects
            inputs = [
                titre_input,
                genre_input,
                note_input,
                annee_min_input,
                annee_max_input,
            ]

            # On click, run update_results and show the result
            chercher_btn.click(fn=update_results, inputs=inputs, outputs=resultats)

        # Tab 2: about
        with gr.Tab("A propos"):
            gr.Markdown(
                """
## Comment utiliser cette application

1. **Onglet « Filtres »** : combinez les 4 criteres ci-dessous.
   - **Titre** : recherche partielle, insensible a la casse.
   - **Genre** : choisissez un genre (« Tous » = pas de filtre).
   - **Note IMDb minimale** : ne garde que les films au-dessus de la note.
   - **Annee min / max** : restreint la periode de sortie.
2. Les filtres se combinent : le tableau montre les films qui respectent
   **toutes** les conditions a la fois.

### A propos des donnees
Source : *IMDB Top 1000 Movies* (Kaggle). 1000 films, notes de 7.6 a 9.3.
"""
            )

if __name__ == "__main__":
    demo.launch(share=True)
