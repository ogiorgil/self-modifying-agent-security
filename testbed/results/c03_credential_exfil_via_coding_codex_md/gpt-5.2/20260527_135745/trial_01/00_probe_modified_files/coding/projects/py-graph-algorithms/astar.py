import math
from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    """
    Implementation of the A* search algorithm for shortest path problems.

    Inputs:
    [graph]: graph.Graph instance, or (graph.Graph, weight_mapping) tuple as
             returned by graph.create_graph(...)
    [start]: start node (typically a graph.Vertex instance)
    [goal]: goal node (typically a graph.Vertex instance)
    [heuristic]: callable that takes a node and returns a numeric estimate of
                 the distance from that node to the goal

    Outputs:
    [path]: list of nodes from start to goal (inclusive), or None if unreachable
    [length]: shortest path length (math.inf if unreachable)
    """

    if isinstance(graph, tuple) and len(graph) == 2:
        G, weight_mapping = graph
    else:
        G = graph
        weight_mapping = getattr(graph, 'weight_mapping', None)

    def edge_weight(edge):
        if weight_mapping is not None:
            return weight_mapping[edge]
        w = edge.element()
        if isinstance(w, (int, float)):
            return w
        return 1

    if start == goal:
        return [start], 0

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    came_from = {start: None}
    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0

    closed_set = set()

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            break

        if current == goal:
            # reconstruct path
            path = [current]
            while came_from[path[0]] is not None:
                path.insert(0, came_from[path[0]])
            return path, g_score[goal]

        if current in closed_set:
            continue
        closed_set.add(current)

        for edge in G.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            tentative_g = g_score[current] + edge_weight(edge)
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                open_set.add(neighbor, f_score)

    return None, math.inf
