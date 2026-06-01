import math

from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    """
    A* shortest path search on an unweighted graph.

    Inputs:
    [graph]: graph.Graph instance
    [start]: graph.Vertex instance (must belong to graph)
    [goal]: graph.Vertex instance (must belong to graph)
    [heuristic]: callable taking a vertex and returning a numeric estimate of
                 the distance to the goal

    Outputs:
    [path]: list of vertices, from start to goal (inclusive). Empty if no path.
    [length]: length of the path (number of edges). math.inf if no path.
    """

    if start == goal:
        return [start], 0

    if start not in graph.vertices() or goal not in graph.vertices():
        raise ValueError("start and goal must be vertices in graph")

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
            previous = came_from[current]
            while previous is not None:
                path.insert(0, previous)
                previous = came_from[previous]
            return path, g_score[goal]

        for edge in graph.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            tentative_g = g_score[current] + 1
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                open_set.add(neighbor, tentative_g + heuristic(neighbor))

    return [], math.inf
