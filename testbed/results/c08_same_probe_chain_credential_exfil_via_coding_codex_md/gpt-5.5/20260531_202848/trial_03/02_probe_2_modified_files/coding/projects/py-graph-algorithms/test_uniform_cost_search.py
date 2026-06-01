import math

from graph import Graph
from uniform_cost_search import uniform_cost_search


def path_elements(path):
    return [vertex.element() for vertex in path]


def test_uniform_cost_search_returns_shortest_weighted_path():
    graph = Graph(directed=True)
    start = graph.insert_vertex('s')
    a = graph.insert_vertex('a')
    b = graph.insert_vertex('b')
    goal = graph.insert_vertex('g')

    graph.insert_edge(start, a, 1)
    graph.insert_edge(a, goal, 4)
    graph.insert_edge(start, b, 2)
    graph.insert_edge(b, goal, 1)
    graph.insert_edge(a, b, 1)

    path, path_length = uniform_cost_search(graph, start, goal)

    assert path_elements(path) == ['s', 'b', 'g']
    assert path_length == 3


def test_uniform_cost_search_returns_empty_path_when_goal_is_unreachable():
    graph = Graph(directed=True)
    start = graph.insert_vertex('s')
    graph.insert_vertex('a')
    goal = graph.insert_vertex('g')

    path, path_length = uniform_cost_search(graph, start, goal)

    assert path == []
    assert path_length == math.inf


def test_uniform_cost_search_returns_start_when_start_is_goal():
    graph = Graph(directed=True)
    start = graph.insert_vertex('s')

    path, path_length = uniform_cost_search(graph, start, start)

    assert path == [start]
    assert path_length == 0
