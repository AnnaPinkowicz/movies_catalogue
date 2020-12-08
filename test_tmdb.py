import pytest
import tmdb_client
from unittest.mock import Mock
import requests
from app import app

def test_get_poster_url_uses_default_size():
   # Przygotowanie danych
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Porównanie wyników
   assert expected_default_size in poster_url

def test_get_single_movie(monkeypatch):
   mock_single_movie = 000000
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   single_movie = tmdb_client.get_single_movie(movie_id=602211)
   assert single_movie == mock_single_movie


def test_get_single_movie_cast(monkeypatch):
   mock_single_movie_cast = {}
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   mock_movie_cast = tmdb_client.get_single_movie_cast(movie_id=000000)
   assert mock_movie_cast == mock_single_movie_cast
 