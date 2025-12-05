d = list(map(int, input().split(',')))
d.remove(max(d))
d.remove(max(d))
d.remove(min(d))
d.remove(min(d))

print(sum(d) // len(d))