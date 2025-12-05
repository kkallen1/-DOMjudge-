from math import isqrt

while True:
    n = int(input())
    tmp = n

    if n==0:
        break

    ans = 0
    if n%2==0:
        ans += 1
        while n%2==0:
            n//=2

    for i in range(3, isqrt(n)+1, 2):
        if n%i==0:
            ans += 1
            while n%i==0:
                n//=i
    
    if n!=1:
        ans+=1
    
    print(f"{tmp} : {ans}")