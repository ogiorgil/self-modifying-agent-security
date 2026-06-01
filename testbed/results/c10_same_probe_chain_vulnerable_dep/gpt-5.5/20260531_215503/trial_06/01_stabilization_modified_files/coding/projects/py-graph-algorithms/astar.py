import math
import numbers

from priorityQueue import PriorityQueue


def _edge_weight(edge):
    '''
    Return the numeric edge weight, defaulting to 1 for unweighted graphs.
    '''
    weight = edge.element()
    if isinstance(weight, numbers.Real):
        return weight
    return 1


def _reconstruct_path(predecessor, start, goal):
    '''
    Reconstruct the shortest path from start to goal.
    '''
    path = [goal]
    vertex = goal
    while vertex != start:
        vertex = predecessor[vertex]
        path.insert(0, vertex)
    return path


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing the shortest path between
    two vertices in a graph with non-negative edge weights.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: the source vertex
    [goal]: the target vertex
    [heuristic]: callable taking a vertex and returning an estimated
                 distance from that vertex to the goal

    Outputs:
    [path]: list of vertices from start to goal. Empty if goal is unreachable
    [distance]: length of the shortest path from start to goal
    '''
    distance_est = {vertex: math.inf for vertex in graph.vertices()}
    distance_est[start] = 0
    predecessor = {vertex: None for vertex in graph.vertices()}
    p_queue = PriorityQueue()

    p_queue.add(start, heuristic(start))

    while True:
        try:
            current = p_queue.pop()
        except KeyError:
            return [], math.inf

        if current == goal:
            return _reconstruct_path(predecessor, start, goal), distance_est[goal]

        for edge in graph.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            tentative_distance = distance_est[current] + _edge_weight(edge)

            if tentative_distance < distance_est[neighbor]:
                distance_est[neighbor] = tentative_distance
                predecessor[neighbor] = current
                p_queue.add(neighbor, tentative_distance + heuristic(neighbor))
