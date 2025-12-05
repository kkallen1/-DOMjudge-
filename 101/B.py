d = []
while True:
    tmp = list(input().upper().strip().split())
    if tmp and tmp[0]=='EOF':
        break

    d += tmp

ans = {
    x: d.count(x)
    for x in set(d)
}
ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)

ans = [x[1] for x in ans]
print(*ans[:3:], sep=",")