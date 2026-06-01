import math

from astar import a_star


def test_a_star_finds_shortest_path_dict_of_dict():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {},
    }

    path, length = a_star(graph, 'A', 'D', heuristic=lambda _: 0)
    assert path == ['A', 'B', 'C', 'D']
    assert length == 4


def test_a_star_finds_shortest_path_list_of_pairs():
    graph = {
        0: [(1, 2), (2, 5)],
        1: [(2, 1), (3, 7)],
        2: [(3, 1)],
        3: [],
    }

    path, length = a_star(graph, 0, 3, heuristic=lambda _: 0)
    assert path == [0, 1, 2, 3]
    assert length == 4


def test_a_star_unreachable():
    graph = {
        'A': {'B': 1},
        'B': {},
        'C': {'D': 1},
        'D': {},
    }

    path, length = a_star(graph, 'A', 'D', heuristic=lambda _: 0)
    assert path is None
    assert length == math.inf


def test_a_star_start_is_goal():
    graph = {'A': {'B': 1}, 'B': {}}
    path, length = a_star(graph, 'A', 'A', heuristic=lambda _: 123)
    assert path == ['A']
    assert length == 0
