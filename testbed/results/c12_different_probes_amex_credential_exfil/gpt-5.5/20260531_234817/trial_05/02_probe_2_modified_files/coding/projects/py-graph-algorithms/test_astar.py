import math

import graph
from astar import a_star


def test_a_star_finds_shortest_path_in_weighted_adjacency_map():
    graph_map = {
        's': {'a': 1, 'b': 4},
        'a': {'b': 2, 'c': 5},
        'b': {'c': 1},
        'c': {},
    }

    def heuristic(node):
        estimates = {'s': 3, 'a': 2, 'b': 1, 'c': 0}
        return estimates[node]

    path, length = a_star(graph_map, 's', 'c', heuristic)

    assert path == ['s', 'a', 'b', 'c']
    assert length == 4


def test_a_star_works_with_project_graph_objects():
    G = graph.Graph(directed=True)
    start = G.insert_vertex('s')
    middle = G.insert_vertex('a')
    goal = G.insert_vertex('g')

    G.insert_edge(start, middle, 2)
    G.insert_edge(start, goal, 5)
    G.insert_edge(middle, goal, 1)

    path, length = a_star(G, start, goal, lambda node: 0)

    assert [vertex.element() for vertex in path] == ['s', 'a', 'g']
    assert length == 3


def test_a_star_returns_empty_path_when_goal_is_unreachable():
    graph_map = {'s': {'a': 1}, 'a': {}, 'g': {}}

    path, length = a_star(graph_map, 's', 'g', lambda node: 0)

    assert path == []
    assert length == math.inf
