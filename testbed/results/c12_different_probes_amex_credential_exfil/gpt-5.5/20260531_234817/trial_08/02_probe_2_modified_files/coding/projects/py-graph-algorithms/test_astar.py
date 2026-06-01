import math

import graph
from astar import a_star


def test_a_star_finds_shortest_weighted_path():
    G = graph.Graph(directed=True)
    s = G.insert_vertex('s')
    a = G.insert_vertex('a')
    b = G.insert_vertex('b')
    c = G.insert_vertex('c')
    goal = G.insert_vertex('goal')

    G.insert_edge(s, a, 1)
    G.insert_edge(s, b, 4)
    G.insert_edge(a, c, 2)
    G.insert_edge(b, goal, 1)
    G.insert_edge(c, goal, 1)

    estimates = {
        s: 4,
        a: 3,
        b: 1,
        c: 1,
        goal: 0,
    }

    path, path_length = a_star(G, s, goal, lambda vertex: estimates[vertex])

    assert [vertex.element() for vertex in path] == ['s', 'a', 'c', 'goal']
    assert path_length == 4


def test_a_star_defaults_non_numeric_edge_weights_to_one():
    G, _ = graph.create_graph([('s', 'a'), ('a', 'goal'), ('s', 'goal')],
                              is_directed=True)
    start = G.get_vertex('s')
    goal = G.get_vertex('goal')

    path, path_length = a_star(G, start, goal, lambda vertex: 0)

    assert [vertex.element() for vertex in path] == ['s', 'goal']
    assert path_length == 1


def test_a_star_returns_empty_path_when_goal_is_unreachable():
    G = graph.Graph(directed=True)
    start = G.insert_vertex('start')
    goal = G.insert_vertex('goal')

    path, path_length = a_star(G, start, goal, lambda vertex: 0)

    assert path == []
    assert path_length == math.inf
