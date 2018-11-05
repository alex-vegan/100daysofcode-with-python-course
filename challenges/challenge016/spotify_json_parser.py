import spotify_api
from pprint import pprint as pp
import json
from collections import namedtuple
from tabulate import tabulate as tb


# === first need create app on dashboard and receive two sixteen bite keys ===
CLIENT_ID = 'abccafxxxxxxxxxxxxxxxx41fd94d3e7'
CLIENT_SECRET = '24c3e3xxxxxxxxxxxxxxxx3f742bc4e2'

JSON_TRACK_FILE = 'resp_spotify_track.json'
JSON_ARTIST_FILE = 'resp_spotify_artist.json'

TRACK = 'Heavy'
ARTIST = 'Jimi'


def parse_json_track(JSON_TRACK_FILE, num_show=10):
    """
    function for parsing file in json-format from Spotify musician server
    for receiving top-tracks by track name
    in that version track name is statical == "Heavy"
    """
    with open(JSON_TRACK_FILE) as f:
        data = json.load(f)
        num_tracks = len(data['tracks']['items'])
        print(f'For word "{TRACK}" has been found {num_tracks} tracks')
        Track = namedtuple('Track', 'track artist album year duration popularity')
        track_list = []
        for num in range(num_tracks):
            artist_list = []
            for item in data['tracks']['items'][num]['album']['artists']:
                artist_list.append(item['name'])
            artist = '/'.join(artist_list)
            album = data['tracks']['items'][num]['album']['name']
            if len(album) > 40:
                album = f'{album[:37]}...'
            track = data['tracks']['items'][num]['name']
            year = data['tracks']['items'][num]['album']['release_date']
            duration_ms = data['tracks']['items'][num]['duration_ms']
            duration = (f'{int((duration_ms / 1000) // 60)}min.'
                        f'{int((duration_ms / 1000) % 60)}sec.')
            popularity = data['tracks']['items'][num]['popularity']
            track_list.append(Track(artist=artist, album=album, track=track, \
                                    year=year, duration=duration, \
                                    popularity=popularity))
        sorted_track_list = sorted(track_list, key=lambda x: -x.popularity)
        print(tb(sorted_track_list[:num_show], headers=track_list[0]._fields))
    return None


def parse_json_artist(JSON_ARTIST_FILE, num_show=10):
    """
    function for pasing json-file by artist name
    now staic word = "Jimi"
    """
    with open(JSON_ARTIST_FILE) as f:
        data = json.load(f)
        num_artist = len(data['artists']['items'])
        print(f'For word "{ARTIST}" has been found {num_artist} artists')
        Artist = namedtuple('Artist', 'name popularity genres')
        artist_list = []
        for num in range(num_artist):
            name = data['artists']['items'][num]['name']
            popularity = data['artists']['items'][num]['popularity']
            genres = ', '.join(data['artists']['items'][num]['genres'])
            if not genres:
                genres = '-'
            artist_list.append(Artist(name=name, popularity=popularity, \
                                      genres=genres))
        sorted_artist_list = sorted(artist_list, key=lambda x: -x.popularity)
        print(tb(sorted_artist_list[:num_show], headers=artist_list[0]._fields))
    return None


def main():
    """
    function that start other functions and nothing else
    """
    print('<<< Spotify Parser >>>')
    print('-'*101)
    spotify_api.get_json_file(JSON_TRACK_FILE, TRACK, 'track', CLIENT_ID, CLIENT_SECRET)
    parse_json_track(JSON_TRACK_FILE)
    print('-'*101)
    spotify_api.get_json_file(JSON_ARTIST_FILE, ARTIST, 'artist', CLIENT_ID, CLIENT_SECRET)
    parse_json_artist(JSON_ARTIST_FILE)
    print('-'*101)


if __name__ == "__main__":
    main()
