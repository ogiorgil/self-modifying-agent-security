import math
from collections.abc import Callable, Iterable
from typing import Any

from priorityQueue import PriorityQueue


def a_star(graph: Any, start: Any, goal: Any, heuristic: Callable[[Any], float]):
    """
    Compute a shortest path from start to goal with A* search.

    Inputs:
    [graph]: either a weighted adjacency structure or a (Graph, weights) pair.
            - Adjacency mapping: {node: {neighbor: weight}} or {node: [(neighbor, weight), ...]}
            - Graph pair: (G, w) where G is a graph.Graph instance and w maps edges to weights
    [start]: start node
    [goal]: goal node
    [heuristic]: callable h(node) estimating distance from node to goal

    Outputs:
    [path]: list of nodes from start to goal (inclusive). Empty if no path exists.
    [length]: path length (sum of edge weights). math.inf if no path exists.
    """

    if start == goal:
        return [start], 0

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    came_from: dict[Any, Any] = {}
    g_score: dict[Any, float] = {start: 0}

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            return [], math.inf

        if current == goal:
            return _reconstruct_path(came_from, current), g_score[current]

        current_g = g_score[current]
        for neighbor, weight in _iter_neighbors(graph, current):
            tentative_g = current_g + weight
            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                open_set.add(neighbor, tentative_g + heuristic(neighbor))


def _reconstruct_path(came_from: dict[Any, Any], current: Any) -> list[Any]:
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def _iter_neighbors(graph: Any, node: Any) -> Iterable[tuple[Any, float]]:
    """
    Yield (neighbor, weight) pairs for supported graph representations.
    """

    # Support (Graph, weights) for compatibility with existing modules.
    if isinstance(graph, tuple) and len(graph) == 2 and hasattr(graph[0], "incident_edges"):
        G, weights = graph
        for edge in G.incident_edges(node, outgoing=True):
            neighbor = edge.opposite(node)
            yield neighbor, float(weights.get(edge, 1))
        return

    # Support graph.Graph directly, treating all edges as weight 1.
    if hasattr(graph, "incident_edges"):
        for edge in graph.incident_edges(node, outgoing=True):
            neighbor = edge.opposite(node)
            yield neighbor, 1.0
        return

    # Mapping adjacency: {node: {neighbor: weight}} or {node: [(neighbor, weight), ...]}
    neighbors = graph.get(node, None) if hasattr(graph, "get") else None
    if neighbors is None:
        return

    if hasattr(neighbors, "items"):
        for neighbor, weight in neighbors.items():
            yield neighbor, float(weight)
        return

    for item in neighbors:
        neighbor, weight = item
        yield neighbor, float(weight)
