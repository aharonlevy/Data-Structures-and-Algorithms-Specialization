"""
Shortest Sequence of Operations

This script computes the shortest sequence of operations to transform a number into 1.

Usage:
    python shortest_sequence.py
"""


def compute_operations(n):
    """
    Compute the shortest sequence of operations to transform a number into 1.

    Args:
        n (int): The target number.

    Returns:
        list: A list containing the shortest sequence of numbers that transform
              the input number into 1. The sequence starts with the input number
              and ends with 1.
    """
    int_array = [0] * (n + 1)
    int_array[0] = 0
    return_array = []
    patrol = 1
    while patrol <= n:
        smallest_iterations = int_array[patrol - 1] + 1
        if patrol % 2 == 0 and smallest_iterations > (int_array[patrol // 2] + 1):
            smallest_iterations = int_array[patrol // 2] + 1
        if patrol % 3 == 0 and smallest_iterations > (int_array[patrol // 3] + 1):
            smallest_iterations = int_array[patrol // 3] + 1
        int_array[patrol] = smallest_iterations
        patrol += 1
    # we made an array that have the shortest way to the n first numbers,
    #  now we can use it to find the shortest way to 1
    patrol -= 1
    while patrol > 0:
        return_array.append(patrol)
        cur_iterations = int_array[patrol]
        if patrol % 3 == 0 and cur_iterations > (int_array[patrol // 3]):
            patrol = patrol // 3
        elif patrol % 2 == 0 and cur_iterations > (int_array[patrol // 2]):
            patrol = patrol // 2
        else:
            patrol -= 1

    int_array = return_array[::-1]
    return int_array


if __name__ == "__main__":
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
