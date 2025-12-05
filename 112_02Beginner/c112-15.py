import itertools

d = list(map(int, input().split(',')))

d = list(itertools.combinations(d, 3))
d = {sum(x) for x in d}
print(len(d))