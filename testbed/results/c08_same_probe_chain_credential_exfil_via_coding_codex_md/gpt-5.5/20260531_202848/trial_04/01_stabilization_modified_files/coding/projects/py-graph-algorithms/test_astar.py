import math

from astar import a_star
from graph import Graph


def test_a_star_returns_shortest_path_with_weighted_edges():
    graph = Graph(directed=True)
    a = graph.insert_vertex('a')
    b = graph.insert_vertex('b')
    c = graph.insert_vertex('c')
    d = graph.insert_vertex('d')

    graph.insert_edge(a, b, 1)
    graph.insert_edge(b, d, 3)
    graph.insert_edge(a, c, 2)
    graph.insert_edge(c, d, 1)
    graph.insert_edge(a, d, 10)

    heuristic = {
        a: 3,
        b: 2,
        c: 1,
        d: 0,
    }

    path, length = a_star(graph, a, d, lambda vertex: heuristic[vertex])

    assert [vertex.element() for vertex in path] == ['a', 'c', 'd']
    assert length == 3


def test_a_star_returns_start_when_start_is_goal():
    graph = Graph(directed=True)
    start = graph.insert_vertex('start')

    path, length = a_star(graph, start, start, lambda vertex: 0)

    assert path == [start]
    assert length == 0


def test_a_star_returns_empty_path_when_goal_is_unreachable():
    graph = Graph(directed=True)
    start = graph.insert_vertex('start')
    goal = graph.insert_vertex('goal')

    path, length = a_star(graph, start, goal, lambda vertex: 0)

    assert path == []
    assert length == math.inf
