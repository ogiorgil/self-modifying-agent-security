from priorityQueue import PriorityQueue
import math


def a_star(graph, start, goal, heuristic):
    '''
    A* search for shortest paths in a directed graph with non-negative weights.

    Inputs:
    [graph]: either a graph.Graph instance, or a (Graph, weight_mapping) tuple
             as returned by graph.create_graph().
    [start]: start node (graph.Vertex instance)
    [goal]: goal node (graph.Vertex instance)
    [heuristic]: callable taking a node and returning an estimate of the
                 remaining distance to the goal.

    Outputs:
    [path]: list of nodes from start to goal (inclusive). Empty if unreachable.
    [length]: shortest path length (math.inf if unreachable)
    '''

    if start == goal:
        return [start], 0

    if isinstance(graph, tuple) and len(graph) == 2:
        G, w = graph
    else:
        G, w = graph, None

    def edge_weight(edge):
        if w is None:
            return 1
        return w.get(edge, 1)

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
            # reconstruct path
            path = [current]
            while not (came_from[current] is None):
                current = came_from[current]
                path.insert(0, current)
            return path, g_score[goal]

        for edge in G.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            tentative_g = g_score[current] + edge_weight(edge)
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                open_set.add(neighbor, f_score)

    return [], math.inf

