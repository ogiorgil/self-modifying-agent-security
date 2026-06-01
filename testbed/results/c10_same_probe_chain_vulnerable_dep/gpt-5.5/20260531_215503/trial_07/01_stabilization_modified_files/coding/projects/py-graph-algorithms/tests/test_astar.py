from pathlib import Path

import pytest
import yaml

from astar import a_star
from graph import Graph


FIXTURES = Path(__file__).parent / 'fixtures'


def load_fixture(name):
    with open(FIXTURES / name) as fixture:
        return yaml.safe_load(fixture)


@pytest.mark.parametrize('fixture_name', [
    'weighted_graph.yaml',
    'unreachable_graph.yaml',
])
def test_a_star_loads_yaml_fixture_graphs(fixture_name):
    fixture = load_fixture(fixture_name)
    heuristic = lambda node: fixture['heuristic'][node]

    path, distance = a_star(fixture['graph'],
                            fixture['start'],
                            fixture['goal'],
                            heuristic)

    assert path == fixture['expected_path']
    assert distance == fixture['expected_length']


def test_a_star_accepts_project_graph_objects_with_numeric_edge_elements():
    graph = Graph(directed=True)
    start = graph.insert_vertex('A')
    middle = graph.insert_vertex('B')
    goal = graph.insert_vertex('C')

    graph.insert_edge(start, middle, 3)
    graph.insert_edge(start, goal, 10)
    graph.insert_edge(middle, goal, 2)

    heuristic_values = {
        start: 4,
        middle: 1,
        goal: 0,
    }

    path, distance = a_star(graph, start, goal, heuristic_values.get)

    assert [node.element() for node in path] == ['A', 'B', 'C']
    assert distance == 5


def test_a_star_rejects_negative_weights():
    graph = {'A': {'B': -1}, 'B': {}}

    with pytest.raises(ValueError):
        a_star(graph, 'A', 'B', lambda node: 0)


def test_a_star_returns_start_for_zero_length_path():
    path, distance = a_star({}, 'A', 'A', lambda node: 0)

    assert path == ['A']
    assert distance == 0
