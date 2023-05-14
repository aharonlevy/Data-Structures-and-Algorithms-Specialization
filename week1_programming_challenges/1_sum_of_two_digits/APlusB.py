'''
this app will print the sum of 2 
numbers that the user will write in
'''

def sum_of_two_digits(first_digit, second_digit):
    '''
    Function will return the sum two given numbers
    '''
    return first_digit + second_digit


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))
