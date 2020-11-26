from flask import Flask, render_template

import tmdb_client

from flask import request

app = Flask(__name__)



@app.route('/')
def homepage():
    lists = ["top_rated", "upcoming", "popular", "now_playing"]
    selected_list = request.args.get('list_type', "popular")
    if selected_list not in lists:
        selected_list = "popular"
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, lists=lists)


# @app.route('/')
# def homepage():
#     # movies = tmdb_client.get_popular_movies()["results"][:8]
#     movies = tmdb_client.get_movies(how_many=8)
#     return render_template("homepage.html", movies=movies)

# @app.route("/movie/<movie_id>")
# def movie_details(movie_id):
#     return render_template("movie_details.html")

# @app.route("/movie/<movie_id>")
# def movie_details(movie_id):
#     details = tmdb_client.get_single_movie(movie_id)
#     return render_template("movie_details.html", movie=details)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
   details = tmdb_client.get_single_movie(movie_id)
#    cast = tmdb_client.get_single_movie_cast(movie_id)
   cast = tmdb_client.get_cast(movie_id, how_many=7)
   return render_template("movie_details.html", movie=details, cast=cast)




# @app.route('/')
# def homepage():
#     return render_template("index.html")

# @app.route('/')
# def homepage():
#     movies = ["foo", 123, "qwedjfjsdg", [1,2,3]]
#     return render_template("homepage.html", movies=movies)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


if __name__ == '__main__':
    app.run(debug=True)