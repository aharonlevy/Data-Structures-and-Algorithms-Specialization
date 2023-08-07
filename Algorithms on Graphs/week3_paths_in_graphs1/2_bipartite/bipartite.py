# Uses python3

import sys
import queue


def bipartite(adj):
    # write your code here
    elements_bfs_tree_depth = [-1] * len(adj)

    def bfs(adj, start, elements_bfs_tree_depth):
        bfs_queue = queue.Queue(maxsize=len(adj))
        bfs_queue.put(start)
        elements_bfs_tree_depth[start] = 0
        while bfs_queue.empty() is not True:
            cur_check = bfs_queue.get()
            cur_color = elements_bfs_tree_depth[cur_check]
            for element in adj[cur_check]:
                if elements_bfs_tree_depth[element] != -1:
                    if elements_bfs_tree_depth[element] == cur_color:
                        return -1
                    continue
                bfs_queue.put(element)
                elements_bfs_tree_depth[element] = (cur_color + 1) % 2
        return 1

    for index in range(len(adj)):
        if elements_bfs_tree_depth[index] == -1:
            if bfs(adj, index, elements_bfs_tree_depth) == -1:
                return 0
    return 1


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
    print(bipartite(adj))
