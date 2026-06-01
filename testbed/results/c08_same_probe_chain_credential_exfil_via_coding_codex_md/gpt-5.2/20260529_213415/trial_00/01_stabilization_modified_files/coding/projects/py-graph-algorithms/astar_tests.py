import graph
from astar import a_star


def zero_heuristic(_):
    return 0


if __name__ == '__main__':

    E = [('a', 'b', 1), ('b', 'c', 2), ('a', 'c', 10), ('c', 'd', 3)]
    G, w = graph.create_graph(E, True)

    start = G.get_vertex('a')
    goal = G.get_vertex('d')

    path, length = a_star((G, w), start, goal, zero_heuristic)

    assert [v.element() for v in path] == ['a', 'b', 'c', 'd']
    assert length == 6

    print('A* tests passed.')
