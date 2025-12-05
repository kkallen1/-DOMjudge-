# m, n, n, p
m,n = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(m)]

n,p = map(int, input().split())
B = [[int(x) for x in input().split()] for _ in range(n)]

tmp = [[0]*p for _ in range(m)]
for i in range(m):
    for j in range(p):
        for k in range(n):
            tmp[i][j] += A[i][k] * B[k][j]

ans = "["

for i in tmp[:-1:]:
    ans += '['
    for j in i[:-1:]:
        ans += f"{j},"
    ans += str(i[-1])
    ans += '],'

ans += '['
for i in tmp[-1][:-1:]:
    ans += f"{i},"
ans += str(tmp[-1][-1])
ans += ']'

ans += ']'
print(ans)