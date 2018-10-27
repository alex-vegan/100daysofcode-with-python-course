from typing import List
import requests
import collections
import os
from urllib.request import urlretrieve
from requests.exceptions import ProxyError, ConnectionError, HTTPError, SSLError
import logbook
import sys


FILE = 'movie_logbook.log'

resp_logger = logbook.Logger('Resp')

url_path = 'http://movie_service.talkpython.fm/api/search/'

Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords, '
                                        'duration, genres, rating, year, imdb_score')

def main(file_name=None):
    level = logbook.TRACE
    if file_name:
        logbook.TimedRotatingFileHandler(file_name, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()
    mode = 'stdout' if not file_name else 'file ' + file_name
    msg = f'Logging started. level: {level} mode: {mode}'
    logger = logbook.Logger('Startup')
    logger.notice(msg)
    try:
        keyword = input('Keyword of title search: ')
        if not keyword or not keyword.strip():
            raise ValueError('Must specify a search term.')
        url = os.path.join(url_path, keyword)
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            print(f"OK!")
            resp_logger.notice(f'Connection correctly made. '
                               f'Status code: {response.status_code}')
        results = response.json()
        movies = []
        for r in results.get('hits'):
            movies.append(Movie(**r))
        print(f'There are {len(movies)} movies found.')
        resp_logger.trace(f'For keyword << {keyword} >> has been found {len(movies)} movies')
        for m in movies:
            print(f"{m.title} with code {m.imdb_code} has score {m.imdb_score}")
    except ProxyError:
        error_msg = (f"Could not connect to proxy. "
                     f"Check your proxy settings.")
        print(f"ERROR: " + error_msg)
        resp_logger.warn(error_msg)
    except ConnectionError:
        error_msg = (f"Could not find server. "
                     f"Check your network connection.")
        print(f"ERROR: " + error_msg)
        resp_logger.warn(error_msg)
    except HTTPError:
        error_msg = (f"Could not open the HTTP page. "
                     f"Error number {response.status_code} "
                     f"Reason: {response.reason}")
        print("ERROR: " + error_msg)
        resp_logger.warn(error_msg)
    except SSLError:
        error_msg = (f"Could not open the HTTPS page. "
                     f"Check firewall settings and SSL certificates.")
        print(f"ERROR: " + error_msg)
        resp_logger.warn(error_msg)
    except ValueError:
        print(f"ERROR: You must specify a search term.")
        resp_logger.trace(f'Search term has not been specified')
    except Exception as x:
        print(f"Oh that didn't work!: {x}")
        resp_logger.error(f'!!! System Fatality Crash !!!')


if __name__ == '__main__':
    main(FILE)
