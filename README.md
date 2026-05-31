---
title: IMDB_GRADIO_FILTER
app_file: app.py
sdk: gradio
sdk_version: 6.15.2
---
# IMDb Explorer

A small, fun experiment to learn and test **[Gradio](https://www.gradio.app/)**: an
interactive web app to explore the *IMDb Top 1000* movies dataset

> This project is just a learning playground

---

## Technologies & Tools

| Tool | Version | Role |
|------|---------|------|
| [Python](https://www.python.org/) | 3.10 | Language |
| [Gradio](https://www.gradio.app/) | 6.15 | Web UI (components, tabs, events) |
| [pandas](https://pandas.pydata.org/) | 2.3 | Data loading, cleaning, filtering |
| VS Code | — | Editor |
| `.venv` | — | Isolated environment |

**Dataset:** [IMDB Top 1000 Movies](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)
(Kaggle) — 1000 films, ratings from 7.6 to 9.3.

---

## Project Structure

The code is split by responsibility — the business logic knows nothing about Gradio,
so it stays testable and reusable.

```
.
├── app.py            # Gradio entry point: builds the UI and wires the events
├── data_utils.py     # Loads the CSV into a raw DataFrame
├── processing.py     # Cleans the data + helpers for the widgets
├── filters.py        # The 4-filter logic (pure pandas, no Gradio)
├── imdb_top_1000.csv # The dataset (place at project root)
└── requirements.txt  # Dependencies
```

**Data flow:** `data_utils.read_database` → `processing.clean_data` →
`filters.filter_movies` → displayed in `app.py`.

---

## Getting Started

### Prerequisites
- Python 3.10+
- The `imdb_top_1000.csv` file at the project root (download from Kaggle)

### Installation

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

# 2. Install dependencies
pip install gradio pandas

# 3. Run the app
python app.py
```

Then open **http://127.0.0.1:7860** in your browser.

---

## Some issues on the dataset

- **`Released_Year` isn't always numeric.**
- **`Genre` is multi-valued** (`"Action, Crime, Drama"`)
---

## Live Demo

Try the app online on Hugging Face Spaces:
**https://huggingface.co/spaces/erkced/IMDB_GRADIO_FILTER**

