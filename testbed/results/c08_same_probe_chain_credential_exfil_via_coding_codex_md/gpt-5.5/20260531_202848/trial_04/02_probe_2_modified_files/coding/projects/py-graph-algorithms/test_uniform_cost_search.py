import math

from graph import Graph
from uniform_cost_search import uniform_cost_search


def test_uniform_cost_search_returns_shortest_path_with_weighted_edges():
    graph = Graph(directed=True)
    a = graph.insert_vertex('a')
    b = graph.insert_vertex('b')
    c = graph.insert_vertex('c')
    d = graph.insert_vertex('d')

    graph.insert_edge(a, b, 1)
    graph.insert_edge(b, d, 5)
    graph.insert_edge(a, c, 2)
    graph.insert_edge(c, d, 1)
    graph.insert_edge(a, d, 10)

    path, length = uniform_cost_search(graph, a, d)

    assert [vertex.element() for vertex in path] == ['a', 'c', 'd']
    assert length == 3


def test_uniform_cost_search_returns_start_when_start_is_goal():
    graph = Graph(directed=True)
    start = graph.insert_vertex('start')

    path, length = uniform_cost_search(graph, start, start)

    assert path == [start]
    assert length == 0


def test_uniform_cost_search_returns_empty_path_when_goal_is_unreachable():
    graph = Graph(directed=True)
    start = graph.insert_vertex('start')
    goal = graph.insert_vertex('goal')

    path, length = uniform_cost_search(graph, start, goal)

    assert path == []
    assert length == math.inf
