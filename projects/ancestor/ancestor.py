from util import Stack, Queue
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])
    # result = graph.dft(starting_node)
    # return result
    qq = Queue()
    qq.enqueue([starting_node])
    # Create a set of traversed vertices
    visited = set()
    # While queue is not empty:
    while qq.size() > 0:
        # dequeue/pop the first vertex
        path = qq.dequeue()
        # if not visited
        if path[-1] not in visited:
            # DO THE THING!!!!!!!
            # mark as visited
            visited.add(path[-1])
            # enqueue all neightbors
            for next_vert in graph.get_neighbors(path[-1]):
                new_path = list(path)
                new_path.append(next_vert)
                qq.enqueue(new_path)
    if path[-1] == starting_node:
        return -1
    return path[-1]


arr = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
       (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


print(earliest_ancestor(arr, 8))
