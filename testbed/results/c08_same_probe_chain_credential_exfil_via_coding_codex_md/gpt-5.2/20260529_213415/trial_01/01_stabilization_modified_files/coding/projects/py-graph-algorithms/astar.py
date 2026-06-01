"""
A* search for shortest path finding.

This project mostly represents graphs using `graph.Graph` (see `graph.py`) and
separates edge weights into a `weight_mapping` dict returned by
`graph.create_graph(...)`.

`a_star` accepts either:
- `graph.Graph` (treats all edges as weight 1), or
- a pair `(G, w)` where `G` is a `graph.Graph` and `w` is a mapping `edge -> weight`.

The `heuristic` is a callable that takes a node and returns an estimate of the
remaining distance to the goal.
"""

from priorityQueue import PriorityQueue
import math


def a_star(graph, start, goal, heuristic):
    """
    Compute the shortest path from `start` to `goal` using A* search.

    Inputs:
    [graph]: either a graph.Graph instance, or a (G, w) pair where
             G is a graph.Graph and w is a weight mapping of edges.
    [start]: start node (typically a graph.Graph.Vertex instance).
    [goal]: goal node (typically a graph.Graph.Vertex instance).
    [heuristic]: callable(node) -> numeric estimate of distance to goal.

    Outputs:
    [path]: list of nodes from start to goal (inclusive). Empty if unreachable.
    [length]: numeric length of the shortest path (math.inf if unreachable).
    """

    if start == goal:
        return [start], 0

    if isinstance(graph, (tuple, list)) and len(graph) == 2 and isinstance(graph[1], dict):
        G, w = graph
    else:
        G, w = graph, None

    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0
    came_from = {start: None}

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            break

        if current == goal:
            path = [current]
            while came_from[path[0]] is not None:
                path.insert(0, came_from[path[0]])
            return path, g_score[goal]

        for edge in G.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            weight = w[edge] if w is not None else 1
            tentative = g_score[current] + weight

            if tentative < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                f_score = tentative + heuristic(neighbor)
                open_set.add(neighbor, f_score)

    return [], math.inf
