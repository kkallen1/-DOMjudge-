from collections import Counter

n = int(input())
d = list(map(int, input().split()))
d = Counter(d)

d= sorted(d.items(), key=lambda x: (x[0]))

for i in d:
    print(*i)