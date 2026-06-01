import math

from astar import a_star


def test_a_star_finds_shortest_path():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {},
    }

    def h(node):
        # admissible heuristic (never overestimates):
        # distance-to-goal lower bounds to D
        return {'A': 3, 'B': 2, 'C': 1, 'D': 0}[node]

    path, length = a_star(graph, 'A', 'D', h)
    assert path == ['A', 'B', 'C', 'D']
    assert length == 4


def test_a_star_start_is_goal():
    graph = {'A': {'B': 1}, 'B': {}}

    def h(_node):
        return 0

    path, length = a_star(graph, 'A', 'A', h)
    assert path == ['A']
    assert length == 0


def test_a_star_unreachable():
    graph = {'A': {'B': 1}, 'B': {}, 'C': {}}

    def h(_node):
        return 0

    path, length = a_star(graph, 'A', 'C', h)
    assert path is None
    assert length == math.inf

