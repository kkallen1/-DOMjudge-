from collections import Counter

n = int(input())
d = list(map(int, input().split()))

d = Counter(d)
d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
kk = d[0][1]

for i in d:
    if i[1]!=kk:
        break
    print(*i)