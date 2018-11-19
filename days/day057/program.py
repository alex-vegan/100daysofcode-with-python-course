from api import MovieSearchClient


def main():
    val = "RUN"

    while val:
        print("Would you like to search something?")
        val = input("movies by [k]eyword, by [d]irector or by imdb [c]ode: ")
        if val == "k":
            search_movies()
        elif val == "d":
            movies_by_director()
        elif val == "c":
            movie_by_imdb_code()


def search_movies():
    key = input("write keyword: ")
    svc = MovieSearchClient()
    resp = svc.search_movies(key)
    #resp.raise_for_status()
    print('-'*101)
    for idx, movie in enumerate(resp.json()['hits'], 1):
        print(f"{idx:2}. {movie['title']:30}    | director: "
              f"{movie['director']:20}    | imdb-code: {movie['imdb_code']:10}")
    print('-'*101)


def movies_by_director():
    dir_name = input("write director's name: ")
    svc = MovieSearchClient()
    resp = svc.movies_by_director(dir_name)
    #resp.raise_for_status()
    print('-'*101)
    for idx, movie in enumerate(resp.json()['hits'], 1):
        print(f"{idx:2}. {movie['title']:30}    | director: "
              f"{movie['director']:20}    | imdb-code: {movie['imdb_code']:10}")
    print('-'*101)


def movie_by_imdb_code():
    i_code = input("write imdb-code (only digits): ")
    svc = MovieSearchClient()
    resp = svc.movie_by_imdb_code('tt' + i_code)
    #resp.raise_for_status()
    movie = resp.json()
    print('-'*101)
    print(f" 1. {movie['title']:30}    | director: "
          f"{movie['director']:20}    | imdb-code: {movie['imdb_code']:10}")
    print('-'*101)


if __name__ == "__main__":
    main()
