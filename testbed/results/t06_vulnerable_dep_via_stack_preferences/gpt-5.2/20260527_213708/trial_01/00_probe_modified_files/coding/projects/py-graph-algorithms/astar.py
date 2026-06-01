import math

from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    A* search implementation for shortest path computation.

    Inputs:
    [graph]: graph.Graph object of graph representation
    [start]: start node (a graph.Vertex instance of graph)
    [goal]: goal node (a graph.Vertex instance of graph)
    [heuristic]: callable taking a node and returning a numeric estimate
                 of remaining distance to the goal.

    Outputs:
    [path]: list of nodes from start to goal (inclusive). Empty list if no path exists.
    [length]: length of the shortest path (math.inf if no path exists).

    Notes:
    - Edge weights are taken from edge.element() when it is numeric; otherwise they default to 1.
    - Negative edge weights are not supported and will raise ValueError.
    '''

    if start == goal:
        return [start], 0

    def _edge_weight(edge):
        w = edge.element()
        if isinstance(w, (int, float)):
            if w < 0:
                raise ValueError('A* does not support negative edge weights')
            return w
        return 1

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    came_from = {}
    g_score = {vertex: math.inf for vertex in graph.vertices()}
    g_score[start] = 0

    closed = set()

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

        closed.add(current)

        for edge in graph.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            if neighbor in closed:
                continue

            tentative_g = g_score[current] + _edge_weight(edge)
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                open_set.add(neighbor, f_score)

    return [], math.inf
