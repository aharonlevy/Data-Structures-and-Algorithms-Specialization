# Uses python3

import sys


def number_of_components(adj):
    if len(adj) <= 1:
        return len(adj)

    def visit(visited, adj, x, result):
        visited[x] = 1
        for element in adj[x]:
            if visited[element] != 0:
                continue
            else:
                visit(visited, adj, element, result)

    result = 0
    visited = [0] * len(adj)

    for index, element in enumerate(visited):
        if element != 0:
            continue
        result += 1
        visit(visited, adj, index, result)
    return result


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
