import math
import os
import sys

import graph


# Allow `import astar` when running pytest from repo root.
sys.path.append(os.path.dirname(__file__))
import astar  # noqa: E402


def test_a_star_weighted_finds_shortest_path():
    E = [('a', 'b', 1), ('b', 'c', 1), ('a', 'c', 3)]
    G, w = graph.create_graph(E)
    start = G.get_vertex('a')
    goal = G.get_vertex('c')

    path, length = astar.a_star((G, w), start, goal, heuristic=lambda _: 0)

    assert [v.element() for v in path] == ['a', 'b', 'c']
    assert length == 2


def test_a_star_unweighted_graph_defaults_to_unit_weights():
    E = [('a', 'b'), ('b', 'c'), ('c', 'd')]
    G, _ = graph.create_graph(E)
    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    path, length = astar.a_star(G, start, goal, heuristic=lambda _: 0)

    assert [v.element() for v in path] == ['a', 'b', 'c', 'd']
    assert length == 3


def test_a_star_unreachable_returns_empty_path_and_inf():
    E = [('a', 'b', 1), ('c', 'd', 1)]
    G, w = graph.create_graph(E)
    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    path, length = astar.a_star((G, w), start, goal, heuristic=lambda _: 0)

    assert path == []
    assert length == math.inf
