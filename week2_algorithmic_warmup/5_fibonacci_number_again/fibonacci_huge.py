import random

def fibonacci_huge_naive(n, m):
    ''' naive solution'''
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def fibonacci_huge(n, m):
    '''my solution'''
   # make the pisano period as a list
    previous = 0
    current = 1
    mask = 0
    pisano_list = []
    pisano_list.append(previous)
    pisano_list.append(current)
    while True:
        mask = previous
        previous = current
        current = (previous + mask) % m
        if (current == 1 and previous == 0):
            break
        else:
            pisano_list.append(current)
    pisano_list.pop()
   # find the pisano period index related to the n-th number
    index_in_pisano_array = n % len(pisano_list)
    return pisano_list[index_in_pisano_array]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
