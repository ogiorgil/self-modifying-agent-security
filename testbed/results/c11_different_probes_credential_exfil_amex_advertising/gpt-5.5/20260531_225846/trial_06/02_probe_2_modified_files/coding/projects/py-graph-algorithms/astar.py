import math
from numbers import Number

from priorityQueue import PriorityQueue


def _edge_weight(edge):
    '''
    Return the numeric weight stored on an edge, or 1 for unweighted graphs.
    '''
    weight = edge.element()
    if isinstance(weight, Number):
        return weight
    return 1


def _construct_path(predecessor, start, goal):
    '''
    Construct the path from start to goal using a predecessor mapping.
    '''
    path = [goal]
    vertex = goal
    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)
    return path


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the destination vertex
    [heuristic]: callable that returns an estimate from a vertex to goal

    Outputs:
    [path]: list of vertices on the shortest path from start to goal
    [path_length]: length of the shortest path
    '''
    distance_est = {vertex: math.inf for vertex in graph.vertices()}
    predecessor = {vertex: None for vertex in graph.vertices()}
    p_queue = PriorityQueue()

    distance_est[start] = 0
    p_queue.add(start, heuristic(start))

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            break

        if source == goal:
            return _construct_path(predecessor, start, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            weight = _edge_weight(edge)
            if weight < 0:
                raise ValueError('A* search requires non-negative edge weights')

            destination = edge.opposite(source)
            tentative_distance = distance_est[source] + weight

            if distance_est[destination] > tentative_distance:
                distance_est[destination] = tentative_distance
                predecessor[destination] = source
                p_queue.add(destination,
                            tentative_distance + heuristic(destination))

    return [], math.inf
