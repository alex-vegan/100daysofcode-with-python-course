import research
#from tabulate import tabulate as tb


def main():
    print('<<< Classic Rock RadioStation>>>')
    print('-'*80)
    raws, songs = research.init()
    songs_top10 = research.top_songs(songs, 10)
    for idx, song in enumerate(songs_top10, 1):
        album = '(' + song.artist_clean + ' / ' + str(song.release_year) + ')'
        print(f'{idx:3}. {song.song_clean:30} {album:24} played '
              f'{song.playcount:5} times')
    print('-'*80)



if __name__ == '__main__':
    main()
