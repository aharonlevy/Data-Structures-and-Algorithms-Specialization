from itertools import combinations


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def inversions_fast(sequence):
    """
    Returns the number of inversions in the sequence.
    """

    def special_merge_sort(sequence, inversions):
        return_sequence = []
        if len(sequence) <= 1:
            return_sequence = sequence.copy()
            return return_sequence, inversions
        left_sequence, inversions = special_merge_sort(
            sequence[0 : len(sequence) // 2], inversions
        )
        right_sequence, inversions = special_merge_sort(
            sequence[len(sequence) // 2 :], inversions=inversions
        )
        left_patrol = 0
        right_patrol = 0
        while left_patrol < len(left_sequence) and right_patrol < len(right_sequence):
            if right_sequence[right_patrol] < left_sequence[left_patrol]:
                # right element is smaller than left element
                return_sequence.append(right_sequence[right_patrol])
                inversions += len(left_sequence) - left_patrol
                right_patrol += 1
            else:
                # right element is greater than or equal to left element
                return_sequence.append(left_sequence[left_patrol])
                left_patrol += 1
        # take care of remaining elements in the arrays
        if left_patrol < len(left_sequence):
            # add the remaining elements
            return_sequence.extend(left_sequence[left_patrol:])
        if right_patrol < len(right_sequence):
            # add the remaining elements
            return_sequence.extend(right_sequence[right_patrol:])
        return return_sequence, inversions

    inversions = 0
    _, return_inversions = special_merge_sort(sequence=sequence, inversions=inversions)
    return return_inversions


if __name__ == "__main__":
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_fast(elements))
