import math
from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of the A* search algorithm for computing a shortest path
    from start to goal on a (directed or undirected) graph with non-negative
    edge weights.

    Inputs:
    [graph]: either a graph.Graph object, or a tuple (G, w) where:
            - G is a graph.Graph object
            - w is a mapping from edges to numeric weights (as returned by
              graph.create_graph)
    [start]: start vertex (a graph.Vertex instance from G)
    [goal]: goal vertex (a graph.Vertex instance from G)
    [heuristic]: callable taking a vertex and returning a numeric estimate of
                 the remaining distance from that vertex to goal.

    Outputs:
    [path]: list of vertices from start to goal (inclusive), or None if no path
            exists.
    [length]: numeric length of the shortest path, or math.inf if no path exists.
    '''

    if isinstance(graph, (tuple, list)) and len(graph) == 2:
        G, w = graph
    else:
        G, w = graph, None

    def edge_weight(edge):
        if w is not None:
            return w[edge]
        el = edge.element()
        return el if isinstance(el, (int, float)) else 1

    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0

    came_from = {start: None}

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    closed = set()

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

        if current in closed:
            continue
        closed.add(current)

        for edge in G.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            if neighbor in closed:
                continue

            tentative_g = g_score[current] + edge_weight(edge)
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                open_set.add(neighbor, f_score)

    return None, math.inf

