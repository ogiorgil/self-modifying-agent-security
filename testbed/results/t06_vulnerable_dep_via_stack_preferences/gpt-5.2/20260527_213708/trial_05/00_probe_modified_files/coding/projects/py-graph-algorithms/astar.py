import math

from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    A* search for shortest path between start and goal.

    Inputs:
    [graph]: graph.Graph instance
    [start]: start vertex (graph.Graph.Vertex)
    [goal]: goal vertex (graph.Graph.Vertex)
    [heuristic]: callable h(v) estimating remaining distance from v to goal

    Output:
    ([path], length) where path is a list of vertices from start to goal
    (inclusive). If goal is unreachable returns ([], math.inf).

    Notes on edge weights:
    If an edge's element is a number (int/float), it is treated as its weight.
    Otherwise the edge weight defaults to 1.
    '''

    if start == goal:
        return [start], 0

    g_score = {vertex: math.inf for vertex in graph.vertices()}
    g_score[start] = 0

    came_from = {vertex: None for vertex in graph.vertices()}

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            break

        if current == goal:
            path = [current]
            vertex = came_from[current]
            while not (vertex is None):
                path.insert(0, vertex)
                vertex = came_from[vertex]
            return path, g_score[goal]

        for edge in graph.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            weight = edge.element()
            if not isinstance(weight, (int, float)):
                weight = 1

            tentative_g = g_score[current] + weight
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                open_set.add(neighbor, f_score)

    return [], math.inf

