from uplink import Consumer, get, json, response_handler
import requests


@response_handler
def raise_for_status(response):
    response.raise_for_status()
    return response


@json
@raise_for_status
class MovieSearchClient(Consumer):

    def __init__(self):
        super().__init__(base_url="http://movie_service.talkpython.fm/")

    @get('/api/search/{keyword}')
    def search_movies(self, keyword) -> requests.models.Response:
        """Search movies service"""

    @get('/api/director/{director_name}')
    def movies_by_director(self, director_name) -> requests.models.Response:
        """Movies by director service"""

    @get('/api/movie/{imdb_number}')
    def movie_by_imdb_code(self, imdb_number) -> requests.models.Response:
        """Movie by IMDB code service"""
