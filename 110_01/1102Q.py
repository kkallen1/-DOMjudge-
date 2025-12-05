n = int(input())
d = list(map(int, input().split()))

ans = 0
while len(d)>1:
    d.sort(reverse=True)
    b=d.pop()
    a=d.pop()

    tmp = a+b
    d.append(tmp)
    ans += tmp
print(ans)