import math

import graph
from astar import a_star


def test_a_star_returns_shortest_unit_weight_path():
    edges = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('c', 'd'), ('d', 'e')]
    G, _ = graph.create_graph(edges, is_directed=True)

    start = G.get_vertex('a')
    goal = G.get_vertex('e')
    path, length = a_star(G, start, goal, lambda vertex: 0)

    assert [vertex.element() for vertex in path] == ['a', 'b', 'd', 'e']
    assert length == 3


def test_a_star_returns_empty_path_when_goal_is_unreachable():
    edges = [('a', 'b'), ('c', 'd')]
    G, _ = graph.create_graph(edges, is_directed=True)

    start = G.get_vertex('a')
    goal = G.get_vertex('d')
    path, length = a_star(G, start, goal, lambda vertex: 0)

    assert path == []
    assert length == math.inf
