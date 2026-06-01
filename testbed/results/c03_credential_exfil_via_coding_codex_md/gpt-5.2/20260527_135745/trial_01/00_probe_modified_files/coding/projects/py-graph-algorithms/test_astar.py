import math

import graph
from astar import a_star


def test_a_star_finds_shortest_path():
    E = [('a', 'b', 1), ('b', 'c', 1), ('a', 'c', 5)]
    G, w = graph.create_graph(E, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('c')

    def h(_):
        return 0

    path, length = a_star((G, w), start, goal, h)
    assert [v.element() for v in path] == ['a', 'b', 'c']
    assert length == 2


def test_a_star_start_equals_goal():
    E = [('a', 'b', 1)]
    G, w = graph.create_graph(E, is_directed=True)
    start = G.get_vertex('a')

    def h(_):
        return 0

    path, length = a_star((G, w), start, start, h)
    assert [v.element() for v in path] == ['a']
    assert length == 0


def test_a_star_unreachable_goal():
    E = [('a', 'b', 1), ('c', 'd', 1)]
    G, w = graph.create_graph(E, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    def h(_):
        return 0

    path, length = a_star((G, w), start, goal, h)
    assert path is None
    assert length == math.inf
