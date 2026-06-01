import heapq
import itertools
import math


def a_star(graph, start, goal, heuristic):
    '''
    Compute the shortest path from start to goal using A* search.

    Inputs:
    [graph]: graph.Graph object or adjacency mapping. For graph.Graph objects,
             numeric edge elements are used as weights and non-numeric edge
             elements are treated as unweighted edges of length 1.
    [start]: the source node.
    [goal]: the target node.
    [heuristic]: callable taking a node and returning an estimate of the
                 remaining distance to goal.

    Outputs:
    [path]: list of nodes from start to goal. Empty when goal is unreachable.
    [distance]: length of the shortest path, or math.inf when unreachable.
    '''
    if start == goal:
        return [start], 0

    open_set = []
    counter = itertools.count()
    heapq.heappush(open_set, (heuristic(start), next(counter), 0, start))

    distance_est = {start: 0}
    predecessor = {start: None}

    while open_set:
        _, _, current_distance, current = heapq.heappop(open_set)
        if current_distance != distance_est[current]:
            continue

        if current == goal:
            return _reconstruct_path(predecessor, goal), current_distance

        for neighbor, edge_weight in _neighbors(graph, current):
            if edge_weight < 0:
                raise ValueError('A* search requires non-negative edge weights')

            new_distance = current_distance + edge_weight
            if new_distance < distance_est.get(neighbor, math.inf):
                distance_est[neighbor] = new_distance
                predecessor[neighbor] = current
                priority = new_distance + heuristic(neighbor)
                heapq.heappush(open_set,
                               (priority, next(counter), new_distance, neighbor))

    return [], math.inf


def _reconstruct_path(predecessor, goal):
    '''
    Reconstruct a shortest path from the predecessor mapping.
    '''
    path = []
    current = goal
    while current is not None:
        path.insert(0, current)
        current = predecessor[current]
    return path


def _neighbors(graph, node):
    '''
    Yield (neighbor, weight) pairs for graph.Graph objects and mappings.
    '''
    if hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(node, outgoing=True):
            yield edge.opposite(node), _graph_edge_weight(edge)
    else:
        for neighbor, weight in _mapping_neighbors(graph, node):
            yield neighbor, weight


def _graph_edge_weight(edge):
    '''
    Return the numeric weight stored on a graph.Edge, defaulting to 1.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight
    return 1


def _mapping_neighbors(graph, node):
    '''
    Yield neighbors from common adjacency mapping shapes.
    '''
    adjacency = graph.get(node, {})
    if isinstance(adjacency, dict):
        for neighbor, weight in adjacency.items():
            yield neighbor, weight
    else:
        for entry in adjacency:
            if isinstance(entry, dict):
                yield entry['to'], entry.get('weight', 1)
            elif isinstance(entry, (list, tuple)):
                yield entry[0], entry[1]
            else:
                yield entry, 1
