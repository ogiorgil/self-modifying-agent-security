import math
from numbers import Real

from priorityQueue import PriorityQueue


def _edge_length(edge):
    '''
    Return a numeric length for edge, defaulting to unit length.
    '''
    value = edge.element()
    if isinstance(value, Real):
        return value
    return 1


def a_star(graph, start, goal, heuristic):
    '''
    Find the shortest path from start to goal using A* search.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the start vertex
    [goal]: the goal vertex
    [heuristic]: callable mapping a vertex to an estimate of the remaining
                 distance to goal

    Outputs:
    [path]: list of vertices on the shortest path from start to goal
    [length]: length of that shortest path
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
            path = [goal]
            vertex = predecessor[goal]
            while vertex is not None:
                path.insert(0, vertex)
                vertex = predecessor[vertex]
            return path, distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            candidate = distance_est[source] + _edge_length(edge)
            if candidate < distance_est[destination]:
                distance_est[destination] = candidate
                predecessor[destination] = source
                p_queue.add(destination, candidate + heuristic(destination))

    return [], math.inf
