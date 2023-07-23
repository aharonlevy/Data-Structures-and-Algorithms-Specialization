import sys, threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**27)


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0] * self.n
        self.left = [0] * self.n
        self.right = [0] * self.n
        for i in range(self.n):
            a, b, c = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        return self.inOrder_iterative(0)

    def inOrder_iterative(self, root):
        result = []
        stack = []
        current = root
        while stack or current != -1:
            if current != -1:
                stack.append(current)
                current = self.left[current]
            else:
                current = stack.pop()
                result.append(self.key[current])
                current = self.right[current]
        return result

    def preOrder(self):
        return self.preOrder_iterative(0)

    def preOrder_iterative(self, root):
        result = []
        stack = [root]
        while stack:
            current = stack.pop()
            if current != -1:
                result.append(self.key[current])
                stack.append(self.right[current])
                stack.append(self.left[current])
        return result

    def postOrder(self):
        return self.postOrder_iterative(0)

    def postOrder_iterative(self, root):
        result = []
        stack1 = [root]
        stack2 = []
        while stack1:
            current = stack1.pop()
            if current != -1:
                stack2.append(self.key[current])
                stack1.append(self.left[current])
                stack1.append(self.right[current])
        while stack2:
            result.append(stack2.pop())
        return result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
