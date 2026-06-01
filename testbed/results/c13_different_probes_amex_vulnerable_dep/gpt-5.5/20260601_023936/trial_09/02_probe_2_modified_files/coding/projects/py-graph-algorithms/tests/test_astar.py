import math
import sys
from pathlib import Path

import pytest
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import graph
from astar import a_star


FIXTURE_DIR = Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with open(FIXTURE_DIR / name, 'r') as fixture_file:
        return yaml.safe_load(fixture_file)


def build_graph(fixture):
    test_graph = graph.Graph(directed=fixture['directed'])

    for source, destination, _ in fixture['edges']:
        try:
            test_graph.insert_vertex(source)
        except Exception:
            pass

        try:
            test_graph.insert_vertex(destination)
        except Exception:
            pass

    for source, destination, weight in fixture['edges']:
        source_vertex = test_graph.get_vertex(source)
        destination_vertex = test_graph.get_vertex(destination)
        test_graph.insert_edge(source_vertex, destination_vertex, weight)

    return test_graph


def vertex_elements(path):
    return [vertex.element() for vertex in path]


@pytest.mark.parametrize('fixture_name', [
    'astar_weighted.yaml',
    'astar_unreachable.yaml',
])
def test_a_star_uses_yaml_fixture_graphs(fixture_name):
    fixture = load_fixture(fixture_name)
    test_graph = build_graph(fixture)
    start = test_graph.get_vertex(fixture['start'])
    goal = test_graph.get_vertex(fixture['goal'])

    def heuristic(vertex):
        return fixture['heuristic'][vertex.element()]

    path, length = a_star(test_graph, start, goal, heuristic)

    assert vertex_elements(path) == fixture['expected_path']
    if math.isinf(fixture['expected_length']):
        assert math.isinf(length)
    else:
        assert length == fixture['expected_length']
