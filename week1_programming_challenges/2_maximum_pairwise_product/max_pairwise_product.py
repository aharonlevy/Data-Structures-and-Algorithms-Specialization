def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    biggest_num = -1
    second_biggest = -1
    if (n < 2):
        return max_product
    elif (numbers[0] >= numbers[1]):
        biggest_num = numbers[0]
        second_biggest = numbers [1]
    else:
        biggest_num = numbers[1]
        second_biggest = numbers [0]
    for index in range(2, n):
        if (numbers[index] >= biggest_num):
            second_biggest = biggest_num
            biggest_num = numbers[index]
        elif (numbers[index] > second_biggest):
            second_biggest = numbers[index]
    max_product = biggest_num * second_biggest
    return max_product


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
