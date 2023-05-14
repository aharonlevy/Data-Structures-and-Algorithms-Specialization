
def lcm(a, b):
    gcd = my_gcd(a,b)
    return int((a * b) / gcd)

def my_gcd(a, b, cur = -1):
    if cur == -1:
        cur = 1
    if b == 0 or a == 0:
        return cur
    if a == 0:
        return 1
    big = max(a,b)
    small = min(a,b)
    return my_gcd(small, big % small, small)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
