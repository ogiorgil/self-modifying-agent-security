import heapq
import math


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing a shortest path between
    two vertices in a graph with non-negative edge weights.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex for the search
    [goal]: the destination vertex for the search
    [heuristic]: callable that accepts a vertex and returns an estimate
                 of the remaining distance to the goal

    Outputs:
    [path]: list of vertices from start to goal. Empty if goal is unreachable.
    [path_length]: length of the shortest path, or math.inf if unreachable.
    '''

    distance_est = {vertex: math.inf for vertex in graph.vertices()}
    distance_est[start] = 0
    predecessor = {vertex: None for vertex in graph.vertices()}
    frontier = []
    counter = 0

    heapq.heappush(frontier, (heuristic(start), counter, start))

    while frontier:
        _, _, source = heapq.heappop(frontier)

        if source == goal:
            return _reconstruct_path(predecessor, start, goal), distance_est[goal]

        for edge in graph.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            new_distance = distance_est[source] + _edge_weight(edge)
            if distance_est[destination] > new_distance:
                distance_est[destination] = new_distance
                predecessor[destination] = source
                counter += 1
                priority = new_distance + heuristic(destination)
                heapq.heappush(frontier, (priority, counter, destination))

    return [], math.inf


def _edge_weight(edge):
    '''
    Return an edge's numeric weight, or 1 for unweighted graph edges.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
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
