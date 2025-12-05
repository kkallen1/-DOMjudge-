n = int(input())
d=  list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i):
        if d[j] > d[i]:
            ans += 1
print(ans)