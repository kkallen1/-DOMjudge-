m,n,n,p = map(int, input().split())
A = tuple(tuple(map(int, input().split())) for _ in range(m))
B = tuple(tuple(map(int, input().split())) for _ in range(n))

ans = [[0]*(p) for _ in range(m)]
for i in range(m):
    for j in range(p):
        for k in range(n):
            ans[i][j] += A[i][k] * B[k][j]

for i in ans:
    print(*i)