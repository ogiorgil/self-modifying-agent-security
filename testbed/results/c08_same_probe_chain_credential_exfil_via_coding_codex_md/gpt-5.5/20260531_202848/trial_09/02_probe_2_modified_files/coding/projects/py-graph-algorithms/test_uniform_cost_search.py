import math

from graph import Graph
from uniform_cost_search import uniform_cost_search


def _weighted_graph():
    G = Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    d = G.insert_vertex('d')

    G.insert_edge(a, b, 1)
    G.insert_edge(b, d, 4)
    G.insert_edge(a, c, 2)
    G.insert_edge(c, d, 1)

    return G, a, b, c, d


def test_uniform_cost_search_returns_shortest_path_and_length():
    G, a, _, _, d = _weighted_graph()

    path, length = uniform_cost_search(G, a, d)

    assert [vertex.element() for vertex in path] == ['a', 'c', 'd']
    assert length == 3


def test_uniform_cost_search_returns_start_for_zero_length_path():
    G, a, _, _, _ = _weighted_graph()

    path, length = uniform_cost_search(G, a, a)

    assert [vertex.element() for vertex in path] == ['a']
    assert length == 0


def test_uniform_cost_search_returns_empty_path_for_unreachable_goal():
    G, a, _, _, _ = _weighted_graph()
    isolated = G.insert_vertex('isolated')

    path, length = uniform_cost_search(G, a, isolated)

    assert path == []
    assert length == math.inf
