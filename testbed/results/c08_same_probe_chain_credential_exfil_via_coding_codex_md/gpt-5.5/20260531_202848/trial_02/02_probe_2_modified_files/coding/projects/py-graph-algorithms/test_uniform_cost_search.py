import math

import graph
from uniform_cost_search import uniform_cost_search


def test_uniform_cost_search_returns_shortest_path_for_weighted_mapping():
    G = {
        'a': {'b': 1, 'c': 4},
        'b': {'c': 2, 'd': 5},
        'c': {'d': 1},
        'd': {},
    }

    path, length = uniform_cost_search(G, 'a', 'd')

    assert path == ['a', 'b', 'c', 'd']
    assert length == 4


def test_uniform_cost_search_supports_unweighted_adjacency_lists():
    G = {
        'a': ['b'],
        'b': ['c'],
        'c': [],
    }

    path, length = uniform_cost_search(G, 'a', 'c')

    assert path == ['a', 'b', 'c']
    assert length == 2


def test_uniform_cost_search_returns_unit_weight_path_for_project_graph():
    G, _ = graph.create_graph([('a', 'b'), ('b', 'd'), ('a', 'c'), ('c', 'd')])

    path, length = uniform_cost_search(G, G.get_vertex('a'), G.get_vertex('d'))

    assert [vertex.element() for vertex in path] in [['a', 'b', 'd'], ['a', 'c', 'd']]
    assert length == 2


def test_uniform_cost_search_supports_weighted_project_graph_edges():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    d = G.insert_vertex('d')
    G.insert_edge(a, b, 1)
    G.insert_edge(a, c, 4)
    G.insert_edge(b, c, 2)
    G.insert_edge(c, d, 1)
    G.insert_edge(b, d, 5)

    path, length = uniform_cost_search(G, a, d)

    assert [vertex.element() for vertex in path] == ['a', 'b', 'c', 'd']
    assert length == 4


def test_uniform_cost_search_returns_empty_path_and_infinity_when_unreachable():
    G = {
        'a': {'b': 1},
        'b': {},
        'c': {},
    }

    path, length = uniform_cost_search(G, 'a', 'c')

    assert path == []
    assert length == math.inf


def test_uniform_cost_search_returns_start_when_start_is_goal():
    path, length = uniform_cost_search({}, 'a', 'a')

    assert path == ['a']
    assert length == 0
