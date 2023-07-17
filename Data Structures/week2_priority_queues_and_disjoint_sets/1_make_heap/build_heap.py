# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def build_heap_fast(data):
    swaps = []
    index = (len(data) - 2) // 2
    while index >= 0:
        min_child = -1
        left_child = (index * 2) + 1
        right_child = left_child + 1
        if right_child >= len(data):
            min_child = left_child
        else:
            min_child = min(left_child, right_child, key=lambda idx: data[idx])
        cur_add = sift_down(data, index, min_child)
        for element in cur_add:
            swaps.append(element)
        index -= 1
    return swaps


def sift_down(data, index, min_child):
    swaps_to_add = []
    while index < len(data):
        if data[index] > data[min_child]:
            swaps_to_add.append([index, min_child])
            data[index], data[min_child] = data[min_child], data[index]
            index = min_child
        else:
            break
        left_child = (index * 2) + 1
        right_child = left_child + 1
        if right_child >= len(data):
            if left_child >= len(data):
                break
            min_child = left_child
        else:
            min_child = min(left_child, right_child, key=lambda idx: data[idx])

    return swaps_to_add


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap_fast(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

    # test
    # data = [5, 4, 3, 2, 1]

    # swaps = build_heap_fast(data)

    # print(len(swaps))
    # for i, j in swaps:
    #     print(i, j)


if __name__ == "__main__":
    main()
