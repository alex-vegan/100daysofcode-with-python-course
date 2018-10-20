from typing import List
import requests
import collections
import os
from urllib.request import urlretrieve
from requests.exceptions import ProxyError, ConnectionError, HTTPError, SSLError


url_path = 'http://movie_service.talkpython.fm/api/search/'

Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords, '
                                        'duration, genres, rating, year, imdb_score')

def main():
    try:
        keyword = input('Keyword of title search: ')
        if not keyword or not keyword.strip():
            raise ValueError('Must specify a search term.')
        url = os.path.join(url_path, keyword)
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            print(f"OK!")
        results = response.json()
        movies = []
        for r in results.get('hits'):
            movies.append(Movie(**r))
        print(f'There are {len(movies)} movies found.')
        for m in movies:
            print(f"{m.title} with code {m.imdb_code} has score {m.imdb_score}")
    except ProxyError:
        print(f"ERROR: Could not connect to proxy.\n"
              f"Check your proxy settings.")
    except ConnectionError:
        print(f"ERROR: Could not find server.\n"
              f"Check your network connection.")
    except HTTPError:
        print(f"ERROR: Could not open the HTTP page.\n"
              f"Error number {response.status_code}\n"
              f"Reason: {response.reason}")
    except SSLError: 
        print(f"ERROR: Could not open the HTTPS page.\n"
              f"Check firewall settings and SSL certificates.")
    except ValueError:
        print(f"ERROR: You must specify a search term.")
    except Exception as x:
        print(f"Oh that didn't work!: {x}")


if __name__ == '__main__':
    main()
