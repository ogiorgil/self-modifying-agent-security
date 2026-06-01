import math

import graph
from astar import a_star


def test_a_star_finds_shortest_path_in_adjacency_mapping():
    G = {
        'a': {'b': 1, 'c': 4},
        'b': {'c': 2, 'd': 5},
        'c': {'d': 1},
        'd': {},
    }
    heuristic = {
        'a': 3,
        'b': 2,
        'c': 1,
        'd': 0,
    }

    path, length = a_star(G, 'a', 'd', lambda node: heuristic[node])

    assert path == ['a', 'b', 'c', 'd']
    assert length == 4


def test_a_star_finds_shortest_path_in_graph_object():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    d = G.insert_vertex('d')
    G.insert_edge(a, b, 1)
    G.insert_edge(a, c, 4)
    G.insert_edge(b, c, 2)
    G.insert_edge(c, d, 1)
    heuristic = {
        a: 3,
        b: 2,
        c: 1,
        d: 0,
    }

    path, length = a_star(G, a, d, lambda node: heuristic[node])

    assert [node.element() for node in path] == ['a', 'b', 'c', 'd']
    assert length == 4


def test_a_star_returns_infinity_when_goal_is_unreachable():
    G = {'a': {'b': 1}, 'b': {}, 'c': {}}

    path, length = a_star(G, 'a', 'c', lambda node: 0)

    assert path == []
    assert length == math.inf
