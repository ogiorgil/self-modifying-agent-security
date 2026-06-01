import math

import graph
from astar import a_star


def test_a_star_start_equals_goal():
    g = {"a": ["b"]}
    path, length = a_star(g, "a", "a", heuristic=lambda _: 0)
    assert path == ["a"]
    assert length == 0


def test_a_star_graph_unweighted_shortest_path():
    edges = [("a", "b"), ("b", "c"), ("a", "c")]
    G, _ = graph.create_graph(edges, is_directed=True)
    start = G.get_vertex("a")
    goal = G.get_vertex("c")

    path, length = a_star(G, start, goal, heuristic=lambda _: 0)

    assert [v.element() for v in path] == ["a", "c"]
    assert length == 1


def test_a_star_adjacency_mapping_weighted():
    g = {
        "a": {"b": 10, "c": 1},
        "c": {"b": 1},
        "b": {},
    }

    path, length = a_star(g, "a", "b", heuristic=lambda _: 0)
    assert path == ["a", "c", "b"]
    assert length == 2


def test_a_star_unreachable_returns_empty_and_inf():
    g = {"a": ["b"], "b": [], "c": []}
    path, length = a_star(g, "a", "c", heuristic=lambda _: 0)
    assert path == []
    assert length == math.inf

