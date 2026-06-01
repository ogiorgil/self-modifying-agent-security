import math
from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    A* search for shortest path on a (directed or undirected) graph.

    Inputs:
    [graph]: Either a graph.Graph instance or a tuple (G, w) where:
             - G is a graph.Graph instance
             - w is a mapping from edges to non-negative weights
             If w is not provided, all edges are assumed to have weight 1.
    [start]: start vertex (a graph.Graph.Vertex instance of G)
    [goal]: goal vertex (a graph.Graph.Vertex instance of G)
    [heuristic]: callable taking a vertex and returning a numeric estimate
                of remaining distance to the goal.

    Outputs:
    [path]: list of vertices from start to goal (inclusive). If goal is not
            reachable from start, path is an empty list.
    [length]: total path length (sum of edge weights). If goal is not
             reachable from start, length is math.inf.
    '''

    if isinstance(graph, tuple) and len(graph) == 2:
        G, w = graph
    else:
        G, w = graph, None

    if start == goal:
        return [start], 0

    def edge_weight(edge):
        if w is None:
            return 1
        return w[edge]

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    came_from = {}
    g_score = {vertex: math.inf for vertex in G.vertices()}
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

        if current in closed:
            continue
        closed.add(current)

        for edge in G.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            tentative = g_score[current] + edge_weight(edge)
            if tentative < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                open_set.add(neighbor, tentative + heuristic(neighbor))

    return [], math.inf

