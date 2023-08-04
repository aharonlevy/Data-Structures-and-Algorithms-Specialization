# Uses python3

import sys


def dfs(adj, used, order, x):
    if used[x] != 0:
        return
    used[x] = 1
    if len(adj[x]) == 0:
        order.append(x)
        return
    for element in adj[x]:
        dfs(adj, used, order, element)
    order.append(x)
    return


def toposort(adj):
    used = [0] * len(adj)
    order = []
    for element in range(len(adj)):
        dfs(adj, used, order, element)
    # write your code here
    return reversed(order)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=" ")
