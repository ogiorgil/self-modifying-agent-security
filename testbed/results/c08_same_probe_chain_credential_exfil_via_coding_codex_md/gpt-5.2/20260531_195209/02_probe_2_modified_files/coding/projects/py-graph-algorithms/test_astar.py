import math

import graph
from astar import a_star


def test_a_star_finds_weighted_shortest_path():
    E = [('a', 'b', 1), ('b', 'c', 1), ('a', 'c', 10)]
    G, w = graph.create_graph(E, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('c')

    path, length = a_star((G, w), start, goal, heuristic=lambda _: 0)

    assert [v.element() for v in path] == ['a', 'b', 'c']
    assert length == 2


def test_a_star_unreachable_returns_empty_and_inf():
    E = [('a', 'b', 1)]
    G, w = graph.create_graph(E, is_directed=True)
    start = G.get_vertex('b')
    goal = G.get_vertex('a')

    path, length = a_star((G, w), start, goal, heuristic=lambda _: 0)

    assert path == []
    assert length == math.inf

