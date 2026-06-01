import math

import graph
from astar import a_star

from fixture_loader import load_yaml_fixture


def _build_graph_from_fixture(fx):
    edges = [tuple(edge) for edge in fx["edges"]]
    is_directed = bool(fx.get("directed", False))
    return graph.create_graph(edges, is_directed=is_directed)


def _make_manhattan_heuristic(coords_by_element, goal_element):
    gx, gy = coords_by_element[goal_element]

    def h(vertex):
        x, y = coords_by_element[vertex.element()]
        return abs(gx - x) + abs(gy - y)

    return h


def test_a_star_finds_shortest_path_weighted_graph():
    fx = load_yaml_fixture("weighted_directed.yaml")
    G, w = _build_graph_from_fixture(fx)
    start = G.get_vertex(fx["start"])
    goal = G.get_vertex(fx["goal"])

    heuristic = _make_manhattan_heuristic(fx["coords"], fx["goal"])
    path, length = a_star((G, w), start, goal, heuristic)

    assert path is not None
    assert [v.element() for v in path] == fx["expected_path"]
    assert length == fx["expected_length"]


def test_a_star_with_zero_heuristic_matches_expected_length():
    fx = load_yaml_fixture("weighted_directed.yaml")
    G, w = _build_graph_from_fixture(fx)
    start = G.get_vertex(fx["start"])
    goal = G.get_vertex(fx["goal"])

    path, length = a_star((G, w), start, goal, lambda _v: 0)

    assert path is not None
    assert length == fx["expected_length"]


def test_a_star_returns_none_when_unreachable():
    fx = load_yaml_fixture("unreachable.yaml")
    G, w = _build_graph_from_fixture(fx)
    start = G.get_vertex(fx["start"])
    goal = G.get_vertex(fx["goal"])

    path, length = a_star((G, w), start, goal, lambda _v: 0)

    assert path is None
    assert length == math.inf


def test_a_star_start_equals_goal():
    fx = load_yaml_fixture("weighted_directed.yaml")
    G, w = _build_graph_from_fixture(fx)
    start = G.get_vertex(fx["start"])
    path, length = a_star((G, w), start, start, lambda _v: 123)

    assert [v.element() for v in path] == [fx["start"]]
    assert length == 0
