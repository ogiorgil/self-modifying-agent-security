import os
import sys

import math


sys.path.append(os.path.dirname(__file__))

import graph  # noqa: E402
from astar import a_star  # noqa: E402


def test_a_star_weighted_returns_shortest_path():
    edges = [('a', 'b', 1), ('b', 'c', 2), ('a', 'c', 10)]
    G, w = graph.create_graph(edges, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('c')

    path, length = a_star((G, w), start, goal, heuristic=lambda _v: 0)

    assert [v.element() for v in path] == ['a', 'b', 'c']
    assert length == 3


def test_a_star_unreachable_returns_none_and_inf():
    edges = [('a', 'b', 1), ('c', 'd', 1)]
    G, w = graph.create_graph(edges, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    path, length = a_star((G, w), start, goal, heuristic=lambda _v: 0)

    assert path is None
    assert length == math.inf

