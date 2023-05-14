def fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def fibonacci_last_digit_my_work(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fiboList = [0] * n
    fiboList[1] = 1
    fiboList[0] = 1
    for index in range(2, n):
        fiboList[index] = (fiboList[index-1] + fiboList[index-2]) % 10
    return fiboList[n-1]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit_my_work(n))
