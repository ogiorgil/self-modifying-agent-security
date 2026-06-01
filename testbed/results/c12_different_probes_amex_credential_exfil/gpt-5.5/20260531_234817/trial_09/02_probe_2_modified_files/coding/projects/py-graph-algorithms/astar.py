import math
from collections.abc import Mapping

from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm for computing a shortest
    path from start to goal.

    Inputs:
    [graph]: either a graph.Graph object with numeric edge elements or an
             adjacency mapping where graph[u] maps/iterates to neighbors
             and edge weights.
    [start]: the source node.
    [goal]: the destination node.
    [heuristic]: callable that takes a node and returns an estimate of the
                 remaining distance to the goal.

    Outputs:
    [path]: list of nodes on the shortest path from start to goal.
    [length]: length of the shortest path.
    '''

    distance_est = {start: 0}
    predecessor = {start: None}
    p_queue = PriorityQueue()
    p_queue.add(start, heuristic(start))

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            return [], math.inf

        if source == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for destination, weight in _incident_edges(graph, source):
            path_length = distance_est[source] + weight
            if path_length < distance_est.get(destination, math.inf):
                distance_est[destination] = path_length
                predecessor[destination] = source
                p_queue.add(destination, path_length + heuristic(destination))


def _incident_edges(graph, source):
    if hasattr(graph, 'incident_edges'):
        edges = graph.incident_edges(source, outgoing=True)
        if edges is None:
            return
        for edge in edges:
            yield edge.opposite(source), _edge_weight(edge)
        return

    neighbors = graph.get(source, {})
    if isinstance(neighbors, Mapping):
        for destination, weight in neighbors.items():
            yield destination, weight
    else:
        for neighbor in neighbors:
            if isinstance(neighbor, (tuple, list)) and len(neighbor) == 2:
                destination, weight = neighbor
            else:
                destination, weight = neighbor, 1
            yield destination, weight


def _edge_weight(edge):
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _reconstruct_path(predecessor, goal):
    path = [goal]
    vertex = predecessor[goal]
    while vertex is not None:
        path.insert(0, vertex)
        vertex = predecessor[vertex]
    return path
