import math

import graph
from uniform_cost_search import uniform_cost_search


def build_weighted_graph():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    d = G.insert_vertex('d')
    e = G.insert_vertex('e')

    G.insert_edge(a, b, 1)
    G.insert_edge(a, c, 7)
    G.insert_edge(b, c, 2)
    G.insert_edge(b, d, 5)
    G.insert_edge(c, d, 1)

    return G, a, b, c, d, e


def test_uniform_cost_search_returns_shortest_path_and_length():
    G, a, _, _, d, _ = build_weighted_graph()

    path, length = uniform_cost_search(G, a, d)

    assert [vertex.element() for vertex in path] == ['a', 'b', 'c', 'd']
    assert length == 4


def test_uniform_cost_search_returns_empty_path_for_unreachable_goal():
    G, a, _, _, _, e = build_weighted_graph()

    path, length = uniform_cost_search(G, a, e)

    assert path == []
    assert length == math.inf


def test_uniform_cost_search_returns_start_for_same_start_and_goal():
    G, a, _, _, _, _ = build_weighted_graph()

    path, length = uniform_cost_search(G, a, a)

    assert path == [a]
    assert length == 0
