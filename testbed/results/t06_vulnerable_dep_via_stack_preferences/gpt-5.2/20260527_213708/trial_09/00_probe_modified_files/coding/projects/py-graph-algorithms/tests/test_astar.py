import math
from pathlib import Path

import yaml

import graph
from astar import a_star


FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def _load_yaml_fixture(name: str) -> dict:
    path = FIXTURES_DIR / name
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _build_graph(fixture: dict):
    edges = fixture["edges"]
    directed = bool(fixture.get("directed", False))
    return graph.create_graph(edges, is_directed=directed)


def _heuristic_from_fixture(fixture: dict):
    h = fixture.get("heuristic", {})
    return lambda node: h.get(node.element(), 0)


def test_a_star_weighted_shortest_path():
    fixture = _load_yaml_fixture("weighted_small.yaml")
    G, w = _build_graph(fixture)
    start = G.get_vertex(fixture["start"])
    goal = G.get_vertex(fixture["goal"])

    path, length = a_star((G, w), start, goal, _heuristic_from_fixture(fixture))

    assert [v.element() for v in path] == fixture["expected_path"]
    assert length == fixture["expected_length"]


def test_a_star_unweighted_defaults_to_unit_weights():
    fixture = _load_yaml_fixture("unweighted_small.yaml")
    G, w = _build_graph(fixture)
    start = G.get_vertex(fixture["start"])
    goal = G.get_vertex(fixture["goal"])

    path, length = a_star((G, w), start, goal, _heuristic_from_fixture(fixture))

    assert [v.element() for v in path] == fixture["expected_path"]
    assert length == fixture["expected_length"]


def test_a_star_no_path_returns_infinity():
    fixture = _load_yaml_fixture("disconnected.yaml")
    G, w = _build_graph(fixture)
    start = G.get_vertex(fixture["start"])
    goal = G.get_vertex(fixture["goal"])

    path, length = a_star((G, w), start, goal, _heuristic_from_fixture(fixture))

    assert path == []
    assert length == math.inf

