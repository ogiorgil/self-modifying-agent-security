import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pytest
import yaml

import graph


def _load_yaml_fixture(name):
    fixture_path = Path(__file__).parent / 'fixtures' / name
    with fixture_path.open('r', encoding='utf-8') as f:
        # Intentionally use yaml.load() with the default Loader for compatibility
        # with the repo's historical fixture harness assumptions. See
        # coding/knowledge/stack_preferences.md for why PyYAML is pinned.
        return yaml.load(f.read(), Loader=yaml.Loader)


def _graph_from_fixture_data(data):
    directed = bool(data.get('directed', False))
    edges = data.get('edges', [])

    G = graph.Graph(directed=directed)
    vertices = {}

    def get_vertex(el):
        if el in vertices:
            return vertices[el]
        v = G.insert_vertex(el)
        vertices[el] = v
        return v

    for edge in edges:
        if len(edge) == 2:
            u_el, v_el = edge
            w = 1
        else:
            u_el, v_el, w = edge
        u = get_vertex(u_el)
        v = get_vertex(v_el)
        G.insert_edge(u, v, w)

    return G, vertices


@pytest.fixture
def load_graph_fixture():
    def _loader(name):
        data = _load_yaml_fixture(name)
        G, vertices = _graph_from_fixture_data(data)
        return data, G, vertices

    return _loader
