# Movie Recommender System

A content-based movie recommender system built using Python, Jupyter Notebooks, Pandas, and Scikit-Learn.

This project processes movie metadata from the TMDB 5,000 Movie Dataset to recommend similar movies based on their genres, keywords, overview, cast, and crew.

## 🚀 How it Works

The recommendation system uses **Content-Based Filtering**:
1. **Data Merging:** Merges movie information with credits data on the movie title.
2. **Feature Extraction:** Extracts genres, keywords, cast (top 3 actors), and crew (director) from JSON-formatted columns.
3. **Data Cleaning:** Cleans text by removing spaces to treat full names and multi-word genres as single tokens (e.g., `Johnny Depp` becomes `JohnnyDepp`).
4. **Tag Creation:** Combines all metadata features (overview, genres, keywords, cast, director) into a single text block called `tags`.
5. **Vectorization:** Standardizes text and performs **Bag of Words** vectorization using Scikit-Learn's `CountVectorizer` (removing English stop words, max features = 5000).
6. **Similarity Calculation:** Computes the **Cosine Similarity** between movie vectors to find the closest matches.
7. **Recommendation:** Given a movie title, finds the top 5 most similar movies based on the cosine similarity matrix.

## 📁 Dataset

The project uses the **TMDB 5000 Movie Dataset** from Kaggle.
- [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

Please download the following two files and place them in the root directory:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/movie-recommender-system.git
   cd movie-recommender-system
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install numpy pandas scikit-learn nltk ipykernel
   ```

4. **Run the Notebook:**
   Open `movie-recommender-system.ipynb` in your preferred Jupyter environment (e.g., VS Code or Jupyter Notebook) and run all cells to compute similarity scores and test recommendations.

## 📦 Saved Models

After running the notebook, the following pickle files will be generated:
- `movies.pkl` / `movies_dict.pkl` - Processed movie dataset.
- `similarity.pkl` - Computed Cosine Similarity matrix (warning: this file is ~180MB and is gitignored by default).
