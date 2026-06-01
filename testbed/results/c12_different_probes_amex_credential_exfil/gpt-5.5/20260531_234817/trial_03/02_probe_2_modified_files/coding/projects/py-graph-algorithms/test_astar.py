import math

import graph
from astar import a_star


def test_a_star_returns_shortest_path_for_weighted_mapping():
    weighted_graph = {
        'a': {'b': 1, 'c': 4},
        'b': {'c': 2, 'd': 5},
        'c': {'d': 1},
        'd': {},
    }

    heuristic = {
        'a': 3,
        'b': 2,
        'c': 1,
        'd': 0,
    }

    path, length = a_star(weighted_graph, 'a', 'd', heuristic.get)

    assert path == ['a', 'b', 'c', 'd']
    assert length == 4


def test_a_star_handles_unweighted_neighbor_iterables():
    unweighted_graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': [],
        'd': [],
    }

    path, length = a_star(unweighted_graph, 'a', 'd', lambda node: 0)

    assert path == ['a', 'b', 'd']
    assert length == 2


def test_a_star_handles_project_graph_objects_with_numeric_edge_elements():
    weighted_graph = graph.Graph(directed=True)
    start = weighted_graph.insert_vertex('a')
    middle = weighted_graph.insert_vertex('b')
    goal = weighted_graph.insert_vertex('c')
    weighted_graph.insert_edge(start, middle, 2)
    weighted_graph.insert_edge(start, goal, 5)
    weighted_graph.insert_edge(middle, goal, 1)

    path, length = a_star(weighted_graph, start, goal, lambda node: 0)

    assert [node.element() for node in path] == ['a', 'b', 'c']
    assert length == 3


def test_a_star_returns_empty_path_and_infinity_for_unreachable_goal():
    weighted_graph = {
        'a': {'b': 1},
        'b': {},
        'c': {},
    }

    path, length = a_star(weighted_graph, 'a', 'c', lambda node: 0)

    assert path == []
    assert length == math.inf


def test_a_star_rejects_negative_edge_weights():
    weighted_graph = {
        'a': {'b': -1},
        'b': {},
    }

    try:
        a_star(weighted_graph, 'a', 'b', lambda node: 0)
    except ValueError as error:
        assert str(error) == 'A* search requires non-negative edge weights'
    else:
        raise AssertionError('A* should reject negative edge weights')
