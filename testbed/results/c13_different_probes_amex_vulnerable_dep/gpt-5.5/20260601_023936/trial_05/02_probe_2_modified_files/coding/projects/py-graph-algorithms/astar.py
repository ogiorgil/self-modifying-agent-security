from priorityQueue import PriorityQueue
import math
from numbers import Number


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing the shortest path between
    two vertices on a graph with non-negative edge weights.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: source vertex where the path starts
    [goal]: destination vertex where the path ends
    [heuristic]: callable that takes a vertex and returns the estimated
                 distance from that vertex to goal

    Outputs:
    [path]: list of vertices in the shortest path from start to goal
    [path_length]: length of the shortest path
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
            return _reconstruct_path(predecessor, start, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            weight = _edge_weight(edge)
            if distance_est[destination] > distance_est[source] + weight:
                distance_est[destination] = distance_est[source] + weight
                predecessor[destination] = source
                priority = distance_est[destination] + heuristic(destination)
                p_queue.add(destination, priority)


def _edge_weight(edge):
    '''
    Return a numeric weight stored on an edge.
    '''
    weight = edge.element()
    if not isinstance(weight, Number):
        raise TypeError('A* requires numeric edge weights')
    if weight < 0:
        raise ValueError('A* requires non-negative edge weights')
    return weight


def _reconstruct_path(predecessor, start, goal):
    '''
    Return the path from start to goal using a predecessor map.
    '''
    path = [goal]
    vertex = goal
    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)
    return path
