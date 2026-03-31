# Movie Recommender System (TMDB Dataset)

A content-based movie recommendation web app built with Streamlit and the TMDB movie dataset. The app uses movie metadata and cosine similarity to recommend similar films.

## Features

- Search or select a movie from the TMDB dataset
- Receive the top 5 recommended movies
- Display movie poster images from TMDB API
- Built with Streamlit for a simple interactive UI

## Project Structure

- `app.py` - Streamlit application for movie recommendations
- `model/` - Serialized data artifacts used by the app
  - `movie_dict.pkl` - movie metadata dictionary
  - `similarity.pkl` - precomputed similarity matrix
- `input/` - original TMDB dataset files
  - `tmdb_5000_credits.csv`
  - `tmdb_5000_movies.csv`
- `recommendation.ipynb` - notebook used for exploratory analysis and recommender pipeline
- `requirements.txt` - Python dependencies
- `pyproject.toml` - project metadata and dependency configuration

## Prerequisites

- Python 3.13 or newer
- TMDB API key

## Installation

1. Clone the repository or open the project folder.
2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your TMDB API key:

```text
TMDB_API_KEY=your_tmdb_api_key_here
```

## Usage

Run the Streamlit app from the project folder:

```bash
streamlit run app.py
```

Open the local URL shown in the terminal, then select a movie and click **Show Recommendation**.

## Notes

- The recommender uses precomputed similarity vectors in `model/similarity.pkl`.
- Movie posters are fetched live from the TMDB API using the movie ID.
- If `TMDB_API_KEY` is missing or invalid, the app will display an error.

## License

This project is provided as-is for learning and experimentation.
