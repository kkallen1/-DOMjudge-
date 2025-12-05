ans = {}
for _ in range(int(input())):
    a = list(x for x in input().split())

    a = a.pop(0)
    if a in ans:
        ans[a] += 1
    else:
        ans[a] = 1

ans = sorted(ans.items(), key=lambda x:x[0])
for i in ans:
    print(*i)  