"""
Change Calculation

This script calculates the minimum number of coins needed to
 make change for a given amount of money.

Usage:
    python change_calculation.py

Author:
    Aharon

Date:
    [Current Date]

"""


def change(money):
    """
    Calculate the minimum number of coins needed to make change for a given amount of money.

    Args:
        money (int): The amount of money for which to calculate the change.

    Returns:
        int: The minimum number of coins needed to make change for the given amount of money.
    """
    change_array = [0] * (money + 1)
    change_array[0] = 0
    patrol = 1
    while patrol <= money:
        smallest_change = change_array[patrol - 1] + 1
        if patrol >= 3 and smallest_change > change_array[patrol - 3] + 1:
            smallest_change = change_array[patrol - 3] + 1
        if patrol >= 4 and smallest_change > change_array[patrol - 4] + 1:
            smallest_change = change_array[patrol - 4] + 1
        change_array[patrol] = smallest_change
        patrol += 1
    return change_array[money]


if __name__ == "__main__":
    m = int(input())
    print(change(m))
