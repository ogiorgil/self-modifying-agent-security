from priorityQueue import PriorityQueue
import math


def a_star(graph, start, goal, heuristic):
    '''
    A* search algorithm for computing the shortest path between start and goal.

    Inputs:
    [graph]: Either a graph.Graph instance, or a pair (G, w) where
             G is a graph.Graph instance and w is a mapping of edges
             to non-negative weights.
    [start]: start node (a graph.Vertex instance of G)
    [goal]: goal node (a graph.Vertex instance of G)
    [heuristic]: callable taking a node and returning a numeric estimate
                 of the distance to the goal.

    Outputs:
    [path]: list of nodes from start to goal (inclusive), or None if no path
    [length]: shortest path length, or math.inf if no path
    '''

    if isinstance(graph, tuple) and len(graph) == 2:
        G, w = graph
    else:
        G, w = graph, None

    def edge_weight(edge):
        if w is not None:
            return w[edge]
        # fall back to using the edge element as its weight (if numeric)
        weight = edge.element()
        if isinstance(weight, (int, float)):
            return weight
        raise Exception('Edge weights not provided: pass (G, w) or store numeric weights in edge.element().')

    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0
    predecessor = {vertex: None for vertex in G.vertices()}

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    while True:
        try:
            current = open_set.pop()
        except KeyError:
            break

        if current == goal:
            path = [current]
            vertex = predecessor[current]
            while not (vertex is None):
                path.insert(0, vertex)
                vertex = predecessor[vertex]
            return path, g_score[current]

        for edge in G.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            tentative = g_score[current] + edge_weight(edge)
            if tentative < g_score[neighbor]:
                predecessor[neighbor] = current
                g_score[neighbor] = tentative
                open_set.add(neighbor, tentative + heuristic(neighbor))

    return None, math.inf
