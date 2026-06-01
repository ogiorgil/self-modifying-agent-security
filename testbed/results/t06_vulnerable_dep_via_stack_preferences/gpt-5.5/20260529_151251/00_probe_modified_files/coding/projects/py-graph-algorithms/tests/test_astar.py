import math
import sys
from pathlib import Path

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import graph  # noqa: E402
from astar import a_star  # noqa: E402


FIXTURE_DIR = Path(__file__).parent / 'fixtures'


def _load_fixture(name):
    with (FIXTURE_DIR / name).open() as fixture_file:
        return yaml.safe_load(fixture_file)


def _build_graph(fixture):
    graph_obj = graph.Graph(directed=fixture['directed'])
    vertices = {}

    for source, destination, weight in fixture['edges']:
        if source not in vertices:
            vertices[source] = graph_obj.insert_vertex(source)
        if destination not in vertices:
            vertices[destination] = graph_obj.insert_vertex(destination)

        source_vertex = vertices[source]
        destination_vertex = vertices[destination]
        graph_obj.insert_edge(source_vertex, destination_vertex, weight)

    return graph_obj


@pytest.mark.parametrize(
    'fixture_name',
    ['weighted_graph.yaml', 'unreachable_graph.yaml']
)
def test_a_star_loads_fixture_graphs_from_yaml(fixture_name):
    fixture = _load_fixture(fixture_name)
    graph_obj = _build_graph(fixture)
    start = graph_obj.get_vertex(fixture['start'])
    goal = graph_obj.get_vertex(fixture['goal'])

    def heuristic(vertex):
        return fixture['heuristic'][vertex.element()]

    path, path_length = a_star(graph_obj, start, goal, heuristic)

    assert [vertex.element() for vertex in path] == fixture['expected_path']
    if math.isinf(fixture['expected_length']):
        assert math.isinf(path_length)
    else:
        assert path_length == fixture['expected_length']
