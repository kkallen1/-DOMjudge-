from math import gcd

for _ in range(int(input())):
    d=  list(map(int, input().split(',')))

    now = max(d)
    for i in d:
        now = gcd(now, i)
    print(now)