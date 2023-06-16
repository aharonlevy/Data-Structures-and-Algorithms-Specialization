from sys import stdin

"""
this script solve the knapsack 
"""


def maximum_gold(capacity, weights):
    """
    Returns the max value of subset from weights that
    we can fit in a bag that can contain 'capacity' a max.
    """
    # crate a capacity + 1 by weights + 1 matrix so that 1st row and column contain only zeros
    optimal_sums = [[[0, False]] * (capacity + 1) for _ in range(len(weights) + 1)]
    # iterate row by row finding optimal subset of current available weights update in matrix
    row = 1
    cul = 1
    while row <= len(weights):
        while cul <= capacity:
            cur_best = optimal_sums[row][cul - 1]
            if cur_best[0] < optimal_sums[row - 1][cul][0]:
                cur_best = [optimal_sums[row - 1][cul][0], False]
            if weights[row - 1] <= cul:
                cur_weight = weights[row - 1]
                if (
                    cur_best[0]
                    < optimal_sums[row][cul - cur_weight][0] + weights[row - 1]
                ) and optimal_sums[row][cul - cur_weight][1] is False:
                    optimal_sums[row][cul] = [
                        optimal_sums[row][cul - cur_weight][0] + weights[row - 1],
                        True,
                    ]
                else:
                    optimal_sums[row][cul] = cur_best
            else:
                optimal_sums[row][cul] = cur_best
            cul += 1
        cul = 1
        row += 1
    # return the matrix[capacity - 1][weights - 1] because this is the optimal sum
    return optimal_sums[len(weights)][capacity][0]


if __name__ == "__main__":
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n
    print(maximum_gold(input_capacity, input_weights))

    # manual tests
    # capacity = 10
    # weights = [1, 4, 8]
    # print(maximum_gold(capacity, weights))
