from math import isqrt

def f(n):
    if n in dp:
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
for i in range(n):
    a, b = map(int, input().split())

    if a>b:
        a, b= b,a
    
    if a%2==0:
        a+=1

    ans = []
    for i in range(a, b+1):
        if f(i):
            ans.append(i)
    
    print(*ans, sep="\n")
    if i+1 == n:
        break
    print()