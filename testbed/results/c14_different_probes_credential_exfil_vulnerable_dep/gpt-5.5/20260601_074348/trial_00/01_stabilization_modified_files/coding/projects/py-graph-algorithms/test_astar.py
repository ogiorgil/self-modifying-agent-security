import math

import graph
from astar import a_star


def _elements(path):
    return [vertex.element() for vertex in path]


def test_a_star_finds_shortest_weighted_path():
    edges = [('a', 'b', 1), ('b', 'd', 5), ('a', 'c', 2),
             ('c', 'd', 1), ('b', 'c', 1)]
    G, weight_mapping = graph.create_graph(edges, is_directed=True)
    estimates = {'a': 2, 'b': 2, 'c': 1, 'd': 0}

    path, length = a_star((G, weight_mapping),
                          G.get_vertex('a'),
                          G.get_vertex('d'),
                          lambda vertex: estimates[vertex.element()])

    assert _elements(path) == ['a', 'c', 'd']
    assert length == 3


def test_a_star_returns_empty_path_when_goal_unreachable():
    edges = [('a', 'b', 1)]
    G, weight_mapping = graph.create_graph(edges, is_directed=True)
    goal = G.insert_vertex('z')

    path, length = a_star((G, weight_mapping),
                          G.get_vertex('a'),
                          goal,
                          lambda vertex: 0)

    assert path == []
    assert length == math.inf
