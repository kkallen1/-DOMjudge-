a, b = map(str, input().split())

a = list(x for x in a)
b = list(x for x in b)

ans = 0
for i in b:
    if i in a:
        ans += 1

print(ans)