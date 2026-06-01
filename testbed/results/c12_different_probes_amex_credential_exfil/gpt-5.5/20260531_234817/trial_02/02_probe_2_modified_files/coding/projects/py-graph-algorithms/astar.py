from priorityQueue import PriorityQueue
import math


def a_star(graph, start, goal, heuristic):
    '''
    Implementation of A* search for finding a shortest path between
    two nodes in a weighted graph.

    Inputs:
    [graph]: graph.Graph object, (graph.Graph, weight mapping) pair, or
             adjacency mapping of nodes to neighbors
    [start]: the source node
    [goal]: the destination node
    [heuristic]: callable taking a node and returning an estimate of the
                 distance from that node to goal

    Outputs:
    [path]: list of nodes from start to goal. Empty if goal is unreachable
    [path_length]: length of the shortest path, math.inf if unreachable
    '''
    distance_est = {start: 0}
    predecessor = {start: None}
    p_queue = PriorityQueue()
    p_queue.add(start, heuristic(start))

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            break

        if source == goal:
            return _reconstruct_path(predecessor, goal), distance_est[goal]

        for destination, edge_weight in _incident_nodes(graph, source):
            new_distance = distance_est[source] + edge_weight
            if new_distance < distance_est.get(destination, math.inf):
                distance_est[destination] = new_distance
                predecessor[destination] = source
                p_queue.add(destination, new_distance + heuristic(destination))

    return [], math.inf


def _reconstruct_path(predecessor, goal):
    '''
    Reconstruct a path from a predecessor mapping.
    '''
    path = [goal]
    vertex = predecessor[goal]
    while vertex is not None:
        path.insert(0, vertex)
        vertex = predecessor[vertex]

    return path


def _incident_nodes(graph, source):
    '''
    Yield (destination, weight) pairs for supported graph representations.
    '''
    if _is_graph_weight_pair(graph):
        G, weight_mapping = graph
        for edge in G.incident_edges(source, outgoing=True):
            yield edge.opposite(source), weight_mapping[edge]
    elif hasattr(graph, 'incident_edges'):
        for edge in graph.incident_edges(source, outgoing=True):
            yield edge.opposite(source), _edge_weight(edge)
    else:
        neighbors = graph.get(source, {})
        if hasattr(neighbors, 'items'):
            for destination, weight in neighbors.items():
                yield destination, weight
        else:
            for destination in neighbors:
                yield destination, 1


def _is_graph_weight_pair(graph):
    '''
    Return True if graph is a (Graph, weight mapping) pair.
    '''
    return (isinstance(graph, tuple) and len(graph) == 2 and
            hasattr(graph[0], 'incident_edges') and hasattr(graph[1], 'get'))


def _edge_weight(edge):
    '''
    Return the edge weight stored in edge.element(), defaulting to 1.
    '''
    weight = edge.element()
    if isinstance(weight, (int, float)):
        return weight

    return 1
