from math import isqrt

d= list(map(int, input().split()))

L = isqrt(len(d))

D = [[0]*(L) for _ in range(L)]

idx = 0
for i in range(L):
    for j in range(L):
        D[i][j] = d[idx]
        idx+=1

flag = 1
for i in range(L):
    for j in range(L):
        if D[i][j] != D[j][i]:
            flag = 0
        
    if not flag:
        break

if flag:
    print(True)
else:
    print(False)