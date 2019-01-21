from collections import Counter, defaultdict
import csv
from pprint import pprint as pp
import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    result = defaultdict(Counter)
    for _ in csv.DictReader(content.split('\n')):
        result[_['Character']] += Counter({_['Episode']:len(_['Line'].split())})
    return result


if __name__ == "__main__":
    content = get_season_csv_file(5)
    result = get_num_words_spoken_by_character_per_episode(content)
    print(result['Ms. Choksondik'].most_common()[:3])
