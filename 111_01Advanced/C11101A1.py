a = list(int(x) for x in input().split())
b = list(int(x) for x in input().split())

ans = 0
for i, j in zip(a, b):
    ans += i*j

print(ans)