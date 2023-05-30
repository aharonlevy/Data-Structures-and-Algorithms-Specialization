"""
Module Name: QuickSort with Three-Way Partition

This module provides functions to perform QuickSort on an array using a three-way partition.

"""

from random import randint


def partition3(array, left, right):
    """
    Partition an array into three parts based on a chosen pivot element.

    Args:
        array (list): The array to be partitioned.
        left (int): The left index of the partition range.
        right (int): The right index of the partition range.

    Returns:
        tuple: Two integers representing the indices of the partitioned range.

    """
    pivot = array[left]
    left_rightmost = left
    right_leftmost = left + 1
    patrol = left + 1
    while patrol <= right:
        check = array[patrol]
        if pivot > check:
            left_rightmost += 1
            array[left_rightmost], array[patrol] = array[patrol], array[left_rightmost]
            if left_rightmost == right_leftmost:
                right_leftmost += 1
                patrol += 1
                continue
            array[right_leftmost], array[patrol] = array[patrol], array[right_leftmost]
            right_leftmost += 1
        elif pivot == check:
            array[right_leftmost], array[patrol] = array[patrol], array[right_leftmost]
            right_leftmost += 1
        patrol += 1
    array[left], array[left_rightmost] = array[left_rightmost], array[left]
    return left_rightmost, right_leftmost - 1


def randomized_quick_sort(array, left, right):
    """sort the array smallest to biggest"""
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == "__main__":
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)

    # manual test
    # regular case:

    # elements = [
    #     5,
    #     2,
    #     8,
    #     3,
    #     1,
    #     9,
    #     4,
    #     6,
    #     7,
    #     2,
    #     8,
    #     5,
    #     3,
    #     1,
    #     7,
    #     9,
    #     6,
    #     4,
    #     2,
    #     5,
    #     8,
    #     3,
    #     1,
    #     9,
    #     4,
    #     6,
    #     7,
    #     2,
    #     8,
    #     5,
    #     3,
    #     1,
    #     7,
    #     9,
    #     6,
    #     4,
    #     2,
    #     5,
    #     8,
    #     3,
    #     1,
    # ]
    # # target = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # randomized_quick_sort(elements, 0, len(elements) - 1)
    # print("# elements: ", *elements)
    # # print("# target: ", *target)
