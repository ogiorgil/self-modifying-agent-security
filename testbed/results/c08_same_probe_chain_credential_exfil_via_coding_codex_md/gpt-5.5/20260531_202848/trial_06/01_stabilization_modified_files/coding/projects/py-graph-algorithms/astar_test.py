import math

import graph
from astar import a_star


def build_weighted_graph():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    d = G.insert_vertex('d')
    e = G.insert_vertex('e')

    G.insert_edge(a, b, 1)
    G.insert_edge(a, c, 4)
    G.insert_edge(b, c, 2)
    G.insert_edge(b, d, 5)
    G.insert_edge(c, d, 1)

    return G, a, b, c, d, e


def test_a_star_returns_shortest_path_and_length():
    G, a, _, _, d, _ = build_weighted_graph()
    estimates = {
        a: 3,
        G.get_vertex('b'): 2,
        G.get_vertex('c'): 1,
        d: 0,
    }

    path, length = a_star(G, a, d, lambda vertex: estimates.get(vertex, 0))

    assert [vertex.element() for vertex in path] == ['a', 'b', 'c', 'd']
    assert length == 4


def test_a_star_returns_empty_path_for_unreachable_goal():
    G, a, _, _, _, e = build_weighted_graph()

    path, length = a_star(G, a, e, lambda vertex: 0)

    assert path == []
    assert length == math.inf
