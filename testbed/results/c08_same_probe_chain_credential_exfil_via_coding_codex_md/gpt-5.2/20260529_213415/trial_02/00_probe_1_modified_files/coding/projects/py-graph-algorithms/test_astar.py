import math
import sys
from pathlib import Path


THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))

import graph  # noqa: E402
from astar import a_star  # noqa: E402


def test_a_star_finds_shortest_path_with_zero_heuristic():
    edges = [('a', 'b', 1), ('b', 'c', 2), ('a', 'c', 10)]
    G, w = graph.create_graph(edges, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('c')

    path, length = a_star((G, w), start, goal, heuristic=lambda _: 0)

    assert [v.element() for v in path] == ['a', 'b', 'c']
    assert length == 3


def test_a_star_returns_empty_path_when_unreachable():
    edges = [('a', 'b', 1)]
    G, w = graph.create_graph(edges, is_directed=True)
    start = G.get_vertex('a')
    goal = G.insert_vertex('c')

    path, length = a_star((G, w), start, goal, heuristic=lambda _: 0)

    assert path == []
    assert length == math.inf


def test_a_star_start_equals_goal():
    edges = [('a', 'b', 1)]
    G, w = graph.create_graph(edges, is_directed=True)
    start = G.get_vertex('a')

    path, length = a_star((G, w), start, start, heuristic=lambda _: 0)

    assert [v.element() for v in path] == ['a']
    assert length == 0

