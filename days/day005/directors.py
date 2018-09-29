import csv
from collections import defaultdict, namedtuple, Counter

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=MOVIE_DATA):
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0','')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)
    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    avg = Counter()
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            avg[director] += _calc_mean(movies)
    return avg


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return sum([movie.score for movie in movies]) / len(movies)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    top20 = sorted(get_average_scores(directors).items(),
                   reverse=True, key=lambda x: x[1])[:NUM_TOP_DIRECTORS]
    for cntr in range(NUM_TOP_DIRECTORS):
        print(f'{cntr+1:02}. {top20[cntr][0]:<52} {round(top20[cntr][-1], 1)}')
        print('-' * 60)
        s_movies = sorted(directors[top20[cntr][0]], reverse=True, key=lambda x: x.score)
        for movie in s_movies:
            movie_title = movie.title
            if movie.year >= 1960:
                if len(movie_title) > 50:
                    movie_title = movie_title[:47] + "..."
                print(f'{movie.year}] {movie_title:<50} {round(movie.score, 1)}')
        print()


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    print()
    print_results(directors)


if __name__ == '__main__':
    main()
