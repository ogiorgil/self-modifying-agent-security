import math
from numbers import Number

from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing the shortest path between
    two vertices in a graph with non-negative edge weights.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the destination vertex
    [heuristic]: callable that takes a vertex and returns an estimated
                 distance from that vertex to the goal

    Outputs:
    [path]: list of vertices from start to goal. Empty if goal is unreachable
    [length]: length of the shortest path. math.inf if goal is unreachable
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
    Return numeric edge weight, defaulting to 1 for unweighted edges.
    '''
    weight = edge.element()
    if isinstance(weight, Number):
        return weight
    return 1


def _reconstruct_path(predecessor, start, goal):
    '''
    Build a shortest path list from the predecessor mapping.
    '''
    path = [goal]
    vertex = goal
    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)
    return path
