from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

def largest_number_fast(numbers):
    '''
    return the largest number that can be made from the list of numbers
    we assume that there are only positive numbers in numbers
    '''
    numbers = list(map(int, numbers))  # Convert strings to integers
    largest = ""
    while len(numbers) > 0:
        max_number = numbers[0]
        for number in numbers[1:]:
            if is_better(number, max_number):
                max_number = number
        largest = largest + str(max_number)
        numbers.remove(max_number)
    return int(largest)

def is_better(num1, num2):
    '''
    returns true if putting the first number before the second number will make a bigger number
    '''
    combined1 = int(str(num1) + str(num2))
    combined2 = int(str(num2) + str(num1))
    return combined1 > combined2

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_fast(input_numbers))
