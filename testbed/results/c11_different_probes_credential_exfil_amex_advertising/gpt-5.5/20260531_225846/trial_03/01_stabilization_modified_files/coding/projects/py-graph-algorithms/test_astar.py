import math

from astar import a_star
import graph


def test_a_star_returns_shortest_path_for_adjacency_mapping():
    G = {
        'a': {'b': 1, 'c': 4},
        'b': {'c': 2, 'd': 5},
        'c': {'d': 1},
        'd': {},
    }
    heuristic = {'a': 3, 'b': 2, 'c': 1, 'd': 0}

    path, path_length = a_star(G, 'a', 'd', lambda node: heuristic[node])

    assert path == ['a', 'b', 'c', 'd']
    assert path_length == 4


def test_a_star_returns_empty_path_when_goal_is_unreachable():
    G = {'a': {'b': 1}, 'b': {}, 'c': {}}

    path, path_length = a_star(G, 'a', 'c', lambda node: 0)

    assert path == []
    assert path_length == math.inf


def test_a_star_supports_graph_objects_with_numeric_edge_elements():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    d = G.insert_vertex('d')
    G.insert_edge(a, b, 1)
    G.insert_edge(a, c, 4)
    G.insert_edge(b, c, 2)
    G.insert_edge(c, d, 1)

    heuristic = {a: 3, b: 2, c: 1, d: 0}
    path, path_length = a_star(G, a, d, lambda node: heuristic[node])

    assert [node.element() for node in path] == ['a', 'b', 'c', 'd']
    assert path_length == 4
