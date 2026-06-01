from priorityQueue import PriorityQueue
import math


def _edge_weight(edge):
    '''
    Return the numeric weight stored on edge, defaulting to unit cost.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing the shortest path between
    start and goal.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex from which the shortest path is computed
    [goal]: the destination vertex
    [heuristic]: callable taking a vertex and returning an estimated
                 distance to goal

    Outputs:
    [path]: list of vertices on the shortest path from start to goal
    [path_length]: length of the shortest path
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
            path = []
            vertex = goal
            while vertex is not None:
                path.insert(0, vertex)
                vertex = predecessor[vertex]
            return path, distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            new_distance = distance_est[source] + _edge_weight(edge)
            if distance_est[destination] > new_distance:
                distance_est[destination] = new_distance
                predecessor[destination] = source
                priority = new_distance + heuristic(destination)
                p_queue.add(destination, priority)
