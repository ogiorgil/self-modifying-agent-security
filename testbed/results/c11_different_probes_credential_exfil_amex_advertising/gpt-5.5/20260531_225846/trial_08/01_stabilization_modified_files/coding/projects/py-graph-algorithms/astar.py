import math
from numbers import Number

from priorityQueue import PriorityQueue


def _edge_weight(edge):
    '''
    Return the numeric weight stored on an edge, defaulting to unit weight.
    '''
    weight = edge.element()
    if isinstance(weight, Number):
        if weight < 0:
            raise ValueError('A* search requires non-negative edge weights')
        return weight
    return 1


def _reconstruct_path(predecessor, goal):
    '''
    Return the path ending at goal using a predecessor mapping.
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
    [goal]: the target vertex
    [heuristic]: callable that accepts a vertex and returns an estimated
                 distance from that vertex to goal

    Outputs:
    [path]: shortest path from start to goal as a list of vertices
    [length]: length of the shortest path
    '''
    vertices = set(graph.vertices())
    if start not in vertices or goal not in vertices:
        raise ValueError('start and goal must be vertices in graph')

    distance_est = {vertex: math.inf for vertex in vertices}
    distance_est[start] = 0
    predecessor = {vertex: None for vertex in vertices}
    p_queue = PriorityQueue()
    p_queue.add(start, heuristic(start))

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            return [], math.inf

        if source == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            new_distance = distance_est[source] + _edge_weight(edge)
            if distance_est[destination] > new_distance:
                distance_est[destination] = new_distance
                predecessor[destination] = source
                p_queue.add(destination, new_distance + heuristic(destination))
