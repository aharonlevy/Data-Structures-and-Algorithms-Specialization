# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def compute_height_fast(n, parents):
    if len(parents) <= 1:
        return len(parents)
    hash_array = [[] for _ in range(len(parents))]
    root = -1
    for index, parent in enumerate(parents):
        if parent == -1:
            root = index
        else:
            hash_array[parent].append(index)
    memo = [0] * len(parents)
    return get_max_height(hash_array, root, memo)


def get_max_height(hash_array, root_index, memo):
    if not hash_array[root_index]:
        return 1
    if memo[root_index] != 0:
        return memo[root_index]
    max_height = 0
    for child in hash_array[root_index]:
        height = 1 + get_max_height(hash_array, child, memo)
        max_height = max(max_height, height)
    memo[root_index] = max_height
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height_fast(n, parents))

    # manual tests

    # empty case

    # n = 0
    # parents = []
    # if compute_height_fast(n, parents=parents) != 0:
    #     print("# empty case failed")
    # else:
    #     print("# empty case passed")

    # # hight 1
    # n = 1
    # parents = [-1]
    # if compute_height_fast(n, parents=parents) != 1:
    #     print("# hight 1 test failed")
    # else:
    #     print("# hight 1 test passed")
    # # hight 2
    # n = 5
    # parents = [3, 3, 3, -1, 3]
    # if compute_height_fast(n, parents=parents) != 2:
    #     print("# hight 2 test failed")
    #     print("# got: ", compute_height_fast(n, parents=parents), " when expected 2")
    # else:
    #     print("# hight 2 test passed")
    #     # hight 2 simple
    #     n = 2
    # parents = [-1, 0]
    # if compute_height_fast(n, parents=parents) != 2:
    #     print("# hight 2 test failed")
    #     print("# got: ", compute_height_fast(n, parents=parents), " when expected 2")
    # else:
    #     print("# hight 2 simple test passed")

    #     # case: hight 4
    #     n = 5
    # parents = [1, 2, 3, -1, 3]
    # if compute_height_fast(n, parents=parents) != 4:
    #     print("# hight 4 test failed")
    #     print("# got: ", compute_height_fast(n, parents=parents), " when expected 4")
    # else:
    #     print("# hight 4 test passed")


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
threading.Thread(target=main).start()
