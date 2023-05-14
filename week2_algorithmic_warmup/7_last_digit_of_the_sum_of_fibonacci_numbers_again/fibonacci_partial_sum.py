import random

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10

def fibonacci_sum_fast(n):
    '''
    Function will return the sum of the n first fibonacci numbers
    '''
    if n == 1 :
        return n
    if n <= 0:
        return 0
    # crate a list contaning every number in the pisano period
    previous = 0
    current = 1
    mask = 0
    pisano_list = []
    pisano_list.append(previous)
    pisano_list.append(current)
    while True:
        mask = previous
        previous = current
        current = (previous + mask) % 10
        if (current == 1 and previous == 0):
            break
        else:
            pisano_list.append(current)
    pisano_list.pop()
    pisano_list_sum = sum(pisano_list)
    # iterate through the list for n + 1 [we started at the 0 number]
    _sum = 0
    list_length = len(pisano_list)
    whole_list_iterations = n // list_length
    _sum = whole_list_iterations * pisano_list_sum
    for index in range(1, n % list_length + 1):
        index = index % list_length
        _sum += pisano_list[index]
    return _sum

def fibonacci_partial_sum_fast(start, stop):
    '''
    Returns the first number of the sum of the fibonacci numberst from 'from_' and to 'n'. 
    '''
    if stop <= 1:
        return stop - start
    # get the sum of the n fibonacci numbers
    total_sum = fibonacci_sum_fast(stop)
    total_sum -= fibonacci_sum_fast(start - 1)
    return total_sum % 10

if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_fast(from_, to))

    # manual test
    # while from_ >= 0 and to >= 0:
    #     from_, to = map(int, input().split())
    #     fibo_fast = fibonacci_partial_sum_fast(from_, to)
    #     print("# fast: ", fibo_fast)
    #     fibo_naive = fibonacci_partial_sum_naive(from_, to)
    #     print("# naive: ", fibo_naive)
    #     if fibo_fast != fibo_naive:
    #         print("error! fast got: ", fibo_fast, " and naive got: ", fibo_naive)
    #         from_ = -1
    #     print("good! what next?")

    # stress test
    # while from_ >= 0 and to >= 0:
    #     from_, to = random.randint(0, 15000), random.randint(0, 150000)
    #     while from_ > to:
    #         from_, to = random.randint(0, 15000), random.randint(0, 15000000)
    #     fibo_fast = fibonacci_partial_sum_fast(from_, to)
    #     print("# fast: ", fibo_fast)
    #     fibo_naive = fibonacci_partial_sum_naive(from_, to)
    #     print("# naive: ", fibo_naive)
    #     if fibo_fast != fibo_naive:
    #         print("error! fast got: ", fibo_fast, " and naive got: ", fibo_naive)
    #         print("# start: ", from_, " to: ", to)
    #         from_ = -1
    #     print("good!")
