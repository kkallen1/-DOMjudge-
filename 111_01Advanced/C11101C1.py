from math import isqrt
import itertools
from collections import deque

def f(n):
    if n in dp:
        return True
    
    if n<2:
        return False
    
    if n==2:
        return True

    if n%2==0:
        return False
    
    for i in range(3, isqrt(n)+1, 2):
        if n%i==0:
            return False
    
    dp.append(n)
    return True

dp = deque([2, 3, 5, 7, 11, 13, 17])
while True:
    a = int(input())

    if a==0:
        break

    ans = 0
    for i in range(1, a//2+1):
        if f(i) and f(a-i):
            ans += 1

    print(ans)