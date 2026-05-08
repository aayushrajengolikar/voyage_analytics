import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Load dataset once
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # app/
file_path = os.path.join(BASE_DIR, "data", "hotel.csv")

df_travel = pd.read_csv(file_path)

# Create features
df_travel['features'] = (
    df_travel['place'].astype(str) + " " +
    df_travel['days'].astype(str) + " " +
    df_travel['price'].astype(str)
)

# TF-IDF
tfidf = TfidfVectorizer(max_features=5000)
tfidf_matrix = tfidf.fit_transform(df_travel['features'])


def recommend_similar(index: int, top_n: int = 5):
    try:
        query_vector = tfidf_matrix[index]

        similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()

        top_indices = similarity_scores.argsort()[-50:][::-1]

        recommended_places = []
        seen = set()

        for i in top_indices:
            place = df_travel.iloc[i]['place']

            if place not in seen:
                seen.add(place)
                recommended_places.append(place)

            if len(recommended_places) == top_n:
                break

        return recommended_places

    except Exception as e:
        return {"error": str(e)}