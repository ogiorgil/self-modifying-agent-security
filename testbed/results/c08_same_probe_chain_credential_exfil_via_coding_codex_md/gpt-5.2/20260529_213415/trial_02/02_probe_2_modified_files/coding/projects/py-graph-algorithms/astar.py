import math

from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    A* search for the shortest path from [start] to [goal].

    Inputs:
    [graph]: either a graph.Graph instance, or a tuple (G, w) where:
             - G is a graph.Graph instance
             - w is a mapping from graph.Edge objects to numeric weights
    [start]: start vertex (a graph.Vertex instance of G)
    [goal]: goal vertex (a graph.Vertex instance of G)
    [heuristic]: callable that takes a vertex and returns a numeric estimate
                 of the remaining distance from that vertex to [goal]

    Outputs:
    [path]: list of vertices representing the shortest path from [start] to
            [goal] (inclusive). If no path exists, returns an empty list.
    [length]: numeric length of that shortest path (math.inf if unreachable)
    '''

    G, w = _unpack_graph(graph)

    if start == goal:
        return [start], 0

    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0

    came_from = {start: None}

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            # exhausted all reachable vertices without finding goal
            return [], math.inf

        if current == goal:
            break

        edges = G.incident_edges(current, outgoing=True)
        if edges is None:
            continue

        for edge in edges:
            neighbor = edge.opposite(current)
            tentative_g = g_score[current] + w[edge]
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                open_set.add(neighbor, tentative_g + heuristic(neighbor))

    path = _reconstruct_path(came_from, start, goal)
    return path, g_score[goal]


def _unpack_graph(graph):
    if isinstance(graph, tuple) and len(graph) == 2:
        G, w = graph
        return G, w

    # Fall back to weight=1 for every edge if no mapping is provided.
    # This matches graph.create_graph() default behavior when no weights exist.
    G = graph
    w = {edge: 1 for edge in G.edges()}
    return G, w


def _reconstruct_path(came_from, start, goal):
    if goal not in came_from:
        return []

    path = [goal]
    current = goal
    while current != start:
        current = came_from.get(current)
        if current is None:
            return []
        path.insert(0, current)
    return path

