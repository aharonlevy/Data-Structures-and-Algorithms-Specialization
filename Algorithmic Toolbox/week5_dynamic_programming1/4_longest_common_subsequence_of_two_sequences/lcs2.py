def lcs2(first_sequence, second_sequence):
    if len(first_sequence) < 1 or len(second_sequence) < 1:
        # one of them is empty so we have max subsequence of length 0
        return 0

    first_patrol = len(first_sequence) - 1
    second_patrol = len(second_sequence) - 1
    editing_array = [
        [0] * (len(second_sequence) + 1) for _ in range(len(first_sequence) + 1)
    ]

    # start filling the array from the bottom up
    first_patrol = len(first_sequence) - 1
    second_patrol = len(second_sequence) - 1
    while first_patrol >= 0:
        while second_patrol >= 0:
            if first_sequence[first_patrol] == second_sequence[second_patrol]:
                # we have a matching chars so we already know the best path from here on out
                editing_array[first_patrol][second_patrol] = (
                    editing_array[first_patrol + 1][second_patrol + 1] + 1
                )
            else:
                # we need to check what is the best way from here on out.
                # we have it saved on min_score
                editing_array[first_patrol][second_patrol] = max(
                    editing_array[first_patrol + 1][second_patrol],
                    editing_array[first_patrol][second_patrol + 1],
                )
            second_patrol -= 1
        second_patrol = len(second_sequence) - 1
        first_patrol -= 1
    return editing_array[0][0]


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
