import json
import os
import pytest

from playlist import Playlist, Song


def is_valid(pl):
    for i in range(1, len(pl)):
        assert Song(0, pl[i - 1], 0).last_letter == Song(0, pl[i], 0).first_letter


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


@pytest.mark.parametrize('start, end', [
    ("Caught Up In You", "Universal Thumbs Up"),
    ("Caught Up In You", "Pictures at an Exhibition: The Great Gate of Kiev"),
    ("Caught Up In You", "Suite Bergamesque, Clair de Lune, No. 3"), ("Caught Up In You", "In My Room"),
    ("Suite Bergamesque, Clair de Lune, No. 3", 'Honey, Honey')])
def test_valid_playlist_shortest(start, end, playlist):
    time, songs = playlist.find_any_graph(start, end)

    is_valid(songs)
    assert sum([int(playlist.lookup[s].duration) for s in songs]) == time
