import math
from numbers import Real

from priorityQueue import PriorityQueue


def _edge_weight(edge):
    '''
    Return the edge weight stored in the edge element.
    '''
    weight = edge.element()
    if isinstance(weight, Real):
        if weight < 0:
            raise ValueError('A* search requires non-negative edge weights')
        return weight
    return 1


def _reconstruct_path(predecessor, goal):
    '''
    Reconstruct a path from a predecessor mapping.
    '''
    path = [goal]
    vertex = predecessor[goal]
    while vertex is not None:
        path.insert(0, vertex)
        vertex = predecessor[vertex]
    return path


def a_star(graph, start, goal, heuristic):
    '''
    Compute the shortest path from start to goal using A* search.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the destination vertex
    [heuristic]: callable taking a vertex and returning an estimate of
                 its distance to goal

    Outputs:
    [path]: list of vertices from start to goal, or an empty list if no
            path exists
    [length]: length of the shortest path, or math.inf if no path exists
    '''
    distance_est = {vertex: math.inf for vertex in graph.vertices()}
    distance_est[start] = 0
    predecessor = {vertex: None for vertex in graph.vertices()}

    p_queue = PriorityQueue()
    p_queue.add(start, heuristic(start))

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            return [], math.inf

        if source == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        incident_edges = graph.incident_edges(source, outgoing=True)
        if incident_edges is None:
            continue

        for edge in incident_edges:
            destination = edge.opposite(source)
            weight = _edge_weight(edge)
            candidate_distance = distance_est[source] + weight
            if distance_est[destination] > candidate_distance:
                distance_est[destination] = candidate_distance
                predecessor[destination] = source
                p_queue.add(destination,
                            candidate_distance + heuristic(destination))
