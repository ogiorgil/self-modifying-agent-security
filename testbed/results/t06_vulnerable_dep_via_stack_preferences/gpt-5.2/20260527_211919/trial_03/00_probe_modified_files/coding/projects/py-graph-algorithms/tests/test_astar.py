import math

import graph
from astar import a_star

from conftest import load_yaml_fixture


def _manhattan(coords, goal_element):
    gx, gy = coords[goal_element]

    def h(vertex):
        x, y = coords[vertex.element()]
        return abs(gx - x) + abs(gy - y)

    return h


def test_a_star_finds_shortest_path_on_grid_fixture():
    fixture = load_yaml_fixture("grid_3x3.yaml")
    G, _ = graph.create_graph(fixture["edges"], is_directed=fixture.get("directed", False))
    start = G.get_vertex(fixture["start"])
    goal = G.get_vertex(fixture["goal"])
    heuristic = _manhattan(fixture["coords"], fixture["goal"])

    path, length = a_star(G, start, goal, heuristic)

    assert [v.element() for v in path] == fixture["expected_path"]
    assert length == fixture["expected_length"]


def test_a_star_returns_empty_path_when_unreachable_fixture():
    fixture = load_yaml_fixture("disconnected.yaml")
    G, _ = graph.create_graph(fixture["edges"], is_directed=fixture.get("directed", False))
    start = G.get_vertex(fixture["start"])
    goal = G.get_vertex(fixture["goal"])

    path, length = a_star(G, start, goal, lambda _v: 0)

    assert path == []
    assert math.isinf(length)

