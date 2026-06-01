import math

import graph
from astar import a_star


def test_a_star_returns_shortest_weighted_path():
    G = graph.Graph(directed=True)
    start = G.insert_vertex('start')
    middle = G.insert_vertex('middle')
    detour = G.insert_vertex('detour')
    goal = G.insert_vertex('goal')

    G.insert_edge(start, middle, 2)
    G.insert_edge(middle, goal, 2)
    G.insert_edge(start, detour, 1)
    G.insert_edge(detour, goal, 10)

    estimates = {
        start: 4,
        middle: 2,
        detour: 10,
        goal: 0,
    }

    path, length = a_star(G, start, goal, lambda vertex: estimates[vertex])

    assert [vertex.element() for vertex in path] == ['start', 'middle', 'goal']
    assert length == 4


def test_a_star_returns_start_when_start_is_goal():
    G, _ = graph.create_graph([('a', 'b')], is_directed=True)
    start = G.get_vertex('a')

    path, length = a_star(G, start, start, lambda vertex: 0)

    assert [vertex.element() for vertex in path] == ['a']
    assert length == 0


def test_a_star_returns_infinity_when_goal_is_unreachable():
    G, _ = graph.create_graph([('a', 'b'), ('c', 'd')], is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    path, length = a_star(G, start, goal, lambda vertex: 0)

    assert path == []
    assert length == math.inf
