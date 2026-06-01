import math

import graph
from astar import a_star

from conftest import load_yaml_fixture


def _build_graph_from_fixture(fixture):
    edges = fixture['edges']
    directed = bool(fixture.get('directed', False))
    G, w = graph.create_graph(edges, is_directed=directed)
    return G, w


def _make_heuristic(fixture):
    heuristic_mapping = fixture.get('heuristic', {}) or {}

    def h(v):
        return heuristic_mapping.get(v.element(), 0)

    return h


def test_a_star_weighted_triangle():
    fixture = load_yaml_fixture('weighted_triangle.yaml')
    G, w = _build_graph_from_fixture(fixture)
    start = G.get_vertex(fixture['start'])
    goal = G.get_vertex(fixture['goal'])

    path, length = a_star((G, w), start, goal, _make_heuristic(fixture))
    assert [v.element() for v in path] == fixture['expected']['path']
    assert length == fixture['expected']['length']


def test_a_star_unweighted_prefers_direct_edge():
    fixture = load_yaml_fixture('unweighted_triangle.yaml')
    G, w = _build_graph_from_fixture(fixture)
    start = G.get_vertex(fixture['start'])
    goal = G.get_vertex(fixture['goal'])

    path, length = a_star(G, start, goal, _make_heuristic(fixture))
    assert [v.element() for v in path] == fixture['expected']['path']
    assert length == fixture['expected']['length']


def test_a_star_returns_empty_on_unreachable_goal():
    fixture = load_yaml_fixture('unreachable.yaml')
    G, w = _build_graph_from_fixture(fixture)
    start = G.get_vertex(fixture['start'])
    goal = G.get_vertex(fixture['goal'])

    path, length = a_star((G, w), start, goal, _make_heuristic(fixture))
    assert path == []
    assert length == math.inf


def test_a_star_start_equals_goal():
    fixture = load_yaml_fixture('start_equals_goal.yaml')
    G, w = _build_graph_from_fixture(fixture)
    start = G.get_vertex(fixture['start'])
    goal = G.get_vertex(fixture['goal'])

    path, length = a_star((G, w), start, goal, _make_heuristic(fixture))
    assert [v.element() for v in path] == fixture['expected']['path']
    assert length == fixture['expected']['length']

