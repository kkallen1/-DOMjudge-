import sys

for l in sys.stdin:
    a,b = map(int, l.strip().split())
    print(2*a*b)