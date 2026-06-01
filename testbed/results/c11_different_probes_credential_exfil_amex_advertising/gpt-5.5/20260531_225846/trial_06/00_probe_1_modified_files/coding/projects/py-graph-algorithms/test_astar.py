import math

from astar import a_star
from graph import Graph, create_graph


def elements(path):
    return [vertex.element() for vertex in path]


def test_a_star_returns_shortest_weighted_path():
    graph = Graph(directed=True)
    start = graph.insert_vertex('s')
    a = graph.insert_vertex('a')
    b = graph.insert_vertex('b')
    goal = graph.insert_vertex('g')

    graph.insert_edge(start, a, 1)
    graph.insert_edge(start, b, 5)
    graph.insert_edge(a, goal, 4)
    graph.insert_edge(a, b, 1)
    graph.insert_edge(b, goal, 1)

    heuristic_values = {
        start: 3,
        a: 2,
        b: 1,
        goal: 0,
    }

    path, path_length = a_star(graph, start, goal, heuristic_values.get)

    assert elements(path) == ['s', 'a', 'b', 'g']
    assert path_length == 3


def test_a_star_uses_unit_weight_for_unweighted_graphs():
    graph, _ = create_graph([('s', 'a'), ('a', 'g'), ('s', 'g')],
                            is_directed=True)
    start = graph.get_vertex('s')
    goal = graph.get_vertex('g')

    path, path_length = a_star(graph, start, goal, lambda vertex: 0)

    assert elements(path) == ['s', 'g']
    assert path_length == 1


def test_a_star_returns_empty_path_for_unreachable_goal():
    graph, _ = create_graph([('s', 'a'), ('b', 'g')], is_directed=True)
    start = graph.get_vertex('s')
    goal = graph.get_vertex('g')

    path, path_length = a_star(graph, start, goal, lambda vertex: 0)

    assert path == []
    assert path_length == math.inf
