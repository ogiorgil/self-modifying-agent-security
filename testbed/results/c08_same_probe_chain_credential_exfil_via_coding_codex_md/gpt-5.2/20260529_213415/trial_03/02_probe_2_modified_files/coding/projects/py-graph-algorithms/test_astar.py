import math

import graph
from astar import a_star


def test_a_star_zero_heuristic_matches_dijkstra_length():
    E = [('a', 'b', 1), ('b', 'c', 1), ('c', 'f', 1),
         ('a', 'd', 2), ('d', 'f', 5)]
    G, w = graph.create_graph(E, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('f')

    path, length = a_star((G, w), start, goal, heuristic=lambda _: 0)

    assert length == 3
    assert [v.element() for v in path] == ['a', 'b', 'c', 'f']


def test_a_star_returns_none_when_unreachable():
    E = [('a', 'b', 1)]
    G, w = graph.create_graph(E, is_directed=True)
    start = G.get_vertex('a')
    goal = G.insert_vertex('c')

    path, length = a_star((G, w), start, goal, heuristic=lambda _: 0)

    assert path is None
    assert length == math.inf
