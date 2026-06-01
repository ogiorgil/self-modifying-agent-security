import math

import graph
from uniform_cost_search import uniform_cost_search


def test_uniform_cost_search_returns_shortest_weighted_path():
    G = graph.Graph(directed=True)
    start = G.insert_vertex('start')
    middle = G.insert_vertex('middle')
    detour = G.insert_vertex('detour')
    goal = G.insert_vertex('goal')

    G.insert_edge(start, middle, 2)
    G.insert_edge(middle, goal, 2)
    G.insert_edge(start, detour, 1)
    G.insert_edge(detour, goal, 10)

    path, length = uniform_cost_search(G, start, goal)

    assert [vertex.element() for vertex in path] == ['start', 'middle', 'goal']
    assert length == 4


def test_uniform_cost_search_returns_start_when_start_is_goal():
    G, _ = graph.create_graph([('a', 'b')], is_directed=True)
    start = G.get_vertex('a')

    path, length = uniform_cost_search(G, start, start)

    assert [vertex.element() for vertex in path] == ['a']
    assert length == 0


def test_uniform_cost_search_returns_infinity_when_goal_is_unreachable():
    G, _ = graph.create_graph([('a', 'b'), ('c', 'd')], is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    path, length = uniform_cost_search(G, start, goal)

    assert path == []
    assert length == math.inf


def test_uniform_cost_search_rejects_negative_weights():
    G = graph.Graph(directed=True)
    start = G.insert_vertex('start')
    goal = G.insert_vertex('goal')
    G.insert_edge(start, goal, -1)

    try:
        uniform_cost_search(G, start, goal)
    except ValueError as exc:
        assert str(exc) == 'Uniform-cost search does not support negative edge weights'
    else:
        raise AssertionError('negative edge weights should fail')
