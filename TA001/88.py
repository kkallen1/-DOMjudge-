n = input()
ans =[]

tmp = set()
for i in n:
    if i not in tmp:
        ans.append(i)
        tmp.add(i)
print(*ans, sep="")

ans =[]
tmp = set()
for i in n[::-1]:
    if i not in tmp:
        ans.append(i)
        tmp.add(i)
print(*ans[::-1], sep="")