import math
from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    A* search for shortest path between start and goal.

    Inputs:
    [graph]: either a graph.Graph instance, or a tuple (G, w) where
             G is a graph.Graph instance and w is a mapping of edges to
             weights (as returned by graph.create_graph).
             If no weight mapping is provided, each edge defaults to weight 1.
    [start]: start node (typically a graph.Graph.Vertex)
    [goal]: goal node (typically a graph.Graph.Vertex)
    [heuristic]: callable taking a node and returning a numeric estimate
                 of the distance from that node to the goal.

    Outputs:
    [path]: a list of nodes from start to goal (inclusive). If no path exists,
            returns None.
    [length]: the length (total weight) of the shortest path. If no path exists,
              returns math.inf.
    '''

    if isinstance(graph, tuple) and len(graph) == 2:
        G, w = graph
    else:
        G, w = graph, None

    def edge_weight(edge):
        if w is not None:
            return w[edge]
        try:
            val = edge.element()
            if isinstance(val, (int, float)):
                return val
        except Exception:
            pass
        return 1

    open_set = PriorityQueue()
    came_from = {start: None}

    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0

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

    return None, math.inf

