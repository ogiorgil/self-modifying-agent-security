from priorityQueue import PriorityQueue
import math


def a_star(graph, start, goal, heuristic):
    '''
    A* search implementation for computing shortest path on a graph.

    Inputs:
    [graph]: either a graph.Graph instance, or a tuple (G, w) where
             G is a graph.Graph instance and w is a weight mapping of edges.
    [start]: the source vertex (graph.Vertex instance of G)
    [goal]: the target vertex (graph.Vertex instance of G)
    [heuristic]: callable h(v) that estimates the distance from v to goal

    Outputs:
    [path]: list of vertices in the shortest path from start to goal
           (empty list if goal is unreachable)
    [length]: length of the shortest path (math.inf if goal is unreachable)
    '''

    if isinstance(graph, tuple) or isinstance(graph, list):
        if len(graph) != 2:
            raise ValueError('graph must be a Graph or a tuple (G, w)')
        G, w = graph
    else:
        G = graph
        w = None

    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0
    came_from = {vertex: None for vertex in G.vertices()}

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))
    closed_set = set()

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            break

        if current in closed_set:
            continue
        closed_set.add(current)

        if current == goal:
            path = [goal]
            v = came_from[goal]
            while not (v is None):
                path.insert(0, v)
                v = came_from[v]
            return path, g_score[goal]

        for edge in G.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            cost = w[edge] if not (w is None) else 1
            tentative_g = g_score[current] + cost

            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                open_set.add(neighbor, f_score)

    return [], math.inf
