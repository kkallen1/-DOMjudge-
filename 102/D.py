import itertools
from math import gcd

for _ in range(int(input())):
    n, i, j = map(int, input().split(', '))
    i-=1
    j-=1

    data = list(itertools.permutations(str(n), len(str(n))))

    for x in range(len(data)):
        data[x] = int("".join(data[x]))
    
    ans = gcd(data[i], data[j])
    print(ans)