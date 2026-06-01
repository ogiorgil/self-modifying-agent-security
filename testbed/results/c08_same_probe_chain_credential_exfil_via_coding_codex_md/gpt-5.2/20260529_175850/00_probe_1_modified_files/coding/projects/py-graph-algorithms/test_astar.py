import math

import graph
from astar import a_star


def test_a_star_finds_shortest_path_with_zero_heuristic():
    E = [('a', 'b', 1), ('b', 'c', 1), ('a', 'c', 3)]
    G, w = graph.create_graph(E, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('c')

    path, length = a_star((G, w), start, goal, heuristic=lambda v: 0)

    assert length == 2
    assert [v.element() for v in path] == ['a', 'b', 'c']


def test_a_star_returns_inf_when_no_path_exists():
    E = [('a', 'b', 1), ('c', 'd', 1)]
    G, w = graph.create_graph(E, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    path, length = a_star((G, w), start, goal, heuristic=lambda v: 0)

    assert path is None
    assert math.isinf(length)

