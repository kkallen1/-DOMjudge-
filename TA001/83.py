from math import isqrt

def f(n):
    if n in dp or n==2:
        return True
    
    if n<2 or n%2==0:
        return False
    
    for i in range(3, isqrt(n)+1, 2):
        if n%i==0:
            return False
    
    dp.add(n)
    return True
dp = {2,3,5,7,11}

n = int(input())

ans = []
if n>=2 and n%2==0:
    ans = [2]
for i in range(3, n, 2):
    if n%i==0 and f(i):
        ans.append(i)

print(ans)