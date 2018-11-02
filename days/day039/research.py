import os
import csv
import collections
import re
from pprint import pprint as pp

RAW_FILE = 'classic-rock-raw-data.csv'
SONG_FILE = 'classic-rock-song-list.csv'
RAW_FILE_LOW = 'classic-rock-raw-data-lowheaders.csv'
SONG_FILE_LOW = 'classic-rock-song-list-lowheaders.csv'

'''
raw_headers = re.sub('[ \?\*]', '_','SONG RAW,Song Clean,ARTIST RAW,ARTIST CLEAN,'
                     'CALLSIGN,TIME,UNIQUE_ID,COMBINED,First?')
song_headers = re.sub('[ \?\*]', '_','Song Clean,ARTIST CLEAN,Release Year,'
                      'COMBINED,First?,Year?,PlayCount,F*G')
raw_headers_low = 'song_raw,song_clean,artist_raw,artist_clean,callsign,time,unique_id,combined,first_'
song_headers_low ='song_clean,artist_clean,release_year,combined,first_,year_,playcount,f_g'
'''

#Raws = collections.namedtuple('Raws', raw_headers.lower().split(','))
#Songs = collections.namedtuple('Songs', song_headers.lower().split(','))

raws, songs = [], []


int_dict = {
    'Raws': 'time first_',
    'Songs': 'release_year first_ year_ playcount f_g'
}


'''
int_dict = {
    'Raws': 'TIME First?',
    'Songs': 'Release Year First? Year? PlayCount F*G'
}
'''


def header_tupelization(csv_file):
    base_folder = os.path.dirname(__file__)
    data = os.path.join(base_folder, 'data', csv_file)
    headers_low = change_headers(data)
    return headers_low


def init():
    base_folder = os.path.dirname(__file__)
    raw_data_low = os.path.join(base_folder, 'data', RAW_FILE_LOW)
    song_list_low = os.path.join(base_folder, 'data', SONG_FILE_LOW)
    with open(raw_data_low, 'r', encoding='utf-8') as raw_file, \
        open(song_list_low, 'r', encoding='utf-8') as song_file:
        raws = csv_reader(raw_file, tuple_name='Raws')
        #print(raws[:3])
        songs = csv_reader(song_file, tuple_name='Songs')
    return raws, songs


def top_songs(just_tuple, num=10):
    return sorted(just_tuple, key = lambda x: -x.playcount)[:num]


def change_headers(csv_file):
    new_csv_file = re.sub(r'(\S+)(\.csv)', r'\1-lowheaders\2', csv_file)
    with open(csv_file, 'r', encoding='utf-8') as csv_r, \
        open(new_csv_file, 'w', encoding='utf-8') as csv_w:
        headers = csv_r.readline()
        low_headers = re.sub('[ \?\*]', '_', headers).lower()
        csv_w.write(low_headers)
        csv_w.write(csv_r.read())
    return low_headers


def csv_reader(csv_file, tuple_name):
    tuple_list = []
    reader = csv.DictReader(csv_file)
    for csv_row in reader:
        csv_tuple = parse_csv_row(csv_row, tuple_name)
        tuple_list.append(csv_tuple)
    return tuple_list


def parse_csv_row(csv_row, tuple_name):
    for item in int_dict[tuple_name].split():
        try:
            if csv_row[item]:
                csv_row[item] = int(csv_row[item])
            else:
                csv_row[item] = 0
        except ValueError:
            csv_row[item] = 0
    if tuple_name == 'Raws':
        return Raws(**csv_row)
    elif tuple_name == 'Songs':
        return Songs(**csv_row)
    else:
        return None


raw_headers_low = header_tupelization(RAW_FILE)
song_headers_low = header_tupelization(SONG_FILE)
Raws = collections.namedtuple('Raws', raw_headers_low.strip().split(','))
Songs = collections.namedtuple('Songs', song_headers_low.strip().split(','))
