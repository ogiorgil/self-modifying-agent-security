import math
from typing import Callable, Tuple

from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic: Callable[[object], float]) -> Tuple[list, float]:
    """
    A* search for the shortest path between two nodes.

    Inputs:
    [graph]: either:
        - (G, w) tuple where G is a graph.Graph instance and w maps edges to weights
        - a graph.Graph instance (edge weights inferred from edge.element() when numeric, else 1)
    [start]: start node (typically a graph.Graph.Vertex instance)
    [goal]: goal node (typically a graph.Graph.Vertex instance)
    [heuristic]: callable taking a node and returning a numeric estimate to the goal

    Outputs:
    [path]: list of nodes from start to goal (inclusive). Empty if no path.
    [length]: numeric length of the path. math.inf if no path.
    """

    G, w = _normalize_graph_and_weights(graph)

    if start == goal:
        return [start], 0

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    came_from = {start: None}
    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0

    # Track which nodes are still in the open set to avoid relying on PQ internals
    in_open_set = {start}

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            break
        in_open_set.discard(current)

        if current == goal:
            path = _reconstruct_path(came_from, current)
            return path, g_score[current]

        for edge in G.incident_edges(current, outgoing=True) or ():
            neighbor = edge.opposite(current)
            tentative_g = g_score[current] + w.get(edge, 1)
            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                open_set.add(neighbor, f_score)
                in_open_set.add(neighbor)

    return [], math.inf


def _reconstruct_path(came_from, current) -> list:
    path = [current]
    while True:
        current = came_from.get(current)
        if current is None:
            break
        path.insert(0, current)
    return path


def _normalize_graph_and_weights(graph):
    """
    Normalize [graph] to (G, w) where:
    - G is a graph.Graph instance (or compatible)
    - w maps edges to numeric weights
    """
    if isinstance(graph, tuple) and len(graph) == 2:
        G, w = graph
        return G, w

    G = graph
    w = {}
    for edge in G.edges():
        weight = edge.element()
        if isinstance(weight, (int, float)):
            w[edge] = weight
        else:
            w[edge] = 1
    return G, w
