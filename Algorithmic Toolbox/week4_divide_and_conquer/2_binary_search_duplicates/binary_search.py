"""this doc implement binary search when the elements in the array are not unique  """
# import random


def binary_search(keys, query):
    "return the first occurrence of 'query' in the array; or -1 if not there"
    left = 0
    right = len(keys) - 1
    found_index = -1
    mid = 0
    # find index for an occurrence of 'query'
    while left <= right:
        mid = (left + right) // 2
        check = keys[mid]
        if check == query:
            found_index = mid
            break
        elif check < query:
            # query might be to the right
            left = mid + 1
        else:
            # query might be to the left
            right = mid - 1
    if found_index == -1:
        # query is not in the array
        return found_index
    # we found an occurrence of 'query' now every right-end need to be of number 'query'
    left = 0
    right = found_index
    while left < right:
        mid = (left + right) // 2
        check = keys[mid]
        if check == query:
            # first occurrence might be to the left
            right = mid
        elif check < query:
            # first occurrence might be to the right
            left = mid + 1
    if keys[right - 1] == query and right > 0:
        return right - 1
    return right


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

    # numbers are at the start or end
    # target at the start
    # keys = list(range(random.randint(10, 15)))
    # multi_show = random.randint(0, 4)
    # query = 0
    # for number in range(multi_show):
    #     keys[query + number] = query
    # while query > len(keys) - 1:
    #     query = random.randint(1, 400)
    # result = binary_search(keys, query)
    # if result != query:
    #     print("# num at start failed, got: ", result, "target was: ", query)
    #     print(keys)
    # else:
    #     print("success! result: ", result)

    # target number is lsat number
    # keys = list(range(random.randint(10, 15)))
    # multi_show = random.randint(0, 4)
    # query = len(keys) - 1
    # result = binary_search(keys, query)
    # if result != query:
    #     print("# num at start failed, got: ", result, "target was: ", query)
    #     print(keys)
    # else:
    #     print("success! result: ", result)

    # single number in all of the array
    # keys = list(range(random.randint(10, 15)))
    # query = 0
    # for index in keys:
    #     keys[index] = query
    # result = binary_search(keys, query)
    # if result != query:
    #     print("# num at start failed, got: ", result, "target was: ", query)
    #     print(keys)
    # else:
    #     print("success! result: ", result)

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
    #     keys = list(range(random.randint(10, 15)))
    #     multi_show = random.randint(0, 4)
    #     query = random.randint(1, 6)
    #     for number in range(multi_show):
    #         keys[query + number] = query
    #     while query > len(keys) - 1:
    #         query = random.randint(1, 400)
    #     result = binary_search(keys, query)
    #     if result != query:
    #         print("# test failed, got: ", result, "target was: ", query)
    #         print(keys)
    #         break
    #     else:
    #         print("success! result: ", result)
