data = list(x for x in input().split())
tmp = list(x for x in input())

data.sort()
ans = []
for i in tmp:
    if i=='A':
        ans.append(data[0])
    elif i=='B':
        ans.append(data[1])
    else:
        ans.append(data[2])
print(*ans)