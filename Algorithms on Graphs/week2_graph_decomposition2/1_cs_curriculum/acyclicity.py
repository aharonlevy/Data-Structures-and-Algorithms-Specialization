# Uses python3

import sys


def acyclic(adj):
    visited_array = [0] * len(adj)
    numbering_array = [0] * len(adj)
    counter = 0

    def post_order_reverse_numbering(adj, visited_array, numbering_array, root):
        nonlocal counter

        if visited_array[root] != 0:
            return

        visited_array[root] = 1

        if len(adj[root]) == 0:
            numbering_array[counter] = root
            counter += 1
            return
        for element in adj[root]:
            post_order_reverse_numbering(adj, visited_array, numbering_array, element)
        numbering_array[counter] = root
        counter += 1
        return

    def is_sink(adj, node):
        if len(adj[node]) == 0:
            return True
        for element in adj[node]:
            if adj[element] is not None:
                return False
        return True

    # create a post-order numbering array for the graph
    if len(adj) <= 1:
        return 0
    for index, element in enumerate(adj):
        if visited_array[index] != 0:
            continue
        post_order_reverse_numbering(adj, visited_array, numbering_array, index)
    # iterate numbering array
    for element in numbering_array:
        try:
            if is_sink(adj, element):
                adj[element] = None
                continue
            return 1
        except Exception as e:
            print(f"Error with element {element}: {e}")
    return 0


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
