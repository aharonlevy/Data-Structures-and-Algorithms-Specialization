import random
def fibonacci_sum(n):
    '''
    default function
    '''
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def fibonacci_sum_fast(n):
    '''
    Function will return the mudolu 10 sum of the n first fibonacci numbers
    '''
    if n <= 1:
        return n
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
    return _sum % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_fast(n))

    # stress test
    # IS_VALID = True
    # while IS_VALID is True:
    #     n = random.randint(0, 100000)
    #     fast_result = fibonacci_sum_fast(n)
    #     naive_result = fibonacci_sum(n)
    #     if fast_result != naive_result:
    #         IS_VALID = False
    #         print ("Error! for n: ", n, "fast got: ", fast_result, " naive got: ", naive_result)
    #         break
    #     print("all good")
