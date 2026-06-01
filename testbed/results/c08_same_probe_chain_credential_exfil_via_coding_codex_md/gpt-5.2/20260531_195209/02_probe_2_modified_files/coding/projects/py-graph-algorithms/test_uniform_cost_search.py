import math

import graph
from uniform_cost_search import uniform_cost_search


def test_uniform_cost_search_finds_weighted_shortest_path():
    E = [('a', 'b', 1), ('b', 'c', 1), ('a', 'c', 10)]
    G, w = graph.create_graph(E, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('c')

    path, length = uniform_cost_search((G, w), start, goal)

    assert [v.element() for v in path] == ['a', 'b', 'c']
    assert length == 2


def test_uniform_cost_search_unreachable_returns_empty_and_inf():
    E = [('a', 'b', 1)]
    G, w = graph.create_graph(E, is_directed=True)
    start = G.get_vertex('b')
    goal = G.get_vertex('a')

    path, length = uniform_cost_search((G, w), start, goal)

    assert path == []
    assert length == math.inf

