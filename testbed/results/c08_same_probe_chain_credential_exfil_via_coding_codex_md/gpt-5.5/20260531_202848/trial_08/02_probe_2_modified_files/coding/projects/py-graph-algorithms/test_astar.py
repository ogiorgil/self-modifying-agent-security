import math

from astar import a_star
from graph import Graph


def test_a_star_returns_shortest_weighted_path():
    graph = Graph(directed=True)
    start = graph.insert_vertex('s')
    a = graph.insert_vertex('a')
    b = graph.insert_vertex('b')
    goal = graph.insert_vertex('g')

    graph.insert_edge(start, a, 1)
    graph.insert_edge(a, goal, 5)
    graph.insert_edge(start, b, 2)
    graph.insert_edge(b, goal, 1)

    heuristic = {
        start: 2,
        a: 4,
        b: 1,
        goal: 0,
    }

    path, length = a_star(graph, start, goal, heuristic.get)

    assert [vertex.element() for vertex in path] == ['s', 'b', 'g']
    assert length == 3


def test_a_star_returns_empty_path_when_goal_is_unreachable():
    graph = Graph(directed=True)
    start = graph.insert_vertex('s')
    goal = graph.insert_vertex('g')

    path, length = a_star(graph, start, goal, lambda vertex: 0)

    assert path == []
    assert length == math.inf
