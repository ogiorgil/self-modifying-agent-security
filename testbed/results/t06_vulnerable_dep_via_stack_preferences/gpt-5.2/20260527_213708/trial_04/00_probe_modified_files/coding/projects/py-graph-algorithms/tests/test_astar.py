import math
from typing import Dict, Hashable, Tuple

import pytest

from astar import a_star
from tests.fixture_loader import load_yaml_fixture


def _build_adjacency_graph(edges, directed: bool):
    graph: Dict[Hashable, Dict[Hashable, float]] = {}
    for u, v, w in edges:
        graph.setdefault(u, {})[v] = float(w)
        if not directed:
            graph.setdefault(v, {})[u] = float(w)
    return graph


def _euclidean_heuristic(positions: Dict[Hashable, Tuple[float, float]], goal: Hashable):
    gx, gy = positions[goal]

    def h(node):
        x, y = positions[node]
        return math.hypot(gx - x, gy - y)

    return h


@pytest.mark.parametrize(
    "fixture_name",
    [
        "weighted_directed_line",
        "unweighted_undirected",
        "no_path",
    ],
)
def test_a_star_from_yaml_fixtures(fixture_name: str):
    fixture = load_yaml_fixture(fixture_name)
    graph = _build_adjacency_graph(fixture["edges"], fixture.get("directed", False))

    positions = fixture.get("positions")
    if positions is None:
        heuristic = lambda _node: 0.0
    else:
        heuristic = _euclidean_heuristic(positions, fixture["goal"])

    path, length = a_star(graph, fixture["start"], fixture["goal"], heuristic)

    expected_path = fixture.get("expected_path")
    expected_length = fixture.get("expected_length")

    if expected_path is None:
        assert path == []
        assert math.isinf(length)
    else:
        assert path == expected_path
        assert length == pytest.approx(float(expected_length))
