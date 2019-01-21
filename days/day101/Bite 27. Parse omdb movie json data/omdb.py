import glob
import json
import os
from urllib.request import urlretrieve
from pprint import pprint as pp
import re

'''
BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))
'''

files = glob.glob('*json')

def get_movie_data(files=files):
    movie_data = []
    for file in files:
        with open(file) as f:
            movie_data.append(json.load(f))
    return movie_data


def get_single_comedy(movies):
    for m in movies:
        if 'Comedy' in m['Genre']:
            return m['Title']


def get_movie_most_nominations(movies):
    mn_title = ''
    mn_awards = 0
    for m in movies:
        match = re.search(r'(\d+) nominations', m['Awards'])
        nominations = int(match.groups()[0])
        if nominations > mn_awards:
            mn_awards = nominations
            mn_title = m['Title']
    return mn_title


def get_movie_longest_runtime(movies):
    long_title = ''
    long_runtime = 0
    for m in movies:
        match = re.search(r'(\d+) min', m['Runtime'])
        runtime = int(match.groups()[0])
        if runtime > long_runtime:
            long_runtime = runtime
            long_title = m['Title']
    return long_title


if __name__ == "__main__":
    md = get_movie_data()
    #pp(md)
    #for m in md:
        #pp(f"{m['Title']:20} : {m['Genre']:25} : {'Comedy' in m['Genre']}")
        #print(f"{m['Title']:20} : {m['Awards']}")
        #print(f"{m['Title']:20} : {m['Runtime']}")
    #print(get_movie_most_nominations(md))
    #print(get_movie_longest_runtime(md))