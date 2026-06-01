import math

import graph
from astar import a_star


def test_a_star_weighted_graph_finds_shortest_path():
    # a -> b (1), b -> d (1) is shorter than a -> c (10), c -> d (1)
    edges = [('a', 'b', 1), ('b', 'd', 1), ('a', 'c', 10), ('c', 'd', 1)]
    G, w = graph.create_graph(edges, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    # Admissible heuristic for this tiny test: 0 everywhere => reduces to Dijkstra
    path, length = a_star((G, w), start, goal, heuristic=lambda _v: 0)

    assert length == 2
    assert [v.element() for v in path] == ['a', 'b', 'd']


def test_a_star_unreachable_returns_empty_and_inf():
    edges = [('a', 'b', 1), ('c', 'd', 1)]
    G, w = graph.create_graph(edges, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    path, length = a_star((G, w), start, goal, heuristic=lambda _v: 0)

    assert path == []
    assert length == math.inf
