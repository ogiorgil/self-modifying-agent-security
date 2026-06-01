import math

import graph
import pytest

from astar import a_star


def _build_from_fixture(data):
    G, w = graph.create_graph(data["edges"], is_directed=bool(data.get("directed", False)))
    start = G.get_vertex(data["start"])
    goal = G.get_vertex(data["goal"])
    heuristic_map = data.get("heuristic", {})

    def heuristic(node):
        if not heuristic_map:
            return 0
        return heuristic_map[node.element()]

    return (G, w), start, goal, heuristic


@pytest.mark.parametrize(
    "fixture_name",
    [
        "astar_basic.yaml",
        "astar_directed.yaml",
    ],
)
def test_a_star_fixtures(fixture_name, graph_fixture):
    data = graph_fixture(fixture_name)
    graph_tuple, start, goal, heuristic = _build_from_fixture(data)

    path, length = a_star(graph_tuple, start, goal, heuristic)

    assert [v.element() for v in path] == data["expected"]["path"]
    assert length == pytest.approx(data["expected"]["length"])


def test_a_star_unreachable_returns_empty_and_inf(graph_fixture):
    data = graph_fixture("astar_unreachable.yaml")
    graph_tuple, start, goal, heuristic = _build_from_fixture(data)

    path, length = a_star(graph_tuple, start, goal, heuristic)

    assert path == []
    assert length == math.inf


def test_a_star_start_equals_goal(graph_fixture):
    data = graph_fixture("astar_basic.yaml")
    graph_tuple, start, _, heuristic = _build_from_fixture(data)

    path, length = a_star(graph_tuple, start, start, heuristic)

    assert [v.element() for v in path] == [data["start"]]
    assert length == 0
