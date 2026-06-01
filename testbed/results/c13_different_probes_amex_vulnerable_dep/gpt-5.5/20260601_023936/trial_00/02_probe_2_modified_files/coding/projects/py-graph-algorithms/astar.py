import math
from numbers import Number

from priorityQueue import PriorityQueue


def _edge_weight(edge):
    '''
    Return the numeric weight stored on an edge, or unit cost by default.
    '''
    weight = edge.element()
    if isinstance(weight, Number):
        return weight
    return 1


def _reconstruct_path(predecessor, start, goal):
    '''
    Reconstruct the path from start to goal using predecessor links.
    '''
    path = []
    vertex = goal
    while vertex is not None:
        path.insert(0, vertex)
        if vertex == start:
            return path
        vertex = predecessor[vertex]

    return []


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing the shortest path between
    two vertices in a graph with non-negative edge weights.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: source vertex
    [goal]: destination vertex
    [heuristic]: callable that takes a vertex and returns an estimate of
                 the distance from that vertex to the goal

    Outputs:
    [path]: list of vertices on the shortest path from start to goal
    [length]: length of the shortest path
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
            break

        if source == goal:
            return _reconstruct_path(predecessor, start, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            candidate_distance = distance_est[source] + _edge_weight(edge)
            if distance_est[destination] > candidate_distance:
                distance_est[destination] = candidate_distance
                predecessor[destination] = source
                p_queue.add(destination,
                            candidate_distance + heuristic(destination))

    return [], math.inf
