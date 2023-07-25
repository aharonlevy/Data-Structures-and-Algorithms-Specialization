#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class TreeNode:
    def __init__(self, key, left=-1, right=-1):
        self.key = key
        self.left = left
        self.right = right


def IsBinarySearchTree(tree):
    def inOrder_iterative(tree, root):
        def in_order_traversal(tree, current, result, hashmap):
            stack = []
            while stack or current != -1:
                if current != -1:
                    if tree[current].key in hashmap:
                        return result[:-1]

                    # Add the key to the hashmap in a pre-order manner
                    hashmap[tree[current].key] = True

                    stack.append(current)
                    current = tree[current].left
                else:
                    if not stack:
                        break

                    current = stack.pop()
                    # Remove the key from the hashmap after adding it to the result array
                    del hashmap[tree[current].key]

                    result.append(tree[current].key)
                    current = tree[current].right

            return result

        hashmap = {}
        return in_order_traversal(tree, root, [], hashmap)

    if len(tree) <= 1:
        return True
    tree_as_in_order_array = inOrder_iterative(tree, 0)
    if len(tree_as_in_order_array) < len(tree):
        return False
    prev_element = tree_as_in_order_array[0]
    for element in tree_as_in_order_array[1:]:
        if element < prev_element:
            return False
        prev_element = element
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        key, left, right = map(int, sys.stdin.readline().strip().split())
        tree.append(TreeNode(key, left, right))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
