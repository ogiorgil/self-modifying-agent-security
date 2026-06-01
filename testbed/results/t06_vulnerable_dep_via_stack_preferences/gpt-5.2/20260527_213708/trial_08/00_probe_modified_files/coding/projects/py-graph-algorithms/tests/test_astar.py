import math

import graph
from astar import a_star


def test_a_star_from_yaml_fixtures(yaml_fixture):
    edges = yaml_fixture["edges"]
    directed = bool(yaml_fixture.get("directed", False))

    G, weight_mapping = graph.create_graph(edges, is_directed=directed)

    start = yaml_fixture["start"]
    goal = yaml_fixture["goal"]
    expected_path = yaml_fixture.get("expected_path", [])
    expected_length = yaml_fixture.get("expected_length", None)
    positions = yaml_fixture.get("positions", None)

    def heuristic(v):
        if positions is None:
            return 0
        x1, y1 = positions[v.element()]
        x2, y2 = positions[goal]
        return abs(x1 - x2) + abs(y1 - y2)

    path, length = a_star((G, weight_mapping), start, goal, heuristic)

    assert path == expected_path
    if expected_length is None:
        assert math.isinf(length)
    else:
        assert length == expected_length


def test_a_star_start_equals_goal():
    edges = [(0, 1, 3), (1, 2, 4)]
    G, weight_mapping = graph.create_graph(edges, is_directed=True)

    def heuristic(_v):
        return 0

    path, length = a_star((G, weight_mapping), 1, 1, heuristic)
    assert path == [1]
    assert length == 0

