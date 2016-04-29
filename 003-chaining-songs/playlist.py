import re

"""
My first idea was to do a brute force algorithm, finding all the permutations starting with the lowest amount of
elements and then filter them ut, it was quite a bad idea as I was getting tons of results and filtering them was
taking ages (left for a couple of minutes and was still checking combinations of 3, going up to combinations of
1000 or more qould have literally taken an era).
Then I thought about how to apply a graph structure or a tree structure without much success, even though it seemed
really similar to a pathfinding  algorithm.
After a chat with my gf and some reading online, I got a kind of algorithm (below).
I needed a quick way to look up songs starting/ending with a letter without doing the search everytime, therefore I
stored them in the class then I created the song class as it was better to polish the song names and use them to avoid
lowercase/uppercase mismatches to get the shortest playlist would be probably enough just to get the time from the song
(so add an attribute to Song class) and then sort the matches and the start and end sets by song duration, but i ran
out of time already half an hour ago as it took me a while to get this done so no implementations for that
"""


class Song:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.clean_name = re.sub('[\(\)\.,;:"#\"\'=-]', '', name).strip().rstrip().lower()

    @property
    def first_letter(self):
        return self.clean_name[0]

    @property
    def last_letter(self):
        return self.clean_name[-1]


class Playlist:
    def __init__(self, songs):
        self.songs = [Song(s['id'], s['song']) for s in songs]
        self.start = {}
        self.end = {}
        self._map()

    def _map(self):
        for song in self.songs:
            if song.first_letter in self.start:
                self.start[song.first_letter].add(song.name)
            else:
                self.start[song.first_letter] = set([song.name])
            if song.last_letter in self.end:
                self.end[song.last_letter].add(song.name)
            else:
                self.end[song.last_letter] = set([song.name])

    def find_any(self, song_a, song_b, used=set()):
        starting = self.start.get(song_a[-1].lower(), set()) - used
        ending = self.end.get(song_b[0].lower(), set()) - used
        if not starting or not ending:
            return None
        matches = starting & ending
        if matches:
            return [song_a] + [matches.pop()] + [song_b]
        for start in starting:
            for end in ending:
                ret = self.find_any(start, end, used | set([start, end]))
                if ret:
                    return [song_a] + ret + [song_b]
        return None
