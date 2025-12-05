from math import gcd

for _ in range(int(input())):
    d = list(map(int, input().split(',')))

    ans = 0

    for i in range(len(d)):
        for j in range(i):
            ans = max(ans, gcd(d[i], d[j]))
    
    print(ans)