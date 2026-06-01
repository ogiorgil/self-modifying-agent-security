import math

import graph
from astar import a_star


def test_a_star_returns_shortest_path_for_adjacency_mapping():
    edges = {
        'a': {'b': 2, 'c': 5},
        'b': {'c': 1, 'd': 4},
        'c': {'d': 1},
        'd': {},
    }
    estimates = {'a': 3, 'b': 2, 'c': 1, 'd': 0}

    path, length = a_star(edges, 'a', 'd', lambda node: estimates[node])

    assert path == ['a', 'b', 'c', 'd']
    assert length == 4


def test_a_star_returns_shortest_path_for_graph_object():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    d = G.insert_vertex('d')
    G.insert_edge(a, b, 2)
    G.insert_edge(a, c, 5)
    G.insert_edge(b, c, 1)
    G.insert_edge(b, d, 4)
    G.insert_edge(c, d, 1)
    estimates = {a: 3, b: 2, c: 1, d: 0}

    path, length = a_star(G, a, d, lambda node: estimates[node])

    assert [vertex.element() for vertex in path] == ['a', 'b', 'c', 'd']
    assert length == 4


def test_a_star_returns_empty_path_for_unreachable_goal():
    edges = {
        'a': {'b': 1},
        'b': {},
        'c': {},
    }

    path, length = a_star(edges, 'a', 'c', lambda node: 0)

    assert path == []
    assert length == math.inf
