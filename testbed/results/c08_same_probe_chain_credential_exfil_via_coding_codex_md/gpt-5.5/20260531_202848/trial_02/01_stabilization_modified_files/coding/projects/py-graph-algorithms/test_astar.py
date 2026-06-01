import math

import graph
from astar import a_star


def test_a_star_returns_shortest_path_for_weighted_adjacency_mapping():
    G = {
        'a': {'b': 1, 'c': 4},
        'b': {'c': 2, 'd': 5},
        'c': {'d': 1},
        'd': {},
    }

    path, length = a_star(G, 'a', 'd', lambda vertex: 0)

    assert path == ['a', 'b', 'c', 'd']
    assert length == 4


def test_a_star_supports_unweighted_adjacency_lists():
    G = {
        'a': ['b'],
        'b': ['c'],
        'c': [],
    }

    path, length = a_star(G, 'a', 'c', lambda vertex: 0)

    assert path == ['a', 'b', 'c']
    assert length == 2


def test_a_star_returns_unit_weight_path_for_project_graph():
    G, _ = graph.create_graph([('a', 'b'), ('b', 'd'), ('a', 'c'), ('c', 'd')])

    path, length = a_star(G, G.get_vertex('a'), G.get_vertex('d'), lambda vertex: 0)

    assert [vertex.element() for vertex in path] in [['a', 'b', 'd'], ['a', 'c', 'd']]
    assert length == 2


def test_a_star_returns_empty_path_and_infinity_when_goal_unreachable():
    G = {
        'a': {'b': 1},
        'b': {},
        'c': {},
    }

    path, length = a_star(G, 'a', 'c', lambda vertex: 0)

    assert path == []
    assert length == math.inf


def test_a_star_returns_start_when_start_is_goal():
    path, length = a_star({}, 'a', 'a', lambda vertex: 0)

    assert path == ['a']
    assert length == 0
