import sys

for l in sys.stdin:
    a,b,c,d= map(int, l.strip().split())

    print(56*a+24*b+14*c+6*d)