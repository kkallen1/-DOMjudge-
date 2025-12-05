a = list(map(str, input()))
b = input()

ans = []
for i in a:
    if i not in b:
        ans.append(i)
print(*ans, sep="")