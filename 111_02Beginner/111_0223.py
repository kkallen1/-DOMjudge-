a = list(x for x in input())

ans = [chr(x) for x in range(65, 90+1)]
for i in set(a):
    if ord(i) <= 72:
        if a.count(i)==2:
            ans.remove(i)
    else:
        if a.count(i)==3:
            ans.remove(i)

if ans:
    ans.sort()
    print(*ans, sep="")
else:
    print('*')