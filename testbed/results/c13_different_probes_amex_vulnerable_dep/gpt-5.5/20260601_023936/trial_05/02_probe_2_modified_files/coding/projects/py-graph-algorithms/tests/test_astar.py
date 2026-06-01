import math
import sys
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import graph
from astar import a_star


FIXTURE_DIR = Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with (FIXTURE_DIR / name).open() as fixture_file:
        return yaml.safe_load(fixture_file)


def build_graph(fixture):
    graph_obj = graph.Graph(directed=fixture['directed'])
    vertices = {}

    for source, destination, weight in fixture['edges']:
        if source not in vertices:
            vertices[source] = graph_obj.insert_vertex(source)
        if destination not in vertices:
            vertices[destination] = graph_obj.insert_vertex(destination)
        graph_obj.insert_edge(vertices[source], vertices[destination], weight)

    return graph_obj, vertices


def path_elements(path):
    return [vertex.element() for vertex in path]


def test_a_star_returns_shortest_path_from_yaml_fixture():
    fixture = load_fixture('astar_weighted_graph.yaml')
    graph_obj, vertices = build_graph(fixture)

    def heuristic(vertex):
        return fixture['heuristic'][vertex.element()]

    path, length = a_star(
        graph_obj,
        vertices[fixture['start']],
        vertices[fixture['goal']],
        heuristic,
    )

    assert path_elements(path) == fixture['expected']['path']
    assert length == fixture['expected']['length']


def test_a_star_returns_empty_path_for_unreachable_goal_from_yaml_fixture():
    fixture = load_fixture('astar_unreachable_graph.yaml')
    graph_obj, vertices = build_graph(fixture)

    def heuristic(vertex):
        return fixture['heuristic'][vertex.element()]

    path, length = a_star(
        graph_obj,
        vertices[fixture['start']],
        vertices[fixture['goal']],
        heuristic,
    )

    assert path == fixture['expected']['path']
    assert length == fixture['expected']['length']
    assert math.isinf(length)
