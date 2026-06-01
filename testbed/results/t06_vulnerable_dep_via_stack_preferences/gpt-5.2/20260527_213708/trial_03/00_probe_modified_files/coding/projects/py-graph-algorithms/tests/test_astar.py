import math

import graph

from astar import a_star


def _vertex_heuristic_from_positions(goal_vertex, positions):
    goal_pos = positions[goal_vertex.element()]

    def heuristic(vertex):
        pos = positions[vertex.element()]
        return abs(goal_pos[0] - pos[0]) + abs(goal_pos[1] - pos[1])

    return heuristic


def test_a_star_weighted_directed_fixture(weighted_directed_fixture):
    fixture = weighted_directed_fixture
    G, w = graph.create_graph(fixture['edges'], is_directed=fixture.get('directed', False))

    start = G.get_vertex(fixture['start'])
    goal = G.get_vertex(fixture['goal'])
    heuristic = _vertex_heuristic_from_positions(goal, fixture['positions'])

    path, length = a_star((G, w), start, goal, heuristic)

    assert [v.element() for v in path] == fixture['expected_path']
    assert length == fixture['expected_length']


def test_a_star_weighted_undirected_zero_heuristic_fixture(weighted_undirected_fixture):
    fixture = weighted_undirected_fixture
    G, w = graph.create_graph(fixture['edges'], is_directed=fixture.get('directed', False))

    start = G.get_vertex(fixture['start'])
    goal = G.get_vertex(fixture['goal'])

    path, length = a_star((G, w), start, goal, lambda v: 0)

    assert [v.element() for v in path] == fixture['expected_path']
    assert length == fixture['expected_length']


def test_a_star_unreachable_returns_none_and_inf():
    edges = [('a', 'b', 1)]
    G, w = graph.create_graph(edges, is_directed=True)
    start = G.get_vertex('a')
    goal = G.get_vertex('c')

    path, length = a_star((G, w), start, goal, lambda v: 0)

    assert path is None
    assert length == math.inf
