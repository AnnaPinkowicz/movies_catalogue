from unittest.mock import Mock
import os
import json

import tmdb_client
import pytest


@pytest.fixture
def response_cast():
    response_cast_filepath = os.path.join(
        os.path.dirname(__file__), 'test_sources', 'cast.json'
    )
    with open(response_cast_filepath) as cast_file:
        yield json.load(cast_file)


def test_get_single_movie(monkeypatch):
    mock_movie = ['Movie 1']
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movies_list = tmdb_client.get_single_movie(1)
    assert movies_list == mock_movie


def test_get_single_movie_cast(monkeypatch, response_cast):
    mock_cast = response_cast
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_cast
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movie_cast = tmdb_client.get_single_movie_cast(1)
    assert movie_cast == mock_cast['cast']


def test_get_poster_url():
    size = "w891"
    poster_api_path = "a/b/c"

    poster_url = tmdb_client.get_poster_url(poster_api_path, size)
    poster_url_2 = tmdb_client.get_poster_url(poster_api_path)
    assert f"{tmdb_client.IMAGE_BASE_URL}{size}/{poster_api_path}" == poster_url
    assert f"{tmdb_client.IMAGE_BASE_URL}w342/{poster_api_path}" == poster_url_2



if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
