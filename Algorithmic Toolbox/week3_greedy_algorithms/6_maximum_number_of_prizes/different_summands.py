def optimal_summands(n):
    summands = []
    # write your code here
    cur_prize = 1
    remaining = n
    while cur_prize <= remaining:
        summands.append(cur_prize)
        remaining -= cur_prize
        cur_prize += 1
    summands[-1] += remaining
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
