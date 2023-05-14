def fibonacci_number(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fiboList = [0] * n
    fiboList[1] = 1
    fiboList[0] = 1
    for index in range(2, n):
        fiboList[index] = fiboList[index-1] + fiboList[index-2]
    return fiboList[n-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
