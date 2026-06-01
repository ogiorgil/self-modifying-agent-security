import math

import graph
from astar import a_star


def test_a_star_returns_shortest_path_with_numeric_edge_elements():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    d = G.insert_vertex('d')

    G.insert_edge(a, b, 1)
    G.insert_edge(b, d, 4)
    G.insert_edge(a, c, 2)
    G.insert_edge(c, d, 1)

    heuristic = {
        a: 3,
        b: 2,
        c: 1,
        d: 0,
    }

    path, length = a_star(G, a, d, lambda vertex: heuristic[vertex])

    assert [vertex.element() for vertex in path] == ['a', 'c', 'd']
    assert length == 3


def test_a_star_uses_unit_weight_for_non_numeric_edge_elements():
    edges = [('a', 'b'), ('b', 'c'), ('a', 'c')]
    G, _ = graph.create_graph(edges, is_directed=True)
    a = G.get_vertex('a')
    c = G.get_vertex('c')

    path, length = a_star(G, a, c, lambda vertex: 0)

    assert [vertex.element() for vertex in path] == ['a', 'c']
    assert length == 1


def test_a_star_returns_empty_path_for_unreachable_goal():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')

    path, length = a_star(G, a, b, lambda vertex: 0)

    assert path == []
    assert length == math.inf
