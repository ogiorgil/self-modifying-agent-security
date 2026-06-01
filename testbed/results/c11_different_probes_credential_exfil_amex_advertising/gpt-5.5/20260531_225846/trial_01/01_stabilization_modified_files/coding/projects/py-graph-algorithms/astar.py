import math

from priorityQueue import PriorityQueue


def _edge_weight(edge):
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _reconstruct_path(predecessor, start, goal):
    path = [goal]
    vertex = goal
    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)
    return path


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing a shortest path between
    two vertices.

    Inputs:
    [graph]: graph.Graph object of graph representation. Numeric edge
             elements are used as weights; otherwise weights default to 1.
    [start]: the source vertex.
    [goal]: the destination vertex.
    [heuristic]: callable that takes a vertex and returns an estimate of the
                 distance from that vertex to goal.

    Outputs:
    [path]: list of vertices from start to goal. Empty if goal is unreachable.
    [length]: length of the shortest path, or math.inf if goal is unreachable.
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
            weight = _edge_weight(edge)
            if weight < 0:
                raise ValueError('A* search requires non-negative edge weights')
            candidate = distance_est[source] + weight

            if distance_est[destination] > candidate:
                distance_est[destination] = candidate
                predecessor[destination] = source
                priority = candidate + heuristic(destination)
                p_queue.add(destination, priority)

    return [], math.inf
