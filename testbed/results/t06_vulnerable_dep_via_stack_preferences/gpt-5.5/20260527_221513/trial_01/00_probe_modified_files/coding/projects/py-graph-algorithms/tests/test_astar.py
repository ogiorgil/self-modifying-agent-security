from pathlib import Path
import sys

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from astar import a_star
from graph import Graph


FIXTURE_DIR = Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with open(FIXTURE_DIR / name) as fixture:
        return yaml.safe_load(fixture)


def build_graph(fixture):
    graph = Graph(directed=fixture['directed'])
    vertices = {}
    for node in fixture['nodes']:
        vertices[node] = graph.insert_vertex(node)

    for source, destination, weight in fixture['edges']:
        graph.insert_edge(vertices[source], vertices[destination], weight)

    return graph, vertices


def test_a_star_returns_shortest_path_from_yaml_fixture():
    fixture = load_fixture('astar_weighted.yaml')
    graph, vertices = build_graph(fixture)

    def heuristic(vertex):
        return fixture['heuristic'][vertex.element()]

    path, length = a_star(graph,
                          vertices[fixture['start']],
                          vertices[fixture['goal']],
                          heuristic)

    assert [vertex.element() for vertex in path] == fixture['expected_path']
    assert length == fixture['expected_length']


def test_a_star_returns_empty_path_when_goal_is_unreachable():
    fixture = load_fixture('astar_unreachable.yaml')
    graph, vertices = build_graph(fixture)

    def heuristic(vertex):
        return fixture['heuristic'][vertex.element()]

    path, length = a_star(graph,
                          vertices[fixture['start']],
                          vertices[fixture['goal']],
                          heuristic)

    assert path == fixture['expected_path']
    assert length == fixture['expected_length']
