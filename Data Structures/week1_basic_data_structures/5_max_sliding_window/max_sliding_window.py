# python3
from collections import deque

"""
Sliding Window Maximum

Finds the maximum element in sliding windows of a given size in a sequence.

Functions:
    max_sliding_window_naive(sequence, m): Naive approach for finding max element in each window.
    max_sliding_window_fast(sequence, m): Optimized approach using a deque for finding max element.

Usage:
    - Define input sequence as a list of integers.
    - Set window size.
    - Call `max_sliding_window_fast(sequence, m)`.
    - Returns list with max element in each sliding window.

Example:
    input_sequence = [0, 0, 0, 0, 3, 4, 5]
    window_size = 3
    print(*max_sliding_window_fast(input_sequence, window_size))
"""


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i : i + m]))

    return maximums


def max_sliding_window_fast(sequence, m):
    """
    Finds the maximum element in each sliding window of size m in the given sequence.

    Args:
        sequence (list): The input sequence of integers.
        m (int): The size of the sliding window.

    Returns:
        list: A list containing the maximum element in each sliding window.

    """
    values_deque = deque()
    maximums = []
    counter = 0
    for index in range(m):
        # don't add numbers to the maximums
        value = sequence[index]
        if len(values_deque) == 0:
            values_deque.append(value)
            counter += 1
            continue
        while len(values_deque) > 0 and value > values_deque[-1]:
            values_deque.pop()
        values_deque.append(value)
        counter += 1
    # put first value of first window to maximums
    maximums.append(values_deque[0])
    # take care of every new value and the window slide
    for index in range(m, len(sequence)):
        new_value = sequence[index]
        old_value = sequence[index - m]
        if old_value == values_deque[0]:
            values_deque.popleft()
        while len(values_deque) > 0 and new_value > values_deque[-1]:
            values_deque.pop()
        values_deque.append(new_value)
        maximums.append(values_deque[0])
    return maximums


if __name__ == "__main__":
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    print(*max_sliding_window_fast(input_sequence, window_size))

    # tests
    # input_sequence, window_size = [0, 0, 0, 0, 3, 4, 5], 3
    # print(*max_sliding_window_fast(input_sequence, window_size))
