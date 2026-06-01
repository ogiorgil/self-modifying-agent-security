import math

from astar import a_star
from graph import Graph


def weighted_graph(edges):
    graph = Graph(directed=True)
    vertices = {}

    for source, destination, weight in edges:
        if source not in vertices:
            vertices[source] = graph.insert_vertex(source)
        if destination not in vertices:
            vertices[destination] = graph.insert_vertex(destination)
        graph.insert_edge(vertices[source], vertices[destination], weight)

    return graph, vertices


def path_elements(path):
    return [vertex.element() for vertex in path]


def test_a_star_returns_shortest_path_and_length():
    graph, vertices = weighted_graph([
        ('a', 'b', 1),
        ('a', 'c', 4),
        ('b', 'c', 2),
        ('b', 'd', 5),
        ('c', 'd', 1),
    ])
    heuristic = {
        vertices['a']: 3,
        vertices['b']: 2,
        vertices['c']: 1,
        vertices['d']: 0,
    }

    path, length = a_star(graph, vertices['a'], vertices['d'], heuristic.get)

    assert path_elements(path) == ['a', 'b', 'c', 'd']
    assert length == 4


def test_a_star_returns_empty_path_for_unreachable_goal():
    graph, vertices = weighted_graph([
        ('a', 'b', 1),
        ('c', 'd', 1),
    ])

    path, length = a_star(graph, vertices['a'], vertices['d'], lambda vertex: 0)

    assert path == []
    assert length == math.inf
