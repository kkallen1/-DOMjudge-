from collections import deque
from math import isqrt

for _ in range(int(input())):
    n = int(input())
    
    Count = {}
    if n%2==0:
        Count[2] = 0
        while n%2==0:
            Count[2] += 1
            n//=2

    for i in range(3, isqrt(n)+1, 2):
        if n%i == 0:
            Count[i] = 0
            while n%i==0:
                Count[i] += 1
                n//=i

    if n>1:
        Count[n] = 1

    tmp = 1
    for i in Count.values():
        tmp *= (i+1)
    
    prime = len(list(Count.keys()))
    
    print(tmp - len(Count))