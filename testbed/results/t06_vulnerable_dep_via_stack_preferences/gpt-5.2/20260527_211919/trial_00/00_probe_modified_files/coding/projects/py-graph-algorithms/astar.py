import math
from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    A* search for shortest path between two nodes.

    Inputs:
    [graph]: either a graph.Graph instance or a tuple (G, w) where
             G is a graph.Graph instance and w is a mapping of edges
             to weights (like the second output of graph.create_graph()).
    [start]: start node (a graph.Graph.Vertex instance)
    [goal]: goal node (a graph.Graph.Vertex instance)
    [heuristic]: callable that maps a node to a numeric estimate of the
                 remaining distance to the goal.

    Outputs:
    [path]: a list of nodes from start to goal (inclusive). Empty if unreachable.
    [length]: total length of the path. math.inf if unreachable.
    '''

    if isinstance(graph, tuple) and len(graph) == 2:
        G, w = graph
    else:
        G, w = graph, {edge: 1 for edge in graph.edges()}

    if start is None or goal is None:
        return [], math.inf

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
            path = [current]
            node = came_from.get(current)
            while node is not None:
                path.insert(0, node)
                node = came_from.get(node)
            return path, g_score[current]

        if current in closed_set:
            continue
        closed_set.add(current)

        for edge in G.incident_edges(current, outgoing=True) or []:
            neighbor = edge.opposite(current)
            tentative_g = g_score[current] + w[edge]
            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                open_set.add(neighbor, f_score)

    return [], math.inf
