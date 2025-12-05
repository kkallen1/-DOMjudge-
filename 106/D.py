import itertools

for _ in range(int(input())):
    a, b, c = map(int, input().split(','))

    a = str(a)
    b-=1
    c-=1
    a = list(itertools.permutations(a, len(a)))

    i = list(''.join(a[b]))
    j = list(''.join(a[c]))

    c, d = i[:], j[:]

    A, B = 0, 0
    for x, y in zip(i, j):
        if x==y:
            A += 1
            c.remove(x)
            d.remove(y)
    
    for x in set(d):
        B += min(c.count(x), d.count(x))
    
    print(f"{A}A{B}B")