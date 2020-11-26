import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "214dd728c566a7ef89fbefffb480101d"
    headers = {"Authorization": f"Bearer {api_token}"}
    # print(headers)
    endpoint_2 = endpoint + "?api_key=" + api_token
    response = requests.get(endpoint_2, headers=headers)
    # print(response.headers)
    return response.json()

# def get_list_of_lists():
#     endpoint = f"https://api.themoviedb.org/4/movie/{list_type}" https://api.themoviedb.org/4/list/{list_id}?page=1&api_key=<<api_key>>
#     # headers = {
#     #     "Authorization": f"Bearer {API_TOKEN}"
#     # }
#     # response = requests.get(endpoint, headers=headers)
#     api_token = "214dd728c566a7ef89fbefffb480101d"
#     headers = {"Authorization": f"Bearer {api_token}"}
#     # print(headers)
#     endpoint_2 = endpoint + "?api_key=" + api_token
#     response = requests.get(endpoint_2, headers=headers)
#     response.raise_for_status()
#     return response.json()

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    # headers = {
    #     "Authorization": f"Bearer {API_TOKEN}"
    # }
    # response = requests.get(endpoint, headers=headers)
    api_token = "214dd728c566a7ef89fbefffb480101d"
    headers = {"Authorization": f"Bearer {api_token}"}
    # print(headers)
    endpoint_2 = endpoint + "?api_key=" + api_token
    response = requests.get(endpoint_2, headers=headers)
    response.raise_for_status()
    return response.json()



def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type='popular'):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    # api_token = "twoj-token"
    # headers = {
    #     "Authorization": f"Bearer {api_token}"
    # }
    # response = requests.get(endpoint, headers=headers)
    api_token = "214dd728c566a7ef89fbefffb480101d"
    headers = {"Authorization": f"Bearer {api_token}"}
    # print(headers)
    endpoint_2 = endpoint + "?api_key=" + api_token
    response = requests.get(endpoint_2, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    # headers = {
    #     "Authorization": f"Bearer {API_TOKEN}"
    # }
    # response = requests.get(endpoint, headers=headers)
    api_token = "214dd728c566a7ef89fbefffb480101d"
    headers = {"Authorization": f"Bearer {api_token}"}
    # print(headers)
    endpoint_2 = endpoint + "?api_key=" + api_token
    response = requests.get(endpoint_2, headers=headers)
    return response.json()["cast"]

def get_cast(movie_id, how_many=5):
    data = get_single_movie_cast(movie_id)
    return data[:how_many]

# text = get_popular_movies()

# print(text)

# curl --request GET  --header 'Authorization: Bearer 214dd728c566a7ef89fbefffb480101d' --header 'Content-Type: application/json;charset=utf-8' https://api.themoviedb.org/3/movie/76341