# Movie Recommender System

A content-based movie recommender system built using Python, Jupyter Notebooks, Pandas, and Scikit-Learn.

This project processes movie metadata from the TMDB 5,000 Movie Dataset to recommend similar movies based on their genres, keywords, overview, cast, and crew.

## How it Works

The recommendation system uses **Content-Based Filtering**:
1. **Data Merging:** Merges movie information with credits data on the movie title.
2. **Feature Extraction:** Extracts genres, keywords, cast (top 3 actors), and crew (director) from JSON-formatted columns.
3. **Data Cleaning:** Cleans text by removing spaces to treat full names and multi-word genres as single tokens (e.g., `Johnny Depp` becomes `JohnnyDepp`).
4. **Tag Creation:** Combines all metadata features (overview, genres, keywords, cast, director) into a single text block called `tags`.
5. **Vectorization:** Standardizes text and performs **Bag of Words** vectorization using Scikit-Learn's `CountVectorizer` (removing English stop words, max features = 5000).
6. **Similarity Calculation:** Computes the **Cosine Similarity** between movie vectors to find the closest matches.
7. **Recommendation:** Given a movie title, finds the top 5 most similar movies based on the cosine similarity matrix.

## Dataset

The project uses the **TMDB 5000 Movie Dataset** from Kaggle.
- [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

Please download the following two files and place them in the root directory:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`
