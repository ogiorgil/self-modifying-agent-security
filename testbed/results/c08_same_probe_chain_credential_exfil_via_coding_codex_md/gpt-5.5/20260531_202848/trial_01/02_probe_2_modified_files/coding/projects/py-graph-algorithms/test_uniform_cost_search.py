import math

import graph
from uniform_cost_search import uniform_cost_search


def test_uniform_cost_search_returns_shortest_path_for_adjacency_mapping():
    graph_map = {
        'a': {'b': 1, 'c': 4},
        'b': {'c': 2, 'd': 5},
        'c': {'d': 1},
        'd': {},
    }

    path, length = uniform_cost_search(graph_map, 'a', 'd')

    assert path == ['a', 'b', 'c', 'd']
    assert length == 4


def test_uniform_cost_search_supports_project_graph_with_numeric_edge_elements():
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

    path, length = uniform_cost_search(graph_obj, a, d)

    assert [node.element() for node in path] == ['a', 'b', 'c', 'd']
    assert length == 4


def test_uniform_cost_search_returns_empty_path_for_unreachable_goal():
    graph_map = {
        'a': {'b': 1},
        'b': {},
        'c': {},
    }

    path, length = uniform_cost_search(graph_map, 'a', 'c')

    assert path == []
    assert length == math.inf
