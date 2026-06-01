import math

from astar import a_star


def test_a_star_finds_shortest_path_weighted(load_graph_fixture):
    data, G, vertices = load_graph_fixture('weighted_line.yaml')

    h_map = data['heuristic']
    heuristic = lambda v: h_map[v.element()]

    start = vertices[data['start']]
    goal = vertices[data['goal']]
    path, length = a_star(G, start, goal, heuristic)

    assert [v.element() for v in path] == data['expected_path']
    assert length == data['expected_length']


def test_a_star_prefers_lower_cost_over_fewer_edges(load_graph_fixture):
    data, G, vertices = load_graph_fixture('weighted_alt_routes.yaml')

    h_map = data['heuristic']
    heuristic = lambda v: h_map[v.element()]

    start = vertices[data['start']]
    goal = vertices[data['goal']]
    path, length = a_star(G, start, goal, heuristic)

    assert [v.element() for v in path] == data['expected_path']
    assert length == data['expected_length']


def test_a_star_returns_empty_path_when_unreachable(load_graph_fixture):
    data, G, vertices = load_graph_fixture('unreachable.yaml')

    h_map = data['heuristic']
    heuristic = lambda v: h_map[v.element()]

    start = vertices[data['start']]
    goal = vertices[data['goal']]
    path, length = a_star(G, start, goal, heuristic)

    assert path == []
    assert length == math.inf
