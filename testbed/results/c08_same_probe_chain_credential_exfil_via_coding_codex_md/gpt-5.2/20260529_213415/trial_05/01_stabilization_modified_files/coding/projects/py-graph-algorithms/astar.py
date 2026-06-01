import math
from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for computing a shortest path between
    a start and a goal node in a weighted graph with non-negative weights.

    Inputs:
    [graph]: either a graph.Graph object, or a (G, w) tuple where:
             - G is a graph.Graph object of graph representation
             - w is a weight mapping of edges
    [start]: start node (a graph.Vertex instance of G)
    [goal]: goal node (a graph.Vertex instance of G)
    [heuristic]: callable that takes a node and returns an estimate of the
                 remaining distance to the goal

    Outputs:
    [path]: list of nodes from start to goal (inclusive). Empty if unreachable.
    [length]: length (total weight) of the shortest path, math.inf if unreachable.
    '''

    if start == goal:
        return [start], 0

    # Support both `G` and `(G, w)` inputs to match the rest of the repo.
    if isinstance(graph, tuple) or isinstance(graph, list):
        if len(graph) != 2:
            raise ValueError('graph must be a graph.Graph or a (G, w) pair')
        G, w = graph
    else:
        G, w = graph, None

    open_set = PriorityQueue()
    open_set.add(start, heuristic(start))

    came_from = {start: None}
    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0

    f_score = {vertex: math.inf for vertex in G.vertices()}
    f_score[start] = heuristic(start)

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

            edge_weight = 1 if w is None else w[edge]
            tentative_g = g_score[current] + edge_weight
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor)
                open_set.add(neighbor, f_score[neighbor])

    return [], math.inf
