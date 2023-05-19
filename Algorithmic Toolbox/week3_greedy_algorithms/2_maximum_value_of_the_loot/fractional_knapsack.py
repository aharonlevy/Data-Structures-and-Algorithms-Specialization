'''
Maximizing the Value of the Loot Problem
Find the maximal value of items that fit into the
backpack
'''
from sys import stdin


def optimal_value(capacity, weights, values):
    '''
    The maximum total
    value of fractions of items that fit
    into the backpack of the given capacity: i.
    '''
    value = 0.
    # create a list the weight value tuples
    items_by_weight_value = []
    for weight, val in zip(weights, values):
        items_by_weight_value.append([weight, val])
    cur_capacity = capacity
    # sort the list so it'll be from highest to lowest weight/value rates
    while cur_capacity > 0 and len(items_by_weight_value) > 0:
        hights_rate= -1
        target = [0, 0]
        changed = False
        for weight_value in items_by_weight_value:
            rate = weight_value[1] / weight_value[0]
            if hights_rate < rate:
                hights_rate = rate
                target = weight_value
                changed = True
        if cur_capacity >= target[0]:
            cur_capacity -= target[0]
            value += target[1]
            if changed is True:
                items_by_weight_value.remove(target)
        else:
            # this is the last thing we take we can take 'rate * cur_capacity'
            value = value + (hights_rate * cur_capacity)
            cur_capacity = 0
        if value < 0:
            print("empty List!")
            return 0
    return value

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    OPT_VALUE = optimal_value(capacity, weights, values)
    print(f"{OPT_VALUE:.10f}")
