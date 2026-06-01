from priorityQueue import PriorityQueue
import math


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm.
    Computes the shortest path between start and goal using a heuristic
    estimate of the remaining distance.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex.
    [goal]: the destination vertex.
    [heuristic]: callable that takes a vertex and returns an estimate of
                 the distance from that vertex to goal.

    Outputs:
    [path]: list of vertices from start to goal. Empty if goal is unreachable.
    [path_length]: length of the shortest path, or math.inf if unreachable.
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
            new_distance = distance_est[source] + _edge_weight(edge)
            if distance_est[destination] > new_distance:
                distance_est[destination] = new_distance
                predecessor[destination] = source
                p_queue.add(destination, new_distance + heuristic(destination))

    return [], math.inf


def _edge_weight(edge):
    '''
    Return the numeric weight stored on edge, defaulting to 1.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _reconstruct_path(predecessor, start, goal):
    '''
    Build the path from start to goal using the predecessor mapping.
    '''
    path = [goal]
    vertex = goal
    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)
    return path
