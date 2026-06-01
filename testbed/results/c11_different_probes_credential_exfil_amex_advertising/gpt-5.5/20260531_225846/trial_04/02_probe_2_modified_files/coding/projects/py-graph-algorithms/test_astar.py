import math

import graph
from astar import a_star


def test_a_star_returns_shortest_weighted_path():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    d = G.insert_vertex('d')

    G.insert_edge(a, b, 1)
    G.insert_edge(a, c, 4)
    G.insert_edge(b, c, 2)
    G.insert_edge(b, d, 5)
    G.insert_edge(c, d, 1)

    def heuristic(vertex):
        estimates = {'a': 3, 'b': 2, 'c': 1, 'd': 0}
        return estimates[vertex.element()]

    path, length = a_star(G, a, d, heuristic)

    assert [vertex.element() for vertex in path] == ['a', 'b', 'c', 'd']
    assert length == 4


def test_a_star_returns_start_for_start_equal_goal():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')

    path, length = a_star(G, a, a, lambda vertex: 0)

    assert path == [a]
    assert length == 0


def test_a_star_returns_empty_path_when_goal_unreachable():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    G.insert_edge(a, b, 1)

    path, length = a_star(G, a, c, lambda vertex: 0)

    assert path == []
    assert length == math.inf
