from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)

data = pd.read_csv('cleaned_data.csv')
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(data['artists'] + ' ' + data['name'])
kmeans = KMeans(n_clusters=10, random_state=42)
clusters = kmeans.fit_predict(tfidf_matrix)
data['cluster'] = clusters

@app.route('/')
def index():
    return render_template('index.html')

def recommend_from_cluster(song_id, data, tfidf_matrix, num_recommendations=5):
    if song_id not in data['id'].values:
        return "Song ID not found in the dataset."
    cluster = data.loc[data['id'] == song_id, 'cluster'].iloc[0]
    cluster_songs = data[data['cluster'] == cluster]
    song_index = data.index[data['id'] == song_id].tolist()[0]
    song_vector = tfidf_matrix[song_index:song_index+1]
    cluster_indices = cluster_songs.index
    cosine_similarities = cosine_similarity(song_vector, tfidf_matrix[cluster_indices]).flatten()
    similar_indices = np.argsort(-cosine_similarities)[1:num_recommendations+1]
    similar_songs = cluster_songs.iloc[similar_indices]
    return similar_songs[['id', 'name', 'artists']]

@app.route('/recommend', methods=['POST'])
def recommend():
    song_id = request.form['song_id']
    try:
        recommendations = recommend_from_cluster(song_id, data, tfidf_matrix)
        return jsonify([{'name': row['name'], 'artists': row['artists']} for index, row in recommendations.iterrows()])
    except Exception as e:
        return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)
