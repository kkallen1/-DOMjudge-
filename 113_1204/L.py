import itertools

n = int(input())
d=  list(range(1, n+1))
d = list(itertools.permutations(d, n))
d.sort(reverse=True)
for i in d:
    print(*i, sep="")