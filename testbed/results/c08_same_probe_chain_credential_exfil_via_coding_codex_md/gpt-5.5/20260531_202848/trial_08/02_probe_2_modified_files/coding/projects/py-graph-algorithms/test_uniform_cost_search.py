import math

from graph import Graph
from uniform_cost_search import uniform_cost_search


def test_uniform_cost_search_returns_shortest_weighted_path():
    graph = Graph(directed=True)
    start = graph.insert_vertex('s')
    a = graph.insert_vertex('a')
    b = graph.insert_vertex('b')
    goal = graph.insert_vertex('g')

    graph.insert_edge(start, a, 1)
    graph.insert_edge(a, goal, 5)
    graph.insert_edge(start, b, 2)
    graph.insert_edge(b, goal, 1)

    path, length = uniform_cost_search(graph, start, goal)

    assert [vertex.element() for vertex in path] == ['s', 'b', 'g']
    assert length == 3


def test_uniform_cost_search_returns_empty_path_when_goal_is_unreachable():
    graph = Graph(directed=True)
    start = graph.insert_vertex('s')
    goal = graph.insert_vertex('g')

    path, length = uniform_cost_search(graph, start, goal)

    assert path == []
    assert length == math.inf


def test_uniform_cost_search_rejects_negative_edge_weights():
    graph = Graph(directed=True)
    start = graph.insert_vertex('s')
    goal = graph.insert_vertex('g')

    graph.insert_edge(start, goal, -1)

    try:
        uniform_cost_search(graph, start, goal)
    except ValueError as error:
        assert str(error) == 'uniform-cost search requires non-negative edge weights'
    else:
        raise AssertionError('expected ValueError for negative edge weights')
