import json
import os
import pytest

from playlist import Playlist, Song


@pytest.fixture(scope='session')
def songs():
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'song-library.json')
    with open(path) as f:
        return [s for s in json.loads(f.read())]


@pytest.fixture(scope='session')
def playlist(songs):
    return Playlist(songs)


def test_make_playlist(songs, playlist):
    assert len(songs) == len(playlist.songs)
    assert songs[0]['song'] in playlist.start[songs[0]['song'][0].lower()]
    assert songs[0]['song'] in playlist.end[songs[0]['song'][-1].lower()]


@pytest.mark.parametrize('start, end', [
    ("Caught Up In You", "Universal Thumbs Up"),
    ("Caught Up In You", "Pictures at an Exhibition: The Great Gate of Kiev"),
    ("Caught Up In You", "Suite Bergamesque, Clair de Lune, No. 3"), ("Caught Up In You", "In My Room"),
    ("Suite Bergamesque, Clair de Lune, No. 3", 'Honey, Honey')])
def test_valid_playlist(start, end, playlist):
    result = playlist.find_any(start, end)

    def is_valid(pl):
        for i in range(1, len(pl)):
            assert Song(0, pl[i - 1]).last_letter == Song(0, pl[i]).first_letter

    is_valid(result)
