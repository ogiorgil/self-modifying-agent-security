from priorityQueue import PriorityQueue
import math


def _edge_length(edge):
    '''
    Return the numeric length stored on an edge, or 1 for unweighted edges.
    '''
    length = edge.element()
    if isinstance(length, (int, float)):
        if length < 0:
            raise ValueError('A* search requires non-negative edge lengths')
        return length
    return 1


def _reconstruct_path(predecessor, start, goal):
    '''
    Reconstruct the path from start to goal using a predecessor mapping.
    '''
    path = [goal]
    vertex = goal
    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)
    return path


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for shortest paths.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the destination vertex
    [heuristic]: callable that returns an estimate from a vertex to goal

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
            return [], math.inf

        if source == goal:
            return _reconstruct_path(predecessor, start, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            path_length = distance_est[source] + _edge_length(edge)
            if distance_est[destination] > path_length:
                distance_est[destination] = path_length
                predecessor[destination] = source
                priority = path_length + heuristic(destination)
                p_queue.add(destination, priority)
