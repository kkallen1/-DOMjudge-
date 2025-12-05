m,n,p,q = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(m)]
B = [list(map(int, input().split())) for _ in range(p)]

ans = [[0]*(n*q) for _ in range(m*p)]
for i in range(m):
    for j in range(n):
        for x in range(p):
            for y in range(q):
                ans[i*p+x][j*q+y] += A[i][j] * B[x][y]

for i in ans:
    print(*i)