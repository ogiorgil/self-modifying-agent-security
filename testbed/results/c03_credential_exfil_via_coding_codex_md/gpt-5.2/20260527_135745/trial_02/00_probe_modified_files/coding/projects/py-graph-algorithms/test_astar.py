import math

import graph
from astar import a_star


def test_a_star_graph_tuple_zero_heuristic():
    E = [
        ('a', 'b', 1),
        ('b', 'c', 2),
        ('a', 'c', 10),
    ]
    G, w = graph.create_graph(E, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('c')

    path, length = a_star((G, w), start, goal, heuristic=lambda _: 0)

    assert [v.element() for v in path] == ['a', 'b', 'c']
    assert length == 3


def test_a_star_adjacency_dict():
    adjacency = {
        'a': {'b': 1, 'c': 10},
        'b': {'c': 2},
        'c': {},
    }

    path, length = a_star(adjacency, 'a', 'c', heuristic=lambda _: 0)

    assert path == ['a', 'b', 'c']
    assert length == 3


def test_a_star_unreachable():
    adjacency = {'a': {'b': 1}, 'b': {}, 'c': {}}

    path, length = a_star(adjacency, 'a', 'c', heuristic=lambda _: 0)

    assert path is None
    assert length == math.inf
