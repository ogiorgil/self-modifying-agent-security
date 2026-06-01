from priorityQueue import PriorityQueue
import math
import numbers


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm for finding the shortest
    path between two vertices.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex.
    [goal]: the destination vertex.
    [heuristic]: callable that takes a vertex and returns an estimate of
                 the distance from that vertex to the goal.

    Outputs:
    [path]: list of vertices on the shortest path from start to goal.
    [length]: length of the shortest path from start to goal.
    '''

    distance_est = {vertex: math.inf for vertex in graph.vertices()}
    predecessor = {vertex: None for vertex in graph.vertices()}
    distance_est[start] = 0

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
            edge_length = _edge_length(edge)
            if edge_length < 0:
                raise ValueError('A* search does not support negative edge weights')

            candidate_distance = distance_est[source] + edge_length
            if distance_est[destination] > candidate_distance:
                distance_est[destination] = candidate_distance
                predecessor[destination] = source
                p_queue.add(destination, candidate_distance + heuristic(destination))

    return [], math.inf


def _edge_length(edge):
    '''
    Return the numeric length stored on edge, or 1 for unweighted graphs.
    '''
    element = edge.element()
    if isinstance(element, numbers.Number):
        return element
    return 1


def _reconstruct_path(predecessor, start, goal):
    '''
    Reconstruct a path from a predecessor mapping.
    '''
    path = [goal]
    vertex = goal
    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)

    return path
