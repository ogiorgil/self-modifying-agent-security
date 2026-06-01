import graph
from astar import a_star


def test_a_star_matches_dijkstra_when_heuristic_is_zero():
    edges = [
        ('a', 'b', 1),
        ('b', 'c', 2),
        ('a', 'c', 10),
        ('c', 'd', 1),
        ('b', 'd', 10),
    ]
    G, w = graph.create_graph(edges, is_directed=True)

    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    path, length = a_star((G, w), start, goal, heuristic=lambda _: 0)

    assert [v.element() for v in path] == ['a', 'b', 'c', 'd']
    assert length == 4


def test_a_star_returns_empty_path_when_unreachable():
    edges = [
        ('a', 'b', 1),
        ('c', 'd', 1),
    ]
    G, w = graph.create_graph(edges, is_directed=True)

    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    path, length = a_star((G, w), start, goal, heuristic=lambda _: 0)

    assert path == []
    assert length == float('inf')
