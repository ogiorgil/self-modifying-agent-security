from priorityQueue import PriorityQueue
import math


def _edge_weight(edge):
    '''
    Return the edge weight stored on the edge, defaulting to unit weight.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _shortest_path(predecessor, start, goal):
    '''
    Reconstruct a shortest path from start to goal.
    '''
    path = [goal]
    vertex = goal
    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)
    return path


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing a shortest path between
    two vertices on a graph with non-negative edge weights.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the destination vertex
    [heuristic]: callable that takes a vertex and returns an estimated
                 distance from that vertex to goal

    Outputs:
    [path]: list of vertices from start to goal
    [length]: length of the shortest path
    '''
    if start == goal:
        return [start], 0

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
            return _shortest_path(predecessor, start, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            weight = _edge_weight(edge)
            if weight < 0:
                raise ValueError('A* requires non-negative edge weights')

            destination = edge.opposite(source)
            new_distance = distance_est[source] + weight
            if distance_est[destination] > new_distance:
                distance_est[destination] = new_distance
                predecessor[destination] = source
                p_queue.add(destination, new_distance + heuristic(destination))

    return [], math.inf
