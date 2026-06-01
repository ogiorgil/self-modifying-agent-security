from pathlib import Path

import pytest
import yaml

import graph


@pytest.fixture
def fixture_dir():
    return Path(__file__).parent / 'fixtures'


def _build_graph_from_yaml(doc):
    G = graph.Graph(directed=bool(doc.get('directed', False)))
    vertices = {}

    nodes = doc.get('nodes', {}) or {}
    for label in nodes.keys():
        vertices[label] = G.insert_vertex(label)

    for u, v, w in doc.get('edges', []):
        if u not in vertices:
            vertices[u] = G.insert_vertex(u)
        if v not in vertices:
            vertices[v] = G.insert_vertex(v)
        G.insert_edge(vertices[u], vertices[v], w)

    return G, vertices, nodes


@pytest.fixture
def load_graph_fixture(fixture_dir):
    def _load(name):
        path = fixture_dir / name
        with path.open('r', encoding='utf-8') as f:
            doc = yaml.safe_load(f)
        G, vertices, nodes = _build_graph_from_yaml(doc)
        return doc, G, vertices, nodes

    return _load

