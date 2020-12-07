def test_get_single_movie(monkeypatch):
   mock_movie = ['Movie 1']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movie
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movies_list = tmdb_client.get_single_movie()
   assert movie == mock_movie

def test_get_single_movie_cast(monkeypatch):
   mock_cast = ["Cast"]
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movie_cast = tmdb_client.get_single_movie_cast()
   assert movie_cast == mock_cast

def test_get_movie_images(monkeypatch):
   mock_image = ["Image"]
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_image # tutaj jest zle ale nie wiem jak poprawic
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movie_cast = tmdb_client.get_movie_images()
   assert movie_image == mock_image