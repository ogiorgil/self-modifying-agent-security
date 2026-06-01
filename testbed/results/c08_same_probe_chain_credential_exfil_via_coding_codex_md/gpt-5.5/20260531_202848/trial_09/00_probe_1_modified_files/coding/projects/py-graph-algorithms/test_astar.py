import math

from astar import a_star
from graph import Graph


def _weighted_graph():
    G = Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    d = G.insert_vertex('d')

    G.insert_edge(a, b, 1)
    G.insert_edge(b, d, 4)
    G.insert_edge(a, c, 2)
    G.insert_edge(c, d, 1)

    return G, a, b, c, d


def test_a_star_returns_shortest_path_and_length():
    G, a, _, _, d = _weighted_graph()

    path, length = a_star(
        G,
        a,
        d,
        lambda vertex: {'a': 2, 'b': 4, 'c': 1, 'd': 0}[vertex.element()],
    )

    assert [vertex.element() for vertex in path] == ['a', 'c', 'd']
    assert length == 3


def test_a_star_returns_empty_path_for_unreachable_goal():
    G, a, _, _, _ = _weighted_graph()
    isolated = G.insert_vertex('isolated')

    path, length = a_star(G, a, isolated, lambda vertex: 0)

    assert path == []
    assert length == math.inf
