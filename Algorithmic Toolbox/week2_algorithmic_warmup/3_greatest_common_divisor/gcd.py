def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

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

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(my_gcd(a, b))
