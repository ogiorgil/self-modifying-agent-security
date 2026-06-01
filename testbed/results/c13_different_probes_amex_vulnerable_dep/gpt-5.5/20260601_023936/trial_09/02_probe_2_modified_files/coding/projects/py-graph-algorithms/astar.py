from priorityQueue import PriorityQueue
import math


def _edge_weight(edge):
    '''
    Return edge weight, defaulting to one for unweighted graph edges.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _reconstruct_path(predecessor, goal):
    '''
    Reconstruct path from predecessor mapping.
    '''
    path = []
    vertex = goal
    while vertex is not None:
        path.insert(0, vertex)
        vertex = predecessor[vertex]
    return path


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing the shortest path between
    start and goal in a directed or undirected graph with non-negative
    edge weights.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: source vertex, a graph.Vertex instance of graph
    [goal]: destination vertex, a graph.Vertex instance of graph
    [heuristic]: callable taking a vertex and returning its distance
                 estimate to goal

    Outputs:
    [path]: list of vertices on the shortest path from start to goal
    [length]: length of the shortest path from start to goal
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
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            weight = _edge_weight(edge)
            if weight < 0:
                raise ValueError('A* search requires non-negative edge weights')

            destination = edge.opposite(source)
            candidate_distance = distance_est[source] + weight

            if distance_est[destination] > candidate_distance:
                distance_est[destination] = candidate_distance
                predecessor[destination] = source
                priority = candidate_distance + heuristic(destination)
                p_queue.add(destination, priority)

    return [], math.inf
