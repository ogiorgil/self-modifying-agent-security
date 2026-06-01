import math

import graph
from astar import a_star


def test_a_star_finds_weighted_shortest_path():
    G = graph.Graph(directed=True)
    start = G.insert_vertex('s')
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    goal = G.insert_vertex('g')

    G.insert_edge(start, a, 1)
    G.insert_edge(a, goal, 5)
    G.insert_edge(start, b, 2)
    G.insert_edge(b, goal, 1)

    heuristic = {
        start: 2,
        a: 5,
        b: 1,
        goal: 0,
    }

    path, length = a_star(G, start, goal, lambda vertex: heuristic[vertex])

    assert [vertex.element() for vertex in path] == ['s', 'b', 'g']
    assert length == 3


def test_a_star_uses_unit_weights_for_unweighted_graph():
    G, _ = graph.create_graph([('s', 'a'), ('a', 'g'), ('s', 'g')], True)
    start = G.get_vertex('s')
    goal = G.get_vertex('g')

    path, length = a_star(G, start, goal, lambda vertex: 0)

    assert [vertex.element() for vertex in path] == ['s', 'g']
    assert length == 1


def test_a_star_returns_empty_path_for_unreachable_goal():
    G = graph.Graph(directed=True)
    start = G.insert_vertex('s')
    goal = G.insert_vertex('g')

    path, length = a_star(G, start, goal, lambda vertex: 0)

    assert path == []
    assert length == math.inf
