import math

import graph
from astar import a_star


def test_a_star_returns_shortest_path_for_weighted_mapping():
    road_map = {
        'a': {'b': 1, 'c': 4},
        'b': {'d': 2},
        'c': {'d': 1, 'e': 7},
        'd': {'e': 1},
        'e': {},
    }
    estimates = {'a': 4, 'b': 3, 'c': 2, 'd': 1, 'e': 0}

    path, length = a_star(road_map, 'a', 'e', lambda node: estimates[node])

    assert path == ['a', 'b', 'd', 'e']
    assert length == 4


def test_a_star_supports_project_graph_objects_with_unit_weights():
    edges = [('a', 'b'), ('b', 'c'), ('a', 'c')]
    G, _ = graph.create_graph(edges, is_directed=True)

    path, length = a_star(
        G,
        G.get_vertex('a'),
        G.get_vertex('c'),
        lambda node: 0,
    )

    assert [node.element() for node in path] == ['a', 'c']
    assert length == 1


def test_a_star_returns_empty_path_for_unreachable_goal():
    road_map = {'a': {'b': 1}, 'b': {}, 'c': {}}

    path, length = a_star(road_map, 'a', 'c', lambda node: 0)

    assert path == []
    assert length == math.inf
