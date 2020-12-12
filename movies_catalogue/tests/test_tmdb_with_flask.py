from unittest.mock import Mock

import pytest

from main import app


@pytest.mark.parametrize('list_type, result', (
    ("popular", 200),
    ("upcoming", 200),
    ("top_rated", 200),
    ("now_playing", 200),
))
def test_homepage(monkeypatch, list_type, result):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get(f'/?list_type={list_type}')
    assert response.status_code == result
    api_mock.assert_called_once_with(f'{list_type}')