import math

import graph
from astar import a_star


def test_a_star_finds_shortest_path_for_adjacency_mapping():
    adjacency = {
        's': {'a': 1, 'b': 5},
        'a': {'b': 2, 'c': 4},
        'b': {'c': 1},
        'c': {},
    }

    path, length = a_star(adjacency, 's', 'c', lambda node: 0)

    assert path == ['s', 'a', 'b', 'c']
    assert length == 4


def test_a_star_supports_project_graph_with_unit_weights():
    edges = [('s', 'a'), ('s', 'b'), ('a', 'c'), ('b', 'd'), ('c', 'g')]
    G, _ = graph.create_graph(edges, is_directed=True)
    start = G.get_vertex('s')
    goal = G.get_vertex('g')

    path, length = a_star(G, start, goal, lambda vertex: 0)

    assert [vertex.element() for vertex in path] == ['s', 'a', 'c', 'g']
    assert length == 3


def test_a_star_supports_numeric_edge_elements_on_project_graph():
    G = graph.Graph(directed=True)
    start = G.insert_vertex('s')
    middle = G.insert_vertex('a')
    goal = G.insert_vertex('g')
    G.insert_edge(start, goal, 5)
    G.insert_edge(start, middle, 2)
    G.insert_edge(middle, goal, 1)

    path, length = a_star(G, start, goal, lambda vertex: 0)

    assert [vertex.element() for vertex in path] == ['s', 'a', 'g']
    assert length == 3


def test_a_star_returns_empty_path_for_unreachable_goal():
    adjacency = {
        's': [('a', 1)],
        'a': [],
        'g': [],
    }

    path, length = a_star(adjacency, 's', 'g', lambda node: 0)

    assert path == []
    assert length == math.inf
