def max_pairwise_product(numbers):
    '''Return the max product of the numbers from the numbers list'''
    n = len(numbers)
    max_product = 0
    biggest_num = -1
    second_biggest = -1
    assert n >= 2, "List must have at least 2 elements"

    biggest_num = max(numbers[0], numbers[1])
    second_biggest = min(numbers[0], numbers[1])
    for _ in range(2, n):
        biggest_num = max(numbers)
        numbers.remove(biggest_num)
        second_biggest = max(numbers)

    max_product = biggest_num * second_biggest
    return max_product

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
