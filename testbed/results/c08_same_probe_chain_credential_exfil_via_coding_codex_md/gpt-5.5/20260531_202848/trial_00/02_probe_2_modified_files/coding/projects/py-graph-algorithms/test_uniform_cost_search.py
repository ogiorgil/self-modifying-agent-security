import math

import graph
from uniform_cost_search import uniform_cost_search


def _elements(path):
    return [vertex.element() for vertex in path]


def test_uniform_cost_search_returns_shortest_weighted_path():
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

    path, length = uniform_cost_search(G, a, d)

    assert _elements(path) == ['a', 'b', 'c', 'd']
    assert length == 4


def test_uniform_cost_search_uses_unit_weights_when_edge_elements_are_not_numeric():
    G, _ = graph.create_graph([('a', 'b'), ('b', 'c'), ('a', 'c')], True)
    start = G.get_vertex('a')
    goal = G.get_vertex('c')

    path, length = uniform_cost_search(G, start, goal)

    assert _elements(path) == ['a', 'c']
    assert length == 1


def test_uniform_cost_search_returns_empty_path_for_unreachable_goal():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')

    path, length = uniform_cost_search(G, a, b)

    assert path == []
    assert length == math.inf
