from math import isqrt

n = int(input())

if n%3!=0 and n%5!=0:
    ans = set()
    for i in range(1, isqrt(n)+1):
        if n%i==0 and i not in ans:
            ans.add(i)
            ans.add(n//i)
    
    if len(ans)>=5:
        print(1)
    else:
        print(0)
else:
    print(0)