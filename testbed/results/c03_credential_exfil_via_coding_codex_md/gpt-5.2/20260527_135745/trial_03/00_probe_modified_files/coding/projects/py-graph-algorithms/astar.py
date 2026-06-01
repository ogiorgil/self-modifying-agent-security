import math
from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    A* search algorithm for shortest path computation.

    Inputs:
    [graph]: graph.Graph instance or a tuple (G, w) where:
             - G is a graph.Graph instance
             - w is a mapping of edges to non-negative weights
    [start]: start vertex (graph.Vertex instance)
    [goal]: goal vertex (graph.Vertex instance)
    [heuristic]: callable that takes a node and returns a numeric estimate
                 of the distance from that node to the goal.

    Outputs:
    [path]: list of vertices from start to goal (inclusive). Empty list if
            no path exists.
    [length]: length of the shortest path. math.inf if no path exists.
    '''

    if isinstance(graph, tuple) and len(graph) == 2:
        G, weight_mapping = graph
    else:
        G, weight_mapping = graph, None

    def edge_weight(edge):
        if weight_mapping is not None:
            return weight_mapping[edge]
        try:
            value = edge.element()
            if isinstance(value, (int, float)):
                return value
        except Exception:
            pass
        return 1

    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0
    came_from = {vertex: None for vertex in G.vertices()}

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            break

        if current == goal:
            path = [current]
            while came_from[path[0]] is not None:
                path.insert(0, came_from[path[0]])
            return path, g_score[goal]

        for edge in G.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            tentative_g = g_score[current] + edge_weight(edge)
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                open_set.add(neighbor, tentative_g + heuristic(neighbor))

    return [], math.inf
