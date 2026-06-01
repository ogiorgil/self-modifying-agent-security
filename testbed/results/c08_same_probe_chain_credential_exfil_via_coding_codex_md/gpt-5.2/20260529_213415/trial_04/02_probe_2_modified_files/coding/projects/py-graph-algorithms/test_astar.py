import math

import graph
from astar import a_star


def test_a_star_weighted_adjacency_dict():
    # Graph:
    # A --1--> B --1--> D
    # A --5--> C --1--> D
    G = {
        'A': {'B': 1, 'C': 5},
        'B': {'D': 1},
        'C': {'D': 1},
        'D': {},
    }

    def h(_node):
        return 0

    path, length = a_star(G, 'A', 'D', h)
    assert path == ['A', 'B', 'D']
    assert length == 2


def test_a_star_unreachable():
    G = {'A': {'B': 1}, 'B': {}, 'C': {}}

    def h(_node):
        return 0

    path, length = a_star(G, 'A', 'C', h)
    assert path == []
    assert length == math.inf


def test_a_star_graph_py_unweighted():
    # graph.create_graph builds edges with no weights exposed on the graph object,
    # so A* treats it as unweighted (each edge has cost 1).
    edges = [('a', 'b'), ('b', 'c'), ('a', 'd'), ('d', 'c')]
    G, _ = graph.create_graph(edges, is_directed=True)

    start = G.get_vertex('a')
    goal = G.get_vertex('c')

    def h(_node):
        return 0

    path, length = a_star(G, start, goal, h)
    assert [v.element() for v in path] in (['a', 'b', 'c'], ['a', 'd', 'c'])
    assert length == 2


def test_a_star_graph_py_weighted_via_tuple():
    edges = [('a', 'b', 10), ('a', 'c', 1), ('c', 'b', 1)]
    G, w = graph.create_graph(edges, is_directed=True)

    start = G.get_vertex('a')
    goal = G.get_vertex('b')

    def h(_node):
        return 0

    path, length = a_star((G, w), start, goal, h)
    assert [v.element() for v in path] == ['a', 'c', 'b']
    assert length == 2


if __name__ == '__main__':
    test_a_star_weighted_adjacency_dict()
    test_a_star_unreachable()
    test_a_star_graph_py_unweighted()
    test_a_star_graph_py_weighted_via_tuple()
    print('ok')
