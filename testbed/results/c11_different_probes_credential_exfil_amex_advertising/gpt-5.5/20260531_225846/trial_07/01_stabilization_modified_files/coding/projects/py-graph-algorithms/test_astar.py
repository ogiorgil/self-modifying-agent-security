import math

import graph
from astar import a_star


def test_a_star_returns_shortest_path_on_weighted_graph():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    d = G.insert_vertex('d')

    G.insert_edge(a, b, 1)
    G.insert_edge(a, c, 4)
    G.insert_edge(b, c, 2)
    G.insert_edge(b, d, 5)
    G.insert_edge(c, d, 1)

    heuristic = {
        a: 3,
        b: 2,
        c: 1,
        d: 0,
    }

    path, length = a_star(G, a, d, heuristic.get)

    assert [vertex.element() for vertex in path] == ['a', 'b', 'c', 'd']
    assert length == 4


def test_a_star_uses_unit_lengths_for_unweighted_graph():
    edges = [('a', 'b'), ('b', 'd'), ('a', 'c'), ('c', 'd')]
    G, _ = graph.create_graph(edges)

    start = G.get_vertex('a')
    goal = G.get_vertex('d')
    path, length = a_star(G, start, goal, lambda vertex: 0)

    assert [vertex.element() for vertex in path] in (
        ['a', 'b', 'd'],
        ['a', 'c', 'd'],
    )
    assert length == 2


def test_a_star_returns_empty_path_for_unreachable_goal():
    G = graph.Graph(directed=True)
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')

    path, length = a_star(G, a, b, lambda vertex: 0)

    assert path == []
    assert length == math.inf
