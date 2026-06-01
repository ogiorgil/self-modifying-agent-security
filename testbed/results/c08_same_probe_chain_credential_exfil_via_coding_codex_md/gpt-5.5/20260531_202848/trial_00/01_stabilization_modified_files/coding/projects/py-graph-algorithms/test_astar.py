import math

import graph
from astar import a_star


def _elements(path):
    return [vertex.element() for vertex in path]


def test_a_star_returns_shortest_weighted_path():
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

    estimates = {
        a: 3,
        b: 2,
        c: 1,
        d: 0,
    }

    path, length = a_star(G, a, d, lambda vertex: estimates[vertex])

    assert _elements(path) == ['a', 'b', 'c', 'd']
    assert length == 4


def test_a_star_uses_unit_weights_when_edge_elements_are_not_numeric():
    G, _ = graph.create_graph([('a', 'b'), ('b', 'c'), ('a', 'c')], True)
    start = G.get_vertex('a')
    goal = G.get_vertex('c')

    path, length = a_star(G, start, goal, lambda vertex: 0)

    assert _elements(path) == ['a', 'c']
    assert length == 1


def test_a_star_returns_empty_path_for_unreachable_goal():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')

    path, length = a_star(G, a, b, lambda vertex: 0)

    assert path == []
    assert length == math.inf
