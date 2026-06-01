import math

import graph
from astar import a_star


def test_a_star_returns_shortest_path_for_adjacency_mapping():
    graph_map = {
        'a': {'b': 1, 'c': 4},
        'b': {'c': 2, 'd': 5},
        'c': {'d': 1},
        'd': {},
    }

    heuristic = {'a': 3, 'b': 2, 'c': 1, 'd': 0}

    path, length = a_star(graph_map, 'a', 'd', heuristic.get)

    assert path == ['a', 'b', 'c', 'd']
    assert length == 4


def test_a_star_supports_project_graph_with_numeric_edge_elements():
    graph_obj = graph.Graph(directed=True)
    a = graph_obj.insert_vertex('a')
    b = graph_obj.insert_vertex('b')
    c = graph_obj.insert_vertex('c')
    d = graph_obj.insert_vertex('d')
    graph_obj.insert_edge(a, b, 1)
    graph_obj.insert_edge(a, c, 4)
    graph_obj.insert_edge(b, c, 2)
    graph_obj.insert_edge(b, d, 5)
    graph_obj.insert_edge(c, d, 1)

    heuristic = {a: 3, b: 2, c: 1, d: 0}

    path, length = a_star(graph_obj, a, d, heuristic.get)

    assert [node.element() for node in path] == ['a', 'b', 'c', 'd']
    assert length == 4


def test_a_star_returns_empty_path_for_unreachable_goal():
    graph_map = {
        'a': {'b': 1},
        'b': {},
        'c': {},
    }

    path, length = a_star(graph_map, 'a', 'c', lambda node: 0)

    assert path == []
    assert length == math.inf
