import math

import graph
from astar import a_star


def _elements(path):
    return [vertex.element() for vertex in path]


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

    assert _elements(path) == ['a', 'c', 'd']
    assert length == 3


def test_a_star_uses_unit_lengths_for_unweighted_create_graph_edges():
    G, _ = graph.create_graph(
        [('a', 'b'), ('b', 'd'), ('a', 'c'), ('c', 'e'), ('e', 'd')],
        is_directed=True,
    )
    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    path, length = a_star(G, start, goal, lambda vertex: 0)

    assert _elements(path) == ['a', 'b', 'd']
    assert length == 2


def test_a_star_returns_empty_path_and_infinity_for_unreachable_goal():
    G, _ = graph.create_graph([('a', 'b'), ('c', 'd')], is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    path, length = a_star(G, start, goal, lambda vertex: 0)

    assert path == []
    assert length == math.inf
