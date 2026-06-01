import math

import graph
from astar import a_star


def _heuristic_from_mapping(mapping, goal):
    if mapping is None:
        return lambda _node: 0

    if goal in mapping and isinstance(mapping[goal], dict) and "x" in mapping[goal]:
        goal_x = mapping[goal]["x"]
        goal_y = mapping[goal]["y"]

        def h(node):
            p = mapping[node]
            return abs(p["x"] - goal_x) + abs(p["y"] - goal_y)

        return h

    return lambda node: mapping[node]


def _graph_from_fixture(data):
    if "graph" in data:
        return data["graph"]

    edges = data["edges"]
    directed = bool(data.get("directed", False))
    G, w = graph.create_graph(edges, is_directed=directed)
    return G, w


def test_a_star_yaml_fixtures(load_yaml_fixture):
    for name in [
        "simple_weighted.yaml",
        "edge_list_weighted.yaml",
        "start_is_goal.yaml",
        "unreachable.yaml",
    ]:
        data = load_yaml_fixture(name)
        g = _graph_from_fixture(data)
        start = data["start"]
        goal = data["goal"]

        # If we're using the graph.Graph representation, translate elements to Vertex objects.
        if isinstance(g, tuple) and hasattr(g[0], "get_vertex"):
            G, w = g
            start = G.get_vertex(start)
            goal = G.get_vertex(goal)
            g = (G, w)

            def heuristic(v):
                return _heuristic_from_mapping(data.get("heuristic"), goal.element())(v.element())

        else:
            heuristic = _heuristic_from_mapping(data.get("heuristic"), goal)

        path, length = a_star(g, start, goal, heuristic)

        if data.get("expected_path") is None:
            assert path == []
            assert math.isinf(length)
            continue

        if path and hasattr(path[0], "element"):
            path_elements = [v.element() for v in path]
        else:
            path_elements = path

        assert path_elements == data["expected_path"]
        assert length == data["expected_length"]

