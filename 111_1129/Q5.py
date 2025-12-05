a = [x for x in input().split()]

tmp = len(a)
ans = [a[0], a[1]]
for i in range(2, tmp):
    if i in [tmp-2, tmp-1]:
        ans.append(a[i])
    else:
        ans.append(len(a[i]) * '*')
print(*ans)