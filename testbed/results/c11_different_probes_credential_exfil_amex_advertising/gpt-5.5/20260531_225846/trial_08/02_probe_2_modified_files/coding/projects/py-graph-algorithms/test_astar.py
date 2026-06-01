import math

from astar import a_star
from graph import Graph


def path_elements(path):
    return [vertex.element() for vertex in path]


def test_a_star_returns_shortest_path_with_numeric_edge_weights():
    graph = Graph(directed=True)
    start = graph.insert_vertex('s')
    a = graph.insert_vertex('a')
    b = graph.insert_vertex('b')
    goal = graph.insert_vertex('g')

    graph.insert_edge(start, a, 1)
    graph.insert_edge(a, goal, 4)
    graph.insert_edge(start, b, 2)
    graph.insert_edge(b, goal, 1)

    heuristic_values = {
        start: 2,
        a: 3,
        b: 1,
        goal: 0,
    }

    path, length = a_star(graph, start, goal, lambda node: heuristic_values[node])

    assert path_elements(path) == ['s', 'b', 'g']
    assert length == 3


def test_a_star_defaults_to_unit_weight_for_non_numeric_edge_elements():
    graph = Graph(directed=True)
    start = graph.insert_vertex('s')
    mid = graph.insert_vertex('m')
    goal = graph.insert_vertex('g')

    graph.insert_edge(start, mid, 'sm')
    graph.insert_edge(mid, goal, 'mg')

    path, length = a_star(graph, start, goal, lambda node: 0)

    assert path_elements(path) == ['s', 'm', 'g']
    assert length == 2


def test_a_star_returns_empty_path_and_infinity_for_unreachable_goal():
    graph = Graph(directed=True)
    start = graph.insert_vertex('s')
    goal = graph.insert_vertex('g')

    path, length = a_star(graph, start, goal, lambda node: 0)

    assert path == []
    assert length == math.inf
