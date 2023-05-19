'''
Compute the minimum number of coins needed
to change the given value into coins with denominations 1, 5, and 10.
'''
def change(money):
    '''
    Return the minimum number of coins with denominations 1, 5,
10 that changes money.
    '''
    return (money // 10) + ((money % 10) // 5) + (money % 5)


if __name__ == '__main__':
    m = int(input())
    print(change(m))

    # manual test
    # print("manual test for change(15):")
    # print("#", change(15) == 2)
    # print("manual test for change(0):")
    # print("#", change(0) == 0)
    # print("manual test for change(13):")
    # print("#", change(13) == 4)
    # print("manual test for change(8):")
    # print("#", change(8) == 4)
