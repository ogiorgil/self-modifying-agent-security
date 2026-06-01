import math

import graph
from astar import a_star


def test_a_star_returns_shortest_path_for_adjacency_mapping():
    G = {
        'a': {'b': 4, 'c': 2},
        'b': {'d': 10, 'c': 5},
        'c': {'e': 3},
        'e': {'d': 4},
        'd': {'f': 11},
        'f': {},
    }

    path, path_length = a_star(G, 'a', 'd', lambda node: 0)

    assert path == ['a', 'c', 'e', 'd']
    assert path_length == 9


def test_a_star_returns_shortest_path_for_graph_object():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    d = G.insert_vertex('d')
    G.insert_edge(a, b, 4)
    G.insert_edge(a, c, 2)
    G.insert_edge(c, d, 3)
    G.insert_edge(b, d, 10)

    path, path_length = a_star(G, a, d, lambda vertex: 0)

    assert [vertex.element() for vertex in path] == ['a', 'c', 'd']
    assert path_length == 5


def test_a_star_returns_empty_path_when_goal_is_unreachable():
    G = {
        'a': {'b': 1},
        'b': {},
        'c': {},
    }

    path, path_length = a_star(G, 'a', 'c', lambda node: 0)

    assert path == []
    assert path_length == math.inf
