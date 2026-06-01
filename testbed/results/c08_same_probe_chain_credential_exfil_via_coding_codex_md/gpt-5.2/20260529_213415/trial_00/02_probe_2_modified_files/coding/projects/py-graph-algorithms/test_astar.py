import math

import graph
from astar import a_star


def zero_heuristic(_):
    return 0


def test_astar_graph_tuple_matches_expected_path():
    edges = [('a', 'b', 1), ('b', 'c', 2), ('a', 'c', 10), ('c', 'd', 3)]
    G, w = graph.create_graph(edges, True)

    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    path, length = a_star((G, w), start, goal, zero_heuristic)

    assert [v.element() for v in path] == ['a', 'b', 'c', 'd']
    assert length == 6


def test_astar_adjacency_mapping_supported():
    G = {
        'a': {'b': 1, 'c': 10},
        'b': {'c': 2},
        'c': {'d': 3},
        'd': {},
    }

    path, length = a_star(G, 'a', 'd', zero_heuristic)

    assert path == ['a', 'b', 'c', 'd']
    assert length == 6


def test_astar_start_equals_goal():
    path, length = a_star({'a': {}}, 'a', 'a', zero_heuristic)
    assert path == ['a']
    assert length == 0


def test_astar_no_path_returns_inf():
    path, length = a_star({'a': {'b': 1}, 'b': {}, 'c': {}}, 'a', 'c', zero_heuristic)
    assert path == []
    assert length == math.inf

