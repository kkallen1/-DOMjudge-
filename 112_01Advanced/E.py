from collections import Counter

n = int(input())
d = list(map(int, input().split()))

d = Counter(d)
d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
k = d[0][1]

ans = [x[0] for x in d if x[1]==k]
print(*ans)