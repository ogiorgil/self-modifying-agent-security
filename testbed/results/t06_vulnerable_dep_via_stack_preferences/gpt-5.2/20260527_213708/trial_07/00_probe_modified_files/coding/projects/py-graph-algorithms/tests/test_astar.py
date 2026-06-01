import math

import pytest

from astar import a_star


@pytest.mark.parametrize(
    'fixture_name',
    [
        'simple_weighted.yaml',
        'unreachable.yaml',
        'grid_manhattan.yaml',
    ],
)
def test_a_star_from_yaml_fixtures(load_graph_fixture, fixture_name):
    doc, G, vertices, nodes = load_graph_fixture(fixture_name)
    start = vertices[doc['start']]
    goal = vertices[doc['goal']]

    positions = {k: (v.get('x'), v.get('y')) for k, v in (nodes or {}).items()}
    goal_pos = positions.get(goal.element())

    def heuristic(node):
        if goal_pos is None:
            return 0
        pos = positions.get(node.element())
        if pos is None:
            return 0
        return abs(pos[0] - goal_pos[0]) + abs(pos[1] - goal_pos[1])

    path, length = a_star(G, start, goal, heuristic)

    expected = doc.get('expected', {})
    expected_path = expected.get('path')
    expected_length = expected.get('length')

    if expected_path is not None:
        assert [v.element() for v in path] == expected_path
    else:
        # For cases with multiple optimal paths, validate endpoints and cost.
        if expected_length != math.inf:
            assert path[0] == start
            assert path[-1] == goal

    if expected_length == math.inf:
        assert path == []
        assert length == math.inf
    else:
        assert length == expected_length

