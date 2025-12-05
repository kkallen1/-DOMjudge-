from math import isqrt

for _ in range(int(input())):
    n = int(input())

    ans = 0
    for a in range(isqrt(n)+1):
        a2 = a*a
        for b in range(a, isqrt(n)+1):
            b2 = b*b
            c2 = n-a2-b2
            
            if c2<0:
                break

            c = isqrt(c2)
            if c*c==c2:
                ans = (a,b,c)
                break
        if ans:
            break
    
    if ans:
        print(*ans)
    else:
        print(-1)