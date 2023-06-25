# python3
import sys


class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.__cur_max_stack = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__cur_max_stack) == 0:
            self.__cur_max_stack.append(a)
        elif a >= self.__cur_max_stack[len(self.__cur_max_stack) - 1]:
            self.__cur_max_stack.append(a)
        else:
            self.__cur_max_stack.append(
                self.__cur_max_stack[len(self.__cur_max_stack) - 1]
            )

    def Pop(self):
        assert len(self.__stack)
        self.__stack.pop()
        self.__cur_max_stack.pop()

    def Max(self):
        cur_max = self.__cur_max_stack.pop()
        self.__cur_max_stack.append(cur_max)
        return cur_max


if __name__ == "__main__":
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert 0
