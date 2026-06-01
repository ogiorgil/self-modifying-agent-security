import math
from pathlib import Path

import pytest
import yaml

import graph
from astar import a_star


FIXTURES_DIR = Path(__file__).parent / "fixtures"


def _build_heuristic(spec, goal, positions):
    if spec == "zero":
        return lambda _v: 0

    if spec == "manhattan":
        goal_xy = positions[goal.element()]

        def h(v):
            x, y = positions[v.element()]
            return abs(x - goal_xy[0]) + abs(y - goal_xy[1])

        return h

    raise ValueError("Unknown heuristic: %s" % spec)


def _load_case(path):
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    edges = data["edges"]
    directed = bool(data.get("directed", False))
    G, w = graph.create_graph(edges, is_directed=directed)

    start = G.get_vertex(data["start"])
    goal = G.get_vertex(data["goal"])

    positions = data.get("positions", {})
    heuristic = _build_heuristic(data.get("heuristic", "zero"), goal, positions)

    expected = data.get("expected", {})
    expected_length = expected.get("length", None)
    expected_path = expected.get("path", None)

    return (G, w), start, goal, heuristic, expected_length, expected_path


@pytest.mark.parametrize("fixture_path", sorted(FIXTURES_DIR.glob("*.yaml")))
def test_a_star_from_yaml_fixture(fixture_path):
    graph_bundle, start, goal, heuristic, expected_length, expected_path = _load_case(
        fixture_path
    )

    path, length = a_star(graph_bundle, start, goal, heuristic)

    if expected_length is None:
        assert path == []
        assert length == math.inf
        return

    assert length == expected_length
    if expected_path is not None:
        assert [v.element() for v in path] == expected_path
