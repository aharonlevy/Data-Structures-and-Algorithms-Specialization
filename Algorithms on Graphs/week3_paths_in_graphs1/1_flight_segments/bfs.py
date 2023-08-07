# Uses python3

import sys
import queue


def distance(adj, start, target):
    # write your code here
    elements_bfs_tree_depth = [-1] * len(adj)
    bfs_queue = queue.Queue(maxsize=len(adj))
    bfs_queue.put(start)
    elements_bfs_tree_depth[start] = 0
    while bfs_queue.empty() is not True:
        cur_check = bfs_queue.get()
        for element in adj[cur_check]:
            if element == target:
                return elements_bfs_tree_depth[cur_check] + 1
            elif elements_bfs_tree_depth[element] != -1:
                continue
            bfs_queue.put(element)
            elements_bfs_tree_depth[element] = elements_bfs_tree_depth[cur_check] + 1
    return -1


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
