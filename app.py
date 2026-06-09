import streamlit as st
import pickle
import pandas as pd

@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    movies = pd.DataFrame(movies_dict)

    return movies, similarity


movies, similarity = load_data()


def recommend(movie):

    try:
        movie_index = movies[movies['title'] == movie].index[0]

        distances = similarity[movie_index]

        movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]

        recommendations = []

        for i in movie_list:

            recommendations.append({
                "title": movies.iloc[i[0]].title,
                "score": round(i[1] * 100, 2)
            })

        return recommendations

    except IndexError:
        return []



st.set_page_config(page_title="Movie Recommender",layout="wide")

st.title("Movie Recommendation System")

st.write("Select a movie and get 5 similar movie recommendations.")

selected_movie = st.selectbox(
    "Choose a Movie",
    movies['title'].values,
    index=None,
    placeholder="Search movie..."
)


if st.button("Recommend"):

    if selected_movie:

        recommendations = recommend(selected_movie)

        df = pd.DataFrame(recommendations)

        df.columns = ['Title', 'Score %']

        df.index = df.index + 1

        st.markdown(
            df.to_html(justify='center'),
            unsafe_allow_html=True
        )

    else:
        st.warning("Please select a movie first.")