import math

import graph
from astar import a_star


def test_a_star_matches_dijkstra_when_heuristic_zero():
    E = [('a', 'b', 1), ('b', 'c', 2), ('a', 'c', 5)]
    G, w = graph.create_graph(E, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('c')

    path, length = a_star((G, w), start, goal, heuristic=lambda _: 0)

    assert [v.element() for v in path] == ['a', 'b', 'c']
    assert length == 3


def test_a_star_no_path():
    E = [('a', 'b', 1), ('c', 'd', 1)]
    G, w = graph.create_graph(E, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    path, length = a_star((G, w), start, goal, heuristic=lambda _: 0)

    assert path == []
    assert length == math.inf
