import math
from pathlib import Path

import pytest
import yaml

from astar import a_star
from graph import Graph


FIXTURES = Path(__file__).parent / 'fixtures'


@pytest.fixture
def load_graph_fixture():
    def _load(name):
        with open(FIXTURES / name) as fixture:
            return yaml.safe_load(fixture)

    return _load


def test_a_star_finds_shortest_path_from_yaml_fixture(load_graph_fixture):
    data = load_graph_fixture('weighted_graph.yaml')
    path, length = a_star(
        data['edges'],
        data['start'],
        data['goal'],
        lambda node: data['heuristic'][node],
    )

    assert path == data['expected_path']
    assert length == data['expected_length']


def test_a_star_returns_empty_path_when_goal_unreachable(load_graph_fixture):
    data = load_graph_fixture('unreachable_graph.yaml')
    path, length = a_star(
        data['edges'],
        data['start'],
        data['goal'],
        lambda node: data['heuristic'][node],
    )

    assert path == []
    assert length == math.inf


def test_a_star_supports_existing_graph_class():
    graph = Graph(directed=True)
    vertices = {label: graph.insert_vertex(label) for label in ('A', 'B', 'C', 'D')}
    graph.insert_edge(vertices['A'], vertices['B'], 1)
    graph.insert_edge(vertices['A'], vertices['C'], 4)
    graph.insert_edge(vertices['B'], vertices['C'], 2)
    graph.insert_edge(vertices['B'], vertices['D'], 5)
    graph.insert_edge(vertices['C'], vertices['D'], 1)

    heuristic = {'A': 4, 'B': 2, 'C': 1, 'D': 0}
    path, length = a_star(
        graph,
        vertices['A'],
        vertices['D'],
        lambda node: heuristic[node.element()],
    )

    assert [node.element() for node in path] == ['A', 'B', 'C', 'D']
    assert length == 4
