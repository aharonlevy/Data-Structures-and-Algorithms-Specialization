'''
problem 4 in this week work
'''
from itertools import permutations
import random


def max_dot_product(first_sequence, second_sequence):
    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product

def max_dot_product_fast(first_sequence, second_sequence):
    '''
    returns the biggest sum of products from element
    from first_sequence with element from second_sequence
    '''
    max_product = 0
    first_sequence.sort()
    second_sequence.sort()
    for f_element, sec_element in zip(first_sequence, second_sequence):
        max_product += f_element * sec_element
    return max_product

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product_fast(prices, clicks))

    # # manual test used
    # manual_first_sequence = [1, 3, 5]
    # manual_second_sequence = [2, 4, 1]
    # fast_result = max_dot_product_fast(manual_first_sequence, manual_second_sequence)
    # slow_result = max_dot_product(manual_first_sequence, manual_second_sequence)
    # if  fast_result != slow_result:
    #     print("error: fast got: ", fast_result, " expected: ", slow_result)

    # manual_first_sequence = [15, 20, 10]
    # manual_second_sequence = [2, 4, 1]
    # fast_result = max_dot_product_fast(manual_first_sequence, manual_second_sequence) 
    # slow_result = max_dot_product(manual_first_sequence, manual_second_sequence)
    # if  fast_result != slow_result:
    #     print("# error in manual: fast got: ", fast_result, " expected: ", slow_result)

    # # stress test used
    # is_valid = True
    # while is_valid is True:
    #     test_count = 1
    #     sequence_len = random.randint(1, 10)
    #     stress_first_sequence = []
    #     stress_second_sequence = []
    #     for _ in range(random.randint(1, 10)):
    #         stress_first_sequence.append(random.randint(1,200))
    #         stress_second_sequence.append(random.randint(1,200))   
    #     fast_result = max_dot_product_fast(manual_first_sequence, manual_second_sequence)
    #     slow_result = max_dot_product(manual_first_sequence, manual_second_sequence)
    #     if fast_result != slow_result:
    #         is_valid = False
    #         print("# error in stress: fast got: ", fast_result, " expected: ", slow_result)
    #         break
    #     print("# test ", test_count, " went well")
    #     test_count += 1
