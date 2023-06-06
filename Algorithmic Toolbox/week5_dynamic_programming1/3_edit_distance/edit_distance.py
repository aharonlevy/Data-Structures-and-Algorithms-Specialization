"""
This script calculates the minimum edit distance between two strings.
"""


def edit_distance(first_string, second_string):
    """
    Calculate the minimum edit distance between two strings.

    Args:
        first_string (str): The first input string.
        second_string (str): The second input string.

    Returns:
        int: The minimum edit distance between the two input strings.
    """
    if len(first_string) < 1 or len(second_string) < 1:
        # one of them is empty so the sum will be the length of the other
        return len(second_string) + len(first_string)

    first_patrol = len(first_string)
    second_patrol = len(second_string)
    editing_array = [
        [float("inf")] * (len(second_string) + 1) for _ in range(len(first_string) + 1)
    ]
    # initialize the array to the cases when we try to compare an empty string with some string
    while first_patrol >= 0:
        editing_array[first_patrol][second_patrol] = len(first_string) - first_patrol
        first_patrol -= 1

    while second_patrol >= 0:
        editing_array[len(first_string)][second_patrol] = (
            len(second_string) - second_patrol
        )
        second_patrol -= 1

    # start filling the array from the bottom up
    first_patrol = len(first_string) - 1
    second_patrol = len(second_string) - 1
    while first_patrol >= 0:
        cur_first_char = first_string[first_patrol]
        while second_patrol >= 0:
            cur_second_char = second_string[second_patrol]
            min_score = min(
                editing_array[first_patrol + 1][second_patrol + 1],
                editing_array[first_patrol + 1][second_patrol],
                editing_array[first_patrol][second_patrol + 1],
            )
            if cur_first_char == cur_second_char:
                # we have a metching chars so we alrady know the best path from here on out
                editing_array[first_patrol][second_patrol] = editing_array[
                    first_patrol + 1
                ][second_patrol + 1]
            else:
                # we need to check what is the best way from here on out.
                # we have it saved on min_score
                editing_array[first_patrol][second_patrol] = min_score + 1
            second_patrol -= 1
        second_patrol = len(second_string) - 1
        first_patrol -= 1
    return editing_array[0][0]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # manual tests
    # print(edit_distance("ab", "ab")) res 0
    # print(edit_distance("short", "ports")) res 3
    # print(edit_distance("00", "020")) res 1
