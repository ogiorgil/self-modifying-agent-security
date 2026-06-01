import math
from priorityQueue import PriorityQueue


def a_star(graph, start, goal, heuristic):
    '''
    A* search for shortest path between start and goal.

    Inputs:
    [graph]: either a graph.Graph instance, or a tuple (G, w) where
             G is a graph.Graph instance and w is a mapping edge -> weight.
    [start]: start node (graph.Vertex)
    [goal]: goal node (graph.Vertex)
    [heuristic]: callable that takes a node and returns a numeric estimate
                 of the remaining distance to the goal.

    Outputs:
    [path]: list of nodes from start to goal (inclusive). Empty if unreachable.
    [length]: numeric length of the shortest path. math.inf if unreachable.
    '''

    if isinstance(graph, tuple) and len(graph) == 2:
        G, w = graph
    else:
        G, w = graph, None

    def edge_cost(edge):
        if w is not None:
            return w[edge]
        cost = edge.element()
        if isinstance(cost, (int, float)):
            return cost
        return 1

    open_set = PriorityQueue()
    came_from = {start: None}

    g_score = {vertex: math.inf for vertex in G.vertices()}
    g_score[start] = 0

    f_start = heuristic(start)
    open_set.add(start, f_start)

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
            tentative_g = g_score[current] + edge_cost(edge)
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                open_set.add(neighbor, f_score)

    return [], math.inf
