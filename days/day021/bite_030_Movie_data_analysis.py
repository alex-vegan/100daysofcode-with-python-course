import csv
from collections import defaultdict, namedtuple, Counter
import os
from urllib.request import urlretrieve

#BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
#TMP = '/tmp'

fname = 'movie_metadata.csv'
#remote = os.path.join(BASE_URL, fname)
#local = os.path.join(TMP, fname)
#urlretrieve(remote, local)

#MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    directors = defaultdict(list)
    with open(fname, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0','')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            if year >= MIN_YEAR:
                m = Movie(title=movie, year=year, score=score)
                directors[director].append(m)
    return directors


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    return round(sum([movie.score for movie in movies]) / len(movies), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    avg = Counter()
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            avg[director] += calc_mean_score(movies)
    return sorted(avg.items(), reverse=True, key=lambda x: x[1])

