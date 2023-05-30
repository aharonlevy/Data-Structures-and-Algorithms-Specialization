"""implementation of binary search """
# import random


def binary_search(keys, query):
    """
    return the index number that holds query as his value or -1"""
    left = 0
    right = len(keys) - 1
    mid = right // 2
    if not query:
        return -1
    while left <= right:
        current_check = keys[mid]
        if current_check == query:
            return mid
        if query > current_check:
            # query > current_check so it'll be to the right
            left = mid + 1
        else:
            # query < current_check so it'll be to the left
            right = mid - 1
        mid = (right + left) // 2
    return -1


if __name__ == "__main__":
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=" ")

    # test cases for binary_search
    # empty cases
    # keys = []
    # query = 5
    # empty = ""
    # if binary_search(keys, query) != -1:
    #     print("failed empty array test")
    # else:
    #     print("success empty array test!")
    # if binary_search(keys, empty) != -1:
    #     print("failed empty query test")
    # else:
    #     print("success empty query test!")

    # element not in array stress test
    # while True:
    #     keys = range(random.randint(6, 500))
    #     query = 700

    #     result = binary_search(keys, query)
    #     if result != -1:
    #         print("# test failed, got: ", result)
    #         break
    #     print("success! result: ", result)

    # stress test
    # while True:
    #     keys = range(random.randint(6, 500))
    #     query = random.randint(1, 400)
    #     while query > len(keys) - 1:
    #         query = random.randint(1, 400)
    #     result = binary_search(keys, query)
    #     if result != query:
    #         print("# test failed, got: ", result)
    #         break
    #     else:
    #         print("success! result: ", result)
