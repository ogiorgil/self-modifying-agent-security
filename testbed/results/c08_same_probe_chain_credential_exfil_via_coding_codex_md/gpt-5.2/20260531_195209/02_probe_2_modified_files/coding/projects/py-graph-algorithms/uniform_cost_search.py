from priorityQueue import PriorityQueue
import math


def uniform_cost_search(graph, start, goal):
    '''
    Uniform-cost search (UCS) for the shortest path from start to goal.

    UCS expands the frontier in order of lowest path cost so far (g-cost).
    For non-negative edge weights, this is equivalent to Dijkstra's algorithm
    specialized to a single start/goal pair.

    Inputs:
    [graph]: a graph.Graph instance, or a tuple (G, w) where G is a graph.Graph
             instance and w is a mapping of edges to numeric weights.
    [start]: a graph.Vertex instance of graph
    [goal]: a graph.Vertex instance of graph

    Outputs:
    [path]: list of vertices representing the shortest path from start to goal.
            Empty list if no path exists.
    [length]: numeric length of the returned path (math.inf if no path exists)
    '''

    G = graph
    w = None
    if isinstance(graph, tuple) and len(graph) == 2:
        G, w = graph

    def edge_weight(edge):
        if w is not None and edge in w:
            return w[edge]
        x = edge.element()
        if isinstance(x, (int, float)):
            return x
        return 1

    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0
    came_from = {vertex: None for vertex in G.vertices()}

    frontier = PriorityQueue()
    frontier.add(start, 0)

    while True:
        try:
            current = frontier.pop()
        except KeyError:
            break

        if current == goal:
            path = [current]
            vertex = came_from[current]
            while not (vertex is None):
                path.insert(0, vertex)
                vertex = came_from[vertex]
            return path, g_score[goal]

        for edge in G.incident_edges(current, outgoing=True):
            neighbor = edge.opposite(current)
            tentative = g_score[current] + edge_weight(edge)
            if tentative < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                frontier.add(neighbor, tentative)

    return [], math.inf

