import math

import graph
from astar import a_star


def test_a_star_finds_shortest_weighted_path():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    d = G.insert_vertex('d')

    G.insert_edge(a, b, 1)
    G.insert_edge(a, c, 5)
    G.insert_edge(b, c, 1)
    G.insert_edge(c, d, 1)
    G.insert_edge(b, d, 4)

    estimates = {
        a: 3,
        b: 2,
        c: 1,
        d: 0,
    }

    path, length = a_star(G, a, d, lambda vertex: estimates[vertex])

    assert [vertex.element() for vertex in path] == ['a', 'b', 'c', 'd']
    assert length == 3


def test_a_star_defaults_to_unit_weight_for_unweighted_edges():
    G, _ = graph.create_graph([('a', 'b'), ('b', 'c'), ('a', 'c')],
                              is_directed=True)
    a = G.get_vertex('a')
    c = G.get_vertex('c')

    path, length = a_star(G, a, c, lambda vertex: 0)

    assert [vertex.element() for vertex in path] == ['a', 'c']
    assert length == 1


def test_a_star_returns_empty_path_when_goal_is_unreachable():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')

    path, length = a_star(G, a, b, lambda vertex: 0)

    assert path == []
    assert length == math.inf
