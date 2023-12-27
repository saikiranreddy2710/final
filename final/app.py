from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_TMDB_API_KEY' with your TMDb API key
TMDB_API_KEY = '87f37bd86f3f93c22461b32dbd628f38'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    movie_title = request.form.get('movie_title')
    if not movie_title:
        return jsonify({'error': 'Please provide a movie title'}), 400

    # Search for movies using TMDb API
    search_url = f'https://api.themoviedb.org/3/search/movie'
    search_params = {'api_key': TMDB_API_KEY, 'query': movie_title}
    search_response = requests.get(search_url, params=search_params)
    search_results = search_response.json()

    if 'results' not in search_results:
        return jsonify({'error': 'Error fetching movie data from TMDb'}), 500

    first_result = search_results['results'][0]
    movie_id = first_result['id']

    recommendations_url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
    recommendations_params = {'api_key': TMDB_API_KEY}
    recommendations_response = requests.get(recommendations_url, params=recommendations_params)
    recommendations = recommendations_response.json().get('results', [])

    return render_template('recommendations.html', movie_title=movie_title, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
