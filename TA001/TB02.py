import sys

for l in sys.stdin:
    d=  list(map(int, l.strip().split(', ')))
    d.sort(reverse=True)
    print(d)