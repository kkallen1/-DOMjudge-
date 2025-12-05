n = int(input())
coins = list(map(int, input().split()))

ans = {0}
for i in coins:
    tmp = set()
    for j in ans:
        tmp.add(j+i)
    ans |= tmp
ans =list(ans)
ans.sort()
print(len(ans)-1)
print(*ans[1::])