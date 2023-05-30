"""finds a majority element in tan array using a divide & conquer method"""
import random


def majority_element_naive(elements):
    """return 1 if the provided array have the same element in at least half of it
    this is the naive and inefficient solution"""
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1
    return 0


def majority_element_fast(elements):
    """return 1 if the provided array have the same element in at least half of it
    this is the naive and inefficient solution"""

    # sort array so all the same elements will be next to each other
    sorted_elements = sorted(elements)

    # find mid element, this will be the element we need to check
    # find first occurrence of mid_element
    def find_first_occurrence(arr, target):
        left = 0
        right = len(arr) - 1
        first_index = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                first_index = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return first_index

    half_len = len(sorted_elements) // 2
    middle = sorted_elements[half_len]
    first_index = find_first_occurrence(sorted_elements, middle)
    if first_index + half_len > len(elements) - 1:
        return 0
    if sorted_elements[first_index] == sorted_elements[first_index + half_len]:
        return 1
    return 0


if __name__ == "__main__":
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_fast(input_elements))

    # test cases:
    # stress tests
    # have a majority in array
    # while True:
    #     elements = list(range(random.randint(10, 15)))
    #     multi_show = random.randint(4, 5)
    #     query = random.randint(0, 3)
    #     for number in range(multi_show):
    #         elements[query + number] = query
    #     naive = majority_element_naive(elements)
    #     fast = majority_element_fast(elements)
    #     if fast != naive:
    #         print("# test failed! naive: ", naive, " fast: ", fast)
    #         print("# ", elements)
    #         break
    #     print("# we made it!")
