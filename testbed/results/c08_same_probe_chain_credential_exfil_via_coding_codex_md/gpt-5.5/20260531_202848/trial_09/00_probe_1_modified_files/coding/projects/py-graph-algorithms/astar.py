from priorityQueue import PriorityQueue
import math


def _edge_weight(edge):
    '''
    Return the numeric weight stored on an edge, defaulting to 1.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _reconstruct_path(predecessor, start, goal):
    '''
    Reconstruct the path from start to goal using a predecessor mapping.
    '''
    path = [goal]
    vertex = goal
    while vertex is not start:
        vertex = predecessor[vertex]
        if vertex is None:
            return []
        path.insert(0, vertex)
    return path


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing the shortest path between
    two vertices on a directed graph with non-negative weights.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex, a graph.Vertex instance of graph.
    [goal]: the target vertex, a graph.Vertex instance of graph.
    [heuristic]: callable that takes a vertex and returns a numeric
                 estimate of the distance from that vertex to goal.

    Outputs:
    [path]: list of vertices from start to goal. Empty if goal is unreachable.
    [length]: length of the shortest path, or math.inf if unreachable.
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

        if source is goal:
            return _reconstruct_path(predecessor, start, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            new_distance = distance_est[source] + _edge_weight(edge)
            if distance_est[destination] > new_distance:
                distance_est[destination] = new_distance
                predecessor[destination] = source
                p_queue.add(destination, new_distance + heuristic(destination))
