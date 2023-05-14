def fibonacci_sum_squares(n):
    '''
    trivial given function
    '''
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current * current

    return _sum % 10

def fibonacci_sum_squares_fast(n):
    '''
    Returns the first number from the sum of n fibonacci numbers squared
    '''
    # The only number that can that can change the first numbers,
    #  even when squared is the first number.
    # We'll use the same method but this time store up the squared numbers
    if n == 1 :
        return n
    if n <= 0:
        return 0
    # crate a list containing every number in the pisano period of % 10
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
            pisano_list.append(current ** 2)
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
    return _sum % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_fast(n))

    # manual test
    # while n >= 0 :
    #     n = int(input())
    #     fibo_fast = fibonacci_sum_squares_fast(n)
    #     print("# fast: ", fibo_fast)
    #     fibo_naive = fibonacci_sum_squares(n)
    #     print("# naive: ", fibo_naive)
    #     if fibo_fast != fibo_naive:
    #         print("error! fast got: ", fibo_fast, " and naive got: ", fibo_naive)
    #         n = -1
    #     print("good! what next?")

    # stress test
    # while n >= 0 :
    #     n = int(input())
    #     fibo_fast = fibonacci_sum_squares_fast(n)
    #     print("# fast: ", fibo_fast)
    #     fibo_naive = fibonacci_sum_squares(n)
    #     print("# naive: ", fibo_naive)
    #     if fibo_fast != fibo_naive:
    #         print("error! fast got: ", fibo_fast, " and naive got: ", fibo_naive)
    #         print("# n is: ", n)
    #         from_ = -1
    #     print("good!")

