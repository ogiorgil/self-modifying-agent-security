import math

from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    A* search algorithm for computing the shortest path from start to goal.

    Inputs:
    [graph]: graph.Graph object
    [start]: start node (a graph.Vertex instance of graph)
    [goal]: goal node (a graph.Vertex instance of graph)
    [heuristic]: callable h(node) returning a numeric estimate of the
                 remaining distance from node to goal

    Outputs:
    [path]: list of nodes from start to goal (inclusive). Empty list if
            goal is unreachable from start.
    [length]: length of the shortest path. math.inf if unreachable.
    '''

    if start == goal:
        return [start], 0

    open_set = PriorityQueue()
    came_from = {}

    g_score = {vertex: math.inf for vertex in graph.vertices()}
    g_score[start] = 0

    f_start = heuristic(start)
    if f_start is None:
        f_start = 0
    open_set.add(start, f_start)

    closed = set()

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            break

        if current in closed:
            continue
        closed.add(current)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.insert(0, current)
            return path, g_score[goal]

        edges = graph.incident_edges(current, outgoing=True)
        if edges is None:
            continue

        for edge in edges:
            neighbor = edge.opposite(current)
            weight = edge.element()
            try:
                step_cost = float(weight)
            except (TypeError, ValueError):
                step_cost = 1

            tentative_g = g_score[current] + step_cost
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                h_val = heuristic(neighbor)
                if h_val is None:
                    h_val = 0
                f_score = tentative_g + float(h_val)
                open_set.add(neighbor, f_score)

    return [], math.inf
