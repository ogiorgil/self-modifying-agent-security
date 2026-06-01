import math

import graph
from astar import a_star


def test_a_star_finds_shortest_path_for_graph_with_weight_mapping():
    edges = [('s', 'a', 1), ('s', 'b', 4), ('a', 'c', 2),
             ('b', 'c', 1), ('b', 'g', 6), ('c', 'g', 2)]
    G, weight_mapping = graph.create_graph(edges, is_directed=True)
    heuristic_estimates = {'s': 5, 'a': 3, 'b': 2, 'c': 1, 'g': 0}

    start = G.get_vertex('s')
    goal = G.get_vertex('g')
    path, path_length = a_star((G, weight_mapping), start, goal,
                               lambda vertex: heuristic_estimates[vertex.element()])

    assert [vertex.element() for vertex in path] == ['s', 'a', 'c', 'g']
    assert path_length == 5


def test_a_star_returns_empty_path_for_unreachable_goal():
    adjacency = {
        's': {'a': 1},
        'a': {},
        'g': {},
    }

    path, path_length = a_star(adjacency, 's', 'g', lambda vertex: 0)

    assert path == []
    assert path_length == math.inf
