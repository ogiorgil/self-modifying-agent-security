import math

from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    A* search for shortest path from start to goal.

    Inputs:
    [graph]: either a graph.Graph instance, or a tuple (G, w) where:
             - G is a graph.Graph instance
             - w is a mapping of edges to weights (like graph.create_graph output)
    [start]: start vertex (graph.Vertex)
    [goal]: goal vertex (graph.Vertex)
    [heuristic]: callable taking a vertex and returning a numeric estimate of
                 the remaining distance to the goal.

    Outputs:
    [path]: list of vertices from start to goal (inclusive), or None if no path
    [length]: total path length, or math.inf if no path exists
    '''

    if start == goal:
        return [start], 0

    if isinstance(graph, (tuple, list)) and len(graph) == 2 and isinstance(graph[1], dict):
        G, w = graph
    else:
        G = graph
        w = None

    open_set = PriorityQueue()
    came_from = {}

    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0

    try:
        f_start = heuristic(start)
    except Exception:
        f_start = 0

    open_set.add(start, f_start)

    closed_set = set()

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            break

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.insert(0, current)
            return path, g_score[goal]

        if current in closed_set:
            continue
        closed_set.add(current)

        for edge in G.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            if neighbor in closed_set:
                continue

            edge_weight = 1 if w is None else w[edge]
            tentative_g = g_score[current] + edge_weight

            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                open_set.add(neighbor, tentative_g + heuristic(neighbor))

    return None, math.inf

