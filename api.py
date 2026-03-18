import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.themoviedb.org/3/movie"

endpoints = {
    "playing":"now_playing",
    "upcoming": "upcoming",
    "top": "top_rated",
    "popular": "popular"
}

def fetch_movies(movie_type):
    if movie_type not in endpoints:
        raise ValueError(f"Invalid movie type: {movie_type}")
    url = f"{BASE_URL}/{endpoints[movie_type]}"
    params = {
        "api_key": API_KEY,
        "language": "en-us",
        "page": 1
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return [movie["title"] for movie in data["results"]]
    except requests.exceptions.RequestException as e:
        raise Exception(f"API Error: {e}")
    
