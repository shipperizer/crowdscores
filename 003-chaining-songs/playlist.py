from collections import defaultdict, deque
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

**************************************************UPDATE***************************************************************
moved the complexity of the algorithm on the creation of the graph, therefore I am not going over the recursion limit
(as I was doing with the previous approach), used a graph structure, djikstra is weighted with the duration of each
song
the lookup disctionary is just used to retrieve the song object on the external call
"""


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


class Song:
    def __init__(self, id, name, duration):
        self.id = id
        self.duration = duration
        self.name = name
        self.clean_name = re.sub('[\(\)\.,;:"#\"\'=-]', '', name).strip().rstrip().lower()

    @property
    def first_letter(self):
        return self.clean_name[0]

    @property
    def last_letter(self):
        return self.clean_name[-1]

    def __repr__(self):
        return 'Song #{} - {}'.format(self.id, self.name)


class Playlist:
    def __init__(self, songs):
        self.songs = [Song(s['id'], s['song'], s['duration']) for s in songs]
        self.lookup = {}
        self.graph = Graph()
        self._graph()

    def _graph(self):
        for song in self.songs:
            self.lookup[song.name] = song
            self.graph.add_node(song)
            for s in self.songs:
                if s.id == song.id:
                    next
                if song.last_letter == s.first_letter:
                    self.graph.add_edge(song, s, int(s.duration))

    def dijkstra(self, initial):
        visited = {initial: int(initial.duration)}
        path = {}

        nodes = set(self.graph.nodes)

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node
            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in self.graph.edges[min_node]:
                try:
                    weight = current_weight + self.graph.distances[(min_node, edge)]
                except:
                    continue
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node

        return visited, path

    def shortest_path(self, origin, destination):
        visited, paths = self.dijkstra(origin)
        full_path = deque()
        _destination = paths[destination]

        while _destination != origin:
            full_path.appendleft(_destination)
            _destination = paths[_destination]

        full_path.appendleft(origin)
        full_path.append(destination)

        return visited[destination], list(full_path)

    def find_any_graph(self, song_a, song_b):
        # song_a and song_b are song names
        start = self.lookup[song_a] if song_a in self.lookup else None
        end = self.lookup[song_b] if song_b in self.lookup else None
        if not (start and end):
            return None
        time, songs = self.shortest_path(start, end)
        return time, [s.name for s in songs]
