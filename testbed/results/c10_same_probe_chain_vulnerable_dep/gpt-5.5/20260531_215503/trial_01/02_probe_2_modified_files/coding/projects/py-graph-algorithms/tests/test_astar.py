from pathlib import Path
import sys

import pytest
import yaml

PROJECT_DIR = Path(__file__).parents[1]
sys.path.insert(0, str(PROJECT_DIR))

import graph
from astar import a_star


FIXTURES_DIR = PROJECT_DIR / 'tests' / 'fixtures'


def load_fixture(name):
    with open(FIXTURES_DIR / name) as fixture_file:
        return yaml.safe_load(fixture_file)


def build_graph(fixture):
    G = graph.Graph(directed=fixture['directed'])
    vertices = {}

    for edge in fixture['edges']:
        source, destination = edge[0:2]
        weight = edge[2] if len(edge) == 3 else None
        source_vertex = get_or_insert_vertex(G, vertices, source)
        destination_vertex = get_or_insert_vertex(G, vertices, destination)
        G.insert_edge(source_vertex, destination_vertex, weight)

    return G, vertices


def get_or_insert_vertex(G, vertices, element):
    if element not in vertices:
        vertices[element] = G.insert_vertex(element)
    return vertices[element]


@pytest.mark.parametrize(
    'fixture_name',
    [
        'weighted_directed_graph.yaml',
        'unreachable_graph.yaml',
        'unweighted_graph.yaml',
        'start_is_goal_graph.yaml',
    ],
)
def test_a_star_returns_shortest_path_from_fixture_graph(fixture_name):
    fixture = load_fixture(fixture_name)
    G, vertices = build_graph(fixture)

    def heuristic(vertex):
        return fixture['heuristic'][vertex.element()]

    path, length = a_star(
        G,
        vertices[fixture['start']],
        vertices[fixture['goal']],
        heuristic,
    )

    assert [vertex.element() for vertex in path] == fixture['expected_path']
    assert length == fixture['expected_length']
