import math
from priorityQueue import PriorityQueue


def _edge_weight(edge):
    '''
    Return the numeric edge weight, defaulting to 1 for unweighted edges.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _reconstruct_path(predecessor, start, goal):
    '''
    Return the path from start to goal using a predecessor mapping.
    '''
    path = [goal]
    vertex = goal
    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)
    return path


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for shortest path between two vertices.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the destination vertex
    [heuristic]: callable that takes a vertex and returns a numeric estimate
                 of the distance from that vertex to the goal

    Outputs:
    [path]: list of vertices from start to goal. Empty if no path exists.
    [path_length]: length of the shortest path, or math.inf if no path exists.
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
            tentative_distance = distance_est[source] + _edge_weight(edge)

            if tentative_distance < distance_est[destination]:
                distance_est[destination] = tentative_distance
                predecessor[destination] = source
                p_queue.add(destination,
                            tentative_distance + heuristic(destination))

    return [], math.inf
